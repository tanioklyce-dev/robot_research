---
title: "airockchip/rknn-toolkit2 — README, changelog, operator-support list, license"
type: source
url: https://github.com/airockchip/rknn-toolkit2/
local_path: raw/2026-09-13-rknn-toolkit2-readme-changelog-opsupport-license.md
sha256: ac3c7b70ba6d16f03f4757deffd42cef985900ac58271fc2079b25e238bfbb51
author: Rockchip Electronics Co., Ltd.
published: 2023-09-25
ingested: 2026-09-13
venue: "GitHub; the SDK the Rockchip NPU is programmed through"
format: repository README + CHANGELOG + doc/RKNNToolKit2_OP_Support-2.3.2.md + LICENSE, plus API metadata
github_stats: "3,367 stars, 395 forks, 464 open issues, created 2023-09-25, pushed 2025-07-29, latest release v2.3.2 (2025-04-09) (captured 2026-09-13)"
tags: [rknn, rknn-toolkit2, rockchip, npu, rk3588, rk3576, rk3566, onnx, quantization, model-conversion, edge-ai, toolchain, proprietary-license, github]
---

# airockchip/rknn-toolkit2

## Summary

The public home of **[RKNN-Toolkit2](../entities/rknn-toolkit2.md)**, the software stack through which every Rockchip NPU in this wiki — the [RK3588](../entities/rockchip-rk3588.md)'s three-core unit, the RK3566 under [Microduck](../entities/microduck.md) — is actually used. The README states the model in one sentence: *"users need to first run the RKNN-Toolkit2 tool on the computer, convert the trained model into an RKNN format model, and then inference on the development board using the RKNN C API or Python API."* Four components: the **Toolkit2** converter / quantiser / simulator on a PC, **Toolkit-Lite2** (Python on the board), the **RKNN Runtime** (`librknnrt.so`, C/C++ on the board), and the **RKNPU kernel driver**, which is the only open-source piece and lives in Rockchip's kernel tree. Three facts matter for this wiki. **The operator-support list is the exportability oracle**: 89 of 187 ONNX operators are supported, with `Softmax`, `Slice` and `Tile` restricted to **batch size 1**, and `GroupNormalization`, `Einsum`, `TopK`, `NonMaxSuppression`, `GridSample`, `Loop` and `Neg` all **Not Supported** — which already sorts the wiki's [LeRobot](../entities/lerobot.md) policies into likely-convertible (ACT), blocked-as-exported (Diffusion Policy's GroupNorm UNet), and out-of-scope (anything VLA-sized, which the README redirects to the separate **rknn-llm** SDK). **The license is not open source**: the SDK is Rockchip's proprietary agreement, granted "solely for the design, development and testing of applications that are compatible with Products … of Rockchip." And **the repo is quiet**: last push July 2025, last release April 2025, 464 open issues, while the sibling `rknn-llm` was pushed in June 2026. Also notable: the NPU-generation split the changelog exposes — Flash Attention only on RK3562/RK3576, W4A16 only on RK3576 — meaning the RK3588 is *not* the best Rockchip transformer target despite the highest TOPS.

## Key claims

### The stack (README)
- Convert on PC → run on board. Toolkit2 does conversion, quantisation, **accuracy analysis** and **simulator inference on the PC**, and board-in-the-loop inference through `rknn_server` over adb (USB or Ethernet) — documented for **WSL** hosts in `doc/Using RKNN-ToolKit2 in WSL.md`.
- Toolkit2 is **"not compatible with RKNN-Toolkit"** (v1, for RK1808 / RV1109 / RV1126 / RK3399Pro — separate repos).
- **Supported platforms**: RK3588, RK3576, RK3566/RK3568, RK3562, RV1103/RV1106, RV1103B/RV1106B, RV1126B, RK2118. **The [RK1828](../entities/rockchip-rk1828.md) is not listed.**
- Python 3.6–3.12; wheels for **x86_64 and arm64** (arm64 since v2.3.0, so conversion can run on the RK3588 itself); Toolkit-Lite2 pip-installable since v2.3.0; a Docker image; the full SDK also distributed via a Chinese file-share with a fetch code.
- **LLMs are elsewhere**: "If you want to deploy LLM (Large Language Model), we have introduced a new SDK called RKNN-LLM" (`airockchip/rknn-llm`: 1,674 stars, pushed 2026-06-17). Examples for vision live in `rknn_model_zoo` (2,751 stars, pushed 2025-04-09).
- Support channels: Rockchip's Redmine (account via sales/FAE) and four QQ groups, three of them full.

