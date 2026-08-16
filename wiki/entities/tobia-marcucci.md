---
title: Tobia Marcucci
type: entity
subtype: person
created: 2026-08-16
updated: 2026-08-16
sources: 3
tags: [tobia-marcucci, mit, graphs-of-convex-sets, gcs, convex-optimization, mixed-integer, motion-planning, optimization-theory]
---

# Tobia Marcucci

Optimization researcher; **originator of the Graphs of Convex Sets (GCS) framework** and first author (equal contribution) of [Motion Planning around Obstacles with Convex Optimization](../sources/gcs-motion-planning-paper.md) — MIT affiliation on that paper (EECS, with [Russ Tedrake](russ-tedrake.md)).

## Why he gets a page

Because the intellectual contribution splits cleanly and this wiki should not blur it. **The planner is Tedrake's group's; the mathematical object is Marcucci's.** The planning paper explicitly treats the shortest-path-in-GCS machinery as an external *"modeling language that allows us to formulate, and efficiently solve, an SPP in GCS just by providing the graph `G`, the edge lengths `ℓₑ`, and the sets `X_v` and `X_e`"* — citing his companion framework paper for the MICP formulation and the tightness result that the whole planner rests on.

The two contributions are separable and travel differently: [GCS](../concepts/robotics/graphs-of-convex-sets.md) has since been applied beyond collision avoidance (temporal-logic planning, combinatorial problems over convex sets), while the Bézier-curve trajectory parameterization is specific to motion planning.

## Contributions tracked here

- **[Shortest paths in graphs of convex sets](../sources/shortest-paths-in-graphs-of-convex-sets-paper.md)** (with **Jack Umenberger** and **Pablo Parrilo**; arXiv 2021, **SIAM J. Optimization 34(1) 2024**) — **ingested**. The compact MICP built by extending the network-flow LP and using **perspective operators** to switch edge costs and constraints on and off; a **set-based** relaxation of the resulting bilinear constraints that works through a separation oracle alone; NP-hardness by reduction from Hamiltonian Path; and **hybrid/PWA optimal control** as the stated target application, where it beats the prior perspective formulation **93% → 20% relaxation gap, 17 min → 7.1 s**.
- **GCS-based motion planning** ([Marcucci, Petersen, von Wrangel & Tedrake 2022 / Science Robotics 2023](../sources/gcs-motion-planning-paper.md)) — equal-contribution first author. Global optimality on 95% of quadrotor instances within 1%; beats PRM on a 7-DoF arm on both quality and time; scales to a 14-DoF dual-arm problem.
- **Randomized rounding of relaxed edge indicators**, with the symmetry argument for *why it must be randomized* (§4.2 footnote 3) — a general lesson about reading relaxed binaries as confidences.

**The co-author list is itself evidence for the credit split.** The framework paper is Marcucci with **Parrilo** — the semidefinite-relaxation/SOS authority — and **Umenberger**, published in **SIAM Journal on Optimization**. Tedrake is the fourth author on an optimization paper; he is the senior author on the robotics one. The wiki inferred this division from the planning paper's framing before the framework paper was ingested, and it holds.

> [!note] Live-web facts not verified from an ingested source
> His publication list and current position (he has moved on from MIT since the 2022 preprint) were not confirmed against an ingested source and are deliberately omitted rather than guessed. Both ingested papers state MIT; that is what this page asserts.

## Related

- [Russ Tedrake](russ-tedrake.md) — senior author of the planning paper; the [Drake](drake.md) side of the collaboration.
- [Graphs of convex sets (GCS)](../concepts/robotics/graphs-of-convex-sets.md) — his framework.
- [Motion planning (classical)](../concepts/robotics/motion-planning.md) — the taxonomy the planner lands in.
- [Drake](drake.md) — where the SPP-in-GCS solver ships.

## Mentioned in

- [Shortest Paths in Graphs of Convex Sets](../sources/shortest-paths-in-graphs-of-convex-sets-paper.md) — **first author; the framework paper.**
- [Motion Planning around Obstacles with Convex Optimization (GCS)](../sources/gcs-motion-planning-paper.md) — first author (equal contribution); the robotics instantiation.
- [Planning with Graphs of Convex Sets (in the age of foundation models)](../sources/tedrake-gcs-foundation-models-talk.md) — named by [Tedrake](russ-tedrake.md) as the through-line on every GCS slide ("Tobias" in the auto-captions); the framework's reach beyond collision avoidance — contact via spectrahedra, value-function duals, permutohedron walks — is the case for the credit split this page makes.
