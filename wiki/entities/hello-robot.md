---
title: Hello Robot
type: entity
subtype: company
created: 2026-05-07
updated: 2026-05-07
sources: 4
tags: [hello-robot, stretch, mobile-manipulation, research-platform]
---

Robotics company (Hello Robot, Inc., copyright 2020–2025) that builds [[stretch|Stretch]], a mobile-manipulation robot widely adopted as a research platform in the agentic-robotics community. Maintains the [[stretch-ai|stretch_ai]] open-source software stack including an LLM agent for natural-language tasking.

## What we know
- **Hardware**: [[stretch|Stretch]] (current generation: Stretch 3) — arm + mobile base + gripper + RealSense cameras + LiDAR.
- **Software**: dual-track — ROS 2 via tutorials, and Python via `stretch_body` / [[stretch-ai|stretch_ai]] ([[hello-robot-stretch-docs|Hello Robot Stretch Documentation]]).
- **Adoption signal**: [[robot-utility-models|Robot Utility Models]] (NYU/Meta) chose Stretch as the primary platform for zero-shot generalist policies; Aaron Edsinger (Hello Robot co-founder, ex-MIT/Meka Robotics) is a co-author on the RUM paper ([[robot-utility-models-website|Robot Utility Models Project Page]]).
- **Agentic AI**: ships an LLM agent in [[stretch-ai|stretch_ai]] supporting Qwen2.5, Gemma, GPT-4o-mini ([[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]).

## Why it matters
Hello Robot fills a niche the NVIDIA-centric simulation stack doesn't: **affordable, real-world, mobile-manipulation hardware that academic researchers can actually deploy**. Sim-trained policies need a target platform, and the agentic-robotics community has converged on Stretch.

## Related
- [[stretch|Stretch]] — the robot.
- [[stretch-ai|stretch_ai]] — the software stack.
- [[robot-utility-models|Robot Utility Models]] — major external project using Stretch.

## Mentioned in
- [[hello-robot-stretch-docs|Hello Robot Stretch Documentation]]
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]
- [[robot-utility-models-website|Robot Utility Models Project Page]]
- [[robot-utility-models-paper|Robot Utility Models Paper]]
