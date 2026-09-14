---
title: RKNN-Toolkit2 (Rockchip NPU SDK)
type: entity
subtype: software
created: 2026-09-13
updated: 2026-09-13
sources: 6
tags: [rknn, rknn-toolkit2, rockchip, npu, toolchain, model-conversion, quantization, onnx, proprietary-license, edge-ai, rk3588, rk3576, rk3566]
---

# RKNN-Toolkit2

The SDK through which a [Rockchip](rockchip.md) NPU is programmed: convert a trained PyTorch / ONNX / TensorFlow / Caffe / Darknet model **on a PC** into a `.rknn` graph (quantised, fused, laid out for the NPU), then run it on the board through the **RKNN Runtime** (`librknnrt.so`, C/C++) or **Toolkit-Lite2** (Python). The only open-source component is the RKNPU kernel driver in Rockchip's kernel tree; the SDK itself is under Rockchip's proprietary "RKNN SDK License," restricted to applications for Rockchip products ([repo](../sources/rknn-toolkit2-github.md)).

## What it covers, and what it doesn't

- **Platforms**: RK3588, RK3576, RK3566/68, RK3562, RV1103/1106 (+B), RV1126B, RK2118. Not the older RK1808 / RV1126 / RK3399Pro line (Toolkit v1, incompatible) and not the [RK1828](rockchip-rk1828.md) LLM coprocessor (a different "RKNN3" toolchain per its ODM).
- **Not LLMs**: the README redirects language models to the separate **[RKLLM](rknn-llm.md)** SDK (`rknn-llm`), which is where Rockchip's active development is (v1.3.0 June 2026 vs this repo's July 2025) and which now carries a [measured benchmark table](../sources/rknn-llm-github.md); a multimodal model uses *both* — vision encoder here, language model there.
- **Operator coverage is the whole question.** 89 of 187 ONNX ops; `Softmax`/`Slice`/`Tile` at batch 1 only; `GroupNormalization`, `Einsum`, `TopK`, `NonMaxSuppression`, `GridSample`, `Loop` **unsupported**. Read against the wiki's [LeRobot](lerobot.md) policies: **ACT plausibly converts, Diffusion Policy is blocked by GroupNorm as exported, VLA-class models are out of scope** ([source page](../sources/rknn-toolkit2-github.md) has the table).
- **NPU generations differ under one SDK**: Flash Attention only on RK3562/RK3576, W4A16 only on RK3576 — the **RK3576**, not the higher-TOPS [RK3588](rockchip-rk3588.md), is the transformer-friendly part.
- **Developer loop**: PC-side simulator and accuracy analysis, board-in-the-loop via `rknn_server` over adb (USB or Ethernet), with a documented **WSL** workflow; Toolkit2 wheels for x86_64 *and* arm64 (so conversion can run on the RK3588 itself); Docker image; `rknn_benchmark`, `rknn_zero_copy`, `rknn_matmul_api_demo` examples in `rknpu2/`.
- **Support**: Redmine by arrangement with sales / FAE, QQ groups (three of four full), 464 open GitHub issues.

## The model zoo

[`rknn_model_zoo`](../sources/rknn-model-zoo-github.md) (Apache-2.0, 2,751★, v2.3.2 in step with the toolkit) is where the toolkit's operator list becomes 28 runnable models and one **per-platform execution-only fps table**. Detection (yolov5–yolo11, YOLOX, PP-YOLOE, YOLO-World), segmentation (incl. MobileSAM), pose, OCR, CLIP, and a speech stack (wav2vec2, Whisper, Zipformer, YAMNet, MMS-TTS). Two things to know before using it: the YOLO models are **Rockchip-modified forks** (sigmoid in-graph, fixed shape; running the official structure is "not recommended"), and the table is **single-core** for the RK3588 / RK3576 with pre/post-processing excluded. Headline rows: YOLOv8n INT8 640² **73.5 fps on one RK3588 core / 90.2 on one RK3576 core / 34.0 on the RK3566**; Whisper-base RTF 0.215 on the RK3588.

## Compared with the wiki's other NPU toolchains

| | RKNN-Toolkit2 | [Hailo](hailo.md) Dataflow Compiler → HEF | TensorRT (Jetson GPU / DLA) |
|---|---|---|---|
| Compile where | PC (x86_64 or arm64) | x86 host | on the target or a host |
| Runs arbitrary PyTorch? | No — op list | No — op list | Mostly, via CUDA fallback |
| LLM path | separate `rknn-llm` | Hailo-10H only, via `hailo-apps` | native |
| License | proprietary, Rockchip-products-only | proprietary | proprietary, NVIDIA-only |
| Shipped robot here | [Microduck](microduck.md) (RK3566, `yolo11n`) | none | ROSOrin / XLeRobot Jetson builds |

The pattern the [edge-SoC page](../concepts/robotics/heterogeneous-edge-soc.md) states — an NPU runs *compiled* models and its headline number measures the middle of a pipeline — is what this repo's operator list and `rknn_zero_copy` example are the concrete form of.

## Related
- [Rockchip](rockchip.md) · [Rockchip RK3588](rockchip-rk3588.md) · [Microduck](microduck.md)
- [Hailo](hailo.md) — the parallel compiled-model toolchain.
- [JetPack](jetpack.md) — the CUDA path's SDK bundle, for cadence comparison.
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md)

## Mentioned in
- [airockchip/rknn-toolkit2](../sources/rknn-toolkit2-github.md)
- [RK3588 Architecture Deep Dive (Turing Pi)](../sources/turingpi-rk3588-architecture-deep-dive.md) — the conversion / core-mask / memory-import workflow as used
- [`pollen-robotics/microduck` — the onboard runtime](../sources/microduck-runtime-repo.md) — RKNN in a shipped robot
- [RK1828 vs Jetson Orin NX vs Hailo-8 (Geniatech)](../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md) — names "RKNN3" for the RK1828
- [airockchip/rknn-llm](../sources/rknn-llm-github.md) — the sibling SDK; its vision encoders run through this one
- [airockchip/rknn_model_zoo](../sources/rknn-model-zoo-github.md) — the examples and benchmark table
