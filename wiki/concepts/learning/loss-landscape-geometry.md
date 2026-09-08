---
title: Loss-landscape geometry
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 3
tags: [loss-landscape, spin-glass, critical-points, saddle-points, flat-minima, wide-valleys, local-entropy, hessian-spectrum, generalization, over-parametrization, statistical-physics, collapse]
---

**Loss-landscape geometry** — the study of the shape of a neural network's training loss as a function of its weights: where its critical points are, what their Hessians look like, which of them gradient descent reaches, and which of them generalize. The wiki holds this as a concept because two LeCun-coauthored statistical-physics papers, ingested together, settle one folklore question and open one the wiki's own JEPA thread needs answered.

## Two results, two years apart

| | [Loss Surfaces (2015)](../../sources/choromanska2015-loss-surfaces-multilayer-networks.md) | [Entropy-SGD (2017)](../../sources/chaudhari2017-entropy-sgd.md) |
|---|---|---|
| Question | Why do large networks reach equivalent minima from any seed? | Why do the minima SGD finds generalize, and can we seek better ones? |
| Object | The loss as a random function on the sphere | The Hessian at converged solutions |
| Tool | Map to an H-spin spherical spin-glass Hamiltonian; import random-matrix complexity results | Measure eigenspectra; replace the loss with a local free entropy |
| Finding | Low-index critical points lie in a **band just above the global minimum**; bad minima **vanish exponentially** with size; the global minimum is exponentially hard to reach and **overfits** | SGD's minima are **almost flat** (~94% near-zero eigenvalues), with a long positive and short negative tail; **wide valleys generalize**, and an objective can be biased toward them |
| Status of assumptions | Decoupled inputs and paths — *"possibly unrealistic"*, never removed | Hessian eigenvalue gap for the bound — *"admittedly unrealistic"* |

They compose into the modern picture: **over-parameterized networks are easy to optimize** because almost everything SGD can reach is a low-index critical point near the floor, and **what separates those points is not their loss but their width**. The 2017 paper also qualifies the 2015 one: Entropy-SGD reaches wide valleys with *lower* training loss than SGD's minima, so the minima are not all equivalent after all — the wide ones sit deeper.

## The mechanism, in one paragraph each

**Spin glass.** A ReLU network's output is a degree-*H* polynomial in the weights with one term per input-to-output path. Assume inputs and path activations independent, weights redundant and uniformly spread, and the loss becomes the Hamiltonian of the spherical *H*-spin glass — a Gaussian process on the sphere whose critical-point statistics Auffinger, Ben Arous and Černý had computed. There is an **energy barrier** `E∞ = 2√((H−1)/H)`: above it, essentially all critical points are high-index saddles that descent escapes; below it, low-index points stack in layers — minima first, then index-1 saddles, and so on — and minima dominate exponentially. Train/test correlation falls from 0.76 to 0.41 as width grows from 25 to 500 hidden units, which is the empirical case for not chasing the floor.

**Local entropy.** Replace the loss `f(x)` with `F(x, γ) = log ∫ exp(−f(x′) − γ/2‖x − x′‖²) dx′`, the log-partition function of a Gibbs distribution focused near `x`. Its gradient is `γ(x − ⟨x′⟩)`: a pull toward the *mean* of nearby low-loss weights, which between two neighbouring minima of equal loss points to the wider. Estimate the mean with a few steps of Langevin dynamics — SGD inside SGD. Unlike smoothing the loss, this can prefer a shallower wide valley over a deeper sharp one; unlike classical entropy, it will not prefer a flat high-loss plateau.

## What the wiki takes from it

- **The folklore is grounded, conditionally.** "Local minima are not the problem in deep learning" rests on a decoupled model that resembles real losses empirically. It is a statement about a class of random landscapes, not a theorem about your network.
- **Width is the variable.** Every subsequent flat-minima argument — large-batch sharpness, SAM-style optimizers, the Hochreiter–Schmidhuber 1997 *Flat Minima* paper these authors cite as the ancestor — is downstream of the Hessian-spectrum measurement here. The counter-literature (Dinh et al. 2017, sharp minima can generalize under reparameterization) is not ingested; treat "flat ⇒ generalizes" as a strong regularity with known exceptions.
- **Free energy as an objective is an EBM move.** The [energy-based-models page](energy-based-models.md) records the Les Houches principle that regularized EBM training *bounds the volume of the low-energy region*. Entropy-SGD is the optimizer-side twin: it measures that volume locally and climbs it.

