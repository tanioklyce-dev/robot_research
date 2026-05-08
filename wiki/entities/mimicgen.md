---
title: MimicGen
type: entity
subtype: tool
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [mimicgen, synthetic-data, demonstrations, mandlekar]
status: stub
---

Synthetic data-generation tool used by [RoboCasa](robocasa.md) / RoboCasa365 to scale human teleoperation demonstrations into much larger synthetic demo corpora. Original paper: Mandlekar et al., 2023.

## How it's used
- [RoboCasa365](robocasa.md) generated **1,615 hours** of synthetic demos from 612 hours of human teleop — a ~2.6× expansion ratio ([RoboCasa365 Paper](../sources/robocasa365-paper.md)).
- Enables benchmark scale (500K+ trajectories) without proportional human-teleop cost.
- One of the levers behind the practical viability of large benchmark suites in 2026 (alongside [Genie Sim 3.0](agibot-genie-sim.md)'s LLM-driven scene generation).

## Related
- [RoboCasa](robocasa.md) — primary downstream consumer.
- [Imitation learning](../concepts/imitation-learning.md) — MimicGen expands demonstrations used for behavior cloning.

## Mentioned in
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
