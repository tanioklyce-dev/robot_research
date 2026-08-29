---
title: "YOLO: You Only Look Once — Unified, Real-Time Object Detection (Redmon et al. 2016)"
type: source
url: https://arxiv.org/abs/1506.02640
local_path: raw/1506.02640.pdf
sha256: 54bcd2dd05dc618849e8a94d8b88fe3eeb37f80e96e200600d38f1f733931678
author: Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi
published: 2016-05-09
ingested: 2026-07-23
venue: CVPR 2016 (arXiv:1506.02640, v1 2015-06-08)
tags: [object-detection, yolo, single-stage-detection, computer-vision, real-time, pascal-voc, seminal]
---

# YOLO: You Only Look Once — Unified, Real-Time Object Detection

## Summary

The paper that founded the [single-stage detection](../concepts/robotics/single-stage-object-detection.md) line. Redmon, Divvala, Girshick and Farhadi (University of Washington / [Allen Institute for AI](../entities/ai2.md) / Facebook AI Research) **reframe object detection as a single regression problem** — straight from image pixels to bounding-box coordinates and class probabilities — instead of the then-dominant "repurpose a classifier and run it at many locations/scales" pipeline (DPM sliding windows, R-CNN region proposals). A single convolutional network predicts all boxes and classes in **one forward pass**, so it can be optimized end-to-end on detection performance and runs in real time.

## Key claims

- **Detection as regression.** The image is divided into an **S×S grid**; each cell predicts **B** bounding boxes (each: x, y, w, h, confidence) plus **C** class conditional probabilities. For PASCAL VOC the paper uses **S=7, B=2, C=20**, so the network output is a single **7×7×30 tensor** (§2). Confidence = Pr(object) × IoU; class score at test time = per-cell class prob × box confidence.
- **One-class-per-cell spatial constraint.** Each grid cell predicts only one set of class probabilities regardless of B — a deliberate simplification that **limits how many nearby objects the model can resolve**.
- **Architecture.** 24 convolutional layers + 2 fully connected layers, **inspired by GoogLeNet** but using **1×1 reduction layers** followed by 3×3 convs instead of inception modules; conv layers pretrained on ImageNet at 224×224, detection fine-tuned at 448×448 (§2.1). **Fast YOLO** swaps in a 9-conv-layer backbone.
- **Loss.** Sum-squared error with two hand-set weights to stop the many empty cells from swamping the gradient: **λcoord = 5** (up-weight coordinate loss) and **λnoobj = 0.5** (down-weight confidence loss for boxes with no object); width/height predicted as square-roots so equal error counts less on large boxes (§2.2).
- **Speed / accuracy on PASCAL VOC 2007.** Base **YOLO: 63.4% mAP @ 45 fps**; **Fast YOLO: 52.7% mAP @ 155 fps** — "more than twice as accurate as prior work on real-time detection" (on a Titan X, no batching). Only **30Hz DPM** among prior detectors actually ran in real time.
- **Error profile vs Fast R-CNN.** YOLO makes **more localization errors** but **far fewer background false positives** — it reasons globally over the whole image, so it rarely fires on background patches the way sliding-window/region methods do. This complementarity is why an ensemble with Fast R-CNN helps.
- **Generalization.** Learns "very general representations of objects" — outperforms DPM and R-CNN when transferring from natural photos to **artwork** (Picasso and People-Art person-detection datasets), where region-proposal methods degrade badly.
- **Stated limitations.** Struggles with **small objects that appear in groups** (the canonical "flocks of birds" example); poor on unusual aspect ratios / configurations; coarse features from downsampling; loss treats localization error in small and large boxes too similarly. These are the exact failure modes later YOLO versions and this wiki's [heatmap trackers](../concepts/robotics/heatmap-object-localization.md) target.

## Entities mentioned

- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — the modern library/model family descended from this paper (Ultralytics did not author v1–v3; it later became the maintainer of the lineage).

## Concepts touched

- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md) — the paradigm this paper founds.
- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md) — mAP / PASCAL-VOC AP as used here.
- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md) — the rival representation for the "small objects in groups" regime where YOLO is weakest.

## Open questions

- The one-class-per-cell and 2-box-per-cell constraints are v1-specific; anchor boxes (v2), FPN multi-scale heads, and anchor-free heads (v8+) all exist to relax them — see the [YOLO version lineage](../syntheses/vision/yolo-version-lineage.md).
- The "fewer background false positives" property is often lost in citation; whether it survives into anchor-free NMS-free descendants (v10/v26) is not something the surveys quantify head-to-head.
