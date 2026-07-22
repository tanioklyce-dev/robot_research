---
title: SAHI (Slicing Aided Hyper Inference)
type: concept
created: 2026-07-17
updated: 2026-07-17
sources: 1
tags: [object-detection, small-object-detection, computer-vision, inference, edge-ai, yolo]
---

# SAHI (Slicing Aided Hyper Inference)

**SAHI** (Slicing Aided Hyper Inference; Akyon, Altinuc & Temizel, *CVIU* 2022) is an **inference-time, model-agnostic** technique for improving **small-object detection** without retraining or changing the detector.

## Definition

A standard detector runs on a downsized full frame, so genuinely small objects occupy too few pixels to survive. SAHI instead **slices** the input image `I ∈ ℝ^{H×W×3}` into overlapping `S×S` patches — patch size `S = min(H,W)·r` with `r ∈ (0,1)`, and an overlap ratio `γ ∈ [0,0.5]` so border objects appear whole in at least one slice — runs the **same detector independently on each patch**, maps every prediction back into full-image coordinates, and **merges** the pooled detections with **NMS** (Non-Maximum Suppression) using an IoU threshold `τ` to drop duplicates. Because each object is now seen at higher effective resolution, recall on small / partially-occluded / edge-truncated instances rises. The cost is compute: N patches ≈ N detector passes per frame, an accuracy-for-latency trade the authors argue is justified in safety-critical settings. SAHI also supports a slicing-aided *fine-tuning* mode, but its most common use is pure post-processing.

## Key references

- [Enhancing YOLOv11n for Reliable Child Detection (PTIT 2026)](../../sources/ptit-yolov11n-child-detection.md) — applies SAHI on top of a fine-tuned [YOLOv11n](../../entities/ultralytics-yolo.md) to recover small/truncated children in CCTV footage; SAHI supplies the final mAP@0.5:0.95 bump (0.779 → 0.783) after data augmentation.

## Related concepts

- [AprilTags](apriltags.md) — a different route to reliable small-target perception (fiducial markers vs. slicing a general detector).
- [Ultralytics YOLO](../../entities/ultralytics-yolo.md) — the detector family SAHI most commonly wraps; complements it as a drop-in inference stage.
- [Heatmap-based object localization](heatmap-object-localization.md) — the **rival** answer to small-object detection: change the *output representation* (dense per-pixel map) rather than the *inference procedure* (slicing). Heatmaps win for a single known object class ([TrackNet](../../entities/tracknet.md) beats YOLOv7 by ~30 F1 on shuttlecock tracking); SAHI wins when you need general multi-class detection with extent.
- [Motion attention](motion-attention.md) — a *temporal* cheap bolt-on for small-object recall where SAHI is a *spatial* one; orthogonal and in principle stackable.

## Current state

SAHI is a well-established, off-the-shelf add-on (its own `sahi` PyPI package, native Ultralytics integration) for aerial imagery, surveillance, and any long-range/small-object detection task on edge hardware. It is orthogonal to model choice — it improves whatever detector it slices around — which is exactly why architecture-free papers reach for it to squeeze recall out of a small model like YOLOv11n.

## Mentioned in

- [Enhancing YOLOv11n for Reliable Child Detection (PTIT 2026)](../../sources/ptit-yolov11n-child-detection.md)
