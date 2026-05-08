---
title: Stretch
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 4
tags: [stretch, mobile-manipulation, hello-robot, research-robot]
---

Mobile-manipulation robot from [Hello Robot](hello-robot.md). Currently in third generation (Stretch 3). The de-facto research platform for academic mobile-manipulation work in 2024–2026.

## Capabilities
- Single-arm mobile manipulator: telescoping arm, mobile base, gripper, RealSense cameras, LiDAR.
- Modular tool-changer system.
- Software stacks: ROS 2 + [stretch_ai](stretch-ai.md) (Python; includes an LLM agent).
- Simulation: [MuJoCo](mujoco-playground.md) via "Stretch Mujoco" wrapper, plus Gazebo.

## Notable use cases
- [Robot Utility Models](robot-utility-models.md) zero-shot generalist policies (NYU / Meta).
- [stretch_ai](stretch-ai.md) LLM agent for natural-language tasking.
- Cross-embodiment transfer demonstrations (RUM transferred Stretch-trained policies to xArm 7 zero-shot).

## Related
- [Hello Robot](hello-robot.md) — vendor.
- [stretch_ai](stretch-ai.md) — primary software stack.
- [Robot Utility Models](robot-utility-models.md) — flagship policy framework targeting Stretch.

## Mentioned in
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
