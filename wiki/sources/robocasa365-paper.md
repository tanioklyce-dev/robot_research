---
title: RoboCasa365 Paper
type: source
url: https://openreview.net/forum?id=tQJYKwc3n4
local_path: raw/22486_RoboCasa365_A_Large_Scal.pdf
author: Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu
affiliations: UT Austin, NVIDIA Research
published: 2026 (ICLR 2026 conference paper)
ingested: 2026-05-06
updated: 2026-05-07
tags: [robocasa, household-manipulation, benchmark, simulation, iclr-2026, mimicgen]
---

## Summary
ICLR 2026 conference paper introducing RoboCasa365 — a large-scale simulation benchmark for training and benchmarking generalist household robots, built on top of the existing [RoboCasa](../entities/robocasa.md) platform. From UT Austin and [NVIDIA](../entities/nvidia.md) Research (Yuke Zhu has dual affiliation).

## Key claims
- **365 tasks across 60 distinct kitchen activities**: manipulation, semantic reasoning, long-horizon planning, memory-dependent.
- **2,500 unique kitchen scenes** modeled from real US kitchens.
- **3,200+ object library**, with 2,200+ interactive fixtures.
- **2,200+ hours of robot interaction data**: 612 hours human teleoperation + 1,615 hours synthetic (≈2.6× synthetic-to-human expansion).
- **500K+ trajectories** in the released dataset.
- Synthetic data generated via [MimicGen](../entities/mimicgen.md) (Mandlekar et al., 2023).
- Three benchmark suites: multi-task learning, robot foundation-model training, lifelong learning.
- Designed to be **policy-agnostic** — assesses model classes rather than promoting one architecture. References Octo, TRI LBM, and others as comparison points.
- Predecessor: [RoboCasa](../entities/robocasa.md) (Nasiriany et al., 2024) — same group, smaller scale (100k demos / 30 tasks / 100 scenes).
- Project URL: https://robocasa.ai

## Entities mentioned
- [RoboCasa](../entities/robocasa.md)
- [MimicGen](../entities/mimicgen.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- [Sim-to-real transfer](../concepts/sim-to-real-transfer.md)
- [Imitation learning](../concepts/imitation-learning.md) / synthetic demo expansion
- Generalist robot foundation models
- Multi-task and lifelong learning

## Open questions
- Top model performance on the 365-task suite — not derived from the abstract; need to read results section in the PDF.
- Does the 2.6× synthetic ratio plateau? More synthetic isn't always better.
- TRI LBM and Octo are referenced as baselines — what's their relative ranking on this benchmark?
