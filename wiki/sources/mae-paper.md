---
title: "Masked Autoencoders Are Scalable Vision Learners (He et al., 2021)"
type: source
url: https://arxiv.org/abs/2111.06377
fetch_url: https://arxiv.org/pdf/2111.06377v3
local_path: raw/2111.06377v3.pdf
sha256: 1b490443925c72a2b7c770f90dd797e248729ae34a57e1abfe9ed36751c4cc5b
author: "Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, Ross Girshick (Facebook AI Research)"
published: 2021-11-11
venue: "CVPR 2022 (arXiv v3, 2021-12-19)"
format: paper (PDF, 14 pp.)
tags: [mae, masked-autoencoder, reconstruction, self-supervised, vit, scaling, linear-probing, fine-tuning, evaluation, foundational]
ingested: 2026-09-03
---

## Summary

**The strongest statement of the position the JEPA line argues against — made by the people who built it, with the trade-off disclosed.** MAE masks 75% of an image's patches and reconstructs the missing pixels with MSE. Two designs make it work: an **asymmetric encoder–decoder** where the encoder sees only the *visible* patches and never a mask token, and a **very high masking ratio** that destroys the spatial redundancy that would otherwise make the task trivial. Result: 3–4× faster pretraining and 87.8% ImageNet-1k fine-tuned accuracy with a vanilla ViT-Huge on IN1K data alone.

