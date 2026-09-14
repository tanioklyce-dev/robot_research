---
title: "RK3588 Architecture Deep Dive: CPU, GPU, NPU and Memory Explained (Turing Pi)"
type: source
url: https://turingpi.com/rk3588-architecture-cpu-gpu-npu-memory/
author: Turing Pi
published: 2026-08-15
ingested: 2026-09-13
local_path: raw/2026-08-15-turingpi-rk3588-architecture-deep-dive.html
sha256: 74b6bdc5dc3538bb0ee596635fe118b5c3a76ccc7dac436cc758ab55c967d384
tags: [rk3588, rockchip, turing-pi, edge-ai, npu, arm, soc, memory-bandwidth, llm, llama-cpp, rknn, single-board-computer, onboard-compute, vendor-benchmark]
format: vendor blog article (~4,500 words, 10 parts + FAQ)
---

# RK3588 Architecture Deep Dive: CPU, GPU, NPU and Memory Explained

## Summary

A vendor explainer from [Turing Pi](../entities/turing-pi.md), using their **Turing RK1** compute module as the reference platform, on how the [Rockchip RK3588](../entities/rockchip-rk3588.md)'s engines — 4× Cortex-A76 + 4× Cortex-A55, Mali-G610 MP4 GPU, three-core 6 TOPS NPU, VPU, RGA 2D engine, ISP, display controller — actually behave under load, and why they all depend on one shared 64-bit LPDDR path. Its thesis is that the spec sheet is a list of *engines* and real performance is a question of *coordination*: choosing the right engine per stage, avoiding buffer copies, and running a kernel/userspace stack that exposes the accelerator at all. Three measured results carry the argument. **Four CPU threads beat eight** for `llama.cpp` token generation (5.46 vs 3.85 tok/s on Qwen2.5-7B Q4_K_M) because the A55 cluster adds memory pressure to a bandwidth-bound loop. **A memory-bound job on the *other* cluster cut LLM generation by 46%** without touching the cores running it — the cleanest demonstration in this wiki that unified memory is a shared budget, not a free interconnect. And **a 6 TOPS NPU rating says nothing about end-to-end frame rate**: Rockchip's own model-zoo numbers exclude pre- and post-processing, and a worked 8 + 6 + 5 ms pipeline turns an NPU-only 166 fps into ~52 fps. Aimed at homelab / media-server / Kubernetes readers; it never mentions robotics, ROS, or power draw in watts, which is exactly what makes it useful here as a neutral reference for the class of board that [Microduck](../entities/microduck.md) (RK3566) and the Raspberry-Pi-tier robots sit on.

> [!note] Vendor source, but a methodologically stated one
> Turing Pi sells the RK1. The new measurements are described with kernel version, governor, core-to-cluster mapping, warm-up, median-of-three, run-to-run variance (<1.3%) and peak temperatures, and the article repeatedly *narrows* Rockchip's marketing claims (the 8K decode figure, the TOPS rating, the "eight cores") rather than inflating them. Treat the numbers as vendor-measured but reproducible; treat the absence of any wattage as the significant omission for a robot.

## Key claims

### Reference platform (Part 1)
- **Turing RK1, 32 GB**, in a **Turing Pi 2.5** baseboard, 1 TB NVMe, **Ubuntu Server 24.04 LTS**, kernel **6.1.0-1025-rockchip** (a Rockchip-lineage kernel, not mainline), `performance` governor, RK1 heatsink with 5 V PWM fan. CPUs 0–3 = A55 cluster (≤1.8 GHz), CPUs 4–7 = A76 cluster (≤2.4 GHz). Median of three warmed runs.
- The RK1 ships with **8 / 16 / 32 GB** LPDDR.
- "The software environment is part of the platform": the CPU uses standard Linux interfaces, but NPU and media engines depend on matching kernel, firmware and userspace libraries, and different kernel branches expose different accelerator features.

