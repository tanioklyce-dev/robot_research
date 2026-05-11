---
title: XLeRobot Documentation
type: source
url: https://xlerobot.readthedocs.io/en/latest/
github: https://github.com/Vector-Wangel/XLeRobot
author: Gaotian "Vector" Wang (creator) + contributors
published: 2025-08 (v0.3.0)
ingested: 2026-05-10
tags: [low-cost-robotics, mobile-manipulator, dual-arm, lerobot, lekiwi, so-arm101, embodied-ai, open-source]
---

## Summary

**XLeRobot** is a $660 household dual-arm mobile manipulator designed to "bring embodied AI to every family." Built by Gaotian "Vector" Wang as a composition on top of the [LeRobot](../entities/lerobot.md) ecosystem: two [SO-ARM101](../entities/so-arm101.md) arms (~40 cm reach each) mounted on a [LeKiwi](../entities/lekiwi.md) holonomic base, with optional Raspberry Pi compute and RGB / RealSense depth cameras. 90% 3D-printed; under 4 hours assembly. Version 0.3.0 released August 30, 2025; documentation site is the canonical entry point. License: Apache 2.0.

The project's explicit positioning is *cheaper than an iPhone*, with capabilities the project says compare to $30,000+ commercial bimanual robots — albeit with sharp limitations (fixed height, low payload, no dexterous in-hand manipulation).

## Key claims

- **Hardware stack**:
  - Two SO-ARM101 arms, ~40 cm reach, 600–1000 g payload per arm
  - LeKiwi-class wheeled mobile base
  - 90% 3D-printed
  - Optional: RGB camera, stereo RGB, RealSense RGBD depth, Raspberry Pi
  - Assembly time: < 4 hours
- **Pricing**: $660 USD basic / ~€680 EU / ¥3999 CN / ₹87,000 IN. Developer assembly kit $579 worldwide (excluding battery and IKEA cart used as base). Taobao ¥3,699.
- **Software**: built on [LeRobot](../entities/lerobot.md) (Hugging Face). Multiple control interfaces: keyboard, Xbox controller, Switch Joycon, VR (Quest 3). ManiSkill simulation with URDF support. Imitation-learning + reinforcement-learning environments.
- **Capabilities claimed**: household chores, indoor tasks, plant care, delivery, manipulation roughly competitive with $30k+ commercial robots.
- **Limitations acknowledged**: fixed height (no lift platform), workspace smaller than Aloha-class, no in-hand dexterity, payload <1 kg, no dynamic motion.
- **Safety positioning**: low-torque motors limit physical harm potential — a deliberate design tradeoff for a household platform.
- **Community & ecosystem**: hardware tutorials on YouTube and Bilibili; active Discord; Embodied AI hackathon participation.
- **Lineage**: explicitly builds on [LeRobot](../entities/lerobot.md), [SO-100/SO-101](../entities/so-arm101.md) (The Robot Studio), [LeKiwi](../entities/lekiwi.md) (SIGRobotics-UIUC), and Bambot (Qian Tim).

## Entities mentioned

- [XLeRobot](../entities/xlerobot.md) — the project itself
- [Vector Wang](../entities/vector-wang.md) — creator (Gaotian Wang)
- [LeRobot](../entities/lerobot.md) — software framework
- [LeKiwi](../entities/lekiwi.md) — mobile base
- [SO-ARM101](../entities/so-arm101.md) — arm platform
- [The Robot Studio](../entities/the-robot-studio.md) — SO-ARM creators (referenced via SO-ARM101)
- [Hugging Face](../entities/hugging-face.md) — LeRobot maintainer
- [ManiSkill](../entities/maniskill.md) — simulation environment supported

## Concepts touched

- [Imitation learning](../concepts/imitation-learning.md) — primary learning paradigm
- [Assistive robotics](../concepts/assistive-robotics.md) — household manipulation tasks; positioned in the same affordable-platform space as [Stretch](../entities/stretch.md), [ROSOrin Pro](../entities/rosorin-pro.md), and similar
- [Sim-to-real transfer](../concepts/sim-to-real-transfer.md) — ManiSkill sim → real, RL sim2real (Zhuoyi Lu)

## Open questions

- Real-world performance data: the docs describe capabilities qualitatively but lack benchmark numbers. How does XLeRobot perform on standard household-manipulation benchmarks (e.g., RoboCasa365, BEHAVIOR-1K) where Stretch / OK-Robot / RUM have published numbers?
- Reliability and reproducibility: the $660 figure is striking, but does it hold for an end-user assembler, including failure recovery for 3D-printed parts?
- Comparison to [Stretch](../entities/stretch.md) (~$20k) as an assistive platform — XLeRobot is dual-arm and ~30× cheaper, but lacks Stretch's lift, sturdier mobile base, and integrated stack maturity. Specific tradeoffs deserve a synthesis.
