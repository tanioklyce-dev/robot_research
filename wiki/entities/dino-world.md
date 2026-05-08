---
title: DINO-world
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [dino-world, dinov2, video-world-model, jepa-adjacent, fair, meta-fair, terver, baldassarre]
---

**DINO-world** ("Back to the Features: DINO as a Foundation for Video World Models") — [FAIR](meta-fair.md) paper introduced in [Baldassarre et al. (July 2025)](../sources/dino-world-paper.md). Uses **DINOv2 latent features** as the substrate for video world models. JEPA-adjacent (predicts in latent space) but **not strictly JEPA** since the DINOv2 encoder is frozen, not co-trained.

## Approach
- Frame world-modeling on top of pretrained DINOv2 features.
- Evaluated on video-prediction benchmarks (segmentation forecasting, depth forecasting per abstract).
- Fine-tunable for action-conditioned planning via trajectory simulation (per secondary research).

## Why it matters
- **Lineage signal.** Lead author trio includes Federico Baldassarre, Marc Szafraniec, **Basile Terver** — and Terver leads [JEPA-WMs (Dec 2025)](../sources/jepa-wms-paper.md) five months later. DINO-world → JEPA-WMs is one continuous research line at FAIR moving from generic-video to robot-specific evaluation.
- **Sibling to [DINO-WM](dino-wm.md).** Both build world models on top of frozen DINOv2 features but from different author groups (FAIR / NYU) and different focus (DINO-WM is robotics-first; DINO-world is video-first).

## Environments
Per the abstract, generic only — "driving and indoor scenes to simulated environments." No specific simulator names surfaced.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — JEPA-adjacent.
- [DINO-WM](dino-wm.md) — sibling DINOv2-feature world model.
- [V-JEPA 2](v-jepa-2.md) — full JEPA contrast (encoder co-trained).
- [Meta FAIR](meta-fair.md) — primary lab.
- [JEPA-WMs](../sources/jepa-wms-paper.md) — Terver-led successor.

## Mentioned in
- [DINO-world Paper](../sources/dino-world-paper.md)
