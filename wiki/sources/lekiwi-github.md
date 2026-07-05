---
title: LeKiwi GitHub Repository (SIGRobotics-UIUC/LeKiwi)
type: source
url: https://github.com/SIGRobotics-UIUC/LeKiwi
author: SIGRobotics-UIUC — Manav Chandaka, Bhargav Chandaka, Pepijn Kooijmans (CAD); Pepijn Kooijmans, Gloria Wang, Bhargav Chandaka, Advait Patel (software)
published: 2025 (rolling repo)
ingested: 2026-05-10
tags: [lekiwi, sigrobotics-uiuc, github, open-source, mobile-manipulator, kiwi-drive, raspberry-pi, so-arm101]
---

## Summary

The canonical open-source repository for **LeKiwi**, a low-cost mobile manipulator from SIGRobotics at UIUC. Apache 2.0. Includes CAD (Fusion 360), URDFs, BOM, assembly guides, and Python software for teleoperation, data collection, and streaming. 1,300+ GitHub stars, 138 forks, 95 commits, no formal release tags as of ingest (active development).

LeKiwi is structurally a 3-wheel holonomic Kiwi-drive base with a stacked-base-plate mounting convention (3.5 mm holes, 20 mm spacing) that hosts either an [SO-ARM101](../entities/so-arm101.md) arm or a [Dynamixel](../entities/dynamixel.md)/ROBOTIS Koch-v1.1 alternative. Designed for teleoperation, demonstration collection, and imitation-learning policy training within the [LeRobot](../entities/lerobot.md) ecosystem.

## Key claims

### Hardware design
- **Holonomic 3-wheel Kiwi drive** with omni wheels — omnidirectional movement
- **Dual camera system**: workspace + wrist-mounted RGB
- **Compute & power options**:
  - Primary controller: **Raspberry Pi 5**
  - Two power variants: **12V 5A Li-ion battery** OR **65 W laptop power bank (5V)**
  - Wireless streaming of joint angles + camera feeds to an external laptop for compute-offload
- **Arm**: standard configuration uses **SO-ARM101** (the open-source SO-ARM100 lineage from The Robot Studio); Dynamixel variant available with **ROBOTIS Koch v1.1 + XL430 motors**
- **Stacking convention**: 3.5 mm holes on 20 mm spacing — modular, mountable accessories follow open-hardware platform conventions

### Software
- Python; **LeRobot** integration
- Teleoperation: game controller, laptop (WASD), and a leader-arm with kinesthetic feedback
- Data collection pipeline for IL training
- URDF simulation models exported from the CAD

### Contributors (named in repo)
- **CAD**: Manav Chandaka, Bhargav Chandaka, Pepijn Kooijmans
- **Software**: Pepijn Kooijmans, Gloria Wang, Bhargav Chandaka, Advait Patel

### Community
- Active **Discord** presence on LeRobot's server, channel `#mobile-so100-arm`
- 6 open issues, 4 PRs at ingest (typical for an active small-team open-hardware repo)

### Build recommendations from repo
- **Beginner** → 5V version (laptop power bank, lighter)
- **Experienced builder** → 12V version (heavier payload, more torque)
- **Budget-conscious** → wired configuration (skips battery cost)

## Entities mentioned

- [LeKiwi](../entities/lekiwi.md)
- [SIGRobotics-UIUC](../entities/sigrobotics-uiuc.md)
- [LeRobot](../entities/lerobot.md)
- [SO-ARM101](../entities/so-arm101.md)
- [Hugging Face](../entities/hugging-face.md) — LeRobot maintainer
- [Raspberry Pi](https://www.raspberrypi.com/) (no entity page; foundational)

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — primary use case (data-collection → training pipeline)
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — fits the same low-cost mobile-manipulator slot occupied by [ROSOrin Pro](../entities/rosorin-pro.md) and (at higher cost) [Stretch](../entities/stretch.md)

## Open questions

- 1,300+ stars but no formal release tags — what's the stability story for downstream projects like [XLeRobot](../entities/xlerobot.md) that compose on top?
- SIGRobotics is a student organization; succession / maintenance risk worth tracking as the original contributors graduate.
- The Dynamixel/Koch v1.1 variant suggests dual-track hardware support; which is the recommended default in 2026?
