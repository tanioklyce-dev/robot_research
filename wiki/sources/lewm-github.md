---
title: LeWorldModel GitHub (lucas-maes/le-wm)
type: source
url: https://github.com/lucas-maes/le-wm
author: Lucas Maes
affiliations: Mila
published: Unknown
ingested: 2026-05-09
tags: [leworldmodel, lewm, jepa, github, mila, sigreg]
---

## Summary
Official GitHub repository for [LeWorldModel](../entities/leworldmodel.md). README confirms architectural details, training workflow, environment coverage, baseline comparisons, and licensing not previously in the wiki.

## Key claims

### Architecture (from `jepa.py`)
Four components:
1. **Vision Transformer (ViT) encoder** — maps raw pixel frames to latent `z`.
2. **AR Predictor** — autoregressively predicts next-step latent embedding.
3. **Action encoder + projector MLPs** — encode discrete/continuous actions into the predictor's input space.
4. **Gaussian regularizer (SIGReg)** — enforces isotropic Gaussian latents; the single hyperparameter.

### Training workflow
- Dependency management via `uv` (not pip/conda).
- `uv pip install stable-worldmodel[train,env]` — the `stable-worldmodel` package provides env zoo + training API.
- Datasets in HDF5 from HuggingFace; training config via Hydra under `config/train/`.
- Launch: `python train.py data=pusht`.
- Checkpoints to `$STABLEWM_HOME` (default `~/.stable-wm/`).

### Pretrained checkpoints (HuggingFace)
`quentinll/lewm-{pusht,cube,tworooms,reacher}` — four environments.

### Baseline models (Google Drive)
PLDM, LeJEPA, IVL, IQL, GCBC, [DINO-WM](../entities/dino-wm.md) — comparisons in the paper.

### License
MIT.

### Contact
Lucas Maes — lucas.maes@mila.quebec

## Entities mentioned
- [LeWorldModel](../entities/leworldmodel.md)
- [Mila](../entities/mila.md)
- [DINO-WM](../entities/dino-wm.md) (baseline)

## Open questions
- LeJEPA and IVL are named baselines not yet in the wiki — primary-source ingests would clarify the comparison landscape.
- `stable-pretraining` package (also in the stack) not documented here.
