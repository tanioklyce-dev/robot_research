---
title: "airockchip/rknn_model_zoo — README, per-platform NPU benchmark table, FAQ, license"
type: source
url: https://github.com/airockchip/rknn_model_zoo
local_path: raw/2026-09-13-rknn-model-zoo-readme-faq-license.md
sha256: a9fa21a1c7fef4240883c9c1118fd19883c4aa04d9901d34e9426175bb74b8c8
author: Rockchip Electronics Co., Ltd.
published: 2022-02-15
ingested: 2026-09-13
venue: "GitHub; the reference examples and benchmark table for the Rockchip NPU (RKNN-Toolkit2)"
format: repository README + FAQ + yolov8 example README + LICENSE, plus API metadata
github_stats: "2,751 stars, 469 forks, 338 open issues, Apache-2.0, created 2022-02-15, pushed 2025-04-09, latest release v2.3.2 (2025-04-09) (captured 2026-09-13)"
tags: [rknn, rknn-model-zoo, rockchip, npu, benchmark, yolo, clip, whisper, rk3588, rk3576, rk3566, edge-ai, computer-vision, speech, apache-2, github]
---

# airockchip/rknn_model_zoo

## Summary

The reference examples for [RKNN-Toolkit2](../entities/rknn-toolkit2.md): 28 deployable models with export scripts, C and Python demos, and one **benchmark table giving execution-only fps for every model on every Rockchip NPU** — RK3566/3568, RK3562, RK3588 (single core), RK3576 (single core), and the older RV1109/RV1126/RK1808. It is the primary behind the model-zoo figures the [Turing Pi article](turingpi-rk3588-architecture-deep-dive.md) quoted, **and reading it shows that article copied the wrong column**: its "RK3588 single-core" numbers (467.0 / 99.0 / 90.2 fps) are the zoo's **RK3576** column; the RK3588 column reads **450.7 / 110.1 / 73.5**, and the repo has not changed since April 2025. Two other things the table settles. **The RK3576's single NPU core out-runs the RK3588's on most CNN detectors** (YOLOv8n 90.2 vs 73.5, yolo11n 77.9 vs 60.0) — the newer NPU generation, consistent with the toolkit's Flash-Attention / W4A16 support landing there first — while the RK3588 wins on ResNet-50, CLIP-text and the lite-transformer, and still has three cores to the RK3576's two. And **the zoo carries a whole speech stack for the NPU**: Whisper-base at real-time factor 0.215, streaming Zipformer ASR at 0.065, MMS-TTS at 0.069, YAMNet at 0.004 on one RK3588 core — the voice loop of an onboard agent, measured. Also: the YOLO models are **structurally modified** Rockchip forks (sigmoid moved into the graph, fixed shapes); the repo is **Apache-2.0**, unlike the toolkit it depends on; there is **no multi-core RK3588 number anywhere**; and the RK3566 column lets the wiki cross-check [Microduck](../entities/microduck.md)'s own detector measurement, which it passes.

## Key claims

### Scope
- Platforms: RK3562 / RK3566 / RK3568 / RK3576 / RK3588 / RV1126B fully; RV1103 / RV1106 limited (memory); RV1109 / RV1126 / RK1808 via the older RKNPU1 SDK. Versions track toolkit2 (v2.3.2 requires RKNPU2 SDK ≥ 2.3.2).
- 28 example directories: detection **yolov5 / v6 / v7 / v8 / v10 / yolo11 / yolox / ppyoloe / yolo_world** (open-vocabulary, with a CLIP text encoder), segmentation **deeplabv3 / yolov5-seg / yolov8-seg / ppseg / mobilesam**, **yolov8-pose**, yolov8-obb, RetinaFace, LPRNet, PPOCR det + rec, lite_transformer (NMT), **CLIP** ViT-B/32, speech **wav2vec2 / whisper / zipformer / yamnet**, TTS **mms_tts**.
- FAQ 1.9: *"Is there a LLM model demo? Not provided now"* — LLMs live in [rknn-llm](rknn-llm-github.md).
- License: **Apache-2.0** for the zoo itself; it converts through the proprietary-licensed toolkit.

