---
title: "Object-Detection-Metrics (Rafael Padilla)"
type: source
url: https://github.com/rafaelpadilla/Object-Detection-Metrics
author: Rafael Padilla
published: 2018 (repo created)
ingested: 2026-07-23
local_path: null
venue: GitHub repository
license: MIT
format: GitHub repo (Python) + long explanatory README
tags: [object-detection, evaluation-metrics, precision-recall, average-precision, mAP, iou, computer-vision, pedagogical]
---

# Object-Detection-Metrics (Rafael Padilla)

## Summary

A small MIT-licensed Python toolkit whose real value is its **README**, the
clearest freely-available explanation of how detection metrics are actually
computed. It exists because "the lack of consensus used by different works and
implementations concerning the evaluation metrics of the object detection
problem" makes published numbers hard to compare — so it centralizes the
PASCAL VOC, COCO, and ImageNet metrics in one place with a worked numeric
example. For anyone learning **why** an object detector's F1/AP is not the same
computation as a classifier's F1, this is the reference: the difference is a
**matching step**, and this README walks it end to end. Directly relevant to
[pinball_tracker](pinball-tracker-repo.md)'s scoring, whose distance-threshold
matching is the same idea as this repo's IoU-threshold matching.

## Key claims

- **The counts come from matching, not from a fixed table.** TP = a detection
  whose IoU with a ground-truth box ≥ threshold; FP = a detection with IoU <
  threshold (or a duplicate on an already-matched GT); FN = a ground-truth box
  no detection matched. **There is no TN** in detection — you would have to
  enumerate every possible non-detection. This is the crux that separates
  detection metrics from classification metrics.
- **Precision and recall have different denominators.** `P = TP/(TP+FP)`
  (per-detection: "when it fires, is it right?"); `R = TP/(TP+FN)` (per-object:
  "of the real objects, how many were found?").
- **Matching is greedy over confidence-sorted detections.** Detections are
  ordered by confidence descending; each is matched to the GT it best overlaps;
  when several detections hit one GT, **only the highest-IoU one is TP** and the
  rest are FP. Each GT is matched at most once.
- **The confidence threshold sweeps out the precision-recall curve.** Lowering
  it admits more detections — more potential TPs *and* FPs — tracing P against R.
- **Average Precision is the area under that curve, via interpolation.** Two
  conventions are contrasted:
  - **11-point** (older VOC): average of the max precision at recall ∈ {0, 0.1,
    …, 1.0}. `AP = (1/11) Σ ρ_interp(r)`.
  - **All-point** (current VOC default): interpolate at every recall value —
    a closer approximation to the true area.
  On the repo's toy set (15 GTs, 24 detections, 7 images, IoU≥30%): **11-point
  AP = 26.84%, all-point AP = 24.56%** — the two conventions genuinely disagree,
  which is the whole point about "no consensus."
- **mAP is AP averaged over classes.** Nothing more mysterious than that.
- **Supported formats** are deliberately minimal: plain text files (one per
  image) of `left top right bottom` or `left top width height`, absolute or
  normalized (YOLO-style) — no XML/JSON conversion, which is the friction the
  repo set out to remove.

## Relation to this wiki

- **Distance vs IoU matching.** [pinball_tracker](pinball-tracker-repo.md) and
  the [TrackNet](../entities/tracknet.md) family match on a **distance
  tolerance** (a ball is a point/small blob, so IoU is ill-suited), where this
  repo matches on **IoU** (boxes). The *structure* is identical — sort, greedily
  match under a threshold, count leftovers — which is exactly why this README
  transfers to point-tracking despite being written for box detection.
- **The pinball project's own eval doc** (`docs/EVALUATION.md`) derives the same
  greedy-matching-under-threshold machinery from first principles and documents
  where it silently produced wrong numbers (peak-count cap, tolerance, split
  boundary). This repo is the canonical external companion to that.

## Concepts touched

- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md)
  — the concept page this source anchors.
- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md)
  — the output form pinball/TrackNet use; changes matching from IoU to distance.

## Entities mentioned

- [TrackNet](../entities/tracknet.md) — uses the distance-threshold variant of
  this matching.

## Open questions

- The repo predates and does not cover COCO's **AP averaged over IoU 0.50:0.95**
  or its **101-point** interpolation — see [COCO detection eval](coco-detection-eval.md)
  for the current standard.
- Box-IoU matching has no clean analogue for a **point** target; the pinball
  project substitutes a pixel-distance tolerance, but "what tolerance" is a free
  parameter with no community standard (TrackNet uses 4 px; pinball uses 30 px
  image-space). Worth a concept note if a second point-tracking source appears.
