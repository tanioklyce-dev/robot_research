---
title: "Rosetta — LeRobot for ROS2 Robots (iblnkn/rosetta GitHub)"
type: source
url: https://github.com/iblnkn/rosetta
license: Apache-2.0
author: iblnkn (GitHub user)
created: 2025-09-14
last_pushed: 2026-05-24
ingested: 2026-05-28
stars: 76
forks: 14
languages: Python 99.4% / CMake 0.6%
tags: [rosetta, lerobot, ros2, bridge, yaml-contract, mcap, async-inference, grpc, act, smolvla, pi0, pi0.5, groot, wall-x, x-vla, so-101, turtlebot3, hil]
---

## Summary

**Rosetta** — an open-source framework that integrates [LeRobot](../entities/lerobot.md) with ROS 2, "enabling the ROS2 community to leverage state-of-the-art imitation learning and policy training capabilities" (README). Solo project by GitHub user **iblnkn**; Apache 2.0; created Sep 14 2025; **76 stars / 14 forks / 4 open issues / last push 2026-05-24**. Python 99.4%.

The project's premise: LeRobot's middleware is [FeeTech](../entities/feetech.md)/[Dynamixel](../entities/dynamixel.md)-native ([LeRobot ICLR 2026 paper](lerobot-iclr-2026-paper.md) §3.1), but the production robot world runs on [ROS 2](../entities/ros2.md). Rosetta bridges that gap declaratively — a **YAML "contract"** maps arbitrary ROS 2 topics to LeRobot's data model, so any ROS 2-controllable robot can be a LeRobot platform without writing a `lerobot.robots.<myrobot>` Python class.

## The 5-step pipeline (README "Core Workflow")

1. **Define** a YAML contract mapping ROS 2 topics ↔ LeRobot features.
2. **Record** demonstrations to rosbag2 (MCAP) files.
3. **Convert** bags to [LeRobotDataset format](lerobot-iclr-2026-paper.md).
4. **Train** policies using standard `lerobot-train --policy.type=...`.
5. **Deploy** trained policies back to robots via ROS 2 actions.

## Architecture — 5 packages

- **`rosetta`** — core library + CLI tools.
- **`rosetta_interfaces`** — ROS 2 action / service definitions.
- **`lerobot_robot_rosetta`** — LeRobot Robot plugin (registers a Rosetta-driven robot inside LeRobot).
- **`lerobot_teleoperator_rosetta`** — Teleoperator plugin (experimental).
- **`rosetta_rl`** — Reinforcement learning support (coming soon).

Visible Python nodes in the main package (`rosetta/`): `episode_recorder_node.py`, `episode_keyboard_node.py`, `rosetta_client_node.py`, `rosetta_hil_manager_node.py`, `port_bags.py`, plus `common/`.

## The Contract (YAML)

The contract is the central abstraction. Minimal example from README:

```yaml
robot_type: my_robot
fps: 30

observations:
  - key: observation.state
    topic: /joint_states
    type: sensor_msgs/msg/JointState
    selector:
      names: [position.j1, position.j2]

actions:
  - key: action
    publish:
      topic: /joint_commands
      type: sensor_msgs/msg/JointState
    selector:
      names: [position.j1, position.j2]
```

### Reference contracts shipped in `contracts/`

- **`so_101.yaml`** — [SO-101 arm](../entities/so-arm101.md); 3 compressed-image cameras (front / top / wrist, 512×512), 6-joint follower-arm state, leader-arm-published actions, MCAP storage, `unit_conversion: rad2deg`. Demonstrates a manipulator with multi-camera setup.
- **`so_101_hil.yaml`** — same as above + HIL (human-in-the-loop) extensions: separate `/human/leader_arm/joint_states` teleoperator topic, button-mapped intervention / success / failure / terminate / re-record signals (`buttons.10` triggers intervention), reward topic for RL.
- **`turtlebot3.yaml`** — [TurtleBot3](../entities/turtlebot.md) Waffle; 2 RGB cameras (front + overhead, 224×224), 20-dim observation.state spanning **wheel joint states (4) + IMU quaternion/angular/linear (10) + odometry (6)**, action = 2-dim `geometry_msgs/TwistStamped` (linear.x, angular.z), `safety_behavior: zeros`, `adjunct: [/tf, /scan]` (recorded but not in the policy input).

### Contract features observed across the examples

- **`align: {strategy: hold, stamp: header}`** — timestamp alignment policy per stream.
- **`qos: {reliability: best_effort, history: keep_last, depth: N}`** — ROS 2 QoS per topic.
- **`image.resize: [H, W]`** — declarative image preprocessing.
- **`selector.names`** — pick named fields from compound messages (joint names, IMU axes, quaternion components).
- **`unit_conversion: rad2deg`** — declarative unit conversion at the boundary.
- **`safety_behavior: zeros`** — what to publish on policy failure (zero `cmd_vel` for a mobile base is the obvious safety default).
- **`adjunct`** — extra topics recorded into the bag but not exposed to the policy (e.g. `/tf`, `/scan`); enables post-hoc re-contracting.
- **`recording.storage: mcap`** — MCAP rosbag2 format.

The README emphasizes that **bags preserve raw data** — "Bags can be reprocessed later with different contracts without re-recording." That's a key design choice: data collection is decoupled from policy input shape.

