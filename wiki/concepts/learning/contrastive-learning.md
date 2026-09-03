---
title: Contrastive learning and InfoNCE
type: concept
created: 2026-09-03
updated: 2026-09-03
sources: 8
tags: [contrastive-learning, infonce, cpc, simclr, moco, negatives, mutual-information, self-supervised, anti-collapse, batch-size]
---

**Contrastive learning** — learn a representation by pulling together the embeddings of two views of the same thing (**positive pairs**) and pushing apart embeddings of different things (**negative pairs**). The negatives are what stop the encoder from mapping everything to a constant; they are the field's **first** answer to [representation collapse](../world-models/jepa.md#common-training-challenges), and every later answer is a proposal to remove them.

## InfoNCE, and where it comes from

The loss is **InfoNCE**, and its lineage is longer than the name suggests. [A Cookbook of Self-Supervised Learning](../../sources/ssl-cookbook.md) (Fig. 2) traces it:

| Year | Work | What it added |
|---|---|---|
| 1993 | [Bromley et al.](../../sources/bromley1993-siamese-signature-verification.md) | the contrastive loss |
| 2004 | Goldberger et al. | Neighbourhood Component Analysis — softmax over distances |
| 2005–06 | Chopra et al.; Hadsell et al. | the margin |
| 2009–10 | Weinberger & Saul; Chechik et al. | triplet loss |
| 2016 | Sohn | **(N+1)-tuple loss** — inner products; negatives taken from other samples in the batch |
| 2018 | **Wu et al.** | the **"non-parametric softmax"**: explicit normalization, **the temperature τ**, and **the momentum-encoder idea** (via proximal optimization) |
| 2018 | **[CPC](../../sources/cpc-paper.md)** | *"coins the name infoNCE"* — plus the mutual-information framing and its bound |

> [!note] Two things this corrects
> **The temperature and the momentum encoder predate both CPC and MoCo.** They come from Wu et al. 2018. An earlier version of this page credited CPC as "the origin of InfoNCE"; it is the origin of the name, the MI framing, and the bound.

Given `N` samples containing one positive and `N−1` negatives, with a score `f`:

`L_N = −E[ log ( f(x⁺, c) / Σ_j f(x_j, c) ) ]`

which is categorical cross-entropy for "which of these `N` is the real one." Two properties from the primary that the field's paraphrases usually drop:

- **The optimum is a density ratio** `p(x|c)/p(x)`, independent of `N`.
- **`I(x; c) ≥ log N − L_N`.** Minimizing InfoNCE maximizes a **lower bound on mutual information**, and the bound **tightens as `N` grows**.

