---
title: "A Comprehensive Review of YOLO Architectures: From YOLOv1 to YOLOv8 and YOLO-NAS (Terven & Cordova-Esparza 2023)"
type: source
url: https://arxiv.org/abs/2304.00501
local_path: raw/2304.00501.pdf
author: Juan Terven, Diana Cordova-Esparza
published: 2024-02-04
ingested: 2026-07-23
venue: Machine Learning and Knowledge Extraction (arXiv:2304.00501, v1 2023-04-02, v7 2024-02-04)
tags: [object-detection, yolo, survey, single-stage-detection, computer-vision, review]
---

# A Comprehensive Review of YOLO Architectures: From YOLOv1 to YOLOv8 and YOLO-NAS

## Summary

The most-cited **YOLO survey** — the standard reference for "what changed at each version." Terven & Cordova-Esparza walk the lineage from the original YOLO through **YOLOv8, YOLO-NAS, and YOLO-with-Transformers (RT-DETR)**, first laying out the **evaluation metrics and post-processing** every version shares, then the per-version architecture changes and training tricks, and closing with lessons and future directions. Written for practitioners deploying real-time detection in robotics, driverless cars, and video monitoring.

## Key claims

- **Shared foundation first.** The review front-loads the parts common to all versions — the **AP/mAP metric machinery**, IoU, and **NMS** post-processing — before diffing architectures, which is why it doubles as a metrics primer (complements this wiki's [detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md) page).
- **The lineage it covers (v1 → v8 + NAS).** Original YOLO (grid regression) → v2/YOLO9000 (anchor boxes, batch-norm, high-res classifier, dimension clusters) → v3 (multi-scale FPN-style predictions, residual backbone) → v4 (bag-of-freebies/specials, CSPDarknet, mosaic aug) → v5 (PyTorch, Ultralytics engineering) → v6/v7 (re-parameterization, extended efficient layer aggregation) → v8 (anchor-free, decoupled head) → **YOLO-NAS** (neural-architecture-searched, quantization-friendly) → **RT-DETR** (transformer detector reaching real-time). See the consolidated [YOLO version lineage](../syntheses/vision/yolo-version-lineage.md).
- **Recurring axes of change.** Across versions the survey identifies the same knobs turning: **anchor-based → anchor-free**, coupled → **decoupled heads**, single-scale → **multi-scale (FPN/PAN)** prediction, and steadily heavier **training-time augmentation** (mosaic, mixup) that costs nothing at inference.
- **Framing.** Positions YOLO as *the* real-time detection system for embodied/edge use — the exact niche this wiki's edge-robotics stack ([Ultralytics YOLO](../entities/ultralytics-yolo.md), Jetson/Hailo recipes) occupies.

## Entities mentioned

- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — the survey treats v5/v8 (Ultralytics) as the engineering inflection that made YOLO a broadly-adopted library.

## Concepts touched

- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md)
- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md) — the survey's metrics/post-processing section.

## Open questions

- Ends at v8/NAS/RT-DETR (early 2024); v9–v13 and YOLO26 are picked up by the newer surveys ([Kotthapalli 2025](kotthapalli-yolo-survey-2025.md) through v11, [Sapkota & Karkee 2025](sapkota-ultralytics-yolo-evolution-2025.md) through YOLO26).
