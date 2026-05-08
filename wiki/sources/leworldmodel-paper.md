---
title: LeWorldModel Paper
type: source
url: https://arxiv.org/abs/2603.19312
local_path: raw/LeWorldMode_2603.19312v2.pdf
author: Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
affiliations: Mila / Université de Montréal, NYU, Samsung SAIL, Brown
published: 2026-03-24
ingested: 2026-05-07
code: https://github.com/lucas-maes/le-wm
project_page: https://le-wm.github.io/
tags: [leworldmodel, lewm, jepa, world-model, end-to-end, sigreg, mila]
---

## Summary
Preprint introducing **LeWorldModel (LeWM)** — claimed as the **first JEPA trainable stably end-to-end from raw pixels with only two loss terms**. From researchers at [[mila|Mila]] / Université de Montréal, NYU, Samsung SAIL, and Brown. Senior author Yann LeCun. Emphasis on simplicity, hyperparameter parsimony, and planning speed.

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
- [[leworldmodel|LeWorldModel]]
- [[mila|Mila]]
- [[yann-lecun|Yann LeCun]] — senior author.
- [[pusht|PushT]] — one of four task datasets.
- [[dino-wm|DINO-WM]] — comparison baseline (foundation-based JEPA).

## Concepts touched
- [[jepa|Joint-Embedding Predictive Architecture]]
- [[world-model|World model]] — end-to-end-pixel-trained design point.
- [[world-model-simulators|World-model simulators]] — latent-prediction paradigm

## Open questions
- Does LeWM scale to high-resolution real-robot deployment, or is "2D and 3D control" still a research bench?
- How does SIGReg compare to other anti-collapse mechanisms (VICReg, BarlowTwins) at scale?

## Code & artifacts
- Official repo: https://github.com/lucas-maes/le-wm
- Project page: https://le-wm.github.io/
- Pretrained HF checkpoints: `quentinll/lewm-{pusht,cube,tworooms,reacher}`
- See [[leworldmodel-howto|LeWorldModel — train and run howto]] for install/train/eval commands.
