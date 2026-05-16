---
title: MimicGen
type: entity
subtype: tool
created: 2026-05-07
updated: 2026-05-15
sources: 2
tags: [mimicgen, synthetic-data, demonstrations, mandlekar, gear]
status: stub
---

Synthetic data-generation tool used by [RoboCasa](robocasa.md) / RoboCasa365 to scale human teleoperation demonstrations into much larger synthetic demo corpora. Original paper: **MimicGen** (Mandlekar et al., CoRL 2023, arxiv 2310.17596) — **Outstanding Paper Award**. Authored under [NVIDIA GEAR](nvidia-gear.md) ([GEAR Publications](../sources/nvidia-gear-publications.md)).

## How it's used
- [RoboCasa365](robocasa.md) generated **1,615 hours** of synthetic demos from 612 hours of human teleop — a ~2.6× expansion ratio ([RoboCasa365 Paper](../sources/robocasa365-paper.md)).
- Enables benchmark scale (500K+ trajectories) without proportional human-teleop cost.
- One of the levers behind the practical viability of large benchmark suites in 2026 (alongside [Genie Sim 3.0](agibot-genie-sim.md)'s LLM-driven scene generation).

## Related
- [RoboCasa](robocasa.md) — primary downstream consumer.
- [NVIDIA GEAR](nvidia-gear.md) — originating research lab.
- [Imitation learning](../concepts/learning/imitation-learning.md) — MimicGen expands demonstrations used for behavior cloning.

## Mentioned in
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md)
