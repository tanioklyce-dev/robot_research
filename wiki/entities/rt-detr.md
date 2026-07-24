---
title: RT-DETR (Real-Time Detection Transformer)
type: entity
subtype: model-family
created: 2026-07-24
updated: 2026-07-24
sources: 4
tags: [object-detection, rt-detr, detr, transformer, nms-free, real-time, computer-vision]
---

# RT-DETR (Real-Time Detection Transformer)

**RT-DETR** is a **transformer-based**, real-time object detector — the DETR
(DEtection TRansformer) lineage engineered down to YOLO-class latency. It is the
recurring **non-YOLO alternative** cited throughout this wiki's detection thread:
where [YOLO](ultralytics-yolo.md) reframes detection as CNN grid regression,
RT-DETR keeps DETR's **set-prediction** formulation and is therefore **NMS-free by
design** (bipartite Hungarian matching during training means no duplicate boxes
to suppress at inference). Introduced by **Baidu** (Zhao et al., *"DETRs Beat
YOLOs on Real-time Object Detection,"* CVPR 2024 / arXiv:2304.08069).

## Why it matters in this wiki

RT-DETR is the standing benchmark competitor in every recent YOLO source here, so
it defines the **CNN-vs-transformer frontier** of real-time detection:

- **The NMS-free precedent.** DETR/RT-DETR were *already* NMS-free via set
  prediction; [YOLOv10](../sources/yolov10-nms-free-2024.md)'s "consistent dual
  assignments" is the CNN camp reaching the same end-to-end property a different
  way. RT-DETR is why "NMS-free" was a target worth hitting.
- **The benchmark foil.** YOLOv10 measures itself against it:
  **RT-DETR-R18 = 46.5 AP @ 5.20 ms**, and YOLOv10-S matches that AP while being
  **~1.8× faster with ~40% fewer parameters**
  ([YOLOv10](../sources/yolov10-nms-free-2024.md)). YOLO26 is likewise
  cross-compared against RT-DETR and **[DEIM](deim.md)** (DETR with Improved Matching)
  ([Sapkota & Karkee 2025](../sources/sapkota-ultralytics-yolo-evolution-2025.md)).
- **Surveyed as "YOLO with Transformers."** [Terven & Cordova-Esparza 2023](../sources/terven-yolo-survey-2023.md)
  covers RT-DETR as the transformer entry alongside the CNN YOLO line; hybrid
  CNN-Transformer integration is named an open direction by the newer surveys.

## Key facts

- **Formulation:** DETR-style end-to-end set prediction → **NMS-free**; the main
  structural difference from the YOLO family.
- **Core design (per survey coverage):** an **efficient hybrid encoder** that
  decouples intra-scale interaction from cross-scale fusion, plus **IoU-aware
  query selection**; decoder-layer count is **tunable at inference** to trade
  speed for accuracy without retraining.
- **Deployment:** shipped in the [Ultralytics](ultralytics-yolo.md) library
  back-catalog (`RT-DETR` alongside YOLO/SAM/NAS), so it runs through the same
  `YOLO(...)`-style API and export path ([Ultralytics GitHub](../sources/ultralytics-github.md)).

## Related

- [Ultralytics YOLO](ultralytics-yolo.md) — the CNN family RT-DETR is benchmarked against (and is co-distributed with).
- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md) — RT-DETR sits at that page's "hybrid CNN-Transformer" frontier.
- [YOLO version lineage](../syntheses/vision/yolo-version-lineage.md) — where RT-DETR/DEIM appear as the transformer cross-comparisons.

## Open questions

- **No primary RT-DETR source is ingested** — this page is grounded in the YOLO
  sources that *benchmark against* it, not the RT-DETR paper itself. Ingesting
  arXiv:2304.08069 would upgrade the architecture claims from "per survey" to
  first-party.
- No **edge/Jetson** RT-DETR-vs-YOLO latency numbers in the wiki (same gap noted
  for YOLO26 on [Ultralytics YOLO](ultralytics-yolo.md)).

## Mentioned in

- [YOLOv10 (Wang et al. 2024)](../sources/yolov10-nms-free-2024.md) — RT-DETR-R18 as the transformer baseline.
- [Terven & Cordova-Esparza 2023](../sources/terven-yolo-survey-2023.md) — covers RT-DETR as "YOLO with Transformers."
- [Sapkota & Karkee 2025](../sources/sapkota-ultralytics-yolo-evolution-2025.md) — YOLO26 vs RT-DETR / DEIM cross-comparison.
- [Ultralytics YOLO (GitHub)](../sources/ultralytics-github.md) — RT-DETR in the library back-catalog.
