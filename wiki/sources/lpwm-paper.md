---
title: "LpWM: A Case for Sparse Representations in World Models"
type: source
url: https://arxiv.org/abs/2608.22764
local_path: raw/lpwm_2608.22764.pdf
sha256: 76ab29b8610553410ac6b3c0683ccc6d71baabedf49ee6a4463a652a82c3d5ae
author: Yilun Kuang, Yash Dagade, Quentin Le Lidec, Lucas Maes, Randall Balestriero, Yann LeCun
published: 2026-08-24
ingested: 2026-08-26
venue: arXiv (cs.LG)
format: paper (28 pp)
tags: [jepa, world-model, sparse-representation, rdmreg, sigreg, lewm, planning, pusht, latent-space, interpretability, lecun]
---

# LpWM: A Case for Sparse Representations in World Models

## Summary

Asks whether the **dense** latent geometry that [JEPA](../concepts/world-models/jepa.md) anti-collapse regularizers produce — [SIGReg](../entities/leworldmodel.md)'s isotropic Gaussian, VICReg's decorrelated features — is actually the right geometry for modeling *action-conditioned dynamics*. Argues no. Motivated by a linearization result (nonlinear Lipschitz dynamics can be approximated arbitrarily well by action-conditioned **linear** dynamics in a sufficiently high-dimensional **one-hot** latent space, with rollout error vanishing as dimension grows), the paper introduces **LpWorldModel (LpWM)**: a JEPA regularized with **RDMReg** (Rectified Distribution Matching Regularization) to match encoder features to a **Rectified Generalized Gaussian**, yielding non-negative, exactly sparse codes. The empirical claim is not "sparse is better" but something more precise and more useful: **sparsity lowers the predictor capacity required to plan successfully.**

## Key claims

### The thesis is about predictor complexity, not raw performance

This is the finding to carry, and the abstract's "up to 57%" obscures it. On PushT, measured across predictor families and latent dimensions D ∈ {384, 768, 1536, 2048, 4096}:

| Regime | Result |
|---|---|
| **Wall environment, any predictor** | A linear **LTI(1)** predictor already reaches ~100% closed-loop CEM success for *both* LeWM and LpWM — the environment's latent dynamics are already linear, so **sparsity buys nothing** |
| **PushT, lowest capacity (LTI(1))** | Fails for **both** — PushT dynamics cannot be modeled linearly in practice |
| **PushT, highest capacity (Deep-AdaLN(k), Shallow-AdaLN(k))** | Sparse and dense perform **similarly** — "predictor complexity saturates and we don't observe significant advantages" |
| **PushT, intermediate capacity** | **The gap.** LpWM over LeWM by **24–57%** (MLP∘LTI(k)), **36–45%** (MLP∘LTV(k)), **11–23%** (LTI(k)) |

> [!note] Read the headline correctly
> "57% better than LeWM" is the top of a range, at one predictor family, at intermediate capacity, on one environment. The honest statement is the paper's own: *"at a fixed, intermediate predictor capacity, a shallow predictor plans over sparse codes where it fails over dense ones."* Sparsity is a **capacity-efficiency** claim — it moves where on the predictor-size curve you can afford to sit — not a claim that sparse world models are better.

**The advantage is not specific to SIGReg.** Replacing SIGReg with **VICReg** in LeWM gives another dense baseline, and LpWM beats it across Deep-AdaLN(k), MLP∘LTV(k) and MLP∘LTI(k) — including **at high capacity**, where LpWM did *not* beat SIGReg. So the sparse-vs-dense gap survives the choice of dense regularizer, and SIGReg is the stronger of the two dense options.

### Mode-factored codes: what sparsity buys structurally

On **Piecewise**, a 2D navigation environment partitioned into zones with different force fields (piecewise-affine dynamics):

- **84.7% (LpWM) vs 65.3% (LeWM)** planning success with random goals. Both saturate on goals drawn from evaluation episodes.
- Discretizing the space into a 20×20 grid and binarizing embeddings into support vectors, **Jaccard similarity between supports is high within a zone and drops sharply at zone boundaries** — *and this persists when the zones carry no visual cues.* So the support is recovering the **dynamics regime** from action-conditioned prediction, not from appearance.
- Linear probes confirm the factorization: **the binary support decodes the ground-truth zone at 94–99%**, as accurately as the full embedding, while **continuous agent position decodes better from the magnitudes.** Support = discrete mode; magnitude = continuous within-mode state.
- Long-horizon planning: LpWM beats LeWM at **every** horizon H, **with the gap widening as H increases.**

### The limitation the paper states about itself

On **OGBench-Cube**, contact provides a natural regime change (free motion vs arm–cube interaction). Measuring support instability `1 − J(z_t, z_{t+1})` against physical events:

