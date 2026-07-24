---
title: Basile Terver
type: entity
subtype: person
created: 2026-05-07
updated: 2026-05-07
sources: 4
tags: [person, meta-fair, jepa-wms, dino-world, lineage]
---

**Basile Terver** — researcher associated with [Meta FAIR](meta-fair.md) (institutional affiliation inferred from co-author roster + paper namespace). **The bread-crumb author** between [DINO-world](../sources/dino-world-paper.md) (Jul 2025) and [JEPA-WMs](../sources/jepa-wms-paper.md) (Dec 2025) — the two papers that bracket the FAIR JEPA program's move from generic-video world models to robot-specific RoboCasa + DROID + real-Franka evaluation.

## Papers in this wiki
- [DINO-world](../sources/dino-world-paper.md) (2025-07) — **third author** (Baldassarre, Szafraniec, Terver, Khalidov, Massa, LeCun, Labatut, Seitzer, Bojanowski). DINOv2-feature-based video world model.
- [JEPA-WMs](../sources/jepa-wms-paper.md) (2025-12) — **first author** (Terver, Yang, Ponce, Bardes, LeCun). Investigates "what drives success in physical planning with JEPA-WMs"; first paper in this wiki to use [RoboCasa](robocasa.md) heavy sim alongside [DROID](droid.md) + real Franka.

## Why it matters in this wiki
Terver is the **single-author signal** that DINO-world → JEPA-WMs is one continuous research line, not coincidental shared FAIR institutional context. The progression:

- DINO-world (Jul 2025) — generic video, DINOv2 features → world model.
- JEPA-WMs (Dec 2025) — same DINOv2-foundation design point, now applied to robot-specific evaluation: RoboCasa kitchen manipulation + 42 Metaworld tasks + Push-T + DROID + real Franka.

Five months between the two; same lead-author trajectory; design space evolves from frozen-features-on-video to frozen-features-on-robot-data with planning evaluation. If a third Terver-led paper appears, it likely extends the JEPA-WMs setup further into heavier sim (Isaac Lab? MuJoCo Playground?) or higher-fidelity real-robot data.

## Status
- **Affiliation**: not stated on either arxiv abstract page; inferred FAIR from `facebookresearch/jepa-wms` repo namespace and DINO-world co-author roster (Baldassarre, Szafraniec, Khalidov, Labatut, Bojanowski are all FAIR / DINOv2 authors).
- **Career stage**: not stated. Lead-authoring a high-profile FAIR paper in Dec 2025 plus third-author on a DINO-world paper in Jul 2025 is consistent with a PhD student or early-career researcher embedded in the FAIR team — but this is inference, not citation.

## Related
- [Meta FAIR](meta-fair.md) — inferred affiliation.
- [DINO-world](dino-world.md) / [JEPA-WMs](jepa-wms.md) — papers.
- [Adrien Bardes](adrien-bardes.md) / [Yann LeCun](yann-lecun.md) — JEPA-WMs co-seniors.
- [DINOv2](dinov2.md) — common substrate across both papers.

## Mentioned in
- [DINO-world Paper](../sources/dino-world-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)

## Open questions / TBD
- Affiliation and career stage explicitly — paper-body verification.
- Personal page / Google Scholar / Twitter — if present, would clarify research thread before DINO-world.
- Future paper trajectory — is JEPA-WMs the start of a multi-paper line, or one-off?
