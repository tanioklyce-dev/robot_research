---
title: Identifiability (linear identifiability of latent variables)
type: concept
created: 2026-07-26
updated: 2026-07-26
sources: 5
tags: [identifiability, linear-identifiability, latent-space, jepa, lejepa, theory, causal-representation-learning, nonlinear-ica, planning, generalization-theory]
---

# Identifiability

**Identifiability** asks whether a learned representation recovers the *actual* latent variables generating the observations — not merely a representation that performs well downstream. **Linear identifiability**, the form proved for [LeJEPA](../../sources/lejepa-paper.md), is recovery **up to simple symmetries**: the learned encoder equals the true latents composed with an orthogonal rotation, `h(z) = Qz`, `Q ∈ O(n)`. The practical signature is that the true latents become recoverable by a **linear probe**.

## Why it matters for world models

Every [JEPA](jepa.md)-style system plans in a [learned latent space](latent-space.md). Whether that planning is *principled* or merely *empirically lucky* turns on identifiability:

- **Without it**, a latent space might encode task-useful correlations that are arbitrarily warped relative to the world's actual state variables. Planning still sometimes works, but there's no reason a straight line in latent space corresponds to anything sensible in the world.
- **With it**, latent-space geometry mirrors world geometry up to rotation — so straight-line planning in latents decodes to sensible trajectories. [Klindt, LeCun & Balestriero (2026)](../../sources/when-does-lejepa-learn-a-world-model-paper.md) demonstrate exactly this: on DMC Reacher, straight-line latent planning yields **oracle-quality joint trajectories once linear identifiability exceeds R² > 0.93**, and control cost tracks identifiability monotonically.

This is the strongest formal argument the JEPA program has made for latent prediction over pixel reconstruction — it moves the case from "representation space is more efficient" to "under these conditions, representation space is *the world's*, rotated."

## The conditions (and how restrictive they are)

The guarantee is **conditional**, and the conditions do most of the work:

- Latents evolve under **stationary, additive-noise transitions** with an independence structure.
- Latents are **Gaussian** — and the converse theorem shows the Gaussian is *uniquely* the distribution for which every optimum is linear. This is why [SIGReg](jepa.md)'s isotropic-Gaussian target is more than an anti-collapse trick.
- The learned dimension equals the true latent dimension (**m = n**). Behavior otherwise is explicitly "an important open problem" — and every real system is in that regime.
- Results are **population-level** (infinite data), covering the **encoder only**. Action-conditioned dynamics `p(z'|z,a)` — the part a control world model needs — would require interventional causal representation learning, and are not proved.

> [!warning] Proved identifiability has not produced robust models
> Five days before the identifiability paper, largely the same group published [stable-worldmodel](../../sources/stable-worldmodel-paper.md), showing that [LeWorldModel](../../entities/leworldmodel.md) — which scales the LeJEPA recipe — drops from **50.8 % to 6–26 %** on Push-T under color/size/shape shifts, with quadratic decay under distractors. The two results are not reconciled by either paper. The honest reading is that they occupy different regimes: a color-shifted environment plausibly violates the theory's generative assumptions outright, so the theorem is not contradicted — but neither does it yet buy robustness in practice. **Identifiability under-assumption and generalization-in-practice are separate problems.**

## Related concepts
- [Learned latent space](latent-space.md) — identifiability is a property of one.
- [JEPA](jepa.md) — the architecture family the result applies to.
- [Spectral theory of SSL](../learning/spectral-theory-of-ssl.md) — the shared mathematical frame; identifiability (recoverability) and generalization are the two formal guarantees built on it.
- [World model](world-model.md).

## Key references
- [When Does LeJEPA Learn a World Model? (Klindt, LeCun, Balestriero, 2026)](../../sources/when-does-lejepa-learn-a-world-model-paper.md) — the theorems.
- [LeJEPA (Balestriero & LeCun, 2025)](../../sources/lejepa-paper.md) — the method analyzed; SIGReg.
- [stable-worldmodel (Maes et al., 2026)](../../sources/stable-worldmodel-paper.md) — the empirical counterweight.
- [A Generalization Theory for JEPA-Based World Models (Cui et al., 2026)](../../sources/jepa-generalization-theory-paper.md) — the sibling formal result: where identifiability asks *can the model recover the true latents*, this asks *does low pretraining error provably transfer to downstream planning* (finite-sample bound). Both use spectral-graph language.

## Mentioned in
- [When Does LeJEPA Learn a World Model?](../../sources/when-does-lejepa-learn-a-world-model-paper.md)
- [stable-worldmodel paper](../../sources/stable-worldmodel-paper.md)
- [A Generalization Theory for JEPA-Based World Models](../../sources/jepa-generalization-theory-paper.md) — complementary generalization guarantee.