### The YOLO models are not the official YOLO models
- yolov8 README: *"The model provided here is an optimized model, which is different from the official original model."* Sources are Rockchip forks (`airockchip/yolov5`, `airockchip/ultralytics_yolov8`, `airockchip/ultralytics_yolo11`, `airockchip/YOLOX`).
- FAQ 3.5, *can the NPU run YOLO unmodified?* — **"Yes, but not recommended"**: the modification exists *"based on accuracy and performance considerations. Maintaining the original model structure may lead to poor quantification accuracy and worse inference performance."*
- FAQ 3.1 / 3.2: the demo post-processing **requires the class-confidence output to come from a sigmoid op** in the graph; a missing sigmoid gives confidences > 1 and box floods. FAQ 3.4: zoo mAP is below official because the zoo uses **fixed-shape** models and **INT8 quantisation**, and even the image reader (cv2 vs stbi) moves the number.
- Practical consequence: an [Ultralytics](../entities/ultralytics-yolo.md) checkpoint is not dropped in; it is re-exported through Rockchip's fork, and the CPU post-processing (decode + NMS, since `NonMaxSuppression` is [unsupported on the NPU](rknn-toolkit2-github.md)) is part of the demo.

### Benchmark table — conditions
Max NPU frequency (`scaling_frequency.sh`); **`rknn.run` time only, no pre/post-processing**; C API (Python is slower); on RK3588 / RK3576 **bind the big CPU cores** for the test (FAQ 1.5); other processes sharing CPU / NPU / bandwidth reduce it.

### Benchmark table — selected rows (fps, INT8 unless noted)
| Model | Input | RK3566/68 | RK3562 | **RK3588 @1 core** | **RK3576 @1 core** |
|---|---|---|---|---|---|
| MobileNetV2 | 224² | 180.7 | 281.3 | **450.7** | 467.0 |
| ResNet-50 v2 | 224² | 37.9 | 54.9 | **110.1** | 99.0 |
| YOLOv5n / s | 640² | 39.7 / 19.3 | 47.4 / 23.6 | 82.5 / 48.4 | 112.7 / 57.5 |
| YOLOv6n | 640² | 48.8 | 56.4 | 106.4 | 109.1 |
| **YOLOv8n** / s / m | 640² | 34.0 / 15.1 / 6.5 | 40.9 / 18.4 / 8.2 | **73.5** / 38.0 / 16.2 | 90.2 / 40.8 / 16.7 |
| YOLOv8n-pose | 640² | 22.6 | 31.0 | 55.9 | 66.8 |
| YOLOv8n-seg | 640² | 27.8 | 33.0 | 60.8 | 71.1 |
| YOLOv10n | 640² | 20.7 | 34.1 | 61.2 | 80.2 |
| **yolo11n** / s / m | 640² | **20.6** / 10.2 / 4.6 | 34.0 / 16.7 / 6.5 | 60.0 / 33.0 / 12.7 | 77.9 / 38.2 / 14.6 |
| YOLO-World v2-s (open-vocab) | 640² | 7.4 | 9.6 | 22.1 | 22.3 |
| CLIP ViT-B/32 image (FP16) | 224² | 2.3 | 3.4 | 6.5 | 6.7 |
| CLIP text (FP16) | 20 tokens | 29.7 | 66.6 | 96.0 | 63.7 |
| MobileSAM encoder / decoder (FP16) | 448² / 112² | 1.0 / 24.3 | 6.6 / 69.6 | 10.0 / 116.4 | 11.9 / 108.6 |
| RetinaFace mobile | 320² | 156.4 | 300.8 | 227.2 | 470.5 |
| PPOCR v4 det / rec | 480² / 48×320 | 22.1 / 19.5 | 28.0 / 54.3 | 50.7 / 73.9 | 64.3 / 96.8 |

Speech and TTS, as real-time factor (lower is faster), FP16:
| Model | RK3566/68 | RK3562 | **RK3588** | **RK3576** |
|---|---|---|---|---|
| wav2vec2-base, 20 s | 0.817 | 0.323 | 0.133 | 0.073 |
| **Whisper-base, 20 s** | 1.178 | 0.420 | **0.215** | 0.218 |
| **Zipformer bilingual, streaming** | 0.196 | 0.116 | **0.065** | 0.082 |
| YAMNet, 3 s | 0.013 | 0.008 | 0.004 | 0.005 |
| **MMS-TTS eng, 200 tokens** | 0.311 | 0.138 | **0.069** | 0.069 |

