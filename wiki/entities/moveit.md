---
title: MoveIt
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 4
tags: [moveit, moveit2, ros2, motion-planning, kinematics, ompl, picknik, manipulation, lerobot-ros]
---

**MoveIt** — the **motion-planning and kinematics stack for [ROS 2](ros2.md)**. Maintained by PickNik Robotics. Provides forward / inverse kinematics, collision checking, motion planning (via OMPL + others), trajectory execution, and real-time servoing (**MoveIt Servo**). The canonical answer to "how do I plan and execute a Cartesian-space motion on a ROS 2 arm?" Current generation is **MoveIt 2** (the ROS 2-native rewrite of the ROS 1 MoveIt). Home: [moveit.ai](https://moveit.ai/).

## Why it matters in this wiki

- **`lerobot-ros` exposes MoveIt Servo as a first-class control mode.** [ycheng517/lerobot-ros](lerobot-ros.md) supports `ActionType.CARTESIAN_VELOCITY` via [`moveit_servo`](https://moveit.picknik.ai/main/doc/examples/realtime_servo/realtime_servo_tutorial.html), one of three control modes ([lerobot-ros GitHub](../sources/lerobot-ros-github.md)). This is the Cartesian end-effector path for any ros2_control + MoveIt arm; the joint-position / joint-trajectory modes don't need MoveIt.
- **The standard motion-planning layer on top of ros2_control.** ros2_control handles real-time joint-level command/feedback; MoveIt sits above it for kinematics and planning. Together they're the dominant ROS 2 arm-control stack.
- **Used in `nanavati2025-feeding-out-of-lab.md`** (Stretch RE1 with WonderfulShop Kinova-class arm) and **`elephant-robotics-mybuddy-280.md`** (myBuddy 280 dual-arm desktop bot ships ROS 1 + MoveIt).

## Quick relationships

| Layer | Role | Example |
|---|---|---|
| **MoveIt** | High-level motion planning, kinematics, MoveIt Servo for real-time EE control | `lerobot-ros` Cartesian mode |
| **ros2_control** | Real-time joint command + feedback abstraction | `joint_trajectory_controller`, `position_controllers` |
| **DDS** | Pub/sub middleware | Fast DDS, Cyclone DDS |

## Related

- [ROS 2](ros2.md) — the middleware MoveIt is built on.
- [lerobot-ros](lerobot-ros.md) — uses MoveIt Servo for end-effector velocity control.
- [so101-ros2](so101-ros2.md) — uses MoveIt for SO-101 motion planning (per readthedocs nav).
- [Nav2](nav2.md) — sibling stack on the mobile-base side (analogous role for navigation).

## Mentioned in

- [lerobot-ros GitHub](../sources/lerobot-ros-github.md) — MoveIt 2 + MoveIt Servo are required for Cartesian end-effector control mode.
- [so101_ros2 readthedocs](../sources/so101-ros2-readthedocs.md) — used in the SO-101 controller stack.
- [Elephant Robotics myBuddy 280](../sources/elephant-robotics-mybuddy-280.md) — ROS 1 + MoveIt as the canonical motion-planning stack.
- [Nanavati 2025 — feeding out of lab](../sources/nanavati2025-feeding-out-of-lab.md) — assistive-feeding system uses MoveIt for motion planning.

## Open questions / TBD

- **Direct ingest of MoveIt 2 docs / tutorials** would let us cite specific algorithm choices (OMPL planners, CHOMP, STOMP) and the MoveIt Servo control loop architecture.
- **PickNik Robotics** — the company maintaining MoveIt — has no entity page; worth one if their other tooling becomes relevant.
- The **MoveIt 1 → MoveIt 2 migration story** — most of the open-source robotics world made this jump in 2022–2024; specific lessons for the wiki's mobile-manipulation focus not yet captured.
