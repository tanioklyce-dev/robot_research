---
title: LeWorldModel Paper
type: source
url: https://arxiv.org/abs/2603.19312
local_path: raw/LeWorldMode_2603.19312v2.pdf
sha256: 58dd56c906a98b9871dbbf6c7f7aa6954da1ee923fe5f17f584c6e22d953433a
author: Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
affiliations: Mila / Université de Montréal, NYU, Samsung SAIL, Brown
published: 2026-03-24
ingested: 2026-05-07
code: https://github.com/lucas-maes/le-wm
project_page: https://le-wm.github.io/
tags: [leworldmodel, lewm, jepa, world-model, end-to-end, sigreg, mila]
---

> [!note] Verified 2026-09-07: LeWM trains with **no data augmentation at all**
> Checked against the paper, Appendix D, and the [`le-wm`](https://github.com/lucas-maes/le-wm) configs and source, because [the abstraction-tax synthesis](../syntheses/world-models/abstraction-tax.md) depends on it. **"augment", "crop", "jitter", "flip" and "blur" appear zero times in the paper**; every occurrence of *color* is the violation-of-expectation perturbation being tested, not a training transform. The whole image pipeline is `ToImage(imagenet_stats) + Resize(224)` plus z-score normalization of action/proprio/state — deterministic, no stochastic augmentation.
>
> **LeWM takes SIGReg from [LeJEPA](lejepa-paper.md) but not its multi-view invariance loss.** The positive pair is **(frame *t*, frame *t+1*)** — temporal adjacency is the invariance signal, not two augmented views of one frame.
>
> Why it matters: an objective built on next-frame prediction is **rewarded for encoding static scene attributes**, since the agent's colour, size and shape are the most predictable features in any trajectory. That is a mechanism for [stable-worldmodel](stable-worldmodel-paper.md)'s **50.8% → 6–26%** collapse under colour/size/shape shift, and it should apply equally to [DINO-WM](dino-wm-paper.md) and [PLDM](pldm-paper.md).

## Summary
Preprint introducing **LeWorldModel (LeWM)** — claimed as the **first JEPA trainable stably end-to-end from raw pixels with only two loss terms**. From researchers at [Mila](../entities/mila.md) / Université de Montréal, NYU, Samsung SAIL, and Brown. Senior author Yann LeCun. Emphasis on simplicity, hyperparameter parsimony, and planning speed.

## Key claims
- Two-loss design: (a) next-embedding MSE prediction; (b) **SIGReg** — projects latent embeddings onto random univariate directions and runs a normality test, encouraging an isotropic Gaussian latent distribution and provable anti-collapse.
- **Reduces tunable loss hyperparameters from 6 to 1** vs. existing end-to-end JEPAs (specifically PLDM).
- **15M parameters**; trains on a **single GPU** in hours.
- **Plans up to 48× faster** than foundation-model-based world models.
- No stop-gradient, no exponential moving average (EMA), no pre-trained encoder, no image reconstruction, no reward signal.
- Competitive across diverse 2D and 3D control tasks.
- Latent space probing reveals **encoded physical structure**.
- **Surprise evaluation** confirms the model detects physically implausible events.
- Compared against PLDM (end-to-end), DINO-WM (foundation-based), Dreamer (task-specific reward), TD-MPC (state-based).
- DOI: https://doi.org/10.48550/arXiv.2603.19312

## Entities mentioned
- [LeWorldModel](../entities/leworldmodel.md)
- [Mila](../entities/mila.md)
- [Yann LeCun](../entities/yann-lecun.md) — senior author.
- [PushT](../entities/pusht.md) — one of four task datasets.
- [DINO-WM](../entities/dino-wm.md) — comparison baseline (foundation-based JEPA).

## Concepts touched
- [Optimal control](../concepts/robotics/optimal-control.md)
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md)
- [World model](../concepts/world-models/world-model.md) — end-to-end-pixel-trained design point.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — latent-prediction paradigm
- [Learned latent space](../concepts/world-models/latent-space.md) — first stable end-to-end-from-pixels JEPA latent; SIGReg is the anti-collapse mechanism that makes it work.
- [SIGReg](../concepts/world-models/sigreg.md) — SIGReg as LeWM’s sole anti-collapse term.

## Open questions
- Does LeWM scale to high-resolution real-robot deployment, or is "2D and 3D control" still a research bench?
- How does SIGReg compare to other anti-collapse mechanisms (VICReg, BarlowTwins) at scale?

## Code & artifacts
- Official repo: https://github.com/lucas-maes/le-wm
- Project page: https://le-wm.github.io/
- Pretrained HF checkpoints: `quentinll/lewm-{pusht,cube,tworooms,reacher}`
- See [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md) for install/train/eval commands.