The wiki needed this primary for a specific reason. [Balestriero's Day 3 argument](chicago-booth-world-modeling-workshop-2026-day3.md) — that reconstruction learns the low-frequency half first and the useful half last, and that MAE at equal FLOPs is far behind a JEPA — is aimed at this paper. **MAE's own results both support that and complicate it**, and the complication is the reason to read it rather than cite around it.

## Key claims

**Why masked autoencoding lagged in vision, in three parts** (§1): architectures differed until ViT; **information density differs** — language is human-generated and semantic, images have *"heavy spatial redundancy"* so a missing patch is recoverable from its neighbours *"with little high-level understanding"*; and **the decoder's role differs**, since in vision it outputs pixels, *"of a lower semantic level than common recognition tasks."* The high masking ratio is the answer to the second; the asymmetric design is the answer to the third.

**The asymmetric design** (§3). The encoder is a plain ViT applied **only to visible patches** — mask tokens are introduced afterwards, in a lightweight decoder (default 8 blocks, 512-d, <10% of encoder FLOPs per token). Loss is MSE **on masked patches only**. Implementation needs no sparse ops: shuffle tokens, drop the tail, encode, append mask tokens, unshuffle, decode.

**The ablations, which are the paper's real contribution:**

| Finding | Numbers (ViT-L/16, IN1K) |
|---|---|
| **Masking ratio** | Optimal **75%**, vs BERT's 15%. Linear probing spans **54.6 → 73.5** across ratios; fine-tuning is nearly flat (83.0–85.0) |
| **Mask tokens in the encoder** | Including them costs **14 points of linear probing** (73.5 → 59.6) *and* **3.3× the FLOPs**. The pretrain/deploy gap is the stated cause |
| **Decoder depth** | 1 block → 65.5 linear; 8 blocks → **73.5**. Barely matters for fine-tuning (84.8 vs 84.9) |
| **Reconstruction target** | Normalized pixels **85.4 / 73.9** beats raw pixels (84.9 / 73.5), PCA coefficients (84.6 / 72.3) and dVAE tokens (85.3 / 71.6). *"Tokenization is not necessary"* |
| **Augmentation** | Crop-only works; **no augmentation at all still gives 84.0 / 65.7**. Contrastive methods lose 13 (BYOL) and 28 (SimCLR) points under crop-only |
| **Mask sampling** | Random 75% (84.9/73.5) beats block-wise and grid-wise |
| **Schedule** | Linear probing **not saturated at 1600 epochs** (57.3 → 75.1 from 100 to 1600). MoCo v3 saturates at 300 |

**Speed and scale.** ViT-L 800 epochs: 42.4 h with mask tokens in the encoder, **15.4 h without** (2.8×), 11.6 h with a 1-block decoder (3.7×). ViT-H reaches 4.1×. Total wall-clock beats contrastive methods outright: **ViT-L for 1600 MAE epochs is 31 h against MoCo v3's 36 h for 300**.

**Headline results.** ViT-H fine-tuned **86.9%** (224px) / **87.8%** (448px), IN1K only — beating DINO 82.8, MoCo v3 84.1, BEiT 85.2 at matched scale. COCO detection ViT-L **53.3 AP<sup>box</sup>** vs supervised 49.3. ADE20K **53.6 mIoU** vs supervised 49.9. iNaturalist and Places beat prior bests obtained by pretraining on 1–3.5 *billion* images.

## The evaluation argument, which is the part that matters here

> [!warning] MAE's authors reject linear probing as the metric — and that is exactly the metric Balestriero's case rests on
> §4.3: *"linear probing and fine-tuning results are largely uncorrelated."* Their evidence is **partial fine-tuning**. Tuning **one** transformer block moves ViT-L from **73.5 → 81.0**; tuning half a block (the MLP sub-block) already gives 79.1. And against MoCo v3, which has the **higher linear probe**, MAE wins at *every* partial-fine-tuning depth — by 2.6 points at four blocks. Their conclusion: *"while the MAE representations are less linearly separable, they are stronger non-linear features."*
>
> This is a live disagreement with the wiki's [JEPA](../concepts/world-models/jepa.md) page, and it should be recorded as one rather than resolved by preference:
>
> - **Balestriero's Day 3 claim covers it in advance.** His two-autoencoder demonstration reports the ~20-point gap holding **under nonlinear probes as well as linear** — *"you might think you just artificially untangle the features, but a nonlinear predictor will classify it good — no, you still have a gap."* If that holds, MAE's rebuttal does not apply to his construction.
> - **But the constructions are not comparable.** His is a deliberately built pair of autoencoders with matched MSE, on a small setting; MAE's is a comparison of pretraining methods at ViT-L scale under a fine-tuning protocol. **Neither paper runs the other's experiment.**
> - **The one thing they agree on is the shape of the curve.** MAE's own Figure 7 shows linear probing still climbing at 1600 epochs while contrastive methods saturate at 300. Slow convergence of *linearly accessible* representation quality is not in dispute — the question is whether that is a defect or an artifact of the probe.

The second wiki-relevant disclosure is the augmentation result. MAE works with **no augmentation**, because random masking regenerates the training signal every iteration. Contrastive and JEPA-family methods cannot: *"the two views of an image are the same and can easily satisfy a trivial solution."* That is the flip side of "reconstruction cannot collapse" — reconstruction gets **invariance specification for free** where the joint-embedding family must design it, which is precisely the problem [financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) documents as hard in a new domain.

## Entities mentioned

- [Meta FAIR](../entities/meta-fair.md) — all six authors (as Facebook AI Research).
- [MAE](../entities/mae.md) — the method's entity page.
- [DINO](../entities/dino.md) — the SSL baseline it outperforms on fine-tuning.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the family defined in opposition to this one.
- [SIGReg](../concepts/world-models/sigreg.md) · [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — MAE is the member that needs no anti-collapse term at all.
- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md).
- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) — where the frequency-ordering argument against reconstruction is formalized.

## Open questions

- **Does the spectral argument predict MAE's own ablations?** Balestriero's claim is that MSE gradients follow the pixel covariance's top eigenvectors, so low frequencies are learned first. MAE reports that **PCA coefficients as a reconstruction target degrade accuracy** and that per-patch normalization (which boosts local contrast, i.e. high frequency) **improves** it — *"both experiments suggest that the high-frequency components are useful in our method."* That is at least consistent with the spectral story, and possibly a prediction it makes. Nobody has connected them.
- **What does a JEPA look like under partial fine-tuning?** MAE's strongest defence is a protocol the JEPA literature does not report. The wiki has no source that evaluates [LeJEPA](lejepa-paper.md) or [V-JEPA 2](../entities/v-jepa-2.md) features by tuning `k` blocks.
- **The Philadelphia driving result on the [Day 3 backlog](../backlog.md) is an MAE-style model beating a vision-only V-JEPA** with extra sensor streams. If found, it is a second data point for reconstruction where the wiki currently has only arguments against it.
- **MoCo v3 is cited as the contrastive baseline throughout and is not ingested here.** Its saturation-at-300-epochs behaviour is load-bearing for MAE's scaling claim.
