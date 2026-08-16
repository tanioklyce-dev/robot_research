---
title: Motion planning (classical)
type: concept
created: 2026-07-04
updated: 2026-08-16
sources: 7
tags: [motion-planning, sampling-based, rrt, prm, trajectory-optimization, search, ompl, explicit-model, graphs-of-convex-sets, convex-optimization]
---

**Motion planning** — computing a safe (collision-free) nominal path or trajectory to a goal, given an **explicit model** of the world (geometry + dynamics) under full observability. The mature, deployed core of classical robotics: industrial-arm collision-free planning is "reliably addressed today at high speeds," and mobile navigation in semi-structured domains is reliable ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §4).

## The three classical families ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §2.1)

1. **Search-based** — discretize, then UCS/Dijkstra/A*. Optimal on the discrete representation given admissible/consistent heuristics; suffers the curse of dimensionality. Used for autonomous vehicles and single/dual-arm planning; D* Lite for replanning.
2. **Sampling-based motion planners (SBMPs)** — **PRM** (multi-query roadmaps) and **RRT** (single-query trees; no steering function needed, so handles dynamical systems). Base versions are provably suboptimal; **PRM\*/RRT\*** are asymptotically optimal, with recent planners extending asymptotic optimality to kinodynamic problems. Reference implementations in **OMPL**.
3. **Optimization-based** — CHOMP (covariant gradient descent), TrajOpt (sequential convex optimization), KOMO (k-order Markov sparse NLP), factor graphs (STEAP), **[Graphs of Convex Sets](graphs-of-convex-sets.md)** (GCS — convex free-space regions bridging optimization and SBMPs). Fast, high-quality when they work; local minima on non-convex problems.

Plus a fourth, growing family: **ML-for-planning** — learned sampling distributions, collision predictors, distance metrics, infeasibility proofs; Neural Motion Planning approximates a planner with an encoder + planning network trained from simulator data.

> [!warning] The "local minima" summary of family 3 does not survive contact with GCS
> That clause is [Bekris et al.](../../sources/state-of-robot-motion-generation-2024.md)'s, and it is right for CHOMP / TrajOpt / KOMO — all of which locally optimize a nonconvex program. It is **wrong for [GCS](graphs-of-convex-sets.md)**, which the survey lists in the same breath. GCS solves a *single convex program plus a cheap rounding* and, on the [primary source](../../sources/gcs-motion-planning-paper.md)'s benchmarks, returns the **global** optimum on essentially every instance — 95% of 100 random quadrotor problems within 1% of optimal, worst case 2.9%, and all five 7-DoF arm tasks exactly optimal — while **certifying its own optimality gap per query at no extra cost**.
>
> The honest replacement for "local minima" is **"restricted problem class"**: GCS needs the free space handed to it as a union of convex sets, and cannot express dynamics, task-space constraints, or contact. The tradeoff moved from *reliability* to *modelling power* — a different criticism, and a much better one to be making.

### GCS in production

The optimization-based family is no longer only a benchmark story. **[Dexai Robotics](../../entities/dexai-robotics.md) replaced a tuned PRM with GCS in shipping food-assembly robots** ([Tedrake seminar 2024](../../sources/tedrake-gcs-foundation-models-talk.md); [ARM Institute](../../sources/arm-institute-gcs-dexai-project.md)) — a sampling-based incumbent displaced by an optimization-based planner in a system where cycle time is revenue.

Read the regime, not just the headline: fixed workcell, precompute the decomposition once, thousands of queries a day, free-space transit only. That is the *multi-query* column of the taxonomy above, which is exactly where PRM was supposed to be unbeatable. For the mobile-manipulator case Tedrake expects the opposite answer — *"very fast, very approximate covers that can come directly from perception,"* with optimality traded away.

Two related gaps this closes on the page: **the hand-seeded IRIS regions** are now generated automatically by an approximate **minimum clique cover on a visibility graph** (a clique of mutually visible samples ≈ a convex region), and the "no task-space constraints / no contact" limits have research answers (regions built on manifolds via analytical IK; SDP-relaxation spectrahedra as GCS vertices). See [graphs of convex sets](graphs-of-convex-sets.md).

### GCS vs. the sampling-based family it generalizes

