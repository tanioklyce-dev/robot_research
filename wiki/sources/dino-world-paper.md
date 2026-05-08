---
title: DINO-world Paper ("Back to the Features")
type: source
url: https://arxiv.org/abs/2507.19468
local_path: null
author: Federico Baldassarre, Marc Szafraniec, Basile Terver, Vasil Khalidov, Francisco Massa, Yann LeCun, Patrick Labatut, Maximilian Seitzer, Piotr Bojanowski
affiliations: FAIR at Meta (inferred — DINOv2 / DINO-world author overlap)
published: 2025-07-25
ingested: 2026-05-07
tags: [dino-world, dinov2, world-model, video-prediction, jepa-adjacent, fair, meta-fair]
---

## Summary
**"Back to the Features: DINO as a Foundation for Video World Models"** — FAIR paper (LeCun co-author, plus Bojanowski / Seitzer / Baldassarre from the DINOv2 line). Uses **DINOv2 latent features** as the substrate for video world models — JEPA-adjacent (predicts in latent space) but **not strictly JEPA** since the encoder is the frozen pretrained DINOv2 rather than co-trained with the predictor. Notable for being authored by **Basile Terver**, who is also lead author on [[jepa-wms-paper|JEPA-WMs]] five months later — suggesting the DINO-world → JEPA-WMs progression is one continuous research line.

## Key claims
- Frames world-modeling on top of pretrained DINOv2 features, "from driving and indoor scenes to simulated environments" (abstract — generic).
- Evaluated on **video prediction benchmarks: segmentation and depth forecasting** (per abstract).
- **Fine-tunable for action-conditioned planning via trajectory simulation** (per agent research; verify in body).
- DOI: https://doi.org/10.48550/arXiv.2507.19468

> [!note] Specific environments not named in abstract
> The abstract is generic about environments ("driving and indoor scenes to simulated environments"). Specific simulator/benchmark names need a paper-body read. The agent's research did not surface heavy-sim names (Isaac Lab, MuJoCo Playground, RoboCasa).

## Entities mentioned
- [[dino-world|DINO-world]] — model (entity created with this ingest).
- [[meta-fair|Meta FAIR]] — inferred affiliation.
- [[dino-wm|DINO-WM]] — design-space neighbor (both use DINOv2 features).
- [[dinov2|DINOv2]] — frozen feature substrate.
- [[yann-lecun|Yann LeCun]] — author.
- [[basile-terver|Basile Terver]] — third author; bridge to JEPA-WMs.

## Concepts touched
- [[jepa|Joint-Embedding Predictive Architecture]] — JEPA-adjacent (frozen encoder, latent prediction).
- [[world-model|World model]] — frozen-foundation-feature video world model.
- [[world-model-simulators|World-model simulators]] — latent-prediction paradigm.

## Open questions
- Specific simulator names — none surfaced from abstract.
- How fine-tuning for action-conditioned planning works — generic claim only.
- Code/project URL not provided in abstract page.
- Relationship to [[dino-wm|DINO-WM]]: both use DINOv2 features for world modeling; how do they differ in design and which set of authors is the "canonical" DINOv2-world-model line?

## Why this matters
**Lineage signal**: Basile Terver is on this paper (July 2025) and lead-authors [[jepa-wms-paper|JEPA-WMs]] (December 2025). DINO-world's "DINOv2 features → world model" approach evolves into JEPA-WMs' RoboCasa + DROID + Franka full-stack JEPA evaluation in five months. This is the bread-crumb trail of how the FAIR JEPA line moved from generic-video to robot-specific sim+real evaluation.
