---
title: Siamese network
type: concept
created: 2026-05-14
updated: 2026-05-16
sources: 8
tags: [siamese, joint-embedding, weight-tying, ssl, foundational]
---

**Siamese network** — a neural network with **two (or more) sub-networks that share weights**, applied independently to two inputs, with a downstream head that operates on the two output embeddings (typically a similarity or distance). Introduced by **[Bromley, Guyon, LeCun, Säckinger, Shah 1993](../../sources/bromley1993-siamese-signature-verification.md)** for credit-card-tablet signature verification. The architectural ancestor of essentially every modern joint-embedding self-supervised learning system.

## Defining property

The two branches **share weights** — `f(x_1; θ)` and `f(x_2; θ)` use the same `θ`. The whole architecture is a single network, run twice. The output head consumes the two embeddings; it can be:

- A **cosine / distance head** (original Bromley et al. — `cos(z_1, z_2)` regressed onto `±1` targets).
- A **contrastive loss** (Hadsell 2006; FaceNet/triplet; SimCLR InfoNCE).
- A **redundancy-reduction loss** ([Barlow Twins](../../sources/barlow-twins-paper.md): cross-correlation → I).
- A **variance/covariance/invariance loss** ([VICReg](../../sources/vicreg-paper.md)).
- A **self-distillation head** (DINO / [DINOv2](../../entities/dinov2.md) / [DINOv3](../../entities/dinov3.md): EMA teacher).
- A **predictor head between embeddings** ([JEPA](jepa.md): joint-embedding *predictive* — the predictor `g(z_1, a)` predicts `z_2`).

## Why "Siamese"

Named in [Bromley et al. 1993](../../sources/bromley1993-siamese-signature-verification.md) after the topological resemblance to conjoined ("Siamese") twins — two identical bodies joined at the output. The two branches are not separate networks; they are literally the same network, evaluated on two inputs.

## Variants

- **Standard Siamese** — two weight-tied branches.
- **Asymmetric Siamese** — branches with shared backbone but **asymmetric heads** (e.g., BYOL's predictor on one side only; DINO's EMA teacher).
- **Triplet** — three branches: anchor, positive, negative (FaceNet 2015).
- **N-way** — generalizes to many branches simultaneously (SimCLR's 2N-sample batch).

## Why it matters in this wiki

Every joint-embedding line the wiki tracks — [Barlow Twins](../../sources/barlow-twins-paper.md), [VICReg](../../sources/vicreg-paper.md), [DINOv2](../../entities/dinov2.md), [DINOv3](../../entities/dinov3.md), [V-JEPA 2](../../entities/v-jepa-2.md), [DINO-WM](../../entities/dino-wm.md), [LeWM](../../entities/leworldmodel.md), [LeJEPA](../../sources/lejepa-paper.md), [PLDM](../../sources/pldm-paper.md) — is a Siamese-architecture descendant. The architectural commitment "compare two embeddings produced by the same encoder" is **continuous from 1993 to 2026**. Only the losses, the encoders (TDNN → CNN → ViT), and the data have changed.

## Failure mode: representation collapse

Without explicit negative targets or anti-collapse regularization, a Siamese network can satisfy any "make `z_1` similar to `z_2`" objective trivially by **collapsing the encoder to a constant**. The original Bromley et al. 1993 paper sidestepped this by **using labelled positive AND negative pairs** with explicit `±1` cosine targets. Modern self-supervised methods don't have negative labels and must prevent collapse via other mechanisms — every method in the [JEPA](jepa.md) and SSL lineage is, in part, an answer to "how do we make a Siamese network train without labels and without collapsing?".

See [Module 4](../../syntheses/curriculum/curriculum-04-self-supervised-learning.md) for the full anti-collapse taxonomy.

## Key references

- **[Bromley, Guyon, LeCun, Säckinger, Shah 1993](../../sources/bromley1993-siamese-signature-verification.md)** — original paper, eponymous source.
- **[Barlow Twins (Zbontar et al. 2021)](../../sources/barlow-twins-paper.md)** — non-asymmetric anti-collapse Siamese training.
- **[VICReg (Bardes, Ponce, LeCun 2022)](../../sources/vicreg-paper.md)** — variance + covariance + invariance variant; explicitly breaks the weight-tying requirement (branches can be different).
- **[LeCun 2022 — Path Towards AMI](../../sources/lecun2022-path-towards-ami.md)** — defines [JEPA](jepa.md) as the joint-embedding *predictive* architecture; adds a predictor between embeddings.
- **[Welch Labs — Yann LeCun's $1B Bet Against LLMs](../../sources/welchlabs-lecun-1b-bet-against-llms.md)** — popular explainer; the ~15-min mark walks the Siamese-network step en route to JEPA.

## Related concepts

- **[Joint-Embedding Predictive Architecture (JEPA)](jepa.md)** — the *predictive* extension; adds a predictor head between embeddings.
- **[Learned latent space](latent-space.md)** — Siamese networks define their similarity loss in this space.
- **Contrastive learning** — historically the dominant Siamese training paradigm (InfoNCE / SimCLR / MoCo); now superseded by anti-collapse regularization (LeCun 2022's "regularized SSL" framing).

## Current state

Siamese architectures are the **default backbone for self-supervised vision foundation models** in 2026:

- **[DINOv3](../../entities/dinov3.md)** (7B parameter ViT) — Siamese with EMA teacher + Gram anchoring.
- **[V-JEPA 2](../../entities/v-jepa-2.md) / [LeWM](../../entities/leworldmodel.md)** — Siamese-with-predictor (JEPA).
- **CLIP / SigLIP** — Siamese-shaped cross-modal: image-encoder vs text-encoder.

The **research frontier** is the predictor extension (JEPA) and removing the need for asymmetric tricks (LeJEPA / LeWM's SIGReg replaces EMA + stop-gradient + multi-fix with a single regularizer with proofs). The architecture itself — two weight-tied encoders + a head — is unchanged from 1993.

## Mentioned in
- [Bromley et al. 1993 — Signature Verification using a Siamese TDNN](../../sources/bromley1993-siamese-signature-verification.md)
- [Barlow Twins Paper](../../sources/barlow-twins-paper.md)
- [VICReg Paper](../../sources/vicreg-paper.md)
- [LeCun 2022 — Path Towards AMI](../../sources/lecun2022-path-towards-ami.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](../../sources/welchlabs-lecun-1b-bet-against-llms.md)
- [Onchain AI Garage — LeWM reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md)
- [JEPA concept page](jepa.md)
- [Curriculum Module 4 — Self-supervised learning](../../syntheses/curriculum/curriculum-04-self-supervised-learning.md)
- [Curriculum Module 11 — JEPA in depth](../../syntheses/curriculum/curriculum-11-jepa-deep.md)
