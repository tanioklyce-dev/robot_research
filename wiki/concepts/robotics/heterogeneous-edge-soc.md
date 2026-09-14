---
title: Heterogeneous edge SoCs and the shared-memory budget
type: concept
created: 2026-09-13
updated: 2026-09-13
sources: 10
tags: [edge-ai, soc, npu, memory-bandwidth, unified-memory, onboard-compute, llm-inference, arm, rk3588, jetson, hailo, systems]
---

# Heterogeneous edge SoCs and the shared-memory budget

Every board a robot in this wiki can carry — a [Raspberry Pi 5](../../entities/raspberry-pi-5.md), an [RK3588](../../entities/rockchip-rk3588.md) module, a [Jetson](../../entities/jetson-orin-nano.md), a [Thor](../../entities/jetson-thor.md), even a [DGX Spark](../../entities/dgx-spark.md) — is a **heterogeneous system-on-chip**: several specialised engines (CPU clusters of unequal speed, a GPU, a fixed-function NPU or DLA, video codecs, an image-signal processor, 2D blitters) with **no private memory of their own**, all reading and writing one external LPDDR pool through one memory controller. The spec sheet lists the engines. Performance is decided by three things the spec sheet does not carry: which engine each stage of a pipeline actually reaches, how many times a buffer crosses the memory path on the way, and how much of the shared bandwidth is left once everything else on the board is running.

## The four facts

**1. LLM decode is bandwidth-bound, so bytes per token is the number.** Generating one token streams the whole weight set through the memory path once. On an RK3588 that is why a 4-bit quant beats every higher-precision GGUF and why Qwen2.5-7B Q4_K_M reaches **5.46 tok/s on four A76 cores but 3.85 on all eight** — the slow A55 cluster adds traffic to a loop that was already waiting on LPDDR ([Turing Pi](../../sources/turingpi-rk3588-architecture-deep-dive.md)). On the same principle, the same Orin Nano runs Gemma 4 E2B at **12.2 tok/s on CPU and 24.2 on GPU**, and a Pi 5 sits at 7.6 with no accelerated backend at all ([Gemma 4 E2B card](../../sources/gemma-4-e2b-model-card.md)). Capacity is a different axis: an RK1's bandwidth was flat across 8 / 16 / 32 GB. **The NPU does not escape this.** Rockchip's own [RKLLM benchmark](../../sources/rknn-llm-github.md) puts a 6B model at **4.98 tok/s on the RK3588's NPU at 8-bit weights** — the same rate as the CPU at 4-bit on a 7B (5.46) — so the accelerator is roughly twice as bandwidth-efficient and bounded by the same ~21.5 GB/s. Same board, same wall, two engines.

**2. The bandwidth is one budget, and every engine draws on it.** The cleanest measurement in the wiki: pin `llama.cpp` to the RK3588's fast cluster, run STREAM on the *slow* cluster, and generation drops **46%** (5.46 → 2.94 tok/s) though no core running the LLM was touched ([Turing Pi](../../sources/turingpi-rk3588-architecture-deep-dive.md)). A GPU renderer, an NPU detector, a video encoder and NVMe DMA all do the same. Consequence for a robot's [split-brain](../../syntheses/agents/on-device-and-on-robot-agents.md): per-engine benchmarks do not add, and an onboard LLM sitting beside a camera pipeline must be measured **concurrently**. CPU utilisation will read low while the board is saturated.

**3. A fixed-function accelerator runs compiled models, and its headline number measures the middle of the pipeline.** An NPU executes a graph that a host-side compiler has already lowered — RKNN Toolkit2 for Rockchip, the Dataflow Compiler to HEF for [Hailo](../../entities/hailo.md), TensorRT engines for a Jetson's DLA. Operator coverage decides what maps; anything unsupported falls back to CPU. And the vendor's fps tables measure execution only: Rockchip's **90.2 fps** for YOLOv8n INT8 excludes the resize, normalise and NMS that bracket it, and a worked 8 + 6 + 5 ms pipeline gives ~52 fps ([Turing Pi](../../sources/turingpi-rk3588-architecture-deep-dive.md)). [Microduck](../../sources/microduck-runtime-repo.md) reports its RK3566 detector the honest way, as a pipeline p50 / p95. This is also why **TOPS never compare across vendors**: 6 TOPS (Rockchip), 40 TOPS INT4 (Hailo-10H), 67 TOPS INT8 sparse (Orin Nano) are three units for three middles of three different pipelines ([Hailo vs Jetson](../../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md)).

