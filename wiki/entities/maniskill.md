---
title: ManiSkill
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-06
sources: 1
tags: [maniskill, sapien, manipulation, hillbot, benchmark]
---

GPU-parallelized robotics simulator and manipulation benchmark led by [[hillbot|Hillbot]], Inc. (out of Hao Su's lab at UCSD). Built on the [[sapien|SAPIEN]] simulation framework. ManiSkill-HAB (December 2024) added a low-level implementation of the Home Assistant Benchmark.

## Capabilities
- [[sapien|SAPIEN]]-based GPU-parallel physics.
- Skill primitives (Pick, Place, Open, Close) chainable into long-horizon tasks (TidyHouse, PrepareGroceries, SetTable).
- Realistic low-level control (no "magic grasp" abstraction).
- >4,000 samples/sec on the HAB benchmark — about 3× Habitat 2.0 throughput.

## Related
- [[robocasa|RoboCasa]] — overlapping household-manipulation benchmark.
- [[sapien|SAPIEN]] — underlying simulator framework.
- [[hillbot|Hillbot]] — maintainer.

## Mentioned in
- [[maniskill-hab-paper|ManiSkill-HAB Paper]]
