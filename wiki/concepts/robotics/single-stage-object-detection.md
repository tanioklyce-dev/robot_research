---
title: Single-stage object detection (the YOLO paradigm)
type: concept
created: 2026-07-23
updated: 2026-07-23
sources: 5
tags: [object-detection, yolo, single-stage-detection, anchor-free, nms, computer-vision, real-time, edge-ai]
---

# Single-stage object detection (the YOLO paradigm)

**Single-stage** (a.k.a. one-stage) detectors predict object boxes and classes
in **one forward pass** over the whole image, as a **regression** problem —
versus **two-stage** detectors (R-CNN family) that first *propose* regions and
then *classify* each one. The single-stage idea is what makes detection run in
real time on edge hardware, and it is the paradigm behind every model in this
wiki's [Ultralytics YOLO](../../entities/ultralytics-yolo.md) stack.

## The founding move

[YOLO (Redmon et al. 2016)](../../sources/yolo-you-only-look-once-2016.md)
reframed detection: instead of "run a classifier at many locations/scales"
(sliding-window DPM) or "propose boxes, then classify each" (R-CNN), it divides
the image into an **S×S grid** and has a single CNN regress, per cell, a fixed
set of boxes + class probabilities — the whole image's detections as **one
tensor** (7×7×30 for PASCAL VOC). One network, one pass, optimized end-to-end on
detection. That bought **45 fps at 63.4% mAP** (Fast YOLO: 155 fps) when the only
prior real-time detector was 30 Hz DPM.

The trade it introduced — **more localization error, but far fewer background
false positives** because the net reasons globally over the whole frame — is the
signature of the single-stage family and the reason it generalizes well
(e.g. natural photos → artwork).

## The axes that every version turns

Across the lineage (see the [YOLO version lineage](../../syntheses/vision/yolo-version-lineage.md)
for the version-by-version diff), the same knobs keep turning:

- **Anchor-based → anchor-free.** v1 regressed boxes directly; v2 added
  clustered **anchor boxes** for stable training; v8 went **anchor-free** again,
  now with better assignment. Anchors were a training-stability crutch the field
  learned to remove.
- **Coupled → decoupled head.** Splitting the classification and box-regression
  branches (v8+) improved both.
- **Single-scale → multi-scale.** v3 added **FPN/PAN**-style predictions at
  several resolutions — the main fix for v1's worst weakness, small objects.
- **Heavier free training tricks.** Mosaic/mixup augmentation, better label
  assignment, new optimizers (YOLO26's **MuSGD**, **ProgLoss**) — all cost
  nothing at inference.
- **NMS → NMS-free.** The last non-end-to-end piece.

## Removing NMS — the end-to-end frontier

Classic YOLO trains with **one-to-many** label assignment (many anchors per
object → rich gradients) and then must run **Non-Maximum Suppression** at
inference to collapse the duplicate boxes. NMS is non-differentiable,
latency-adding, and hyperparameter-laden. [YOLOv10 (Wang et al. 2024)](../../sources/yolov10-nms-free-2024.md)
removed it via **consistent dual assignments**: a one-to-one head (trained
alongside the one-to-many head, aligned by a consistent matching metric) learns
to emit a single clean box per object, so inference is genuinely one pass with no
post-processing. **YOLO26** makes NMS-free inference the default
([Sapkota & Karkee 2025](../../sources/sapkota-ultralytics-yolo-evolution-2025.md)).

> [!note] An NMS-free head emits a **fixed, deduplicated** set of predictions —
> structurally close to the "one operating point per frame" regime this wiki
> cares about for reflex trackers (see
> [detection evaluation metrics](detection-evaluation-metrics.md), the fixed-cap-F1
> vs AP distinction). No one has measured whether that changes the story.

## Where single-stage detection stops working

The paradigm's oldest, most durable weakness is stated in the v1 paper itself:
**small objects that appear in groups** ("flocks of birds"), and objects in
unusual aspect ratios. Every generation attacks it — multi-scale heads (v3),
Small-Target-Aware Label Assignment (YOLO26's **STAL**) — but box regression has
a floor. For **2–12 px** objects (a ball in sports/robot video), this wiki's
first-party evidence is that a **YOLOv7 box baseline scores 68.0 F1 vs
TrackNetV3's 97.5** ([TrackNet](../../entities/tracknet.md),
[TrackNetV4](../../sources/tracknetv4-motion-attention-2024.md)). The fix there is
**changing the output representation** to a dense
[heatmap](heatmap-object-localization.md), not turning YOLO's label-assignment
knob. **STAL vs heatmaps is the same problem attacked from opposite ends** — no
head-to-head benchmark exists.

## Key references

- [YOLO: You Only Look Once (Redmon et al. 2016)](../../sources/yolo-you-only-look-once-2016.md)
  — founds the paradigm; the grid/regression formulation.
- [YOLOv10 (Wang et al. 2024)](../../sources/yolov10-nms-free-2024.md) — NMS-free,
  the end-to-end completion.
- [Terven & Cordova-Esparza 2023](../../sources/terven-yolo-survey-2023.md),
  [Kotthapalli et al. 2025](../../sources/kotthapalli-yolo-survey-2025.md),
  [Sapkota & Karkee 2025](../../sources/sapkota-ultralytics-yolo-evolution-2025.md)
  — three surveys covering the lineage to v8/NAS, v11, and YOLO26 respectively.

## Related concepts

- [Detection evaluation metrics](detection-evaluation-metrics.md) — how mAP/AP
  (the yardstick every YOLO paper reports) is actually computed.
- [Heatmap-based object localization](heatmap-object-localization.md) — the rival
  output representation for the tiny-object regime where boxes fail.
- [SAHI (slicing inference)](sahi-slicing-inference.md) — a *procedural* small-object
  fix that wraps YOLO-class detectors (change the inference loop, not the model).

## Current state

Single-stage detection is the default for real-time / edge CV; the frontier as of
YOLO26 is **anchor-free + NMS-free + small-target-aware**, plus deployment
concerns (quantization, export). Open challenges named by the surveys: **dense
scenes**, **hybrid CNN-Transformer** designs ([RT-DETR](../../entities/rt-detr.md),
[DEIM](../../entities/deim.md)), **open-vocabulary** detection, and **edge-aware
training**.

## Mentioned in

- [YOLO: You Only Look Once (Redmon et al. 2016)](../../sources/yolo-you-only-look-once-2016.md)
- [YOLOv10 (Wang et al. 2024)](../../sources/yolov10-nms-free-2024.md)
- [Terven & Cordova-Esparza 2023](../../sources/terven-yolo-survey-2023.md)
- [Kotthapalli et al. 2025](../../sources/kotthapalli-yolo-survey-2025.md)
- [Sapkota & Karkee 2025](../../sources/sapkota-ultralytics-yolo-evolution-2025.md)
