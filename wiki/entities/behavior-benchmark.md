---
title: BEHAVIOR / BEHAVIOR-1K
type: entity
subtype: benchmark
created: 2026-07-04
updated: 2026-08-03
sources: 6
tags: [behavior, behavior-1k, benchmark, household, simulation, omnigibson, bddl, stanford, sim-to-real]
---

**BEHAVIOR-1K** — Stanford's **human-centered household-activity benchmark**: **1,000 everyday activities** grounded in **50 scenes** with **9,000+ objects**, simulated in **[OmniGibson](omnigibson.md)** (NVIDIA Omniverse + PhysX 5). Its signature is that activity selection is **survey-grounded** (1,461 people ranked what they want robots to do), and it simulates what most benchmarks can't — deformables, fluids, and extended states (temperature, soaked, cooked, sliced). Primary source: [BEHAVIOR-1K Paper](../sources/behavior-1k-paper.md) (arXiv 2403.09227, CoRL 2022). In this wiki it is the **hard end of the [sim-to-real gap](../concepts/learning/sim-to-real-transfer.md)** — the long-horizon, real-household yardstick.

## The benchmark
- **1,000 activities** (909 top survey-ranked + 91 from BEHAVIOR-100), **50 scenes** (houses/stores/restaurants/offices), **9,000+ object instances / 1,900+ categories** (2,964 leaf synsets).
- **BDDL (BEHAVIOR Domain Definition Language)** — predicate-logic task defs (initial + goal conditions, semantic not geometric), e.g. `food is cooked and onTop of a plate`.
- **Survey-grounded**: 1,461 respondents ranked 2,090 activities; tedious tasks (scrub the bathroom floor) rank highest — the "human-centered" claim.

## Why it's hard (the numbers)
Long-horizon (CollectTrash ≥16 steps) + deformables/fluids + extended states. Baselines ([paper](../sources/behavior-1k-paper.md)): **end-to-end visuomotor RL scores 0.0**; PPO + motion primitives reaches 0.42–0.77; + observation history 0.55–0.88. Real robot (TIAGo bimanual): ~40% sim → ~22% optimal → **0% trained-vision**. Physics-based grasping is decisive.

> [!note] The 12.4% number vs the paper baselines
> The widely-cited **12.4% BEHAVIOR-1K full-task success** ([AI Index 2026](../sources/stanford-hai-ai-index-2026.md), the "89.4% RLBench vs 12.4% BEHAVIOR-1K" gap) is the **2025 BEHAVIOR-1K Challenge** winner — a *later, separate* result from the paper's own 0%–22% baselines. Both say the same thing: real-household long-horizon manipulation is far from solved.

## Why it matters in this wiki
- **The canonical "how far are we really" yardstick** for household manipulation — cited whenever a controlled-benchmark result needs puncturing.
- **A GR00T data substrate**: [GR00T N1.6](../sources/groot-n1_6.md) trains on **simulated [Galaxea R1 Pro](galaxea-r1.md) on the BEHAVIOR suite**.
- Its BDDL + extended-state simulation is what *learned* world-model sims still can't reproduce (fluids, temperature, cooking).

## Related
- [OmniGibson](omnigibson.md) — the simulator BEHAVIOR-1K runs in (its own entity).
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — BEHAVIOR-1K is the hard end of the gap.
- [Galaxea R1](galaxea-r1.md) — the robot GR00T N1.6 runs on the BEHAVIOR suite (sim).
- [RoboCasa](robocasa.md), [Metaworld](metaworld.md), [LIBERO](libero.md) — peer manipulation benchmarks (RoboCasa is the closest — kitchen-scale).
- [Roberto Martín-Martín](roberto-martin-martin.md) — co-author.

## Mentioned in
- [BEHAVIOR-1K Paper](../sources/behavior-1k-paper.md) — **primary source**.
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md) — the 12.4% challenge figure.
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — simulated Galaxea R1 Pro on BEHAVIOR.
- [CaP-X paper](../sources/cap-x-paper.md) — 50 BEHAVIOR tasks integrated into CaP-Gym; CaP-Agent0 exceeds the human expert on radio-pickup task success (56% vs 36%, n=25).
- [ASPIRE paper](../sources/aspire-paper.md) — long-horizon mobile manipulation; ASPIRE beats both human experts and CaP-Agent0 (radio task success 56% → 88%).

## Open questions
- **Primary source now ingested** ([paper](../sources/behavior-1k-paper.md)); the earlier stub's "5,000 objects" is corrected to **9,000+**.
- Relationship to **BEHAVIOR-100** (iGibson 2.0; 100 activities) and the **iGibson** lineage — predecessors not ingested.
- Whether the 12.4% is partial-credit or strict binary (the paper's own metric is BDDL goal-condition satisfaction).
