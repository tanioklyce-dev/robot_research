---
title: MimicGen
type: entity
subtype: tool
created: 2026-05-07
updated: 2026-11-10
sources: 6
tags: [mimicgen, synthetic-data, demonstrations, mandlekar, gear]
---

Synthetic data-generation tool used by [RoboCasa](robocasa.md) / RoboCasa365 to scale human teleoperation demonstrations into much larger synthetic demo corpora. Original paper: **MimicGen** (Mandlekar et al., CoRL 2023, arxiv 2310.17596) — **Outstanding Paper Award**. Authored under [NVIDIA GEAR](nvidia-gear.md) ([GEAR Publications](../sources/nvidia-gear-publications.md)).

## DexMimicGen
**DexMimicGen** is the bimanual/dexterous extension used by [GR00T N1](../sources/groot-n1-paper.md): it multiplies a few dozen human demos into **780,000 trajectories ≈ 6,500 hours (nine person-months of demonstration) in 11 hours**, and provides one of GR00T's three sim benchmarks (9 bimanual tasks, 3 embodiments). The most aggressive demo-multiplication ratio documented in the wiki.

**Real-robot figures, per NVIDIA** ([R²D² digest](../sources/nvidia-r2d2-dexterous-robots-blog.md)). The DexMimicGen paper generated 21,000 demonstrations from 60 human ones. A real humanoid reached 90% on can sorting with generated data, against 0% with human data alone. **SkillMimicGen** adapts contact-rich skill segments from about three annotated demonstrations and links them with motion planning, reaching 35% zero-shot sim-to-real on a nut assembly task.

## How it's used
- [RoboCasa365](robocasa.md) generated **1,615 hours** of synthetic demos from 612 hours of human teleop — a ~2.6× expansion ratio ([RoboCasa365 Paper](../sources/robocasa365-paper.md)).
- [GR00T N1](../sources/groot-n1-paper.md) pre-training: 540k DexMimicGen demos under RoboCasa (GR-1 embodiment) = 1,742.6 h — the "simulation" middle layer of the data pyramid.
- Enables benchmark scale (500K+ trajectories) without proportional human-teleop cost.
- One of the levers behind the practical viability of large benchmark suites in 2026 (alongside [Genie Sim 3.0](agibot-genie-sim.md)'s LLM-driven scene generation).

## Related
- [RoboCasa](robocasa.md) — primary downstream consumer.
- [NVIDIA GEAR](nvidia-gear.md) — originating research lab.
- [Imitation learning](../concepts/learning/imitation-learning.md) — MimicGen expands demonstrations used for behavior cloning.

## Mentioned in
- [GR00T N1 Paper](../sources/groot-n1-paper.md) (DexMimicGen)
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md)
- [R²D²: dexterous robots](../sources/nvidia-r2d2-dexterous-robots-blog.md) — DexMimicGen 90% vs 0% real; SkillMimicGen.
