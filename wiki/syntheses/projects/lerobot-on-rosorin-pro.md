---
title: LeRobot on ROSOrin Pro — adaptation plan for in-home floor-pickup-and-tidy
type: synthesis
created: 2026-05-28
updated: 2026-05-28
tags: [lerobot, rosorin-pro, hiwonder, hx-12h, openclaw, smolvla, act, dobb-e, robot-utility-models, async-inference, floor-pickup, in-home, feasibility, project-plan, rosetta]
---

# LeRobot on ROSOrin Pro — adaptation plan for in-home floor-pickup-and-tidy

A practical question: **can [LeRobot](../../entities/lerobot.md) be adapted to drive a [ROSOrin Pro](../../entities/rosorin-pro.md), and would it actually improve the robot's AI control toward the end-user goal of "navigate the house, pick objects off the floor, put them away in an organized fashion"?** Short answer: **yes to both, and the integration is much shorter than originally scoped here** — there is a community bridge ([Rosetta](../../entities/rosetta.md), Sep 2025) that resolves the LeRobot↔ROS 2 gap declaratively, so the dominant cost shifts to **demo collection**.

> [!warning] Updated 2026-05-28 — three LeRobot↔ROS 2 bridges exist; Rosetta is the right one for ROSOrin Pro
> The original "Path 1 — wrap `~/arm_group_control` in a `lerobot.robots.rosorin_pro` Python class" plan is **superseded** by [Rosetta](../../entities/rosetta.md): a community project that lets you write a YAML contract mapping ROS 2 topics to LeRobot features. Three independent LeRobot↔[ROS 2](../../entities/ros2.md) bridges have been ingested into the wiki:
>
> | Bridge | Approach | Hardware | ROS 2 distro | Fit for ROSOrin Pro? |
> |---|---|---|---|---|
> | **[Rosetta](../../entities/rosetta.md)** (76★) | YAML contract | any ROS 2 robot | distro-agnostic | **✓ Yes — use this** |
> | **[lerobot-ros](../../entities/lerobot-ros.md)** (194★) | Python sub-class | any ros2_control / MoveIt arm | **Jazzy only** | ✗ ROSOrin Pro is Humble |
> | **[so101-ros2](../../entities/so101-ros2.md)** (50★) | SO-101 workspace | **SO-101 only** | Humble only | ✗ ROSOrin Pro is not an SO-101 |
>
> **Rosetta is the right choice for ROSOrin Pro** because (a) it's distro-agnostic (the other two are pinned to either Humble or Jazzy in ways that don't both line up with ROSOrin Pro), (b) it supports mobile bases via the `turtlebot3.yaml` reference contract — neither sibling does, and (c) the YAML-contract approach maps cleanly to ROSOrin Pro's mixed control surface (`~/arm_group_control` for the arm + `/controller/cmd_vel` for the base). Step 1 below assumes Rosetta. The remaining content is preserved for context on the underlying gaps; the [revised recommended ladder](#recommended-ladder-updated-2026-05-28-with-rosetta) is the current plan.

> [!note] Why this pairing
> [ROSOrin Pro](../../entities/rosorin-pro.md) ships with the [OpenClaw](../../entities/openclaw.md) LLM-agent that orchestrates **deterministic, hand-coded** skills (color-thresholded grasps, AprilTag-anchored deliveries). It will not generalize to "any object that doesn't belong on the floor." A learned visuomotor policy — exactly what [LeRobot](../../entities/lerobot.md)'s reference algorithms ([ACT](../../entities/act.md), [Diffusion Policy](../../entities/diffusion-policy.md), [SmolVLA](../../entities/smolvla.md), [π0](../../entities/pi-zero.md)) produce — is the missing primitive.

## What ROSOrin Pro provides today

From [ROSOrin Pro entity](../../entities/rosorin-pro.md) + [user manual](../../sources/hiwonder-rosorin-pro-user-manual.md) + [OpenClaw tutorial](../../sources/hiwonder-openclaw-tutorial.md):

- **Compute**: [Jetson Orin Nano](../../entities/jetson-orin-nano.md) / NX (or Jetson Nano / Raspberry Pi 5). Orin Nano 8 GB is the reference target.
- **Arm**: 6-DOF, **HX-12H bus servos** (12 kg·cm stall @ 11.0 V, 0.2 s/60°), gripper end-effector.
- **Base**: differential-drive (Ackermann variant).
- **Sensors**: COIN-D6 LiDAR (360°, 12 m, 9.5–10.5 Hz); Deptrum Aurora930 depth + RGB (640×400 @ **12 fps**, 15–300 cm); MPU6050 IMU; 6-mic array.
- **Low-level MCU**: STM32F407VET6 (168 MHz; 512 KB Flash).
- **Stack**: ROS 2 Humble (Ubuntu 22.04 on Orin); SLAM + Nav2 wired up; Hiwonder's [`openclaw_controller`](../../entities/openclaw-controller.md) ROS 2 module exposes string-command services to upstream [OpenClaw](../../entities/openclaw.md): `~/arm_group_control`, `/start_pick`, `/place`, `/controller/cmd_vel`, plus skill-level launch files (`navigation_manager.launch.py`, `smart_scene_navigation.launch.py`).