### Changelog highlights
| Version | Date | What it tells you |
|---|---|---|
| v1.6.0 | 2023 | ONNX opset 12–19; custom CPU/GPU operators; "improve transformer support"; RK3588 gains int4×int4→int16 MatMul |
| v2.0.0-beta0 | 2024-03-25 | RK3576 + RK2118 (beta); **SDPA** for transformers; PyTorch 2.1; QAT models |
| v2.1.0 | 2024-08-08 | **Flash Attention — only RK3562 and RK3576**; int32/int64 |
| v2.2.0 | 2024-09-18 | pip install; Python 3.12; "optimize transformer model performance" |
| v2.3.0 | 2024-11-11 | Toolkit2 on ARM64; Lite2 via pip; **W4A16 symmetric quantisation (RK3576 only)**; LayerNorm / LSTM / MatMul optimisation |
| v2.3.2 | 2025-04-09 | RV1126B; einsum and Norm improvements; **automatic mixed precision**; graph-optimisation |

### Operator support (doc/RKNNToolKit2_OP_Support-2.3.2.md)
- ONNX table: **89 supported / 187 listed**. Supported with restrictions: `Softmax` (batch 1), `Slice` (batch 1), `Tile` (batch 1, no broadcast), `Resize` (nearest / bilinear only), `RoiAlign` (average, batch 1), `GRU` (batch 1), `If` (constant input only).
- Supported and relevant to policies: `Conv`, `ConvTranspose`, `MatMul`, `Gemm`, `LayerNormalization`, `InstanceNormalization`, `BatchNormalization`, `Gelu`-via-`Erf`, `Mish`, `HardSwish`, `Sigmoid`/`Tanh`, `Where`, `ScatterND`, `Gather`/`GatherElements`, `Sin`/`Cos`, `Expand`, `Pad`, `LSTM`.
- **Not Supported**: `GroupNormalization`, `Einsum`, `TopK`, `NonMaxSuppression`, `GridSample`, `DeformConv`, `CumSum`, `Range`, `Loop`, `Scan`, `Neg`, `Not`, `Round`, `Sign`, `Trilu`, `GatherND`, the trig/hyperbolic family beyond sin/cos, `MatMulInteger`, `DynamicQuantizeLinear`.
- PyTorch table (210 rows, TorchScript `aten::` ops, PyTorch > 1.6): `aten::layer_norm`, `aten::gelu`, `aten::silu`, `aten::mish`, `aten::matmul`, `aten::bmm`, `aten::linear`, `aten::embedding`, `aten::softmax` supported; **`aten::sin` / `aten::cos` not supported** through this path (they are through ONNX), `adaptive_avg_pool1d` not supported. Caffe, TensorFlow and Darknet tables also present.

### License
- **"RKNN SDK License"**, Rockchip proprietary: a royalty-free right to use, modify and redistribute derivatives *"solely for the design, development and testing of applications that are compatible with Products of Rockchip or its affiliates."* GitHub shows it as "Other" / no SPDX id. Not OSI open source; the kernel driver is the exception (in-tree, Rockchip kernel).

