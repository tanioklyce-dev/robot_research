---
title: DINOv2
type: entity
subtype: model
created: 2026-05-07
updated: 2026-09-03
sources: 23
tags: [dinov2, vision-foundation-model, self-supervised, vit, meta-fair, dino, frozen-encoder]
---

> [!note] The original [DINO](dino.md) is now on the wiki
> This page and [DINOv3](dinov3.md) are the *scaling* papers; **[DINO (Caron et al., ICCV 2021)](dino.md) is the one with the finding** — emergent object segmentation in `[CLS]` attention (Jaccard 45.9 vs supervised 27.3) and **k-NN classification at 78.3% with no head at all**. That second result is the original evidence for the frozen-encoder pattern this page's downstream users ([DINO-WM](dino-wm.md), [DINO-world](dino-world.md)) all depend on, and it emerges only with a ViT. Also worth carrying: how much of DINOv2's advantage is **LVD-142M** rather than the objective has never been separated in this wiki — the original reaches 80.1% ImageNet linear on IN1k alone with two 8-GPU servers.

**DINOv2 — "Learning Robust Visual Features without Supervision."** Self-supervised vision foundation model from [Meta FAIR](meta-fair.md), released 2023. Vision Transformer trained on 142M images with no labels via the DINO self-distillation objective; produces patch-level and image-level embeddings that transfer to downstream tasks **without fine-tuning** at near-supervised quality. arxiv 2304.07193. Code: https://github.com/facebookresearch/dinov2. Apache 2.0 for standard weights.

## Authors
Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy V. Vo, Marc Szafraniec, Vasil Khalidov, Patrick Labatut, Armand Joulin, Piotr Bojanowski. Companion paper on Vision Transformers at arxiv 2309.16588. **Notable overlap with [DINO-world](../sources/dino-world-paper.md) (2025)**: Szafraniec, Khalidov, Labatut, and Bojanowski all reappear there — DINOv2 → DINO-world is one continuous research thread.

## Architecture & training
- **ViT-S/14** (21M), **ViT-B/14** (86M), **ViT-L/14** (300M), **ViT-g/14** (1.1B). Patch size 14.
- Distilled and **register-equipped** variants available.
- **Self-supervised training** via the DINO approach — student/teacher self-distillation without negatives, no labels.
- **142M training images** (unlabeled).
- Strong **k-NN and linear-eval** performance on ImageNet without fine-tuning — i.e. the features themselves are useful, not just the model.

## Downstream use claimed in the README
- Image classification (k-NN, linear eval, logistic regression).
- Depth estimation (NYU, KITTI).
- Semantic segmentation (ADE20K, VOC2012).
- Zero-shot vision-language (`dino.txt` framework).
- Biomedical imaging (Cell-DINO, X-ray-DINO, with separate FAIR Noncommercial Research License).

## Why it matters in this wiki
DINOv2 is the **substrate** for an entire branch of the JEPA-adjacent world-model literature ingested here. Three sources use frozen DINOv2 features:

- **[DINO-WM](dino-wm.md)** ([paper](../sources/dino-wm-paper.md)) — DINOv2 patch features + learned predictor for zero-shot planning.
- **[DINO-world](dino-world.md)** ([paper](../sources/dino-world-paper.md)) — DINOv2 features for video world models. Title literally is *"Back to the Features: DINO as a Foundation for Video World Models."*
- **[JEPA-WMs](jepa-wms.md)** ([paper](../sources/jepa-wms-paper.md)) — likely uses DINOv2-feature predictor (DINO-world's design point evolves into JEPA-WMs); explicit framing in paper body should confirm.

This makes DINOv2 the most consequential **non-JEPA** building block in the JEPA-for-robotics line. The design choice of *frozen DINOv2 vs. end-to-end-trained encoder* is itself an axis of the [JEPA](../concepts/world-models/jepa.md) design space — see [LeWorldModel](leworldmodel.md) for the end-to-end alternative.

## Position vs other foundation models
- **Self-supervised, not supervised** — contrast with CLIP / SigLIP / EVA family (image-text-paired).
- **Patch-level features at quality** — most foundation models give a single image embedding; DINOv2 emphasizes spatially structured patch features that downstream world models can index.
- **Open weights, Apache 2.0** — downstream commercial use is unencumbered for the standard variants.

## Related
- [Meta FAIR](meta-fair.md) — origin lab.
- [Learned latent space](../concepts/world-models/latent-space.md) — DINOv2's 768-dim embedding is the substrate that downstream JEPA-adjacent models (DINO-WM / DINO-world / JEPA-WMs) freeze and predict in.
- [DINO-WM](dino-wm.md) / [DINO-world](dino-world.md) / [JEPA-WMs](jepa-wms.md) — primary downstream consumers in this wiki.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — JEPA family. DINOv2 is JEPA-adjacent (encoder trained without action-conditioning) but predates the action-conditioned JEPA-WM line.
- [LeWorldModel](leworldmodel.md) — end-to-end alternative to frozen-DINOv2 design.

## Successor: DINOv3
**[DINOv3](dinov3.md)** ([paper, August 2025](../sources/dinov3-paper.md)) is the architectural and training-recipe successor: 7B params, patch size 16, axial RoPE + box jittering, constant-schedule 1M-iteration training, and **Gram anchoring** (a new regularizer that finally fixes the long-training dense-feature degradation observed in DINOv2 at scales above ~300M params). DINOv3 is the natural drop-in upgrade for the JEPA-adjacent world-model line below.

## Mentioned in
- [DINOv2 Paper](../sources/dinov2-paper.md)
- [DINO paper (Caron et al., 2021)](../sources/dino-paper.md) — the original objective and the emergent properties DINOv2 scales
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [DINO-world Paper](../sources/dino-world-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [DINOv3 Paper](../sources/dinov3-paper.md) — establishes DINOv3 as DINOv2's successor and the new SSL state-of-the-art
- [DiT World-Action Model for AV Scene Prediction](../sources/dit-world-action-model-av-paper.md) — **best single-frame encoder** on a six-encoder nuScenes ego-action probe (steer RMSE 0.104), ahead of CLIP and supervised ViT-S/16, behind only V-JEPA2. Another datapoint that self-supervised features carry more geometric structure than language-aligned or label-supervised ones.

## Open questions / TBD
- The [DINOv2 Paper](../sources/dinov2-paper.md) (arxiv 2304.07193) is now filed (2026-05-16). LVD-142M curation pipeline details and self-distillation specifics remain open from the abstract-level ingest — methods section would close them.
- Cell/X-ray DINO variants (under FAIR Noncommercial Research License) not yet tracked.
