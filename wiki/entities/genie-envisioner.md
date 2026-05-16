---
title: Genie Envisioner
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-16
sources: 7
tags: [genie-envisioner, world-model, agibot, cosmos, manipulation]
---

[AGIBOT](agibot.md)'s world-model simulator for embodied AI. Originally a unified world foundation platform for robotic manipulation (paper: 2025-08); evolved into Genie Envisioner 2.0 / GE-Sim2 — a fully interactive "world simulator" where robots can be trained inside a generative model rather than a physics engine.

## Capabilities
- World Action Model (WAM) framework: action is a first-class variable in the model.
- Robots simulate `state → action → next state` rollouts inside a learned environment.
- Built on `nvidia/Cosmos-Predict2-2B-Video2World` (uses [NVIDIA Cosmos](nvidia-cosmos.md)).
- Minute-scale stable simulation: full task sequences, not fragmented clips.
- Positioned as a "physical evolution engine" for embodied AI.

## Why it matters
Most prominent example of the [World-model simulators](../concepts/world-models/world-model-simulators.md) paradigm in agentic robotics: training environments are generated rather than authored. Reduces dependence on physics engines for high-level skill learning, but real-world task fidelity is still being validated.

## Related
- [AGIBOT](agibot.md) — maintainer.
- [NVIDIA Cosmos](nvidia-cosmos.md) — underlying generative video model.
- [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) — companion physics-based simulator from the same vendor.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — concept page.

## Mentioned in
- [AGIBOT Genie Envisioner 2.0 Announcement](../sources/agibot-genie-envisioner-2-announcement.md)
- [Genie Envisioner Paper](../sources/genie-envisioner-paper.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
