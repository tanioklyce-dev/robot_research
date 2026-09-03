---
title: "Exploring Simple Siamese Representation Learning — SimSiam (Chen & He, 2020)"
type: source
url: https://arxiv.org/abs/2011.10566
fetch_url: https://arxiv.org/pdf/2011.10566v1
local_path: raw/2011.10566v1.pdf
sha256: 37d37c81d423d503f54d99bc5c9d9dc23d07c7bd1aad62f37b47ec7d2871e63e
author: "Xinlei Chen, Kaiming He (Facebook AI Research)"
published: 2020-11-20
venue: "CVPR 2021 (arXiv v1)"
format: paper (PDF, 10 pp.)
tags: [simsiam, stop-gradient, siamese, self-supervised, anti-collapse, byol, em-algorithm, predictor, foundational]
ingested: 2026-09-03
---

## Summary

**The subtraction paper.** SimSiam removes, one at a time, everything the field believed was preventing collapse — negative pairs, large batches, momentum encoders, clustering — and finds that a plain weight-sharing Siamese network with a **predictor on one branch and a stop-gradient on the other** still reaches 67.7% ImageNet linear top-1. Its framing is a hub: *"BYOL without the momentum encoder,"* *"SimCLR without negative pairs,"* *"SwAV without online clustering"* — each obtained by deleting one core component of a method that claimed to need it.

