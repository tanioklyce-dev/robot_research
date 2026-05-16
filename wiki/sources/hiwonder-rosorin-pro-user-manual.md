---
title: Hiwonder ROSOrin Pro User Manual
type: source
url: https://wiki.hiwonder.com/projects/rosorin-pro/en/latest/docs/1_ROSOrin_Pro_User_Manual.html
author: Hiwonder
published: 2024-2025
ingested: 2026-05-07
tags: [hiwonder, rosorin-pro, user-manual, hardware-specs, jetson-orin-nano, manipulation]
---

## Summary
Chapter 1 hardware reference for [Hiwonder](../entities/hiwonder.md)'s **[ROSOrin Pro](../entities/rosorin-pro.md)** — a 6-DOF arm + mobile-base variant of [ROSOrin](../entities/rosorin.md). Same compute platform options ([Jetson Orin Nano](../entities/jetson-orin-nano.md)/NX, Jetson Nano, Raspberry Pi 5) and the same STM32F407VET6 low-level MCU as the base kit; adds an HX-12H-servo arm with a gripper end-effector. Note: ROSOrin Pro docs live on a different subdomain (`wiki.hiwonder.com`) than the base ROSOrin docs (`docs.hiwonder.com`).

## Key claims

### Sensors
- LiDAR: **COIN-D6**, 360° scanning, 12 m radius (black objects), 9.5–10.5 Hz scan, 0.9° angular resolution.
- Depth camera: **Deptrum Aurora930**, 3D structured light, 640×400 @ 12 fps, 15–300 cm working range. NV12 RGB integrated in the same module.
- IMU: **MPU6050**, 3-axis accelerometer + 3-axis gyroscope, I2C.
- Audio: "AI voice interaction box" referenced — same WonderEcho Pro / 6-microphone array architecture as the base ROSOrin docs.

### Manipulator arm ([6-DOF arm](../entities/rosorin-pro-arm.md))
- 6 degrees of freedom.
- Joint actuation: **HX-12H** bus servos — 0–240° rotation, 12 kg·cm stall torque @ 11.0 V, 0.2 s/60° speed.
- Gripper controlled by the same HX-12H servo class.
- Specific arm dimensions, reach, and payload **not stated in the manual**.

### Compute & software
- Controller options:
  - Jetson Nano — Ubuntu 18.04, ROS Melodic + ROS 2 Humble in Docker.
  - Jetson Orin Nano / Orin NX — Ubuntu 22.04, ROS 2 Humble.
  - Raspberry Pi 5 — Debian 12.
- Low-level MCU: **STM32F407VET6**, 168 MHz, 512 KB Flash, 192 KB SRAM.

### Power
- 11.1 V 6000 mAh lithium battery.
- 12.6 V charging voltage; ~3 hr charge from 10 V.
- Low-voltage warning at <10 V (buzzer "beep-beep-beep").
- Charger-only charging; do not charge while powered on.

## Entities mentioned
- [Hiwonder](../entities/hiwonder.md)
- [ROSOrin Pro](../entities/rosorin-pro.md)
- [ROSOrin Pro 6-DOF arm](../entities/rosorin-pro-arm.md)

## Concepts touched
- Mobile manipulation (no concept page yet — bare text)

## Open questions
- Overall robot dimensions, weight, max speed, payload — not consolidated in the manual.
- Arm reach / workspace / payload — only servo-level numbers (12 kg·cm torque per joint).
- "AI voice interaction box" — confirm this is the WonderEcho Pro from base ROSOrin docs.
