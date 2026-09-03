---
title: Contrastive learning and InfoNCE
type: concept
created: 2026-09-03
updated: 2026-09-03
sources: 4
tags: [contrastive-learning, infonce, cpc, simclr, moco, negatives, mutual-information, self-supervised, anti-collapse, batch-size]
---

**Contrastive learning** — learn a representation by pulling together the embeddings of two views of the same thing (**positive pairs**) and pushing apart embeddings of different things (**negative pairs**). The negatives are what stop the encoder from mapping everything to a constant; they are the field's **first** answer to [representation collapse](../world-models/jepa.md#common-training-challenges), and every later answer is a proposal to remove them.

## InfoNCE, and where it comes from

The loss is **InfoNCE**, introduced by **[Contrastive Predictive Coding](../../sources/cpc-paper.md)** (van den Oord, Li & Vinyals, DeepMind, 2018). Given `N` samples containing one positive and `N−1` negatives, with a score `f`:

`L_N = −E[ log ( f(x⁺, c) / Σ_j f(x_j, c) ) ]`

which is categorical cross-entropy for "which of these `N` is the real one." Two properties from the primary that the field's paraphrases usually drop:

- **The optimum is a density ratio** `p(x|c)/p(x)`, independent of `N`.
- **`I(x; c) ≥ log N − L_N`.** Minimizing InfoNCE maximizes a **lower bound on mutual information**, and the bound **tightens as `N` grows**.

> [!note] That inequality is the origin of every batch-size complaint in this literature
> More negatives ⇒ tighter bound ⇒ better representation, so contrastive methods want large batches (SimCLR), memory banks (MoCo), or mining strategies. [BYOL](../../entities/byol.md)'s opening paragraph is a list of exactly these workarounds, and its selling point is escaping them. When [BYOL's ablation](../../sources/byol-paper.md) shows SimCLR degrading with batch size while BYOL stays flat, that is this bound showing up as an engineering constraint.

CPC's own formulation is **temporal and patch-autoregressive**, not two-augmented-views: encode observations to `z_t`, summarize with an autoregressive model into a context `c_t`, predict `z_{t+k}` several steps ahead. On images that becomes predicting lower rows of a 7×7 grid of crops from upper rows. **The familiar SimCLR-style two-view setup is a simplification of CPC, not its original form** — and CPC's temporal version is structurally [LeWM](../../entities/leworldmodel.md) minus the action conditioning.

## What the negatives cost

Three prices, all documented in the primaries this wiki now holds:

1. **Batch size / memory.** Directly from the MI bound above.
2. **Augmentation sensitivity, and the reason is specific.** Crops of one image mostly share a colour histogram, and colour histograms differ across images — so **a contrastive task on crops alone can be solved by colour histogram and nothing else**, and the representation is never pushed further ([BYOL](../../sources/byol-paper.md) §5). Hence SimCLR's mandatory colour distortion, and its **−27.6 point** collapse under crop-only augmentation where BYOL loses 13.1 and [MAE](../../sources/mae-paper.md) works with **no augmentation at all**.
3. **Semantic false negatives.** Two images of the same class are pushed apart because they are different images. [X-CLR](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) attacks exactly this by replacing binary positive/negative with a **continuous similarity graph** built from captions — which, under the [spectral view](spectral-theory-of-ssl.md), is the same objective with a better-specified affinity graph.

## Where it sits among the alternatives

Contrastive learning is one of four mechanisms this wiki now has primaries for. The comparison is on [SSL anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md); in one line each:

| Mechanism | Anti-collapse device | Primary |
|---|---|---|
| **Contrastive** | negative pairs | [CPC](../../sources/cpc-paper.md) → SimCLR, MoCo |
| **Momentum + predictor** | asymmetric predictor **and** EMA target, together | [BYOL](../../sources/byol-paper.md) |
| **Self-distillation** | centering **and** sharpening of an EMA teacher | [DINO](../../sources/dino-paper.md) |
| **Reconstruction** | *none needed* — the target is the input | [MAE](../../sources/mae-paper.md) |
| **Distributional** | one provable term matched to an isotropic Gaussian | [LeJEPA / SIGReg](../world-models/sigreg.md) |

Under the [spectral theory of SSL](spectral-theory-of-ssl.md), contrastive methods recover **global** spectral embeddings (kernel MDS / kernel CCA) while non-contrastive ones recover **local** embeddings (Laplacian eigenmaps) — the first theoretical bridge between the two families, and the frame in which "choose negatives" becomes "choose a graph over samples."

## Current state

Pure contrastive pretraining has largely lost the vision frontier to distillation ([DINOv2](../../entities/dinov2.md), [DINOv3](../../entities/dinov3.md)), reconstruction ([MAE](../../entities/mae.md)) and distributional ([SIGReg](../world-models/sigreg.md)) methods. But InfoNCE has not gone anywhere — it is the loss inside [CLIP](../../entities/clip.md), and negatives remain the default in retrieval, in multimodal alignment, and wherever a similarity structure is already given rather than being the thing to learn.

## Related concepts

- [Spectral theory of SSL](spectral-theory-of-ssl.md) — where contrastive and non-contrastive are unified.
- [JEPA](../world-models/jepa.md) — the latent-prediction architecture CPC prefigures.
- [SIGReg](../world-models/sigreg.md) — the argument that the whole heuristic stack is replaceable by one term.
- [Latent space](../world-models/latent-space.md) — what all of these are shaping.

## Mentioned in

- [CPC paper (van den Oord, Li & Vinyals, 2018)](../../sources/cpc-paper.md) — **the origin of InfoNCE**.
- [BYOL paper (Grill et al., 2020)](../../sources/byol-paper.md) — the ablation showing what negatives were doing and what replaces them.
- [DINO paper (Caron et al., 2021)](../../sources/dino-paper.md) — MoCo v2's InfoNCE as a baseline row.
- [MAE paper (He et al., 2021)](../../sources/mae-paper.md) — the augmentation-dependence contrast.
