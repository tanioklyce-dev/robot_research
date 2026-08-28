---
title: Graphs of Convex Sets (GCS)
type: concept
created: 2026-08-16
updated: 2026-08-16
sources: 5
tags: [graphs-of-convex-sets, gcs, convex-optimization, mixed-integer, socp, shortest-path, bezier-curves, motion-planning, global-optimality, certificates, drake, deployment, planning-through-contact, semidefinite-relaxation, perspective-function, hybrid-systems, piecewise-affine, network-flow]
---

**Graphs of Convex Sets (GCS)** — an optimization framework in which each **vertex of a graph carries a convex set** (and a continuous decision variable constrained to lie in it), and each **edge carries a convex, nonnegative length function** of the variables at its two endpoints, plus convex constraints coupling them. The **shortest-path problem in a GCS** then asks for *both* a discrete path σ→τ *and* the continuous values along it, jointly.

```
minimize  Σ_{e=(u,v) ∈ E_p}  ℓ_e(x_u, x_v)        (convex, ≥ 0)
over      a path p from σ to τ,  and points x_v
s.t.      x_v ∈ X_v      for v on p               (convex)
          (x_u, x_v) ∈ X_e  for e on p            (convex)
```

The definitional subtlety, and the source of its power: **the convex constraints apply only to the vertices the path actually visits.** That is what makes it a genuinely mixed discrete-continuous object rather than a graph search with a convex program bolted on.

**It is NP-hard, and the proof is two paragraphs** ([Marcucci et al. 2021](../../sources/shortest-paths-in-graphs-of-convex-sets-paper.md) Thm 3.1). Reduce Hamiltonian Path: put `X_s = {0}`, `X_t = {1}`, `X_v = [0,1]`, and use *squared* Euclidean distance. A `K`-edge path spaces its points uniformly for a cost of `K·(1/K)² = 1/K`, so **minimizing cost means maximizing the number of vertices visited** — a Hamiltonian path iff one exists. One-dimensional intervals suffice. And it stays NP-hard under every obvious escape hatch: acyclic graph *and* disjoint sets *and* positively homogeneous edge lengths (Thm 3.2).

## How the MICP is built ([Marcucci, Umenberger, Parrilo & Tedrake](../../sources/shortest-paths-in-graphs-of-convex-sets-paper.md))

The formulation is an **extension of the classical network-flow LP for shortest paths**, not a new encoding — which is why it inherits that LP's structure and why so much of it comes out clean.

1. **Flows.** Keep the LP's edge variables `y_e`: one unit injected at the source, ejected at the target, conservation and a degree constraint elsewhere.
2. **Positions make it bilinear.** The cost addend wants to be `ℓ_e(x_u, x_v)·y_e`, which is **undefined when `ℓ_e = ∞` and `y_e = 0`** — precisely the case that matters, since an infinite edge length is how the framework encodes a violated edge constraint.
3. **Perspective operators switch edges on and off.** With `z_e := y_e x_u`, `z'_e := y_e x_v`, the perspective `ℓ̃_e(z_e, z'_e, y_e)` equals the product when `y_e > 0` and evaluates to **zero when `y_e = 0`, even if `ℓ_e = ∞`**. The remaining nonconvexity is only the bilinear equalities.
4. **Relax them by multiplying valid inequalities.** Any valid linear inequality on the flows at `v`, multiplied by `x_v ∈ X_v` and linearized, becomes a **perspective-cone constraint** `(·, ·) ∈ X̃_v`. That is the MICP.

Size: `O(|E|)` binaries, `O(n|E|)` continuous variables, `O(n(|V|+|E|))` constraints.

Three properties are worth carrying beyond GCS:

- **The relaxation is *set-based*.** It never touches the inequalities defining `X_v`, only the set's abstract representation — so the sets may be **black boxes reachable only through a separation oracle**. Perspective is free in conic form: polyhedral/ellipsoidal/spectrahedral sets keep their LP/SOCP/SDP representation.
- **It is exact at extreme points of the flow polytope** — and a genuine path *is* an extreme point. That single lemma is the correctness proof, and it generalizes an RLT result from polytopes to arbitrary closed convex sets.
- **It is first-level RLT specialized to this bilinear structure**: it collapses to a McCormick envelope on real intervals, and is *"as tight as the first level of the Lovász–Schrijver hierarchy… without semidefinite constraints."* It **cannot** be the convex hull in general — that would solve an NP-hard bilinear program in polynomial time.

