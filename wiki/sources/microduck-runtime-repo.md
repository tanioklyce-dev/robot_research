---
title: "pollen-robotics/microduck — the onboard runtime and its design docs"
type: source
url: https://github.com/pollen-robotics/microduck/tree/main
author: Pollen Robotics (design docs signed "pierre"; runtime lineage from apirrone/microduck_runtime)
published: 2026-08-27
ingested: 2026-08-27
venue: GitHub
license: Apache-2.0
format: Rust workspace — 19 crates, 131 .rs files, 25 design/project/robot docs (~10,700 lines of prose)
tags: [microduck, pollen-robotics, hugging-face, embedded-systems, rust, systems-architecture, ota-updates, robot-safety, fall-detection, onnx, rknn, npu, rk3566, dynamixel, webrtc, control-loop, ipc]
---

# `pollen-robotics/microduck` — the onboard runtime

> [!note] Read as a design-document set, not a code drop
> The interesting artifact here is `docs/` — **~10,700 lines** across 25 files, of which `updater-design.md` alone is 1,467 lines and `robotd-design.md` is 956. They are written in the style that records *why the alternative was rejected*, with measured numbers attached. This page mostly quotes them. Snapshot at `590b986`.

## Summary

The onboard software for [Microduck](../entities/microduck.md): **seven daemons in Rust on a Rockchip RK3566**, talking JSON-RPC 2.0 over unix sockets, with a 50 Hz control loop that runs ONNX policies onto fifteen [Dynamixel](../entities/dynamixel.md) servos. Companion to the [product launch bundle](pollen-robotics-microduck.md); this is what actually runs on the robot.

Its value to this wiki is not that it drives a $399 duck. It is that the wiki has **almost no ingested material on how a shipped consumer robot's onboard software is structured** — everything else here is a policy, a framework, a benchmark, or a bridge. This is a complete, publicly readable answer to *what runs on the robot in someone's living room, and how does it not brick itself*. See [Onboard robot service architecture](../concepts/robotics/onboard-robot-service-architecture.md).

Design status is honest about itself: *"this describes where we're going for the **first shipped version**, not the current prototype (`microduck_runtime`, which is exploratory and will be rewritten)."*

## The service split

