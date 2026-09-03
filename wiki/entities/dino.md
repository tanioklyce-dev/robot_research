---
title: DINO (self-distillation with no labels)
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 4
tags: [dino, self-distillation, vit, self-supervised, ema, centering-sharpening, anti-collapse, segmentation, knn, meta-fair, caron]
---

**DINO** — *self-**di**stillation with **no** labels*, Caron et al. ([paper](../sources/dino-paper.md), FAIR + Inria + Sorbonne, ICCV 2021). A student network predicts a momentum-EMA teacher's temperature-softmaxed output distribution under cross-entropy, with **centering and sharpening** of the teacher output as the entire anti-collapse mechanism. No negatives, no predictor, no batch norm when used with a ViT.

It is the first entry in the lineage this wiki has been citing from the middle: [DINOv2](dinov2.md) and [DINOv3](dinov3.md) are its scaling successors, and DINO-the-original is where the properties they inherit were found.

## The two emergent properties

Neither was designed for, and both are why the name is everywhere in this wiki:

- **Attention maps segment objects.** The `[CLS]` token's last-layer self-attention contains object boundaries with no segmentation supervision. Measured as Jaccard against VOC12 (ViT-S/16, thresholded at 60% of attention mass): **random 22.0, supervised 27.3, DINO 45.9**. Different heads attend to different objects or parts.
- **The features are k-NN classifiers.** **78.3%** ImageNet top-1 from a plain nearest-neighbour vote — no head, no fine-tuning, no augmentation. k-NN nearly matches linear probing (74.5 vs 77.0 on ViT-S/16), and **this emerges only with ViT**, not with ResNet-50 and not for other SSL methods on ViT.

The second is the load-bearing fact under this wiki's whole **frozen-encoder** design pattern — [DINO-WM](dino-wm.md), [DINO-world](dino-world.md), and every "frozen features + learned predictor" world model. If features were not usable without fine-tuning, none of those designs would exist.

## Anti-collapse: centering and sharpening

Two collapse modes, one operation each. **Centering** (subtract an EMA of the batch mean from the teacher output) prevents a single dimension dominating, but pushes toward uniform. **Sharpening** (low teacher temperature) does the reverse. Applying both balances them. The proof is a decomposition of the loss, `H(P_t, P_s) = h(P_t) + D_KL(P_t‖P_s)`: with either operation missing, **KL → 0** (constant output) and the entropy settles at a *different* value in each case.

Centering uses only **first-order batch statistics**, which is what makes DINO tolerant of batch size — an advantage over queue- and negative-based methods.

> [!warning] The momentum encoder is not optional, and the failure is total
> Remove it and DINO scores **0.1 / 0.1** — chance — on both k-NN and linear (Table 7, row 2). This is the concrete form of [Balestriero](randall-balestriero.md)'s complaint that DINO moves *"from almost state-of-the-art to completely random"* with hyperparameters, and the reason [SIGReg](../concepts/world-models/sigreg.md) exists.
>
> The nuance the papers downstream lose: a **teacher from the previous epoch** (no EMA, no momentum hyperparameter) reaches **66.6** k-NN — MoCo-v2/BYOL territory. The authors say outright that *"there is a space to investigate alternatives for the teacher."* The field went to bigger EMAs instead.

Two more ablation results worth carrying: **cross-entropy over softmaxed distributions beats MSE on embeddings by ~20 k-NN points**, so the loss form matters independently of anti-collapse; and **adding BYOL's predictor does nothing here** (71.8 vs 72.8) despite being essential in [BYOL](byol.md) — anti-collapse mechanisms are not modular across methods.

## Practicalities

**Patch size beats parameter count.** ViT-S/8 (21M) reaches 79.7 linear against ViT-B/16 (85M) at 78.2 — no extra parameters, at 180 vs 312 im/s. Multi-crop (2 global 224² + several local 96²) is worth ~5 k-NN points on its own. Cost: two 8-GPU servers over 3 days for 76.1% linear.

## Related

- [DINOv2](dinov2.md) · [DINOv3](dinov3.md) — the scaling successors; this wiki's coverage started with them.
- [BYOL](byol.md) — the method DINO takes its inspiration from, with a different similarity loss and no predictor.
- [MAE](mae.md) — the reconstruction alternative published the same year.
- [SIGReg](../concepts/world-models/sigreg.md) — the single-term regularizer proposed to replace DINO's EMA stack.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — the four mechanisms side by side.
- [DINO-WM](dino-wm.md) · [DINO-world](dino-world.md) — frozen-feature world models downstream.

## Mentioned in

- [DINO paper (Caron et al., 2021)](../sources/dino-paper.md) — the primary.
