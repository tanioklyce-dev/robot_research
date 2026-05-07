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

Synthetic data-generation tool used by [[robocasa|RoboCasa]] / RoboCasa365 to scale human teleoperation demonstrations into much larger synthetic demo corpora. Original paper: Mandlekar et al., 2023.

## How it's used
- [[robocasa|RoboCasa365]] generated **1,615 hours** of synthetic demos from 612 hours of human teleop — a ~2.6× expansion ratio ([[robocasa365-paper|RoboCasa365 Paper]]).
- Enables benchmark scale (500K+ trajectories) without proportional human-teleop cost.
- One of the levers behind the practical viability of large benchmark suites in 2026 (alongside [[agibot-genie-sim|Genie Sim 3.0]]'s LLM-driven scene generation).

## Related
- [[robocasa|RoboCasa]] — primary downstream consumer.
- [[imitation-learning|Imitation learning]] — MimicGen expands demonstrations used for behavior cloning.

## Mentioned in
- [[robocasa365-paper|RoboCasa365 Paper]]
