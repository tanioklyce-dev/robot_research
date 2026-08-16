---
title: Shortest Paths in Graphs of Convex Sets (Marcucci, Umenberger, Parrilo & Tedrake)
type: source
url: https://arxiv.org/abs/2101.11565
local_path: raw/Marcucci_ShortestPathsInGCS_2101.11565.pdf
author: Tobia Marcucci, Jack Umenberger, Pablo A. Parrilo, Russ Tedrake
published: 2021-01-27
ingested: 2026-08-16
venue: arXiv 2101.11565 (v1 2021-01-27; v5 2023-07-03, cs.DM); SIAM Journal on Optimization 34(1):507–532, Feb 2024
format: pdf
tags: [graphs-of-convex-sets, gcs, shortest-path, mixed-integer, micp, perspective-function, convex-relaxation, bilinear, mccormick, rlt, lovasz-schrijver, network-flow, hybrid-systems, piecewise-affine, optimal-control, mpc, drake, mosek, np-hard]
---

# Shortest Paths in Graphs of Convex Sets

## Summary

This is **the framework paper** that the [GCS motion planner](gcs-motion-planning-paper.md) treats as an external "modeling language," and reading it changes what GCS looks like. The planner is one application; the object is a **general-purpose mixed-integer formulation technique**. The problem: a directed graph where each vertex `v` carries a compact convex set `X_v` and a continuous position `x_v ∈ X_v`, each edge a convex nonnegative length `ℓ_e(x_u, x_v)`; find the source–target path *and* the vertex positions along it, jointly. NP-hard (Theorem 3.1).

The contribution is a **compact MICP whose convex relaxation is empirically very tight**, built from two ideas: extend the classical **network-flow LP** for shortest paths rather than inventing a new encoding, and use **perspective operators** to turn the resulting bilinear products `z_e = y_e x_u` into a **set-based convex relaxation** that never touches the inequalities defining `X_v`. Size: `O(|E|)` binaries, `O(n|E|)` continuous variables, `O(n(|V| + |E|))` constraints.

Its headline application is not motion planning but **optimal control of hybrid (piecewise-affine) systems**, where it beats the prior state of the art by an order of magnitude and change: on a PWA control problem the previous perspective formulation has a **93% relaxation gap and takes 17 minutes**; this one has a **20% gap and takes 7.1 seconds** (§9.3).

