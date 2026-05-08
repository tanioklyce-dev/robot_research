---
title: ManiSkill-HAB Paper
type: source
url: https://arxiv.org/abs/2412.13211
author: Hillbot / Hao Su lab (UCSD)
published: 2024-12
ingested: 2026-05-06
tags: [maniskill, sapien, manipulation, benchmark, hab]
---

## Summary
ArXiv paper introducing MS-HAB — a GPU-accelerated implementation of the Home Assistant Benchmark (HAB) inside [ManiSkill](../entities/maniskill.md), focused on low-level manipulation chains for home rearrangement tasks.

## Key claims
- Provides skill primitives (Pick, Place, Open, Close) chained for long-horizon HAB tasks: TidyHouse, PrepareGroceries, SetTable.
- Achieves >4,000 samples/sec — about 3× Habitat 2.0 throughput at a fraction of the GPU memory.
- Realistic low-level control (vs. "magic grasp" abstractions used by older HAB implementations).

## Entities mentioned
- [ManiSkill](../entities/maniskill.md)
- [Hillbot](../entities/hillbot.md)
- [SAPIEN](../entities/sapien.md)

## Concepts touched
- Long-horizon manipulation chains
- GPU-parallelized benchmark execution
- Low-level vs. high-level action abstractions

## Open questions
- How does MS-HAB compare in throughput to [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md) or [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)?
- VLA model leaderboard on the suite?
