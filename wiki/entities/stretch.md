---
title: Stretch
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-17
sources: 13
tags: [stretch, mobile-manipulation, hello-robot, research-robot]
---

**Vendor:** [hello-robot.com](https://hello-robot.com/) — Stretch 3 product features at [hello-robot.com/stretch-3-whats-new](https://hello-robot.com/stretch-3-whats-new); purchase information at [hello-robot.com/purchase](https://hello-robot.com/purchase/).

Mobile-manipulation robot from [Hello Robot](hello-robot.md). Currently in third generation (Stretch 3). The de-facto research platform for academic mobile-manipulation work in 2024–2026.

## Capabilities
- Single-arm mobile manipulator: telescoping arm, mobile base, gripper, RealSense cameras, LiDAR.
- Modular tool-changer system.
- Software stacks: ROS 2 + [stretch_ai](stretch-ai.md) (Python; includes an LLM agent).
- Simulation: [MuJoCo](mujoco-playground.md) via "Stretch Mujoco" wrapper, plus Gazebo.

## Price
$20,000 ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)) — a fraction of PR2's $400,000. ~2 kg lift capacity; gripper based on inexpensive Amazon assistive tool.

## Notable use cases
- [Robot Utility Models](robot-utility-models.md) zero-shot generalist policies (NYU / Meta).
- [stretch_ai](stretch-ai.md) LLM agent for natural-language tasking.
- Cross-embodiment transfer (RUM transferred Stretch-trained policies to xArm 7 zero-shot).
- **[Open Vocabulary Mobile Manipulation (OVMM)](../sources/ovmm-homerobot.md)** — baseline platform (20% real-world success rate).
- **[OK-Robot](ok-robot.md)** — zero-shot pick-and-drop (58.5% success, 10 NYC homes); 1.8× over OVMM.
- **[Assistive use](../concepts/robotics/assistive-robotics.md)** — documented in-home use by Henry Evans (quadriplegic); scratching, laundry, meals, social play ([IEEE Spectrum, 2023](../sources/ieee-spectrum-stretch-assistive.md)). "Assistive autonomy" concept: user-directed via GUI, not fully autonomous.
- **[HCR Lab](hcrlab.md) long-term deployments** — [Maya Cakmak](maya-cakmak.md)'s lab ran 4-week summers deployments with Henry Evans in 2021, 2022, and 2023, expanding the task set each year. A prototype end-user programming (EUP) tool was built specifically for Henry in summer 2022 ([Maya Cakmak Research](../sources/maya-cakmak-research.md)).
- **EUP transfer to Stretch SE2** — HCR Lab's end-user robot programming tools have been ported to the commercial Hello Robot Stretch SE2.

## Related
- [Hello Robot](hello-robot.md) — vendor.
- [stretch_ai](stretch-ai.md) — primary software stack.
- [Robot Utility Models](robot-utility-models.md) — flagship policy framework targeting Stretch.

## Mentioned in
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [IEEE Spectrum — Stretch assistive robot](../sources/ieee-spectrum-stretch-assistive.md)
- [HomeRobot / OVMM](../sources/ovmm-homerobot.md)
- [OK-Robot Project Page](../sources/ok-robot-project-page.md)
- [Sense of Agency — Yang et al. 2025](../sources/yang2025-sense-of-agency.md)
- [Grasping in Clutter IVFP — Murray et al. 2024](../sources/murray2024-grasping-clutter-ivfp.md)
