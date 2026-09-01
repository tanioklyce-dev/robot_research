---
title: Jeannette Bohg
type: entity
subtype: person
created: 2026-08-31
updated: 2026-08-31
sources: 2
tags: [jeannette-bohg, stanford, researcher, manipulation, dexterous-manipulation, failure-detection, sim-to-real]
---

**Jeannette Bohg** — Stanford professor working on robotic manipulation, and one of the field's central figures in grasping and contact-rich control. The [Sentinel](../sources/sentinel-paper.md) ingest flagged her as *"no page yet despite being a major manipulation-research"* figure; this closes that.

## In this wiki

| Work | Role | What it does |
|---|---|---|
| **[SimToolReal](../sources/simtoolreal-paper.md)** (Kedia, Lum, Bohg†, Liu†; RSS 2026) | equal advising | One RL policy on procedurally generated tool primitives, zero-shot to real tools. Reduces tool use to **goal-pose sequences**, removing per-task reward design. |
| **[Sentinel](../sources/sentinel-paper.md)** (Agia, Sinha, Yang, Cao, Antonova, Pavone, Bohg) | co-author | [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) for manipulation policies. |

## The through-line

Both works are about **what a policy cannot observe**. SimToolReal deliberately withholds detailed geometry and physics from the policy — giving it only a 6D pose and a coarse grasp bounding box — and lets an LSTM infer the rest from interaction, because those are the only quantities reliably measurable at deployment. Sentinel asks the complementary question: when the policy is failing, how would you know in time?

That pairing — **design for the observable, then detect when you are outside it** — is a more coherent research position than either paper states alone, and it is the same boundary the wiki's [belief-state](../concepts/world-models/belief-states-and-mixed-states.md) material approaches from theory.

## Related

- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md)
- [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md)
- **C. Karen Liu** — Stanford co-advisor on SimToolReal; no page yet.

## Mentioned in

- [SimToolReal paper](../sources/simtoolreal-paper.md)
- [Sentinel paper](../sources/sentinel-paper.md)
