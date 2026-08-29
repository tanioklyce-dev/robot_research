---
title: Motion Planning around Obstacles with Convex Optimization (GCS)
type: source
url: https://arxiv.org/abs/2205.04422
local_path: raw/Tedrake_GCS_MotionPlanning_2205.04422v1.pdf
sha256: 1b76b910b39fca1460f2d8e5f1445bfa7df1c19a33d11492714e281e5aac40fe
author: Tobia Marcucci, Mark Petersen, David von Wrangel, Russ Tedrake
published: 2022-05-09
ingested: 2026-08-16
venue: arXiv cs.RO (v1, 2022-05-09); published as Science Robotics 8(84), 2023-11-15, DOI 10.1126/scirobotics.adf7843
format: pdf
tags: [motion-planning, convex-optimization, graphs-of-convex-sets, gcs, mixed-integer, socp, bezier-curves, trajectory-optimization, prm, drake, iris, kuka-iiwa, quadrotor, russ-tedrake, mit]
---

# Motion Planning around Obstacles with Convex Optimization (GCS)

## Summary

Marcucci, Petersen, von Wrangel & Tedrake show that **collision-free motion planning around obstacles can be solved reliably by convex optimization** — the problem the field had long treated as the textbook source of nonconvexity. Decompose the free configuration space into overlapping convex "safe regions," build a graph whose vertices are those regions and whose edges connect overlapping ones, pair each vertex with a **Bézier curve** trajectory segment plus a Bézier **time-scaling** function, and the whole planning problem becomes a **shortest-path problem in a Graph of Convex Sets (GCS)** — a mixed-integer program whose convex relaxation is so tight that solving the relaxation once and applying a cheap randomized rounding almost always returns the *global* optimum. The reduction turns an intractable MICP back into a single **SOCP** (an LP for the pure minimum-time polytopic case), and the gap between relaxation cost and rounded cost is a **free certificate** on the plan's suboptimality. On a 7-DoF KUKA iiwa the planner beats PRM on **both** trajectory quality and runtime; it scales to a 14-DoF dual-arm problem in a confined space.

The named planner is **GCS**, after its underlying optimization framework — the shortest-path-in-graphs-of-convex-sets machinery from Marcucci et al.'s companion work, here treated as a modeling language.

> [!note] Why this paper matters to this wiki specifically
> The wiki's [motion planning](../concepts/robotics/motion-planning.md) page — built from [Bekris et al. 2024](state-of-robot-motion-generation-2024.md) — files optimization-based planners as *"fast, high-quality when they work; **local minima on non-convex problems**."* That characterization is correct for CHOMP / TrajOpt / KOMO and **is exactly what this paper's method does not do**. For its (restricted) problem class GCS returns a *globally optimal* trajectory and *proves* it, per query, at no extra cost. A one-word mention in a survey is now a primary source with the numbers attached.

## The construction, in the order it has to be understood

1. **Assume a convex decomposition of the free space.** `Q ⊂ ℝⁿ` (collision-free configurations) is covered by possibly-overlapping bounded convex sets `Qᵢ`. Exact for polyhedral obstacles; approximate via **IRIS** region inflation for real configuration spaces (§7.4).
2. **Graph.** Vertex per region; edge `(i,j)` iff `Qᵢ ∩ Qⱼ ≠ ∅`; plus source `σ` / target `τ` vertices carrying the boundary conditions (§5.1).
3. **Two Bézier curves per vertex.** A trajectory segment `rᵢ: [0,1] → Qᵢ` and a **time-scaling** `hᵢ`, both of user-chosen degree `d ≥ η+1` where `η` is the required differentiability of the final trajectory (§5.2). Decoupling *shape* `r` from *timing* `h` via a path coordinate `s` is what makes duration a decision variable without making the program nonconvex.
4. **Bézier properties do the heavy lifting.** The convex-hull property converts the *infinite* family of constraints `rᵢ(s) ∈ Qᵢ ∀s` into `d+1` constraints on control points, `rᵢ,ₖ ∈ Qᵢ` (§5.2). Same trick bounds velocity (`ṙᵢ,ₖ ∈ ḣᵢ,ₖ D`) and gives convex upper bounds on path length and energy (§5.4).
5. **Solve the relaxation, round, certify.** Relax the per-edge binaries `ϕₑ ∈ {0,1}` to `[0,1]` and read them as transition probabilities; run **randomized depth-first search with backtracking** weighted by `ϕₑ` (N=10 distinct paths, M=100 max trials); solve a tiny convex program per candidate path; keep the cheapest (§4.2).