> [!note] A redundant constraint that stops being redundant
> The **degree constraint** (at most one unit of flow through a vertex) is provably redundant in the classical shortest-path LP. In the MICP it is load-bearing: without it, a five-vertex example admits an optimal solution containing a **disjoint cycle** at a cost *below* the true optimum. Redundancy in a relaxation's ancestor is not redundancy in the relaxation — a good general reflex when transporting formulations.

Against the naive alternative (relax each bilinear with a McCormick envelope), this formulation's median relaxation gap on random instances is near zero versus **29–34%**, and it solves **10–13× faster**.

## Why it is not just "another mixed-integer program"

The framework's engineering claim is about **relaxation tightness**, not expressiveness. Using perspective functions to switch edge costs and vertex/edge constraints on and off, GCS admits a compact MICP formulation whose **convex relaxation is empirically extremely tight**. In practice that means:

1. Solve the relaxation once — a plain LP or SOCP.
2. Read the relaxed binaries `ϕₑ ∈ [0,1]` as **transition probabilities** and round them with a cheap randomized depth-first search.
3. Recover the continuous values with a tiny convex program per candidate path.

The mixed-integer program has been reduced to *the cost of one convex program*, and branch-and-bound never runs ([Marcucci et al. 2022](../../sources/gcs-motion-planning-paper.md) §4.2).

> [!note] The rounding is deliberately randomized, and the footnote explaining why is the sharpest idea in the paper
> Greedily taking the highest-probability edge is *"in general, a bad idea."* When several graph paths encode the same underlying decision — symmetric solutions — the relaxation **splits the probability mass evenly among them**, so a greedy search can pick a *different* decision that happens to concentrate its mass on one edge. Randomized rounding weights the two decisions correctly in expectation. This is a general hazard when interpreting relaxed indicator variables as confidences, and it is not specific to planning.

## The free certificate

Because the relaxation lower-bounds the optimum and the rounded solution upper-bounds it:

```
C_relax  ≤  C_opt  ≤  C_round
δ_opt := (C_round − C_opt)/C_opt  ≤  δ_relax := (C_round − C_relax)/C_relax
```

`δ_relax` costs one subtraction and is an **upper bound on the true suboptimality, per instance**. If the relaxation returns binary `ϕₑ` outright, `δ_relax = 0` and the answer is *proven* optimal with no rounding at all — which is what happened on the 2,500-cell maze in [the planning paper](../../sources/gcs-motion-planning-paper.md) §7.2.

This is a rare property in this wiki's corpus. It is the structural opposite of [robot policy evaluation](robot-policy-evaluation.md), where a learned policy's quality is estimable only by rollouts (±2 pp needs ≈1,030 of them) and never per-instance. Here the answer arrives with its own error bar, before the robot moves.

## Instance: collision-free motion planning

The wiki's primary source is the **motion-planning instantiation**, which is also the name of the resulting planner ([Marcucci, Petersen, von Wrangel & Tedrake 2022 / Science Robotics 2023](../../sources/gcs-motion-planning-paper.md)):

| GCS element | Motion-planning meaning |
|---|---|
| Vertex `i` | A convex **safe region** `Qᵢ ⊆ Q` of collision-free configurations |
| Edge `(i,j)` | `Qᵢ ∩ Qⱼ ≠ ∅` — the regions overlap, so the trajectory can cross |
| `x_v` | Control points of two **Bézier curves**: trajectory segment `rᵢ` and time-scaling `hᵢ` |
| `X_v` | Control points in `Qᵢ` (⇒ whole segment collision-free, by the convex-hull property); velocity limits |
| `X_e` | `Cη` continuity between adjacent segments; boundary conditions at σ/τ |
| `ℓ_e` | Weighted duration + path length + energy |

Two choices carry the construction:

- **Bézier curves turn infinite constraint families into finitely many.** `rᵢ(s) ∈ Qᵢ ∀s ∈ [0,1]` becomes `d+1` constraints on control points. The alternative — sums-of-squares polynomials — parameterizes a richer trajectory class but demands **semidefinite** programming; Bézier gives a more stringent condition at SOCP cost. That tradeoff is what lets the planner reach `C⁴` trajectories (needed for quadrotor differential flatness) where SOS-based mixed-integer planners cannot.
- **Decoupling shape from timing** via a path coordinate `s` with `t = h(s)` makes trajectory *duration* a decision variable without introducing nonconvexity. The price is that costs and constraints on `q̈` and higher become nonconvex in `(r,h)` — hence the framework's central limitation: **no dynamics, no task-space constraints, no contact.**

## Instance: optimal control of hybrid systems

The framework paper's own target application is **not** motion planning — it is **piecewise-affine (hybrid) optimal control**, and the mapping is worth knowing because it is the template for casting any mode-switching problem into GCS:

| GCS element | Hybrid-control meaning |
|---|---|
| Vertex | One `(time step, discrete mode)` pair; `T` layers of `\|N\|` modes, consecutive layers fully connected |
| `X_v` | That mode's compact convex state-and-control region `D_ν` |
| `ℓ_e` | Stage cost `γ(s_u, a_u)` **if** `s_v = A_ν s_u + B_ν a_u + c_ν`, **∞ otherwise** — the dynamics enter as an infinite-length edge |
| Path | The mode sequence *and* the trajectory, chosen jointly |

> [!note] The modeling decision that produces the speedup, in the authors' words
> *"We do not use binary variables to encode the discrete mode in which the system is at each time step but, instead, we use them to select the **transitions** between modes. This different parameterization yields slightly larger but much stronger MICPs."*
>
> The graph is **quadratic** in the mode count rather than linear. On a PWA double integrator across 7 regions with mode-dependent controllability (`T = 30`, `|V| = 212`, `|E| = 1435`, sets in `ℝ⁶`): the prior state-of-the-art perspective formulation gives a **93% relaxation gap in 17 minutes**; this one gives **20% in 7.1 s** — ~142×. And the relaxed solution is *legible*: it avoids the low-controllability regions and clusters along the true optimum, where the baseline's relaxation heads straight at the goal with uninformative mode indicators.

This matters for how the wiki files GCS. The motion planner is the famous instance; the framework is a **general mixed-integer modeling technique** whose most-improved application is [hybrid MPC](optimal-control.md), and whose reach — per the framework paper's appendix — extends to TSP- and MST-with-neighborhoods and other graph problems with continuous vertex positions.

## Where it sits in the planning taxonomy

GCS is filed under **optimization-based** planning ([motion planning](motion-planning.md)), but the authors argue it **generalizes PRM**: *"each collision-free sample is expanded to a collision-free convex region, that is inflated as much as the obstacles allow; reducing in this way a dense roadmap to a compact GCS."* Empirically, **8 IRIS regions replaced a 15,000-sample roadmap** on a 7-DoF arm, and beat it on trajectory length and runtime on all five benchmark tasks.

That reframing matters more than the benchmark: the optimization-based family **absorbs** the roadmap idea rather than competing with it, and the multi-query/single-query distinction survives the move (GCS is multi-query — the graph is reusable across start/goal pairs).

> [!warning] This complicates the wiki's own summary of optimization-based planning
> [Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md), the survey behind the [motion planning](motion-planning.md) page, files optimization-based planners as *"fast, high-quality when they work; local minima on non-convex problems"* and lists GCS among them in a single clause. For GCS's restricted problem class the characterization is **wrong in the direction that matters**: it returns global optima and certifies them. The correct qualifier is not "local minima" but **"restricted problem class"** — kinematic, convex-decomposable free space, no dynamics or task-space constraints. The tradeoff moved from *reliability* to *modelling power*, which is a different critique.

## Deployment status

**GCS is in production, in exactly one publicly named place, in exactly the regime its restrictions permit.** [Dexai Robotics](../../entities/dexai-robotics.md) replaced a *"pretty optimized"* PRM planner with GCS in shipping food-assembly robots ([Tedrake seminar](../../sources/tedrake-gcs-foundation-models-talk.md) 34:13; [ARM Institute](../../sources/arm-institute-gcs-dexai-project.md), which reports commercial transition, multiple customer sites, and >$10k/robot/year).

The qualifying condition is the content of the finding:

> *"In a setting where you're going to be making plans all day long, you're willing to precompute once, it makes a lot of sense. I think it just really clobbers that problem."*

Fixed workcell ⇒ the offline decomposition amortizes to nothing. Thousands of queries against one graph ⇒ multi-query pays. Free-space transit only ⇒ no dynamics, contact, or task-space constraint needed. Cycle time = revenue ⇒ the customer already measures the axis GCS optimizes. Tedrake makes the same point negatively for the mobile-manipulator case, where he expects the answer to *"change completely"* — fast approximate covers straight from perception, not precomputed optimal ones.

So the correct summary is **narrow deployment, load-bearing**: proof that the niche is real and monetizable, not evidence of general adoption. Note also that the strongest published evidence is a **spoken remark from April 2024**; nothing in this wiki tracks what happened since.

## Extensions past the paper's stated limits

The [2022 paper](../../sources/gcs-motion-planning-paper.md) lists its limits plainly; the [2024 seminar](../../sources/tedrake-gcs-foundation-models-talk.md) shows each one being attacked, mostly successfully:

| Limit as published | Status in 2024 |
|---|---|
| Euclidean C-space only | **Geodesic convexity** — planning on manifolds (SO(2) mobile bases, continuous-rotation joints) |
| No task-space constraints | **Analytical IK used to build regions on the constraint manifold** — bimanual "hands stay together" as a hard constraint |
| Hand-placed IRIS seeds | **Visibility-graph clique cover** (above) |
| No contact | **Spectrahedra as vertices** (below) |
| A plan, not a policy | **The GCS dual is a lower bound on the value function** (below) |

**Contact.** Quasi-static planar pushing has SO(2) constraints and force × distance bilinear terms — a **QCQP**. Take the standard SDP relaxation, add strengthening constraints exploiting SO(2) structure, and the feasible set is a **spectrahedron**, which is convex — so it can be a GCS vertex. One spectrahedron per contact mode; solve the whole thing as a shortest path. The bar is deliberately lowered: the relaxation *"doesn't have to be perfect… it just has to be strong enough to help you know which path to take through the graph"* — push from this side or that — after which local nonconvex cleanup is easy. A correction to a decade of contact-graph literature falls out: the combinatorial hardness is **not** making/breaking contact (that can be smoothed) but **which side you contact on**.

**Policies.** In ordinary shortest-path LP the duals are the cost-to-go; in GCS the dual is a **piecewise-affine lower bound on the value function over every set**. Make it quadratic or polynomial and it becomes an [SOS](../learning/formal-verification.md) program with tighter bounds — one offline solve covering all initial conditions. Pushing the piecewise-quadratic value function back to the primal looks like **propagating probability distributions through the graph**, with higher-order polynomials ↔ higher moments, which is a route to planning under uncertainty. This is GCS reaching into [dynamic programming](optimal-control.md), and it is the technical basis for Tedrake's "GCS as robotics' missing MCTS" pitch.

**Beyond shortest paths.** A box-shuffling TAMP instance turned out to need a walk on the **permutohedron** rather than a shortest path, because box order is irrelevant. The generalizable advice: ask what network-flow problem your combinatorial structure reduces to when the sets shrink to points; if that flow has a good convex formulation, its GCS extension probably does too — and if it is NP-hard (TSP), GCS will not rescue it.

## Where the relaxation is loose

**Symmetry is the characteristic failure, and it now has three independent sightings.** The relaxation splits flow evenly between equal-cost routes and places the surrogate points where neither alone would be legal: it is why the planner's rounding [must be randomized](../../sources/gcs-motion-planning-paper.md) (footnote 3), it is the [framework paper](../../sources/shortest-paths-in-graphs-of-convex-sets-paper.md)'s own §9.4 counterexample (5% gap in the illustration, **100%** in a variant — *"our relaxation can, in principle, be arbitrarily loose"*), and it is what [Tedrake reports](../../sources/tedrake-gcs-foundation-models-talk.md) seeing on a UAV that routed the long way around rather than through **one of two near-identical windows** (57:35).

**And the loosening is measurable, with a counterintuitive shape.** On 500 random instances (squared-Euclidean lengths), worst-case relaxation gap by batch: nominal **2.1%**, large sets **9.1%**, dimension 4→20 **28.9%**, edges 100→500 **32.9%** — then vertices 50→250 at the *same* 500 edges drops it back to **5.3%**. It is **graph density, not graph size**, that hurts (cycles are the mechanism), which is the opposite of the intuition most people bring from search. With plain Euclidean lengths the relaxation is tight almost everywhere regardless. There is also a genuine dial: **smaller regions make convex approximations of nonlinear dynamics tighter but enlarge the discrete problem** — *"you can move the work from the convex optimization into the discrete problem and vice versa."*

The scaling limit is stated by its own author: *"I don't think we can solve dexterous hands with GCS as it is. The graph gets too big. I need help"* (61:19). His proposed fix is to have a learned generalist policy propose which nodes to expand — the MCTS move — which as of that talk is a plan, not a result.

## What it requires that nobody counts — and what has since been automated

A GCS needs its convex sets **supplied**. For a polyhedral world the decomposition is exact; for a real manipulator's configuration space it comes from **IRIS**-style region inflation around seed configurations — and in the primary source those **seeds were placed by hand via inverse kinematics**, with the graph's connectivity checked visually. Automatic seeding was called "certainly possible" and not done. This was the framework's equivalent of the reward-shaping labor in RL or the demonstration-collection labor in [imitation learning](../learning/imitation-learning.md): real, offline, human, and absent from the runtime table.

**By 2024 it was done** ([Tedrake seminar](../../sources/tedrake-gcs-foundation-models-talk.md), 28:14–30:07). The replacement is a **visibility graph plus approximate minimum clique cover**:

1. Sample configurations; connect any two that see each other along a straight collision-free line (distance-independent, unlike a PRM's k-nearest wiring).
2. A **clique in the visibility graph almost corresponds to a convex set in the underlying space** — so an approximate minimum clique cover says where to put the regions.
3. Iterate to patch coverage gaps.

Described as *"almost turnkey convex decomposition algorithms."* The clique↔convexity correspondence is the load-bearing idea and it is worth stating on its own: mutual straight-line visibility is a *combinatorial* proxy for convexity, so the geometric question "where do the convex sets go?" becomes a graph problem you already know how to approximate.

> [!note] The residual labor moved rather than vanished
> The paper's manual step was *seeding*; the remaining judgment call is **coverage policy**. Tedrake's own guidance is to give up on completeness — *"for higher dimensions, I think that trying to cover every nook and cranny of the configuration space is a false goal,"* preferring to initialize the clique cover from samples representing the *important* regions (*[Robotic Manipulation](https://manipulation.csail.mit.edu/trajectories.html)*, Ch. 6 — live-web reference, not an ingested source). Which regions matter is a task-design decision, not an algorithmic one.

## Related concepts

- [Motion planning (classical)](motion-planning.md) — the taxonomy this sits in; GCS is the optimization-based family's strongest result.
- [Optimal control](optimal-control.md) — the shared trajectory-optimization machinery. GCS is the corner where the problem is made *convex by construction* rather than solved locally; the price is dropping the dynamics constraint that defines OC.
- [Task and motion planning](task-and-motion-planning.md) — the symbolic layer above. A motion primitive that returns a per-query optimality bound is a better thing for a task planner to call than one that returns "some path."
- [Formal verification](../learning/formal-verification.md) — the certificate is a proof obligation discharged numerically; same family of ambition, different mechanism.
- [Behavior trees](behavior-trees.md) — the other formalism this wiki tracks that buys **legibility of composition**; GCS buys legibility of *optimality*.

## Key references

- [Motion Planning around Obstacles with Convex Optimization](../../sources/gcs-motion-planning-paper.md) — Marcucci, Petersen, von Wrangel & Tedrake; arXiv 2205.04422, Science Robotics 8(84) 2023. **The primary source for this page** and the motion-planning instantiation.
- [Shortest Paths in Graphs of Convex Sets](../../sources/shortest-paths-in-graphs-of-convex-sets-paper.md) — Marcucci, Umenberger, Parrilo & Tedrake; arXiv 2101.11565, **SIAM J. Optimization 34(1) 2024**. **The framework paper**: the perspective-based MICP, the set-based bilinear relaxation, the NP-hardness proofs, and hybrid-system optimal control as the target application. The planning paper treats this as *"a modeling language."*
- Marcucci et al., *Temporal Logic Motion Planning with Convex Optimization via Graphs of Convex Sets* (T-RO 2023) — GCS + LTL specifications. Not ingested.
- [Planning with Graphs of Convex Sets (in the age of foundation models)](../../sources/tedrake-gcs-foundation-models-talk.md) — MIT Robotics Seminar, 2024-04-07. **The status-report source**: deployment, automatic seeding, contact, policies, and the honest scaling limit.
- [Drake](../../entities/drake.md) — ships the SPP-in-GCS implementation and `IrisInConfigurationSpace`.
- *Robotic Manipulation* (Tedrake, [manipulation.csail.mit.edu](https://manipulation.csail.mit.edu/trajectories.html) Ch. 6) — the practitioner's version: keep costs simple (joint-centering quadratic), don't chase full coverage in high dimensions. Live-web reference, not ingested.

## Mentioned in

- [Motion Planning around Obstacles with Convex Optimization (GCS)](../../sources/gcs-motion-planning-paper.md) — the motion-planning instantiation.
- [Shortest Paths in Graphs of Convex Sets](../../sources/shortest-paths-in-graphs-of-convex-sets-paper.md) — **the framework itself**; MICP construction, relaxation analysis, hybrid control.
- [Planning with Graphs of Convex Sets (in the age of foundation models)](../../sources/tedrake-gcs-foundation-models-talk.md) — the 2024 seminar; deployment and extensions.
- [Time-Optimal Motion Planning Using Convex Sets (ARM Institute)](../../sources/arm-institute-gcs-dexai-project.md) — the corroborating deployment record.
- [The State of Robot Motion Generation (Bekris et al. 2024)](../../sources/state-of-robot-motion-generation-2024.md) — names GCS among optimization-based planners, in one clause.