## Recording → Conversion → Training → Deployment

- **Recording**: `episode_recorder_node` captures rosbag2 + optional **keyboard control** (`episode_keyboard_node`) or action-based control. Stores MCAP.
- **Conversion**: applies contract mapping, timestamp alignment, encodes videos into the LeRobotDataset Parquet format. Batch conversion supported; optional HF Hub push.
- **Training**: standard LeRobot — `lerobot-train --dataset.repo_id=my-org/my-dataset --policy.type=act`.
- **Deployment**: `rosetta_client_node` wraps LeRobot inference in ROS 2 actions. Local or **remote GPU server via LeRobot's gRPC interface** — i.e. Rosetta uses the same [async inference stack](lerobot-iclr-2026-paper.md) from the ICLR 2026 paper, but exposes it through ROS 2 lifecycle nodes.

## Supported policies (broader than upstream LeRobot)

Per README: **ACT, SmolVLA, Pi0, Pi0.5, GR00T, Wall-X, X-VLA**. This is a superset of the [LeRobot ICLR 2026 paper](lerobot-iclr-2026-paper.md)'s reference set (ACT, Diffusion Policy, VQ-BET, HIL-SERL, TD-MPC, π0, SmolVLA) — adds:

- **[π0.5](../entities/pi-zero-6.md)** (sibling of [π0.7](../entities/pi07.md))
- **[GR00T](../entities/nvidia-groot.md)** (NVIDIA's humanoid foundation model)
- **Wall-X** — VLA referenced but not in this wiki yet (open question).
- **X-VLA** — VLA referenced but not in this wiki yet (open question).

> [!note] Coverage delta vs upstream LeRobot
> Rosetta extends LeRobot's policy coverage with newer / non-HF VLAs. This is a downstream community accelerator — the kind of contribution the LeRobot paper explicitly invites in Limitation #2 ("algorithm coverage is non-exhaustive, future work"). But it means Rosetta users get GR00T support before/without upstream LeRobot adopting it.

## HIL (human-in-the-loop) support

`rosetta_hil_manager_node.py` + `so_101_hil.yaml` show first-class support for HIL workflows à la [HIL-SERL](../entities/hcrlab.md):

- Separate teleoperator topic for intervention.
- Button-mapped events: intervention, success, failure, terminate, re-record.
- Reward topic for RL.

This is the operational complement to the upcoming `rosetta_rl` package and aligns with LeRobot's existing HIL-SERL integration.

## Entities mentioned

- [LeRobot](../entities/lerobot.md) — the upstream framework Rosetta bridges to ROS 2.
- [SO-ARM101](../entities/so-arm101.md) — reference contract.
- [Turtlebot](../entities/turtlebot.md) (TurtleBot3 Waffle specifically) — reference contract.
- [ACT](../entities/act.md), [SmolVLA](../entities/smolvla.md), [π0](../entities/pi-zero.md), [π0.5/π0.6](../entities/pi-zero-6.md), [GR00T](../entities/nvidia-groot.md) — supported policies.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md)
- [VLA models](../concepts/learning/vla-models.md)
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) (loosely — bag→dataset→policy→deploy is the IL-driven analogue)

## Why this matters for this wiki

This directly addresses **Gap 1** from the just-filed [LeRobot on ROSOrin Pro synthesis](../syntheses/projects/lerobot-on-rosorin-pro.md): the "HX-12H servos ≠ FeeTech/Dynamixel SDKs" problem. ROSOrin Pro is a ROS 2 robot that already exposes joint state on `/joint_states` and accepts arm commands via `~/arm_group_control` ([OpenClaw tutorial](hiwonder-openclaw-tutorial.md)). With Rosetta, the LeRobot integration becomes a **YAML contract** rather than a Python driver subclass — possibly a 1-day task instead of 1–2 weeks.

The TurtleBot3 contract is particularly relevant — it demonstrates a working contract for a **wheeled mobile base** publishing to `/cmd_vel` (exactly the same control surface ROSOrin Pro exposes via `/controller/cmd_vel`).

## Open questions

- **What's the production maturity?** 76 stars / 14 forks / 4 open issues / solo author / 8 months old (Sep 2025 → May 2026). Active but small-team. Risk profile of relying on it for a personal project: moderate.
- **Author identity**: "iblnkn" is the GitHub handle. No organizational affiliation visible. Worth identifying for context on roadmap commitment.
- **Wall-X and X-VLA** — referenced as supported policies but neither is in this wiki yet. Worth a follow-up ingest.
- **`rosetta_rl` timeline** — README says "coming soon"; HIL infrastructure (`rosetta_hil_manager_node.py`, HIL contract) is already in place, so RL is plausibly the next major milestone.
- **Is Rosetta on PyPI / available via `pip install`?** README workflow examples imply yes but the package distribution channel isn't surfaced from the README alone.
- **Relationship to upstream LeRobot** — is there an upstreaming conversation? The [ICLR 2026 paper](lerobot-iclr-2026-paper.md) doesn't reference Rosetta (paper was Feb 2026; Rosetta launched Sep 2025).
- **Empirical reports / blog posts / demos** — none surfaced from the README. Anyone actually used it to deploy a trained policy on a non-SO-101 / non-TurtleBot3 robot?
