---
title: Hello Robot
type: entity
subtype: company
created: 2026-05-07
updated: 2026-05-25
sources: 9
tags: [hello-robot, stretch, mobile-manipulation, research-platform]
---

Robotics company (Hello Robot, Inc., copyright 2020–2025) that builds [Stretch](stretch.md), a mobile-manipulation robot widely adopted as a research platform in the agentic-robotics community. Maintains the [stretch_ai](stretch-ai.md) open-source software stack including an LLM agent for natural-language tasking.

## What we know
- **Hardware**: [Stretch](stretch.md). **Current generation: Stretch 4** (launched 2026-05-12, **$29,950 base**; +$2,495 for optional Jetson Orin NX AI accelerator) — see [Stretch 4 launch source](../sources/hello-robot-stretch-4-launch.md) + [Stretch 4 datasheet](../sources/hello-robot-stretch-4-datasheet.md). Major upgrades over Stretch 3: new omnidirectional holonomic base (top 60 cm/s, 20 mm step clearance), dual Hesai J128 hemispherical 3D LiDAR, dual Luxonis OAK-FFC AR0234 (2.3 MP global-shutter RGB) + Luxonis OAK-FFC IMX378 (12 MP) head cameras + Luxonis OAK-D SR wrist depth (4 TOPs), 3DOF cobot-style ambidextrous wrist with 310° per axis, 9-DOF (or "8 redundant + gripper"), ~2× faster motion, +10% reach, 8 hr runtime with self-charging dock, 24 V Feetech RS485 tool bus, 6× Pixart cliff curtains, dedicated head Runstop button.
- **Software**: dual-track — ROS 2 (Stretch 4 ships **ROS 2 Jazzy**; Stretch 3 was Humble) via tutorials, and Python via `stretch_body` / [stretch_ai](stretch-ai.md) ([Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)). Stretch Body @ 100 Hz with MuJoCo-based self-collision avoidance on Stretch 4.
- **Key people**: **Aaron Edsinger** (co-founder, ex-MIT/Meka Robotics) — co-author on the RUM paper; **Charlie Kemp** (Georgia Tech) — Robots for Humanity initiative co-founder, close research collaborator; **Vy Nguyen** — occupational therapist at Hello Robot ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)).
- **Agentic AI**: ships an LLM agent in [stretch_ai](stretch-ai.md) supporting Qwen2.5, Gemma, GPT-4o-mini ([Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)).
- **Assistive use**: documented deployment with Henry Evans (quadriplegic), reducing caregiver burden and restoring user agency ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)).
- **Research benchmarks**: HomeRobot/OVMM baseline (20% real success), OK-Robot (58.5% success in 10 NYC homes).

## Why it matters
Hello Robot fills a niche the NVIDIA-centric simulation stack doesn't: **affordable, real-world, mobile-manipulation hardware that academic researchers can actually deploy**. Sim-trained policies need a target platform, and the agentic-robotics community has converged on Stretch.

## Related
- [Stretch](stretch.md) — the robot.
- [stretch_ai](stretch-ai.md) — the software stack.
- [Robot Utility Models](robot-utility-models.md) — major external project using Stretch.

## Mentioned in
- [Stretch 4 Datasheet (Rev 5, As Launched)](../sources/hello-robot-stretch-4-datasheet.md) — canonical Stretch 4 spec sheet (2026-05-12).
- [Stretch 4 launch — Hello Robot purchase + product + forum announcement](../sources/hello-robot-stretch-4-launch.md) — Stretch 4 launch reference (2026-05-12).
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [IEEE Spectrum — Stretch assistive robot](../sources/ieee-spectrum-stretch-assistive.md)
- [HomeRobot / OVMM](../sources/ovmm-homerobot.md)
