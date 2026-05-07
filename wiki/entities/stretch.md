---
title: Stretch
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 3
tags: [stretch, mobile-manipulation, hello-robot, research-robot]
---

Mobile-manipulation robot from [[hello-robot|Hello Robot]]. Currently in third generation (Stretch 3). The de-facto research platform for academic mobile-manipulation work in 2024–2026.

## Capabilities
- Single-arm mobile manipulator: telescoping arm, mobile base, gripper, RealSense cameras, LiDAR.
- Modular tool-changer system.
- Software stacks: ROS 2 + [[stretch-ai|stretch_ai]] (Python; includes an LLM agent).
- Simulation: [[mujoco-playground|MuJoCo]] via "Stretch Mujoco" wrapper, plus Gazebo.

## Notable use cases
- [[robot-utility-models|Robot Utility Models]] zero-shot generalist policies (NYU / Meta).
- [[stretch-ai|stretch_ai]] LLM agent for natural-language tasking.
- Cross-embodiment transfer demonstrations (RUM transferred Stretch-trained policies to xArm 7 zero-shot).

## Related
- [[hello-robot|Hello Robot]] — vendor.
- [[stretch-ai|stretch_ai]] — primary software stack.
- [[robot-utility-models|Robot Utility Models]] — flagship policy framework targeting Stretch.

## Mentioned in
- [[hello-robot-stretch-docs|Hello Robot Stretch Documentation]]
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]
- [[robot-utility-models-website|Robot Utility Models Project Page]]
