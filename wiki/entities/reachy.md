---
title: Reachy 2
type: entity
subtype: robot
created: 2026-05-09
updated: 2026-07-08
sources: 8
tags: [reachy, pollen-robotics, open-source, humanoid, embodied-ai, ros2, lerobot]
---

**Vendor product page:** [pollen-robotics.com/reachy](https://www.pollen-robotics.com/reachy/)

**Reachy 2** — open-source bimanual mobile manipulator from [Pollen Robotics](pollen-robotics.md) (France). "The first open-source humanoid robot specifically designed for the development of embodied AI and real-world applications." Torso-on-wheels form factor (not full bipedal); 7 DOF per arm; multiple variants from single-arm stationary to dual-arm + mobile base.

## Specs ([Pollen Robotics product page](../sources/pollen-robotics-reachy.md))
- Arms: 7 DOF each; human-arm proportions and dimensions
- Payload: 3 kg per arm
- Mobile base: three omniwheels + LiDAR + navigation sensors

## Variants
1. Dual Arm + Mobile Base (most capable)
2. Single Arm + Mobile Base
3. Dual Arm (stationary)
4. Single Arm (stationary)

## Software
- Python SDK; ROS 2 Humble
- VR teleoperation with camera feedback
- Fully open-source hardware + software
- CPU-powered; AI framework compatible

## Pricing
Not listed. Contact required.

## Position in the robot landscape
- **Open-source research humanoid** — rare class. Alternatives are mostly closed (Atlas, Figure, 1X NEO) or lower-DOF (Stretch, ROSOrin Pro).
- **Torso-on-wheels**, not full bipedal — different trade-off from Fauna Robotics Sprout (bipedal) and typical consumer humanoids.
- Positioned for embodied AI research — the same target as [V-JEPA 2-AC](v-jepa-2.md) and [LeWorldModel](leworldmodel.md) deployment experiments.
- Reachy Mini: smaller companion product with HuggingFace presence (content not retrieved in this ingest).

## Related
- [Pollen Robotics](pollen-robotics.md) — manufacturer
- [Fauna Robotics](fauna-robotics.md) — comparable positioning (developer humanoid platform)
- [Stretch](stretch.md) — comparable research-platform role, different form factor

## LeRobot integration

[LeRobot](lerobot.md) natively supports Reachy 2 as one of its 8 hardware platforms ([ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md), §3.1). Citation is **Mick et al. 2019** — the original "Reachy, a 3D-printed human-like robotic arm" paper from Frontiers in Neurorobotics.

As of the July 2026 NVIDIA↔HF partnership, NVIDIA announced **[Jetson Thor](jetson-thor.md) integration with Reachy 2** "to support deployment of VLA models on open source humanoid robots" ([NVIDIA blog, 2026-07-06](../sources/nvidia-hf-lerobot-open-robotics-blog.md)) — one sentence, no technical detail yet (reference image? LeRobot plugin?), but it makes Reachy 2 the named open-hardware deploy target for the Thor + LeRobot VLA stack. Notable given Reachy 2 shipped **CPU-powered** ([product page](../sources/pollen-robotics-reachy.md)) — Thor would be its first vendor-blessed GPU brain.

## Mentioned in
- [Reachy 2 product page](../sources/pollen-robotics-reachy.md)
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — Reachy-2 listed among 8 natively-supported platforms.
- [NVIDIA + HF LeRobot partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md) — Jetson Thor integration for VLA deployment.
