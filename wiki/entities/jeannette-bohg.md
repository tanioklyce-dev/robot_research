---
title: Jeannette Bohg
type: entity
subtype: person
created: 2026-08-31
updated: 2026-08-31
sources: 5
tags: [jeannette-bohg, stanford, researcher, manipulation, dexterous-manipulation, failure-detection, sim-to-real]
---

**Jeannette Bohg** — Stanford professor working on robotic manipulation, and one of the field's central figures in grasping and contact-rich control. The [Sentinel](../sources/sentinel-paper.md) ingest flagged her as *"no page yet despite being a major manipulation-research"* figure; this closes that.

## In this wiki

| Work | Role | What it does |
|---|---|---|
| **[SimToolReal](../sources/simtoolreal-paper.md)** (Kedia, Lum, Bohg†, Liu†; RSS 2026) | equal advising | One RL policy on procedurally generated tool primitives, zero-shot to real tools. Reduces tool use to **goal-pose sequences**, removing per-task reward design. |
| **[Sentinel](../sources/sentinel-paper.md)** (Agia, Sinha, Yang, Cao, Antonova, Pavone, Bohg) | co-author | [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) for manipulation policies. |
| **[Robot-Powered Data Flywheels](../sources/robot-powered-data-flywheels-paper.md)** (Grannen, Pan, Llontop, Ho, Zolotas, Bohg, [Sadigh](dorsa-sadigh.md); 2025) | co-author | **Scanford** in the East Asia Library for two weeks: the robot self-labels against the library catalog, lifting a VLM 32.4→71.8% on book ID and 24.8→46.6% on *general* English OCR. |
| **[Causal-PIK](../sources/causal-pik-paper.md)** (Parés-Morlans, Yi, Chen, Wu, Antonova, Gerstenberg, Bohg; ICML 2025) | senior author | Physics intuition inside a **GP kernel**: rank actions by *causal-effect similarity*, not geometric proximity. Beats SOTA and (at generous budgets) humans on PHYRE / Virtual Tools. |

## Two prescriptions, unreconciled

SimToolReal argues real demonstration data is the **wrong** path for dexterity and generates synthetic coverage instead; Data Flywheels argues real deployment data is **precisely** what foundation models lack. Both Bohg-advised, three months apart. The implied reconciliation — *synthetic for control, real for perception* — is stated by neither paper.

## The through-line

Both works are about **what a policy cannot observe**. SimToolReal deliberately withholds detailed geometry and physics from the policy — giving it only a 6D pose and a coarse grasp bounding box — and lets an LSTM infer the rest from interaction, because those are the only quantities reliably measurable at deployment. Sentinel asks the complementary question: when the policy is failing, how would you know in time?

That pairing — **design for the observable, then detect when you are outside it** — is a more coherent research position than either paper states alone, and it is the same boundary the wiki's [belief-state](../concepts/world-models/belief-states-and-mixed-states.md) material approaches from theory.

## Related

- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md)
- [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md)
- **C. Karen Liu** — Stanford co-advisor on SimToolReal; no page yet.

## Mentioned in
- [Third World Modeling Workshop, Chicago Booth 2026](../sources/chicago-booth-world-modeling-workshop-2026.md) — invited talk (SimToolReal, Causal-PIK) and panel, incl. the counterfactual argument for training world models on **failures** rather than curated successes.

- [SimToolReal paper](../sources/simtoolreal-paper.md)
- [Sentinel paper](../sources/sentinel-paper.md)
- [Robot-Powered Data Flywheels paper](../sources/robot-powered-data-flywheels-paper.md)
- [Causal-PIK paper](../sources/causal-pik-paper.md)