Seven daemons, one board, one unix socket each ([`architecture.md`](https://github.com/pollen-robotics/microduck/blob/main/docs/design/architecture.md)):

| service | owns | reaches |
|---|---|---|
| `robotd` | motor control, kinematics, odometry, policies, sensing, **safety**, `robot.health` | the Dynamixel bus |
| `configd` | wifi, robot identity/name, pairing PIN, gamepad bonding, reboot | BlueZ + NetworkManager over D-Bus |
| `updaterd` | releases: verify, install, swap, health-gate, roll back | GitHub releases, `systemctl`, `robotd` |
| `btd` | **nothing** — BLE transport for a subset of the API | `robotd`, `configd`, `updaterd` |
| `padd` | **nothing** — gamepad transport | `robotd` |
| `mediad` | camera/audio pipeline, perception, WebRTC; the remote gateway | `robotd`, `configd`, `updaterd` |
| `tofd` | the head's 8×8 depth matrix — publishes frames, reads nobody | the HAT's I²C bus |

Three organising rules, each with a stated reason rather than a convention:

- **`robotd` is the only thing that touches the robot.** Clients send *intents* — "go this fast," "look there," "stand up." Nothing else in the system can command a motor.
- **`configd`, `updaterd` and `btd` survive a dead `robotd`.** No systemd dependency on it, no ML runtime, no media stack, because *"a robot whose control loop will not start is exactly the robot someone needs to reconfigure, update, or roll back."* Config lives in `configd` specifically because *"provisioning wifi is exactly what someone needs when the robot is broken, so putting config in `robotd` would make it unreachable in the one case that matters."*
- **`btd`, `padd` and `mediad` own nothing.** They are transports over one shared API definition, *"all three exercised daily, so the API an app will use cannot quietly rot."*

## The 50 Hz tick

From [`robotd-design.md`](https://github.com/pollen-robotics/microduck/blob/main/docs/design/robotd-design.md) §1.4 — two bus transactions per tick, plus a third once a second:

```
read()    one sync_read  · IMU board + 15 servos · registers 124–136
decide    observation → policy → targets → clamp
write()   one sync_write · goal positions
publish   atomics always; a state frame only if someone subscribed
every 1s  slow_sensors() · registers 144–146 · voltage + temperature
```

Details worth having:

- **`MissedTickBehavior::Skip`.** `Burst` *"fires the backlog back to back and stacks motor commands on top of each other."* `Delay` is wrong less obviously — it reschedules at *now + period* after each tick, *"so every wakeup latency is added to the period instead of being absorbed, and the loop drifts slower than its own configured rate."*
- **Not real-time, on purpose.** A plain `tokio` task on its own runtime so IPC cannot sit in front of it. *"Moving perception out to `mediad` removed most of what competed with the loop for free."*
- **`driving` has four load-bearing conditions**: enabled ∧ policy loaded ∧ **sensors this tick** ∧ ¬limp-fall. The third is the non-obvious one — *"a read that failed leaves nothing to build an observation from, and inventing one would feed the policy a robot that does not exist."*
- **Edges matter more than states.** On starting to drive, `controller.reset()`, *"else a stale last action, or a filter anchored to where the robot was a minute ago, shows up as a lurch."* On stopping, the hold pose is captured **once** — *"re-reading each tick would sag under gravity."*

## The observation contract, resolved

The [previous ingest](pollen-robotics-microduck.md) left the 15-vs-14 motor count open. The code settles it:

> Every alpha policy is `obs[1,61] → actions[1,14]`. `[ gyro(3) | projected_gravity(3) | joint_pos(14) | joint_vel(14) | last_action(14) | command(13) ]`, command = `vel(3) + head(4) + body(6)`. *"Joints exclude the mouth throughout; actions map back into 15 motor slots with index 9 left at zero."*

So: **15 servos, 14 of them policy-driven, the beak commanded outside the policy.** Dynamixel IDs `20–24 / 30–34 / 10–14`. Nine ONNX files ship in `policies/`, ~794 KB each.

Three encoding traps the doc names because they are *"individually plausible and wrong"*:

1. **All-zero body is the nominal encoding, not a placeholder** — body x, y and yaw are hardcoded zero as "unbound in training."
2. **Head targets ride in the command and are not added on top of the policy output.** Doing both *"bends the head twice."*
3. **The body block is ordered `z, roll, pitch`** — *"swapping the last two tilts the robot sideways when asked to lean forward."*

And the sim-to-real coupling made concrete in a constant:

> `DEFAULT_POSITION` must match `HOME_FRAME` in the training env: *"a policy observes joint positions **relative** to the home pose, so a discrepancy here is a constant offset on 14 observation slots."*

## Safety: structural, and deliberately narrow

`safety` owns the only `RobotIo` write handle — *"the borrow checker is the enforcement."* The stated reason generalises well beyond Rust:

> "Code that only runs once something has already gone wrong is the code most likely to be quietly broken, so **make the broken state unrepresentable instead**."

What it actually enforces is small: **refuse non-finite** (a `NaN` target is refused, not clamped), **clamp to actuator range**, and a **deadman on the command** — and *"stop is not limp… losing comms makes the robot stand still, because standing is the safe state for a biped."*

> [!note] The fall verdict gates nothing, on purpose
> Fall detection runs every tick (projected gravity in the trunk frame, debounced 0.2 s) and is **published, not enforced**: *"a fallen robot is enabled, init'd, driven and sent skills exactly like an upright one."* Earlier revisions had a `fall_limp` gate and a `fall_recover` auto-stand-up in the safety layer and **both were removed** — *"because **a safety rule that recovery has to bypass in order to work is not one**."* Being on the floor is exactly when those calls need to work.

This is a sharper claim than anything in the wiki's [safety-filter](../concepts/robotics/safety-filters.md) coverage, which is all academic: the filter should be *structurally unbypassable* and *judgmentally minimal*. Everything the robot needs in order to *recover* lives above it.

## Predictive fall mitigation

The interesting control result. The position-based verdict is the wrong instrument for softening a landing — *"gravity past `fall_gravity_z` held for 200 ms **is** the robot on the floor, and the window worth acting in has closed by then."* So `limp_fall` runs a **second detector on the rate**:

> Projected gravity rotates with the trunk, so **ġ = −ω × g** is exact and comes straight from the gyro in the same 12-byte IMU block; extrapolating it over ~0.3 s says where gravity is heading. It fires when the robot is already tilted (**≈26°**), still tipping rather than recovering, and predicted past the fall threshold — debounced three ticks. *"Differentiating the SFLP quaternion instead would add the filter's lag to the one number whose whole value is being early."*

The payoff is not the landing:

> "What it buys is not the landing itself but **the stand-up after it**. The standing policy gets a still robot in a known posture up cleanly and a thrashing one up only after several attempts at walking gain against the floor, which is where the load on the motors comes from."

Sequence: limp at `gain_limp` following the joints down → wait for the gyro to go quiet → ramp to standing pose over ~1 s → hand back. The handover is nothing special: the twist was held at zero throughout, so command magnitude selects the standing network on its own.

> [!note] Asymmetric tuning, stated as such
> *"A false positive is a fall the robot **caused**, which is worse than the stiff landing it was trying to avoid. The defaults sit deliberately on the late side."* A rare instance of a shipped robot documenting which direction its detector is biased and why.

## The NPU, measured

The [last ingest](pollen-robotics-microduck.md) asked what the camera and ToF are for and whether an RK3566 can run anything. [`npu-bringup.md`](https://github.com/pollen-robotics/microduck/blob/main/docs/project/npu-bringup.md) answers with numbers.

**0.8 TOPS INT8, one core.** Model: `yolo11n` at 320×320, one class (a duck), **150 frames from three sessions**, mAP50 **0.976** held out, **3.9 MB** after INT8 quantisation.

| | measured |
|---|---|
| driver / runtime | 0.9.8 / 2.3.2 |
| latency p50 / p95 | **25.7 ms / 58.4 ms** (infer + decode) |
| CPU per frame | 20.7 ms |
| SoC temp | 63 °C at the end of a paced run |

Two caveats the doc raises against its own numbers — the kind most vendor benchmarks omit:

- **The CPU figure is not the NPU's cost**, and *"the way it is reported invites reading it as one"*: it includes a 1280×720 → 320×320 CPU resample that is not in the latency column at all. *"Before anyone quotes that as the price of perception, the two should be measured apart."*
- **The quantised model's scores are on their own scale** — *"the float model's 0.5 is not this model's 0.5 — so a run that detects nothing is more likely a threshold than a broken conversion."*

Also a hardware gotcha with a wide blast radius: **Armbian ships `npu@fde40000` as `status = "disabled"` on every Radxa Zero 3**, so a stock board *"has the hardware, the kernel and the driver and still no NPU."* The fix ships as a `preinstall` hook so *"a board provisioned before the NPU existed is fixed by an update rather than by somebody remembering a command."*

## Updates: swap, health-gate, roll back

> "Releases are swapped, not patched. A build lands as a whole directory under `/opt/robot/daemon/releases/<version>/`; `updaterd` verifies its signature, moves the `current` symlink, restarts the units, and **then asks `robotd` whether it is healthy**. If not, it puts the old release back on its own. A crash-loop that gets past that is caught by a boot counter."

The rule that makes it work: *"everything outside `releases/<ver>/` survives both an update and a rollback. That is the whole rule, and it is why per-board config is not shipped in the release."*

**Build order is the design decision most worth stealing:**

> "`updaterd` is built **first**, then used to ship every subsequent iteration of the rest of this architecture. This front-loads update-system risk while failures are still free (no clients, nothing valuable to break) and means the update path is exercised **hundreds of times** before a robot ships."

With the discipline that goes with it: *"Keep a manual recovery path (SSH / reflash) throughout early development. The updater is both unproven and rapidly changing, and **it ships inside the artifact it updates** — do not make it the only way back."*

And a diagnostic subtlety: after every update the running `updaterd` legitimately lags the installed release for a few seconds, because it cannot restart itself mid-update. *"Any tool reporting one version number is therefore wrong for that window, and wrong in the direction that makes a working robot look broken."* `robotctl version` reports both and names which skew it is, because *"`updaterd` behind the installed release"* and *"`robotd` behind it"* are different diagnoses.

## Transport choices, with the alternatives priced

JSON-RPC 2.0 / NDJSON over unix sockets. The doc tabulates nine alternatives with dependency counts (`jsonrpsee-server` is excluded outright — *"cannot serve a unix socket"*), then argues on failure modes rather than deps:

- **Filesystem permissions are free authorization** — mode 0660 plus a dedicated group; a TCP port is reachable by every process on the box.
- **`SO_PEERCRED` in two layers**: the socket's group decides who may *talk*; `allow_uids`/`allow_gids` decide who may *change the robot*, on mutating calls only. Read-only calls are ungated *"because support must be able to inspect a robot it is not authorised to change."*
- **The weighted-heaviest reason**: *"binding `0.0.0.0` by typo, by config, or by a 'make it work from my laptop' patch would expose **firmware update control** to the network. Over a unix socket that mistake is **unrepresentable**."*

And the data-plane rule: **features, not frames.** *"`robotd` does not need camera frames — it needs derived features… Shipping frames to `robotd` so it can run its own vision would waste most of the board's memory bandwidth."* `robotd` subscribes once and reads a cached latest snapshot, so *"a stalled `mediad` degrades perception rather than adding jitter to motor control."*

One more that generalises past robots — on serving LLM-driven control ([`architecture.md`](https://github.com/pollen-robotics/microduck/blob/main/docs/design/architecture.md) §5.3):

> "For an LLM-driven controller, WebRTC is the *harder* path. An agent doesn't want a 30 fps H.264 track to decode — it wants a frame every second or two plus a state blob." So agents get a **WebSocket** with `get_frame` → JPEG on demand. *"Open a WebSocket, poll a frame, send intents — a few dozen lines, no media stack."*

With the split stated correctly: *"LLM latency (hundreds of ms to seconds) means the agent is a **high-level** controller… Reactive control stays local in `robotd`. This is the correct split regardless of transport."*

## What is not built

The [roadmap](https://github.com/pollen-robotics/microduck/blob/main/docs/project/roadmap.md) is candid about the gap between the shipping robot and the advertised one:

- **M8 — policies from the Hub: not built.** Today *"every policy ships inside the daemon artifact… so a new gait needs a daemon release."* The engine already resolves `huggingface.co/{repo}/resolve/{revision}/{file}` and verifies *"**our own** minisign signature, because HF signs nothing for us."* Missing at both ends: `robotd` **has no SIGHUP handler and no way to swap an `ort` session under a running 50 Hz loop**, nothing publishes a bundle, and *"who may publish a policy a robot will run is a new custody question."*
- **M9 — the autonomous brain: not started.** *"The biggest untracked gap: the runtime's `autonomous.rs` exists nowhere in the daemon and no design doc owns it."* The prototype had a **16-state machine** (Chill, LookAround, Wander, TurnInPlace, Zoomies, Startle, Stretch, Ruffle, Preen, Sneeze, Dance, GroundPick, Nap, BallPlay, Petted, Held) on an energy/mood model with novelty-grid exploration memory and ToF obstacle avoidance. Done when *"a duck left alone in a room does something worth watching for ten minutes."*
- **Nothing on the robot can get a camera frame yet.** `mediad` has a raw NV12 tee branch *"that exists precisely for this… but no IPC exposes it, which is also why capturing a dataset has to stop `mediad` to take the camera."*
- **Explicitly not doing**: A/B image updates, OS/kernel OTA, fleet dashboards/telemetry, delta updates, staged rollouts, peripheral firmware OTA.

## Multi-robot, which turns out to exist

The [last ingest](pollen-robotics-microduck.md) flagged that nothing shipped lets the ducks perceive each other. Partly wrong — the substrate is built, the brain that would use it is not:

- **`ChoraleBeacon`** — nearby ducks by **stable id**, surviving BLE address rotation (*"never key on the address"*).
- **A shared beat with no clock sync** — **±20 ms across ducks**.
- **RSSI per advertisement** as free coarse distance; **~245 spare bytes** of extended-advertising payload.
- Planned fusion, stated cleanly: *"vision cannot tell identical ducks apart — **camera = direction, ToF = distance, BLE beacon = identity + presence**."*

Behaviour ideas filed *"roughly by charm-per-line"*: recognition and greeting with a persisted met-list, Marco Polo, follow-the-leader, a message that hops duck to duck through the spare payload and mutates, and voting where *"majority picks the group's next behavior."* Plus a design instinct worth recording: *"the chorale ends up as a **spontaneous event, not a command**… a surprise duet is a delight, a jukebox is not."*

## Entities mentioned

- [Microduck](../entities/microduck.md) · [Pollen Robotics](../entities/pollen-robotics.md) · [Hugging Face](../entities/hugging-face.md) · [Dynamixel](../entities/dynamixel.md)

## Concepts touched

- [Onboard robot service architecture](../concepts/robotics/onboard-robot-service-architecture.md)
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md)
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — `DEFAULT_POSITION` ↔ `HOME_FRAME`
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — limp-fall as reset preparation

## Open questions

- **Does the 50 Hz loop hold its rate on a loaded board?** The health summary reports *"the achieved tick rate as a percentage of target"* every five minutes, and the doc concedes *"a loop running at 60% of target is alive and passing its health check."* No measured tick-rate distribution is published anywhere in the repo. For a robot whose policies were **trained at 50 Hz**, that is the number that decides whether sim-to-real holds in the field.
- **Is `Skip` right when the loop is chronically late rather than occasionally?** Dropping ticks keeps the schedule but silently lowers the effective control rate the policy was trained against. No stated threshold at which degraded rate should become an unhealthy verdict — and §3.4's rule that only *"what a release can be blamed for"* may reach the verdict cuts against adding one.
- **The `ort` allocation note is unresolved**: *"the current path allocates a 61-float vector per inference… Worth measuring on the board before optimising."* Never measured in-repo.
- **How much of this is Claude-written?** [`autonomous_behavior.md`](https://github.com/pollen-robotics/microduck/blob/main/docs/ideas/autonomous_behavior.md) cites its governing "parity audit" as a `claude.ai/code/artifact/…` URL — an artifact nobody outside Pollen can open, load-bearing for the port it describes — and the sibling `microduck_rl` keeps its reward-design playbook in a `CLAUDE.md` *"also aimed at AI coding agents working in this repo."* Not a criticism of the output, which is unusually good; it is a **provenance gap in a public repo**, and the private-artifact citation is a broken reference by construction.
- **`microduck_rl` is described as "private"** in the M8 text while being publicly readable — decision #5 (*"decided 2026-08-26: publish this repository"*) landed a day before launch and the roadmap prose had not caught up. Minor, but a reminder that the dates in these docs run right up to the announcement.
