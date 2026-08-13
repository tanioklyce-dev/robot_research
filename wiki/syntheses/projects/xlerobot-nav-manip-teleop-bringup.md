---
title: XLeRobot — navigate, pick-and-place, teleoperate — sequenced bring-up plan
type: synthesis
created: 2026-08-13
updated: 2026-08-13
tags: [xlerobot, so-arm101, lerobot, act, smolvla, nav2, rtab-map, orin-nx, dgx-spark, rosetta, teleoperation, data-collection, projects]
---

# XLeRobot bring-up — nav, pick-and-place, teleop

**Starting state:** XLeRobot assembled and teleoperating. 2× [SO-ARM101](../../entities/so-arm101.md) (5 DoF + gripper), **2-wheel differential** base (non-holonomic), [Jetson Orin NX 16 GB](../../entities/jetson-orin-nano.md) onboard, [LeRobot](../../entities/lerobot.md)-native, [DGX Spark](../../entities/dgx-spark.md) available off-board.

**What this plan is:** the concrete execution of **steps 0–1 of the [fleet agentic framework](fleet-agentic-framework.md) build ladder** for the single XLeRobot — not a new framework. Step 0 is "record → HF → train on the Spark → async deploy"; step 1 is "add ROS 2 + a [Rosetta](../../entities/rosetta.md) contract, wrap Nav2 + the learned pick as skills." Everything below either de-risks or executes those two rungs.

> [!note] Good news first: navigation is the *least* risky leg, not the most
> The instinct is to treat SLAM as the hard part. On this platform it is the **solved** part. [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) (Correll lab, CU Boulder) ran **RealSense D435 + RTAB-Map in localization-only mode + [Nav2](../../entities/nav2.md)** on an *Orin Nano Super* — a strictly weaker board than your Orin NX 16 GB — inside a $1,202 XLeRobot build. There is a published, measured recipe for exactly your robot. The fleet framework page says the same thing from the other direction: *"Navigation — already Nav2 + SLAM; the framework adds nothing there."*
>
> **The hard part is manipulation data, and the hard part after that is making the two coexist on one serial bus.**

---

## 1. The real dependency structure

```
teleop (DONE) ──► demo collection ──► ACT (single task) ──► SmolVLA (multi-task)
                                              │                      │
                                              └──────► pick skill ◄──┘
                                                           │
   depth camera ──► RTAB-Map + Nav2 ──► navigate_to ────────┤
                                                           ▼
                                              nav-then-pick  ◄── ⚠ serial-bus conflict
```

Manipulation and navigation are **independent until they meet**, and where they meet there is a specific, known blocker (§4). Plan them in parallel; budget the integration separately rather than assuming it falls out.

---

## 2. Leg A — manipulation

### A1. Upgrade teleop from *driving* to *data collection*

Teleoperating works. Recording **usable demonstrations** is a different bar, and this is the step most likely to be quietly done badly.

What has to be true before you record 50 episodes you'll actually train on:

- **Fixed camera framing.** Both wrist views and the fixed view must not move between episodes. Policy learning is exquisitely sensitive here — [SmolVLA](../../entities/smolvla.md)'s pretraining pipeline needed explicit *camera-view normalization* across community datasets to be usable at all.
- **Episode boundary discipline** — start / save / discard as explicit operator actions. [DimOS](../../entities/dimos.md)'s collection loop is a good model: hold-to-engage, toggle-record, discard-in-progress. Cutting the Cord's VR teleop *"doubles as an imitation-learning data-collection pipeline"* for the same reason.
- **One task, one strategy.** The single most transferable lesson from [X-VLA](../../sources/xvla-paper.md)'s cloth-folding dataset: humans perform the same task *"in a wide variety of methods in a seemingly random manner,"* and different strategies are different behavioral modes that **entangle the policy**. Decompose the task into stages, do it the same way every time, and discard takes that drift.

