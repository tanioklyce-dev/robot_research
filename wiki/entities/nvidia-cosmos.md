---
title: NVIDIA Cosmos
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 4
tags: [cosmos, world-model, video-generation, nvidia, foundation-model]
---

NVIDIA's world foundation model and simulation platform for modeling physical environments at scale. Underpins downstream world-model simulators including [[genie-envisioner|Genie Envisioner]].

## Capabilities
- Generates physically-plausible video rollouts of dynamic scenes.
- Variants released as "Cosmos-Predict" series — e.g. Cosmos-Predict2-2B-Video2World powers [[genie-envisioner|GE-Sim2]].
- Used for autonomous-driving simulation, robot training, games, and metaverse applications requiring high-throughput simulation.
- Cosmos-Reason2-2B is the backbone of [[nvidia-groot|GR00T N1.7]].

## Why it matters
Cosmos is the underlying generative video model that's enabling the rise of [[world-model-simulators|World-model simulators]] in agentic robotics — where the simulator is a learned model rather than a physics engine. Sits in **paradigmatic contrast** to the [[jepa|JEPA]] / latent-prediction world-model line ([[v-jepa-2|V-JEPA 2]], [[leworldmodel|LeWorldModel]]) — Cosmos generates pixels; JEPA predicts representations.

## Related
- [[genie-envisioner|Genie Envisioner]] — built on Cosmos-Predict2.
- [[nvidia|NVIDIA]] — vendor.
- [[nvidia-isaac-sim|NVIDIA Isaac Sim]] / [[nvidia-isaac-lab|NVIDIA Isaac Lab]] — adjacent stack components for synthetic data.

## Mentioned in
- [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]
- [[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]]
