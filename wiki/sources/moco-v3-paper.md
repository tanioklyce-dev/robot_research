---
title: "An Empirical Study of Training Self-Supervised Vision Transformers — MoCo v3 (Chen, Xie & He, 2021)"
type: source
url: https://arxiv.org/abs/2104.02057
fetch_url: https://arxiv.org/pdf/2104.02057v4
local_path: raw/2104.02057v4.pdf
sha256: 5f75bd90555f8d549e2b57328ede2f4383757114c8d9fc7955f959d62723b1c7
author: "Xinlei Chen, Saining Xie, Kaiming He (Facebook AI Research)"
published: 2021-04-05
venue: "ICCV 2021 (arXiv v4, 2021-08-16)"
format: paper (PDF, 10 pp.)
tags: [moco-v3, vit, instability, training-stability, self-supervised, contrastive-learning, patch-projection, knn-monitor, foundational]
ingested: 2026-09-03
---

## Summary

*"This paper does not describe a novel method."* It is an empirical study of what breaks when you put a ViT inside a Siamese SSL framework, and its finding is a methodological one that reaches well past SSL:

> **Instability degrades accuracy by 1–3% without ever diverging, and that degradation is invisible unless you already have a more stable run to compare against.**

Re-running the same config varies by only 0.1–0.3%, so **variance across seeds does not reveal it either**. Their words: *"This behavior is harmful to explorative research: unlike catastrophic failure that is easily noticeable, the small degradation can be fully hidden."*

Ingested because MoCo v3's *"saturates at 300 epochs"* behaviour is load-bearing for [MAE](mae-paper.md)'s scaling argument and this wiki was quoting it from MAE. It is confirmed here — and the paper turns out to be worth more for the instability result than for the number it was fetched to check.

## The instability finding, and how to see it

**The instrument is a k-NN monitor run during training.** Loss curves look fine; the k-NN curve shows *dips*. Gradient monitoring locates them: an ℓ∞-norm **spike appears first in the patch-projection layer and reaches later layers tens of iterations afterwards.**

**Batch size, MoCo v3 + ViT-B/16, 100 epochs, AdamW:**

| batch | 1024 | 2048 | 4096 | 6144 |
|---|---:|---:|---:|---:|
| linear acc. | 71.5 | **72.6** | 72.2 (dips) | 69.7 (big dips) |

More negatives help until instability outweighs them, and at 6144 *"the training does not diverge, but the accuracy depends on how good the local restart is"* — a partial failure that still reports a plausible 69.7%.

**Learning rate** shows the same shape: 0.5e-4 → 70.4 (underfits), 1.0e-4 → 72.2, 1.5e-4 → 71.7 (less stable). **LAMB** matches AdamW at its optimum (72.5) but falls off a cliff above it (−1.6 at 6e-4, −6.0 at 8e-4) with *smooth* curves that *"degrade gradually in the middle"* — a second failure mode that hides even better.

### The fix: freeze the patch projection

Use a **fixed random patch-projection layer** (stop-gradient right after it). It is not an architecture change — it *narrows* the solution space — and it works across frameworks:

| lr ×1e-4 | 0.5 | 1.0 | 1.5 |
|---|---:|---:|---:|
| learned patch proj. | 70.4 | 72.2 | 71.7 |
| **random patch proj.** | 70.8 | 72.8 | **73.4** |

Also **SimCLR +0.8** (69.3 → 70.1), **BYOL +1.3** (69.7 → 71.0), and SwAV — which *diverges* to NaN when unstable — gains a usable larger learning rate. BatchNorm or WeightNorm on that layer does not help; gradient clipping helps *"if given a sufficiently small threshold, which to the extreme becomes freezing the layer."*

The authors are careful about what they have shown: *"The trick alleviates the issue, but does not solve it… **The first layer is unlikely the essential reason for the instability**; instead, the issue concerns all layers. The first layer is merely easier to be handled separately."*