### Repository shape
- `rknn-toolkit2/` (packages x86_64 + arm64, docker, examples, doc), `rknn-toolkit-lite2/`, `rknpu2/` (runtime `librknn_api` + `rknn_server` for Linux and Android; examples incl. `rknn_yolov5_demo`, `rknn_matmul_api_demo`, `rknn_zero_copy`, `rknn_dynamic_shape_input_demo`, `rknn_internal_mem_reuse_demo`, `rknn_custom_op_demo`), `autosparsity/`, `doc/` (Quick Start, User Guide, API references, compiler operator list — as PDFs up to 68 MB, CN + EN).

## What this settles for the wiki

**The RKNN twin of the Hailo-HEF question now has a paper answer, pending a real export.** Reading the operator table against the [LeRobot](../entities/lerobot.md) policies the wiki deploys:

| Policy | Ops it needs | Verdict from the list |
|---|---|---|
| **ACT** | ResNet-18 conv/BN/ReLU/MaxPool; transformer MatMul + Softmax + LayerNorm + ReLU/GELU; constant sinusoidal embeddings | **Plausibly convertible at batch 1.** Nothing it needs is in the Not-Supported column. Latency unknown. |
| **Diffusion Policy** | 1D conditional UNet: Conv1d, **GroupNorm**, Mish, FiLM (Mul/Add); N denoising steps driven from the host | **Blocked as exported** — `GroupNormalization` is Not Supported. A decomposed export (reshape + InstanceNorm) might pass; each denoising step is a separate NPU call. |
| **SmolVLA / π0-class** | VLM backbone with KV cache, RoPE, dynamic shapes; flow-matching head | **Out of scope for Toolkit2** — the README sends LLMs to `rknn-llm`; `Einsum`, `TopK`, `Loop` unsupported; `Softmax` batch-1 only. |

Two structural notes follow. The **RK3576, not the RK3588, is Rockchip's transformer part** on this evidence (Flash Attention, W4A16), so a Rockchip-based robot brain for VLA-class models would not be the board the [Turing Pi article](turingpi-rk3588-architecture-deep-dive.md) benchmarked. And **the toolchain is where the vendor lock lives**, not the silicon: proprietary SDK, support via Redmine-by-sales and QQ, last release seventeen months before capture — the mirror image of the [JetPack](../entities/jetpack.md) cadence the wiki tracks for the CUDA path.

## Entities mentioned
- [RKNN-Toolkit2](../entities/rknn-toolkit2.md) (new) · [Rockchip](../entities/rockchip.md) · [Rockchip RK3588](../entities/rockchip-rk3588.md) · [Rockchip RK1828](../entities/rockchip-rk1828.md) (absent from the list).
- [Microduck](../entities/microduck.md) — the wiki's shipped RKNN user (RK3566).
- [Hailo](../entities/hailo.md) — the comparable compiled-model toolchain (HEF).
- [LeRobot](../entities/lerobot.md) — the policies the table is read against.

## Concepts touched
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md) — the compiled-model fact, now with the operator list behind it.
- [VLA models](../concepts/learning/vla-models.md) · [Imitation learning](../concepts/learning/imitation-learning.md) — ACT / Diffusion Policy exportability.
- [Low-rank adaptation](../concepts/learning/low-rank-adaptation.md) is *not* touched — no PEFT story; conversion is post-training only.

## Open questions
- Actually export ACT to `.rknn` and run it on an RK3588 with `rknn_benchmark` — the cheapest test of the table above (filed in the [backlog](../backlog.md)).
- Does a decomposed GroupNorm export of Diffusion Policy convert, and what does the per-step latency come to over 10–100 steps?
- What `rknn-llm` supports in June 2026 (models, quant, tokens/s per SoC) — the wiki has only its star count.
- Is the RK1828's "RKNN3" a successor to this repo or a separate RISC-V-hosted stack?
- Why is the repo quiet since July 2025 while `rknn-llm` is active — has development moved to a private tree with GitHub as a release mirror?
