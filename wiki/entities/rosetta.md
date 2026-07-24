---
title: Rosetta
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 7
tags: [rosetta, lerobot, ros2, bridge, yaml-contract, mcap, async-inference, grpc, iblnkn, apache-2-0, downstream]
---

**Rosetta** — open-source bridge between [LeRobot](lerobot.md) and ROS 2. Tagline: *"LeRobot for ROS2 Robots."* Apache 2.0; **76 stars / 14 forks (May 2026)**; solo project by GitHub user **`iblnkn`**; created Sep 14 2025; active development (last push 2026-05-24). Python 99.4%. Repo: [github.com/iblnkn/rosetta](https://github.com/iblnkn/rosetta).

## What it does

Rosetta extends LeRobot to any **ROS 2-controllable robot** without writing a `lerobot.robots.<myrobot>` Python class. Instead, you write a **YAML "contract"** that declaratively maps ROS 2 topics to LeRobot's data model:

- `observation.images.<name>` ← compressed image topic (with declarative `resize`).
- `observation.state` ← composable from `JointState`, `Imu`, `Odometry`, etc. via `selector.names`.
- `action` → published as a ROS 2 message (`JointState`, `TwistStamped`, …).
- Per-topic QoS, alignment strategy, unit conversion, safety behavior — all declarative.
- `adjunct` topics get recorded into the bag but aren't fed to the policy — enables re-contracting without re-collecting.

## The 5-step pipeline

1. **Define** YAML contract.
2. **Record** demos via `episode_recorder_node` to MCAP rosbag2 (optional keyboard-driven episode control via `episode_keyboard_node`).
3. **Convert** bags → [LeRobotDataset](../sources/lerobot-iclr-2026-paper.md) Parquet (timestamp align, video encode, batch + HF Hub push supported).
4. **Train** using standard `lerobot-train --policy.type=...`.
5. **Deploy** via `rosetta_client_node` (wraps LeRobot inference in ROS 2 lifecycle actions; local or remote-server via LeRobot's gRPC interface).

## Five packages

- `rosetta` — core library + CLI.
- `rosetta_interfaces` — ROS 2 action/service definitions.
- `lerobot_robot_rosetta` — LeRobot Robot plugin (registers a Rosetta-driven robot inside LeRobot).
- `lerobot_teleoperator_rosetta` — Teleoperator plugin (**experimental**).
- `rosetta_rl` — RL support (**coming soon**; HIL infra via `rosetta_hil_manager_node.py` and `so_101_hil.yaml` already present).

## Reference contracts shipped

- **`so_101.yaml`** — [SO-101](so-arm101.md) arm; 3 cameras (front / top / wrist, 512×512); 6-joint follower-arm state; leader-arm-published actions; MCAP storage; `unit_conversion: rad2deg`.
- **`so_101_hil.yaml`** — SO-101 + HIL extensions: teleoperator topic, button-mapped intervention/success/failure/terminate/re-record, reward topic for RL.
- **`turtlebot3.yaml`** — [TurtleBot3](turtlebot.md) Waffle; 2 RGB cameras (224×224); 20-dim observation.state (wheel JointState + IMU + Odometry); 2-dim `TwistStamped` action; `safety_behavior: zeros`; `adjunct: [/tf, /scan]`.

## Supported policies

Per README: **ACT, [SmolVLA](smolvla.md), [π0](pi-zero.md), [π0.5](pi-zero-6.md), [GR00T](nvidia-groot.md), Wall-X, X-VLA**. This is a **superset** of the [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md)'s reference policy set — Rosetta adds π0.5, GR00T, Wall-X, X-VLA on top of LeRobot's native ACT / DP / VQ-BET / HIL-SERL / TD-MPC / π0 / SmolVLA.

> [!note] Policy-coverage tradeoff
> Rosetta extends LeRobot's policy menu with newer / non-HF VLAs faster than upstream — this is the kind of downstream community acceleration LeRobot's [paper Limitation #2](../sources/lerobot-iclr-2026-paper.md) explicitly invites. But it means Rosetta users depend on a single solo maintainer for those policies' integration.

## Why it matters in this wiki

Rosetta directly **resolves the central gap** identified in the [LeRobot on ROSOrin Pro synthesis](../syntheses/projects/lerobot-on-rosorin-pro.md): the "HX-12H servos aren't in LeRobot's FeeTech/Dynamixel-native middleware" problem. ROSOrin Pro is a ROS 2 robot exposing `/joint_states` and accepting `~/arm_group_control` strings (the same services Hiwonder's [`openclaw_controller`](openclaw-controller.md) wraps for [OpenClaw](openclaw.md)). With Rosetta, the LeRobot integration is a **YAML contract**, not a Python driver — possibly a 1-day task instead of 1–2 weeks.

The shipped `turtlebot3.yaml` contract is the closest reference for a wheeled mobile base; the `so_101.yaml` contract is the closest reference for a 6-DOF tabletop arm. ROSOrin Pro is essentially "TurtleBot3 base + SO-101-class arm" — both contract templates apply.

## Maturity / risk profile

| Signal | Value |
|---|---|
| Stars / forks | 76 / 14 (May 2026) |
| Age | ~8 months (Sep 2025 → May 2026) |
| Open issues | 4 |
| Last push | 2026-05-24 |
| Maintainers | Solo author (`iblnkn`) |
| License | Apache-2.0 |
| Languages | Python 99.4% / CMake 0.6% |

Active, narrowly-scoped, solo. Risk profile for a personal project: **moderate** — write your contract conservatively, don't depend on `rosetta_rl` (coming-soon) until it ships.

## Related

- [LeRobot](lerobot.md) — upstream framework.
- [ROS 2](ros2.md) — middleware substrate.
- [lerobot-ros](lerobot-ros.md) — **sibling generic bridge** using Python sub-classing (vs Rosetta's YAML); Jazzy only; 194 stars (most popular of the 3).
- [so101-ros2](so101-ros2.md) — **sibling SO-101-specific bridge**; ships URDF/USD + Isaac Sim integration; Humble only; 50 stars.
- [SO-ARM101](so-arm101.md) — reference contract.
- [Turtlebot](turtlebot.md) — reference contract.
- [ROSOrin Pro](rosorin-pro.md) — closest non-shipped use case in this wiki; see the [LeRobot-on-ROSOrin-Pro synthesis](../syntheses/projects/lerobot-on-rosorin-pro.md).
- [OpenClaw](openclaw.md) — the LLM-orchestrator on ROSOrin Pro (via [`openclaw_controller`](openclaw-controller.md)) that would dispatch a Rosetta-trained policy as a learned skill.
- [GR00T](nvidia-groot.md) — supported policy not in upstream LeRobot.

## Mentioned in

- [Rosetta GitHub](../sources/rosetta-github.md) — primary source.

## Open questions

- Production maturity beyond the README — any blog posts, demos, or independent users?
- Author identity / affiliation of `iblnkn` — for context on roadmap commitment.
- **Wall-X** and **X-VLA** — referenced as supported but not in this wiki yet.
- Distribution channel — on PyPI / `pip install rosetta`?
- Upstreaming conversation with the LeRobot team at Hugging Face?
