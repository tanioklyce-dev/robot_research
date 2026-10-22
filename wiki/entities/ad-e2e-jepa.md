---
title: AD-E2E-JEPA
type: entity
subtype: model
created: 2026-10-22
updated: 2026-10-22
sources: 1
tags: [ad-e2e-jepa, jepa, autonomous-driving, navsim, dinov3, sigreg, leworldmodel, dino-wm, jepa-wms, lecun, choromanska]
---

# AD-E2E-JEPA

**AD-E2E-JEPA** is an action-conditioned [JEPA](../concepts/world-models/jepa.md) world model for end-to-end autonomous driving. It plans by rolling out candidate trajectories in latent space, with no trained driving policy. A small learned compressor sits on a **frozen DINOv3** encoder, with [SIGReg](../concepts/world-models/sigreg.md) applied per patch and a stop-gradient. It cuts tokens 16× and width 4×. Zhu, Zhang, [LeCun](yann-lecun.md), [Choromanska](anna-choromanska.md) (NYU), arXiv 2609.34085, September 2026 ([paper](../sources/ad-e2e-jepa-autonomous-driving-paper.md)).

## Results
- It is the first head-to-head of [LeWM](leworldmodel.md), [DINO-WM](dino-wm.md) and [JEPA-WMs](jepa-wms.md) on driving (NAVSIM v2, front camera, goal = the real frame 4 s ahead). On a 100-scene subset: LeWM **48.3 EPDMS at 0.7 s per scene**, DINO-WM 68.3 at 91.8 s, JEPA-WM 74.2 at 101 s, AD-E2E-JEPA **76.6 at 0.8 s**.
- Full 12,146-scene test set: **67.3 EPDMS** (72.9 with 8,192 candidates), against LeWM's 39.8.
- The pretrained compressor lifts an imitation-learning planner from 80.2 to 85.4 EPDMS.

## Caveats
NAVSIM scores plans against replayed traffic, so nothing is driven closed-loop. A future-frame goal makes the task close to an inverse problem, so scores are not comparable with driving policies. There is one seed. The LeWM baseline is a ViT-L at batch size 8, not the published recipe. Code is public; no weights.

## Why it matters here
It is the only paper in the [autumn collapse batch](../syntheses/world-models/jepa-dynamics-collapse-fixes.md) on scene-diverse real video. There LeWM, the one model that trains its own encoder, has plans that barely depend on the action, which is consistent with [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md). AD-E2E-JEPA sidesteps the problem with the **frozen-encoder** route. That is the same split described in [Three ways to scale a JEPA world model](../syntheses/world-models/three-ways-to-scale-a-jepa-world-model.md#the-encoder-split-and-the-collapse-each-side-hits).

## Mentioned in
- [AD-E2E-JEPA paper](../sources/ad-e2e-jepa-autonomous-driving-paper.md)
- Synthesis: [What the latent throws away](../syntheses/world-models/jepa-dynamics-collapse-fixes.md)
