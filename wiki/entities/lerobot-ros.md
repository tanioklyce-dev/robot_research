---
title: lerobot-ros (ycheng517)
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 3
tags: [lerobot-ros, lerobot, ros2, jazzy, ros2_control, moveit, moveit-servo, ycheng517, downstream, generic-bridge]
---

**`ycheng517/lerobot-ros`** — generic Python-class-based ROS 2 wrapper for [LeRobot](lerobot.md). Tagline: *"Lightweight interface for controlling ROS-based robotic arms using LeRobot."* **194 stars / 28 forks (May 2026)** — the **most-starred LeRobot↔ROS 2 bridge in this wiki**, ~2.5× [Rosetta](rosetta.md) and ~4× [so101-ros2](so101-ros2.md). No license listed in repo metadata. ROS 2 **Jazzy only** ("This repo is only tested on Jazzy"). Created Jul 27 2025; last push Nov 6 2025. Repo: [github.com/ycheng517/lerobot-ros](https://github.com/ycheng517/lerobot-ros).

## Architectural stance

**Sub-class `ROS2Robot` and `ROS2Config`** in Python, then register with LeRobot via `@RobotConfig.register_subclass("my_ros2_robot")`. ~30 lines to add a new robot. This is the orthogonal alternative to [Rosetta](rosetta.md)'s YAML-contract approach (which is declarative — no Python required) and [so101-ros2](so101-ros2.md)'s hardware-specific workspace.

Two packages, no monolith:

- `lerobot_robot_ros/` — the LeRobot Robot plugin (`ROS2Robot` + `ROS2Config`).
- `lerobot_teleoperator_devices/` — gamepad teleop (6-DoF end-effector) + keyboard teleop (joint position).

## Three control modes

| Mode | `action_type` | Backing controller | Use case |
|---|---|---|---|
| Joint position | `JOINT_POSITION` | `position_controllers/JointGroupPositionController` | Direct joint targets |
| Joint trajectory | `JOINT_TRAJECTORY` | `joint_trajectory_controller/JointTrajectoryController` | Smooth trajectory execution |
| EE velocity | `CARTESIAN_VELOCITY` | `moveit_servo` + `joint_trajectory_controller` | Cartesian-space control (needs MoveIt 2) |

Gripper modes: trajectory (via `JointTrajectoryController`) or action (via `GripperActionController`).

## Three-bridge comparison (this wiki)

| Dimension | **lerobot-ros** | [Rosetta](rosetta.md) | [so101-ros2](so101-ros2.md) |
|---|---|---|---|
| Approach | Python sub-class | YAML contract | SO-101 workspace |
| Hardware coverage | any ros2_control / MoveIt arm | any ROS 2 robot | SO-101 only |
| Packages | **2** | 5 | 8 |
| Stars (May 2026) | **194** | 76 | 50 |
| ROS 2 distro | **Jazzy only** | distro-agnostic | **Humble only** |
| Mobile-base support | ✗ (arm-focused) | ✓ (TurtleBot3 contract) | ✗ |
| License | **not specified** | Apache-2.0 | MIT |
| Sim | Gazebo (per quickstart) | not specified | **Isaac Sim 5.0+** |
| Last push | 2025-11-06 (~6 mo) | 2026-05-24 (days) | 2025-12-13 (~5 mo) |

## When to choose lerobot-ros

- You're on **Jazzy** (or willing to upgrade from Humble).
- You have a **ros2_control or MoveIt-compatible arm** and want generic LeRobot integration.
- You want the **minimum operational footprint** (2 packages, 1 conda env, upstream LeRobot).
- You're willing to accept the **missing license** caveat for personal / research use.

**Don't choose it** if: you're on Humble, you need mobile-base support (use [Rosetta](rosetta.md)), you specifically want SO-101 + Isaac Sim (use [so101-ros2](so101-ros2.md)), or you need a clean license for redistribution.

## Related

- [LeRobot](lerobot.md) — upstream framework.
- [ROS 2](ros2.md) — middleware substrate; Jazzy specifically.
- [MoveIt](moveit.md) — required for end-effector velocity control mode (via `moveit_servo`).
- [Gazebo](gazebo.md) — quickstart simulator for the simulated SO-101.
- [Rosetta](rosetta.md) — sibling LeRobot↔ROS 2 bridge (YAML approach).
- [so101-ros2](so101-ros2.md) — sibling LeRobot↔ROS 2 bridge (hardware-specific approach).
- [SO-ARM101](so-arm101.md) — reference quickstart robot.

## Mentioned in

- [lerobot-ros GitHub](../sources/lerobot-ros-github.md) — primary source.

## Open questions

- **No license** — blocks redistribution. Should be raised with author.
- **Maintenance momentum** — last push 6 months old; star count is the highest of the 3 bridges but activity may be slowing.
- **Multi-camera dataset capture** — not the primary focus.
- **Mobile-base path** — explicitly arm-focused; [Rosetta](rosetta.md) is the better fit for wheeled robots.
- **Author identity** — `ycheng517` also maintains [`ar4_ros_driver`](https://github.com/ycheng517/ar4_ros_driver) (a real-robot ROS 2 driver used as the MoveIt Servo example); no organizational affiliation visible.
