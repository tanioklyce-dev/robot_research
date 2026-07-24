---
title: Ultralytics YOLO (GitHub)
type: source
url: https://github.com/ultralytics/ultralytics
author: Ultralytics
published: 2022-09-11
ingested: 2026-06-14
local_path: null
venue: GitHub (ultralytics/ultralytics)
license: AGPL-3.0 (or paid Enterprise License)
format: GitHub repository (Python package + README)
tags: [ultralytics, yolo, object-detection, segmentation, pose-estimation, computer-vision, edge-ai, pytorch, onnx, tensorrt, agpl]
---

## Summary

**Ultralytics** is the Python package (`pip install ultralytics`) and repo behind the modern **YOLO** family — the de-facto, batteries-included library for real-time computer vision. A single `YOLO(...)` class loads a pretrained checkpoint and runs **detection, instance segmentation, classification, pose estimation, oriented-bounding-box (OBB) detection, and multi-object tracking** from either Python or the `yolo` CLI, with one-line training, validation, prediction, and export to deployment formats (ONNX, TensorRT, etc.). It is enormously popular (58k★, 11k forks; created 2022-09-11, updated daily) and is the upstream behind the [jetson-examples](seeed-jetson-examples.md) `ultralytics-yolo` / `yolo11` / `yolo26` / `yolov10` recipes. **License is AGPL-3.0** (strong copyleft) with a paid **Enterprise License** escape hatch — the key gotcha for any closed-source / commercial robotics deployment.

## Key claims

- **Install + minimal use:**
  ```bash
  pip install ultralytics
  yolo predict model=yolo26n.pt source='https://ultralytics.com/images/bus.jpg'   # CLI
  ```
  ```python
  from ultralytics import YOLO
  model = YOLO("yolo26n.pt")        # load pretrained
  results = model("image.jpg")       # predict
  ```
- **Current flagship: YOLO26** (n/s/m/l/x size variants). The repo ships a deep back-catalog of model families under `ultralytics/cfg/models/`: **YOLOv3, v5, v6, v8, v9, v10, 11, 12, 26**, plus **[RT-DETR](../entities/rt-detr.md)** (real-time transformer detector). Additional model classes under `ultralytics/models/`: **SAM** (Segment Anything) + **FastSAM**, and **YOLO-NAS**. (Newer families drop the "v" prefix: 11/12/26.)
- **Tasks:** Detect, Segment (instance), Classify, Pose, OBB; **Track** mode layers on top of detect/segment/pose models. *(The README's mention of "semantic segmentation / Cityscapes" does not match Ultralytics' actual task set — instance segmentation on COCO is the segmentation task; treat that line as an error.)*
- **Pretrained weights:** COCO (detect / segment / pose / OBB), ImageNet (classify) — auto-downloaded by checkpoint name.
- **Export / deployment:** ONNX and TensorRT are highlighted; the Ultralytics export pipeline broadly targets edge/server runtimes (ONNX, TensorRT, CoreML, TFLite, OpenVINO, etc.). TensorRT export is the relevant path for [Jetson](../entities/jetson-orin-nano.md) edge inference.
- **Integrations:** Weights & Biases, Comet ML, Roboflow, Intel OpenVINO.
- **License:** **AGPL-3.0** for open-source/research use; separate **Enterprise License** required for commercial/closed products.

## Entities mentioned

- [Ultralytics YOLO](../entities/ultralytics-yolo.md) (this library/model family)
- [jetson-examples / reComputer runner](../entities/jetson-examples.md) — packages YOLO recipes for Jetson
- [Jetson Orin Nano](../entities/jetson-orin-nano.md) — typical edge inference target (via TensorRT export)

## Concepts touched

- **Real-time object detection / segmentation / pose** as a commodity: pretrained weights + one-line train/predict/export.
- **Edge deployment via export** — PyTorch → ONNX/TensorRT for Jetson and other accelerators; the CV counterpart to the LLM/VLM container recipes in [jetson-examples](seeed-jetson-examples.md).
- **AGPL copyleft as a deployment constraint** — relevant to any robot product shipping YOLO without an enterprise license.

## Open questions

- YOLO26 vs YOLO11 accuracy/latency tradeoffs on Jetson-class hardware — the README doesn't give edge benchmarks; the per-recipe tier question carries over from [jetson-examples](seeed-jetson-examples.md).
- How the AGPL terms interact with onboard-robot deployments (is running YOLO on a fielded robot "distribution"?) — a real licensing question for any of the wiki's edge-robot projects.