## What this settles for the wiki

> [!warning] Contradiction — the Turing Pi article quotes the wrong column
> [Turing Pi's RK3588 deep dive](turingpi-rk3588-architecture-deep-dive.md) states "Rockchip's current single-core RK3588 model-zoo results include approximately **467.0** fps for INT8 MobileNetV2, **99.0** fps for INT8 ResNet-50, and **90.2** fps for INT8 YOLOv8n at 640×640," linking this table. Those three values are the **RK3576 @single_core** column, which sits immediately to the right of the RK3588 column. The RK3588 values are **450.7 / 110.1 / 73.5**. The repo's last push (2025-04-09) predates the article (2026-08-15), so the table the author saw is this one. The error does not affect the article's argument (its 8 + 6 + 5 ms pipeline example is hypothetical) but it had propagated to three wiki pages, now corrected. A reminder that "vendor-sourced" and "correctly transcribed" are separate checks.

- **RK3576 vs RK3588, per NPU core.** On 21 of the 28 CNN-detector rows the RK3576 core is faster; the RK3588 core wins on ResNet-50, CLIP-text, lite-transformer and the MobileSAM decoder. The RK3588 still has **three cores** (the RK3576 two) and roughly twice the memory bandwidth, and nothing in the zoo measures multi-core — so per-board throughput for independent streams likely favours the RK3588, and single-stream latency the RK3576. Both are inferences; the table only gives single-core.
- **Microduck's detector number is consistent with the zoo.** [Microduck](../entities/microduck.md) reports `yolo11n` at 320×320 on the RK3566 at **p50 25.7 ms including pre/post**; the zoo gives yolo11n at 640×640 on the same NPU at **20.6 fps ≈ 48.5 ms execution-only**. A quarter of the pixels at roughly a quarter of the execution time plus pre/post lands near 25 ms. The one shipped-robot NPU measurement in the wiki passes its cross-check.
- **A voice loop fits on the NPU.** Whisper-base at RTF 0.215 and MMS-TTS at 0.069 on one RK3588 core, with Zipformer for streaming ASR, means the [on-device agent](../syntheses/agents/on-device-and-on-robot-agents.md)'s speech in/out need not touch the CPU or the [RKLLM](rknn-llm-github.md) budget — though they *do* share the LPDDR path with everything else, per the [edge-SoC page](../concepts/robotics/heterogeneous-edge-soc.md).
- **Open-vocabulary detection on-NPU exists**: YOLO-World v2-s at 22 fps (single core) plus a CLIP text encoder at 96 fps gives a text-promptable detector on the robot; CLIP image at 6.5 fps is the slow half.
- **The RKNN path's vision column is now measured for the wiki's three Rockchip tiers**, which the [Hailo-vs-Jetson](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md) page's Hailo column still is not (no fps for any Hailo part on file).

## Entities mentioned
- [RKNN-Toolkit2](../entities/rknn-toolkit2.md) — the SDK it exercises; [RKLLM](../entities/rknn-llm.md) — where the LLM demos are.
- [Rockchip](../entities/rockchip.md) · [Rockchip RK3588](../entities/rockchip-rk3588.md) · [Microduck](../entities/microduck.md) (RK3566 cross-check) · [Turing Pi](../entities/turing-pi.md) (the column misread).
- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — modified forks; [Hailo](../entities/hailo.md) — the comparable model-zoo pattern.

## Concepts touched
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md) — fact 3's numbers, corrected.
- [Single-stage object detection](../concepts/robotics/single-stage-object-detection.md) — what the RKNN export changes in a YOLO head.
- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md) — FAQ 3.4's fixed-shape + INT8 mAP loss.

## Open questions
- **Multi-core RK3588 scaling** — absent from the table; the toolkit says three cores ≠ 3×, nobody says what it is.
- **Accuracy after INT8** per model — the FAQ admits a loss and offers hybrid / QAT quantisation, but publishes no mAP deltas.
- Whether a YOLO trained in stock Ultralytics can be re-exported through the Rockchip fork without retraining (the fork changes the head's export, not its weights — plausible, unverified here).
- End-to-end demo fps (with pre/post) for any row — the FAQ says it is scenario-dependent and never gives one.
