---
title: "DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control"
type: source
url: https://arxiv.org/abs/2409.12192
local_path: raw/dynamo_2409.12192.pdf
author: Zichen Jeff Cui, Hengkai Pan, Aadhithya Iyer, Siddhant Haldar, Lerrel Pinto
published: 2024-09-18
ingested: 2026-08-26
venue: "arXiv (NYU); NeurIPS 2024"
format: paper (23 pp)
tags: [dynamo, in-domain-pretraining, self-supervised, inverse-dynamics, forward-dynamics, latent-prediction, imitation-learning, anti-collapse, lerrel-pinto, vq-bet]
---

# DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control

## Summary

Argues that visual representations for imitation learning are trained the wrong way twice over: either **pretrained on out-of-domain data** (ImageNet, R3M, VC-1) or **trained directly through the behavior-cloning objective**, and both are data-inefficient. DynaMo is the third option — **in-domain self-supervised pretraining on the expert demonstrations you already have.** Given a demo set, it jointly learns a **latent inverse dynamics model** and a **latent forward dynamics model** over image embeddings, predicting the next frame *in latent space*, with **no augmentations, no contrastive sampling, no ground-truth actions, and no out-of-domain data whatsoever**. Reports **+39% overall** downstream policy performance over prior self-supervised and pretrained representations.

## Why this belongs in the wiki despite predating its world-model thread

> [!note] DynaMo is a JEPA in everything but name, from the lab that later argued against it
> Latent next-frame prediction, an inverse-dynamics term, an explicit anti-collapse mechanism — this is the [JEPA](../concepts/world-models/jepa.md) recipe, published September 2024, framed as representation learning for imitation rather than as a world model. It belongs on the wiki's [anti-collapse design space](../concepts/world-models/jepa.md#common-training-challenges) and predates [SMWM](../entities/smwm.md), which the wiki records as introducing inverse-dynamics regularization as a *sole* anti-collapse mechanism in 2026. DynaMo got there first with inverse dynamics as *half* of the objective.
>
> And the lab's own trajectory is the interesting part: [Lerrel Pinto](../entities/lerrel-pinto.md)'s group published DynaMo (2024, **in-domain**, train your own encoder) and then [Patch Policy](patch-policy-paper.md) (2026, **out-of-domain**, freeze someone else's web-scale encoder and use its patch tokens) — where **DynaMo is the baseline Patch Policy beats.**

## Key claims

### Method

- Jointly train **encoder + latent inverse dynamics + latent forward dynamics**, end-to-end, predicting the next embedding.
- **Anti-collapse is two mechanisms, not one**: a **SimSiam-style stop-gradient** on the target embedding `s*ₜ := sg(sₜ)` (with an EMA momentum encoder named as a compatible alternative), **plus covariance regularization** at **λ = 0.04**, following VICReg. The paper is direct about why: *"Naively, this objective admits a constant embedding solution."* Covariance regularization "slightly improves downstream task performance" — it is the smaller of the two effects.
- Multi-view environments compute the loss per view and average.
- **No augmentations, no contrastive negatives, no action labels.**

> [!note] Placement on the anti-collapse ladder
> DynaMo sits at the **heavy** end: stop-gradient *and* a variance-covariance term, i.e. roughly where [PLDM](../entities/pldm.md) sits, and well above [SIGReg](../concepts/world-models/sigreg.md)'s single distributional regularizer or [SMWM](../entities/smwm.md)'s single inverse-dynamics term. The wiki's ladder has been getting lighter over time; DynaMo is a datapoint near its start.

### Results

- **+39% overall** over prior SSL and pretrained representations, **concentrated on the harder closed-loop tasks** — Block Pushing and Push-T — and on real robots.
- **Six environments**: Franka Kitchen, Block Pushing, Push-T, LIBERO Goal (simulated); **Allegro Manipulation** (Allegro Hand on a Franka, 23-D action space) and **xArm Kitchen** (multi-task, goal-conditioned BAKU + VQ-BeT head) (real).
- **Policy-class agnostic**: gains hold across **Behavior Transformer, Diffusion Policy, MLP, and nearest neighbors**.
- **Low-data regime**: real Allegro tasks trained from as few as **6 demonstrations**.
- Baselines: Random / ImageNet / **R3M** (ResNet18 weights), **VC-1**, **MVP**, **MAE** (ViT-B), plus **BYOL, MoCo, TCN**. DynaMo and most baselines use a **ResNet18** backbone.

## The tension with the wiki's later material

[Patch Policy](patch-policy-paper.md) (2026, overlapping authors) reports DynaMo as a **globally-pooled-feature** baseline and beats it decisively on the spatial tasks: DynaMo VQ-BeT scores **0.65 / 0.28** on BlockPush / Cube against WebSSL-patch VQ-BeT's **1.68 / 1.68**.

That is not a refutation of DynaMo — it is a change of subject. DynaMo's claim is *how to pretrain when you have only in-domain demos*; Patch Policy's is *how to consume features you did not train*. The comparison is fair only in the regime where a strong frozen web encoder exists and the task is in-domain with enough demonstrations, which is exactly Patch Policy's stated scope. **Where the wiki should be careful is in reading Patch Policy's win as evidence that in-domain pretraining is obsolete** — nothing tests DynaMo in the low-demo regime it was built for (6 demonstrations) against a frozen web backbone.

## Entities mentioned

- [DynaMo](../entities/dynamo.md) — the method.
- [Lerrel Pinto](../entities/lerrel-pinto.md) — senior author; **Zichen Jeff Cui** is also first author here and a [Patch Policy](patch-policy-paper.md) co-author.
- [VQ-BeT](../entities/vq-bet.md) / [Diffusion Policy](../entities/diffusion-policy.md) / [LIBERO](../entities/libero.md) — policy heads and benchmark.
- **R3M, VC-1, MVP, BYOL, MoCo, TCN, BAKU, Allegro Hand** — no pages.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the architecture family it belongs to without the label.
- [SIGReg](../concepts/world-models/sigreg.md) — the later, lighter anti-collapse alternative.
- [Imitation learning](../concepts/learning/imitation-learning.md) — the setting.
- [VLA models](../concepts/learning/vla-models.md) — the alternative route to the same tasks.

## Open questions

- **No comparison against frozen web-scale SSL** — DINOv2 is not a baseline here, and the strongest 2026 result says frozen DINOv2/WebSSL patch features beat in-domain pretraining. Whether DynaMo *plus* a strong frozen backbone beats either alone is untested.
- **ResNet18 backbone** for DynaMo against ViT-B for the MAE-style baselines — an architecture confound the paper does not fully separate.
- **"39% improvement" is an aggregate** across six environments and several policy classes; the per-task spread is not summarized here, and the wiki's [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) standard would want trial counts.
