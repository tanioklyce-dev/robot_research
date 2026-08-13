---
title: AGIBOT Genie Sim 3.0
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 3
tags: [agibot, genie-sim, embodied-ai, isaac-sim, scene-generation]
---

Open-source embodied-AI simulation platform from [AGIBOT](agibot.md), unveiled at CES 2026. Built on top of [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / Omniverse, with LLM-driven scene generation and a large evaluation suite for [VLA models](../concepts/learning/vla-models.md).

## Capabilities
- Decoupled physics + rendering; physics up to 1,000 Hz.
- Massively parallel simulation for high data throughput.
- **LLM-driven scene generation**: describe an environment in natural language, get structured scenes plus thousands of semantic variations.
- "Spatial world model" generates interactive 3D environments from text or image inputs.
- Built-in reward signals → closed-loop training and evaluation.
- 100,000+ evaluation scenarios.
- 10,000+ hours of synthetic dataset including real-world robot operation scenarios.
- Benchmarks support [GR00T](nvidia-groot.md) series, Pi series, and GO-2 series.
- Fully open source: assets, datasets, evaluation code on GitHub.

## Why it matters
Combines a research-grade evaluation harness (largest open embodied-AI dataset, 100k+ scenarios) with practical LLM-driven authoring — making it one of the most complete open stacks for benchmarking [VLA models](../concepts/learning/vla-models.md) in 2026.

## Related
- [AGIBOT](agibot.md) — maintainer.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — runtime substrate.
- [Genie Envisioner](genie-envisioner.md) — companion world-model project from AGIBOT.

## Mentioned in
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [ManiSkill-HAB Paper](../sources/maniskill-hab-paper.md)
