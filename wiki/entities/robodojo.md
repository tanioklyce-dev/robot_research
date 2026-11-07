---
title: RoboDojo
type: entity
subtype: benchmark
created: 2026-11-07
updated: 2026-11-07
sources: 2
tags: [robodojo, benchmark, evaluation, isaac-sim, isaac-lab-arena, sim-and-real, bimanual, arx-x5, piper, xpolicylab, robotwin, mit]
---

# RoboDojo

**RoboDojo** is a unified **sim-and-real benchmark** for generalist manipulation policies, from the team led by Tianxing Chen that also maintains [RoboTwin](robotwin.md). It was released 2026-07-06 (arXiv 2607.04434) under the MIT license ([branch READMEs](../sources/robodojo-isaaclabarena-branch.md)).

## Design (per the main-branch README)
- **Coverage.** **42 simulation tasks** on Isaac Sim and **18 real-world tasks**, across 3 embodiments: Piper X, [Piper](agilex-piper.md) and ARX X5.
- **Five capability dimensions.** Generalization, Memory, Precision, Long-Horizon and Open. The README calls them *"designed to probe different skills rather than simple object or layout reskins"* and the tasks *"intentionally hard."*
- **Simulation.** Heterogeneous parallel simulation runs different tasks and scenes concurrently. Rigid, articulated and deformable assets share one configuration-driven scene.
- **Eval only.** Policies plug in through **XPolicyLab** (arXiv 2608.09892), *"40+ policies behind one interface"* for sim and real alike. There is also a RoboDojo-RealEval protocol and a live leaderboard.
- **Shared maintenance with RoboTwin.** The September 2026 RGB channel-ordering fix was made *"together with RoboTwin"* to keep the two consistent.

## Isaac Lab-Arena port (2026-10-30)
- RoboDojo is the second suite from this team ported to [Isaac Lab-Arena](isaac-lab-arena.md), after RoboTwin 2.0. The port lives on the `RoboDojo-IsaacLabArena` branch.
- **Scope.** **54 tasks** (42 + 12 `_random` variants), **2,100 episodes**, on the dual ARX X5, with a [π0.5](pi-zero-5.md) adapter.
- **Pins.** A pinned 38.4 GiB asset snapshot and pinned Arena and Isaac Lab commits, on Isaac Sim 5.1.
- **Checks and multi-env.** CPU contract tests, and heterogeneous multi-environment batches with per-slot termination.
- **No results yet.** No success rates and no native-vs-Arena parity numbers have been published, only the tooling to compute them ([branch READMEs](../sources/robodojo-isaaclabarena-branch.md)).

## Why it matters for this wiki
- It is a direct check on Arena's pitch. A third-party benchmark was ported in, and it took a pinned, older Arena commit plus an offline-assets patch to do it.
- It is one of the few benchmarks with a **real-world track and a sim track on the same embodiments**. That is the sim-to-real correlation question [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) keeps asking. Whether the paper answers it is unknown until the paper is ingested.
- The Piper embodiment ties it to the low-cost arms the wiki tracks.

## Related
- [RoboTwin](robotwin.md), the sibling benchmark from the same team.
- [Isaac Lab-Arena](isaac-lab-arena.md) · [Isaac Sim](nvidia-isaac-sim.md)
- [ToyBlocks](toyblocks.md), the opposite design choice: one narrow, editable world rather than a broad fixed suite.

## Mentioned in
- [RoboDojo — RoboDojo-IsaacLabArena branch (GitHub READMEs)](../sources/robodojo-isaaclabarena-branch.md)
- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md): listed as "coming soon" in Arena's ecosystem, 2026-09-14.
