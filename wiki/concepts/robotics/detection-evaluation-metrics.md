---
title: Detection evaluation metrics (precision/recall/F1/AP under matching)
type: concept
created: 2026-07-23
updated: 2026-07-23
sources: 4
tags: [object-detection, evaluation-metrics, precision-recall, average-precision, mAP, f1, iou, computer-vision]
---

# Detection evaluation metrics (precision/recall/F1/AP under matching)

Scoring an object detector is **not** the same computation as scoring a
classifier, and the difference is the single most common source of confusion —
and of wrong numbers — in applied detection work. A classifier is handed a fixed
confusion matrix; a detector's TP/FP/FN counts must first be *produced* by a
**matching step** that decides which prediction corresponds to which ground-truth
object. Everything else (precision, recall, F1, AP, mAP) is downstream of that
matching, and inherits its free parameters.

## The matching step (where the counts come from)

For one image/frame you have a set of ground-truth objects and a set of
predictions. Matching assigns them:

1. **Sort** predictions by confidence, descending.
2. **Greedily match** each prediction to the ground-truth object it best
   overlaps, if that overlap clears a **threshold**. Each ground-truth is matched
   at most once; extra predictions on an already-matched object are false
   positives.
3. **Count leftovers:** unmatched ground truth → **FN**, unmatched predictions →
   **FP**, matched pairs → **TP**. There is **no true negative** — you would have
   to enumerate every possible non-detection.

The "overlap" and its threshold are the crux:

- **Box detectors** use **IoU** (intersection-over-union) with a threshold like
  0.50 or 0.75 ([Padilla](../../sources/padilla-object-detection-metrics.md),
  [COCO](../../sources/coco-detection-eval.md)).
- **Point / small-blob trackers** (a ball is ~2–12 px) use a **pixel-distance
  tolerance** instead, because IoU degenerates for a point — the
  [TrackNet](../../entities/tracknet.md) family uses 4 px; the first-party
  [pinball_tracker](../../sources/pinball-tracker-repo.md) uses 30 px in image
  space. **Same greedy-under-threshold structure, different overlap function.**

## The downstream metrics

- **Precision** `= TP/(TP+FP)` — per-prediction, "when it fires, is it right?"
  Low precision = firing on non-objects (e.g. round playfield decorations).
- **Recall** `= TP/(TP+FN)` — per-object, "of the objects that existed, how many
  were found?" Different denominator from precision, so they move independently.
- **F1** `= 2PR/(P+R) = 2TP/(2TP+FP+FN)` — the *harmonic* mean, which collapses
  toward the smaller of P and R, so a model cannot score well by acing one and
  ignoring the other. `Fᵦ` re-weights toward recall (β>1) or precision (β<1); the
  right β is task-dependent and the metric does not encode it.
- **Average Precision (AP)** — the area under the precision-recall curve traced
  by sweeping the confidence threshold, computed by interpolation (VOC 11-point
  or all-point; COCO **101-point**). **mAP** averages AP over classes; **COCO AP**
  further averages over ten IoU thresholds (0.50:0.05:0.95) so a method cannot win
  on lenient overlap alone.

## F1-at-an-operating-point vs AP-over-all-operating-points

A load-bearing distinction for *deployed* trackers. **AP** integrates over the
whole confidence-ranked curve — it answers "how good is the detector across all
operating points," which is the right question for an offline benchmark. A
**real-time reflex tracker** emits a *fixed* set of peaks per frame and runs at
one operating point, so a single-threshold **F1 at a fixed detection cap** is the
honest measure of the point it actually ships. This is why
[pinball_tracker](../../sources/pinball-tracker-repo.md) reports F1 rather than
COCO AP, and its `docs/EVALUATION.md` derives the machinery from scratch.

## The free parameters that silently change the number

Every detection score carries hidden conditions; state them or it is not
reproducible:

- **The overlap threshold** (IoU 0.50 vs 0.75; distance 4 px vs 30 px) — flatters
  or sharpens every model.
- **The detection cap** (COCO `maxDets`; pinball `--max-peaks`) — a cap above the
  true object count manufactures false positives. On a one-ball clip, the pinball
  project read **F1 0.537 at cap-4 vs 0.914 at cap-1** — same model, different
  harness setting.
- **Greedy vs optimal matching** — greedy (nearest/highest-IoU first) vs Hungarian
  min-cost assignment; they diverge only when objects are close relative to the
  threshold.
- **The split boundary and sample independence** — orthogonal to matching but
  co-equal in producing honest numbers; see the pinball project's held-out-by-
  machine discipline.

## Key references

- [Object-Detection-Metrics (Padilla)](../../sources/padilla-object-detection-metrics.md)
  — the clearest walk-through of matching → PR curve → AP, with a worked numeric
  example (11-point 26.84% vs all-point 24.56% on the same toy set).
- [COCO Detection Evaluation](../../sources/coco-detection-eval.md) — the standard
  12-metric panel; AP averaged over IoU 0.50:0.95; 101-point interpolation.
- [TrackNet](../../entities/tracknet.md) — the distance-threshold variant, for
  small fast objects where IoU degenerates.
- [pinball_tracker](../../sources/pinball-tracker-repo.md) — a first-party
  detector whose `docs/EVALUATION.md` documents these metrics *and the wrong
  numbers each produced* when a hidden condition was violated.

## Related concepts

- [Heatmap-based object localization](heatmap-object-localization.md) — the output
  representation that makes matching distance-based (peak) rather than IoU-based
  (box).
- [Motion attention](motion-attention.md) — a recall-buying, precision-costing
  module; understanding the P/R trade above is what makes its "+0.4–0.6 F1"
  legible.

## Current state

Detection metrics are mature and standardized for *offline box benchmarking*
(COCO AP is universal). What remains under-specified is the **point-tracking**
and **real-time / single-operating-point** regime: there is no community standard
distance tolerance, and no agreed causal accuracy metric for a controller that
must act on each frame. The pinball project's fixed-cap F1 + localization is one
reasonable answer, explicitly flagged as untested against real control
performance. Continuity/identity (tracking, not just detection) needs CLEAR-MOT /
HOTA on top — a separate metric family.

## Mentioned in

- [Object-Detection-Metrics (Padilla)](../../sources/padilla-object-detection-metrics.md)
- [COCO Detection Evaluation](../../sources/coco-detection-eval.md)
- [pinball_tracker GitHub](../../sources/pinball-tracker-repo.md)
