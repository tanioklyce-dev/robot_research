---
title: ManiSkill
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-08
sources: 2
tags: [maniskill, sapien, manipulation, hillbot, benchmark]
---

GPU-parallelized robotics simulator and manipulation benchmark led by [Hillbot](hillbot.md), Inc. (out of Hao Su's lab at UCSD). Built on the [SAPIEN](sapien.md) simulation framework. ManiSkill-HAB (December 2024) added a low-level implementation of the Home Assistant Benchmark.

## Capabilities
- [SAPIEN](sapien.md)-based GPU-parallel physics.
- Skill primitives (Pick, Place, Open, Close) chainable into long-horizon tasks (TidyHouse, PrepareGroceries, SetTable).
- Realistic low-level control (no "magic grasp" abstraction).
- >4,000 samples/sec on the HAB benchmark — about 3× Habitat 2.0 throughput.

## Related
- [RoboCasa](robocasa.md) — overlapping household-manipulation benchmark.
- [SAPIEN](sapien.md) — underlying simulator framework.
- [Hillbot](hillbot.md) — maintainer.

## Mentioned in
- [ManiSkill-HAB Paper](../sources/maniskill-hab-paper.md)
