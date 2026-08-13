---
title: VoxPoser
type: entity
subtype: system
created: 2026-08-03
updated: 2026-08-03
sources: 1
tags: [voxposer, code-as-policy, value-maps, motion-planning, stanford, manipulation]
---

**VoxPoser** — a zero-shot manipulation system (Stanford/UIUC, CoRL 2023) in which an LLM writes code that **composes 3D voxel value maps** — reward at the target, cost near obstacles — which a model-based motion planner optimizes into dense 6-DoF trajectories ([paper](../sources/voxposer-paper.md)).

## The move it makes
VoxPoser keeps the LLM writing code but changes the **output type**: from a sequence of primitive calls to an *objective function in observation space*. This escapes [Code as Policies](../sources/code-as-policies-paper.md)' dependence on someone having pre-defined the right motion primitive — the ceiling CaP itself named in its limitations.

## Headline numbers
- **Real world, 5 tasks x 10 trials:** 88% without disturbance, **70% with** — against a CaP-style primitives baseline at 24% and **0% under disturbance**.
- **Simulated, 13 tasks / 2,766 instructions / 20 episodes each:** beats both a U-Net costmap learner and the CaP-style baseline in **all six** seen/unseen cells, staying roughly flat across them.
- **Dynamics learning:** zero-shot trajectories as exploration priors reach 80–92% on door/window/fridge in **under 3 minutes** of online interaction, versus exceeding a 12-hour budget without priors.
- **Lowest specification error** of the methods compared; most residual real-world failure is **perception**.

## Related
- [Code as Policies](../sources/code-as-policies-paper.md) — the baseline and the limitation targeted.
- [Language to Rewards](../sources/language-to-rewards-paper.md) — sibling "write the objective" paper, same conference; rewards instead of value maps.
- [CaP-X](cap-x.md) — the 2026 framework that measures the primitive-abstraction axis rather than routing around it.
- [Wenlong Huang](wenlong-huang.md) / [Fei-Fei Li](fei-fei-li.md) — first and senior author.
- [Code as policy](../concepts/agents/code-as-policy.md) — the concept.

## Mentioned in
- [VoxPoser paper](../sources/voxposer-paper.md) — primary source.
- [Introducing Waddle](../sources/waddle-labs-introducing-waddle.md) — cited in Waddle's lineage survey as a model-writes-intermediate-structure variant.
