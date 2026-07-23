---
title: "COCO Detection Evaluation (cocoeval)"
type: source
url: https://cocodataset.org/#detection-eval
author: COCO Consortium (Lin et al.) — Microsoft COCO
published: 2014 (dataset); cocoeval as maintained in cocodataset/cocoapi
ingested: 2026-07-23
local_path: null
venue: cocodataset.org + github.com/cocodataset/cocoapi (pycocotools/cocoeval.py)
license: BSD-2-Clause (cocoapi); dataset CC-BY 4.0
format: web page + reference implementation (Python/C)
tags: [object-detection, evaluation-metrics, average-precision, mAP, iou, coco, benchmark, computer-vision]
---

# COCO Detection Evaluation (cocoeval)

## Summary

The de-facto standard for reporting object-detection accuracy, and the concrete
"grown-up" version of the [Padilla toolkit](padilla-object-detection-metrics.md)'s
Average-Precision machinery. COCO does not report a single AP but a **12-number
panel**, and — the decision that made it the standard — it **averages AP over ten
IoU thresholds (0.50:0.05:0.95)** rather than fixing one, so a method cannot win
by being good only at a lenient overlap. The authoritative definition lives in
`pycocotools/cocoeval.py` (the numbers below are quoted from its `Params` class
and `summarize()`), not the web page, which is a JS shell. Relevant to
[pinball_tracker](pinball-tracker-repo.md) as the reference every detection paper
scores against — and as the thing its ad-hoc single-threshold F1 is a deliberate
simplification of.

## Key claims

- **The 12 summary metrics** (`_summarizeDets`): six AP and six AR.
  - **AP** (the primary challenge metric) = AP averaged over IoU 0.50:0.95;
    **AP@.50** (PASCAL-VOC-style, lenient); **AP@.75** (strict); **AP-small**,
    **AP-medium**, **AP-large** (by object area).
  - **AR** (average recall) at **maxDets = 1, 10, 100**, plus **AR-small/medium/
    large**.
- **IoU thresholds:** `np.linspace(.5, .95, 10)` → **10 thresholds**, 0.50 to
  0.95 step 0.05. "AP" without a suffix means the mean over all ten. This is
  COCO's signature choice: rewarding *localization quality*, not just detection.
- **101-point interpolation:** recall thresholds `np.linspace(0, 1, 101)` — AP is
  the mean of interpolated precision at 101 evenly-spaced recall levels (finer
  than VOC's 11-point; see [Padilla](padilla-object-detection-metrics.md) for the
  11-point/all-point contrast COCO supersedes).
- **Matching** mirrors the general recipe: detections sorted by confidence
  descending, greedily matched to ground truth by IoU per threshold, **each GT
  matched at most once**; crowd/ignore regions and out-of-area-range detections
  are flagged `ignore` rather than scored.
- **Detection cap:** `maxDets = [1, 10, 100]` — AP uses 100 detections/image; the
  AR variants report at 1/10/100 to show recall vs. detection budget. (Directly
  analogous to [pinball](pinball-tracker-repo.md)'s `--max-peaks` cap, which set
  per-clip is the difference between FF val reading 0.537 and 0.914.)
- **Area ranges (px²):** all `[0, 1e5²]`; **small** `[0, 32²]`; **medium**
  `[32², 96²]`; **large** `[96², 1e5²]`. The scale breakdown is why COCO is the
  reference for **small-object** detection — the regime a 2–12 px ball lives in
  ([TrackNet](../entities/tracknet.md)).

## Relation to this wiki

- **Why pinball/TrackNet don't just use COCO AP.** AP integrates over a
  confidence-ranked PR curve; a real-time tracker emits a **fixed** set of peaks
  per frame (no free confidence sweep at deploy time) and cares about the
  operating point it will actually run at, so a single-threshold **F1** at a
  fixed peak cap is the honest match — see `docs/EVALUATION.md` in
  [pinball_tracker](pinball-tracker-repo.md). COCO answers "how good is the
  detector across all operating points"; the pinball F1 answers "how good is the
  one operating point I ship."
- **IoU → distance.** COCO matches boxes by IoU; point/blob trackers substitute a
  pixel-distance tolerance. Same greedy-under-threshold structure — see
  [detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md).

## Concepts touched

- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md)
- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md)

## Entities mentioned

- [TrackNet](../entities/tracknet.md) — small-object detector; COCO's scale
  buckets frame why it operates in the hardest (small) regime.

## Open questions

- COCO AP is designed for **offline** benchmarking with a confidence-ranked
  detection list. What is the right *causal, single-operating-point* accuracy
  metric for a **reflex controller** (fire-a-solenoid) tracker? The pinball
  project uses fixed-cap F1 + localization; whether that under- or over-states
  real control performance is untested.
- COCO has no continuity/identity notion (it is per-image). Tracking needs
  CLEAR-MOT / HOTA on top — noted for the pinball project's open CLEAR-MOT item.
