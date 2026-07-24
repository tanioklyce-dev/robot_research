---
title: "YOLOv1 to YOLOv11: A Comprehensive Survey of Real-Time Object Detection Innovations and Challenges (Kotthapalli et al. 2025)"
type: source
url: https://arxiv.org/abs/2508.02067
local_path: raw/2508.02067.pdf
author: Manikanta Kotthapalli, Deepika Ravipati, Reshma Bhatia
published: 2025-08-04
ingested: 2026-07-23
venue: arXiv:2508.02067
tags: [object-detection, yolo, survey, single-stage-detection, multi-task, computer-vision, review]
---

# YOLOv1 to YOLOv11: A Comprehensive Survey of Real-Time Object Detection Innovations and Challenges

## Summary

A 2025 refresh of the YOLO survey genre that carries the lineage forward to **YOLOv11** and, importantly, documents YOLO's **expansion beyond bounding-box detection** into instance segmentation, pose estimation, object tracking, and domain-specific verticals (medical imaging, industrial automation). Traces how each version rebalanced **speed, accuracy, and deployment efficiency** through architectural and algorithmic changes.

## Key claims

- **Extended lineage.** Picks up where [Terven & Cordova-Esparza 2023](terven-yolo-survey-2023.md) left off, covering through **YOLOv9 / v11** (the abstract cites "the latest YOLOv9" in the core-detection narrative and reviews up to v11's multi-task heads). Consolidated in the [YOLO version lineage](../syntheses/vision/yolo-version-lineage.md).
- **Multi-task is now first-class.** Modern YOLO releases ship not just detection but **instance segmentation, pose estimation, and tracking** as native tasks off a shared backbone — exactly the `detect/segment/classify/pose/OBB/track` surface of the [Ultralytics YOLO](../entities/ultralytics-yolo.md) library. The survey frames this as a defining shift: YOLO went from a detector to a **real-time vision multi-tool**.
- **Vertical applications.** Emphasizes medical imaging and industrial automation as proof that the same architecture generalizes across domains with fine-tuning — the transfer story that makes YOLO the commodity perception layer in edge-robotics stacks.
- **Critical framing.** Explicitly "critically analyzes" the evolution and flags emerging research directions rather than just cataloguing — a survey with a point of view about where the diminishing returns and open problems are.

## Entities mentioned

- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — the multi-task library the survey's later versions describe.

## Concepts touched

- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md)
- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md)

## Open questions

- Stops at v11; **YOLO26** (NMS-free, STAL, MuSGD) is covered instead by [Sapkota & Karkee 2025](sapkota-ultralytics-yolo-evolution-2025.md).
- Three overlapping surveys (this, Terven, Sapkota) now cover the lineage with different cutoffs and emphases — the [YOLO version lineage](../syntheses/vision/yolo-version-lineage.md) synthesis exists to reconcile them into one table.