> "Sparsity alone does not determine which temporal factor is encoded by the support. RDMReg constrains only the **per-frame marginal**, and without an explicit temporal prior the support tends to follow the dominant fast-varying signal."

Without temporal regularization the support is essentially a **motion detector**: correlation with effector motion **r ≈ 0.87**, with gripper contact **r ≈ 0.05**. Adding an optional **temporal Jaccard (TJ)** loss encouraging support stability across adjacent frames inverts this — effector correlation **0.87 → 0.40**, cube motion **0.21 → 0.80**, gripper contact **0.05 → 0.61** — **at no change in planning success.**

> [!note] The interpretability and the performance are decoupled
> TJ changes *what the support means* without changing *how well it plans*. That is worth stating plainly: the mode-factored structure is a real, measurable property, but on contact-rich tasks it is not automatically the semantically meaningful factorization, and making it so is a separate objective that buys interpretability rather than capability. The paper is explicit — "we leave the design of temporal regularization for more complex dynamics to future work."

### Method details

- **RDMReg** matches encoder features to a **Rectified Generalized Gaussian**; the parameter **μ** controls sparsity (μ = 0, 1, 2 swept). Non-negative codes by construction.
- **μP (maximum update parameterization)** used to stabilize training across widths, since the core experiment is a width sweep.
- Predictor families compared, with parameter counts at D = 4096: Deep-AdaLN(k) **822.4M**, Shallow-AdaLN(k) **151.1M**, MLP∘LTV(k) **84.7M**, MLP∘LTI(k) **83.9M**, LTI(k) **67.1M**, LTI(1) **33.6M**. The attention-free predictors are an order of magnitude smaller.
- Planning is **CEM**, as in [LeWM](../entities/leworldmodel.md); open-loop and closed-loop both reported.

## Contradiction with the wiki's identifiability thread

> [!warning] Sparse dynamics geometry vs. the uniqueness of the Gaussian
> The wiki records, from [When Does LeJEPA Learn a World Model?](when-does-lejepa-learn-a-world-model-paper.md), that **the Gaussian latent distribution is *uniquely* the one for which every optimum is linear** — which "elevates SIGReg's isotropic-Gaussian target from an anti-collapse trick to the load-bearing choice." LpWM, from an overlapping author set four months later, deliberately targets a **non-Gaussian** (Rectified Generalized Gaussian) distribution and reports better dynamics modeling.
>
> **These do not formally contradict**, and it is worth being precise about why: the identifiability theorem is about the **encoder** recovering true latents up to rotation, at the population level, under stationary additive-noise transitions with m = n. LpWM is about the **predictor's** capacity requirement for modeling `p(z'|z,a)` — which the identifiability paper explicitly lists as *not proved* ("action-conditioned dynamics would require interventional causal representation learning, and are not proved").
>
> But the practical tension is real and the wiki should hold it: **the latent geometry that makes an encoder identifiable and the latent geometry that makes dynamics cheap to predict may not be the same geometry.** LpWM is the first evidence in this wiki that they diverge. Neither paper cites the other on this point.

## Entities mentioned

- [LeWorldModel / LeWM](../entities/leworldmodel.md) — the dense baseline; LpWM shares its encoder architecture and CEM planner.
- [Yann LeCun](../entities/yann-lecun.md), [Randall Balestriero](../entities/randall-balestriero.md), [Lucas Maes](../entities/lucas-maes.md) — the [stable-worldmodel](stable-worldmodel-paper.md) / LeWM author cluster.
- **LpWM** — [entity page](../entities/lpwm.md).

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — adds a new axis to the anti-collapse design space: *what latent geometry*, not just *how to avoid collapse*.
- [Identifiability](../concepts/world-models/identifiability.md) — the tension above.
- [Learned latent space](../concepts/world-models/latent-space.md) — sparse vs dense geometry.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — JEPA/latent-prediction paradigm.
- [SIGReg](../concepts/world-models/sigreg.md) — a non-Gaussian sparse target for dynamics.

## Open questions

- **Only two environments carry the main result** (Wall, PushT), plus Piecewise and OGBench-Cube for structure. No 3D manipulation, no real robot, no comparison to [DINO-WM](../entities/dino-wm.md) or [HWM](../entities/hwm.md).
- **No out-of-distribution testing.** Given that [stable-worldmodel](stable-worldmodel-paper.md) — same author cluster — measured LeWM collapsing from 50.8% to 6–26% under color/size/shape shift, whether sparse codes are more or less robust than dense ones is the obvious next question and is not asked.
- **The linearization theorem motivates but does not explain the result.** It concerns exact one-hot codes in the infinite-dimension limit; LpWM uses distributed sparse codes at D ≤ 4096, and the paper says these "may not linearize the dynamics exactly."
- **Wall-clock and planning-cost comparisons are absent.** The wiki's interest in LeWM is partly its **48× faster planning**; whether sparse codes preserve that is untested here.
