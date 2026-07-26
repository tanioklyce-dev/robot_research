---
title: "When Does LeJEPA Learn a World Model? (Klindt, LeCun, Balestriero, 2026)"
type: source
url: https://arxiv.org/abs/2605.26379
local_path: null
author: David Klindt, Yann LeCun, Randall Balestriero
affiliations: Cold Spring Harbor Laboratory (Klindt); New York University (LeCun); Brown University (Balestriero)
published: 2026-05-25
ingested: 2026-07-26
venue: arXiv preprint (cs.LG)
tags: [lejepa, jepa, world-model, identifiability, sigreg, vicreg, theory, lecun, balestriero, klindt, latent-space, planning]
---

# When Does LeJEPA Learn a World Model?

## Summary

The **theory paper the JEPA program had been missing**: a formal answer to when a joint-embedding predictive architecture actually recovers the world's latent variables rather than merely some useful-looking representation. It proves that [LeJEPA](lejepa-paper.md) — alignment plus Gaussian regularization ([SIGReg](../concepts/world-models/jepa.md)) — achieves **linear identifiability** of the true latents from nonlinear observations, *and* that among all worlds satisfying its assumptions the **Gaussian latent distribution is uniquely the one that guarantees this**. The practical payoff is stated directly: where linear identifiability holds, straight-line planning in the learned latent space decodes to near-oracle trajectories.

> [!note] This is a *population-level* result about the encoder
> The theorems concern the optimum of the objective with infinite data, and cover the **encoder only** — not the action-conditioned dynamics `p(z'|z,a)` that a control-capable world model needs. See Limitations. The paper is a foundation for the JEPA claim, not a validation of any deployed system.

## Key claims

### The two theorems

- **Theorem 5.1 (forward).** For a Gaussian world, any measurable map satisfying the LeJEPA constraints attains minimum loss **only** when it recovers an orthogonal transformation of the true latents — `h(z) = Qz` for `Q ∈ O(n)`. Proved via spectral decomposition using **Hermite polynomials**, showing that nonlinearity strictly reduces correlation.
- **Theorem 5.2 (converse — Gaussian uniqueness).** Across worlds meeting the independence / stationarity / additive-noise assumptions, **only** the Gaussian latent distribution guarantees that every LeJEPA optimum is linear. Established via **Sturm–Liouville theory**.

Together: Gaussian regularization isn't one anti-collapse trick among many — under these assumptions it is *the* distributional choice that makes identifiability provable.

### Linear identifiability

Defined as a guarantee that the learned representation recovers the underlying latent variables **up to simple symmetries** — here, orthogonal rotations. The practical consequence is that the latents become recoverable by a **linear probe**, which is what makes latent-space planning well-posed rather than merely empirical.

### The setting's assumptions

Latents evolve under **stationary, additive-noise transitions** with independence structure. The Gaussian result is conditional on this class; the paper defends the Gaussian assumption itself (which is unknowable from observations alone) with **maximum-entropy and central-limit-theorem** arguments rather than empirical evidence.

### Experiments

| Setting | Detail |
|---|---|
| 2D synthetic | Four nonlinear mixings: spiral rotation, sinusoidal shear, parabolic shear, **RealNVP coupling** |
| Dimension sweep | N ∈ {2, 4, 8, …, **1024**} |
| Distributional sweep | Recovery peaks **sharply at Gaussian** (α = 2) |
| Robotic control | **DMC Reacher** — 2D joint angles recovered from pixel observations |

- **SIGReg and VICReg maintain R² > 0.999** for linear identifiability up to **1024 dimensions**.
- On Reacher goal-reaching, **straight-line planning in the learned latent space decodes to oracle-quality joint trajectories when linear identifiability R² > 0.93**.
- **Control cost tracks linear identifiability monotonically** (Fig. 4d) — the paper's tightest link from the theory to a control outcome.
- **Regularizer comparison (Table 1):** SIGReg, [VICReg](vicreg-paper.md), and InfoNCE *all* yield identifiability under the theory's assumptions; **SIGReg is the most robust to non-Gaussian latents**.

> [!note] The regularizer result cuts both ways
> That VICReg and InfoNCE also achieve identifiability under-assumption means the theorems are **not** a proof that SIGReg is uniquely necessary — SIGReg's advantage in Table 1 is *robustness when the assumptions are violated*, which is an empirical finding, not a theorem.

### Formal verification

The Lean 4 theorem proofs are **axiomatized in Appendix G** — verified *modulo background lemmas*, not a fully machine-checked development from first principles.

## Entities mentioned
- [Yann LeCun](../entities/yann-lecun.md) — co-author (NYU affiliation, **not** AMI Labs)
- [Randall Balestriero](../entities/randall-balestriero.md) — co-author; LeJEPA co-first-author
- [David Klindt](../entities/david-klindt.md) — lead author
- [LeWorldModel](../entities/leworldmodel.md) — cited as scaling the LeJEPA recipe to action-conditioned control from pixels
- [DINO-WM](../entities/dino-wm.md) — referenced for zero-shot planning via latent dynamics
- [V-JEPA 2](../entities/v-jepa-2.md) — cited as achieving zero-shot planning on pretrained features

## Concepts touched
- [Identifiability](../concepts/world-models/identifiability.md) — the concept this paper introduces to the wiki
- [JEPA](../concepts/world-models/jepa.md) — the architecture family being analyzed
- [Learned latent space](../concepts/world-models/latent-space.md) — what identifiability is a property *of*
- [World model](../concepts/world-models/world-model.md)

## Open questions

Carried directly from the paper's own limitations section:

- **The Gaussian assumption is unfalsifiable from observations alone.** Defended on maximum-entropy / CLT grounds — a modeling choice, not a verified property of any real environment.
- **Dimension mismatch (m ≠ n)** — the theory assumes the learned dimension equals the true latent dimension. Behavior otherwise is called "an important open problem," and every real system is in this regime.
- **Finite samples and optimization dynamics** are unaddressed; results are population-level.
- **Action-conditioned dynamics are out of scope.** Extending to `p(z'|z,a)` "requires interventional causal representation learning" — i.e. the part a *control* world model most needs is exactly the part not yet proved.
- No code or data release is stated in the paper.

**Wiki-specific:** does the [stable-worldmodel](stable-worldmodel-paper.md) brittleness result (published five days earlier, sharing two authors) fall inside or outside these assumptions? The two papers are never reconciled — see [JEPA identifiability vs measured brittleness](../syntheses/world-models/generative-video-vs-jepa-world-models.md).