> [!warning] Design your tasks around top-down grasps — this is a hard kinematic constraint, not a preference
> SO-101 is `shoulder_pan` (vertical yaw) + **three parallel pitch joints** + `wrist_roll` (about the tool axis). Consequence, derived in the [5-DoF analysis](five-dof-arms-in-robotwin.md):
> - **Top-down approach: fully general.** `wrist_roll` becomes world yaw when the tool points down, so any jaw orientation is reachable.
> - **Lateral approach: radial only.** The tool's yaw is slaved to the shoulder-pan angle. You **cannot** approach an object from a tangential direction.
>
> So: pick tasks with top-down grasps (bin picking, tabletop tidy, place-into-container) and avoid anything needing a sideways reach across the workspace (handover between arms at arbitrary orientation, opening a hinged door from the side). If a demo feels awkward to teleoperate, that is usually the kinematics telling you the policy will fail there too.

Two more scoping constraints from the platform: **reach ≈ 0.36 m from the cart edge**, and **vertical workspace 0.5–1.25 m with no lift**. Floor pickups are out. Counter and tabletop height is the operating envelope.

### A2. First policy: ACT, single task

**Target: ~50 demonstrations of one top-down task.** At a realistic 20–25 episodes/hour including resets and discards (X-VLA's measured rate), that is **2–3 hours of teleoperation**.

Train [ACT](../../entities/act.md) on the [Spark](../../entities/dgx-spark.md). Note the ARM64 gotcha the wiki already records: Spark needs its own torch wheels — `torch==2.11.0+cu130` from the cu130 index.

Why ACT before [SmolVLA](../../entities/smolvla.md), despite SmolVLA being better:

| Policy | Orin Nano latency (measured) | Rate |
|---|---:|---:|
| **ACT** | 36 ms | **27.8 Hz** |
| Diffusion Policy | 539.6 ms | 1.8 Hz |
| SmolVLA (450 M) | 713.8 ms | 1.4 Hz |

ACT is the only one of the three that runs **onboard at control rate**. Cutting the Cord's diagnosis of why is worth internalizing: *"the bottleneck on edge is the iterative action expert + denoising steps, not the VLM"* — so SmolVLA's slowness is inherent to flow matching at the edge and is **not** fixable by shrinking the language model.

**Stop condition (ladder step 0): a learned pick works on-robot.**

### A3. Second policy: SmolVLA off-board on the Spark

Once one task works, ACT's limits bite — it is single-task and does not generalize. SmolVLA is the upgrade, and it is the single strongest argument that your 5-DoF arm is *not* a second-class citizen:

- **Trained and validated on SO-100/SO-101** — your exact arm — at **78.3% real-world multi-task**, vs ACT single-task 48.3% and [π0](../../entities/pi-zero.md) 3.5 B multi-task 61.7%.
- **+26.6 pts** from community pretraining on an *out-of-distribution* SO-101 pick-and-place task (51.7 → 78.3). Your demos land on a base checkpoint that already understands this arm.
- Ships as `lerobot/smolvla_base`.

**Architecture: serve it from the Spark over LeRobot's async inference stack**, robot as client. Three reasons, in order of weight:
1. **It's the only way to run it fast.** 1.4 Hz onboard is unusable; the Spark is bandwidth-class comparable to Thor, and at 450 M rather than GR00T's 3 B it should sit far under the [~90–120 ms Spark estimate for GR00T](gr00t-spark-zmq-xlerobot.md).
2. **LeRobot's async client/server is built for this** — threshold-`g` queue management and an observation-similarity filter, designed to keep control responsive across a network hop.
3. **Power.** Keeping heavy inference off the robot leaves the 288 Wh pack running the Orin NX and motors only, preserving the stock multi-hour runtime rather than collapsing it.

---

## 3. Leg B — navigation

**Recipe, taken directly from [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md):** RGB-D camera → **RTAB-Map in localization-only mode** → **[Nav2](../../entities/nav2.md)**. Validated on a weaker board than yours, in a real XLeRobot build.

### The one prerequisite decision

**Do you have a depth camera on the robot?** XLeRobot ships RGB; the RealSense D415 is a +$220 option. Cutting the Cord used a **D435**. The wiki's [camera options analysis](xlerobot-camera-options-low-light.md) recommends the **D435i** over the stock D415 for low light and clutter — global shutter, wider FOV, onboard IMU — and flags that it needs a **mount tweak** because the housings differ (D435i 90×25×25 mm vs D415 99×20×23 mm), with a [bracket already designed](xlerobot-d435i-bracket.md).

The IMU matters more than it looks for this leg: RTAB-Map's localization is materially more robust with one, and a differential base pushed by hand or slipping on carpet is exactly the case where visual odometry alone drifts.

**Alternative worth pricing:** a ~$100 2-D LiDAR (RPLIDAR A1 class) gives a much easier SLAM problem than RGB-D, at the cost of losing the depth stream you'd also want for grasping. Given that the arm work needs depth anyway, **RGB-D is the better single purchase** — but if navigation robustness becomes the sticking point, adding 2-D LiDAR alongside is a cheap fix.

### Odometry — you have it, and Sourccey doesn't

Worth stating because it is a genuine advantage of this platform: the base runs **FeeTech STS3215 servos with absolute 0–4095 encoders**, so wheel odometry is available to fuse into RTAB-Map. This is exactly what [Sourccey](../../entities/sourccey.md) gave up with open-loop PWM wheels — and it is why its Oct-2026 "improved SLAM" roadmap item is harder than it sounds. You are starting from the better position.

### The non-holonomic consequence

Your base is **2-wheel differential** — it cannot strafe. The fleet framework already worked out what that means for grasping: a holonomic base can sidle sideways to fine-align before a grasp; yours must **turn-then-approach**. So `navigate_to` should target a **grasp-ready pose head-on**, not "get close, then align." Design the nav goal poses accordingly, and expect pre-grasp positioning to be the place this shows up.

---

## 4. Leg C — integration, and the blocker to plan around

> [!warning] One serial port has exactly one owner
> This is the concrete thing standing between "nav works" + "pick works" and "nav-then-pick works." The wiki already hit it: a ROS 2 `sensor_msgs/JointState` publisher reading the FeeTech bus **cannot coexist with LeRobot holding the same bus** — *"a serial port has exactly one owner, so this node and LeRobot cannot both hold the arm bus. It works when LeRobot isn't driving; it does not solve the general case."*
>
> **The general fix is [Rosetta](../../entities/rosetta.md) owning the bus and serving both sides** — a declarative YAML contract mapping ROS 2 topics to LeRobot's `observation.*` / `action` model. That makes Rosetta's arm-bus contract a **load-bearing dependency of this project**, not a nice-to-have. Ladder step 1 is doing more work than its one-line description suggests.
>
> **Cheap interim:** time-slice. Nav owns the base and never touches the arm bus; LeRobot takes the arm bus only during a pick, releases it after. Good enough for "navigate to the table, then pick" as a sequenced task; **not** good enough for anything needing arm state during navigation (carrying an object, visual servoing while moving).

The task-level layer above this — deciding *when* to navigate and *when* to pick — is fleet-ladder steps 2–3 (ROS 2 ↔ MCP server, then an onboard agent). Explicitly out of scope here; this plan ends when nav and pick both run as callable skills.

---

## 5. Sequence

Legs A and B are independent. Run them in parallel; the integration is the join.

| Phase | Work | Stop condition |
|---|---|---|
| **0** | **Decide the depth camera** (D435i + [bracket](xlerobot-d435i-bracket.md), or reuse existing). Order early — it gates Leg B and helps Leg A. | Camera mounted, streaming, calibrated. |
| **A1** | Data-collection discipline: fixed framing, episode boundaries, one strategy per task. Pick a **top-down** task. | 5 clean demos recorded and replayed. |
| **A2** | ~50 demos (2–3 h). Train ACT on the Spark (`cu130` wheels). Deploy onboard. | **A learned pick works on-robot** — ladder step 0. |
| **B1** | RTAB-Map mapping run of the operating area; save the map. | A map you can localize against. |
| **B2** | Nav2 bringup, costmaps, footprint tuned for the differential base. | `navigate_to` reaches a named pose reliably. |
| **C1** | Time-sliced bus arbitration; sequence nav → pick as one scripted task. | **Nav-to-object-then-pick runs** — ladder step 1, interim form. |
| **A3** | Fine-tune SmolVLA from `smolvla_base` on your demos; serve from the Spark via LeRobot async. | Multi-task pick beats the single-task ACT baseline. |
| **C2** | Rosetta arm-bus contract, replacing the time-slice. | Arm state available during navigation. |

Phases 0/A1/B1 can all start now. **A2 is the highest-value single milestone** — it is the first point where the robot does something learned, and it validates the whole data flywheel.

---

## 6. Risks, in order of how likely they are to actually bite

1. **Demo quality, not demo quantity.** The most common failure is 50 inconsistent episodes that train a policy which does nothing. Mitigation: replay your first 5 recordings before collecting 45 more, and adopt X-VLA's DAgger habit — retrain every ~100 episodes, find the failure modes, collect *against* them rather than collecting more of the same.
2. **The serial-bus conflict** (§4). Known, has a known fix, and will still cost time.
3. **Grasp geometry fighting the 5-DoF kinematics.** If a task needs a non-radial lateral approach it will not work, and it will look like a policy problem. Check reachability by teleoperating the grasp *by hand* before recording 50 demos of it.
4. **Network latency on the SmolVLA hop.** Wired is fine; Wi-Fi is the wildcard — the [Spark→XLeRobot serving estimate](gr00t-spark-zmq-xlerobot.md) puts the ZMQ hop at 10–40 ms and calls Wi-Fi the uncertainty. Mitigate with action chunking, which LeRobot does by default.
5. **Spark ARM64 friction.** Real but bounded, and already scoped in the wiki: pin the `cu130` torch wheels and expect occasional missing ARM builds. This is *training and serving*, which NVIDIA ships multi-arch containers for — unlike the [SAPIEN/RoboTwin case](five-dof-arms-in-robotwin.md), where ARM64 is a genuine unknown.
6. **Scope creep into the agent layer.** "Pick up the sock and put it in the basket" *spoken* is ladder step 2, not this plan. Ending at callable skills is what keeps this finite.

---

## 7. What this plan deliberately does not do

- **No RoboTwin, no synthetic data.** [Deferred, with reasons](five-dof-arms-in-robotwin.md#3a-is-this-on-the-critical-path-to-a-working-xlerobot) — SmolVLA is validated on this exact arm, so real demos are the shorter path. Revisit only if demonstration collection becomes the measured bottleneck.
- **No cross-embodiment VLA.** The 5-DoF exclusion documented across [X-VLA](../../entities/x-vla.md) / [RoboMIND](../../entities/robomind.md) / [RoboTwin](../../entities/robotwin.md) is a real research gap and **not your problem** — the single-platform LeRobot line already covers this arm.
- **No agent / MCP / natural-language layer.** Ladder steps 2+, already scoped in the [fleet framework](fleet-agentic-framework.md).
- **No fleet.** One robot, end to end, first.

## Related

- [Fleet agentic framework](fleet-agentic-framework.md) — the ladder this executes steps 0–1 of; [implementation notes](fleet-framework-implementation-notes.md)
- [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) — the measured onboard-Jetson XLeRobot precedent and the nav recipe
- [GR00T on DGX Spark → XLeRobot](gr00t-spark-zmq-xlerobot.md) — the off-board serving leg
- [XLeRobot camera options](xlerobot-camera-options-low-light.md) · [D435i bracket](xlerobot-d435i-bracket.md) · [power budget](xlerobot-thor-power-budget.md)
- [SmolVLA](../../entities/smolvla.md) · [ACT](../../entities/act.md) · [Rosetta](../../entities/rosetta.md) · [Nav2](../../entities/nav2.md)
- [5-DoF arms in RoboTwin](five-dof-arms-in-robotwin.md) — where the top-down grasp constraint comes from
