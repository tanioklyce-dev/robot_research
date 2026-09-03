---
title: LpWM (LpWorldModel)
type: entity
subtype: model
created: 2026-08-26
updated: 2026-08-26
sources: 2
tags: [lpwm, jepa, world-model, sparse-representation, rdmreg, lewm, planning, lecun]
---

**LpWM (LpWorldModel)** — an action-conditioned [JEPA](../concepts/world-models/jepa.md) regularized with **RDMReg** (Rectified Distribution Matching Regularization) to match encoder features to a **Rectified Generalized Gaussian**, producing **non-negative, exactly sparse** latent codes. Same encoder architecture and CEM planner as [LeWM](leworldmodel.md); the change is the latent *geometry*. Kuang, Dagade, Le Lidec, [Maes](lucas-maes.md), [Balestriero](randall-balestriero.md), [LeCun](yann-lecun.md), August 2026 ([paper](../sources/lpwm-paper.md)).

## The claim, stated precisely

**Sparsity lowers the predictor capacity required to plan** — not "sparse world models are better."

| Regime | Sparse vs dense |
|---|---|
| Wall env, any predictor | No difference — linear LTI(1) already ~100% for both |
| PushT, lowest capacity | Both fail |
| PushT, **intermediate** capacity | **LpWM +24–57%** (MLP∘LTI), +36–45% (MLP∘LTV), +11–23% (LTI(k)) |
| PushT, highest capacity (Deep-AdaLN) | Similar — "predictor complexity saturates" |

Against **VICReg**-regularized LeWM (a second dense baseline), LpWM wins **including at high capacity** — so the sparse advantage survives the choice of dense regularizer, and SIGReg is the stronger dense option.

## Mode-factored codes

On **Piecewise** (2D navigation partitioned into force-field zones): **84.7% vs 65.3%** for LeWM on random goals, and the sparse code factorizes cleanly —

- **Support** (which features are active) decodes the ground-truth dynamics zone at **94–99%**, as well as the full embedding.
- **Magnitudes** decode continuous within-zone position better.
- Support similarity is high within a zone and drops at boundaries **even when zones carry no visual cues** — so it is recovering the *dynamics regime* from action-conditioned prediction, not appearance.
- Beats LeWM at **every** planning horizon, **gap widening with horizon**.

> [!warning] Sparsity alone does not produce semantic structure
> On OGBench-Cube the support behaves as a **motion detector** — correlation with effector motion r ≈ 0.87, with gripper contact r ≈ 0.05 — because RDMReg constrains only the per-frame marginal. An optional **temporal-Jaccard** loss flips this (cube motion 0.21 → 0.80, contact 0.05 → 0.61) **at no change in planning success**. Interpretability and capability are decoupled here; the paper leaves temporal regularization to future work.

## Why it matters in this wiki

It opens a **new axis in the [JEPA anti-collapse design space](../concepts/world-models/jepa.md)**. Every mechanism the wiki tracked — EMA/stop-grad, VICReg, [SIGReg](leworldmodel.md), [SMWM](smwm.md)'s inverse dynamics — answers *how do you avoid collapse*. LpWM asks *what latent geometry makes the dynamics cheap to model*, which is a different question and gets a different answer.

> [!warning] In tension with the identifiability result
> [When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md) proves the **Gaussian is uniquely** the latent distribution for which linear identifiability holds. LpWM deliberately targets a **non-Gaussian** distribution and reports better dynamics modeling. No formal contradiction — the theorem covers the **encoder**, at population level, and explicitly does *not* cover action-conditioned dynamics — but the practical implication stands: **the geometry that makes an encoder identifiable may not be the geometry that makes its dynamics predictable.** See [identifiability](../concepts/world-models/identifiability.md).

## Open questions

- No OOD testing — pointed, given the same author cluster measured [LeWM collapsing under distribution shift](../sources/stable-worldmodel-paper.md).
- No planning-speed comparison; [LeWM's 48× advantage](leworldmodel.md) is untested under sparsity.
- Two environments carry the main result; no 3D manipulation, no real robot.

## Related

- [LeWorldModel](leworldmodel.md) — the dense baseline it modifies.
- [SIGReg](../concepts/world-models/sigreg.md) — the dense-Gaussian regularizer RDMReg replaces.
- [JEPA](../concepts/world-models/jepa.md) / [identifiability](../concepts/world-models/identifiability.md) / [latent space](../concepts/world-models/latent-space.md).
- [SMWM](smwm.md) — the other 2026 attempt to change what the regularizer is *for*.

## Mentioned in

- [LpWM paper](../sources/lpwm-paper.md)
