---
title: DEIM (DETR with Improved Matching)
type: entity
subtype: model-family
created: 2026-07-24
updated: 2026-07-24
sources: 1
tags: [object-detection, deim, detr, rt-detr, transformer, real-time, computer-vision]
---

# DEIM (DETR with Improved Matching)

**DEIM** — *DETR with Improved Matching* — is a training/matching improvement for
the [RT-DETR](rt-detr.md) / DETR line of transformer detectors (Huang et al.,
CVPR 2025). Where [RT-DETR](rt-detr.md) made the DETR architecture real-time,
DEIM attacks DETR's other chronic weakness — **slow, sparse training convergence**
— by improving the **bipartite matching** that supervises the one-to-one head.

## Why it matters in this wiki

DEIM appears here as one of the **state-of-the-art transformer detectors** that
[YOLO26](../sources/sapkota-ultralytics-yolo-evolution-2025.md) is benchmarked
against — so it marks the current CNN-vs-transformer frontier alongside
[RT-DETR](rt-detr.md). It is the "matching got better" chapter of the DETR story
that the YOLO camp reached from the other side with
[YOLOv10](../sources/yolov10-nms-free-2024.md)'s consistent dual assignments:
**both lines are converging on how to supervise a clean one-box-per-object head.**

## Key facts

- **What it improves (per its design):** **Dense O2O** (dense one-to-one) matching
  to give the model many more positive-matching signals per image early in
  training, plus a **Matchability-Aware Loss (MAL)** — together yielding faster
  convergence and higher accuracy than the RT-DETR baseline at similar cost.
- **Lineage:** built on the DETR / RT-DETR set-prediction framework, so it inherits
  the **NMS-free** property.
- **Role in the wiki:** a benchmark cross-comparison for **YOLO26**
  ([Sapkota & Karkee 2025](../sources/sapkota-ultralytics-yolo-evolution-2025.md)).

> [!note] Not yet ingested. This page is grounded in the one survey that
> benchmarks against DEIM, not the DEIM paper itself; the architecture claims are
> "per its design." Ingesting the primary paper would upgrade them to first-party
> and is the obvious next step if DEIM becomes load-bearing.

## Related

- [RT-DETR](rt-detr.md) — the real-time DETR baseline DEIM builds on and improves.
- [YOLOv10](../sources/yolov10-nms-free-2024.md) — the CNN camp's route to the same NMS-free, clean-assignment goal.
- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md) — the "hybrid CNN-Transformer" frontier this sits on.
- [YOLO version lineage](../syntheses/vision/yolo-version-lineage.md).

## Mentioned in

- [Sapkota & Karkee 2025](../sources/sapkota-ultralytics-yolo-evolution-2025.md) — YOLO26 vs RT-DETR / DEIM cross-comparison.
