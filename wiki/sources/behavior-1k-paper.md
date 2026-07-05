---
title: "BEHAVIOR-1K — A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation (paper)"
type: source
url: https://arxiv.org/abs/2403.09227
author: Chengshu Li, Ruohan Zhang, Josiah Wong, Cem Gokmen, Sanjana Srivastava, Roberto Martín-Martín, … (Stanford Vision & Learning Lab + HAI; + UT Austin, UIUC, USC)
published: 2022 (CoRL 2022, PMLR v205); arXiv 2403.09227v1 (human-centered version, 2024-03)
ingested: 2026-07-04
format: web (arXiv HTML)
tags: [behavior-1k, benchmark, household, omnigibson, bddl, sim-to-real, long-horizon, stanford, mobile-manipulation]
---

## Summary

Primary source for **[BEHAVIOR-1K](../entities/behavior-benchmark.md)** — Stanford's human-centered embodied-AI benchmark of **1,000 everyday household activities** simulated in **[OmniGibson](../entities/omnigibson.md)** (NVIDIA Omniverse + PhysX 5). Its distinguishing move: activity selection is **survey-grounded** (1,461 people ranked what they want robots to do) rather than researcher-curated, and it simulates what most benchmarks can't — **deformables, fluids, and extended object states** (temperature, soaked, cooked, sliced). The headline finding is a stark capability gap: end-to-end visuomotor RL scores **0.0** on these long-horizon tasks, and even primitive-augmented agents + real-robot transfer land in the low tens of percent — the empirical basis for the wiki's [sim-to-real gap](../concepts/learning/sim-to-real-transfer.md) framing.

## Key claims

### Two components
1. **The BEHAVIOR-1K dataset** — **1,000 activities** (909 top-ranked from the survey + 91 inherited from BEHAVIOR-100), grounded in **50 scenes** (houses, stores, restaurants, offices, …) with **9,000+ object instances across 1,900+ categories** (2,964 leaf synsets; 1,538 WordNet + 1,426 custom). Objects carry rich physical/semantic properties (cookable, freezable, breakable, fillable, flammable…) + transition rules (tomato + salt → sauce).
2. **[OmniGibson](../entities/omnigibson.md)** — the simulator that instantiates them: rigid + deformable bodies + fluids, **continuous extended states** (temperature/toggled/soaked/dirtiness), a **Transition Machine** for state changes (dough + hot oven → pie), thermal effects, ray/path-traced rendering. "Over half of BEHAVIOR-1K activities would not be simulatable" without fluid + deformable support.

### Task definition — BDDL
Activities are specified in **BDDL (BEHAVIOR Domain Definition Language)** — predicate-logic initial + goal conditions (e.g. `food is cooked and onTop of a plate`), *semantic* rather than geometric/image-based, so any scene instantiation satisfying the predicates is a valid start/goal.

### Survey grounding
**1,461 respondents** rated **2,090 candidate activities** (50 ten-point Likert responses/activity, Amazon Mechanical Turk); **tedious tasks rank highest** ("scrubbing the bathroom floor"), recreational lowest (game-play); Gini index 0.158 (high preference diversity). This is the "human-centered" claim — the benchmark tests what households *want*, not what's easy to simulate.

### Results (hard numbers — why it's the hard end of the gap)
Three baselines on StoreDecoration / CollectTrash / CleanTable:
| Baseline | Method | numbers |
|---|---|---|
| RL-VMC | end-to-end visuomotor (SAC) | **0.0 / 0.0 / 0.0** |
| RL-Prim | PPO + motion primitives (pick/place/push/navigate/dip/wipe) | 0.48 / 0.42 / 0.77 |
| RL-Prim+Hist | + 3-step observation history | **0.55 / 0.63 / 0.88** |
- **End-to-end RL from images completely fails**; action primitives are *necessary* for long-horizon success; memory helps (CollectTrash 0.42→0.63). CollectTrash needs ≥16 primitive steps.
- **Physics-based grasping is decisive**: training with assistive grasping but evaluating with full physics drops success to ~0.
- **Real robot (TIAGo bimanual mobile manipulator**, RRT-Connect primitives, dual-LiDAR particle-filter localization, YOLOv3 detection): ~**40%** sim → ~**22%** optimal-policy → **0%** trained-vision-policy. Failure sources: grasping (40%), visual-perception misalignment (44%), navigation compounding error.
- **Visual realism** user study (60 subjects): OmniGibson **3.20±1.23** vs Habitat 2.0 1.74, AI2-THOR 1.73, iGibson 2.0 1.69.

### Lineage
Successor to **BEHAVIOR-100** (iGibson 2.0-based; 100 activities, 15 house scenes, 300+ categories) — 10× activities, 3× scene types, richer physics; inherits BEHAVIOR-100's ATUS activity sourcing + BDDL + metrics but fixes its diversity/realism ceiling.

## Entities mentioned
- [BEHAVIOR-1K](../entities/behavior-benchmark.md) — this is its primary source. [OmniGibson](../entities/omnigibson.md) — the simulator (own entity).
- [Roberto Martín-Martín](../entities/roberto-martin-martin.md) — co-author (Stanford → UT Austin). Stanford Vision & Learning Lab; + UT Austin / UIUC / USC.
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) / [OpenUSD](../entities/openusd.md) — the Omniverse substrate OmniGibson builds on. YOLOv3 ([Ultralytics YOLO](../entities/ultralytics-yolo.md) lineage). TIAGo ([Tiago](../entities/tiago.md)) real robot.

## Concepts touched
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — BEHAVIOR-1K is the **hard, long-horizon, real-household end** of the gap (the paper's 0%–22% real-robot numbers; the AI-Index [12.4% challenge figure](stanford-hai-ai-index-2026.md) is a later, separate BEHAVIOR-1K Challenge result).
- [Imitation learning](../concepts/learning/imitation-learning.md) / RL — the primitive-vs-end-to-end result argues classical motion primitives + memory still beat end-to-end for long-horizon household tasks (echoes [Bekris et al.](state-of-robot-motion-generation-2024.md)).
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — OmniGibson is a *physics* simulator (not a learned one); the extended-state simulation (temperature/fluids) is what learned sims still can't match.

## Open questions
- The paper's **12.4%** is not in it — that's the 2025 BEHAVIOR-1K Challenge ([AI Index 2026](stanford-hai-ai-index-2026.md)); the paper's own numbers are the 0%–22% baselines above.
- **BEHAVIOR-100 / iGibson** predecessors + **AI2-THOR / Habitat** peer sims are named but not ingested.
- OmniGibson performance (~60 fps/house) vs the real-time needs of large-scale RL — a scaling bottleneck the paper flags.
- Survey demographic bias (≈75% white, 92.56% no-disability) — underrepresents the elderly/disabled who most benefit; a stated limitation.
