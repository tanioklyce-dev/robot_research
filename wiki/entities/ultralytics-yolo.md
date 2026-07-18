---
title: Ultralytics YOLO
type: entity
subtype: software-library
created: 2026-06-14
updated: 2026-07-17
sources: 3
tags: [ultralytics, yolo, object-detection, segmentation, pose-estimation, computer-vision, edge-ai, pytorch, agpl]
---

# Ultralytics YOLO

**Ultralytics YOLO** — the Python library (`pip install ultralytics`) and model family that is the de-facto standard for real-time computer vision. A single `YOLO(...)` class + `yolo` CLI cover **detection, instance segmentation, classification, pose estimation, OBB, and tracking**, with one-line train / val / predict / export. Maintained by **Ultralytics**; 58k★; **AGPL-3.0 or paid Enterprise License**.

## Why it matters in this wiki

It is the **perception workhorse** that shows up across the wiki's edge-robotics stacks: the upstream of the [jetson-examples](jetson-examples.md) `ultralytics-yolo` / `yolo11` / `yolo26` / `yolov10` recipes, and the detector behind Hailo-NPU and Jetson vision demos. Where the wiki's VLA/world-model work is the "learned policy" layer, YOLO is the commodity "what/where is the object" layer — pretrained, export-to-edge, and trivially fine-tunable. Its **AGPL license** is a recurring deployment caveat for any closed/commercial robot product.

## Key facts

- **Install / use:** `pip install ultralytics`; `from ultralytics import YOLO; YOLO("yolo26n.pt")`; or `yolo predict model=yolo26n.pt source=...`.
- **Current flagship:** **YOLO26** (n/s/m/l/x). Back-catalog in-repo: YOLOv3/v5/v6/v8/v9/v10/11/12/26, **RT-DETR**, **SAM** + **FastSAM**, **YOLO-NAS**.
- **Tasks:** Detect, Segment (instance), Classify, Pose, OBB; **Track** on top of detect/segment/pose.
- **Pretrained on:** COCO (detect/segment/pose/OBB), ImageNet (classify) — auto-downloaded.
- **Export:** ONNX, TensorRT (Jetson edge path), CoreML, TFLite, OpenVINO, etc.
- **License:** **AGPL-3.0** (copyleft) or Enterprise License for commercial use.
- **Repo:** ultralytics/ultralytics — Python; created 2022-09-11; updated daily.

## Related

- [jetson-examples](jetson-examples.md) — one-command YOLO recipes for Jetson.
- [jetson-containers](jetson-containers.md) — container substrate those recipes build on.
- [Jetson Orin Nano](jetson-orin-nano.md) — typical TensorRT edge-inference target.

## Open questions

- YOLO26-vs-YOLO11 accuracy/latency on Jetson-class hardware (no edge benchmarks in README).
- AGPL applicability to fielded onboard-robot inference (distribution boundary).

## Mentioned in

- [Ultralytics YOLO (GitHub)](../sources/ultralytics-github.md) — primary repo ingest.
- [Seeed jetson-examples (repo + reComputer runner)](../sources/seeed-jetson-examples.md) — `ultralytics-yolo` / `yolo11` / `yolo26` / `yolov10` recipes.
- [Enhancing YOLOv11n for Reliable Child Detection (PTIT 2026)](../sources/ptit-yolov11n-child-detection.md) — YOLOv11n fine-tuned from Ultralytics COCO weights + [SAHI](../concepts/robotics/sahi-slicing-inference.md) for small-object recall on edge CCTV.