### Engine map and caches (Parts 2–3, from Rockchip's brief datasheet)
- Per-core private L1/L2; **3 MB shared CPU L3**; GPU **4 × 256 KB L2 = 1 MB**; NPU **1 MB shared on-chip memory**.
- A76: 64 + 64 KB L1, **512 KB L2 per core** (2 MB total). A55: 32 + 32 KB L1, **128 KB L2 per core** (512 KB total).
- Arm describes the A76 as four-wide decode, out-of-order, 128-bit SIMD; the A55 runs the same ARM64 code with less work per clock.
- Shared memory does not make data movement free: Rockchip MPP (`MppBuffer`) and RKNN support buffer import and synchronisation, but a copy is avoided only when producer and consumer agree on **layout, format, alignment and ownership**. Otherwise a frame "never leaves the RK3588, but it can still cross LPDDR multiple times."

### CPU cluster benchmark (Part 3)

| Workload | 4× A76 | 4× A55 | All 8 cores |
|---|---|---|---|
| sysbench CPU (events/s) | 3,904.34 | 1,452.89 | 5,298.59 |
| `llama-bench` tg256, Qwen2.5-7B-Instruct Q4_K_M (tok/s) | **5.462** | 1.493 | 3.846 |

- sysbench scales: A76 cluster ≈ 2.7× the A55 cluster; all eight ≈ +36% over A76-only.
- LLM generation inverts: **all eight cores are ~30% *slower* than the four A76s**. The generation loop is memory-sensitive; adding the slow cluster adds cache and memory traffic and uneven completion times. "This does not mean 'never use eight threads'" — compilation, rendering and compression scale across all eight.
- Peak temperatures 75.77 °C (A76 llama-bench), 62.85 °C (A55), 72.08 °C (all-core); **no frequency throttling observed** in any test, so the deltas are not thermal.

### Memory system (Part 4)
- **Four 16-bit LPDDR channels = a 64-bit external path**; LPDDR4 / 4X / 5 supported at the SoC level.
- Earlier RK1 measurements: **STREAM ~21–22 GB/s**, mbw block copy 17–19 GB/s, memcpy 8–9 GB/s. **Bandwidth was broadly the same across the 8 / 16 / 32 GB capacities** — capacity and bandwidth solve different problems.
- Earlier concurrency test: two simultaneous memory-bound sessions each got ~60–65% of single-session bandwidth; three each got ~40–50%.
- **Contention benchmark (new)**: `llama-bench` pinned to the A76s while STREAM (4 OpenMP workers, 2.2 GiB working set) ran on the A55s. Generation fell **5.462 → 2.939 tok/s (−46.2%)**; STREAM Triad fell 21.53 → 11.75 GB/s. "The competing workload never used the A76 cores running llama.cpp, yet generation still slowed substantially… CPU utilization alone would not reveal that bottleneck." Peak 74.85 °C, no throttling.

### GPU (Part 5)
- **Mali-G610 MP4** — "MP4" = four GPU cores, not MPEG-4; third-generation Valhall; Rockchip lists OpenGL ES 3.2, Vulkan 1.2, OpenCL. **No discrete VRAM**: textures, buffers and framebuffers live in LPDDR and compete with everything else.
- Arm Frame Buffer Compression cuts traffic within graphics/display, but a consumer that cannot read the compressed layout forces a conversion.
- What applications can actually use depends on **vendor `libmali` vs upstream Mesa** and the kernel; "graphics output alone does not describe the full compute or API support available."

### NPU (Part 6)
- Three cores, **up to 6 TOPS** "under supported low-precision workloads"; Rockchip lists INT4 / INT8 / INT16 / FP16 / BF16 / TF32.
- Toolchain: **RKNN Toolkit2** converts PyTorch / TensorFlow / ONNX graphs on a development host (layout changes, op fusion, optional quantisation); the on-device runtime loads the compiled model, assigns cores via a **core mask**, binds memory, submits inference. Enabling all three cores "does not guarantee three times the performance."
- Inference is more than the matmul: CPU input load → decode / resize / normalise / layout (CPU or RGA) → NPU → CPU post-processing (thresholds, NMS) → overlay (GPU / RGA / CPU). Worked example: **8 ms pre + 6 ms NPU + 5 ms post ≈ 19 ms → ~52 fps, not the 166 fps the NPU time alone implies.**
- Rockchip model-zoo **single-core execution-only** references at max NPU clock, explicitly excluding pre/post-processing:

