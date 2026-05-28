---
title: Optimal control
type: concept
created: 2026-05-14
updated: 2026-05-15
sources: 9
tags: [optimal-control, mpc, lqr, pontryagin, hamilton-jacobi-bellman, dynamic-programming, brachystochrone, calculus-of-variations, control-theory, rl-bridge]
---

**Optimal control** — the mathematical theory of choosing a control signal `u(t)` for a dynamical system `q̇ = f(q, u, t)` so as to minimize an objective `J = ∫ L(q, u, t) dt + Φ(q(T))` over a trajectory. Born **1696–1697** with [Johann Bernoulli's brachystochrone problem](../../sources/sussmann-willems-1997-300-years-optimal-control.md); reached its modern form with **Pontryagin's Maximum Principle (1956)** and **Bellman's dynamic programming (1957)**. Every wiki-tracked world model + planner ([LeWM](../../entities/leworldmodel.md), [DINO-WM](../../entities/dino-wm.md), [V-JEPA 2-AC](../../entities/v-jepa-2.md), [TD-MPC2](../../sources/td-mpc2-paper.md), [DreamerV3](../../sources/dreamer-v3-paper.md)) is doing some form of optimal control over its learned dynamics model.

## The problem class

```
minimize  J = ∫₀ᵀ L(q, u, t) dt + Φ(q(T))          (running cost + terminal cost)
subject to  q̇(t) = f(q(t), u(t), t)                 (dynamics)
            q(0) = q₀                               (initial state)
            u(t) ∈ U                                (control constraints)
            g(q(T)) = 0                             (terminal constraints, optional)
```

Three structural ingredients distinguish optimal control (OC) from the simpler **calculus of variations** (CoV) it grew out of, per the central argument of [Sussmann & Willems 1997](../../sources/sussmann-willems-1997-300-years-optimal-control.md):

1. **Dynamical constraints `q̇ = f(q, u, t)`** — the trajectory is determined by the control through a differential equation, not free to vary arbitrarily as in CoV.
2. **Control-set constraints `u ∈ U`** — `u` lives in a bounded set (saturated actuators, energy budgets); the optimum may lie on the boundary, where CoV's stationarity conditions fail.
3. **Free terminal time `T`** (often) — when does the trajectory end? Minimum-time problems take `L ≡ 1`, so only the dynamics matter.

OC ⊋ CoV: the calculus of variations is the special case where `u = q̇` (control = velocity, no separation), `U = ℝᵐ` (unbounded), and `T` is fixed.

## Three classical solution paths

### 1. Euler–Lagrange (1755, the variational approach)

When `U = ℝᵐ` (no control constraints), set the first variation of `J` to zero:

```
d/dt (∂L/∂q̇) = ∂L/∂q                       (Euler–Lagrange equation)
∂²L/∂q̇² ≥ 0                                (Legendre's 2nd-order necessary condition)
```

Works for the [brachystochrone](../../sources/sussmann-willems-1997-300-years-optimal-control.md) (Bernoulli's solution → cycloid via Fermat's least-time + Snell's law), geodesics, classical mechanics — but breaks the moment `u` is bounded.

### 2. Hamilton–Jacobi–Bellman / dynamic programming (1834 / 1957)

Define the **value function** `V(q, t)` = optimal cost-to-go starting from state `q` at time `t`. It satisfies the **HJB partial differential equation**:

```
−∂V/∂t = min_u [ L(q, u, t) + ∇V(q, t) · f(q, u, t) ]    (HJB)
V(q, T) = Φ(q)                                            (terminal BC)
```

The **Hamiltonian** `H(q, p, u, t) = L(q, u, t) + p · f(q, u, t)` where `p = ∇V` (the *costate*). Optimal `u*(q, t) = argmin_u H`.

**This is the discrete-time Bellman optimality equation when you discretize time** — exactly the equation that grounds [reinforcement learning](../../sources/sutton-barto-rl-textbook.md). HJB is RL's parent.

### 3. Pontryagin's Maximum Principle (1956)

The *inequality* form. Handles bounded controls correctly via the maximum-principle inequality. Introduce a **costate** `p(t)` (the Lagrange multiplier on the dynamics constraint):

```
q̇* = ∂H/∂p             (state dynamics)
ṗ* = −∂H/∂q             (costate dynamics — backward in time)
u*(t) = argmin_{u ∈ U} H(q*(t), p*(t), u, t)   (maximum principle — pointwise!)
```

The control is chosen *pointwise in time* to minimize the Hamiltonian — and crucially, that minimum may sit on the boundary of `U` ("bang-bang control"). Time-optimal trajectories on a robot with saturated motors are textbook PMP problems.

**Relationship between the three** (per [Sussmann & Willems](../../sources/sussmann-willems-1997-300-years-optimal-control.md)):
- Euler–Lagrange is PMP with `U = ℝᵐ` (interior optimum).
- HJB → PMP via the method of characteristics; PMP is "the necessary condition you can solve numerically when the value function is too hard to compute."
- PMP is the *inequality version* of Euler–Lagrange (via the **Weierstrass excess function**, 1879).

## Modern computational instances

| Instance | Setting | Where in this wiki |
|---|---|---|
| **LQR — Linear Quadratic Regulator** | Linear dynamics `q̇ = Aq + Bu` + quadratic cost. HJB has a closed-form Riccati-equation solution. The "easy case" everyone learns first. | DS4DS 7.03–7.05 in [DS4DS 7.01 intro](../../sources/ds4ds-7-01-optimal-control-intro.md) |
| **MPC — Model Predictive Control** | Solve a finite-horizon OC problem online at each step, execute the first action, replan. **Receding-horizon** approximation of the full problem. | Glossary [MPC](../../glossary.md#mpc); [LeWM](../../entities/leworldmodel.md), [DINO-WM](../../entities/dino-wm.md), [V-JEPA 2-AC](../../entities/v-jepa-2.md), [TD-MPC2](../../sources/td-mpc2-paper.md) all use MPC against a learned world model |
| **iLQR / DDP** | Linearize dynamics + quadraticize cost around a nominal trajectory; iterate. Workhorse for trajectory optimization on robots with smooth dynamics. | Implicit in MuJoCo-based work; not yet a wiki source |
| **CEM — Cross-Entropy Method** | Derivative-free sampling-based optimizer. Run inside MPC against a learned world model — sample `K` action sequences, score, fit a Gaussian to the top-`k`, repeat. | [LeWM](../../sources/leworldmodel-paper.md) inner loop, [glossary CEM](../../glossary.md#cem) |
| **HJB / value iteration with NN approximation** | Replace `V(q, t)` with `V_θ(q, t)`. **Approximate dynamic programming.** Stepping-stone to RL. | [DreamerV3](../../sources/dreamer-v3-paper.md), [TD-MPC2](../../sources/td-mpc2-paper.md) |
| **Adaptive control** | Online estimation of unknown parameters in `f`, combined with optimal control law. | [MIT drone adaptive control](../../sources/mit-drone-adaptive-control.md) |

## Connection to reinforcement learning

[Sutton & Barto Ch 4](../../sources/sutton-barto-rl-textbook.md) makes this explicit: **reinforcement learning is approximate optimal control under uncertainty, where you sample from the dynamics instead of differentiating against a known model**. The two perspectives:

| Optimal control | Reinforcement learning |
|---|---|
| Dynamics `f(q, u, t)` known | Dynamics unknown — sample from environment |
| Plan with gradients / HJB / PMP | Estimate value functions from samples |
| Cost `L(q, u, t)` given | Reward `r` given (`r ≈ −L` typically) |
| Deterministic (usually) | Stochastic |
| Solve once, execute open-loop or via feedback law | Update policy online from experience |
| Continuous time + state (often) | Discrete time + state (often) |

Modern **model-based reinforcement learning** ([DreamerV3](../../sources/dreamer-v3-paper.md), [TD-MPC2](../../sources/td-mpc2-paper.md), every JEPA-line world model) is *optimal control over a learned dynamics model*. The whole [Curriculum Module 10 — World models, broad](../../syntheses/curriculum/curriculum-10-world-models.md) thread is "use a neural network to estimate `f`, then run MPC + CEM (or value iteration) against it."

## Why it matters in this wiki

1. **Every learned-world-model paper does OC over its learned `f`.** [LeWM](../../entities/leworldmodel.md) uses CEM-MPC over its trained JEPA. [DINO-WM](../../entities/dino-wm.md) plans with MPC + cross-entropy. [V-JEPA 2-AC](../../entities/v-jepa-2.md) does MPC against the action-conditioned predictor. [TD-MPC2](../../sources/td-mpc2-paper.md) literally has "MPC" in the name + learns a value function for the terminal cost. [PLDM](../../sources/pldm-paper.md), [JEPA-WMs](../../entities/jepa-wms.md) likewise.
2. **Every robot trajectory-tracking system uses LQR / iLQR / MPC.** Drone control ([MIT drone adaptive control](../../sources/mit-drone-adaptive-control.md)), manipulator path-following, walking humanoids ([Atlas](../../entities/atlas.md), [Optimus](../../entities/tesla-optimus.md)).
3. **The OC ↔ RL bridge** is the conceptual link between the wiki's two main control-and-decision-making threads — [Sussmann-Willems 1997](../../sources/sussmann-willems-1997-300-years-optimal-control.md) at one end, [Sutton & Barto](../../sources/sutton-barto-rl-textbook.md) at the other.
4. **Imitation-learning-meets-control hybrids** — [Murray, Gupta & Cakmak 2024](../../sources/murray2024-grasping-clutter-ivfp.md) and [Walker et al. 2024](../../sources/walker2024-explicit-input-teleoperation.md) layer learned components on top of OC primitives. [Learning control-oriented dynamical structure (Murray 2023)](../../sources/learning-control-oriented-dynamical-structure.md) embeds OC priors in the policy architecture itself.

## Historical lineage

```
1696   Bernoulli — brachystochrone challenge (Acta Eruditorum)
1697   Bernoulli + Newton + Leibniz + l'Hôpital + Jacob B. + Tschirnhaus — solutions
1744   Euler — Methodus Inveniendi (systematic calculus of variations)
1755   Lagrange — δ-variation formalism; Euler–Lagrange equation
1786   Legendre — 2nd-order necessary condition
1834   Hamilton — canonical equations
~1840  Jacobi — Hamilton–Jacobi PDE
1879   Weierstrass — excess function (inequality form)
1956   Pontryagin et al. — Maximum Principle (Soviet group)
1957   Bellman — Dynamic Programming + the principle of optimality
1960   Kalman — LQR + Kalman filter (linear-Gaussian closed-form OC)
1970s  Industrial MPC (process control)
1989   Watkins — Q-learning (the RL form of approximate DP)
1997   Sussmann & Willems — tercentenary retrospective
2013+  Deep-RL renaissance: DQN, then AlphaGo, then PPO
2022+  Learned-WM + MPC era: TD-MPC, DreamerV3, LeWM, DINO-WM, V-JEPA 2-AC
```

## Key references

**Primary sources (this wiki):**
- [Sussmann & Willems 1997 — 300 Years of Optimal Control](../../sources/sussmann-willems-1997-300-years-optimal-control.md) — historical retrospective; the field's tercentenary essay. Argues OC was born in 1697 with Bernoulli, not 1956 with Pontryagin.
- [DS4DS 7.01 — Optimal Control, Introduction (Peitz & Wallscheid)](../../sources/ds4ds-7-01-optimal-control-intro.md) — modern open-pedagogy intro; opening lecture of a 7-lesson series covering LQR, linear MPC, data-driven MPC via DMD, differential predictive control. CC BY-SA 4.0 + Julia notebooks.
- [Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed., 2018)](../../sources/sutton-barto-rl-textbook.md) — Ch 4 (Dynamic Programming) is the RL-side bridge to OC; Ch 17.4 ("Designing Reward Signals") flags the brittleness of reward specification that pushed the field from pure RL to OC-over-learned-models.

**Foundational works not yet in the wiki's `raw/`:**
- Bellman, *Dynamic Programming* (Princeton 1957) — the canonical DP reference.
- Pontryagin, Boltyanskii, Gamkrelidze, Mishchenko, *The Mathematical Theory of Optimal Processes* (Wiley 1962) — the Maximum Principle reference.
- Bryson & Ho, *Applied Optimal Control* (1969) — the classical engineering text.
- Bertsekas, *Dynamic Programming and Optimal Control* (Athena Scientific, multiple editions) — the modern graduate textbook; Vol II is the RL-bridge volume.

## Related concepts

- **[Joint-Embedding Predictive Architecture (JEPA)](../world-models/jepa.md)** — JEPA-line world models are the "learn `f` so we can do OC over it" half of the modern recipe.
- **[Latent space](../world-models/latent-space.md)** — the space in which learned-WM OC actually does its planning (CEM samples / gradients live in the latent action / state spaces).
- **[World-model simulators](../world-models/world-model-simulators.md)** — the "model" half of model-based OC. A learned simulator is exactly `f̂(q, u, t)`.
- **[Sim-to-real transfer](../learning/sim-to-real-transfer.md)** — the practical problem: OC plans inside a simulated `f` need to survive deployment against the real `f`.
- **[VLA models](../learning/vla-models.md)** — the *other* dominant 2024–2026 paradigm. VLAs sidestep explicit OC by learning policies via imitation + RLHF instead.

## Open questions

- **`concepts/reinforcement-learning.md` hub page** — the natural RL-side companion to this page. Both Sutton-Barto + this concept hub are now in place; the RL hub remains the most-overdue concept page in the wiki.
- **A `syntheses/optimal-control-and-rl.md` page** — would unify [Sussmann-Willems 1997](../../sources/sussmann-willems-1997-300-years-optimal-control.md) and [Sutton-Barto 2018](../../sources/sutton-barto-rl-textbook.md) into a single "the two foundational books and how to read them in conversation" piece. The two primary sources are now both in the wiki; the synthesis is overdue.
- **iLQR / DDP source page** — workhorse trajectory-optimization algorithm; cited implicitly across the MuJoCo-based literature but no dedicated source.
- **Kalman 1960 LQR paper** — foundational primary source not in `raw/`.
- **Bertsekas DP and OC textbook** — would be the second canonical-textbook ingest (after Sutton-Barto). Vol II in particular is the RL-bridge.
- **The Deadly Triad (Sutton & Barto Ch 11.3)** as a standalone concept page — already flagged in the Sutton-Barto source page's open questions; would explain why naive "approximate DP" fails when the model is learned.

## Mentioned in

Sources with explicit OC vocabulary and a back-link to this hub:
- [Sussmann & Willems 1997 — 300 Years of Optimal Control](../../sources/sussmann-willems-1997-300-years-optimal-control.md) (historical anchor)
- [DS4DS 7.01 — Optimal Control, Introduction (Peitz & Wallscheid)](../../sources/ds4ds-7-01-optimal-control-intro.md) (modern-pedagogy companion)
- [Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed., 2018)](../../sources/sutton-barto-rl-textbook.md) (RL-side bridge)
- [LeWorldModel Paper](../../sources/leworldmodel-paper.md) (CEM-MPC against learned JEPA)
- [TD-MPC2 Paper](../../sources/td-mpc2-paper.md) (MPC + TD-bootstrapped value)
- [DreamerV3 Paper](../../sources/dreamer-v3-paper.md) (latent-imagined-rollouts MBRL = approximate OC)

Aspirationally referenced from this page but not yet linked back from the source (these papers do MPC/planning but don't use the "optimal control" phrase explicitly — back-links pending if/when justified):
- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md), [PLDM Paper](../../sources/pldm-paper.md), [LeJEPA Paper](../../sources/lejepa-paper.md), [Learning control-oriented dynamical structure (Murray 2023)](../../sources/learning-control-oriented-dynamical-structure.md), [MIT drone adaptive control](../../sources/mit-drone-adaptive-control.md), [Onchain AI Garage — LeWM reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md).

Synthesis / curriculum pages that link here:
- [Curriculum Module 8 — RL vocabulary](../../syntheses/curriculum/curriculum-08-rl-vocabulary.md)
- [Curriculum Module 10 — World models, broad](../../syntheses/curriculum/curriculum-10-world-models.md)
- [Curriculum Module 11 — JEPA in depth](../../syntheses/curriculum/curriculum-11-jepa-deep.md)
- [Curriculum Module 12 — LeWorldModel deep-dive](../../syntheses/curriculum/curriculum-12-lewm-deep-dive.md)
