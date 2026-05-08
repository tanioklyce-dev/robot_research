---
title: RoboCasa
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 2
tags: [robocasa, household-manipulation, benchmark, ut-austin, nvidia, iclr-2026, mimicgen]
---

Large-scale simulation framework for training and benchmarking generalist robots on everyday household tasks. Originally released in 2024 by Nasiriany et al. at UT Austin; expanded to **RoboCasa365** (ICLR 2026) by the same group with [NVIDIA](nvidia.md) Research co-authorship via Yuke Zhu's dual UT Austin / NVIDIA appointment. Authors of RoboCasa365: Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu.

## Capabilities (RoboCasa365)
- **365 tasks** spanning **60 distinct kitchen activities**: manipulation, semantic reasoning, long-horizon planning, memory-dependent.
- **2,500 unique kitchen scenes** modeled from real US kitchens.
- **3,200+ object library** plus 2,200+ interactive fixtures.
- **2,200+ hours of robot interaction data**: 612 hr human teleop + 1,615 hr synthetic via [MimicGen](mimicgen.md) (~2.6× expansion).
- **500K+ trajectories** in the released dataset.
- Three benchmark suites: multi-task learning, foundation-model training, lifelong learning.

## Cross-references in JEPA work
- [JEPA-WMs](jepa-wms.md) (Terver et al., FAIR, Dec 2025) trains and evaluates on **RoboCasa kitchen manipulation** alongside Metaworld + DROID + real Franka — making this the first JEPA-for-robotics paper in the wiki to use heavy sim. See [paper](../sources/jepa-wms-paper.md) and [revised synthesis](../syntheses/why-jepa-research-skips-the-simulator-stack.md).

## Related
- [MimicGen](mimicgen.md) — synthetic data generator powering RoboCasa365's demo expansion.
- [ManiSkill](maniskill.md) — overlapping manipulation benchmark space.
- [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) — newer, larger benchmark with comparable focus.
- [NVIDIA](nvidia.md) — co-authoring institution via Yuke Zhu.
- [JEPA-WMs](jepa-wms.md) — uses RoboCasa as a JEPA-WM evaluation environment.

## Mentioned in
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
