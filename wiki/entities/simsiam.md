---
title: SimSiam
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 2
tags: [simsiam, stop-gradient, siamese, self-supervised, anti-collapse, meta-fair, kaiming-he, em-algorithm]
---

**SimSiam** — Chen & He ([paper](../sources/simsiam-paper.md), FAIR, CVPR 2021). A plain weight-sharing Siamese network with a **predictor on one branch and a stop-gradient on the other**. No negatives, no momentum encoder, no clustering, no large batch, no LARS. **67.7%** ImageNet linear top-1.

Its value is subtractive: it is *"[BYOL](byol.md) without the momentum encoder,"* *"[SimCLR](simclr.md) without negative pairs,"* and *"SwAV without online clustering"* — each obtained by deleting the one component that method claimed to need.

## The one thing that matters

| | Linear top-1 |
|---|---:|
| with stop-gradient | **67.7 ± 0.1** |
| without stop-gradient | **0.1** |

Everything else is accuracy, not collapse: batch size **flat from 128 to 2048** with plain SGD; removing all BN from the heads gives a poor-but-uncollapsed 34.6; cross-entropy instead of cosine similarity works (63.2); removing symmetrization works (64.8). *"It is mainly the stop-gradient operation that plays an essential role."*

The predictor is the exception — remove it and you get 0.1, because with the symmetrized loss that makes stop-gradient equivalent to no stop-gradient. Freeze it at random init and training fails **without collapsing** (loss stays high): it has to be *trained*. And **not decaying its learning rate beats the baseline** (68.1 vs 67.7).

> [!note] A collapse monitor worth stealing, five years early
> Track the **per-channel std of the ℓ2-normalized output**. Collapse → 0. A zero-mean **isotropic Gaussian** → **1/√d**, which is where the healthy run sits. Label-free, one line, and its reference distribution is the one [SIGReg](../concepts/world-models/sigreg.md) would later prove uniquely optimal and turn into a loss. See [representation evaluation](../concepts/learning/representation-evaluation.md).

## Why it is EM

Their hypothesis: SimSiam alternates between two variable sets — network parameters `θ` and a per-image representation `η_x` — *"analogous to k-means."* The **stop-gradient falls out of the derivation** (η is constant while solving for θ), and the **predictor exists to approximate an expectation over augmentations** that the single-sample approximation drops. Both are tested: multi-step alternation works and is slightly *better* (68.9 at 100 steps), and replacing the predictor with a moving-average η reaches **55.0% with no predictor at all**, where removing the predictor otherwise gives 0.1.

They also say what it does not do: *"It does not explain why collapsing is prevented… [that] still remains as an empirical observation."*

## Where it sits

Best at 100 epochs among SimCLR / MoCo v2 / BYOL / SwAV / SimSiam (68.1), worst gain from training longer (71.3 at 800 vs BYOL's 74.3). Transfer to VOC/COCO detection and instance segmentation is competitive with all of them, and every method there matches or beats ImageNet-supervised pretraining — which they read as evidence that **the Siamese structure itself** is the common cause of success.

## Related

- [BYOL](byol.md) — the method it subtracts from; its appendix (Tables 21–22) independently shows the EMA is removable for ~6 points with a 10× predictor learning rate.
- [SimCLR](simclr.md) · [MoCo](moco.md) · [DINO](dino.md) — the contemporaries.
- [SIGReg](../concepts/world-models/sigreg.md) — what eventually replaced the whole empirical-anti-collapse era.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md).

## Mentioned in

- [SimSiam paper (Chen & He, 2020)](../sources/simsiam-paper.md) — the primary.
- [A Cookbook of Self-Supervised Learning](../sources/ssl-cookbook.md) — filed in the self-distillation family; the predictor-learning-rate condition.
