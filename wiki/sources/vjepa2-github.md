---
title: V-JEPA 2 GitHub (facebookresearch/vjepa2)
type: source
url: https://github.com/facebookresearch/vjepa2
author: Meta FAIR
affiliations: Meta FAIR
published: Unknown
ingested: 2026-05-09
tags: [v-jepa-2, jepa, github, meta-fair, video, action-conditioned]
---

## Summary
Official GitHub repository for [V-JEPA 2](../entities/v-jepa-2.md). README confirms the full variant family (V-JEPA 2 / V-JEPA 2.1 / V-JEPA 2-AC), parameter ranges, benchmark numbers, V-JEPA 2.1 architectural additions, and licensing.

## Key claims

### Model variants
| Variant | ViT backbone | Resolution | Notes |
|---|---|---|---|
| V-JEPA 2 | ViT-L/H/g | 256–384px | Original pretraining |
| V-JEPA 2.1 | ViT-B through ViT-G | 384px | Dense features focus |
| V-JEPA 2-AC | — | — | Action-conditioned post-training |

**Parameter range across variants: 80M to 2B.**

### V-JEPA 2.1 architectural additions (vs V-JEPA 2)
- Dense predictive loss
- Deep self-supervision at multiple representation levels
- Multi-modal tokenizers

### Training pipeline
- Pretraining: masked latent feature prediction + cooldown phase on internet video.
- Action-conditioned post-training: robot trajectory data ([DROID](../entities/droid.md) — 62 hr Franka Panda teleop).
- Supports local + distributed SLURM training.

### Pretrained models
Available via PyTorch Hub and HuggingFace.

### Benchmark results
- **EK100**: 39.7% (prev. best 27.6%)
- **Something-Something v2**: 77.3% (prev. 69.7%)
- **Diving48**: 90.2% (prev. 86.4%)
- **Robot manipulation**: 100% reach success; 60–80% grasp / pick-and-place success

### License
Dual: **MIT** (majority of code) + **Apache 2.0** (specific utility modules).

## Entities mentioned
- [V-JEPA 2](../entities/v-jepa-2.md)
- [Meta FAIR](../entities/meta-fair.md)
- [DROID](../entities/droid.md)

## Open questions
- V-JEPA 2.1 multi-modal tokenizers: what modalities beyond video? (not specified in README)
- Exact boundary between MIT and Apache 2.0 coverage not stated.
