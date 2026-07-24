---
title: "The YOLO version lineage (v1 → v26): what actually changed"
type: synthesis
created: 2026-07-23
updated: 2026-07-23
tags: [object-detection, yolo, single-stage-detection, lineage, survey-synthesis, computer-vision]
---

# The YOLO version lineage (v1 → v26): what actually changed

YOLO is not one lab's roadmap. Like the [TrackNet](../../entities/tracknet.md)
family, "YOLO" spans **multiple independent groups** who each grabbed the name —
Redmon (v1–v3), Bochkovskiy/Wang (v4/v7/v9), Ultralytics (v5/v8/v11/26), Meituan
(v6), Deci (NAS), Tsinghua (v10), and others (v12/v13). This page reconciles the
three surveys and two primary papers ingested here into **one annotated
timeline**, so the naming churn doesn't obscure the handful of ideas that actually
moved the field.

Source coverage by cutoff:
[Terven & Cordova-Esparza 2023](../../sources/terven-yolo-survey-2023.md) covers
**v1 → v8 / YOLO-NAS / RT-DETR**;
[Kotthapalli et al. 2025](../../sources/kotthapalli-yolo-survey-2025.md) extends
through **v11** and the multi-task expansion;
[Sapkota & Karkee 2025](../../sources/sapkota-ultralytics-yolo-evolution-2025.md)
anchors on **YOLO26**. The v1 and v10 rows are grounded in the
[primary](../../sources/yolo-you-only-look-once-2016.md)
[papers](../../sources/yolov10-nms-free-2024.md).

## The timeline