**4. Shared memory is not zero-copy.** Avoiding a copy requires producer and consumer to agree on layout, pixel or tensor format, alignment and ownership; a VPU frame the NPU cannot consume gets a conversion buffer, and the data crosses LPDDR again without ever leaving the chip. The vendor libraries (MPP buffer import, RKNN memory import, DMA-BUF on Linux generally) exist to make that agreement possible, and **which kernel branch you run decides whether they are reachable** — the RK3588 measurements were on a Rockchip 6.1 kernel, and the article declines to say which accelerators mainline exposes ([Turing Pi](../../sources/turingpi-rk3588-architecture-deep-dive.md)). The Jetson equivalent is the [JetPack](../../entities/jetpack.md) release that ships the CUDA / TensorRT / multimedia APIs as one bundle.

**5. The counter-design is memory in the accelerator's package — and it trades bandwidth for capacity.** [Rockchip](../../entities/rockchip.md)'s [RK1828](../../entities/rockchip-rk1828.md) M.2 coprocessor claims **1,024 GB/s** from 5 GB of 3D-stacked DRAM on-package at ~5 W, behind a **PCIe 2.0 ×1** host link ([Geniatech](../../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md), vendor claim, no primary). The bandwidth is real only for what is already resident, so the model is capped by the card's capacity — a 7B at 4-bit, thin KV headroom — and nothing about it helps a vision pipeline that must stream frames across the lane. The [Hailo-10H](../../entities/hailo.md) with its 8 GB of own DRAM is the same idea at lower bandwidth. Fact 3's fine print is now also on file: the [rknn-toolkit2 operator list](../../sources/rknn-toolkit2-github.md) — 89 of 187 ONNX ops, `GroupNormalization` and `Einsum` unsupported, `Softmax` at batch 1 — is what "compiled models, operator coverage permitting" means in practice.

## Where the wiki's boards sit

| Board | Fast CPU | Accelerator (programming model) | Memory path | Measured bandwidth |
|---|---|---|---|---|
| [Raspberry Pi 5](../../entities/raspberry-pi-5.md) | 4× A76 | none onboard; [Hailo](../../entities/hailo.md) HAT over one PCIe lane (HEF) | LPDDR4X | — |
| [RK3588](../../entities/rockchip-rk3588.md) (RK1, Orange Pi 5, Rock 5) | 4× A76 + 4× A55 | 3-core NPU (RKNN) + Mali-G610 (OpenCL) | 64-bit LPDDR4/5 | **~21.5 GB/s** STREAM |
| [Jetson Orin Nano 8 GB](../../entities/jetson-orin-nano.md) | 6× A78AE | Ampere GPU (CUDA) | 128-bit LPDDR5 | 102 GB/s (spec) |
| [Jetson Orin NX 16 GB](../../entities/jetson-orin-nx.md) | 8× A78AE | Ampere GPU + 2 DLA (CUDA / TensorRT) | 128-bit LPDDR5 | 102.4 GB/s (spec) |
| [Jetson Thor T5000](../../entities/jetson-thor.md) | 14× Neoverse-V3AE | Blackwell GPU (CUDA) | 256-bit LPDDR5X | 273 GB/s (spec) |
| [DGX Spark](../../entities/dgx-spark.md) | 20× Arm (Grace) | Blackwell GPU (CUDA) | 128 GB unified | 273 GB/s (spec) |

Jetson and Spark rows from the [module ladder](../../syntheses/platforms/jetson-module-ladder-power-performance.md) and [Spark overview](../../sources/nvidia-dgx-spark-hardware-overview.md); the RK3588 row is the only *measured* bandwidth in the table, and the Pi 5's is not recorded anywhere in the wiki. The ladder's lesson is the ratio: the ARM-SBC tier has **about one fifth** of the entry Jetson's bandwidth, and the Jetson tier about one third of Thor's.

## Why it matters for the wiki's questions

