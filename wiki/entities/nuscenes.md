---
title: nuScenes
type: entity
subtype: dataset
created: 2026-09-01
updated: 2026-09-01
sources: 2
tags: [nuscenes, dataset, autonomous-driving, benchmark, motional, can-bus, multimodal]
---

**nuScenes** — a multimodal autonomous-driving dataset (Caesar et al., CVPR 2020), and the default public benchmark for driving perception, prediction, and planning. Used in this wiki both as a **world-model training set** and as a **planning benchmark**.

## Composition

Per the [DiT world-action model paper](../sources/dit-world-action-model-av-paper.md), which uses `v1.0-trainval`:

- **850 scenes** of roughly 20 s each, **33,552 keyframes** total.
- **2 Hz keyframe rate** — coarse by robot-control standards, and a real constraint on what temporal dynamics a model trained on it can express.
- Collected in **Boston and Singapore**, giving left- and right-hand traffic and distinct urban conditions.
- **Synchronized camera and CAN-bus data** — the CAN bus supplies logged ego-actions (steering angle, acceleration), which is what makes nuScenes usable for *action-conditioned* world modeling rather than passive video prediction.

Scene-level splitting matters here: the DiT paper partitions **630 / 70 / 150** by scene, because windows within a scene overlap and a frame-level split would leak.

## Use in this wiki

| Source | Role of nuScenes |
|---|---|
| [DiT World-Action Model for AV Scene Prediction](../sources/dit-world-action-model-av-paper.md) | Training + evaluation set for a compact action-conditioned [world-action model](../concepts/world-models/world-action-model.md); also the substrate for its six-encoder benchmark (ego-action regression from frozen features) |
| [VQ-BeT](../sources/vq-bet-paper.md) | One of eight benchmark environments — as a **planning** benchmark scored by average L2 (m) and collision rate. VQ-BeT reports 0.73 m / 0.29%, best L2 among compared methods |

Note the two use it for different things: one predicts **future scenes** conditioned on actions, the other predicts **actions**. That nuScenes supports both directions on the same data is precisely the [world-action model](../concepts/world-models/world-action-model.md) framing — forward dynamics and policy over one stream.

## Mentioned in
- [Sharifullin, Jiang & Chew 2026 — Diffusion Transformer World-Action Model for AV Scene Prediction](../sources/dit-world-action-model-av-paper.md)
- [VQ-BeT](../sources/vq-bet-paper.md)
