---
title: V-JEPA 2
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [v-jepa-2, jepa, world-model, meta-fair, video, action-conditioned, franka]
---

[[meta-fair|Meta FAIR]]'s flagship JEPA-style world model (June 2025). Two stages: **V-JEPA 2** (1B-param ViT-g video encoder pretrained on 1M+ hours of internet video) and **V-JEPA 2-AC** (300M-param action-conditioned predictor post-trained on 62 hr of Droid robot data). Notable for **zero-shot pick-and-place on Franka arms in new labs** via image-goal MPC. **Successor: [[v-jepa-2-1-paper|V-JEPA 2.1]]** (March 2026) — same FAIR group, "dense features" focus, +20pt real-Franka grasping per secondary research.

## Architecture
- **V-JEPA 2 encoder**: ViT-g, 1B parameters. Pretrained with visual mask denoising in representation space (not pixel space). EMA target encoder, L1 loss. 22M videos, 1M+ hours, 3D-RoPE positions, progressive resolution.
- **V-JEPA 2-AC predictor**: 300M-param transformer with block-causal attention. Frozen V-JEPA 2 encoder. Autoregressively predicts the representation of the next video frame from past frames + actions + end-effector states.

## Headline results
- **Robot manipulation**: zero-shot on Franka arms in two different labs; image-goal pick-and-place via MPC. No data, training, or rewards from those robots.
- Motion understanding: 77.3 top-1 on SSv2.
- Action anticipation: 39.7 R@5 on Epic-Kitchens-100 (SOTA, surpassing prior task-specific models).
- LLM-aligned VQA: 84.0 PerceptionTest, 76.9 TempCompass at 8B-parameter scale.

## Why it matters
First public demonstration of a **latent-prediction world model** ([[jepa|JEPA]]) doing zero-shot real-robot manipulation in untouched labs. Validates the JEPA thesis: predict in representation space, not pixel space, and you can scale to internet-video pretraining without paying the cost of generating video. Sits in **paradigmatic contrast** to [[nvidia-cosmos|NVIDIA Cosmos]] / [[genie-envisioner|Genie Envisioner]] (generative-video world models).

## Related
- [[meta-fair|Meta FAIR]] — primary lab.
- [[mila|Mila]] — co-affiliation (Artem Zholus dual appointment).
- [[jepa|Joint-Embedding Predictive Architecture]] — architecture family.
- [[world-model-simulators|World-model simulators]] — broader paradigm.
- [[leworldmodel|LeWorldModel]] — sibling JEPA architecture (different group).
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]] — direct successor (March 2026), dense features focus.
- [[jepa-wms|JEPA-WMs]] — same FAIR group's robot-specific JEPA work, but with sim (Dec 2025).

## Mentioned in
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]
