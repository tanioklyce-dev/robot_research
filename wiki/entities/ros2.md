---
title: ROS 2
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 11
tags: [ros2, ros, middleware, dds, ament, colcon, humble, jazzy, kilted, lyrical, robotics, open-source]
---

**ROS 2** — the open-source **robotics middleware framework** that is the de-facto integration substrate for nearly all real-robot software in this wiki. Successor to ROS 1; built on DDS (Data Distribution Service) for pub/sub, services, and actions. Maintained by Open Robotics / Open Source Robotics Foundation. **New distribution released yearly on May 23rd (World Turtle Day)**; LTS distributions get ~5 years of support, non-LTS ~18 months.

## Current distributions (May 2026)

| Codename | Released | EOL | LTS? |
|---|---|---|---|
| **Lyrical Luth** | 2026-05-22 | May 2031 | (newest; status TBC) |
| Kilted Kaiju | 2025-05-23 | December 2026 | non-LTS |
| **Jazzy Jalisco** | 2024-05-23 | May 2029 | **LTS** |
| **Humble Hawksbill** | 2022-05-23 | May 2027 | **LTS** |

Cross-distribution communication is **not guaranteed** — a node on Humble may not interoperate with a node on Jazzy without explicit testing.

## Why it matters in this wiki

ROS 2 is the **control surface assumed by**:

- All Hiwonder educational kits: [ROSOrin](rosorin.md), [ROSOrin Pro](rosorin-pro.md) (both Humble).
- [Stretch](stretch.md) — Stretch 4 uses **ROS 2 Jazzy**.
- [TurtleBot 4](turtlebot.md) — Humble.
- [Reachy 2](reachy.md) — ROS 2 Humble.
- [PX4 Autopilot](px4-autopilot.md) — bridges to ROS 2 via uXRCE-DDS.

It is **not** the integration surface of the LeRobot platforms — [LeRobot](lerobot.md)'s middleware ([ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) §3.1) is built directly on FeeTech / Dynamixel SDKs and bypasses ROS 2 entirely. This is the gap that the **LeRobot↔ROS 2 bridges** ([Rosetta](rosetta.md), [lerobot-ros](lerobot-ros.md), [so101-ros2](so101-ros2.md)) close.

## Distribution split is operationally load-bearing

For LeRobot↔ROS 2 bridge compatibility:

| Bridge | Humble | Jazzy | Stance |
|---|---|---|---|
| [Rosetta](rosetta.md) | ✓ (distro-agnostic claimed) | ✓ | YAML contract layer |
| [lerobot-ros](lerobot-ros.md) | ✗ | ✓ (**only**) | Python sub-class layer |
| [so101-ros2](so101-ros2.md) | ✓ (**only**) | ✗ | SO-101 workspace |

A reader asking "can I run a LeRobot-trained policy on my Humble robot?" must check this matrix. [ROSOrin Pro](rosorin-pro.md) (Humble) → Rosetta or so101-ros2 (if SO-101). [Stretch 4](stretch.md) (Jazzy) → Rosetta or lerobot-ros.

## Key ecosystem pieces

- **DDS**: pub/sub middleware (default `rmw_fastdds_cpp` or `rmw_cyclonedds_cpp`).
- **ros2_control**: real-time control framework (used by [lerobot-ros](lerobot-ros.md), [so101-ros2](so101-ros2.md)).
- **[MoveIt 2](moveit.md)**: motion planning + kinematics (used for end-effector control in [lerobot-ros](lerobot-ros.md)).
- **[Nav2](nav2.md)**: autonomous navigation stack (used by every mobile robot in the wiki).
- **[Gazebo](gazebo.md)**: default open-source simulator.
- **rclpy / rclcpp**: Python and C++ client libraries.
- **rosbag2**: data recording (MCAP is the default modern container format).
- **Ament + colcon**: build tooling.
- **rmw_dds_common**: DDS abstraction layer.

## Related

- [LeRobot](lerobot.md) — non-ROS framework; bridged via [Rosetta](rosetta.md), [lerobot-ros](lerobot-ros.md), [so101-ros2](so101-ros2.md).
- [PX4 Autopilot](px4-autopilot.md) — UAV stack with first-class ROS 2 bridge.
- [Stretch AI](stretch-ai.md) / [OpenClaw](openclaw.md) (the latter via Hiwonder's [`openclaw_controller`](openclaw-controller.md) bridge) — LLM-agent stacks built on ROS 2.

## Mentioned in

- [ROS 2 Humble docs](../sources/ros2-humble-docs.md) — official documentation reference; primary source.
- [alfredang/lerobot — ChatGPT LeKiwi](../sources/alfredang-lerobot-lekiwi-chatgpt.md) — ROS 2 Humble (SLAM Toolbox + rplidar_ros) running in parallel with LeRobot on a LeKiwi, bridged to the control loop over HTTP rather than native topics.

## Open questions

- Lyrical Luth (2026-05-22) — LTS status not yet confirmed publicly.
- ROS 2 distribution Ubuntu pinning — only loosely "Humble = 22.04, Jazzy = 24.04" is the convention; would need per-distro install pages to confirm.
- Cross-distribution bridges (`ros2_bridge`-style tooling) — not yet ingested.
- ROS 1 → ROS 2 migration state in the robotics community — mostly complete in 2026 but residual ROS 1 still exists on legacy platforms.