Ingested to settle a contradiction this wiki had filed as open. It settles it, and so does [BYOL's own appendix](byol-paper.md) — see below.

## The finding, and the number

**Stop-gradient is the essential operation, and nothing else is.** Same architecture, same hyperparameters, one difference:

| | Linear top-1 |
|---|---:|
| with stop-gradient | **67.7 ± 0.1** (5 trials) |
| without stop-gradient | **0.1** |

Without it the optimizer *"quickly finds a degenerated solution and reaches the minimum possible loss of −1"* — the loss goes to its floor, which is the diagnostic. So **collapsing solutions demonstrably exist** for this architecture; the predictor, BN and ℓ2-norm do not prevent them. Only the stop-gradient does.

> [!note] The collapse monitor is worth stealing, and it prefigures SIGReg's target
> They track the **per-channel std of the ℓ2-normalized output**. If the output collapses to a constant, std → 0. If the output is a **zero-mean isotropic Gaussian**, std → **1/√d**. With stop-gradient the curve sits at 1/√d — *"the outputs do not collapse, and they are scattered on the unit hypersphere."*
>
> That is a one-line, label-free collapse check available in 2020, and its healthy reference distribution is **the isotropic Gaussian** that [SIGReg](../concepts/world-models/sigreg.md) would later make a training objective and prove uniquely optimal. See [representation evaluation](../concepts/learning/representation-evaluation.md). They also run a **k-NN monitor** during training as a progress signal — the same instrument [MoCo v3](moco-v3-paper.md) uses to expose instability.

## The ablations, which say what does *not* matter

| Knob | Result | Reading |
|---|---|---|
| **Predictor removed** | **0.1** | Necessary. With the symmetrized loss, removing it makes stop-gradient equivalent to *not* stop-gradient (scaled by ½) |
| **Predictor frozen at random init** | 1.5 | Fails, but **not by collapsing** — the loss stays high. It must be *trained* |
| **Predictor lr not decayed** | **68.1** (> baseline 67.7) | *"h should adapt to the latest representations"* — do not force it to converge early |
| **Batch size 64 → 4096** | 66.1 / 67.3 / 68.1 / 68.1 / 68.0 / 67.9 / 64.0 | **Flat from 128 to 2048.** Plain SGD, no LARS. Unlike SimCLR and SwAV, which need ~4096 |
| **All BN removed from heads** | 34.6 | Low, **but no collapse** — an optimization problem, not a collapse mechanism |
| **BN on predictor output** | unstable | Loss oscillates; again not collapse |
| **Cosine → cross-entropy similarity** | 63.2 vs 68.1 | Works. *"Collapsing prevention is not just about the cosine similarity"* |
| **Symmetrization removed** | 64.8 (67.3 with 2× sampling) | Helps accuracy, **unrelated to collapse** |

The summary sentence is the contribution: *"The optimizer (batch size), batch normalization, similarity function, and symmetrization may affect accuracy, but we have seen **no** evidence that they are related to collapse prevention. It is mainly the stop-gradient operation that plays an essential role."*

## The hypothesis: SimSiam is EM, and stop-gradient is a consequence

They propose that SimSiam implicitly optimizes `L(θ, η) = E[‖F_θ(T(x)) − η_x‖²]` over **two** sets of variables — network parameters `θ` and a per-image representation `η_x` — by alternation, *"analogous to k-means clustering"* where θ is the cluster centres and η the assignments.

Under that reading, **the stop-gradient is not a trick but a derivation**: solving for θ with η fixed means η carries no gradient. And the **predictor exists to approximate an expectation** — the exact solution for η is `E_T[F_θ(T(x))]`, the average representation over augmentations, which SimSiam approximates with a *single* sample; the predictor learns to supply the missing expectation.

Two proof-of-concept experiments support it:

- **Multi-step alternation** (k SGD steps per outer loop): 1-step **68.1** (= SimSiam), 10-step 68.7, 100-step 68.9, 1-epoch 67.0. All work; SimSiam is the k=1 special case.
- **Moving-average η instead of a predictor**: maintaining `η_x ← m·η_x + (1−m)·F_θ(T′(x))` reaches **55.0% with no predictor at all**, where removing the predictor otherwise gives 0.1. Evidence that the predictor's job is approximating `E_T[·]`.

> [!warning] They are explicit about what the hypothesis does not do
> *"Our hypothesis is about what the optimization problem can be. **It does not explain why collapsing is prevented.** … SimSiam and its variants' non-collapsing behavior still remains as an empirical observation."*
>
> So as of 2020, three papers in a row ([BYOL](byol-paper.md), [DINO](dino-paper.md), SimSiam) have a working anti-collapse mechanism and an admittedly incomplete account of why it works. That is the gap [SIGReg](../concepts/world-models/sigreg.md) is built to close, and this page is the clearest statement of it from inside the pre-SIGReg era.

## Results in context

ImageNet linear, ResNet-50, two 224² views, all reproduced by the authors:

| | batch | negatives | momentum enc. | 100 ep | 800 ep |
|---|---:|:---:|:---:|---:|---:|
| SimCLR | 4096 | ✓ | | 66.5 | 70.4 |
| MoCo v2 | 256 | ✓ | ✓ | 67.4 | 72.2 |
| BYOL | 4096 | | ✓ | 66.5 | **74.3** |
| SwAV | 4096 | | | 66.5 | 71.8 |
| **SimSiam** | **256** | | | **68.1** | 71.3 |

**Best at 100 epochs, worst gain from training longer.** Transfer (VOC/COCO detection + instance segmentation) is competitive with all of them, and every method here matches or beats ImageNet-supervised pretraining — which they read as evidence that *"the Siamese structure is a core factor for their general success."*

## The contradiction this resolves — and the correction it forces

The wiki filed [BYOL Table 5b row 7](byol-paper.md) (predictor, no target network, no negatives → **0.2%**) against SimSiam's claim that the configuration works, and called it unresolved. Both are right, and **the answer was in BYOL's own paper**:

> [!warning] Correction — BYOL's appendix answers this, and this wiki's BYOL page did not read it
> SimSiam's footnote 2 points straight at it: *"In BYOL's arXiv v3 update, it reports **66.9% accuracy** with 300-epoch pre-training when removing the momentum encoder and **increasing the predictor's learning rate by 10×**."*
>
> BYOL v3 **Table 21** — hard-copy the online weights into the target (no EMA at all), sweeping a predictor learning-rate multiplier λ: **λ=0 → 0.01, λ=1 → 5.5, λ=2 → 62.8, λ=10 → 66.6, λ=20 → 66.3**, against a 72.5 baseline. Table 22 sweeps projector and predictor multipliers jointly and tops out at **66.9**.
>
> So the main-text 0.3% row is **λ=1**, the un-tuned case. The [BYOL page here](byol-paper.md) was written from pages 1–9 and presented the contradiction as needing an outside source; it did not. Corrected there.
>
> **What survives, and it is the more interesting statement:** removing the EMA costs ~6 points (72.5 → 66.6) even when you tune for it. The moving average is *not* the collapse-prevention mechanism — but it is worth real accuracy. And SimSiam, tuning differently (constant predictor lr, batch 256, SGD), gets within ~4 points of BYOL at 800 epochs while beating it at 100.

## Entities mentioned

- [Meta FAIR](../entities/meta-fair.md) — both authors.
- [SimSiam](../entities/simsiam.md) · [BYOL](../entities/byol.md) · [SimCLR](../entities/simclr.md) · [MoCo](../entities/moco.md).

## Concepts touched

- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — where this sits.
- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) · [SIGReg](../concepts/world-models/sigreg.md) · [JEPA](../concepts/world-models/jepa.md).
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — the 1/√d std monitor and the k-NN progress monitor.

## Open questions

- **Does the 1/√d std check work on an action-conditioned latent?** It is cheaper than SIGReg's own diagnostic and needs no target distribution to be *trained* toward, only compared against. Nothing in this wiki has tried it on a world model.
- **Is the EM reading compatible with the spectral one?** [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) casts SSL as spectral embedding on an affinity graph; SimSiam casts it as alternating optimization with per-image latent variables. Both are framed as unifications and neither cites the other in what this wiki holds.
- **The multi-step result (68.9 at 100 steps vs 68.1 at 1) was never pursued.** It is better, at the cost of caching η. Nobody scaled it.