| Model | RK3588 single-core execution reference |
|---|---|
| MobileNetV2 INT8, 224×224 | 467.0 fps |
| ResNet-50 INT8, 224×224 | 99.0 fps |
| YOLOv8n INT8, 640×640 | 90.2 fps |

### Media engines (Part 7)
- VPU: Rockchip advertises 8K-class decode for H.265 / H.264 / VP9 / AV1 / AVS2 and H.264 / H.265 encode; the article warns that "8K60 decode" does not apply to every format/profile. **RGA** is a separate 2D engine (scale / crop / rotate / colour-convert / compose) that bridges camera or decoded frames into NPU- or encoder-sized inputs. **ISP** does HDR and noise reduction; display controller scans out to HDMI / DP / eDP / MIPI.
- Earlier Jellyfin measurement — the case for dedicated blocks:

| Source → output | Software (CPU) | Hardware pipeline (RKMPP) |
|---|---|---|
| 4K HEVC Main10 → 540p H.264 | 727% CPU, 39 fps (0.65× real time) | 3–8% CPU, ~306 fps |
| 4K AV1 Main → 540p H.264 | 733% CPU, 37 fps | 4–8% CPU, ~306 fps |

- If the configured software path cannot reach RKMPP, the application silently falls back to CPU — "software support matters just as much as the hardware block itself."

### Worked workloads (Part 8)
- **GGUF LLM via llama.cpp (CPU only)**: weights exceed caches, generation streams from LPDDR; Q4_K_M consistently fastest because fewer bytes move per token; GPU and NPU stay idle "unless a separate offload path is explicitly configured and verified."
- **Vision model on the NPU**: the NPU accelerates only the middle of the chain; a weak preprocessing path leaves it idle between frames; a copy-avoiding buffer path raises throughput without touching NPU clock or TOPS.
- **Linux 6.1 kernel build**: ~28–32 min from eMMC; NVMe ~20–30% faster.
- **AI camera pipeline**: ISP → RGA resize → NPU detect → CPU interpret → GPU/RGA overlay → display, with the VPU encoding a recording concurrently. "No single utilization number describes that pipeline."

### Design rules (Parts 9–10, paraphrased)
Keep latency-sensitive code on the A76s when measured; A55s for background and cleanly parallel work; VPU for codecs, not the GPU; RGA before CPU for resize/format; **convert and quantise for the actual RKNN target, then measure the whole application rather than quoting TOPS**; reuse DMA-capable buffers with compatible layouts; **treat memory bandwidth as a shared budget and benchmark alone *and* under realistic concurrency**; choose mainline vs Rockchip BSP kernel by which accelerators the deployment needs.

## Relevance to this wiki

