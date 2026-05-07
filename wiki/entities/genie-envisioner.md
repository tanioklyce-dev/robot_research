---
title: Genie Envisioner
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 4
tags: [genie-envisioner, world-model, agibot, cosmos, manipulation]
---

[[agibot|AGIBOT]]'s world-model simulator for embodied AI. Originally a unified world foundation platform for robotic manipulation (paper: 2025-08); evolved into Genie Envisioner 2.0 / GE-Sim2 — a fully interactive "world simulator" where robots can be trained inside a generative model rather than a physics engine.

## Capabilities
- World Action Model (WAM) framework: action is a first-class variable in the model.
- Robots simulate `state → action → next state` rollouts inside a learned environment.
- Built on `nvidia/Cosmos-Predict2-2B-Video2World` (uses [[nvidia-cosmos|NVIDIA Cosmos]]).
- Minute-scale stable simulation: full task sequences, not fragmented clips.
- Positioned as a "physical evolution engine" for embodied AI.

## Why it matters
Most prominent example of the [[world-model-simulators|World-model simulators]] paradigm in agentic robotics: training environments are generated rather than authored. Reduces dependence on physics engines for high-level skill learning, but real-world task fidelity is still being validated.

## Related
- [[agibot|AGIBOT]] — maintainer.
- [[nvidia-cosmos|NVIDIA Cosmos]] — underlying generative video model.
- [[agibot-genie-sim|AGIBOT Genie Sim 3.0]] — companion physics-based simulator from the same vendor.
- [[world-model-simulators|World-model simulators]] — concept page.

## Mentioned in
- [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]
- [[genie-envisioner-paper|Genie Envisioner Paper]]
