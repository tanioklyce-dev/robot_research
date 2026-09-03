---
title: MAE (Masked Autoencoder)
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 1
tags: [mae, masked-autoencoder, reconstruction, self-supervised, vit, scaling, linear-probing, evaluation, meta-fair, kaiming-he]
---

**MAE — Masked Autoencoder**, He et al. ([paper](../sources/mae-paper.md), FAIR, CVPR 2022). Mask 75% of an image's patches, reconstruct the missing pixels with MSE. Two designs carry it: an **asymmetric encoder–decoder** in which the encoder sees only *visible* patches and never a mask token, and a **masking ratio high enough** to defeat the spatial redundancy that would otherwise make the task trivial.

In this wiki MAE is the **named opponent** of the [JEPA](../concepts/world-models/jepa.md) line — the concrete thing [Balestriero](randall-balestriero.md) means by "reconstruction-based method" — and the entity page exists so that opposition rests on the paper rather than on paraphrase.

## What it gets right

- **87.8%** ImageNet fine-tuned (ViT-H, 448px), using **IN1K data only** — beating DINO 82.8, MoCo v3 84.1, BEiT 85.2 at matched scale.
- **Speed.** Keeping mask tokens out of the encoder cuts pretraining FLOPs 3.3× and wall-clock **2.8–4.1×**. ViT-L for 1600 MAE epochs costs 31 h against MoCo v3's 36 h for 300.
- **Transfer.** COCO ViT-L **53.3 AP<sup>box</sup>** (supervised 49.3); ADE20K **53.6 mIoU** (supervised 49.9); iNaturalist and Places beating prior bests that had pretrained on 1–3.5 *billion* images.
- **It needs no augmentation.** Crop-only works, and **no augmentation at all still gives 84.0 fine-tuned**, because random masking regenerates the signal every iteration. Contrastive methods lose 13 (BYOL) and 28 (SimCLR) points under crop-only.
- **It cannot collapse**, which is why it needs no anti-collapse term and is robust to architecture choices.

## The disagreement, stated fairly

**Balestriero's case** ([Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md)): reconstruction loss carries no information about representation quality (two autoencoders, identical train *and* test MSE, ~20 points of downstream accuracy apart, under **linear and nonlinear** probes); and MSE gradients follow the pixel covariance's top eigenvectors, so the **low-frequency half is learned first and the useful half last**, which is MAE's slow convergence at equal FLOPs.

**MAE's own answer, which predates the objection by five years**: linear probing is the wrong metric. *"Linear probing and fine-tuning results are largely uncorrelated."* Tuning **one** transformer block moves ViT-L from **73.5 → 81.0**; MAE beats MoCo v3 at *every* partial-fine-tuning depth despite MoCo v3's higher linear probe. *"While the MAE representations are less linearly separable, they are stronger non-linear features."*

> [!warning] Neither side has run the other's experiment
> Balestriero's construction is a deliberately built autoencoder pair at small scale; MAE's is a pretraining-method comparison at ViT-L under a fine-tuning protocol. His claim explicitly covers nonlinear probes, which would defeat MAE's rebuttal *if it transfers* — and nothing establishes that it does. **What both agree on is the shape of the curve**: MAE's linear probing is still climbing at 1600 epochs while contrastive methods saturate at 300. Slow convergence of *linearly accessible* quality is not in dispute; whether that is a defect or an artifact of the probe is.
>
> One suggestive detail nobody has connected: MAE finds **PCA coefficients degrade** as a reconstruction target while **per-patch normalization** (which boosts local contrast, i.e. high frequency) **improves** results — *"the high-frequency components are useful in our method."* That is at least consistent with the spectral story being told against it.

## Ablations worth knowing

| Knob | Finding |
|---|---|
| Masking ratio | **75%** optimal (BERT uses 15%); linear probing spans 54.6 → 73.5 across ratios, fine-tuning nearly flat |
| Mask tokens in encoder | **−14 points linear probing** and **3.3× FLOPs**. Pretrain/deploy gap is the stated cause |
| Decoder depth | 1 block → 65.5 linear; 8 blocks → 73.5. Irrelevant to fine-tuning |
| Reconstruction target | Normalized pixels beat raw pixels, PCA, and dVAE tokens. *"Tokenization is not necessary"* |
| Mask sampling | Random beats block-wise and grid-wise |

## Related

- [JEPA](../concepts/world-models/jepa.md) — the family defined against this one.
- [DINO](dino.md) · [BYOL](byol.md) — the joint-embedding contemporaries.
- [Dreamer](dreamer.md) — the same reconstruction bet inside a world model; the same critique lands on its causal tokenizer.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — MAE as the member that needs no anti-collapse term at all.

## Mentioned in

- [MAE paper (He et al., 2021)](../sources/mae-paper.md) — the primary.