| Version | Year / group | The one thing it changed |
|---|---|---|
| **v1** | 2016, Redmon et al. | **The paradigm.** Detection as one-pass grid regression; 7×7 grid, no anchors; 63.4% mAP @ 45 fps ([paper](../../sources/yolo-you-only-look-once-2016.md)). |
| **v2 / YOLO9000** | 2017, Redmon | **Anchor boxes** (k-means dimension clusters), batch-norm, high-res classifier, Darknet-19. Anchors stabilized training. |
| **v3** | 2018, Redmon | **Multi-scale prediction** (3 scales, FPN-style) + Darknet-53 residual backbone — the main fix for small objects. Redmon's last. |
| **v4** | 2020, Bochkovskiy et al. | **"Bag of freebies/specials"**: CSPDarknet backbone, PANet neck, **mosaic augmentation**, CIoU loss — free training-time gains. |
| **v5** | 2020, Ultralytics | **The PyTorch foundation.** No new architecture landmark; the engineering (auto-anchor, easy train/export, packaging) that made YOLO a *library*. Named by two surveys as the enabling inflection. |
| **v6** | 2022, Meituan | Industrial focus; re-parameterizable (RepVGG-style) backbone, anchor-free, decoupled head. |
| **v7** | 2022, Wang et al. | **E-ELAN** (extended efficient layer aggregation) + trainable bag-of-freebies + model re-parameterization. (The v7 box baseline is this wiki's [heatmap-vs-boxes](../../concepts/robotics/heatmap-object-localization.md) reference: 68.0 vs 97.5 F1.) |
| **v8** | 2023, Ultralytics | **Anchor-free + decoupled head**, C2f blocks, and **multi-task** as first-class (detect/seg/pose/cls/OBB). Undoes v2's anchors, now with better label assignment. |
| **[YOLO-NAS](../../entities/yolo-nas.md)** | 2023, Deci | **Neural-architecture-searched** (AutoNAC), **quantization-friendly** (INT8-robust) — optimized for deployment, not novelty. |
| **[RT-DETR](../../entities/rt-detr.md)** | 2023–24, Baidu | Not a YOLO — the **transformer** (DETR) line brought to real-time; NMS-free by set prediction. The standing benchmark foil the YOLO papers measure against. |
| **[DEIM](../../entities/deim.md)** | 2024–25, Huang et al. | Not a YOLO — **DETR with Improved Matching** (Dense O2O + MAL); fixes DETR's slow convergence. A YOLO26 benchmark cross-comparison. |
| **v9** | 2024, Wang et al. | **PGI** (programmable gradient information) + **GELAN** — better gradient flow to deeper layers. |
| **v10** | 2024, Tsinghua | **NMS-free, end-to-end** via consistent dual assignments (one-to-many + one-to-one heads); removes the last post-processing step ([paper](../../sources/yolov10-nms-free-2024.md)). |
| **v11** | 2024, Ultralytics | Efficiency modules (C3k2), multi-task refinements; replaced v8 as Ultralytics flagship. |
| **v12 / v13** | 2025, other groups | Attention-centric / newer designs. *(Named by [Sapkota & Karkee](../../sources/sapkota-ultralytics-yolo-evolution-2025.md) as cross-comparisons; per-version detail not verified here.)* |
| **YOLO26** | 2025–26, Ultralytics | **DFL removal**, native **NMS-free** inference (v10's idea as default), **ProgLoss**, **STAL** (small-target-aware assignment), **MuSGD** optimizer ([overview](../../sources/sapkota-ultralytics-yolo-evolution-2025.md)). |

> [!note] Confidence. The v1 and v10 rows are grounded in the primary papers. The
> intermediate rows report the **canonical, field-standard** innovation for each
> version as covered by the three surveys; specific micro-claims (exact block
> names, the v12/v13 details) are corroborated by the surveys' scope rather than
> quoted, and the newest, most-churned versions carry the most uncertainty.

## The four ideas underneath the twelve versions

Strip the names and almost every jump is one of four recurring moves — the axes
detailed on [single-stage object detection](../../concepts/robotics/single-stage-object-detection.md):

1. **Anchors, added then removed.** v1 anchor-free → v2 anchors (stability) → v8
   anchor-free again (once label assignment got good enough). A crutch the field
   picked up and put back down.
2. **Multi-scale + neck.** v3's FPN, v4's PAN — most of the small-object gains.
3. **Free training tricks.** Mosaic/mixup (v4), re-parameterization (v6/v7), PGI
   (v9), ProgLoss/MuSGD/STAL (v26) — all inference-cost-neutral.
4. **Toward end-to-end.** Decoupled heads (v8) → **NMS-free** (v10 → v26). The
   pipeline that v1 already called "a single network" finally became one, with no
   post-processing.

## So what, for this wiki

- **Which version to reach for.** For edge-robot perception the practical choice
  is the current [Ultralytics](../../entities/ultralytics-yolo.md) flagship
  (**YOLO11 / YOLO26**) — that's what has the export/TensorRT/quantization path and
  the multi-task heads. The research-y forks (v9/v10/v12) matter mainly for the
  *idea* they contributed, which Ultralytics tends to absorb.
- **The persistent ceiling.** Every version from v1 to v26 attacks **small
  objects in groups** — v3's multi-scale, v26's **STAL** — but it remains YOLO's
  named weakness. For **2–12 px** objects this wiki's first-party evidence still
  favors **changing the output representation** to a
  [heatmap](../../concepts/robotics/heatmap-object-localization.md) over turning
  YOLO's assignment knob (YOLOv7 68.0 vs TrackNetV3 97.5 F1). **STAL vs heatmaps
  is the same problem attacked from opposite ends, un-benchmarked head-to-head** —
  the sharpest open question the YOLO thread and the
  [fast-ball-tracking](../projects/fast-ball-tracking-for-robots.md) thread share.
- **NMS-free changes the shipping story.** A v10/v26 one-to-one head emits a
  **fixed, deduplicated** set of boxes — structurally the "one operating point per
  frame" a reflex tracker runs at (see
  [detection evaluation metrics](../../concepts/robotics/detection-evaluation-metrics.md)).
  Whether that makes YOLO26 a better fit for real-time robot control than the F1-at-
  fixed-cap trackers this wiki benchmarks is untested and worth a probe.

## Related

- [Single-stage object detection](../../concepts/robotics/single-stage-object-detection.md) — the paradigm and its axes.
- [Ultralytics YOLO](../../entities/ultralytics-yolo.md) — the library that maintains the mainline (v5/v8/v11/26).
- [Fast-ball tracking for robots](../projects/fast-ball-tracking-for-robots.md) — where the YOLO-vs-heatmap boundary is tested first-party.
- [Detection evaluation metrics](../../concepts/robotics/detection-evaluation-metrics.md) — how every "mAP" in the table above is computed.