## What LeRobot provides (per ICLR 2026 paper)

From [LeRobot ICLR 2026 paper](../../sources/lerobot-iclr-2026-paper.md):

- **Unified middleware** built on **FeeTech and Dynamixel** low-level SDKs.
- **`LeRobotDataset` format** (16K+ datasets / 2.2K+ contributors as of Sep 2025).
- **Async producer-consumer inference stack** with physical + logical decoupling (policy on a remote server, control on the robot client).
- **Reference policies**: [ACT](../../entities/act.md), [Diffusion Policy](../../entities/diffusion-policy.md), [VQ-BET](../../entities/vq-bet.md), [HIL-SERL](../../entities/hcrlab.md), [TD-MPC](../../entities/td-mpc.md), [π0](../../entities/pi-zero.md), [SmolVLA](../../entities/smolvla.md).
- **Native sim integration**: [LIBERO](../../entities/libero.md), [Metaworld](../../entities/metaworld.md).

## The three concrete gaps

### Gap 1 — Motor SDK lineage (FeeTech / Dynamixel ≠ HX-12H)

[LeRobot's middleware](../../entities/lerobot.md) is built explicitly on FeeTech and Dynamixel low-level SDKs ([ICLR 2026 paper §3.1](../../sources/lerobot-iclr-2026-paper.md)). The ROSOrin Pro's HX-12H bus servos are a Hiwonder lineage not in LeRobot's tree. None of LeRobot's 8 supported platforms ([SO-100/101](../../entities/so-arm101.md), Koch-v1.1, [ALOHA-2](../../entities/aloha.md), [HopeJR-Arm](../../entities/hope-jr-arm.md), [LeKiwi](../../entities/lekiwi.md), [Stretch-3](../../entities/stretch.md), [Reachy-2](../../entities/reachy.md)) covers it.

Two ports of entry, in order of preference:

1. **Wrap the existing ROS 2 service interface.** Implement `lerobot.robots.rosorin_pro` and `lerobot.teleoperators.rosorin_pro` classes that publish to `~/arm_group_control` and read `~/move_status` (the same services Hiwonder's [`openclaw_controller`](../../entities/openclaw-controller.md) bridge already wraps for [OpenClaw](../../entities/openclaw.md) per [chapter 13](../../sources/hiwonder-openclaw-tutorial.md)). Latency is bounded by ROS 2 round-trips; pragmatically the fastest path to a working integration.
2. **Talk to the STM32F407 directly over serial**, bypassing ROS — what LeRobot's existing FeeTech driver does. Cleaner integration but requires reverse-engineering Hiwonder's serial protocol.

Start with (1).

### Gap 2 — Cameras and sampling rate

LeRobot datasets are typically **30 Hz**. The Deptrum Aurora930 is **12 fps**. Either downsample the entire pipeline to 12 Hz globally (simplest), or use the depth channel only for proprioceptive grounding and supplement with a higher-rate USB RGB camera (e.g. a Logitech C920-class, what [ALOHA](../../entities/aloha.md) uses).

The `LeRobotDataset` schema is multi-modal and supports `delta_timestamps={"observation.images.X": [-0.2, -0.1, 0.0]}` for multi-step history — straightforward to add depth as an extra modality.

### Gap 3 — Compute budget

From [LeRobot ICLR 2026 paper Tables 2 + 3](../../sources/lerobot-iclr-2026-paper.md) (fp32, RTX 4090 / A100 reference):

| Model | # Params | Peak mem (A100) | Latency RTX 4090 | Orin Nano 8 GB feasibility |
|---|---|---|---|---|
| [ACT](../../entities/act.md) | 52 M | 211 MB | **5 ms** | **Real-time; recommended starting point.** |
| [Diffusion Policy](../../entities/diffusion-policy.md) | 263 M | 1.12 GB | 69.8 ms | Borderline (CPU latency was 3454 ms, 100% timeout in paper); needs TensorRT. |
| [SmolVLA](../../entities/smolvla.md) | 450 M | 1.75 GB | 99.2 ms | Feasible but **<5 Hz** without TensorRT compilation; the *only* frontier VLA that runs on CPU at all. |
| [π0](../../entities/pi-zero.md) | 3.5 B | 13.32 GB | 209 ms | **Won't fit on Orin Nano.** Must use LeRobot's [async inference stack](../../sources/lerobot-iclr-2026-paper.md) with a server (laptop/desktop GPU). |

ACT is the obvious starting point. SmolVLA via async inference (laptop policy server + Orin Nano client over WiFi) is the next step.

## Three paths to the in-home tidy goal

The compositional task is: **navigate to room X → find anything not-in-its-place → pick it → navigate to its bin → place it**. The navigation piece is solved (Nav2 + ROSOrin's LiDAR/SLAM). The interesting part is **open-vocabulary floor-pickup of arbitrary household objects** — which is exactly where OpenClaw's deterministic skills fail.

### Path A — Dobb·E / RUM-style: stick-camera demos, fine-tune on ROSOrin

The closest reference is [Robot Utility Models](../../entities/robot-utility-models.md): **81% success across 109 tasks in 10 homes with 5 min demo + 15 min adaptation** on [Stretch](../../entities/stretch.md), built on [Dobb·E](../../entities/dobb-e.md)'s "Stick" + Homes-of-New-York data ([RUM paper](../../sources/robot-utility-models-paper.md), [Dobb·E paper](../../sources/dobb-e-paper.md)). The stick-camera collection is platform-independent — you'd:

1. Use a phone-on-a-stick (Dobb·E's "Stick") to collect first-person grasp demos in your house.
2. Pretrain on community data ([16K+ LeRobotDataset datasets](../../sources/lerobot-iclr-2026-paper.md), heavily SO-10X — at Sep 2025 the SO-10X arms drive 50%+ of community-contributed datasets, including pick-place repos like `lerobot/svla_so100_pickplace`).
3. Fine-tune on your ROSOrin demos.

**Pros**: well-validated recipe; cheapest in equipment.
**Cons**: kinematic mismatch between stick-frame demos and HX-12H joint trajectories; requires retargeting.

### Path B — Build an SO-100 leader (~€225) for puppeteering

The canonical LeRobot collect→train→deploy loop uses a leader-follower pair. The ROSOrin's arm is a follower only; you'd build a cheap [SO-100](../../entities/so-arm101.md) leader (~€225 per the [ICLR 2026 Table 1a](../../sources/lerobot-iclr-2026-paper.md)) and use your new `lerobot.teleoperators.rosorin_pro_leader` adapter to publish leader joint angles into ROSOrin's `~/arm_group_control`.

**Pros**: unlocks the full LeRobot teleop pipeline; demos are in-distribution at deploy time.
**Cons**: 6-DOF SO-100 → 6-DOF HX-12H joint-angle mapping is non-trivial (different reach, different joint limits, different gripper). Expect 1–2 weeks of retargeting.

### Path C — Zero-shot pretrained SmolVLA

Try [`lerobot/smolvla_base`](../../entities/smolvla.md) zero-shot via the async inference stack (laptop GPU as policy server, Orin Nano as client). SmolVLA beats π0 by +16.6 pts on real-world SO-100 multi-task ([SmolVLA paper](../../sources/smolvla-paper.md)) — but it was trained on SO-100/SO-101 and the embodiment gap to ROSOrin's HX-12H arm is unproven.

**Pros**: zero collection cost.
**Cons**: likely a baseline, not a solution. Reserve for an early sanity check.

## Recommended ladder (updated 2026-05-28 with Rosetta)

Smallest-bet first. **Step 1 is dramatically shorter than originally scoped** — what was "1–2 weeks of writing `lerobot.robots.rosorin_pro` in Python" becomes "1 day of writing a Rosetta YAML contract."

| Step | Effort | Goal | Stop condition |
|---|---|---|---|
| **0.** Zero-shot SmolVLA on ROSOrin (Path C) via SmolVLA-compatible kinematic adapter on a laptop GPU policy server. | 1–3 days | Baseline; check whether anything transfers across the embodiment gap. | If success >20%, lean harder on SmolVLA. If <5%, expect to need real demos. |
| **1.** Write a [Rosetta](../../entities/rosetta.md) YAML contract for ROSOrin Pro — `observation.images.{front,wrist}` from the Aurora930 RGB, `observation.state` from `/joint_states` + odom, `action` publishing `JointState` to `~/arm_group_control` for the arm and `TwistStamped` to `/controller/cmd_vel` for the base. Combine the [`so_101.yaml`](https://github.com/iblnkn/rosetta/blob/main/contracts/so_101.yaml) and [`turtlebot3.yaml`](https://github.com/iblnkn/rosetta/blob/main/contracts/turtlebot3.yaml) reference contracts. | **1 day** | LeRobot can record + replay demos via `episode_recorder_node` → MCAP → LeRobotDataset Parquet. | Demos round-trip end-to-end. |
| **2.** Dobb·E-style "Stick" demo collection (Path A) — 50–200 floor-pickup trajectories in your house, recorded to MCAP via Rosetta's `episode_keyboard_node`. | 1–2 weeks of evenings | A small in-distribution dataset; convert to LeRobotDataset; optionally push to HF Hub. | Replay validates camera + retargeting on actual ROSOrin. |
| **3.** Train [ACT](../../entities/act.md) (52 M params, real-time on Orin Nano) on the combined community + Dobb·E + ROSOrin data using `lerobot-train --policy.type=act`. | 1 day (single GPU) + iteration | First learned floor-pickup skill. Deploy via `rosetta_client_node` (ROS 2 action). | Replace OpenClaw's deterministic `/start_pick` with a ROS 2 action call to the Rosetta client; rest of OpenClaw orchestration is unchanged. |
| **4.** If ACT plateaus, scale up. Two branches: (a) build an SO-100 leader (~€225) and use [`so_101_hil.yaml`](https://github.com/iblnkn/rosetta/blob/main/contracts/so_101_hil.yaml)-style HIL contract to capture intervention demos; (b) migrate to SmolVLA via Rosetta's gRPC policy-server async inference (laptop or desktop GPU). | 2–4 weeks | Open-vocab pickup with language conditioning. | "Pick up the sock by the couch and put it in the laundry hamper" works on average. |

The recommended near-term **architecture** keeps OpenClaw as the orchestrator (LLM dispatching ROS services + navigation) and swaps only the *deterministic* pick skill for a learned LeRobot policy. This is the same composition pattern as [stretch_ai](../../entities/stretch-ai.md) on the research tier — LLM-as-orchestrator + learned manipulation primitive — and the most efficient use of the work already invested in ROSOrin Pro's nav stack.

## What this does NOT solve

- **House navigation.** That's already Nav2 + LiDAR SLAM. LeRobot's scope is end-to-end visuomotor manipulation; it adds nothing to the nav piece.
- **Object permanence + room-scale memory.** Knowing "the sock that was in the hallway needs to go to the bedroom hamper" is an LLM-agent / memory problem, not a policy-learning problem. Belongs in the OpenClaw layer.
- **Compositional autonomy** ("tidy 5 different objects in sequence"). Comes from the orchestrator, not the policy. Today OpenClaw does this — keep it.

## Open questions for execution

- **Servo-protocol reverse-engineering** — if Path 1 latency is too high, would falling back to direct STM32 serial talk to the HX-12H bus actually be faster than the ROS round-trip? Bench-test before committing.
- **Aurora930 12 fps cap** — is this hardware-limited or driver-limited? If driver, can we raise it? 30 Hz is the LeRobot default; 12 Hz halves the effective control loop bandwidth.
- **Open-source status of Hiwonder's `openclaw_controller` bridge** — upstream [OpenClaw](../../entities/openclaw.md) is MIT (`github.com/openclaw/openclaw`, 375K stars), but the [bridge module's source / license](../../entities/openclaw-controller.md) hasn't surfaced. If the bridge is closed, building the learned-skill replacement is the right play; if it's open, you may be able to upstream the LeRobot integration as an alternative skill backend in `openclaw_controller`.
- **Async inference on consumer WiFi** — LeRobot's async stack assumes a network. Home WiFi jitter could destabilize the producer-consumer queue. Bench-test before relying on it.
- **Path B's leader/follower kinematic mismatch** — what fraction of SO-100 demos actually transfer to HX-12H joint space after retargeting? No data; would need an early bench experiment.

## Related

- [Rosetta](../../entities/rosetta.md) — the LeRobot↔ROS 2 bridge that resolves Gap 1; YAML-contract-driven; ships SO-101 and TurtleBot3 reference contracts. **Read this first** — it dictates the Step 1 approach.
- [LeRobot ICLR 2026 paper](../../sources/lerobot-iclr-2026-paper.md) — canonical reference for the framework.
- [LeRobot entity](../../entities/lerobot.md) — current state of supported platforms / algorithms.
- [ROSOrin Pro](../../entities/rosorin-pro.md) — target hardware.
- [OpenClaw](../../entities/openclaw.md) — current LLM-orchestrator on the platform.
- [Robot Utility Models](../../entities/robot-utility-models.md) / [Dobb·E](../../entities/dobb-e.md) — closest in-home tidy precedent.
- [stretch_ai](../../entities/stretch-ai.md) — LLM-agent + learned-skill composition on Stretch; same architectural pattern.
- [LeWM on ROSOrin Pro — feasibility analysis](lewm-on-rosorin-pro-feasibility.md) — sibling project on the same hardware with a world-model approach.
- [ROSOrin Pro LEGO pick-place](rosorin-pro-lego-pick-place.md) — smaller-scope ROSOrin project from earlier wiki work.
