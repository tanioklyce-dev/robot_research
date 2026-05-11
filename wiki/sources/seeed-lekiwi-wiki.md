---
title: Seeed Studio LeRobot LeKiwi Wiki / Tutorial
type: source
url: https://wiki.seeedstudio.com/lerobot_lekiwi/
author: Seeed Studio (distributor) — content based on SIGRobotics-UIUC LeKiwi designs + Hugging Face LeRobot framework
published: 2025-06 (verified against LeRobot stable release of 2025-06-05)
ingested: 2026-05-10
tags: [lekiwi, lerobot, mobile-manipulator, imitation-learning, seeed-studio, raspberry-pi-5, so-arm101, tutorial]
---

## Summary

Seeed Studio's tutorial and product page for the **LeKiwi** mobile manipulator, an end-to-end build/use guide for the LeKiwi platform sold through Seeed's bazaar. Covers BOM, assembly (11 major steps), system requirements, software install, motor calibration, teleoperation, data collection, ACT policy training, and autonomous evaluation. Seeed is the **commercial distributor** of LeKiwi hardware; SIGRobotics-UIUC is the design authority; Hugging Face owns the LeRobot framework.

This is one of the cleaner end-to-end "buy → assemble → train → deploy" tutorials available for a sub-$1k research-grade mobile manipulator running an open-source IL stack.

## Key claims

### Hardware spec
- **3× STS3215 servo motors** (12V, 1:345 gear ratio) — base drive
- **12-bit magnetic encoders**
- **3× omnidirectional wheels** (Kiwi-drive holonomic base)
- Motor control board with USB-C interface; UART protocol
- 12V DC power required; optional power supply or user-provided battery
- Operating temperature: 0–40 °C
- 3D-printed chassis: PLA+, 0.2 mm layer height, 15% infill, 150 mm/s

### Compute paths
- **Onboard**: Raspberry Pi 5 (4–16 GB RAM), Python 3.10, PyTorch 2.6
- **Training / evaluation**: x86 with CUDA 12+ or Jetson Orin with JetPack 6.0+; Ubuntu 22.04; Python 3.10, PyTorch 2.6

### Optional add-ons in BOM
- Raspberry Pi 5
- USB camera, depth camera
- **SO-ARM101** robotic arm (the manipulator that turns this from a base into a mobile manipulator)
- 12V lithium-ion battery

### Software pipeline (the seven canonical LeRobot steps)
1. Install — Miniconda + LeRobot dependencies
2. Motor configuration — port detection, motor ID assignment
3. Calibration — joint ranges for leader + follower arms
4. Teleoperation — leader-arm remote control, keyboard for mobile base
5. Data collection — record demonstrations for IL
6. Training — **ACT (Action Chunking with Transformers)** policy
7. Evaluation — autonomous task execution

### Distribution model
- Manufacturer / hardware design: **SIGRobotics-UIUC**
- Hardware sales: **Seeed Studio** bazaar ("Get One Now" links)
- Software framework: **Hugging Face** (LeRobot)
- Wiki content: hosted by Seeed Studio on their wiki platform

## Entities mentioned

- [LeKiwi](../entities/lekiwi.md)
- [LeRobot](../entities/lerobot.md)
- [SIGRobotics-UIUC](../entities/sigrobotics-uiuc.md)
- [Seeed Studio](../entities/seeed-studio.md)
- [Hugging Face](../entities/hugging-face.md)
- [SO-ARM101](../entities/so-arm101.md)

## Concepts touched

- [Imitation learning](../concepts/imitation-learning.md) — ACT (Action Chunking Transformer) is the recommended default policy class for LeRobot tasks; this tutorial is one of the most-followed entry points for IL practitioners outside of Stretch / Franka.
- [Assistive robotics](../concepts/assistive-robotics.md) — at sub-$1k for the base + arm, LeKiwi is among the cheapest mobile-manipulator platforms usable for accessible-robotics research.

## Open questions

- The tutorial caveats "Hugging Face has released significant framework updates; users should consult official documentation for latest features" — i.e., LeRobot moves fast and the Seeed tutorial may lag the framework. How current is it as of mid-2026?
- ACT is referenced as the default; would [Diffusion Policy](../entities/diffusion-policy.md), [VQ-BeT](../entities/vq-bet.md), or [BET](../entities/bet.md) (all already in this wiki) work equally well on LeKiwi? No benchmark comparisons in the tutorial.