> [!warning] The bound is real; the "you need huge batches" conclusion is not
> More negatives ⇒ tighter bound, so contrastive methods were built with large batches (SimCLR), memory banks (MoCo) and mining strategies, and [BYOL](../../entities/byol.md)'s opening paragraph is a list of those workarounds. **But the [Cookbook](../../sources/ssl-cookbook.md) §3.5.1 calls the requirement "misleading":** with **square-root learning-rate scaling** (SimCLR's own appendix, worth up to 5 points at 100 epochs) SimCLR trains on ImageNet **on a single GPU**; **DCL reaches top performance at batch 256** for SimCLR and queue 256 for MoCo, simply by removing the positive pair from the softmax denominator.
>
> So [BYOL's ablation](../../sources/byol-paper.md) showing SimCLR degrading with batch size is a fact about *SimCLR as configured in 2020*, not a necessity of contrastive learning. An earlier version of this page presented it as the latter. The durable cost of negatives is **augmentation sensitivity and false negatives**, below — not batch size.

CPC's own formulation is **temporal and patch-autoregressive**, not two-augmented-views: encode observations to `z_t`, summarize with an autoregressive model into a context `c_t`, predict `z_{t+k}` several steps ahead. On images that becomes predicting lower rows of a 7×7 grid of crops from upper rows. **The familiar SimCLR-style two-view setup is a simplification of CPC, not its original form** — and CPC's temporal version is structurally [LeWM](../../entities/leworldmodel.md) minus the action conditioning.

## What the negatives cost

Three prices, all documented in the primaries this wiki now holds:

1. **Batch size / memory.** Directly from the MI bound above.
2. **Augmentation sensitivity, and the reason is specific.** Crops of one image mostly share a colour histogram, and colour histograms **alone suffice to distinguish images** — so a contrastive task on crops alone is solvable by colour and the representation is never pushed further. Measured in [SimCLR](../../sources/simclr-paper.md) §3.1 (the primary; the wiki previously carried this from BYOL's reproduction), which also finds **no single augmentation suffices** and that contrastive learning wants *stronger* colour augmentation than supervised learning does — the same strength that takes SimCLR 59.6 → 64.5 takes the supervised baseline 77.0 → 75.4. Downstream: SimCLR's **−27.6 point** collapse under crop-only augmentation where BYOL loses 13.1 and [MAE](../../sources/mae-paper.md) works with **no augmentation at all**.
3. **Semantic false negatives.** Two images of the same class are pushed apart because they are different images. [X-CLR](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) attacks exactly this by replacing binary positive/negative with a **continuous similarity graph** built from captions — which, under the [spectral view](spectral-theory-of-ssl.md), is the same objective with a better-specified affinity graph.

## Where it sits among the alternatives

> [!note] Two ways to cut the field, and they cross-cut
> The [Cookbook](../../sources/ssl-cookbook.md) sorts SSL by **mechanism of the training signal** into four families — **Deep Metric Learning** (SimCLR, NNCLR), **Self-Distillation** (BYOL, SimSiam, DINO **and MoCo**), **Canonical Correlation Analysis** (VICReg, Barlow Twins, **SwAV**, W-MSE), and **Masked Image Modeling** (BEiT, MAE, SimMIM).
>
> That puts **MoCo with the self-distillation family even though its loss is InfoNCE**, because its defining contribution is the momentum encoder. An earlier version of this page listed MoCo here without qualification. Both cuts are defensible — the table below sorts by **anti-collapse device** instead — but a reader should know they disagree about MoCo and SwAV.

Contrastive learning is one of four mechanisms this wiki now has primaries for. The comparison is on [SSL anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md); in one line each:

| Mechanism | Anti-collapse device | Primary |
|---|---|---|
| **Contrastive** | negative pairs | [CPC](../../sources/cpc-paper.md) → [SimCLR](../../sources/simclr-paper.md) ([MoCo](../../entities/moco.md)'s loss too, though the Cookbook files it elsewhere) |
| **Momentum + predictor** | asymmetric predictor **and** EMA target — or a **faster predictor** instead of the EMA | [BYOL](../../sources/byol-paper.md), [SimSiam](../../sources/simsiam-paper.md) |
| **Self-distillation** | centering **and** sharpening of an EMA teacher | [DINO](../../sources/dino-paper.md) |
| **Reconstruction** | *none needed* — the target is the input | [MAE](../../sources/mae-paper.md) |
| **Distributional** | one provable term matched to an isotropic Gaussian | [LeJEPA / SIGReg](../world-models/sigreg.md) |

Under the [spectral theory of SSL](spectral-theory-of-ssl.md), contrastive methods recover **global** spectral embeddings (kernel MDS / kernel CCA) while non-contrastive ones recover **local** embeddings (Laplacian eigenmaps) — the first theoretical bridge between the two families, and the frame in which "choose negatives" becomes "choose a graph over samples."

> [!note] The projector is where the information goes, and it is measurable
> [SimCLR](../../sources/simclr-paper.md) Table 3 trains a probe to predict *which augmentation was applied*, from the backbone output `h` and from the projector output `g(h)`. Rotation: **67.6% from `h`, 25.6% from `g(h)` — chance is 25%.** Original-vs-corrupted: 99.5 vs 59.6. **The projector output is trained to be invariant, so it discards exactly what the invariance targets**, which is why every method keeps the backbone and throws the head away. It is also a general-purpose diagnostic for *what an invariance destroyed*, and it is barely used.

## The unified view, and the doubts about the MI story

Two threads from the [Cookbook](../../sources/ssl-cookbook.md) §2.6.1 worth carrying:

- **One loss family.** Tian (2022) unifies contrastive losses as `L_{φ,ψ}` for monotone φ, ψ — InfoNCE, MINE, Triplet, Soft Triplet, N+1-Tuplet and Lifted Structured are all instances. And contrastive learning with a **deep linear network is equivalent to PCA**.
- **The mutual-information account is contested.** Tschannen et al. (2020) show *"the performance of InfoNCE cannot be explained only in terms of mutual information"* — the feature extractor and the estimator's form matter more. Competing accounts: **alignment + uniformity** (Wang & Isola), an **HSIC** bound, and **nonlinear ICA**-style latent identification under strong assumptions. Also relevant: the `ψ = e^{x/τ}` form **already up-weights hard negatives at the batch level**, which is why explicit hard-negative mining adds less than it looks like it should — and why large batches help by making hard negatives *appear* at all.

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
- [A Cookbook of Self-Supervised Learning](../../sources/ssl-cookbook.md) — **corrects this page twice**: the InfoNCE lineage, and the batch-size requirement.
- [SimCLR paper (Chen et al., 2020)](../../sources/simclr-paper.md) — **the canonical instantiation**; the colour-histogram shortcut and the projector measurement, from the primary.
- [MoCo v3 paper (Chen, Xie & He, 2021)](../../sources/moco-v3-paper.md) — hidden instability, and batch size *hurting* past ~2k on ViT.
- [SimSiam paper (Chen & He, 2020)](../../sources/simsiam-paper.md) — "SimCLR without negative pairs" still works.
