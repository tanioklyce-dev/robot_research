---
source_url: https://github.com/lucas-maes/le-wm
collected: 2026-05-09
published: Unknown
author: Lucas Maes
affiliation: Mila
---

# le-wm GitHub README

LeWorldModel (LeWM) is a Joint Embedding Predictive Architecture for learning world models from raw pixels. "The first JEPA that trains stably end-to-end from raw pixels using only two loss terms."

## Key claims
- Reduces tunable hyperparameters from six to one compared to alternatives (PLDM)
- ~15M parameters, trainable on a single GPU in hours
- Plans "up to 48× faster than foundation-model-based world models"
- Latent space encodes meaningful physical structure detectable through probing

## Installation
Uses `uv` for dependency management:
```
uv venv --python=3.10
source .venv/bin/activate
uv pip install stable-worldmodel[train,env]
```

## Data & training
- Datasets in HDF5 format downloaded from HuggingFace
- Training configured via Hydra config files under `config/train/`
- Checkpoints saved to `$STABLEWM_HOME` (defaults to `~/.stable-wm/`)
- Launch: `python train.py data=pusht`

## Core architecture components (jepa.py)
- Vision Transformer (ViT) encoder
- AR Predictor for next-embedding prediction
- Action encoder and projector MLPs
- Gaussian regularizer (SIGReg) for latent embeddings

## Evaluation & checkpoints
- Evaluation via `eval.py` using configs under `config/eval/`
- Pretrained checkpoints on HuggingFace Hub for: pusht, cube, tworooms, reacher
- Baseline models (PLDM, LeJEPA, IVL, IQL, GCBC, DINO-WM) on Google Drive

## License
MIT

## Contact
Lucas Maes (lucas.maes@mila.quebec)
