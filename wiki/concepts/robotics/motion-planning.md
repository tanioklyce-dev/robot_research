---
title: Motion planning (classical)
type: concept
created: 2026-07-04
updated: 2026-07-04
sources: 4
tags: [motion-planning, sampling-based, rrt, prm, trajectory-optimization, search, ompl, explicit-model]
---

**Motion planning** — computing a safe (collision-free) nominal path or trajectory to a goal, given an **explicit model** of the world (geometry + dynamics) under full observability. The mature, deployed core of classical robotics: industrial-arm collision-free planning is "reliably addressed today at high speeds," and mobile navigation in semi-structured domains is reliable ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §4).

## The three classical families ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §2.1)

1. **Search-based** — discretize, then UCS/Dijkstra/A*. Optimal on the discrete representation given admissible/consistent heuristics; suffers the curse of dimensionality. Used for autonomous vehicles and single/dual-arm planning; D* Lite for replanning.
2. **Sampling-based motion planners (SBMPs)** — **PRM** (multi-query roadmaps) and **RRT** (single-query trees; no steering function needed, so handles dynamical systems). Base versions are provably suboptimal; **PRM\*/RRT\*** are asymptotically optimal, with recent planners extending asymptotic optimality to kinodynamic problems. Reference implementations in **OMPL**.
3. **Optimization-based** — CHOMP (covariant gradient descent), TrajOpt (sequential convex optimization), KOMO (k-order Markov sparse NLP), factor graphs (STEAP), **Graph of Convex Sets** (GCS — convex free-space regions bridging optimization and SBMPs). Fast, high-quality when they work; local minima on non-convex problems.

Plus a fourth, growing family: **ML-for-planning** — learned sampling distributions, collision predictors, distance metrics, infeasibility proofs; Neural Motion Planning approximates a planner with an encoder + planning network trained from simulator data.

## Relation to the learned stack

- The wiki's learned-policy line ([Diffusion Policy](../../entities/diffusion-policy.md), [VLA models](../learning/vla-models.md)) *replaces* explicit planning with implicit models — strongest exactly where explicit models fail (contact-rich manipulation, clutter), weakest on guarantees and out-of-distribution setups ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §4).
- Learned-world-model planning ([LeWM](../../entities/leworldmodel.md), [DINO-WM](../../entities/dino-wm.md), [TD-MPC](../../entities/td-mpc.md)) is the hybrid: sampling-based optimization (CEM/MPPI — SBMP cousins in action space) over a *learned* dynamics model instead of an explicit one.
- Bekris et al.'s recommendation 1 — use explicit-model planners in simulation as **demonstrators** for data-driven policies — is already standard practice in the wiki's corpus ([MimicGen](../../entities/mimicgen.md)/DexMimicGen trajectory generation for [GR00T N1](../../sources/groot-n1-paper.md); [ManiSkill-HAB](../../sources/maniskill-hab-paper.md)-style scripted demos).

## Key references

- [The State of Robot Motion Generation (Bekris et al. 2024)](../../sources/state-of-robot-motion-generation-2024.md) — the organizing survey for this page.
- Kavraki et al. 1996 (PRM), LaValle 1998 (RRT), Karaman & Frazzoli 2011 (PRM*/RRT*) — foundational papers, not in `raw/`.
- [MoveIt](../../entities/moveit.md) — the ROS-ecosystem motion-planning framework (OMPL-backed) the wiki already tracks on the platform side.

## Related concepts

- [Task and motion planning](task-and-motion-planning.md) — the long-horizon layer above single-query motion planning.
- [Optimal control](optimal-control.md) — trajectory optimization is the shared machinery; MPC is the feedback form.
- [World model](../world-models/world-model.md) — planning over learned rather than explicit models.
- [Imitation learning](../learning/imitation-learning.md) — the implicit-model alternative.

## Mentioned in

- [The State of Robot Motion Generation (Bekris et al. 2024)](../../sources/state-of-robot-motion-generation-2024.md)
- [Kober, Bagnell & Peters 2013](../../sources/kober-rl-robotics-survey-2013.md) — hierarchical decomposition and operational-space reductions as dimensionality-curse mitigations.