The GCS authors' own framing is that their planner **is a PRM whose samples have been inflated into regions**: *"each collision-free sample is expanded to a collision-free convex region, that is inflated as much as the obstacles allow; reducing in this way a dense roadmap to a compact GCS."* On a 7-DoF KUKA iiwa, **8 IRIS regions replaced a 15,000-sample roadmap** and won every task on trajectory length *and* runtime — including against PRM-with-shortcutting, the version practitioners actually deploy ([Marcucci et al. 2022](../../sources/gcs-motion-planning-paper.md) §7.4).

Two structural differences behind that, both worth keeping:

- **Collision-freeness is continuous, not sampled.** SBMPs check collision at finitely many points along an edge; GCS constrains the trajectory to lie in the safe regions *for all* `t`, via the Bézier convex-hull property.
- **The cost of the decomposition is human.** IRIS seed poses in the paper were placed **manually by inverse kinematics**; roadmap construction is automatic. The 53 s region build vs. 16 min roadmap build understates the asymmetry, because only one of them needed a person.

## Relation to the learned stack

- The wiki's learned-policy line ([Diffusion Policy](../../entities/diffusion-policy.md), [VLA models](../learning/vla-models.md)) *replaces* explicit planning with implicit models — strongest exactly where explicit models fail (contact-rich manipulation, clutter), weakest on guarantees and out-of-distribution setups ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §4).
- Learned-world-model planning ([LeWM](../../entities/leworldmodel.md), [DINO-WM](../../entities/dino-wm.md), [TD-MPC](../../entities/td-mpc.md)) is the hybrid: sampling-based optimization (CEM/MPPI — SBMP cousins in action space) over a *learned* dynamics model instead of an explicit one.
- Bekris et al.'s recommendation 1 — use explicit-model planners in simulation as **demonstrators** for data-driven policies — is already standard practice in the wiki's corpus ([MimicGen](../../entities/mimicgen.md)/DexMimicGen trajectory generation for [GR00T N1](../../sources/groot-n1-paper.md); [ManiSkill-HAB](../../sources/maniskill-hab-paper.md)-style scripted demos).

## Key references

- [The State of Robot Motion Generation (Bekris et al. 2024)](../../sources/state-of-robot-motion-generation-2024.md) — the organizing survey for this page.
- [Motion Planning around Obstacles with Convex Optimization (Marcucci, Petersen, von Wrangel & Tedrake 2022 / Science Robotics 2023)](../../sources/gcs-motion-planning-paper.md) — the optimization-based family's strongest result and the page's only primary *method* source.
- Kavraki et al. 1996 (PRM), LaValle 1998 (RRT), Karaman & Frazzoli 2011 (PRM*/RRT*) — foundational papers, not in `raw/`.
- [MoveIt](../../entities/moveit.md) — the ROS-ecosystem motion-planning framework (OMPL-backed) the wiki already tracks on the platform side.

## Related concepts

- [Graphs of convex sets (GCS)](graphs-of-convex-sets.md) — the optimization framework under the family-3 result above; also the wiki's clearest instance of a planner that certifies its own suboptimality.
- [Task and motion planning](task-and-motion-planning.md) — the long-horizon layer above single-query motion planning.
- [Optimal control](optimal-control.md) — trajectory optimization is the shared machinery; MPC is the feedback form.
- [World model](../world-models/world-model.md) — planning over learned rather than explicit models.
- [Imitation learning](../learning/imitation-learning.md) — the implicit-model alternative.

## Mentioned in

- [The State of Robot Motion Generation (Bekris et al. 2024)](../../sources/state-of-robot-motion-generation-2024.md)
- [Motion Planning around Obstacles with Convex Optimization (GCS)](../../sources/gcs-motion-planning-paper.md) — the family-3 primary source; PRM comparison, maze binary-count argument, 14-DoF dual-arm scaling.
- [Planning with Graphs of Convex Sets (in the age of foundation models)](../../sources/tedrake-gcs-foundation-models-talk.md) — GCS displacing PRM in production; automatic region generation; the roadmap-as-design-complaint framing.
- [Kober, Bagnell & Peters 2013](../../sources/kober-rl-robotics-survey-2013.md) — hierarchical decomposition and operational-space reductions as dimensionality-curse mitigations.
