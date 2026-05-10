---
title: Hello Robot
type: entity
subtype: company
created: 2026-05-07
updated: 2026-05-10
sources: 7
tags: [hello-robot, stretch, mobile-manipulation, research-platform]
---

Robotics company (Hello Robot, Inc., copyright 2020–2025) that builds [Stretch](stretch.md), a mobile-manipulation robot widely adopted as a research platform in the agentic-robotics community. Maintains the [stretch_ai](stretch-ai.md) open-source software stack including an LLM agent for natural-language tasking.

## What we know
- **Hardware**: [Stretch](stretch.md) (current generation: Stretch 3) — arm + mobile base + gripper + RealSense cameras + LiDAR. Price: $20,000.
- **Software**: dual-track — ROS 2 via tutorials, and Python via `stretch_body` / [stretch_ai](stretch-ai.md) ([Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)).
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
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [IEEE Spectrum — Stretch assistive robot](../sources/ieee-spectrum-stretch-assistive.md)
- [HomeRobot / OVMM](../sources/ovmm-homerobot.md)