The certificate falls out of `C_relax ≤ C_opt ≤ C_round`: report `δ_relax := (C_round − C_relax)/C_relax` as a free upper bound on the true optimality gap `δ_opt`.

## Key claims

- **The binary-variable count is the structural win.** Prior MICP planners parameterize one trajectory cut into fixed segments and use a binary per (segment, region) pair — worst case `|I|²`. GCS uses **two binaries per pair of intersecting regions**. On the 50×50 maze (2,500 cells): prior formulation `|I|² = 6.25×10⁶` binaries, *"a quantity well beyond the capability of today's solvers"*; GCS **5,198 ≈ 2|I|**, solved exactly through a single SOCP (§7.2).
- **The relaxation is tight enough that rounding is usually unnecessary.** On the maze, both objectives returned **binary `ϕₑ` straight from the relaxation** — `δ_relax = δ_opt = 0%`, no rounding step at all (§7.2).
- **Statistically, on 100 randomly generated buildings (quadrotor, 3D, `η := 4`, degree 7):** **95% of instances have `δ_opt < 1%`; worst case 2.9%** (§7.3, Fig. 7a). Self-certified: 68% of problems certified within 4%, 84% within 7%; largest certified `δ_relax = 27.1%` on an instance whose *actual* gap was 2.3% — i.e. the loose certificate came from a loose relaxation, not a bad plan.
- **Against PRM on a 7-DoF KUKA LBR iiwa (5 rack/bin tasks, minimum-length objective, 8 IRIS regions vs. a 15,000-sample roadmap): GCS wins every task on both axes.**

  | Task | GCS length (rad) | PRM | PRM + shortcut | GCS time (s) | PRM | PRM + shortcut |
  |---|---|---|---|---|---|---|
  | 1 | **3.3** | 9.7 | 5.6 | **0.11** | 0.26 | 0.61 |
  | 2 | **2.1** | 6.7 | 5.2 | **0.01** | 0.21 | 0.60 |
  | 3 | **2.6** | 3.7 | 2.7 | **0.05** | 0.20 | 0.44 |
  | 4 | **3.5** | 6.1 | 3.8 | **0.14** | 0.21 | 0.51 |
  | 5 | **1.8** | 4.2 | 1.9 | **0.08** | 0.21 | 0.54 |

  (§7.4, Fig. 10.) All five rounded solutions were the global optimum (`δ_opt = 0%`); mean certified `δ_relax` 4.1%, max 13.0%. Task 2's 0.01 s is the pre-processing stage collapsing the graph to the single feasible path `(σ,2,6,3,τ)`.
- **It scales past where sampling-based planners are chosen.** Dual KUKA iiwa, **14-dimensional** configuration space, arm-arm self-collision included, 22 seed regions, `C¹` cubic trajectories: three tasks solved in **4.0 / 8.4 / 12.9 s** with certified gaps 3.3% / 2.0% / 0.6%; two verified globally optimal, the third `δ_opt = 0.3%` (§7.5).
- **GCS is a generalization of PRM**, and the authors say so: *"each collision-free sample is expanded to a collision-free convex region, that is inflated as much as the obstacles allow; reducing in this way a dense roadmap to a compact GCS"* (§8.3). 8 regions replaced 15,000 samples.
- **Collision-freeness is continuous, not sampled.** Constraint (1c) holds `∀t ∈ [0,T]` — *"a stronger constraint than is usual in sampling-based motion planning, where trajectories are typically checked to be collision-free only at a finite number of points"* (§2).
- **Bézier vs. sums-of-squares is a deliberate tradeoff.** The prior MICP formulation enforces region containment with SOS polynomials and semidefinite programming; Bézier control points give a *more stringent* but far cheaper condition. This is what lets GCS reach `η ≥ 4` differentiability with SOCPs where SOS-based planners need *"prohibitive mixed-integer semidefinite programs that cannot be tackled with common solvers"* (§5.6, §8.2). `η ≥ 4` is not academic: it is what quadrotor differential flatness requires.
- **Implementation is in [Drake](../entities/drake.md).** The SPP-in-GCS machinery ships in Drake, as does `IrisInConfigurationSpace`; the paper's own interface is at `mpetersen94/gcs` (the Science Robotics release lives at `RobotLocomotion/gcs-science-robotics`). Solver: **MOSEK 9.2**.

