---
title: MoCo (Momentum Contrast) / MoCo v3
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 4
tags: [moco, moco-v3, momentum-encoder, contrastive-learning, vit, instability, meta-fair, kaiming-he, self-supervised]
---

**MoCo — Momentum Contrast** (He et al., CVPR 2020), through **MoCo v2** (+projection head, stronger augmentation) to **MoCo v3** ([paper](../sources/moco-v3-paper.md), Chen, Xie & He, ICCV 2021). InfoNCE with a **momentum-updated key encoder**, introduced as an alternative to a memory bank for keeping a large, consistent set of negatives.

> [!note] Two placements worth knowing
> **The momentum encoder is not MoCo's invention.** [The Cookbook](../sources/ssl-cookbook.md) traces it to **Wu et al. 2018**, via proximal optimization, alongside the temperature and explicit normalization. MoCo's contribution is the *queue*-replacing use of it.
>
> And the Cookbook files **MoCo in the self-distillation family, not the contrastive one** — because the momentum encoder is its defining mechanism even though its loss is InfoNCE. This wiki's [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) sorts it the other way. Both cuts are defensible; they cross-cut.

**MoCo v3** drops the queue entirely (*"diminishing gain if the batch is sufficiently large"*), symmetrizes the loss, and adds a prediction head to the query encoder only. ResNet-50 800-ep linear: v2 **71.1** → v2+ **72.2** → v3 **73.8**.

## Why the v3 paper matters more than the method

*"This paper does not describe a novel method."* It is an empirical study of ViT + Siamese SSL, and its finding is methodological:

**Instability degrades accuracy by 1–3% without diverging, and it is invisible without a more stable run to compare against.** Re-running the same config varies by only 0.1–0.3%, so seed variance does not expose it either. *"Unlike catastrophic failure that is easily noticeable, the small degradation can be fully hidden."*

The instrument that reveals it is a **k-NN monitor during training** — loss curves look fine, k-NN curves dip. Gradient ℓ∞-norm spikes appear **first in the patch-projection layer**, which motivates the fix: **freeze it at random initialization**. +1.7 points for MoCo v3 at the largest learning rate, **+0.8 for SimCLR, +1.3 for BYOL**, and a usable larger learning rate for SwAV, which otherwise NaNs.

Batch size on ViT-B/16: 1024 → 71.5, **2048 → 72.6**, 4096 → 72.2 with dips, 6144 → 69.7. **Bigger is not better past ~2k here** — the opposite of the contrastive folklore.

## The saturation number

| MoCo v3 | 300 ep | 600 ep |
|---|---:|---:|
| ViT-S/16 | 72.5 | 73.4 |
| ViT-B/16 | 76.5 | **76.7** |

**+0.2 for doubling the schedule on ViT-B** — the source of [MAE](mae.md)'s "MoCo v3 saturates at 300 epochs," now sourced from the primary rather than from MAE. The qualification MAE omits: **ViT-S still gains +0.9**, so saturation is a model/schedule property, not a property of contrastive learning.

Two ViT results with reach: **position embeddings contribute only 1.6 points** (sin-cos 76.5, none 74.9) — the model works nearly as well on a permutation-invariant *set* of patches; and the `[CLS]` token is dispensable (76.3 with mean pooling) provided you also drop the final LayerNorm (69.7 if you keep it).

## Related

- [SimCLR](simclr.md) · [BYOL](byol.md) · [SimSiam](simsiam.md) · [DINO](dino.md) — the framework comparison, whose **ranking changes between ResNet-50 and ViT-B**.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — the k-NN training monitor as an instability detector.
- [MAE](mae.md) — quotes MoCo v3's saturation as its scaling contrast.
- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md).

## Mentioned in

- [MoCo v3 paper (Chen, Xie & He, 2021)](../sources/moco-v3-paper.md) — the primary.
- [A Cookbook of Self-Supervised Learning](../sources/ssl-cookbook.md) — the momentum-encoder lineage and the family placement.
