---
title: Genie Envisioner
type: entity
subtype: product
created: 2026-05-06
updated: 2026-08-08
sources: 10
tags: [genie-envisioner, world-model, agibot, cosmos, manipulation]
---

[AGIBOT](agibot.md)'s world-model simulator for embodied AI. Originally a unified world foundation platform for robotic manipulation (paper: 2025-08); evolved into Genie Envisioner 2.0 / GE-Sim2 — a fully interactive "world simulator" where robots can be trained inside a generative model rather than a physics engine.

> [!warning] Independently benchmarked, it comes last
> [WorldArena](worldarena.md) (Feb 2026) ranks Genie Envisioner **14th of 14** on EWMScore — **43.65**, seven points below 13th place — with the lowest instruction-following score in the field (0.2028 vs Veo 3.1's 0.9328) and near-lowest trajectory accuracy (0.0679). It scores **0% / 0%** on both of [WorldArena 2.0](../sources/worldarena-2-paper.md)'s visuotactile tasks, and 10%/20% as an action planner. The paper attributes this to "persistent gaps in long-horizon coherence and instruction compliance" in earlier text-conditioned embodied models.
>
> Everything below this callout comes from **AGIBOT's own announcements**. The gap between the two records is large, and the wiki's standing pattern is that [vendor world-model claims have not once survived independent measurement](../syntheses/world-models/what-world-models-are-measurably-good-for.md). Caveats worth stating on the other side: WorldArena post-trains every model on RoboTwin 2.0 following official implementations, which may disadvantage a system tuned for AGIBOT's own hardware, and it evaluated the original GE rather than GE-Sim2.

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

- [WorldArena paper](../sources/worldarena-paper.md) — last of 14 on EWMScore.
- [WorldArena 2.0 paper](../sources/worldarena-2-paper.md) — 0% on both visuotactile tasks.
