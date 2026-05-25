---
title: V-JEPA 2
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-25
sources: 16
tags: [v-jepa-2, jepa, world-model, meta-fair, video, action-conditioned, franka]
---

[Meta FAIR](meta-fair.md)'s flagship JEPA-style world model (June 2025). Two stages: **V-JEPA 2** (1B-param ViT-g video encoder pretrained on 1M+ hours of internet video) and **V-JEPA 2-AC** (300M-param action-conditioned predictor post-trained on 62 hr of Droid robot data). Notable for **zero-shot pick-and-place on Franka arms in new labs** via image-goal MPC. **Successor: [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md)** (March 2026) — same FAIR group, "dense features" focus, +20pt real-Franka grasping per secondary research.

## Variant family ([V-JEPA 2 GitHub](../sources/vjepa2-github.md))

| Variant | ViT backbone | Resolution | Notes |
|---|---|---|---|
| V-JEPA 2 | ViT-L/H/g | 256–384px | Original video pretraining |
| V-JEPA 2.1 | ViT-B through ViT-G | 384px | Dense features; adds dense predictive loss + deep self-supervision + multi-modal tokenizers |
| V-JEPA 2-AC | — | — | Action-conditioned post-training on top of V-JEPA 2 |

**Parameter range across variants: 80M to 2B.** Pretrained checkpoints on PyTorch Hub and HuggingFace. License: MIT (majority) + Apache 2.0 (utility modules).

## Architecture
- **V-JEPA 2 encoder**: ViT-g, 1B parameters. Pretrained with visual mask denoising in representation space (not pixel space). EMA target encoder, L1 loss. 22M videos, 1M+ hours, 3D-RoPE positions, progressive resolution.
- **V-JEPA 2-AC predictor**: 300M-param transformer with block-causal attention. Frozen V-JEPA 2 encoder. Autoregressively predicts the representation of the next video frame from past frames + actions + end-effector states.

## Headline results
- **Robot manipulation**: zero-shot on Franka arms in two different labs; image-goal pick-and-place via MPC. No data, training, or rewards from those robots.
- Motion understanding: 77.3 top-1 on SSv2.
- Action anticipation: 39.7 R@5 on Epic-Kitchens-100 (SOTA, surpassing prior task-specific models).
- LLM-aligned VQA: 84.0 PerceptionTest, 76.9 TempCompass at 8B-parameter scale.

## Why it matters
First public demonstration of a **latent-prediction world model** ([JEPA](../concepts/world-models/jepa.md)) doing zero-shot real-robot manipulation in untouched labs. Validates the JEPA thesis: predict in representation space, not pixel space, and you can scale to internet-video pretraining without paying the cost of generating video. Sits in **paradigmatic contrast** to [NVIDIA Cosmos](nvidia-cosmos.md) / [Genie Envisioner](genie-envisioner.md) (generative-video world models).

> [!note] V-JEPA-2-AC beaten by FAIR's own JEPA-WMs recipe
> The same FAIR group's **[JEPA-WMs (Terver et al., TMLR 05/2026)](../sources/jepa-wms-paper.md)** beats V-JEPA-2-AC on every env where both were evaluated — **Rc-R 25.4 vs 16.2, Rc-Pl 30.7 vs 33.1 (tie), DROID 48.2 vs 42.9**. The JEPA-WMs ablation also surfaces a structural reason: **DINO encoders outperform V-JEPA encoders** as the frozen backbone for control, because DINO's fine object segmentation translates object motion into localized sparse token changes the predictor can learn efficiently. V-JEPA's coarser segmentation spreads object information across overlapping tokens. The JEPA-WMs numbers come from a retraining with a "rollout-loss bug fix" the authors document in §C of the paper.

## Related
- [Meta FAIR](meta-fair.md) — primary lab.
- [Mila](mila.md) — co-affiliation (Artem Zholus dual appointment).
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — architecture family.
- [Learned latent space](../concepts/world-models/latent-space.md) — V-JEPA 2 trains its latent on 1M+ hours of internet video before action-conditioned post-training; canonical example of broad-pretraining → small-action-dataset.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — broader paradigm.
- [LeWorldModel](leworldmodel.md) — sibling JEPA architecture (different group).
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md) — direct successor (March 2026), dense features focus.
- [JEPA-WMs](jepa-wms.md) — same FAIR group's robot-specific JEPA work, but with sim (Dec 2025).

## Mentioned in
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md)
- [V-JEPA 2 GitHub](../sources/vjepa2-github.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md) — direct successor / same FAIR group
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md) — comparator
- [Towards AI — LeCun / AMI Labs](../sources/towardsai-lecun-ami-labs.md) — secondary journalism
