---
title: LeWorldModel
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-15
sources: 21
tags: [leworldmodel, lewm, jepa, world-model, mila, end-to-end, sigreg]
---

LeWorldModel (LeWM) — a JEPA-style world model from [Mila](mila.md), NYU, Samsung SAIL, and Brown, presented as the **first JEPA trainable stably end-to-end from raw pixels** without the typical battery of training heuristics (stop-gradient, EMA, frozen encoder). Senior author: Yann LeCun (March 2026).

## Approach
- **Two loss terms only**:
  1. Next-embedding prediction (MSE) — encoder + predictor jointly trained.
  2. **SIGReg** — projects latent embeddings onto random univariate directions; runs a normality test on each; aggregates statistics to enforce isotropic Gaussian latents. Provides provable anti-collapse.
- Reduces tunable loss hyperparameters from **6 to 1** vs. PLDM (the prior end-to-end JEPA baseline).
- **15M parameters**; single GPU; hours of training.

## Architecture components (from GitHub `jepa.py`)
Four modules ([le-wm GitHub](../sources/lewm-github.md)):
1. **ViT encoder** — raw pixel frames → latent `z`
2. **AR Predictor** — autoregressively predicts next-step latent
3. **Action encoder + projector MLPs** — encode actions into predictor input space
4. **Gaussian regularizer (SIGReg)** — enforces isotropic Gaussian latents; the single hyperparameter

## Baselines compared against
PLDM, LeJEPA, IVL, IQL, GCBC, [DINO-WM](dino-wm.md) — checkpoints on Google Drive.

## License
MIT.

## Headline claims
- **Plans up to 48× faster** than foundation-model-based world models (e.g. DINO-WM).
- Competitive across diverse 2D and 3D control tasks.
- Latent space probing reveals **encoded physical structure**.
- Surprise scores reliably detect physically implausible events.
- Reconstruction-free, reward-free, task-agnostic, pixel-based.

## Why it matters
- Strips JEPA training down to two losses, making latent-prediction world models more practical for resource-limited research.
- Provides a single-GPU baseline that's hard to argue against — research labs without massive compute can do JEPA work.
- Different point in design space from [V-JEPA 2](v-jepa-2.md): smaller, simpler, end-to-end pixel-trained, vs. V-JEPA 2's massive video pretraining + frozen-encoder post-training.

## Related
- [Mila](mila.md) — primary affiliation.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — architecture family.
- [Learned latent space](../concepts/world-models/latent-space.md) — LeWM is the first JEPA to learn its latent space *end-to-end from raw pixels* (no frozen DINOv2); SIGReg is the anti-collapse mechanism.
- [V-JEPA 2](v-jepa-2.md) — sibling JEPA model from a different group.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — broader paradigm.

## Code
- Official repo: https://github.com/lucas-maes/le-wm (built on `stable-worldmodel` + `stable-pretraining`)
- Pretrained HF checkpoints: `quentinll/lewm-{pusht,cube,tworooms,reacher}`
- See [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md) for the practical recipe.

## Mentioned in
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md)
- [le-wm GitHub](../sources/lewm-github.md)
- [MLWorks — Navigate the World from Raw Pixels](../sources/medium-lewm-navigate-world.md)
- [Towards Deep Learning — This World Model Learns Physics by Watching Videos](../sources/towardsdeeplearning-world-model-physics.md)
