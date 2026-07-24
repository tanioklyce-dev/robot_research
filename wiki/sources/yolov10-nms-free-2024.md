---
title: "YOLOv10: Real-Time End-to-End Object Detection (Wang et al. 2024)"
type: source
url: https://arxiv.org/abs/2405.14458
local_path: raw/2405.14458.pdf
author: Ao Wang, Hui Chen, Lihao Liu, Kai Chen, Zijia Lin, Jungong Han, Guiguang Ding (Tsinghua University)
published: 2024-10-30
ingested: 2026-07-23
venue: NeurIPS 2024 (arXiv:2405.14458, v1 2024-05-23)
tags: [object-detection, yolo, single-stage-detection, nms-free, end-to-end, computer-vision, coco]
---

# YOLOv10: Real-Time End-to-End Object Detection

## Summary

YOLOv10 (Tsinghua University) removes the **last non-end-to-end piece** of the YOLO pipeline — the **NMS post-processing** — and does a from-scratch efficiency/accuracy audit of every component. Its two headline contributions: **consistent dual assignments** for NMS-free training (so the network emits one clean box per object directly, no duplicate-suppression pass) and a **holistic efficiency-accuracy design** that trims redundant compute and adds capability where it pays off. Result: a Pareto step forward on the COCO speed/accuracy frontier, and true end-to-end deployment.

## Key claims

- **The NMS problem.** Classic YOLO trains with **one-to-many label assignment** (many anchors per object → rich supervision) but must then run **NMS** at inference to collapse the duplicates. NMS is a non-differentiable, latency-adding, hyperparameter-laden post-step that breaks end-to-end deployment.
- **Consistent dual assignments.** YOLOv10 adds a **one-to-one head** alongside the usual **one-to-many head**. Both are trained jointly; the one-to-many head supplies rich gradients, the one-to-one head learns to emit a single prediction per object so **NMS can be dropped at inference**. A **consistent matching metric** aligns which prediction each head treats as "the" positive, so the two heads don't fight — the one-to-one head is supervised toward the same top pick the one-to-many head favors.
- **Holistic efficiency-accuracy design** — component-level redesign:
  - **Lightweight classification head** (the cls branch was over-provisioned relative to the reg branch).
  - **Spatial-channel decoupled downsampling** — separate spatial reduction from channel expansion to cut cost.
  - **Rank-guided block design** — allocate blocks/compute by measured stage redundancy rather than uniformly.
  - **Large-kernel convolution** and **partial self-attention (PSA)** — cheap ways to enlarge receptive field / add global context only where accuracy benefits.
- **COCO benchmarks (val2017).** YOLOv10-S **46.3 AP @ 1.84 ms / 3.3M params**; -M 52.5 AP; -B 53.1 AP; -L 53.4 AP; -X **54.4 AP**. **YOLOv10-S is ~1.8× faster than RT-DETR-R18 at similar AP with ~40% fewer parameters**; **YOLOv10-B has 46% lower latency than YOLOv9-C at equal AP with 25% fewer parameters.**

## Entities mentioned

- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — ships YOLOv10 in the back-catalog (`yolov10` recipes / weights); its NMS-free idea is a direct ancestor of the later **YOLO26** NMS-free inference.

## Concepts touched

- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md) — YOLOv10 completes the "single-stage" promise by removing NMS, making detection genuinely one forward pass.
- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md) — COCO AP (0.50:0.95) is the yardstick used.

## Open questions

- NMS-free (one-to-one) heads emit a **fixed, deduplicated** set of predictions — structurally closer to the "one operating point" regime this wiki cares about for reflex trackers. Whether that changes the fixed-cap-F1 vs AP story for real-time robot use isn't addressed here.
- The dual-assignment idea is now mainstream (v10 → YOLO26); the surveys ([Sapkota & Karkee 2025](sapkota-ultralytics-yolo-evolution-2025.md), [Kotthapalli 2025](kotthapalli-yolo-survey-2025.md)) trace it but don't isolate how much of YOLO26's gain is NMS-free vs the rest.