## The question this opens for the JEPA thread

> [!warning] On a joint-embedding loss, the widest valley is collapse — the wiki's own reading, stated by neither paper
> Both papers assume the global minimum is *desirable* and merely hard to reach or not worth reaching. In predictive self-supervised learning the global minimum of the prediction loss is the **constant encoder** — every input maps to one point, prediction error zero — and it is not a point but a vast flat manifold: any encoder that ignores its input works. It is, by construction, the widest low-loss valley in the landscape. Two consequences:
>
> 1. **The 2015 picture does not transfer as stated.** The "band of good minima near the floor" presupposes a floor worth reaching. Add a trivial basin at the floor and the question becomes whether *useful* minima form a band *above* it that descent lands in — which is what the [anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md) has spent eight years engineering, device by device, without a landscape theory to say when it is needed.
> 2. **An Entropy-SGD-style objective would accelerate collapse**, not prevent it, on an unregularized JEPA loss. What [SIGReg](../world-models/sigreg.md), VICReg, EMA teachers and inverse-dynamics terms do, in this language, is **change which minima exist** — remove or narrow the collapsed basin — rather than change which minima the optimizer finds. That is a different intervention from anything in the flat-minima literature, and it may be why the [curriculum](../../syntheses/curriculum/curriculum-04-self-supervised-learning.md) calls collapse "an attractor": it is the landscape's own preference, not a failure of the optimizer.
>
> Testable at low cost: **compute the Hessian spectrum at a converged [LeWorldModel](../../entities/leworldmodel.md) or DINO-WM solution** and compare it with the ~94%-near-zero profile above. If the profile matches, the regularizer has produced a landscape the flat-minima story applies to; if the solution sits on a narrow ridge above a wide collapsed basin, the JEPA training problem is geometrically unlike supervised training and the wiki's anti-collapse ladder is fighting the landscape, not the optimizer.

## Key references

- [Choromanska, Henaff, Mathieu, Ben Arous & LeCun 2015 — The Loss Surfaces of Multilayer Networks](../../sources/choromanska2015-loss-surfaces-multilayer-networks.md)
- [Chaudhari et al. 2017 — Entropy-SGD](../../sources/chaudhari2017-entropy-sgd.md)
- Cited by both and not ingested: Dauphin et al. 2014 (saddle points, empirical); Hochreiter & Schmidhuber 1997 (*Flat Minima*); Baldassi et al. 2015–16 (local entropy for discrete weights); Sagun, Bottou & LeCun 2016 (Hessian singularity); Dinh et al. 2017 (the sharp-minima counter).

## Related concepts

- [Energy-based models](energy-based-models.md) — the spin-glass prehistory (Hopfield, Boltzmann) and the volume-bounding principle.
- [Spectral theory of SSL](spectral-theory-of-ssl.md) — the other place the wiki's LeCun-orbit theory uses spectral and random-matrix tools.
- [JEPA](../world-models/jepa.md) · [SIGReg](../world-models/sigreg.md) · [Identifiability](../world-models/identifiability.md) — where the collapse question lives.
- [Gradient-based planning](../world-models/gradient-based-planning.md) — the other landscape the wiki cares about: planning *through* a learned model, where the [train–test gap paper](../../sources/train-test-gap-world-models-paper.md) shows the optimizer attacking the model.
- [Inductive bias](inductive-bias.md) — what shapes which minima exist.

## Current state

Both papers are foundational rather than current. The 2015 assumptions were never lifted; the 2017 flat-minima claim was contested on reparameterization grounds within months and survived as a regularity rather than a law. What the wiki lacks, and could produce cheaply, is a single Hessian spectrum at a JEPA solution.

## Mentioned in

- [The Loss Surfaces of Multilayer Networks](../../sources/choromanska2015-loss-surfaces-multilayer-networks.md)
- [Entropy-SGD](../../sources/chaudhari2017-entropy-sgd.md)
- [JEPA Through the Eyes of a Physicist](../../sources/jepa-vs-physics-moudrkat.md) — the essay that surfaced both papers and posed the collapse question.
- [Dawid & LeCun — Latent-Variable EBM lecture notes](../../sources/dawid-lecun-lvebm-lecture-notes.md) — the volume-bounding principle Entropy-SGD twins.
