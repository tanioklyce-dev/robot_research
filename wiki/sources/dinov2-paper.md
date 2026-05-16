---
title: DINOv2 — Learning Robust Visual Features without Supervision (paper)
type: source
url: https://arxiv.org/abs/2304.07193
author: Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy V. Vo, Marc Szafraniec, Vasil Khalidov, et al. (26 authors, Meta FAIR)
published: 2023-04
ingested: 2026-05-16
tags: [dinov2, self-supervised, vision-foundation-model, vit, fair, ssl]
---

## Summary
The primary [DINOv2](../entities/dinov2.md) paper from [Meta FAIR](../entities/meta-fair.md), 26 authors. Establishes a vision foundation model trained **purely via self-supervision** on a custom curated 142M-image dataset (LVD-142M), producing patch- and image-level features that work across distributions and tasks **without fine-tuning** at near-supervised quality. Headline architectural choice: train a **ViT with 1B parameters** at scale, then **distill into smaller ViTs** for deployment. The distilled models surpass OpenCLIP — the prior best general-purpose visual feature — on most image- and pixel-level benchmarks. Foundational to subsequent DINO-line robotics work in this wiki: [DINO-WM](../entities/dino-wm.md), [DINO-world](../entities/dino-world.md), the [V-JEPA 2](../entities/v-jepa-2.md) encoder lineage, and [DINOv3](../entities/dinov3.md).

## Key claims

### Abstract (verbatim)
"The recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer vision. These models could greatly simplify the use of images in any system by producing all-purpose visual features, i.e., features that work across image distributions and tasks without finetuning. This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources. We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size. Most of the technical contributions aim at accelerating and stabilizing the training at scale. In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised literature. In terms of models, we train a ViT model (Dosovitskiy et al., 2020) with 1B parameters and distill it into a series of smaller models that surpass the best available all-purpose features, OpenCLIP (Ilharco et al., 2021) on most of the benchmarks at image and pixel levels."

### Design choices
- **Data**: LVD-142M — an automatic pipeline producing a "dedicated, diverse, and curated" image dataset, in deliberate contrast to the uncurated web crawls typical in prior SSL work.
- **Model**: ViT 1B parameters trained at scale, then distilled into smaller deployable models (the public release includes ViT-S/B/L/g per the entity-page lineage).
- **Training contributions**: "Most of the technical contributions aim at accelerating and stabilizing the training at scale" — practical engineering rather than a new conceptual objective. Builds on the DINO self-distillation framework.

### Headline benchmark claim
- Distilled DINOv2 surpasses **OpenCLIP** (Ilharco et al. 2021) on most benchmarks at **both image and pixel levels** — the latter being significant because OpenCLIP was image-level-trained.

### Notable author overlap with downstream papers
- **Szafraniec, Khalidov, Labatut, Bojanowski** all reappear on the [DINO-world paper](dino-world-paper.md) (2025) — DINOv2 → DINO-world is one continuous research thread.
- **Assran** (V-JEPA 2 senior author) is also on the DINOv2 paper, linking the DINO/JEPA threads at the author level.

## Entities mentioned
- [DINOv2](../entities/dinov2.md)
- [Meta FAIR](../entities/meta-fair.md)
- [DINO-WM](../entities/dino-wm.md), [DINO-world](../entities/dino-world.md), [DINOv3](../entities/dinov3.md) — downstream DINO-line.
- [V-JEPA 2](../entities/v-jepa-2.md) — JEPA line that shares Assran.

## Concepts touched
- [Siamese network](../concepts/world-models/siamese-network.md) — DINO/DINOv2 inherits the joint-embedding-with-self-distillation architecture descended from the Siamese lineage.
- [Latent space](../concepts/world-models/latent-space.md) — DINOv2 features are the canonical "frozen visual latent space" reused across the wiki's frozen-feature world-model and JEPA literature.

## Open questions
- LVD-142M composition (image sources, deduplication, curation thresholds) — abstract only mentions "automatic pipeline / diverse / curated." Worth pulling from §3 if dataset-curation methodology becomes load-bearing.
- Self-distillation specifics relative to original DINO (cluster centers, teacher EMA, etc.) not surfaced from abstract.
- License: arxiv standard non-exclusive; the public DINOv2 weights are Apache 2.0 per the entity page — confirm against the paper / GitHub release.
- No direct robotics/control claims in the abstract; the entity-page robotics usage (DINO-WM, V-JEPA-2 encoder) is downstream of this paper.
