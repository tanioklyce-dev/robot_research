---
title: SimCLR
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 4
tags: [simclr, contrastive-learning, nt-xent, projector, augmentation, google-brain, hinton, self-supervised]
---

**SimCLR** — Chen, Kornblith, Norouzi & Hinton ([paper](../sources/simclr-paper.md), Google Brain, ICML 2020). Two augmented views, an encoder, a small MLP **projection head**, and **NT-Xent** over in-batch negatives. No memory bank, no specialized architecture. **69.3%** ImageNet linear top-1 with ResNet-50; **76.5%** with ResNet-50(4×); **85.8%** top-5 from 1% of labels.

The canonical contrastive method, and the source of two mechanisms the rest of the field repeats.

## The colour-histogram shortcut

**No single augmentation suffices** — composition is what works, and **crop + colour distortion** is the pair that stands out. The reason is a measured shortcut: patches from one image share a colour distribution, and **colour histograms alone distinguish images**, so a contrastive task on crops alone is solvable by colour and the representation stops there.

That single mechanism explains [BYOL](byol.md)'s robustness pitch, the [Cookbook](../sources/ssl-cookbook.md)'s insistence on colour distortion, and [MAE](mae.md)'s contrast with augmentation-dependent methods. **It also generalizes**: the [financial time-series case](../concepts/economics/financial-time-series-augmentations.md) is the same failure — an augmentation whose invariance is solvable by a nuisance statistic — found by derivation instead of ablation.

Second finding from the same section: **contrastive learning wants *stronger* augmentation than supervised learning.** Increasing colour strength takes SimCLR 59.6 → 64.5 while taking the supervised baseline 77.0 → 75.4. AutoAugment, tuned by supervised search, loses to plain crop + strong colour.

## Why you use the layer before the projector

Nonlinear projection beats linear (+3%) and no projection (>10%) — and then **`h` beats `z = g(h)` by >10%**. The mechanism is measured: train a probe to predict which augmentation was applied.

| Predict | chance | from `h` | from `g(h)` |
|---|---:|---:|---:|
| Rotation | 25 | **67.6** | **25.6** |
| Original vs corrupted | 50 | 99.5 | 59.6 |

**The projector output is trained to be invariant, so it discards exactly what the invariance targets.** Rotation falls to chance. This is the concrete basis for *Guillotine Regularization* and for why every method since keeps the backbone and throws the head away.

> [!note] The batch-size reputation is a short-schedule artifact, per SimCLR's own §5.2
> SimCLR is remembered as the method that needs batch 4096. Its own paper says *"with more training steps/epochs, the gaps between different batch sizes decrease or disappear,"* and footnote 10 adds that **square-root learning-rate scaling** improves small-batch runs. What propagated was the 100-epoch ablation table, not the sentence underneath it — including into [this wiki](../concepts/learning/contrastive-learning.md) until it was corrected.

**Global BN** is a detail worth knowing: batch-norm statistics must be aggregated across devices, or positives computed on the same device let the model *"exploit the local information leakage to improve prediction accuracy without improving representations."* A second shortcut of the same family as the colour histogram.

**Bigger models benefit more from unsupervised than supervised learning** — the gap to supervised shrinks as size grows. That is the scaling argument later SSL papers inherit.

## Related

- [MoCo](moco.md) · [BYOL](byol.md) · [SimSiam](simsiam.md) · [DINO](dino.md) — the contemporaries; SimSiam is "SimCLR without negative pairs."
- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) — the family.
- [MAE](mae.md) — the reconstruction alternative that needs no augmentation at all.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md).

## Mentioned in

- [SimCLR paper (Chen et al., 2020)](../sources/simclr-paper.md) — the primary.
- [BYOL paper](../sources/byol-paper.md) · [MAE paper](../sources/mae-paper.md) · [MoCo v3 paper](../sources/moco-v3-paper.md) — where it is the standing baseline.
