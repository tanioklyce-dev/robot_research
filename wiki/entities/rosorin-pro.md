---
title: ROSOrin Pro
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [rosorin-pro, hiwonder, jetson-orin-nano, education, mobile-manipulation, llm-agent]
---

Educational mobile-manipulation robot kit from [[hiwonder|Hiwonder]] — the **6-DOF arm + mobile base** variant of [[rosorin|ROSOrin]]. Same compute and chassis as the base kit; adds an HX-12H-servo arm with a gripper end-effector and ships [[openclaw|OpenClaw]] as the manipulation-aware LLM-agent framework.

## Hardware
- Compute: Jetson Orin Nano / NX (also Jetson Nano, Raspberry Pi 5).
- Chassis: differential-drive (Ackermann variant available); same as base [[rosorin|ROSOrin]].
- **[[rosorin-pro-arm|6-DOF arm]]**: HX-12H bus servos with a gripper end-effector.
- Sensors: COIN-D6 LiDAR (360°, 12 m), Deptrum Aurora930 depth + RGB camera (640×400 @ 12 fps), MPU6050 IMU, 6-microphone circular array, WonderEcho Pro voice module.
- Battery: 11.1 V 6000 mAh.
- Low-level MCU: STM32F407VET6.

## Curriculum delta from base ROSOrin
The Pro docs (`wiki.hiwonder.com/projects/rosorin-pro/...`) add three chapters relative to the base ROSOrin curriculum (`docs.hiwonder.com/projects/ROSOrin/...`):
- **Chapter 8** — ROS 2 Robotic Arm Control (basic control, deviation adjustment, 2D vision, 3D vision).
- **Chapter 11** — Group Control (multi-component coordination).
- **Chapter 13** — [[openclaw|OpenClaw]] Applications (the LLM-agent for manipulation).

Base-ROSOrin chapters (chassis, LiDAR, camera, mapping/nav, OpenCV, ML, Gazebo, voice, AI courses) are preserved with renumbering.

## Why it matters
First **manipulation-capable LLM-agent** example in the wiki on the educational tier. Confirms the [[llm-agent-architecture|LLM-agent pattern]] extends naturally from mobile-only ([[rosorin|ROSOrin]]) to mobile + arm — same JSON tool-call architecture, just a richer skill library.

## Related
- [[hiwonder|Hiwonder]] — vendor.
- [[rosorin|ROSOrin]] — mobile-only sibling kit.
- [[rosorin-pro-arm|ROSOrin Pro 6-DOF arm]] — manipulator hardware.
- [[openclaw|OpenClaw]] — manipulation-aware LLM-agent framework that ships with this kit.
- [[stretch|Stretch]] — research-tier arm + base counterpart from [[hello-robot|Hello Robot]].

## Mentioned in
- [[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]]
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]
