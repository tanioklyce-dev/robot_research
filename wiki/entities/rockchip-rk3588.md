---
title: Rockchip RK3588
type: entity
subtype: product
created: 2026-09-13
updated: 2026-09-13
sources: 3
tags: [rk3588, rockchip, soc, arm, npu, edge-ai, single-board-computer, onboard-compute, memory-bandwidth]
---

# Rockchip RK3588

[Rockchip](rockchip.md)'s flagship ARM application processor: **4× Cortex-A76 (≤2.4 GHz) + 4× Cortex-A55 (≤1.8 GHz)**, an Arm **Mali-G610 MP4** GPU, a **three-core NPU rated 6 TOPS**, 8K-class video decode / H.264-H.265 encode, an RGA 2D engine, camera ISPs and a **64-bit (4 × 16-bit) LPDDR4/4X/5** memory interface. It is the SoC under most of the "faster than a Raspberry Pi 5" single-board computers and compute modules (Turing RK1, Orange Pi 5, Radxa Rock 5, Khadas Edge2, Banana Pi M7 and others), and the top of the same Rockchip family whose RK3566 runs [Microduck](microduck.md).

## Architecture, as measured on a Turing RK1

All figures from [Turing Pi's architecture deep dive](../sources/turingpi-rk3588-architecture-deep-dive.md) (32 GB RK1, kernel 6.1.0-1025-rockchip, performance governor, median of three; datasheet figures attributed there to Rockchip's brief datasheet).

| Block | Detail |
|---|---|
| CPU | 4× A76: 64+64 KB L1, 512 KB L2/core. 4× A55: 32+32 KB L1, 128 KB L2/core. 3 MB shared L3. |
| GPU | Mali-G610 MP4 (four cores, Valhall gen 3); OpenGL ES 3.2 / Vulkan 1.2 / OpenCL per Rockchip; 1 MB L2; **no VRAM** — all buffers in LPDDR |
| NPU | 3 cores, 6 TOPS "under supported low-precision workloads"; INT4/INT8/INT16/FP16/BF16/TF32; 1 MB on-chip shared memory; programmed via **RKNN Toolkit2** (compile on host) + RKNN runtime (core mask, memory import) |
| Media | VPU (H.265/H.264/VP9/AV1/AVS2 decode, H.264/H.265 encode, via Rockchip MPP); **RGA** 2D scale/crop/convert; ISP with HDR/NR; display controller (HDMI/DP/eDP/MIPI) |
| Memory | 4 × 16-bit LPDDR channels = 64-bit; **STREAM ~21–22 GB/s measured**, memcpy 8–9 GB/s; bandwidth flat across 8/16/32 GB |

### The three numbers that matter for a robot

- **CPU LLM decode: 5.46 tok/s** on Qwen2.5-7B-Instruct Q4_K_M with four threads on the A76s; **3.85 tok/s with all eight** — the A55 cluster hurts a bandwidth-bound loop ([Turing Pi](../sources/turingpi-rk3588-architecture-deep-dive.md)).
- **Memory contention: −46%** LLM generation when a STREAM job runs on the *other* cluster (2.94 tok/s; Triad 21.5 → 11.8 GB/s). Every engine shares one LPDDR path, so per-engine benchmarks do not add ([Turing Pi](../sources/turingpi-rk3588-architecture-deep-dive.md)).
- **NPU: execution-only fps is not pipeline fps.** Rockchip's single-core model-zoo references — MobileNetV2 INT8 467 fps, ResNet-50 INT8 99 fps, **YOLOv8n INT8 640² 90.2 fps** — exclude pre- and post-processing; a worked 8 + 6 + 5 ms pipeline gives ~52 fps where the NPU alone implies 166 ([Turing Pi](../sources/turingpi-rk3588-architecture-deep-dive.md)).

## Where it sits in the wiki's compute ladder

| | RK3588 board | [Raspberry Pi 5](raspberry-pi-5.md) | [Jetson Orin Nano 8 GB](jetson-orin-nano.md) |
|---|---|---|---|
| CPU | 4× A76 + 4× A55 | 4× A76 | 6× A78AE |
| Accelerator | 3-core NPU, 6 TOPS (RKNN) + Mali-G610 (OpenCL) | none (add [Hailo](hailo.md) HAT, compiled HEF) | 1024-core Ampere GPU, 67 TOPS INT8 sparse (CUDA) |
| Memory bandwidth | **~21.5 GB/s measured** (64-bit LPDDR) | not measured in the wiki | **102 GB/s** (128-bit LPDDR5) |
| Runs a PyTorch policy unchanged? | No — ONNX → RKNN compile, operator coverage permitting | No | Yes |

The bandwidth row is the one that decides LLM decode and, by the [backlog](../backlog.md)'s standing argument, VLA action-chunk latency: an RK3588 has **about one fifth** of the entry Jetson's. Comparison rows for the Jetson are from the [module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md); the TOPS figures are in three different units and are not comparable, as that page and [Hailo vs Jetson](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md) both warn.

> [!note] What the wiki does not know about this SoC
> Power draw under load (no source here gives a wattage), whether any [LeRobot](lerobot.md) policy exports cleanly to RKNN, measured multi-core NPU scaling, and which accelerators a mainline kernel exposes versus the Rockchip BSP. See the source page's open questions.

## Toolchain and siblings

The NPU is reached through [RKNN-Toolkit2](rknn-toolkit2.md), whose [operator list](../sources/rknn-toolkit2-github.md) is the exportability oracle: ACT plausibly converts, Diffusion Policy is blocked by `GroupNormalization`, VLA-class models are redirected to the separate `rknn-llm` SDK. Two things that page settles about *this* chip: the RK3588's NPU gets int4×int4 MatMul but **not Flash Attention or W4A16, which Rockchip shipped only for the RK3576** — so the highest-TOPS Rockchip part is not its best transformer target; and Rockchip's own proposed LLM topology is **RK3588 as host plus an [RK1828](rockchip-rk1828.md) M.2 coprocessor** with on-package memory, rather than the RK3588's NPU ([Geniatech](../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md), vendor claim).

## Related
- [Rockchip](rockchip.md) — vendor; RK3566 sibling. [RKNN-Toolkit2](rknn-toolkit2.md) — the SDK. [RK1828](rockchip-rk1828.md) — the LLM coprocessor pitched alongside it.
- [Turing Pi](turing-pi.md) — the RK1 module the measurements were taken on.
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md) — the concept this chip is the worked example for.
- [Microduck](microduck.md) — a shipped robot on the RK3566, with an end-to-end NPU measurement.

## Mentioned in
- [RK3588 Architecture Deep Dive (Turing Pi)](../sources/turingpi-rk3588-architecture-deep-dive.md)
- [airockchip/rknn-toolkit2](../sources/rknn-toolkit2-github.md) — supported platform; generation split vs RK3576
- [RK1828 vs Jetson Orin NX vs Hailo-8 (Geniatech)](../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md) — as proposed host for the RK1828
