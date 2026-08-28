---
title: Onboard robot service architecture
type: concept
created: 2026-08-27
updated: 2026-08-27
sources: 2
tags: [embedded-systems, systems-architecture, ota-updates, ipc, recovery-path, consumer-robotics, rust, systemd, robot-software, reliability]
---

**Onboard robot service architecture** is the question of how the software on a shipped robot is split into processes, how those processes talk, which of them are allowed to fail, and how a new version reaches the machine without bricking it. It is the layer *below* everything else this wiki tracks — beneath the policy, beneath [ROS 2](../../entities/ros2.md), beneath the framework — and it is the layer that decides whether a robot in someone's home stays reachable when the interesting part breaks.

> [!note] One ingested instance
> This page is built almost entirely from [`pollen-robotics/microduck`](../../sources/microduck-runtime-repo.md), which is the only shipped consumer-robot runtime in this wiki whose design documents are public. Treat the patterns below as *one team's worked answer*, well-argued and not yet corroborated, rather than as established practice.

## Why it is a distinct problem from robot middleware

The wiki's software coverage is dominated by **middleware and frameworks** — [ROS 2](../../entities/ros2.md) topics, [LeRobot](../../entities/lerobot.md)'s device abstraction, the various bridges. Those answer *how do components exchange data*. They do not answer:

- What still works when the control loop won't start?
- Who is allowed to write to a motor, and what enforces it?
- How does version N+1 get onto a robot you cannot physically reach, and what happens when it is worse than version N?
- Which failures should roll back a release, and which are just facts about the board?

A research robot answers these with "SSH in and fix it." A robot in a stranger's living room cannot.

## The patterns

### 1. Split by what must survive, not by what is related

The intuitive split is functional — perception here, control there. The load-bearing split is **by failure domain**: which services constitute the recovery path, and therefore must not depend on the thing most likely to be broken.

In Microduck, `configd` (wifi, identity, pairing), `updaterd` (install, swap, roll back) and `btd` (BLE transport) have **no systemd dependency on the control daemon**, no ML runtime and no media stack, because *"a robot whose control loop will not start is exactly the robot someone needs to reconfigure, update, or roll back."* Config lives in `configd` rather than the control daemon for exactly this reason — *"provisioning wifi is exactly what someone needs when the robot is broken."*

The corollary is that a **transport must own no state**. If provisioning lived inside the Bluetooth daemon, everything else would depend on Bluetooth, and an SDK would absurdly have to go through BLE.

### 2. Make the dangerous state unrepresentable, not merely checked

The strongest form of a safety boundary is one the type system enforces. Microduck's `safety` module owns the **only** write handle to the motor bus, so *"nothing above it can command a motor — the invariant is structural rather than remembered."*

The stated reasoning generalises to any recovery or safety code in any language:

> "Code that only runs once something has already gone wrong is the code most likely to be quietly broken, so **make the broken state unrepresentable instead**."

Same argument reappears in transport choice: a unix socket is preferred over localhost TCP partly because *"binding `0.0.0.0` by typo, by config, or by a 'make it work from my laptop' patch would expose firmware update control to the network. Over a unix socket that mistake is **unrepresentable**."*

### 3. The safety layer should judge as little as possible

A counter-intuitive one, and the sharpest idea in the source. Microduck's safety layer enforces only **non-finite refusal**, **actuator-range clamping** and a **command deadman**. Its fall detector runs every tick and **gates nothing** — a fallen robot accepts every command an upright one does.

Earlier revisions *did* put fall-limp and auto-recovery in the safety layer, and both were removed:

> "A safety rule that recovery has to bypass in order to work is not one."

The generalisation: **anything the robot needs in order to recover must live above the safety layer, not inside it.** A safety layer with exemptions has stopped being a boundary. See [safety filters](safety-filters.md) for the academic instances, all of which assume the filter is the arbiter rather than a floor.

### 4. Features, not frames