> [!note] The credit split this wiki drew in advance turns out to be right, and sharper than expected
> [Marcucci's page](../entities/tobia-marcucci.md) asserts that *"the planner is Tedrake's group's; the mathematical object is Marcucci's,"* inferred from the planning paper's own framing. This paper confirms it and adds context: the co-authors are **Jack Umenberger** and **Pablo Parrilo** — Parrilo being the sums-of-squares/semidefinite-relaxation authority — and the venue is **SIAM Journal on Optimization**, not a robotics conference. This is an optimization paper that happens to have a roboticist on it.

## The formulation, in the order it has to be understood

**1. Start from the network-flow LP, not from a new encoding.** Classical SPP as an LP over edge flows `y_e ∈ [0,1]`: one unit injected at the source, one ejected at the target, conservation plus a degree constraint at every other vertex. Basic feasible solutions of this LP are already binary, so integrality is free in the classical case.

**2. Add positions, and the nonconvexity appears as a product.** Put `x_v ∈ X_v` in as decision variables and the cost addend for edge `e` wants to be `ℓ_e(x_u, x_v) · y_e`. That product is **undefined when `ℓ_e = ∞` and `y_e = 0`** — the exact case that matters, since an infinite edge length is how the framework encodes an edge constraint (dynamics, continuity) being violated.

**3. Perspective functions fix it, and this is the paper's central trick.** Introduce `z_e := y_e x_u`, `z'_e := y_e x_v` and use the perspective `ℓ̃_e(z_e, z'_e, y_e)`. For `y_e > 0` it equals `ℓ_e(x_u, x_v) y_e` exactly; for `y_e = 0` it is well-defined and evaluates to **zero even when `ℓ_e = ∞`**. Perspective operators *"give us a convenient and rigorous way to 'turn on and off' the length of an edge using the corresponding flow variable."* What remains is a **biconvex** program whose only nonconvexity is the bilinear equalities `z_e = y_e x_u`.

**4. Relax the bilinears by multiplying valid inequalities (Lemma 5.4).** Any valid linear inequality on the flows incident to `v` can be multiplied by `x_v ∈ X_v`, and the product linearized through the bilinear equality, yielding a **perspective-cone constraint** `(Σ c_e z_e + d x_v, Σ c_e y_e + d) ∈ X̃_v`. Apply it to each flow constraint and the MICP (5.5) falls out. Dropping integrality gives the relaxation.

**5. Why it is correct (Lemma 7.4, the geometric proof).** The relaxation `S'` is **exact at the extreme points of the flow polytope** — and the flow vectors corresponding to an actual path *are* extreme points. So the MICP is valid for a reason that fits in two sentences, and the result generalizes a known RLT property (Adams & Sherali) from polytopes to **generic closed convex sets**.

## Key claims

- **NP-hard, and the proof is a two-paragraph gem.** Reduce Hamiltonian Path: sets `X_s = {0}`, `X_t = {1}`, `X_v = [0,1]`, edge length = **squared** Euclidean distance. For a path with `K` edges the optimal spacing is uniform and the cost is `K·(1/K)² = 1/K`, so **minimizing cost = maximizing path length = finding a Hamiltonian path**. One-dimensional intervals are already enough to make the problem hard.
- **And it stays hard under every obvious escape.** Theorem 3.2: acyclic graph **and** disjoint sets **and** positively homogeneous edge lengths — still NP-hard.
- **The relaxation is *set-based*, which is the underrated property.** It *"does not rely on the explicit constraints that define the sets… but works directly with their abstract set representations."* Consequence (Remark 5.9): the sets may be **black boxes accessible only through a separation oracle**, since such an oracle adapts directly to membership in the perspective cone. Perspective is cheap in conic form — polyhedral/ellipsoidal/spectrahedral sets keep their linear/SOC/SDP representation (Example 4.3).
- **Where it sits among relaxation techniques.** It is first-level **RLT** restricted to the bilinear structure at hand; for real intervals it *collapses to the McCormick envelope*; it is closest in spirit to the **Lovász–Schrijver** hierarchy but *"smaller and as tight as the first level… without semidefinite constraints."* And it **cannot** be the convex hull in general (Remark 7.3): `S' = conv S` would solve an NP-hard bilinear program in polynomial time. The convex hull is available via disjunctive programming (7.4) at a size proportional to the number of *extreme points* rather than facets — tested, and slower.
- **Against the naive alternative, by a wide margin.** McCormick-envelope MICP on the random benchmark: median relaxation gap **29%/34%** (Euclidean / squared) versus near-zero, and median runtime **12.9× / 10.3×** larger, frequently hitting a one-hour limit on harder batches.
- **The degree constraint is redundant in the LP and load-bearing in the MICP.** Example 5.10 exhibits a five-line instance where, without it, the optimal "path" contains a **disjoint cycle** and the cost drops below the true optimum. A redundancy in the relaxation's ancestor is not a redundancy in the relaxation.

### What loosens the relaxation (§9.2, 500 random instances per edge length)

Nominal: `Λ = 0.01` set volume, `n = 4`, `|V| = 50`, `|E| = 100`; each batch increases one parameter 5×.

| Batch | Max relaxation gap | Max MICP runtime |
|---|---|---|
| Nominal (squared length) | 2.1% | 0.66 s |
| Large sets (Λ → 0.05) | 9.1% | 1.12 s |
| **High dimension (n → 20)** | **28.9%** | **72 s** |
| **Dense graph (\|E\| → 500, \|V\| = 50)** | **32.9%** | **174 s** |
| Large graph (\|V\| → 250, \|E\| = 500) | 5.3% | 5.4 s |

**Density, not size.** The last row is the informative one: same edge count as the worst batch, five times the vertices — and the gap collapses from 32.9% to 5.3% because the graph got **sparser**. Cycles are the mechanism (*"the combination of the quadratic edge length and the large number of cycles that we have in a graph with high density"*). With the plain **Euclidean** length the relaxation is tight in almost every instance regardless.

> [!warning] The relaxation can be arbitrarily loose, and the authors build the counterexample themselves (§9.4)
> A five-vertex acyclic graph with a **symmetry** — two equal-cost routes into a shared region — has the relaxation split flow ½/½ and place the two surrogate points where neither would be legal alone, for a 5% gap. Shift the geometry and *"the relaxation gap becomes **100%**."* Their own hedge: *"this is a contrived problem, and the instances we encounter in practice lead to these phenomena very rarely."*
>
> Symmetry is the same failure mode that the [planning paper](gcs-motion-planning-paper.md)'s footnote 3 gives as the reason rounding must be randomized, and the same one [Tedrake reports observing on a UAV](tedrake-gcs-foundation-models-talk.md) (two near-identical windows). **Three independent appearances of one mechanism** — it is the framework's characteristic weakness, not an anecdote.

## Optimal control is the target application, and the win is large

§8 shows how to cast control problems as SPPs in GCS, and the modeling choice is the whole contribution:

- **Minimum-time control** — chain of vertices, one per time step, each with an extra edge straight to the target; edge length 1 if `s_v = A s_u + B a_u` and **∞ otherwise**. Path length = time horizon.
- **PWA / hybrid systems** — `T` layers of `|N|` vertices (one per discrete mode), consecutive layers fully connected; `X_v` = that mode's state/control region; edge length = stage cost if the mode's affine dynamics are satisfied, ∞ otherwise.

> [!note] The idea worth stealing, stated plainly by the authors
> *"We do not use binary variables to encode the discrete mode in which the system is at each time step but, instead, we use them to select the **transitions** between modes. This different parameterization yields slightly larger but much stronger MICPs."*
>
> Cost: the graph is **quadratic** in `|N|` rather than linear. Benefit, measured (§9.3, double integrator across 7 regions with mode-dependent controllability, `T = 30`, `|V| = 212`, `|E| = 1435`, sets in `ℝ⁶`):
>
> | Formulation | Relaxation gap | MICP solve time |
> |---|---|---|
> | Prior state of the art (Moehle & Boyd; Marcucci & Tedrake 2019) | **93%** | **1011 s ≈ 17 min** |
> | This paper | **20%** | **7.1 s** |
>
> **~142× faster.** And the qualitative difference is more interesting than the ratio: the baseline's relaxed trajectory *"heads straight to the goal"* and its mode indicators light up in the low-controllability regions — uninformative. This paper's relaxed solution **avoids those regions and clusters along the true optimal trajectory**: *"our relaxation contains detailed information about the optimal path."* A relaxation you can read is worth more than a bound you can only compare.

## The dual is a value function (Appendix B)

The dual assigns each vertex an **affine potential function** `r_v^⊤ x_v + p_v` over its set; the objective maximizes the source-to-target potential jump, and each edge constrains that jump to be no more than its length — the exact generalization of the classical shortest-path dual, where potentials are cost-to-go. Complementary slackness makes the jump tight along the chosen path.

This is the same object [Tedrake's 2024 seminar](tedrake-gcs-foundation-models-talk.md) describes as *"a piecewise-affine lower bound on the value function,"* upgradeable to quadratic/polynomial (⇒ SOS) for tighter bounds and thereby turning a plan into a policy. **The plan-to-policy result is written into the appendix of the 2021 framework paper**, three years before it was pitched as GCS's route to being robotics' missing MCTS.

## Beyond shortest paths (Appendix A)

The technique is not specific to the SPP. Any graph problem written as `min Σ l_e y_e s.t. y ∈ Y ∩ {0,1}^|E|` — TSP, minimum spanning tree, and the rest of the "with neighborhoods" literature — extends to its GCS version by the same construction. Two options: keep only the vertex-wise-separable flow constraints (compact, possibly weak), or introduce `n|V||E|` product variables `Z = x y^⊤` (larger, stronger). Existing exact algorithms for these problems *"rely on expensive mixed-integer nonconvex optimization… and do not scale beyond two or three dimensions"* — the claim is that this technique lifts that ceiling. Left as future work, unevaluated.

## Entities mentioned

- [Tobia Marcucci](../entities/tobia-marcucci.md) — first author; the framework is his.
- [Russ Tedrake](../entities/russ-tedrake.md) — senior author.
- [Drake](../entities/drake.md) — cited in the paper's own numerics section: *"A mature implementation of the techniques presented in this paper is also provided by the open-source software Drake."*
- Without pages: **Jack Umenberger**, **Pablo A. Parrilo** (MIT; the SOS/semidefinite-relaxation authority — his presence explains the paper's fluency with hierarchies), **Hongkai Dai** (thanked for the solver interface), **MOSEK 10.0** (solver), and the prior-art authors Moehle & Boyd.
- Code: `github.com/TobiaMarcucci/shortest-paths-in-graphs-of-convex-sets`.

## Concepts touched

- [Graphs of convex sets (GCS)](../concepts/robotics/graphs-of-convex-sets.md) — **the primary source for the framework half of that page.**
- [Optimal control](../concepts/robotics/optimal-control.md) — hybrid/PWA MPC is the paper's target application, and the 17 min → 7.1 s result belongs there.
- [Motion planning (classical)](../concepts/robotics/motion-planning.md) — the downstream application this wiki ingested first.
- [Formal verification](../concepts/learning/formal-verification.md) — perspective/SOS/semidefinite relaxation machinery, and Parrilo's lineage.

## Open questions

- **Has anyone taken Appendix A seriously?** TSP-with-neighborhoods and MST-with-neighborhoods in `n` dimensions via this technique is offered and never evaluated. If it works, the reach of GCS is far wider than robotics.
- **Hybrid MPC at control rates.** 7.1 s for a 30-step PWA problem is a planning result, not a control result. Closing the loop needs warm starts (Marcucci & Tedrake 2021 exists, uningested) or the newer heuristic-search line (`GCS*`, implicit graphs). Where is hybrid-MPC-via-GCS today?
- **When is the relaxation exact?** Empirically it is tight with Euclidean lengths and loosens with dimension, density, and symmetry. There is no characterization here — only Remark 5.8 (singleton sets) and the observation that exactness holds at extreme points of the flow polytope. A structural condition would be worth a lot.
- **This wiki still has no ingested source on IRIS**, the other half of every GCS pipeline. Region generation remains the one component covered only secondhand.
