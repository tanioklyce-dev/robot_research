---
title: NVIDIA Cosmos
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-10
sources: 7
tags: [cosmos, world-model, video-generation, nvidia, foundation-model]
---

NVIDIA's world foundation model and simulation platform for modeling physical environments at scale. Underpins downstream world-model simulators including [Genie Envisioner](genie-envisioner.md).

## Capabilities
- Generates physically-plausible video rollouts of dynamic scenes.
- Variants released as "Cosmos-Predict" series — e.g. Cosmos-Predict2-2B-Video2World powers [GE-Sim2](genie-envisioner.md).
- Used for autonomous-driving simulation, robot training, games, and metaverse applications requiring high-throughput simulation.
- Cosmos-Reason2-2B is the backbone of [GR00T N1.7](nvidia-groot.md).

## Why it matters
Cosmos is the underlying generative video model that's enabling the rise of [World-model simulators](../concepts/world-model-simulators.md) in agentic robotics — where the simulator is a learned model rather than a physics engine. Sits in **paradigmatic contrast** to the [JEPA](../concepts/jepa.md) / latent-prediction world-model line ([V-JEPA 2](v-jepa-2.md), [LeWorldModel](leworldmodel.md)) — Cosmos generates pixels; JEPA predicts representations.

## Related
- [Genie Envisioner](genie-envisioner.md) — built on Cosmos-Predict2.
- [NVIDIA](nvidia.md) — vendor.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — adjacent stack components for synthetic data.

## Mentioned in
- [AGIBOT Genie Envisioner 2.0 Announcement](../sources/agibot-genie-envisioner-2-announcement.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
