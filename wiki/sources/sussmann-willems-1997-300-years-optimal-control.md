---
title: "300 Years of Optimal Control: From the Brachystochrone to the Maximum Principle (Sussmann & Willems, IEEE CSM, 1997)"
type: source
url: https://doi.org/10.1109/37.588098
local_path: raw/300Years_Of_Optimal_Control.pdf
author: Hector J. Sussmann (Rutgers), Jan C. Willems (Groningen)
affiliation: Department of Mathematics, Rutgers University (Sussmann; partly supported by NSF Grant DMS95-00798 and AFOSR Grant 0923); Department of Mathematics, University of Groningen (Willems)
published: 1997-06 — IEEE Control Systems Magazine, Vol. 17, No. 3, pp. 32–44 ("Historical Perspectives")
ingested: 2026-05-14
tags: [optimal-control, history, calculus-of-variations, brachystochrone, pontryagin-maximum-principle, hamilton-jacobi-bellman, euler-lagrange, weierstrass, foundational, ieee-csm]
---

> [!note] Ingest depth
> The PDF is **image-only / scanned**, so text extraction returns empty pages. Ingest is therefore based on **page-by-page visual reading of the 13 rendered images** (`pdftoppm -r 150 -png` → `/tmp/300y-*.png`), with verbatim quotations transcribed by eye where they appear in the body below. Cross-checked against the title in the PDF metadata (`/Title: "300 Years Of Optimal Control: From The Brachystochrone to the Maximum Principle - IEEE Control Systems Magazine"`).

## Summary

**"300 Years of Optimal Control: From the Brachystochrone to the Maximum Principle"** — Hector J. Sussmann (Rutgers Mathematics) and Jan C. Willems (Groningen Mathematics), IEEE Control Systems Magazine, June 1997, "Historical Perspectives," pp. 32–44. A 13-page tercentenary essay arguing that **optimal control was born in 1697, in Groningen, with Johann Bernoulli's solution of the brachystochrone problem** — *not* in the 1950s with Pontryagin's Maximum Principle, as conventional wisdom holds.

The opening sentence sets the tone:

> "Optimal control was born in 1697 — 300 years ago — in Groningen, a university town in the north of The Netherlands, when Johann Bernoulli, professor of mathematics at the local university from 1695 to 1705, published his solution of the brachystochrone problem."

The authors openly admit a "professional and nationalistic" bias — Willems was Bernoulli's successor at Groningen, Sussmann was a professor there once — but use that bias to drive a precise technical argument: **optimal control is broader than the calculus of variations**, and the *modern* form of optimal control (with dynamic constraints, free time, and the Maximum Principle) is the natural completion of the program Bernoulli started in 1696.

