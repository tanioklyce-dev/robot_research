---
title: ROSOrin Pro
type: entity
subtype: product
created: 2026-05-07
updated: 2026-07-04
sources: 4
tags: [rosorin-pro, hiwonder, jetson-orin-nano, education, mobile-manipulation, llm-agent]
---

**Hiwonder product page:** [hiwonder.com/products/rosorin-pro](https://www.hiwonder.com/products/rosorin-pro)

Educational mobile-manipulation robot kit from [Hiwonder](hiwonder.md) — the **6-DOF arm + mobile base** variant of [ROSOrin](rosorin.md). Same compute and chassis as the base kit; adds an HX-12H-servo arm with a gripper end-effector and ships upstream [OpenClaw](openclaw.md) as the LLM-agent brain, driven through Hiwonder's [`openclaw_controller`](openclaw-controller.md) ROS 2 bridge module.

## Hardware
- Compute: [Jetson Orin Nano](jetson-orin-nano.md) / NX (also Jetson Nano, Raspberry Pi 5).
- Chassis: differential-drive (Ackermann variant available); same as base [ROSOrin](rosorin.md). **A mecanum / omnidirectional (holonomic) chassis variant also ships** — confirmed on an owner's unit (reach-comparison photo in the [fleet framework synthesis](../syntheses/projects/fleet-agentic-framework.md)); which chassis you get depends on the kit SKU.
- **[6-DOF arm](rosorin-pro-arm.md)**: HX-12H bus servos with a gripper end-effector. **Swappable for an [SO-ARM101](so-arm101.md)** to make the arm LeRobot-native and homogenize a mixed fleet — see the [fleet framework](../syntheses/projects/fleet-agentic-framework.md) arm-swap decision (the 11.1 V 3S pack powers the 12 V STS3215 bus; drive it from the Jetson over a FeeTech USB adapter; add a wrist cam for observation-space parity).
- Sensors: COIN-D6 LiDAR (360°, 12 m), Deptrum Aurora930 depth + RGB camera (640×400 @ 12 fps), MPU6050 IMU, 6-microphone circular array, WonderEcho Pro voice module.
- Battery: 11.1 V 6000 mAh.
- Low-level MCU: STM32F407VET6.

## Curriculum delta from base ROSOrin
The Pro docs (`wiki.hiwonder.com/projects/rosorin-pro/...`) add three chapters relative to the base ROSOrin curriculum (`docs.hiwonder.com/projects/ROSOrin/...`):
- **Chapter 8** — ROS 2 Robotic Arm Control (basic control, deviation adjustment, 2D vision, 3D vision).
- **Chapter 11** — Group Control (multi-component coordination).
- **Chapter 13** — [OpenClaw](openclaw.md) Applications (the LLM-agent for manipulation).

Base-ROSOrin chapters (chassis, LiDAR, camera, mapping/nav, OpenCV, ML, Gazebo, voice, AI courses) are preserved with renumbering.

## Why it matters
First **manipulation-capable LLM-agent** example in the wiki on the educational tier. Confirms the [LLM-agent pattern](../concepts/agents/llm-agent-architecture.md) extends naturally from mobile-only ([ROSOrin](rosorin.md)) to mobile + arm — same JSON tool-call architecture, just a richer skill library.

## LeRobot integration path

ROSOrin Pro's [ROS 2](ros2.md)-native (Humble) control surface (`/joint_states`, `~/arm_group_control`, `/controller/cmd_vel`) makes it a natural target for the LeRobot↔ROS 2 bridges. **Distribution split matters**: ROSOrin Pro is Humble, so the viable bridges are [Rosetta](rosetta.md) (distro-agnostic, YAML contract) — **[lerobot-ros](lerobot-ros.md) is Jazzy-only and [so101-ros2](so101-ros2.md) is SO-101-only**, neither directly applies. See the [LeRobot-on-ROSOrin-Pro synthesis](../syntheses/projects/lerobot-on-rosorin-pro.md) for the concrete porting plan; Rosetta's shipped [`so_101.yaml`](https://github.com/iblnkn/rosetta/blob/main/contracts/so_101.yaml) (arm) + [`turtlebot3.yaml`](https://github.com/iblnkn/rosetta/blob/main/contracts/turtlebot3.yaml) (base) reference contracts cover both control axes between them.

## Related
- [Hiwonder](hiwonder.md) — vendor.
- [ROSOrin](rosorin.md) — mobile-only sibling kit.
- [ROSOrin Pro 6-DOF arm](rosorin-pro-arm.md) — manipulator hardware.
- [OpenClaw](openclaw.md) — LLM-agent framework that ships on this kit.
- [openclaw_controller](openclaw-controller.md) — Hiwonder's ROS 2 bridge module that exposes the kit's skills to OpenClaw.
- [Rosetta](rosetta.md) — LeRobot↔ROS 2 bridge; YAML-contract path to running [LeRobot](lerobot.md) policies on this platform.
- [Stretch](stretch.md) — research-tier arm + base counterpart from [Hello Robot](hello-robot.md).

## Mentioned in
- [Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md)
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)
