---
title: "Ultralytics YOLO Evolution: An Overview of YOLO26, YOLO11, YOLOv8 and YOLOv5 (Sapkota & Karkee 2025)"
type: source
url: https://arxiv.org/abs/2510.09653
local_path: raw/2510.09653.pdf
sha256: 9e4f6831b21af0c2f3df027f3c6510cb31f76070110fa7984a12ff81e9c5ab7c
author: Ranjan Sapkota, Manoj Karkee
published: 2026-03-16
ingested: 2026-07-23
venue: arXiv:2510.09653 (v1 2025-10-06, v3 2026-03-16)
tags: [object-detection, yolo, yolo26, survey, single-stage-detection, nms-free, edge-ai, deployment]
---

# Ultralytics YOLO Evolution: An Overview of YOLO26, YOLO11, YOLOv8 and YOLOv5

## Summary

The most current YOLO overview — anchored on **YOLO26**, the [Ultralytics](../entities/ultralytics-yolo.md) flagship — and read backward through the four releases that got there (YOLO26 ← YOLO11 ← YOLOv8 ← YOLOv5). Beyond architecture it is explicitly a **deployment** paper: export formats, quantization, and real-world use in robotics, agriculture, surveillance, and manufacturing, plus a benchmark table against contemporaries (YOLOv12/v13, RT-DETR, DEIM).

## Key claims

- **YOLO26's innovations** (the paper's headline list):
  - **DFL removal** — drops Distribution Focal Loss from the regression branch.
  - **Native NMS-free inference** — end-to-end detection with no NMS post-step (the [YOLOv10](yolov10-nms-free-2024.md) idea, now the default).
  - **ProgLoss (Progressive Loss Balancing)** — schedules the loss-term weights over training.
  - **STAL (Small-Target-Aware Label Assignment)** — assignment biased toward small objects, directly targeting YOLO's oldest weakness (v1's "flocks of birds").
  - **MuSGD optimizer** — a new optimizer for training stability.
- **Backward lineage.** YOLO11 (hybrid task assignment, efficiency modules) → YOLOv8 (decoupled head, anchor-free) → **YOLOv5 (the modular PyTorch foundation** that made the whole modern lineage tractable). This "v5 as foundation" framing matches the [Terven survey](terven-yolo-survey-2023.md)'s read.
- **Benchmarking.** Quantitative MS-COCO comparison of v5/v8/v11/26 with cross-comparisons to **YOLOv12, YOLOv13, [RT-DETR](../entities/rt-detr.md), and [DEIM](../entities/deim.md)** (DETR with Improved Matching), across precision, recall, F1, mAP, and inference speed — the accuracy/efficiency trade-off surface.
- **Deployment perspective.** Export formats, quantization strategies, and named application domains (**robotics**, agriculture, surveillance, manufacturing) — the practitioner's view this wiki's edge stack ([jetson-examples](../entities/jetson-examples.md), Hailo apps) actually consumes.
- **Open challenges named:** dense-scene limitations, **hybrid CNN-Transformer** integration, **open-vocabulary** detection, and **edge-aware training**.

## Entities mentioned

- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — YOLO26 is its current flagship; this source is the best single reference for what YOLO26 changed.
- [jetson-examples](../entities/jetson-examples.md) — the edge-deployment target for these models.

## Concepts touched

- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md) — YOLO26 as the current state of the anchor-free, NMS-free single-stage line.
- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md) — the precision/recall/F1/mAP panel used to benchmark.

## Open questions

- STAL and "dense-scene limitations" are the same problem the [heatmap-localization](../concepts/robotics/heatmap-object-localization.md) / [TrackNet](../entities/tracknet.md) thread solves a different way (change the *output*, not the *label assignment*) — no head-to-head exists on 2–12 px objects.
- Naming churn is real: "YOLO26 (or YOLOv26)", v12/v13 from other groups — the [version lineage](../syntheses/vision/yolo-version-lineage.md) synthesis disambiguates who authored what.
