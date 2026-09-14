---
title: Rockchip
type: entity
subtype: company
created: 2026-09-13
updated: 2026-09-13
sources: 5
tags: [rockchip, soc, arm, npu, edge-ai, semiconductor, china]
---

# Rockchip

Chinese fabless ARM SoC vendor (Fuzhou) whose chips sit under a large share of the non-Raspberry-Pi single-board computers and compute modules — and, in this wiki, under two very different robots: the **RK3566** inside [Microduck](microduck.md) and the **[RK3588](rockchip-rk3588.md)** on the Turing RK1 / Orange Pi 5 / Radxa Rock 5 class of boards.

## Silicon in the wiki

| SoC | CPU | NPU | Seen in |
|---|---|---|---|
| **RK3566** | 4× Cortex-A55 | 1 core, **0.8 TOPS INT8** (measured `yolo11n`@320: p50 25.7 ms) | [Microduck](microduck.md), 1 GB RAM ([runtime repo](../sources/microduck-runtime-repo.md)) |
| **[RK3588](rockchip-rk3588.md)** | 4× A76 + 4× A55 | 3 cores, **6 TOPS**; ~21.5 GB/s LPDDR measured | Turing RK1 ([Turing Pi deep dive](../sources/turingpi-rk3588-architecture-deep-dive.md)) |
| **RK3576** | (not ingested) | the transformer-friendly generation: Flash Attention and W4A16 land here, not on the RK3588 ([rknn-toolkit2 changelog](../sources/rknn-toolkit2-github.md)) | — |
| **[RK1828](rockchip-rk1828.md)** / RK1820 | 3× RISC-V (coprocessor, not an SoC) | 20 TOPS INT8 with **5 GB / 2.5 GB on-package DRAM**, ~5 W, PCIe 2.0 ×1, "RKNN3" toolchain — vendor claims only | M.2 LLM cards ([Geniatech](../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md)) |

## The software stack that decides what the hardware does

Rockchip's accelerators are reached through vendor libraries rather than a general-purpose runtime, which is the whole reason the [Turing Pi article](../sources/turingpi-rk3588-architecture-deep-dive.md) exists:

- **[RKNN-Toolkit2](rknn-toolkit2.md) / RKNN runtime** — compile a PyTorch / TensorFlow / ONNX graph on a host (layout, fusion, quantisation), load the compiled model on device, choose NPU cores with a core mask. Operator coverage determines what maps to the NPU at all — the same **compiled-model** pattern as [Hailo](hailo.md)'s HEF. The [repo](../sources/rknn-toolkit2-github.md) shows the fine print: 89 of 187 ONNX ops, batch-1 restrictions, a **proprietary Rockchip-products-only license**, LLMs pushed to a separate `rknn-llm` SDK, and no release since April 2025.
- **MPP / RKMPP** — the video codec interface; when an application's path does not reach it, decode falls back to CPU silently (Jellyfin: 727% CPU vs 3–8%).
- **RGA** — the 2D engine library for resize / crop / colour conversion that feeds the NPU and encoder without CPU frame copies.
- **Kernel branch matters**: Rockchip BSP kernels expose vendor NPU / MPP / GPU interfaces that mainline may not; the reference measurements were taken on a `6.1.0-rockchip` kernel, not mainline.

Microduck's runtime is the wiki's one shipped example of building on this stack in production — it measured its own NPU rather than quote the datasheet, and pairs Rust daemons with RKNN inference on the RK3566 ([runtime repo](../sources/microduck-runtime-repo.md)).

## Related
- [Rockchip RK3588](rockchip-rk3588.md) · [Rockchip RK1828](rockchip-rk1828.md) · [RKNN-Toolkit2](rknn-toolkit2.md)
- [Microduck](microduck.md) · [Pollen Robotics](pollen-robotics.md)
- [Hailo](hailo.md) — the other compiled-model NPU vendor in the wiki.
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md)

## Mentioned in
- [RK3588 Architecture Deep Dive (Turing Pi)](../sources/turingpi-rk3588-architecture-deep-dive.md)
- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md)
- [`pollen-robotics/microduck` — the onboard runtime](../sources/microduck-runtime-repo.md)
- [airockchip/rknn-toolkit2](../sources/rknn-toolkit2-github.md)
- [RK1828 vs Jetson Orin NX vs Hailo-8 (Geniatech)](../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md)