- **Onboard VLA feasibility** is a bandwidth question before it is a TOPS question: an action-chunk forward pass streams the policy's weights the same way a token does. The [backlog](../../backlog.md) already frames the deployability audit that way ("the 4090 figure does not survive edge memory bandwidth"); this page gives it the arithmetic.
- **The compiled-model question is the same on every NPU.** The open item on the [Hailo](../../entities/hailo.md) page — can ACT / Diffusion Policy / SmolVLA be compiled to HEF — has an exact RKNN twin, and neither has been tried here.
- **Design rule for a big.LITTLE host running a control loop**: pin the loop to the fast cluster, keep housekeeping off it, and benchmark the loop with the rest of the robot's software running. [Microduck](../../concepts/robotics/onboard-robot-service-architecture.md)'s daemon split on a four-A55 RK3566 is the wiki's one shipped instance.

## Key references
- [RK3588 Architecture Deep Dive (Turing Pi)](../../sources/turingpi-rk3588-architecture-deep-dive.md) — the source this page is built from: cluster benchmark, contention benchmark, NPU pipeline arithmetic, buffer-copy discussion.
- [Gemma 4 E2B model card + LiteRT benchmarks](../../sources/gemma-4-e2b-model-card.md) — the CPU-vs-GPU-vs-NPU decode table across Pi 5, Orin Nano, Dragonwing.
- [`pollen-robotics/microduck` runtime](../../sources/microduck-runtime-repo.md) — a shipped NPU pipeline measured end-to-end.
- [Raspberry Pi AI HAT+ 2](../../sources/raspberry-pi-ai-hat-plus-2.md) and [hailo-apps](../../sources/hailo-apps-github.md) — the HEF compiled-model path.
- [Jetson module ladder](../../syntheses/platforms/jetson-module-ladder-power-performance.md) — the bandwidth column for the CUDA tier.
- [airockchip/rknn-toolkit2](../../sources/rknn-toolkit2-github.md) — the operator list, batch-1 restrictions, license and cadence behind fact 3.
- [airockchip/rknn-llm](../../sources/rknn-llm-github.md) — NPU-measured LLM / VLM throughput on RK3588 / RK3576; the NPU-equals-CPU-at-6B confirmation of fact 1, and the 0.7–3.3 s image-encoder cost.
- [RK1828 vs Jetson Orin NX vs Hailo-8 (Geniatech)](../../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md) — the on-package-memory counter-design (fact 5), secondary and vendor-interested.

## Related concepts
- [Onboard robot service architecture](onboard-robot-service-architecture.md) — the process layer that decides which engine each stage reaches.
- [Control abstraction levels](control-abstraction-levels.md) and the [control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) — required vs measured rates; this page is the hardware reason measured rates fall short.
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — decode rate is what a conversational onboard agent lives on.
- [VLA models](../learning/vla-models.md) — the policies whose weight streaming the bandwidth column bounds.

## Current state
The wiki now has one measured bandwidth for the ARM-SBC tier and only spec-sheet figures for the Jetson tier; no page records wall power for an RK3588 under load, and no LeRobot policy has been pushed through either RKNN or HEF. The [Hailo vs Jetson](../../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md) decision page gains a third column — an RK3588 board with its NPU on-die — but until a policy export is attempted, the CUDA path remains the only one the wiki can call validated for control.

## Mentioned in
- [RK3588 Architecture Deep Dive (Turing Pi)](../../sources/turingpi-rk3588-architecture-deep-dive.md)
- [Gemma 4 E2B model card + LiteRT benchmarks](../../sources/gemma-4-e2b-model-card.md)
- [`pollen-robotics/microduck` — the onboard runtime](../../sources/microduck-runtime-repo.md)
- [Hailo NPU vs Jetson for an onboard XLeRobot brain](../../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md)
- [Jetson module ladder — performance and power](../../syntheses/platforms/jetson-module-ladder-power-performance.md)
- [On-device and on-robot agents](../../syntheses/agents/on-device-and-on-robot-agents.md)
- [airockchip/rknn-toolkit2](../../sources/rknn-toolkit2-github.md)
- [RK1828 vs Jetson Orin NX vs Hailo-8 (Geniatech)](../../sources/geniatech-rk1828-vs-orin-nx-vs-hailo-8.md)
- [airockchip/rknn-llm](../../sources/rknn-llm-github.md)
- [KickPi RK3566 Microduck case study](../../sources/kickpi-rk3566-microduck-case-study.md) — the RK3566 as the bottom rung: one NPU core, no LLM path
