---
title: "You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences"
type: source
url: https://arxiv.org/abs/2606.15956
local_path: raw/tdv_2606.15956.pdf
sha256: 2becb6e3a77c05861ed1b1179c8443fc717dc166cbc0b90f54256a07a2117dba
author: Ninad Daithankar, Alexi Gladstone, Yann LeCun, Heng Ji
published: 2026-06-14
ingested: 2026-08-26
venue: arXiv (cs.CV, cs.AI, cs.LG)
format: paper (25 pp)
tags: [self-supervised-learning, inductive-bias, video, representation-learning, dino, ibot, optical-flow, depth, scaling, lecun]
---

# You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences

## Summary

Two contributions, and the first is more portable than the second. **(1) An empirical scaling claim**: the *optimal strength of [inductive bias](../concepts/learning/inductive-bias.md) decreases as data grows*, tested by sweeping masking ratio across subsets of ImageNet-1k. **(2) TDV (Temporal Difference in Vision)**, an SSL method that drops the augmentation/masking/cropping biases modern SSL still relies on, keeping only a **causal** assumption — the past causes the future. A frame encoder and a **motion encoder** are jointly trained so that *current frame representation + encoded motion = next frame representation*.

## Key claims

### The scaling result

Sweeping masking ratio (as a proxy for assumption strength) across ImageNet-1k subsets, measured by KNN accuracy:

- At **0.1% of ImageNet**, the best masking ratio is **50%**; 30% and 10% fall behind "by a significant margin."
- As data grows, **30% masking eventually overtakes 50%**, and **10% approaches 50%**.

The generalization offered: strong assumptions "encode beliefs that are only approximately correct," and at scale the approximation error dominates the guidance benefit. If the trend holds, today's remaining SSL biases become tomorrow's bottleneck.

### TDV mechanism

`ẑ_{t+1} = z_t + Δz_t`, matched by MSE against a stop-gradient EMA-teacher encoding of frame t+1. The motion encoder compresses the **raw RGB difference** between frames, forcing it to capture "compact spatial change rather than full scene appearance."

**Naively removing DINO's inductive biases collapses the representation** (their Table 1) — so TDV adds a **DINO-style self-distillation cross-entropy** as the anti-collapse term, with one extension: applied over **both the [CLS] token and the patch tokens**, "encouraging spatially consistent representations at the patch level."

> [!note] The "no strong assumptions" framing has an asterisk
> TDV still requires an EMA teacher, a stop-gradient, and a DINO self-distillation loss to avoid collapse. What it removes is **augmentation, masking, and cropping**. That is a real reduction, but the paper's own Table 1 establishes that the causal assumption *alone* leaves no learning signal — so "learning without strong inductive biases" means *without the image-level ones*, not without machinery.

### Results — it wins on motion, loses slightly on semantics

**Semantic segmentation (UperNet), ViT-S / SSv2 pretraining:**

| Method | ADE20K mIoU | Cityscapes mIoU |
|---|---:|---:|
| iBOT | 10.60 | 39.34 |
| DINO | **10.71** | **39.85** |
| **TDV** | 10.54 | **37.54** |

**Optical flow and stereo depth, ViT-S / SSv2:**

| Method | Sintel EPE (clean) | Sintel EPE (final) | SceneFlow bad@1px |
|---|---:|---:|---:|
| iBOT | 11.31 | 11.27 | 44.91 |
| DINO | 13.03 | 12.92 | 45.30 |
| **TDV** | **9.84** | **10.75** | **39.70** |

> [!warning] "Matches state-of-the-art on dense spatial tasks" is doing work
> On segmentation TDV is **level on ADE20K and ~2.3 mIoU behind DINO on Cityscapes** — matched, not better. Where it clearly wins is **optical flow (9.84 vs 13.03 EPE) and stereo depth** (bad@1px 39.70 vs 45.30), with a small trade-off on stereo depth *average* error. That is a coherent and unsurprising pattern rather than a disappointment: a method trained on temporal differences learns motion structure, and motion tasks are where it shows. The wiki should record it as **a motion-representation method that stays competitive on semantics**, not as a general SSL replacement.

## Relevance to this wiki

Adjacent rather than central. TDV is not a world model — there is no action conditioning and no planning — but the update rule `z_t + Δz_t = z_{t+1}` is a linear-in-latent-space transition model learned from video, which is the same structural bet [JEPA](../concepts/world-models/jepa.md) makes. Two things carry over:

- **The scaling claim bears on the whole JEPA program.** The wiki's JEPA material tracks an [anti-collapse design space](../concepts/world-models/jepa.md) that has been getting *lighter* over time — from EMA + stop-grad + frozen encoder, to VICReg, to a single distributional regularizer ([SIGReg](../entities/leworldmodel.md)), to a single inverse-dynamics term ([SMWM](../entities/smwm.md)). TDV supplies an argument for *why* that trajectory should be expected to continue, and a measured instance of it.
- **The backbone question.** [Patch Policy](patch-policy-paper.md), same batch and overlapping authors, finds visual representation quality is "a primary bottleneck for policy learning, independent of the downstream action head." TDV is an attempt to build better dense features. It was not evaluated as a policy backbone.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md), Heng Ji (UIUC).
- [DINO / DINOv2](../entities/dinov2.md), **iBOT** — baselines.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — architectural cousin; the anti-collapse machinery it reuses.
- [Learned latent space](../concepts/world-models/latent-space.md) — additive latent transitions.
- **[Inductive bias](../concepts/learning/inductive-bias.md)** — this paper is the wiki's most direct measurement of the bias-vs-data-scale trade-off, and the source of the mechanism it offers (strong assumptions encode only-approximately-correct beliefs, and at scale the approximation error dominates the guidance benefit).
- **Self-supervised learning** — the scaling claim.

## Open questions

- **The scaling experiment varies one bias (masking ratio) on one dataset.** "Optimal assumption strength decreases with data" is a broad claim resting on a narrow probe.
- **Pretraining is SSv2 only** — a relatively small, human-action-centric video dataset. No web-scale video run, which is the regime the scaling argument points at.
- **Never tested on control or robotics.** The obvious experiment given the co-authors — TDV features as a [Patch Policy](patch-policy-paper.md) backbone — is not run.
