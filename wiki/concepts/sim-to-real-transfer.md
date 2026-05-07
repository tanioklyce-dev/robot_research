---
title: Sim-to-real transfer
type: concept
created: 2026-05-06
updated: 2026-05-07
sources: 4
tags: [sim-to-real, domain-gap, rl, simulation]
---

**Sim-to-real transfer** is the practice of training a robot policy in simulation and deploying it on a physical robot with little or no fine-tuning. The "reality gap" — differences between sim physics, sensor noise, lighting, dynamics — is the central obstacle.

## Why it matters
Real-robot data collection is slow and expensive. Simulation gives unlimited cheap training time. The whole agentic-robotics stack assumes that policies trained in simulators (Isaac Lab, MuJoCo Playground, Genesis, Genie Sim) will generalize to real robots — so the quality of sim-to-real determines whether simulation investment pays off.

## Common techniques
- **Domain randomization** — randomize physics, textures, lighting, friction in sim so the policy learns invariances.
- **Domain adaptation** — fine-tune on a small amount of real data after sim training.
- **High-fidelity rendering** — use photorealistic renderers (Omniverse RTX, Madrona) so vision-based policies see realistic input.
- **High-frequency physics** — match real-robot control rates (e.g. [[agibot-genie-sim|AGIBOT Genie Sim 3.0]]'s 1,000 Hz physics).
- **Vision pretraining on real images** — augment sim data with real video to anchor representations.

## Notable claims
- [[mujoco-playground|MuJoCo Playground]] demonstrates **zero-shot** transfer from both state and pixel inputs across quadrupeds, humanoids, hands, and arms ([[mujoco-playground-paper|MuJoCo Playground Paper]]).
- Tesla Optimus combines sim-to-real with imitation from human teleoperated/wearable-camera video.

## Related
- [[vla-models|VLA models]] — the typical policy class undergoing sim-to-real.
- [[world-model-simulators|World-model simulators]] — sidesteps sim-to-real partially by training inside a learned model of reality.

## Mentioned in
- [[mujoco-playground-paper|MuJoCo Playground Paper]]
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]
- [[robocasa365-paper|RoboCasa365 Paper]]
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
