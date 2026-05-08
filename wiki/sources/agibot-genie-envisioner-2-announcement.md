---
title: AGIBOT Genie Envisioner 2.0 Announcement
type: source
url: https://www.therobotreport.com/agibot-unveils-genie-envisioner-2-0-advance-world-models-scalable-simulators-embodied-ai/
author: The Robot Report
published: 2026
ingested: 2026-05-06
tags: [agibot, world-model, genie-envisioner, cosmos]
---

## Summary
Announcement of [Genie Envisioner](../entities/genie-envisioner.md) 2.0 (GE-Sim2) from [AGIBOT](../entities/agibot.md) — an evolution of world models from passive observers into interactive "world simulators" that can train, evaluate, and optimize robot policies inside a model-generated environment, reducing reliance on real-world trial and error.

## Key claims
- Introduces the World Action Model (WAM) framework: action is treated as a first-class variable in the model.
- Robots simulate `state → action → next state` rollouts inside a generative environment.
- Built on `nvidia/Cosmos-Predict2-2B-Video2World` — i.e., layered on top of [NVIDIA Cosmos](../entities/nvidia-cosmos.md).
- Supports minute-scale stable simulation: full task sequences, not fragmented clips.
- Positioned as a "physical evolution engine" for embodied AI.

## Entities mentioned
- [AGIBOT](../entities/agibot.md)
- [Genie Envisioner](../entities/genie-envisioner.md)
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md)

## Concepts touched
- [World-model simulators](../concepts/world-model-simulators.md)
- World Action Model framework
- Generative-model-based training environments

## Open questions
- What's the fidelity ceiling for policies trained purely inside the world-model rollout?
- How well does GE-Sim2 handle out-of-distribution tasks vs. those near the training video distribution?
- Does it replace or complement physics-engine training?
