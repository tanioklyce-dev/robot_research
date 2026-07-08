---
title: SO-ARM101 (SO-ARM100 lineage)
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-07-07
sources: 12
tags: [so-arm, so-arm100, so-arm101, the-robot-studio, low-cost-arm, open-source, lerobot, leader-follower, teleoperation]
---

**Open-source hardware:** [github.com/TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) — BOM, CAD, and firmware for both SO-ARM100 and SO-ARM101 designs. Apache 2.0.

**SO-ARM101** — open-source low-cost manipulator arm, successor to the **SO-ARM100** lineage from [The Robot Studio](the-robot-studio.md). The standard arm option across most LeRobot-compatible mobile manipulators in this wiki, including [LeKiwi](lekiwi.md) and [XLeRobot](xlerobot.md). Designed to be sourced primarily from off-the-shelf servos + 3D-printed brackets; supports **leader–follower teleoperation** (two arms wired together; the user moves the leader, the follower mirrors) — the canonical data-collection mode for the [LeRobot](lerobot.md) framework.

## Why it matters in this wiki

SO-ARM100/101 is the **dominant low-cost arm in the LeRobot ecosystem**. It plays an analogous role to what Franka Panda plays in the high-cost / research-lab tier:

| Tier | Arm | Typical cost | Default IL framework |
|---|---|---|---|
| Research lab | [Franka Panda](franka-panda.md) | $20k+ | research code (Diffusion Policy etc.) |
| Mid-cost integrated | [Stretch](stretch.md) | ~$20k | [Stretch AI](stretch-ai.md), LeRobot |
| **Low-cost open** | **SO-ARM101** | **sub-$500** | **[LeRobot](lerobot.md)** |
| Educational | [ROSOrin Pro arm](rosorin-pro-arm.md) | bundled in kit | OpenClaw |

Its low cost is the load-bearing assumption behind **[XLeRobot](xlerobot.md)**'s $660 dual-arm price point — two SO-ARM101s are the largest expense and still keep the total under $700.

## Variants in use

- **SO-ARM100** — original generation; commonly built around STS3215-class servos.
- **SO-ARM101** — current generation; default option for new LeRobot builds.
- **Dynamixel ROBOTIS Koch v1.1 + XL430 motors** — alternative arm available for [LeKiwi](lekiwi.md) for builders who prefer Dynamixel servos.

## Teleoperation pattern

In LeRobot deployments, SO-ARM101 is typically used in pairs:
- **Leader arm** — moved by the human; provides kinesthetic input and feedback
- **Follower arm** — mirrors the leader; performs the task

The leader-follower convention is the dominant data-collection pattern for imitation learning across [LeKiwi](lekiwi.md), [XLeRobot](xlerobot.md), and similar platforms.

## Related

- [The Robot Studio](the-robot-studio.md) — origin / design authority
- [LeRobot](lerobot.md) — primary software framework
- [FeeTech](feetech.md) — motor bus servo lineage
- [LeKiwi](lekiwi.md) — default mobile-base companion
- [XLeRobot](xlerobot.md) — dual-SO-ARM101 composition
- [Franka Panda](franka-panda.md) — research-tier counterpart
- [NexArm](nexarm.md) — Hiwonder's commercial leader-follower competitor (6-DOF, from $279.99; LeRobot-native)
- [Imitation learning](../concepts/learning/imitation-learning.md)

## Mentioned in

- [NVIDIA Isaac Teleop and GR00T 1.7 in LeRobot (HF blog)](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) — the reference platform for NVIDIA's first-party [GR00T](nvidia-groot.md) 1.7 fine-tune walkthrough (50-episode teleop → 20k-step fine-tune → rollout), incl. XR-headset teleop via [Isaac Teleop](nvidia-isaac-teleop.md).
- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [LeKiwi GitHub](../sources/lekiwi-github.md)
- [LeRobot Worldwide Hackathon 2025 — All Winners](../sources/lerobot-worldwide-hackathon-2025-winners.md) — SO-101 was prize hardware for the 25th–30th tier.
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — Table 1a price (~€225 single / €550 bimanual); confirms SO-101 ranks **top** for community-contributed datasets (3,965 datasets, 320K downloads, 58K episodes as of Sep 2025) and SO-100 (5,161 datasets, 279K downloads, 79K episodes). **Together SO-10X contributes 50%+ of all community datasets** in the LeRobotDataset format. Cited as Knight et al. 2024.
- [Rosetta GitHub](../sources/rosetta-github.md) — ships `so_101.yaml` (standard manipulator contract: 3 cameras + 6-joint follower state + leader-arm actions, MCAP storage) and `so_101_hil.yaml` (adds button-mapped intervention / success / failure / re-record + reward topic for HIL workflows).
- [lerobot-ros GitHub](../sources/lerobot-ros-github.md) — SO-101 is the simulated quickstart robot (Gazebo + MoveIt) for [lerobot-ros](lerobot-ros.md)'s generic ros2_control / MoveIt-Servo wrapper; ROS 2 Jazzy only.
- [so101_ros2 readthedocs](../sources/so101-ros2-readthedocs.md) — [so101-ros2](so101-ros2.md) is an SO-101-hardware-specific complete workspace (8 packages: URDF/USD, hardware interface, controllers, bringup, teleop, bridge, ros2_externals); MIT; ROS 2 Humble; ships **Isaac Sim 5.0+ integration** and tested SmolVLA + π0.5 deployment. **SO-101 is now the most-tooled platform in the LeRobot↔ROS 2 ecosystem** — all three bridges use it as their reference.

## Open questions / TBD

- Payload / reach / repeatability specs for SO-ARM101 (XLeRobot's "~40 cm reach, 600–1000 g payload" is the closest figure we have).
- The SO-ARM100 → SO-ARM101 delta isn't documented in the ingested sources.
- The Robot Studio's own documentation has not been ingested into this wiki; that would resolve the upstream-of-the-upstream questions.
