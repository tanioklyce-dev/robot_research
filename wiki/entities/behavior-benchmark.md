---
title: BEHAVIOR / BEHAVIOR-1K
type: entity
subtype: benchmark
created: 2026-07-04
updated: 2026-07-04
sources: 2
status: stub
tags: [behavior, behavior-1k, benchmark, household, simulation, omnigibson, stanford, sim-to-real]
---

> [!note] Stub entity
> Filed 2026-07-04 during lint (referenced across ~10 wiki files). Primary source — the BEHAVIOR-1K paper (Li, Fei-Fei et al., Stanford) and OmniGibson — **not yet ingested**; deepen when filed.

**BEHAVIOR / BEHAVIOR-1K** — Stanford's large-scale **household-activity benchmark**: **1,000 everyday tasks** drawn from surveys of what people actually want robots to do, simulated (OmniGibson, on NVIDIA Omniverse/Isaac Sim). In this wiki it is the **hard end of the sim-to-real gap** — the long-horizon, real-household counterpart to controlled short-horizon benchmarks.

## What we know via the wiki's existing references
- **The 12.4% number.** BEHAVIOR-1K full-task success is the low end of the canonical [sim-to-real gap](../concepts/learning/sim-to-real-transfer.md): **89.4% RLBench (controlled, short-horizon) vs 12.4% BEHAVIOR-1K (real household, long-horizon)** — the 2025 Challenge winner ([Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md)).
- **A GR00T data embodiment substrate.** [GR00T N1.6](../sources/groot-n1_6.md) trains on **simulated [Galaxea R1 Pro](galaxea-r1.md) on the BEHAVIOR suite** — one of its added data sources.
- **1,000 tasks from household surveys** — the design contrast the sim-to-real page draws: BEHAVIOR tests what households want, not what's easy to simulate.

## Why it matters in this wiki
- **The canonical "how far are we really" yardstick** for household manipulation — the number the wiki cites whenever it wants to puncture a controlled-benchmark result.
- Fills a ~10-mention gap flagged during lint (referenced by [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [GR00T N1.6](../sources/groot-n1_6.md), [Galaxea R1](galaxea-r1.md), [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md), [assistive robotics](../concepts/robotics/assistive-robotics.md)).

## Related
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — BEHAVIOR-1K is the hard end of the gap.
- [Galaxea R1](galaxea-r1.md) — the robot GR00T N1.6 runs on the BEHAVIOR suite (sim).
- [RoboCasa](robocasa.md), [Metaworld](metaworld.md), [LIBERO](libero.md) — peer manipulation benchmarks (RoboCasa is the closest — kitchen-scale, also Omniverse-adjacent).
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — the Omniverse substrate OmniGibson builds on.

## Mentioned in
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md) — the 12.4% figure.
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — simulated Galaxea R1 Pro on BEHAVIOR.

## Open questions
- **Primary source not ingested** — the BEHAVIOR-1K paper + OmniGibson would anchor task taxonomy, the activity list, the simulator stack, and the scoring rubric behind "12.4%".
- Relationship to the earlier BEHAVIOR-100 and iGibson lineage.
- Whether the 12.4% is partial-credit or strict binary success.