> [!note] Why this matters to a robotics wiki
> Three of this wiki's recurring problems are the same problem. **[Balestriero warns not to use planning success as a research signal](chicago-booth-world-modeling-workshop-2026-day3.md)** because it is slow and noisy — MoCo v3 shows the *fast* signal (loss) can be silently wrong too, and that the fix is a cheap **online monitor sensitive to the failure you care about**. **[Representation evaluation](../concepts/learning/representation-evaluation.md)** now carries both. And an ablation table comparing two SSL methods without stability monitoring may be comparing one stable run against one partially-failed run — which is a general caution on every "method A beats method B" row in this wiki.

## What MoCo v3 is

MoCo v1/v2 incrementally simplified: InfoNCE over keys **co-existing in the batch**, with **the memory queue abandoned** (*"diminishing gain if the batch is sufficiently large"*); symmetrized loss; query encoder = backbone + projection head + **prediction head**; key encoder = momentum copy without the prediction head. ResNet-50 800-ep linear: MoCo v2 71.1 → MoCo v2+ 72.2 → **MoCo v3 73.8**, mainly from the extra prediction head and batch 4096.

**Framework comparison** (ImageNet linear, two 224² crops, random patch projection throughout):

| | MoCo v3 | SimCLR | BYOL | SwAV |
|---|---:|---:|---:|---:|
| ResNet-50, 800 ep | 73.8 | 70.4 | **74.3** | 71.8 |
| ViT-S/16, 300 ep | **72.5** | 69.0 | 71.0 | 67.1 |
| ViT-B/16, 300 ep | **76.5** | 73.9 | 73.9 | 71.6 |

**The ranking changes with the backbone** — BYOL leads on ResNet-50 and ties for third on ViT-B. A method comparison is not backbone-independent.

## The number this was fetched to check

| MoCo v3 | 300 ep | 600 ep |
|---|---:|---:|
| ViT-S/16 | 72.5 | 73.4 |
| ViT-B/16 | 76.5 | **76.7** |

**+0.2 points for doubling the schedule on ViT-B.** So [MAE](mae-paper.md)'s characterization — that MoCo v3 saturates where MAE's linear probing is still climbing at 1600 epochs — is fair, and is now sourced from the primary rather than from MAE. Note the qualification MAE does not carry: **ViT-S still gains +0.9**, so saturation is a property of the model/schedule pairing, not of contrastive learning as such.

## Two ViT findings with reach beyond SSL

- **Position embeddings contribute 1.6 points.** sin-cos 76.5, learned 76.1, **none 74.9**. *"The model can learn strong representations just by a set of patches, which are fully permutation-invariant… On the negative side, it also suggests that the model has not made good use of positions, and the gesture of the object contributes relatively little."* For a wiki whose world models care about spatial structure, that is a pointed result.
- **The `[CLS]` token is not the point; the LayerNorm after it is.** With `[CLS]` 76.5; without `[CLS]` but keeping the final LN and pooling **69.7**; without both, pooling only, **76.3**.

**Cost, for calibration:** ViT-H at 300 epochs is ≈ **625 TPU·days (~1.7 TPU·years)**; ViT-B is 2.1 h per 100 epochs on 256 TPUs, versus 24 h on 128 GPUs.

## Entities mentioned

- [Meta FAIR](../entities/meta-fair.md) — all three authors.
- [MoCo](../entities/moco.md) · [SimCLR](../entities/simclr.md) · [BYOL](../entities/byol.md) · [DINO](../entities/dino.md) · [MAE](../entities/mae.md).

## Concepts touched

- [Representation evaluation](../concepts/learning/representation-evaluation.md) — the k-NN training monitor as an instability detector.
- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) · [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) · [JEPA](../concepts/world-models/jepa.md).

## Open questions

- **Has anyone checked JEPA-family training for hidden instability?** [LeJEPA](lejepa-paper.md)'s central claim is *stability*, and its evidence is loss curves plus 50+ architectures training to within a small delta. MoCo v3's point is that loss curves are exactly what hides this failure. A k-NN or [RankMe](../concepts/learning/representation-evaluation.md) monitor over a LeJEPA run would test the claim on the axis it is made about.
- **Does the frozen-patch-projection trick transfer to video and to world models?** It is architecture-neutral and free. Nothing in this wiki mentions it.
- **Is the "positions contribute 1.6%" result still true at scale and on video?** If so it is an argument about what ViT-based world models are actually encoding.
