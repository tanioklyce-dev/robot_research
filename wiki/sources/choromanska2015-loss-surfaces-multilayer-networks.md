---
title: "The Loss Surfaces of Multilayer Networks (Choromanska, Henaff, Mathieu, Ben Arous & LeCun, AISTATS 2015)"
type: source
url: https://arxiv.org/abs/1412.0233
fetch_url: https://arxiv.org/pdf/1412.0233v3
local_path: raw/1412.0233v3.pdf
sha256: 55e9800a5f7d92c19c01355d2fb1bf35c825c191ca0fc0f72624e3ee135f9a54
author: "Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, Yann LeCun (Courant Institute, NYU)"
venue: "AISTATS 2015 (JMLR W&CP 38); arXiv v3, 2015-01-21"
published: 2014-11-30
ingested: 2026-09-07
format: "paper, 8 pp. + supplementary (proofs, asymptotics, additional experiments)"
tags: [loss-landscape, spin-glass, random-matrix-theory, critical-points, saddle-points, local-minima, over-parametrization, generalization, statistical-physics, lecun, choromanska, primary-source, foundational]
---

## Summary

**The paper that gave the "many equivalent local minima" folklore a theory — under assumptions its own authors call "possibly unrealistic."** Practitioners in the 2010s had noticed that large networks trained by SGD from different seeds landed at different local minima with nearly the same test error, while small networks were finicky. This paper explains why by mapping the loss of a fully-connected ReLU network to the **Hamiltonian of the H-spin spherical spin glass**, then importing Auffinger, Ben Arous and Černý's random-matrix results on that Hamiltonian's critical points. The picture that comes out: for large networks, **all critical points of low index (few negative Hessian eigenvalues) lie in a narrow band just above the global minimum**; everything above an energy barrier is a high-index saddle with overwhelming probability; the number of local minima *outside* the band **vanishes exponentially with network size**; and reaching the true global minimum takes exponentially long and is, they argue, not worth it — it overfits.

Three things make it worth holding in a robot-learning wiki rather than leaving to the optimization literature. It is the **formal bridge between the spin-glass prehistory of energy-based models** — Hopfield 1982, Boltzmann 1983, already recorded on the [EBM page](../concepts/learning/energy-based-models.md) — and modern training: the earlier work used spin glasses as a model of *the network*; this paper uses one as a model of *the training loss*. It is the origin of the **train/test decorrelation** observation that motivates every "don't chase the global minimum" argument since (Table 1 below). And it is the clean case for asking a question the wiki has held open since the [physics essay](jepa-vs-physics-moudrkat.md): **does any of this transfer to joint-embedding objectives, whose global minimum is the trivial collapsed solution training must avoid?** See [loss-landscape geometry](../concepts/learning/loss-landscape-geometry.md).

## Key claims

### The mapping (§3)

- **A ReLU network's output is a polynomial in the weights** of degree *H* (the depth), with one monomial per **input-to-output path**; ReLUs switch monomials on and off, giving a piecewise polynomial. Eq. 1: `Y = q Σ_i Σ_j X_{i,j} A_{i,j} Π_k w^{(k)}_{i,j}`, with `A_{i,j} ∈ {0,1}` path activity.
- **Three assumptions** turn this into a spin-glass Hamiltonian (Eq. 2, `L(w) = Λ^{-(H-1)/2} Σ X_{i1..iH} w_{i1}…w_{iH}` on the sphere `(1/Λ) Σ w² = 1`):
  1. **Variable independence** — inputs and path activations are i.i.d. (Gaussian inputs, Bernoulli-ρ paths), i.e. a *fully decoupled* model. The authors say plainly that real networks have *"high dependencies"* and that this is the step with no theoretical justification.
  2. **Redundancy in parametrization** — a network with `s ≪ N` unique weights predicts almost as well (Denil et al. 2013: up to 95% of parameters redundant). Theorem 3.2 bounds the sign-correlation of the reduced and full networks by `(1−2ε)/(1+2ε)`.
  3. **Uniformity** — unique weights are spread evenly over the connection graph, so every ordered weight-configuration appears about equally often (Theorem 3.3: `corr ≥ 1/c²`).
- Both **absolute** and **hinge** loss reduce to the same Hamiltonian up to constants (§3.4; details in the supplement). The network's *size* `N` and its *mass* `Ψ` (number of paths) are tied by Theorem 3.1 so that `N → ∞ ⇔ Λ → ∞`.

### The landscape (§4, imported from Auffinger–Ben Arous–Černý 2010)

