---
title: Safety-CHORES
type: entity
subtype: benchmark
created: 2026-09-07
updated: 2026-09-07
sources: 2
tags: [safety-chores, benchmark, safe-rl, vla, ai2thor, procthor, objaverse, mobile-manipulation, safety-evaluation]
---

# Safety-CHORES

A **safety-instrumented embodied benchmark** for vision-language-action policies: long-horizon navigation-plus-manipulation tasks in procedurally generated indoor scenes, with **formally specified unsafe behaviors** scored alongside task success. Introduced with [SafeVLA](../sources/safevla-paper.md) (NeurIPS 2025 Spotlight); built on the [AI2](ai2.md) stack — **AI2-THOR** simulator, **150K ProcTHOR** scenes, **800K Objaverse** assets.

The wiki's first ingested benchmark that scores safety and task performance **together**. Everything else in its [policy-evaluation](../concepts/robotics/robot-policy-evaluation.md) coverage reports success rate.

## Tasks

- **Safety-ObjNav** — navigate through multiple rooms to locate a designated object.
- **Safety-PickUp** — starting in front of a surface, pick up a specified object.
- **Safety-Fetch** — navigate to find the object, then pick it up. The hard one; costs run 5–6× the other two.

Instructions are natural language, with the goal object category sampled per episode.

## The five safety-critical components

The design idea is that a benchmark for safety has to **elicit** unsafe behavior, not merely permit it — so specific environmental features and object arrangements are deliberately instantiated:

| Component | Unsafe behavior | Predicate type |
|---|---|---|
| **Corners** | navigating into confined space, getting stuck or repeatedly colliding | state-action |
| **Blind spots** | colliding with an obstacle **previously seen but not currently observed** — a short-term spatial-memory failure | trajectory |
| **Fragile collections** | collateral damage to nearby fragile items during manipulation | trajectory |
| **Critical points** | destabilizing a precariously placed object (a knife on an edge) so it falls | trajectory |
| **Dangerous equipment** | prohibited interaction with intrinsically hazardous objects — active stovetops, exposed wiring | state-action |

Two of the five — blind spots and critical points — are only expressible as **trajectory-level** predicates, over a temporal pattern rather than a single state-action pair. That is the design detail worth keeping: it lets "hit something it had seen thirty steps ago" be a first-class, attributable violation.

## Metric

**Cumulative cost (CC)** — the sum, over an episode, of all violations across all constraint types, with each violation costing 1. Reported next to **success rate (SR)**. Costs are **binary and unweighted**: destabilizing a knife and clipping a corner score identically. The authors state severity weighting as future work, on the grounds that severity is context-dependent.

> [!warning] It measures collisions, not forces
> Every predicate is a **discrete event with simulator ground truth** — a collision, a fall, a prohibited interaction. There is no wrench, no force envelope, no contact-mode reasoning. Safety-CHORES is the field's most-cited VLA safety benchmark and it does **not** address the gap the [contact-rich survey](../sources/safe-learning-contact-rich-survey.md) names as its first future direction: *there is no standardized contact-force evaluation protocol.* By that survey's own definition the tasks here are not even [contact-rich](../concepts/robotics/contact-rich-manipulation.md) — navigation, plus pick-and-place whose contacts are fixed after the grasp.
>
> This is a scope statement, not a fault. Collision-and-clutter safety in cluttered homes is a real hazard class and nothing else measures it.

## Why the benchmark, not the algorithm, may be the contribution

SafeVLA's own ablation: run the **identical** alignment recipe in simplified one-room scenes without the safety-critical components and cumulative cost goes **1.854 → 5.01**, worse than the reward-shaping baseline, with success falling 0.865 → 0.645. And under identical measurement, cumulative cost on Safety-CHORES runs **more than 2×** that on iTHOR or ProcTHOR for the same models — standard benchmarks do not surface these failures because nothing in them is built to.

**A constrained optimizer can only constrain behaviors it observes.** That makes the elicitation environment load-bearing, and makes Safety-CHORES the part of that paper most likely to outlast it.

## Availability

Data, models and the environment at `pku-safevla.github.io` (per the paper; not independently verified here).

## Related

- [SafeVLA](../sources/safevla-paper.md) — the paper that introduces it.
- [Safety-Gymnasium](safety-gymnasium.md) — **the direct predecessor**, from the same group: same CMDP framing, same co-reported reward/cost metric, and the same constraint vocabulary moved one step toward embodiment — **speed thresholds and regions there, collisions and fragile-object displacement here, forces in neither**. Its stated future work, *"transferring policy refined within the Safety-Gymnasium to physical robotic platforms,"* is what Safety-CHORES attempts; both are simulation-only.
- [PKU-Alignment](pku-alignment.md) — the group; also authors of Safety-Gymnasium and Safe-RLHF.
- [Allen Institute for AI](ai2.md) — AI2-THOR, ProcTHOR, Objaverse, and the SPOC/FLaRe/PoliFormer models it benchmarks against.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — where cumulative cost and the extreme-failure protocol belong.
- [Safe reinforcement learning](../concepts/learning/safe-reinforcement-learning.md) — the paradigm it exists to measure.

## Mentioned in

- [SafeVLA paper](../sources/safevla-paper.md)
