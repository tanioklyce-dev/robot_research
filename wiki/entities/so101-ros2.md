---
title: so101_ros2 (nimiCurtis)
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 1
tags: [so101-ros2, lerobot, ros2, humble, so-101, isaac-sim, smolvla, pi05, nimicurtis, downstream, hardware-specific]
---

**`nimiCurtis/so101_ros2`** — SO-101-hardware-specific ROS 2 workspace + LeRobot bridge. **MIT-licensed**, 50 stars / 8 forks (May 2026), Python 3.10+, ROS 2 **Humble**. Created Jun 12 2025; v0.1.1 released Dec 13 2025. Docs at [so101-ros2.readthedocs.io](https://so101-ros2.readthedocs.io/latest/); code at [github.com/nimiCurtis/so101_ros2](https://github.com/nimiCurtis/so101_ros2).

The most opinionated of the three LeRobot↔ROS 2 bridges in this wiki. Ships a **complete 8-package workspace** including URDF/USD, hardware interface, controllers, bringup, teleop, and bag→LeRobotDataset converter — plus **Isaac Sim 5.0+ integration** that the other two don't have.

## 8-package workspace

| Package | Role |
|---|---|
| `so101_description` | URDF + Xacro + meshes + USD files (Isaac Sim) |
| `so101_hardware_interface` | ROS 2 control hardware interface for real SO-101 |
| `so101_controller` | ros2_control controllers + launch files |
| `so101_bringup` | System launch + configuration |
| `so101_ros2` | Core utilities |
| `so101_ros2_bridge` | **The LeRobot↔ROS 2 bridge nodes** (primary integration) |
| `so101_teleop` | Manual control / teleop utilities |
| `ros2_externals/` | Bundled external dependencies |

Plus separate `so101_rosbag2lerobot_dataset` for rosbag → LeRobotDataset conversion.

## Lerobot integration features (per README)

- Real-time leader/follower SO-101 teleoperation via LeRobot API.
- Camera pipelines: V4L USB + Intel RealSense 2.0.
- Demo recording via `system_data_recorder`.
- `so101_rosbag2lerobot_dataset` for offline rosbag → LeRobotDataset conversion.
- VLA training / fine-tuning via LeRobot.
- **Deployment of SmolVLA + π0.5** policies.
- **Isaac Sim 5.0+** for virtual teleop + inference.

## Heavier operational footprint

Requires **two conda envs** (LeRobot wants Python 3.10; Isaac Sim 5.0+ wants 3.11) **plus the author's own LeRobot fork** ([`nimiCurtis/lerobot`](https://github.com/nimiCurtis/lerobot)) rather than upstream `huggingface/lerobot`. The fork dependency is a maintenance risk if upstream LeRobot drifts.

## Three-bridge comparison

| Dimension | **so101-ros2** | [Rosetta](rosetta.md) | [lerobot-ros](lerobot-ros.md) |
|---|---|---|---|
| Approach | SO-101 reference workspace | YAML contract | Python sub-class |
| Hardware coverage | **SO-101 only** | any ROS 2 robot | any ros2_control / MoveIt arm |
| Packages | **8** | 5 | 2 |
| Stars (May 2026) | 50 | 76 | **194** |
| ROS 2 distro | **Humble** | distro-agnostic | **Jazzy only** |
| License | **MIT** | Apache-2.0 | not specified |
| Sim | **Isaac Sim 5.0+** | not specified | Gazebo |
| URDF / USD | shipped | not in scope | not in scope |
| Policies tested | SmolVLA + π0.5 | LeRobot menu + π0.5 + GR00T + Wall-X + X-VLA | not the focus |
| Operational footprint | **2 conda envs + author's LeRobot fork** | 1 env + upstream LeRobot | 1 env + upstream LeRobot |
| Documentation | **dedicated readthedocs site** | README only | README only |

## When to choose so101_ros2

- You own an **SO-101 specifically** (not SO-100, not Koch, not another arm).
- You want **Isaac Sim integration** (the unique feature vs the other two bridges).
- You're on **Humble** (not Jazzy).
- You're OK with a 2-conda-env install + dependency on the author's LeRobot fork.

**Don't choose it** if: you have any other robot, you're on Jazzy, you want a minimal install, or you want to track upstream `huggingface/lerobot` directly.

## Related

- [LeRobot](lerobot.md) — upstream framework (this project uses an author fork).
- [ROS 2](ros2.md) — middleware substrate; Humble specifically.
- [SO-ARM101](so-arm101.md) — the only supported hardware.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — integrated simulator.
- [SmolVLA](smolvla.md) / [π0.5/0.6](pi-zero-6.md) — supported deployment policies.
- [Rosetta](rosetta.md) — sibling generic LeRobot↔ROS 2 bridge.
- [lerobot-ros](lerobot-ros.md) — sibling generic LeRobot↔ROS 2 bridge.

## Mentioned in

- [so101_ros2 readthedocs](../sources/so101-ros2-readthedocs.md) — primary source.

## Open questions

- **LeRobot fork divergence** — how out-of-date is `nimiCurtis/lerobot` vs upstream? What does the fork add?
- **SO-100 backport feasibility** — would changes to motor IDs / baud rates suffice, or is hardware-interface code SO-101-specific?
- **VLA deployment maturity** — claims SmolVLA + π0.5 deployment work. No public demos / benchmarks surfaced.
- **Isaac Sim teleop latency profile** — the unique value-add; performance characteristics not in the README.
- **Author identity** — `nimiCurtis` = Nimi Curtis. No organizational affiliation visible.
