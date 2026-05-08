---
title: V-JEPA 2 Paper
type: source
url: https://arxiv.org/abs/2506.09985
local_path: raw/JEPA_2506.09985v1.pdf
author: Mahmoud Assran, Adrien Bardes, David Fan, Quentin Garrido, ..., Yann LeCun, Michael Rabbat, Nicolas Ballas
affiliations: FAIR at Meta, Mila — Quebec AI Institute / Polytechnique Montréal
published: 2025-06-13
ingested: 2026-05-07
tags: [v-jepa, jepa, world-model, meta-fair, self-supervised, video, droid, franka]
---

## Summary
Two-stage self-supervised world-model paper from [[meta-fair|FAIR at Meta]] (with [[mila|Mila]] collaborators). **V-JEPA 2** is a 1B-parameter ViT-g video encoder pretrained with mask denoising on 1M+ hours of internet video. **V-JEPA 2-AC** is a 300M-parameter action-conditioned predictor post-trained on just 62 hours of unlabeled robot videos from the [[droid|DROID]] dataset. Demonstrates **zero-shot deployment on Franka arms in two new labs** for prehensile pick-and-place via image-goal planning (model predictive control), with no robot-specific data, training, or rewards.

## Key claims
- **V-JEPA 2 pretraining**: 22M videos, 1M+ hours; ViT-L → ViT-g (300M → 1B parameters); warmup-constant-decay schedule; 252K iterations; progressive resolution.
- Self-supervised objective: visual mask denoising in *representation space* (not pixel space) with EMA-encoder targets and L1 regression loss.
- 3D-RoPE position embeddings (over 1D RoPE) helps stabilize training of largest models.
- **V-JEPA 2-AC**: 300M-param transformer with **block-causal attention**; autoregressively predicts representation of next video frame conditioned on action and previous states. Frozen V-JEPA 2 encoder.
- Trained on 62 hours of unlabeled [[droid|DROID]] robot interaction data.
- **Robot deployment**: zero-shot on Franka arms in two different labs; image-goal pick-and-place via MPC. **No data collected from those robots, no task-specific training, no rewards.**
- **Understanding**: 77.3 top-1 accuracy on Something-Something v2 (motion); SOTA on Epic-Kitchens-100 anticipation (39.7 R@5).
- **Aligned with LLM**: 84.0 PerceptionTest, 76.9 TempCompass at 8B-parameter scale.
- Code: https://github.com/facebookresearch/vjepa2
- Blog: https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks
- DOI: https://doi.org/10.48550/arXiv.2506.09985

## Entities mentioned
- [[v-jepa-2|V-JEPA 2]]
- [[meta-fair|Meta FAIR]]
- [[mila|Mila]]
- [[droid|DROID]] — post-training data source (62 hr subset).

## Concepts touched
- [[jepa|Joint-Embedding Predictive Architecture]]
- [[world-model-simulators|World-model simulators]] — latent-prediction paradigm (vs. video generation)
- [[sim-to-real-transfer|Sim-to-real transfer]] — zero-shot to new robot environments

## Open questions
- How does V-JEPA 2-AC compare to [[nvidia-cosmos|NVIDIA Cosmos]] / [[genie-envisioner|Genie Envisioner]] on robot tasks where the latter would generate video rollouts?
- Exact Franka task success rate? Abstract claims "enable picking and placing" but precise numbers need the paper body.
- 62 hours of [[droid|DROID]] is small — existence proof or production-ready?