Control loops need *derived* facts ("ball at (x,y)", "person detected") at tens of bytes and 10–30 Hz, not pixels. Microduck's rule — *"put perception next to the sensor"* — keeps the camera, inference and feature extraction in one service that publishes results, because shipping 640×480 RGB at 30 fps (~27 MB/s) across a process boundary *"would waste most of the board's memory bandwidth."*

The consumption rule matters as much as the production rule: the control loop **subscribes once and reads a locally cached latest snapshot**, non-blocking, last-value-wins. *"A stalled perception service then degrades perception rather than adding jitter to motor control."*

### 5. Swap releases atomically, gate on health, roll back automatically

The shape: a release is a whole directory; installation verifies a signature, moves a symlink, restarts units, **then asks the robot whether it is healthy** and reinstates the previous release if not. A crash-loop that survives that is caught by a boot counter.

The rule that makes it survivable: *"everything outside `releases/<ver>/` survives both an update and a rollback,"* which is why per-board configuration is never shipped inside a release.

And the discipline about **what may reach the verdict**: *"only what a release can be blamed for."* Battery level and motor temperature are reported, never judged — *"a release must never be rolled back for the state of the board it landed on."*

### 6. Build the updater first

> "`updaterd` is built **first**, then used to ship every subsequent iteration of the rest of this architecture. This front-loads update-system risk while failures are still free (no clients, nothing valuable to break) and means the update path is exercised **hundreds of times** before a robot ships."

With the necessary caveat, which is the part teams skip: *"keep a manual recovery path (SSH / reflash) throughout early development. The updater is both unproven and rapidly changing, and **it ships inside the artifact it updates**."*

### 7. Observability is a contract, because you cannot attach a debugger

*"A robot in someone's home cannot be debugged by attaching a debugger. What support can ask for has to already be on the robot."* Three rules that follow:

- **Every service logs its own identity first**, including the path it was launched from — *"the difference between 'the update worked' and 'the symlink moved but systemd is still running the old path'."*
- **Log volume is a retention decision.** A per-tick line at info would be ~86k entries a day from an idle robot, and *"under a journal size cap those entries are what **evict** the logs an incident needs."*
- **Update history gets different durability from logs** — `fsync`ed JSONL outside the journal, so *"what did this robot install, and what happened"* survives a wiped or volatile journal, *"which is the realistic support case, not the ideal one."*

### 8. Different consumers deserve different transports over one API

One API definition, thin adapters: BLE for provisioning (a subset — physical presence implies authorization), a unix socket for local tooling and any on-board SDK, WebRTC for human telepresence, and — the non-obvious one — a plain **WebSocket** for LLM-driven control, because *"an agent doesn't want a 30 fps H.264 track to decode — it wants a frame every second or two plus a state blob."*

Which lands on the right control split regardless of transport: *"LLM latency (hundreds of ms to seconds) means the agent is a **high-level** controller… Reactive control stays local."* Compare [LLM agent architecture](../agents/llm-agent-architecture.md) and [control abstraction levels](control-abstraction-levels.md).

## Related concepts

- [Safety filters for learned policies](safety-filters.md) — the academic treatment; this page's §3 argues against making the filter the arbiter.
- [Runtime failure detection](runtime-failure-detection.md) — is *this rollout* failing; §5 here is is *this release* failing.
- [Robot security](robot-security.md) — the socket-permissions and signing-custody arguments overlap directly.
- [Control abstraction levels](control-abstraction-levels.md) — what an intent is, versus a motor write.

## Current state

Single-source and therefore provisional. What would strengthen it: the equivalent documents from any other shipped consumer robot. Nothing comparable is public for [Reachy Mini](../../entities/reachy-mini.md) (10,000+ units, same company), and the closed humanoid vendors publish nothing at this layer at all. The [ROS 2](../../entities/ros2.md) ecosystem has conventions for the middleware question and essentially none for the *"what survives a broken robot"* question, which is the gap this page names.

## Mentioned in

- [`pollen-robotics/microduck` — the onboard runtime](../../sources/microduck-runtime-repo.md)