**Why this matters to this wiki.** The wiki has been accumulating sources that ride on optimal-control machinery — [Model Predictive Control (MPC)](../glossary.md#mpc) in [LeWM](../entities/leworldmodel.md) / [DINO-WM](../entities/dino-wm.md) / [V-JEPA 2-AC](../entities/v-jepa-2.md); the **[Cross-Entropy Method (CEM)](../glossary.md#cem)** used as the MPC inner-loop optimizer; [TD-MPC2](../sources/td-mpc2-paper.md); [meta-learning adaptive control](../sources/mit-drone-adaptive-control.md); the [Murray–Gupta–Cakmak](../sources/murray2024-grasping-clutter-ivfp.md) and [Walker 2024](../sources/walker2024-explicit-input-teleoperation.md) IL/control-theory hybrids — without a primary-source anchor for *what optimal control even is, historically and mathematically*. This article is that anchor. It is also the natural pre-read for any "control theory" concept page the wiki spawns from future ingests.

## Article structure (section-by-section)

The article runs 13 pages, with the following sections:

1. **Opening** (p. 32) — Optimal control born 1697 in Groningen; the authors confess a nationalistic bias; brachystochrone as the founding problem.
2. **Before 1696** (p. 33) — Optimization problems traceable to the Greeks (shortest path; Heron's principle for light reflection — angle of incidence = angle of reflection; Dido's problem — isoperimetric inequality, fixed perimeter to maximize area).
3. **Bernoulli's Challenge** (p. 33, sidebar) — Verbatim translation of the *Acta Eruditorum* June 1696 challenge: *"If in a vertical plane two points `A` and `B` are given, then it is required to specify the orbit `AMB` of the movable point `M`, along which it, starting from `A`, and under the influence of its own weight, arrives at `B` in the shortest possible time."*
4. **1696–1697: The Watershed** (p. 33) — Solutions submitted by Johann Bernoulli, Jacob Bernoulli, Newton, Leibniz, Tschirnhaus, l'Hôpital. (Famous Newton anecdote: solved it in 12 hours and submitted anonymously; Bernoulli recognized him by *"recognizing the lion by his claws"* — *"ex ungue leonem."*) The "first calculus-of-variations problem" enters the historical record.
5. **Why Optimal Control?** (p. 34) — The central argument. The "conventional wisdom" that optimal control was born ~40 years ago with Pontryagin's Maximum Principle is challenged. The authors distinguish:
   - **Calculus of variations**: minimize `I = ∫_a^b L(q, q̇, t) dt` (or `J = ∫_a^b f_0(x, ẋ, t) dt`) over "all" curves `q : [a, b] → R^n` with endpoint constraints. The minimization is over a function space — that's the defining feature.
   - **Optimal control**: minimize over **trajectory-control pairs `(q, u)`** where `q̇(t) = f(q(t), u(t), t)` is a *dynamical constraint* and `u` is the **control function**. Two interesting structures — the dynamics `f` and the functional `J` — instead of one. At the extreme, `L ≡ 1` gives **minimum-time problems** where *only* the dynamics matter — the problems where the difference between OC and CoV is most clearly seen.
6. **Bernoulli's Solution of the Brachystochrone Problem** (pp. 35–36) — Modern formulation: `B ⊂ R²`, `f : [0, T] → R²` Lipschitz, `f(0) = (0, 0)`, `f(T) = (a, b)`, minimize `(1/√(2g)) ∫_0^T √(f₁'² + f₂'²) / √(f₂) dt`. Bernoulli's *trick*: connect to **Fermat's least-time principle** — a light ray in a medium where the speed of light varies with depth follows the brachystochrone. Then **Snell's law** at every depth: `sin α / v = constant` (where `α` is angle from vertical and `v` is the local speed `√(2g·y)`). This gives a first-order ODE for the path — and integrating it yields the **cycloid** `x(θ) = (C/2)(θ − sin θ), y(θ) = (C/2)(1 − cos θ)`. (Bernoulli's elegant analogy is the historical first appearance of what is now called the **Hamilton–Jacobi viewpoint**: the optimum is a level set of a value function.)
7. **Johann Bernoulli and his Family** (pp. 36–37) — Biographical excursion. Johann (1667–1748) and Jacob (1654–1705) Bernoulli; the pedagogical-priority quarrels with their students (including a young Daniel Bernoulli); the propagation of the calculus of variations from Basel into the Paris Academy via Maupertuis and l'Hôpital.
8. **Euler, Lagrange, Legendre** (pp. 38–39) — The mathematical apparatus, late 1700s. With Johann and Jacob Bernoulli, Leibniz, Tschirnhaus, Newton, and l'Hôpital on the brachystochrone, **Euler** entered the University of Basel at 13 and became a student of Johann Bernoulli, who gave him private lessons once a week. In Basel Euler worked on isoperimetric problems in 1732 and 1736. In 1744 he published *Methodus Inveniendi Lineas Curvas Maximi Minimive Proprietate Gaudentes* (the first systematic treatment of the calculus of variations). The **Euler–Lagrange equation** appears (Eq. 10): `(d/dt) ∂L/∂q̇ = ∂L/∂q`, with **Legendre's second-order necessary condition** `∂²L/∂q̇² ≥ 0` (Eq. 13). Lagrange (12 January 1755, age 19, to Euler) introduced systematic variations of the curve `q`. *"From this `δ` we get the differential and integral calculus of variations."* The transformation from the geometric Bernoulli-style argument to the analytic Euler–Lagrange framework is complete.
9. **The First Fork in the Road: Hamilton** (pp. 39–40) — The Legendre transform `p = ∂L/∂q̇` and the resulting **Hamilton's equations** (Eq. 19, 20): `q̇ = ∂H/∂p, ṗ = −∂H/∂q`, with `H(q, p, t) = pq̇ − L(q, q̇, t)`. Defines the **Hamiltonian** `H` as the modern object that subsumes the Euler–Lagrange equation. The article carefully credits the geometric viewpoint (Hamilton 1834) and the analytic (Jacobi). This is the route from CoV to **Hamilton–Jacobi PDEs** — the value-function-as-PDE viewpoint that ultimately fuses with Bellman's dynamic programming in the 20th century.
10. **The Second Fork in the Road: Weierstrass** (pp. 40–41) — Weierstrass (1815–1897) considered the more general form `min ∫_a^b L(q, q̇) dt` *without* a priori homogeneity assumption on `L`. The **Weierstrass excess function** `E(q, ū, v) = L(q, v) − L(q, ū) − ∂L/∂q̇(q, ū) · (v − ū)` (Eq. 25). This identifies the convexity condition that distinguishes a true minimum from a critical point — the conceptual ancestor of **Pontryagin's Maximum Principle** (an *inequality*, not just a stationarity condition).
11. **From Principle to Theorem** (pp. 41–42) — Working out the precise necessary conditions. The authors state **Conjecture MN1**: a `C¹` curve `t → q(t)` is a *solution* (i.e., a local minimum) only if there is a path `p` with `(q̇, ṗ) = (∂H/∂p, −∂H/∂q)` and so on; **Conjecture MN2**: variants of MN1 for free-time problems; **Conjecture MAX1, MAX2**: for problems where the control variable `u` is restricted to lie in some subset `U` of `R^m` and `u` is *not required to be differentiable* — `H(q, u, p, t) = sup_{u ∈ U} H(q, u, p, t)` (Eq. 31). This is the modern statement of the **Maximum Principle** in its precise form.
12. **The Maximum Principle** (pp. 41–43) — The section that completes the historical arc. Pontryagin's group (1956–1958) formalized MAX1/MAX2; the announcement at the 1958 ICM met with **unenthusiastic reaction** (the article quotes L. Markus on this), partly mathematical (looked like a minor calculus-of-variations addition) and partly non-mathematical (Pontryagin's anti-Semitism; suspicion that the result was driven by Soviet military applications). The authors argue the result was, in fact, deep: it captures **inequality constraints on the control** (`u ∈ U`) — the structural feature that distinguishes optimal control from the classical calculus of variations.
13. **Finale for Brachystochrone and Control** (pp. 43–44) — The article closes by re-deriving the brachystochrone *as an optimal-control problem* (rather than as a CoV problem). The control is `u = (cos θ, sin θ)`, with `u ∈ U = unit circle`; dynamics `(ẋ, ẏ) = v(y) · u`. The Hamiltonian `H(x, y, u, v, p, q, p_0) = p · v(y) cos θ + q · v(y) sin θ + p_0`, and the Maximum Principle picks out the optimal `θ(t)`. The result: *the cycloid again* — but now derived as the trajectory–control pair of a free-time optimal-control problem with bounded control. The argument shows that "modern" optimal control swallows Bernoulli's 1697 result whole.
14. **References** (p. 44) — 13 references including L.D. Berkovitz, *Optimal Control Theory* (Springer 1974); E.B. Lee & L. Markus, *Foundations of Optimal Control Theory* (Wiley 1967); H. Goldstine, *History of the Calculus of Variations* (Springer 1980); L.S. Pontryagin et al., *The Mathematical Theory of Optimal Processes* (Wiley 1962); H. Sussmann, "A nonsmooth hybrid maximum principle" (1996); H. Sussmann, "300 Years of Optimal Control: A Postscript to History" (preprint, 1996).

## Key conceptual claims

1. **Optimal control is older than its conventional birthdate.** The 1696 Bernoulli challenge and its 1697 solutions in *Acta Eruditorum* are the historical and conceptual founding of the field — not the 1956 Pontryagin paper. The authors don't dispute that the *name* "optimal control" is mid-20th-century; they argue the *problem class* is 300 years old.

2. **OC ⊋ CoV.** The calculus of variations is a special case of optimal control where the control `u` can be identified with the velocity `q̇` and is *unrestricted*. Optimal control adds two structural elements: (a) **dynamical constraints** `q̇ = f(q, u, t)` separating the trajectory from the control; (b) **inequality / set constraints** `u ∈ U` allowing controls that are not interior to their domain. Both are essential for engineering applications (saturated actuators, energy budgets, minimum-time landing, etc.).

3. **The Maximum Principle is the inequality version of the Euler–Lagrange equation.** Euler–Lagrange + Legendre give a stationary-point condition plus a second-derivative inequality. The Weierstrass excess function generalizes this; Pontryagin's MP completes it for the control-set-constrained case, giving `H(q*, u*, p*, t) = sup_{u ∈ U} H(q*, u, p*, t)` — an inequality that holds at the optimum trajectory–control pair, not just a stationarity equation.

4. **Bernoulli's brachystochrone solution is, in modern language, a Hamilton–Jacobi argument.** The "least-time light ray" analogy gives Snell's law at every point, which is the level-set / wave-front form of the Hamilton–Jacobi equation. Bernoulli got this before the analytic machinery (Euler–Lagrange 1744, Hamilton 1834, Jacobi 1830s) was assembled — a remarkable example of geometric intuition outrunning formal apparatus.

5. **Why the brachystochrone is the canonical optimal-control problem.** It has **bounded control** (the unit-vector direction of motion lives on a circle), **dynamics that depend on state** (speed depends on depth `√(2gy)`), and **a free terminal time** (`T` is part of what you optimize). All three features are absent from the standard textbook CoV setup, and all three are present in modern robotic control problems — including, the authors note, *time-optimal trajectory tracking under actuator saturation*, the problem space that motivates almost every applied optimal-control deployment of the late 20th century.

## Verbatim passages (transcribed from the scanned PDF)

> "Optimal control was born in 1697 — 300 years ago — in Groningen, a university town in the north of The Netherlands, when Johann Bernoulli, professor of mathematics at the local university from 1695 to 1705, published his solution of the brachystochrone problem." (p. 32)

> *Bernoulli's Challenge (Acta Eruditorum, June 1696):* "If in a vertical plane two points `A` and `B` are given, then it is required to specify the orbit `AMB` of the movable point `M`, along which it, starting from `A`, and under the influence of its own weight, arrives at `B` in the shortest possible time." (p. 33, sidebar)

> "The conventional wisdom holds that optimal control theory was born about 40 years ago in the former Soviet Union, with the work on the 'Pontryagin maximum principle' by L.S. Pontryagin and his group … We believe that optimal control is significantly richer and broader than the calculus of variations, from which it differs in some fundamental ways …" (p. 34)

> "The distinctive feature of these problems is that the minimization of [the calculus-of-variations integral] takes place in the space of 'all' curves … Optimal control problems, by contrast, involve a minimization over a set `C` of curves which is itself determined by some dynamical constraints. For example, `C` might be the set of all curves `t → q(t)` that satisfy a differential equation `q̇(t) = f(q(t), u(t), t)` for some choice of the 'control function' `t → u(t)`. … So in an optimal control problem there are at least two objects that give the situation interesting structure, namely, the dynamics `f` and the functional `J` to be minimized." (p. 34)

> "It is in these [minimum-time] problems that the difference between optimal control and the calculus of variations is most clearly seen, and it is no accident that these were the problems …" (p. 34)

## Entities mentioned

- **Johann Bernoulli (1667–1748)** — Groningen, then Basel; brachystochrone challenger; "founder" of optimal control in the authors' framing. Portrait reproduced on pp. 32, 37.
- **Jacob Bernoulli (1654–1705)** — Johann's elder brother; submitted independent brachystochrone solution. (Co-portrait on p. 37.)
- **Isaac Newton, Gottfried Leibniz, Ehrenfried Walther von Tschirnhaus, Guillaume François Antoine, Marquis de l'Hôpital** — submitted brachystochrone solutions in 1696–1697. Newton solved in 12 hours, anonymously.
- **Leonhard Euler (1707–1783)** — student of Johann Bernoulli at Basel; published *Methodus Inveniendi* (1744); Euler–Lagrange equation.
- **Joseph-Louis Lagrange (1736–1813)** — introduced the systematic `δ`-variation calculus at age 19 in correspondence with Euler.
- **Adrien-Marie Legendre (1752–1833)** — second-order necessary condition `∂²L/∂q̇² ≥ 0`.
- **William Rowan Hamilton (1805–1865)** — Legendre transform; Hamilton's canonical equations.
- **Carl Gustav Jacob Jacobi (1804–1851)** — Hamilton–Jacobi PDE.
- **Karl Weierstrass (1815–1897)** — excess function; the conceptual precursor to the Maximum Principle inequality.
- **Lev Semenovich Pontryagin (1908–1988)** — Maximum Principle; ICM 1958 announcement met with "unenthusiastic reaction"; Soviet group included V.G. Boltyanskii, R.V. Gamkrelidze, and E.F. Mishchenko (cited as Pontryagin et al., *The Mathematical Theory of Optimal Processes*, Wiley 1962).
- **Hector J. Sussmann** — Rutgers Mathematics; specializes in nonsmooth MP, geometric control. Wrote a companion essay "300 Years of Optimal Control: A Postscript to History" (1996 preprint, referenced in the bibliography).
- **Jan C. Willems** — Groningen Mathematics; pioneer of behavioral systems theory.
- **L. Markus** — author cited for the historical reaction to Pontryagin's 1958 ICM announcement.

(None of these have wiki entity pages yet. **Johann Bernoulli** and **Lev Pontryagin** are candidate entity stubs if a future "control theory" thread accumulates more sources.)

## Concepts touched

The following concepts are introduced or contextualized by this article and currently lack their own wiki pages — strong candidates for follow-on concept-page creation if the wiki's control-theory coverage deepens:

- **Optimal control** — the umbrella concept. *Not yet a concept page in this wiki.*
- **Calculus of variations** — the historical predecessor. *Not yet a concept page.*
- **Brachystochrone problem** — the founding example.
- **Cycloid** — the brachystochrone solution curve; also the tautochrone and the isochrone.
- **Fermat's principle of least time** — Bernoulli's bridge between mechanics and optics.
- **Snell's law** — the local condition Bernoulli used to derive the cycloid.
- **Euler–Lagrange equation** — `(d/dt) ∂L/∂q̇ = ∂L/∂q`. Modern CoV foundation.
- **Legendre's second-order necessary condition** — convexity in the velocity argument.
- **Hamilton's canonical equations** — `q̇ = ∂H/∂p, ṗ = −∂H/∂q`.
- **Hamilton–Jacobi equation** — the value-function PDE; the conceptual root of dynamic programming.
- **Weierstrass excess function** — convexity-style inequality, conceptual ancestor of MP.
- **Pontryagin's Maximum Principle (PMP / MP)** — the inequality version of Euler–Lagrange for control-set-constrained problems. The headline result that completes the historical arc.
- **Bellman dynamic programming / value function** — implicit in the Hamilton–Jacobi framing (article does not name Bellman, but his work is the 20th-century synthesis).
- **[MPC](../glossary.md#mpc)** — already a glossary entry in this wiki; the receding-horizon practical instantiation of optimal control. The article does not discuss MPC directly (1997 predates the MPC explosion in robotics), but every modern MPC inherits the OC framework Sussmann and Willems lay out.

## Connections to existing wiki content

The wiki has been quietly accumulating control-theory-adjacent sources without an anchor source for the underlying field:

- **[MPC glossary entry](../glossary.md#mpc)** — "Model Predictive Control — at each step, plan a short-horizon action sequence using a model, execute the first action, replan." Pointed at by [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [V-JEPA 2-AC](../entities/v-jepa-2.md). MPC is a *receding-horizon* approximation of the full optimal-control problem Sussmann and Willems describe; the [CEM](../glossary.md#cem) inner loop is a derivative-free way to solve the OC sub-problem at each step.
- **[Curriculum Module 10 — World models, broad](../syntheses/curriculum/curriculum-10-world-models.md)** — discusses MPC + CEM + gradient-based planning over a learned WM. The Sussmann–Willems article is the missing primary-source anchor for the *control side* of that pairing.
- **[TD-MPC2 (Hansen et al.)](td-mpc2-paper.md)** — TD-MPC combines a learned latent dynamics model with MPC and TD bootstrapping. The "MPC" in TD-MPC is exactly the receding-horizon OC the article describes.
- **[Learning control-oriented dynamical structure (Murray 2023)](learning-control-oriented-dynamical-structure.md)** — embeds prior knowledge about the structure of an OC problem into a learned policy.
- **[MIT drone adaptive control (2025)](mit-drone-adaptive-control.md)** — meta-learning the *optimization geometry* of an adaptive controller; the control problem itself is the time-optimal trajectory-tracking problem class described in Sussmann & Willems §13 ("Finale").
- **[Murray–Gupta–Cakmak 2024 — Grasping in clutter with IVFP](murray2024-grasping-clutter-ivfp.md)** — interactive visual failure prediction over a learned grasping policy; the planner is implicitly solving an OC problem (maximize success rate subject to action constraints).

A future "control theory" or "optimal control" concept page would naturally hub from this source. *Logged as a follow-up in [Open questions](#open-questions--tbd) below.*

## Position in the lineage

```
1696   Johann Bernoulli — brachystochrone challenge (Acta Eruditorum, June 1696)
1697   Johann + Jacob Bernoulli, Newton, Leibniz, Tschirnhaus, l'Hôpital — solutions
       Bernoulli's solution = least-time light-ray analogy → Snell → cycloid
1744   Euler — Methodus Inveniendi (systematic CoV)
1755   Lagrange (age 19) → Euler — δ-variation; modern CoV formalism
       Legendre — second-order necessary condition
1834   Hamilton — canonical equations
       Jacobi — Hamilton–Jacobi PDE
1860+  Weierstrass — excess function (inequality form of necessary condition)
1956+  Pontryagin, Boltyanskii, Gamkrelidze, Mishchenko — Maximum Principle
1957   Bellman — Dynamic programming (HJB equation)
1997   Sussmann & Willems — this article (tercentenary essay)
       ↓
2020s  MPC + learned world models (TD-MPC, LeWM, DINO-WM, V-JEPA 2-AC)
       — receding-horizon OC against a neural dynamics model
```

This article sits at the historical hinge: it is the **canonical modern retrospective** on the field that the 2020s control-as-machine-learning literature builds on top of.

## Open questions / TBD

- ✅ **Resolved 2026-05-14:** A wiki [`concepts/optimal-control.md`](../concepts/robotics/optimal-control.md) hub page was created using this article as the historical anchor, paired with [DS4DS 7.01](ds4ds-7-01-optimal-control-intro.md) (modern pedagogy) and [Sutton & Barto](sutton-barto-rl-textbook.md) (RL bridge).
- **A "Bellman & dynamic programming" entity or concept stub.** Not in the article (Bellman's parallel 1950s development is conspicuously absent — the authors focus on the European calculus-of-variations lineage), but essential context for any wiki control-theory thread.
- **The "Postscript to History" preprint** (Sussmann 1996) cited at the end of the bibliography is more technically detailed than this article. Not in the wiki's `raw/`; flagged for possible future ingest if a control-theory thread accumulates.
- **Riemannian-metric formulation of the brachystochrone.** The article mentions (p. 35) that Bernoulli's path is the geodesic of the metric `ds² = (dx² + dy²) / (2gy)` — a clean connection between optimal control and Riemannian geometry. Could feed a "geometric control" concept page in the future.
- **Why was the 1958 ICM reaction unenthusiastic?** The article gives a two-pronged explanation (mathematical taste + Pontryagin's politics). A more careful sociology-of-science synthesis would be possible but is well outside this wiki's scope.
- **Bernoulli–Newton anecdote.** "*Ex ungue leonem*" ("recognized the lion by his claws") — Bernoulli identifying Newton's anonymous brachystochrone solution. Folkloric but commonly cited. The article confirms it as the actual record (p. 36, paraphrased) but doesn't give the primary source.
