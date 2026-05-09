---
title: Sim-to-real transfer
type: concept
created: 2026-05-06
updated: 2026-05-08
sources: 8
tags: [sim-to-real, domain-gap, rl, simulation]
---

**Sim-to-real transfer** is the practice of training a robot policy in simulation and deploying it on a physical robot with little or no fine-tuning. The "reality gap" — differences between sim physics, sensor noise, lighting, dynamics — is the central obstacle.

## Why it matters
Real-robot data collection is slow and expensive. Simulation gives unlimited cheap training time. The whole agentic-robotics stack assumes that policies trained in simulators (Isaac Lab, MuJoCo Playground, Genesis, Genie Sim) will generalize to real robots — so the quality of sim-to-real determines whether simulation investment pays off.

## Common techniques
- **Domain randomization** — randomize physics, textures, lighting, friction in sim so the policy learns invariances.
- **Domain adaptation** — fine-tune on a small amount of real data after sim training.
- **High-fidelity rendering** — use photorealistic renderers (Omniverse RTX, Madrona) so vision-based policies see realistic input.
- **High-frequency physics** — match real-robot control rates (e.g. [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md)'s 1,000 Hz physics).
- **Vision pretraining on real images** — augment sim data with real video to anchor representations.

## Notable claims
- [MuJoCo Playground](../entities/mujoco-playground.md) demonstrates **zero-shot** transfer from both state and pixel inputs across quadrupeds, humanoids, hands, and arms ([MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)).
- Tesla Optimus combines sim-to-real with imitation from human teleoperated/wearable-camera video.

## Related
- [VLA models](vla-models.md) — the typical policy class undergoing sim-to-real.
- [World-model simulators](world-model-simulators.md) — sidesteps sim-to-real partially by training inside a learned model of reality.

## Mentioned in
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