## What it does not do — stated plainly by the authors

- **The convex decomposition is an input, not an output.** For the arm experiments the IRIS **seed poses were produced manually via inverse kinematics** with visual inspection of the resulting graph connectivity (§7.4, §7.5) — *"Automatic seeding of the regions is certainly possible, but we have found that producing seeds manually … is straightforward and highly effective."* Region construction took **53 s** (8 regions, parallelized). That is real human labor and real offline cost, sitting outside the reported query times.
- **The fast IRIS implementation does not certify its own regions.** *"While these polytopes could be rigorously certified to be collision free, for the experiments reported here we use a fast implementation based on nonconvex optimization that does not provide a rigorous certification, but that appears to be very reliable in practice."* The end-to-end guarantee is therefore optimality-of-plan-within-the-regions, not collision-freeness-of-the-regions.
- **No dynamics.** Equality constraints coupling `q` to its derivatives *"makes these constraints nonconvex, even for a linear control system"* under the joint shape/timing parameterization (§8.1). Kinematics only.
- **No task-space constraints.** *"the nonlinearity of the kinematics of a robot manipulator makes task-space constraints not directly suitable for our framework"* (§8.1). Suggested workaround: post-process with a local nonconvex optimizer.
- **No contact.** Listed as future work (§9).
- **Higher derivatives are regularized, not bounded.** Penalties on `q̈` and above are nonconvex in `(r,h)`; §6 substitutes penalties on `r̈`, `ḧ` plus raising `ḣ_min` — *"not as tight as the velocity bounds."*
- **The control-point condition is sufficient, not necessary** — conservative, attenuated by raising curve degree (§5.2).
- **The SPP in GCS is NP-hard**; the rounding is a heuristic with no worst-case guarantee. What the method actually offers is: it works nearly always in practice, *and you always know how well it worked*.
- **Numerical fragility.** MOSEK needed `MSK_IPAR_INTPNT_SOLVE_FORM = 1` (primal form) to avoid numerical issues on the quadrotor and dual-arm problems, which *"sensibly slow[ed] down the planning times"* — quadrotor relaxation solves median **3.7 s**, mean 6.4 s, max **31.2 s**. The authors expect an order of magnitude from a tailored pre-solve; that is a promise, not a result.
- **Complexity of use.** *"the implementation of GCS is very involved and requires familiarity with convex-optimization techniques"* — against PRM's principal virtue, simplicity (§8.3).

> [!note] The comparison is fair in kind but the setup costs differ by an order of magnitude in the other direction
> GCS's 8 IRIS regions took **53 s** to build; the PRM's 15,000-sample roadmap took **16 minutes**. Both are amortized multi-query offline costs, and the paper's runtime figures exclude both. The reason to raise it anyway: the roadmap build is *automatic*, the region seeding was *manual*. Automatic seeding is the load-bearing missing piece for anyone wanting this in a pipeline.

## The result worth carrying beyond motion planning

**A planner that certifies its own suboptimality per query, for free.** `δ_relax` costs one subtraction and bounds the true gap from above. Almost nothing else in this wiki's corpus does this — a learned policy's quality is knowable only by [rollouts](../concepts/robotics/robot-policy-evaluation.md), where establishing ±2 pp takes ~1,030 trials. Here the guarantee is per-instance, attached to the answer, and computed before the robot moves.

