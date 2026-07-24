---
title: Ultralytics YOLO
type: entity
subtype: software-library
created: 2026-06-14
updated: 2026-07-23
sources: 11
tags: [ultralytics, yolo, object-detection, segmentation, pose-estimation, computer-vision, edge-ai, pytorch, agpl]
---

# Ultralytics YOLO

**Ultralytics YOLO** — the Python library (`pip install ultralytics`) and model family that is the de-facto standard for real-time computer vision. A single `YOLO(...)` class + `yolo` CLI cover **detection, instance segmentation, classification, pose estimation, OBB, and tracking**, with one-line train / val / predict / export. Maintained by **Ultralytics**; 58k★; **AGPL-3.0 or paid Enterprise License**.

## Why it matters in this wiki

It is the **perception workhorse** that shows up across the wiki's edge-robotics stacks: the upstream of the [jetson-examples](jetson-examples.md) `ultralytics-yolo` / `yolo11` / `yolo26` / `yolov10` recipes, and the detector behind Hailo-NPU and Jetson vision demos. Where the wiki's VLA/world-model work is the "learned policy" layer, YOLO is the commodity "what/where is the object" layer — pretrained, export-to-edge, and trivially fine-tunable. Its **AGPL license** is a recurring deployment caveat for any closed/commercial robot product.

## Key facts

- **Install / use:** `pip install ultralytics`; `from ultralytics import YOLO; YOLO("yolo26n.pt")`; or `yolo predict model=yolo26n.pt source=...`.
- **Current flagship:** **YOLO26** (n/s/m/l/x). Back-catalog in-repo: YOLOv3/v5/v6/v8/v9/v10/11/12/26, **[RT-DETR](rt-detr.md)**, **SAM** + **FastSAM**, **[YOLO-NAS](yolo-nas.md)**.
- **Tasks:** Detect, Segment (instance), Classify, Pose, OBB; **Track** on top of detect/segment/pose.
- **Pretrained on:** COCO (detect/segment/pose/OBB), ImageNet (classify) — auto-downloaded.
- **Export:** ONNX, TensorRT (Jetson edge path), CoreML, TFLite, OpenVINO, etc.
- **License:** **AGPL-3.0** (copyleft) or Enterprise License for commercial use.
- **Repo:** ultralytics/ultralytics — Python; created 2022-09-11; updated daily.

## Lineage (v1 → v26)

Ultralytics did **not** author the original YOLO — the paradigm was founded by
[Redmon et al. 2016](../sources/yolo-you-only-look-once-2016.md) (grid-regression,
one-pass detection). Ultralytics' contribution is **v5's modular PyTorch
foundation** and the sustained engineering that turned YOLO from a research model
into the de-facto library. The line since: anchor-free + decoupled head (v8) →
efficiency modules (v11) → **NMS-free end-to-end** ([YOLOv10](../sources/yolov10-nms-free-2024.md),
now default in **YOLO26** with STAL/ProgLoss/MuSGD,
[Sapkota & Karkee 2025](../sources/sapkota-ultralytics-yolo-evolution-2025.md)).
Full version-by-version diff: [YOLO version lineage](../syntheses/vision/yolo-version-lineage.md).
The paradigm itself: [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md).

## Related

- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md) — the paradigm YOLO belongs to.
- [jetson-examples](jetson-examples.md) — one-command YOLO recipes for Jetson.
- [jetson-containers](jetson-containers.md) — container substrate those recipes build on.
- [Jetson Orin Nano](jetson-orin-nano.md) — typical TensorRT edge-inference target.
- [TrackNet](tracknet.md) — where YOLO **loses**: on shuttlecock tracking a YOLOv7 baseline scores **68.0 F1** vs TrackNetV3's **97.5**, because balls 2–12 px across defeat box regression. A useful boundary marker on YOLO's applicability.

## Open questions

- YOLO26-vs-YOLO11 accuracy/latency on Jetson-class hardware (no edge benchmarks in README).
- AGPL applicability to fielded onboard-robot inference (distribution boundary).

## Mentioned in

- [YOLO: You Only Look Once (Redmon et al. 2016)](../sources/yolo-you-only-look-once-2016.md) — the founding paper of the paradigm.
- [YOLOv10 (Wang et al. 2024)](../sources/yolov10-nms-free-2024.md) — NMS-free end-to-end detection.
- [Terven & Cordova-Esparza 2023](../sources/terven-yolo-survey-2023.md) — survey v1→v8/NAS.
- [Kotthapalli et al. 2025](../sources/kotthapalli-yolo-survey-2025.md) — survey through v11 + multi-task.
- [Sapkota & Karkee 2025](../sources/sapkota-ultralytics-yolo-evolution-2025.md) — overview anchored on YOLO26.
- [Ultralytics YOLO (GitHub)](../sources/ultralytics-github.md) — primary repo ingest.
- [Seeed jetson-examples (repo + reComputer runner)](../sources/seeed-jetson-examples.md) — `ultralytics-yolo` / `yolo11` / `yolo26` / `yolov10` recipes.
- [Enhancing YOLOv11n for Reliable Child Detection (PTIT 2026)](../sources/ptit-yolov11n-child-detection.md) — YOLOv11n fine-tuned from Ultralytics COCO weights + [SAHI](../concepts/robotics/sahi-slicing-inference.md) for small-object recall on edge CCTV.
- [TrackNetV4 (Raj et al. 2024)](../sources/tracknetv4-motion-attention-2024.md) — uses **YOLOv7** as the bounding-box baseline that [heatmap localization](../concepts/robotics/heatmap-object-localization.md) outperforms by ~30 F1 on tiny fast objects.
- [TrackNet (Huang et al. 2019)](../sources/tracknet-huang-2019.md) — cites the YOLO family as the fast one-stage alternative it deliberately rejects for tiny-object tracking.