- **The bandwidth number the Jetson ladder was missing a comparator for.** The [module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) lists **102 GB/s** for an Orin Nano 8 GB and 273 GB/s for Thor. The RK3588's measured **~21.5 GB/s STREAM** puts a whole class of ARM SBCs (RK1, Orange Pi 5, Radxa Rock 5, and by construction the Raspberry Pi 5, which also carries four A76 cores) at **roughly one fifth of the entry Jetson** on the resource that bounds LLM decode. This is the quantitative form of the [backlog](../backlog.md)'s standing worry that desktop-GPU VLA latencies "do not survive edge memory bandwidth."
- **The −46% contention result is the argument against "run the policy on the NPU and the LLM on the CPU and they won't interfere."** Every engine draws on one LPDDR path; an onboard [split-brain](../syntheses/agents/on-device-and-on-robot-agents.md) that puts a talking LLM next to a vision pipeline on one of these SoCs has to be benchmarked *concurrently*, not per-engine.
- **The NPU section is the Rockchip mirror of the [Hailo](../entities/hailo.md) page**: a fixed-function accelerator runs models compiled ahead of time (RKNN here, HEF there), operator coverage decides what maps, and the vendor's fps table measures execution only. It also explains [Microduck](../sources/microduck-runtime-repo.md)'s decision to report a *pipeline* `yolo11n` latency on its RK3566 (p50 25.7 ms at 320×320, one NPU core, 0.8 TOPS) rather than a model-zoo figure — the same toolchain family, two SoC tiers apart.
- **TOPS across vendors, again.** 6 TOPS (Rockchip, precision unspecified in the headline), 40 TOPS INT4 (Hailo-10H), 67 TOPS INT8 sparse (Orin Nano): three units, three measurement conventions, as the [Hailo-vs-Jetson](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md) page already warns. This source adds the reason a single number can never close the gap: the number describes the middle of a pipeline whose ends run elsewhere.
- **Four threads beat eight** generalises to any big.LITTLE host running a control loop: pin the loop to the fast cluster and keep housekeeping off it. This is the CPU-side sibling of the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md)'s measured-vs-required distinction.
- **What is not here for a robot**: no power draw at any point (not even the cluster tests), no ROS 2 or real-time kernel discussion, no measurement of the NPU on the tested board (all NPU numbers are Rockchip's), no GPU compute benchmark, no camera/ISP throughput. A buying decision for a battery robot needs all of those from elsewhere.

## Entities mentioned
- [Rockchip RK3588](../entities/rockchip-rk3588.md) — the SoC (new entity).
- [Rockchip](../entities/rockchip.md) — vendor; RKNN / MPP / RGA toolchains (new entity).
- [Turing Pi](../entities/turing-pi.md) — author; RK1 module and Pi 2.5 baseboard (new entity).
- [Raspberry Pi 5](../entities/raspberry-pi-5.md) — the same-tier comparator (four A76s, no NPU, no A55 cluster).
- [Hailo](../entities/hailo.md) — the other compiled-model NPU path in the wiki.
- [Jetson Orin Nano](../entities/jetson-orin-nano.md) — the CUDA comparator at ~5× the bandwidth.
- [Microduck](../entities/microduck.md) — RK3566 sibling; its runtime measures the NPU end-to-end.
- Qwen2.5-7B-Instruct ([Qwen](../entities/qwen.md)) — the benchmark model.

## Concepts touched
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md) — new concept page built from this source.
- [Onboard robot service architecture](../concepts/robotics/onboard-robot-service-architecture.md) — the software layer that decides which engine each stage reaches.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — decode-rate arithmetic for an onboard agent.
- [VLA models](../concepts/learning/vla-models.md) — what a 21 GB/s, 6 TOPS board can and cannot host.

## Open questions
- **Power.** What does the RK1 (or any RK3588 board) draw at the wall during the A76 llama-bench, and during NPU + ISP + VPU concurrency? Not stated; needed before any onboard-robot comparison against a 7–15 W Orin Nano.
- **Does any LeRobot policy run through RKNN?** ACT / Diffusion Policy / SmolVLA export to ONNX; whether their operators map to RKNN Toolkit2 and what the *pipeline* latency is on three NPU cores is untested in this wiki (the same open question the Hailo page carries for HEF).
- **Multi-core NPU scaling on a real detector** — the article says three cores ≠ 3×, but gives no measured ratio.
- **Mainline vs BSP kernel**: which of NPU / MPP / RGA / Mali-OpenCL is reachable on a 6.x mainline kernel today? The article says "it depends" and stops.
- The article cites its own earlier RK1 benchmark, RK3588 LLM benchmark and Jellyfin guide for the STREAM, GGUF and transcode numbers; those primaries are not ingested.
