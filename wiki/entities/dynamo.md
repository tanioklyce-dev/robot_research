---
title: DynaMo
type: entity
subtype: method
created: 2026-08-26
updated: 2026-08-26
sources: 2
tags: [dynamo, in-domain-pretraining, self-supervised, inverse-dynamics, forward-dynamics, latent-prediction, anti-collapse, imitation-learning, lerrel-pinto, nyu]
---

**DynaMo** — **in-domain** self-supervised visual pretraining for imitation learning: given only your expert demonstrations, jointly learn a **latent inverse dynamics model** and a **latent forward dynamics model** over image embeddings, predicting the next frame *in latent space*. **No augmentations, no contrastive sampling, no ground-truth actions, no out-of-domain data.** Cui, Pan, Iyer, Haldar, [Pinto](lerrel-pinto.md) (NYU), NeurIPS 2024 ([paper](../sources/dynamo-paper.md)). **+39% overall** downstream policy performance over prior SSL and pretrained representations.

> [!note] A JEPA in everything but the label, published before the wiki's JEPA thread starts
> Latent next-frame prediction + an inverse-dynamics term + an explicit anti-collapse mechanism is the [JEPA](../concepts/world-models/jepa.md) recipe. DynaMo (Sept 2024) frames it as representation learning for imitation rather than as a world model, which is why the wiki filed the whole later literature without it. It also **predates [SMWM](smwm.md)**, which the wiki credits with introducing inverse-dynamics regularization as an anti-collapse mechanism in 2026 — DynaMo had inverse dynamics as *half the objective* two years earlier, though not as the *sole* collapse defence.

## Anti-collapse: two mechanisms, at the heavy end of the ladder

*"Naively, this objective admits a constant embedding solution."* DynaMo's answer:

1. **SimSiam-style stop-gradient** on the target embedding, `s*ₜ := sg(sₜ)` — an EMA momentum encoder is named as a compatible alternative.
2. **Covariance regularization**, λ = 0.04, following VICReg. Explicitly the *smaller* effect: it "slightly improves downstream task performance."

On the wiki's [anti-collapse design space](../concepts/world-models/jepa.md#common-training-challenges) that places DynaMo roughly where [PLDM](pldm.md) sits — stop-grad *plus* a variance-covariance term — and well above the single-regularizer approaches ([SIGReg](../concepts/world-models/sigreg.md), [SMWM](smwm.md)) that came later. **The ladder has been getting lighter; DynaMo is near its start.**

## Results

- **+39% overall**, concentrated on the harder **closed-loop** tasks (Block Pushing, Push-T) and on real robots.
- **Six environments**: Franka Kitchen, Block Pushing, Push-T, [LIBERO](libero.md) Goal (sim); **Allegro Manipulation** (Allegro Hand on a Franka, 23-D actions) and **xArm Kitchen** (goal-conditioned BAKU + [VQ-BeT](vq-bet.md) head) (real).
- **Policy-class agnostic** — gains hold across Behavior Transformer, [Diffusion Policy](diffusion-policy.md), MLP, and nearest neighbours.
- **Low-data**: real Allegro tasks trained from as few as **6 demonstrations**.
- Baselines: Random / ImageNet / R3M, VC-1, MVP, MAE, BYOL, MoCo, TCN. ResNet18 backbone (MAE-family baselines use ViT-B).

## The in-domain vs frozen-web axis

> [!warning] The same lab later published the opposite bet — and DynaMo is its baseline
> [Patch Policy](patch-policy.md) (2026, [Pinto](lerrel-pinto.md) again, with Cui as a co-author on both) freezes a **web-scale** encoder and consumes its **patch tokens**, and beats DynaMo decisively on the spatial tasks: DynaMo VQ-BeT **0.65 / 0.28** on BlockPush / Cube against WebSSL-patch VQ-BeT's **1.68 / 1.68**.
>
> That is a change of subject rather than a refutation. DynaMo answers *how to pretrain when all you have is in-domain demos*; Patch Policy answers *how to consume features you did not train*, in its own stated scope of in-domain tasks **with sufficient demonstrations**. **What nobody has tested is DynaMo's actual regime** — six demonstrations, no suitable web encoder — against a frozen web backbone. Reading Patch Policy's win as "in-domain pretraining is obsolete" outruns the evidence.

## Open questions

- **No frozen web-scale SSL baseline** — DINOv2 is not compared against in the DynaMo paper.
- **Architecture confound**: ResNet18 for DynaMo vs ViT-B for MAE-family baselines.
- **"+39%" is an aggregate** across six environments and several policy classes; per-task spread and trial counts are not recorded here, which the wiki's [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) standard would want.
- **Untested combined with a strong frozen backbone** — in-domain dynamics pretraining *on top of* DINOv2/WebSSL features is the obvious experiment neither paper runs.

## Related

- [Lerrel Pinto](lerrel-pinto.md) — senior author on this and [Patch Policy](patch-policy.md).
- [Patch Policy](patch-policy.md) / [WebSSL](webssl.md) — the out-of-domain frozen-feature bet that beats it in-distribution.
- [JEPA](../concepts/world-models/jepa.md) / [SIGReg](../concepts/world-models/sigreg.md) / [SMWM](smwm.md) / [PLDM](pldm.md) — the anti-collapse lineage it belongs to.
- [VQ-BeT](vq-bet.md) / [Diffusion Policy](diffusion-policy.md) — the policy heads.

## Mentioned in

- [DynaMo paper (Cui et al., NeurIPS 2024)](../sources/dynamo-paper.md) — the primary.
- [Patch Policy paper](../sources/patch-policy-paper.md) — DynaMo as the globally-pooled-feature baseline.