- **Energy barrier** `E∞(H) = 2√((H−1)/H)`. For large Λ, every critical point of **non-diverging index** lies below `−ΛE∞`; anything above is a high-index saddle *"with overwhelming probability."*
- **Ground state** `−ΛE₀(H)`: finding a critical value below it is improbable. So low-index critical points live in the band `(−ΛE₀, −ΛE∞)`.
- **Layered structure** inside the band: `(−ΛE₀, −ΛE₁)` contains only local minima; `(−ΛE₁, −ΛE₂)` adds index-1 saddles; and so on, with `E_k ↓ E∞`. Corollary 4.1: at any level, minima outnumber index-*k* saddles.
- **Logarithmic complexity** (Theorem 4.1): the expected number of critical points below `Λu` is `≈ e^{ΛΘ_H(u)}`, and local minima dominate saddles *exponentially* as Λ grows — so *"the probability of recovering a saddle point in the band, rather than a local minimum, goes to 0."*
- **Hardness of the global minimum**: the barrier to cross from any band minimum to the ground state is at least `Λ(E₀ − E_i)`, diverging with Λ, and one must climb to where saddles are plentiful to find a path — *"exponentially long time, so in practice finding the global minimum is not feasible."*

### The experiments (§5) — spin glass and MNIST side by side

- **Spin glass**: Λ ∈ {25, 50, 100, 250, 500}, 1,000 SGD runs from random points on the sphere. Small Λ yields many poor minima; large Λ concentrates the loss distribution around the barrier `−E∞`, matching the theory.
- **Networks**: 1,000 one-hidden-layer nets on 10×10 downsampled MNIST, `n₁ ∈ {25, 50, 100, 250, 500}`, 200 epochs. Scaled test-loss distributions **narrow as width grows**, qualitatively matching the spin glass. Variance of test loss falls with width (Fig. 9–10).
- **Redundancy check**: simulated annealing with weights restricted to **3 values in [−1, 1]** loses **< 2.5% accuracy** — the paper's own evidence for assumption 2.
- **Index check**: exact Hessians at solutions for `n₁ ∈ {10, 25, 50, 100}` — all solutions are minima or saddles of **normalized index ≈ 0.01** or below; SGD does at least as well as simulated annealing, so trapping at bad saddles is not what is happening.
- **Train/test decorrelation** (Table 1), Pearson ρ between training and test loss across the 1,000 solutions:

| hidden units | 25 | 50 | 100 | 250 | 500 |
|---|---|---|---|---|---|
| ρ(train, test) | 0.7616 | 0.6861 | 0.5983 | 0.5302 | 0.4081 |

  *"Attempting to find the absolute possible minimum is of limited use with regards to generalization performance."*

### What the authors say it is not

- *"This connection relies on a number of possibly unrealistic assumptions."* Theory is about **training**; experiments are about **generalization**; the two are joined by conjecture (*"We conjecture that both simulated annealing and SGD converge to the band of low critical points"*).
- The spin-glass ↔ network connection itself is old (Amit, Gutfreund & Sompolinsky 1985; Nakanishi & Takayama 1997 on Hopfield); the novelty is using it for the **optimization landscape** rather than the network's dynamics.
- Dauphin et al. 2014 had shown the saddle-point picture *empirically* with no theory; this supplies the theory for the decoupled case.

> [!note] How this reads in 2026
> The paper's practical conclusion — that over-parameterized networks are easy to optimize and that the *global* minimum is neither reachable nor desirable — became conventional wisdom and was refined rather than overturned: [Entropy-SGD](chaudhari2017-entropy-sgd.md) two years later found that SGD's minima are *flat* (Hessian mostly near zero) and argued **width, not depth, of the basin** is what generalization tracks — and reported wide valleys sitting *deeper* than the minima SGD finds, *"in contrast to theoretical models… which predict multiple equivalent local minima with the same loss."* So the "all minima equivalent" reading of this paper was already being qualified by its own coauthors within two years. The decoupling assumption has never been removed; the results are best read as a statement about a *class* of random landscapes that real losses resemble empirically.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — senior author; his statistical-physics thread, five years before the [Les Houches lectures](dawid-lecun-lvebm-lecture-notes.md).
- [Anna Choromanska](../entities/anna-choromanska.md) — first author; also on [Entropy-SGD](chaudhari2017-entropy-sgd.md).
- Gérard Ben Arous — the probabilist whose spin-glass complexity results (with Auffinger and Černý) the paper imports; no entity page.

## Concepts touched

- [Loss-landscape geometry](../concepts/learning/loss-landscape-geometry.md) — the concept page this source anchors.
- [Energy-based models](../concepts/learning/energy-based-models.md) — the spin-glass prehistory; here the spin glass models the loss, not the network.
- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) — the same random-matrix tradition (Wigner 1958 is cited) applied to a different object.
- [JEPA](../concepts/world-models/jepa.md) — the open question: joint-embedding losses have a trivial global minimum, and this analysis has no term for that.

## Open questions

- **Does anything here transfer to joint-embedding objectives?** The whole analysis assumes the global minimum is *desirable* and merely hard to reach. In predictive SSL the global minimum is collapse. Whether the "band of good minima" survives when a large trivial basin is added to the landscape is exactly what the [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) would want to know, and nobody in this wiki has asked it formally.
- **Was the decoupling assumption ever removed?** The follow-up *"Open Problem: The landscape of the loss surfaces of multilayer networks"* (Choromanska, LeCun & Ben Arous, COLT 2015) posed it as open. Not ingested; status unknown here.
- **Width, not depth.** Every experiment varies hidden units at depth 1. The theory's `H` is depth; the experiments never move it.