That is the shape of the argument [Drake](../entities/drake.md) makes generally — *expose the structure so you can optimize and verify* — reduced to a single number.

## Entities mentioned

- [Russ Tedrake](../entities/russ-tedrake.md) — senior author (equal contribution).
- [Tobia Marcucci](../entities/tobia-marcucci.md) — first author; the GCS shortest-path framework this planner is built on is his.
- [Drake](../entities/drake.md) — the implementation substrate (SPP-in-GCS solver, `IrisInConfigurationSpace`).
- Mark Petersen (Harvard SEAS), David von Wrangel (MIT) — co-authors; no pages.
- Without wiki pages: **IRIS** (region inflation), **MOSEK** / **Gurobi** (conic solvers), **KUKA LBR iiwa** (the 7-DoF benchmark arm), PRM/OMPL.

## Concepts touched

- **[Graphs of convex sets (GCS)](../concepts/robotics/graphs-of-convex-sets.md)** — new concept page from this ingest.
- [Motion planning (classical)](../concepts/robotics/motion-planning.md) — updated: the optimization-based family now has a primary source and a counterexample to its "local minima" characterization.
- [Optimal control](../concepts/robotics/optimal-control.md) — trajectory optimization as the shared machinery; GCS is the globally-optimal, dynamics-free corner of it.
- [Task and motion planning](../concepts/robotics/task-and-motion-planning.md) — the layer above; a planner with per-query optimality bounds is a better primitive for a symbolic layer to call.
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the quadrotor experiment turns on differential flatness requiring `C⁴` trajectories.

## Open questions

> [!note] Three of these were closed the same day, by [Tedrake's 2024 MIT Robotics Seminar](tedrake-gcs-foundation-models-talk.md)
> Answers inlined below; the seminar page carries the detail.

- ~~**Automatic region seeding.**~~ **Closed.** Replaced by a **visibility graph + approximate minimum clique cover** (a clique of mutually-visible samples ≈ a convex set), described as *"almost turnkey"* by 2024. The residual judgment is *coverage policy*, not seeding: Tedrake's guidance is that covering every corner of a high-dimensional C-space is *"a false goal."*
- ~~**Did GCS reach deployment?**~~ **Closed — narrowly yes.** [Dexai Robotics](../entities/dexai-robotics.md) *"switched from their pretty optimized… PRM-based planner. Now they're using GCS in production"* in food assembly, corroborated with a >$10k/robot/year figure by the [ARM Institute](arm-institute-gcs-dexai-project.md). One named user, in precisely the regime where every limitation below is free: fixed workcell, precompute once, plan all day, cycle-time-is-revenue. **Not** general adoption — and the evidence is a spoken remark from April 2024 with no follow-up tracked here.
- **GCS ∘ learned policies.** Still open, but now with a proposed mechanism from the same source: the graph explodes for dexterous contact (*"I can't even put it in memory"*), so **roll out a generalist policy a few times to decide which nodes to expand** — MCTS with GCS at the leaves. That is a plan, not a result. The reverse direction *has* happened: GCS-planned contact trajectories were fed into a [Diffusion Policy](../entities/diffusion-policy.md) as co-training curriculum.
- **The limits below did not survive as stated.** By 2024, task-space constraints are handled by building regions on a manifold via analytical IK, non-Euclidean C-spaces by geodesic convexity, and **contact** by making each mode's SDP-relaxation **spectrahedron** a GCS vertex. What remains true is the *scaling* limit, in the author's words: *"I don't think we can solve dexterous hands with GCS as it is. The graph gets too big."*
- **Follow-on GCS literature is uningested**: temporal-logic planning via GCS (T-RO 2023), and the broader shortest-paths-in-GCS theory paper this one treats as a black box.
- **The dynamics gap is the real limit.** Kinematic plans still need a tracking controller; the wiki's [optimal control](../concepts/robotics/optimal-control.md) page has that layer (LQR/MPC), but nothing here connects the two ends.
