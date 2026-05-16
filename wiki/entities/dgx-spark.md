---
title: NVIDIA DGX Spark
type: entity
subtype: product
created: 2026-05-16
updated: 2026-05-16
sources: 1
tags: [dgx-spark, gb10, grace-blackwell, workstation, unified-memory, physical-ai]
---

# NVIDIA DGX Spark

NVIDIA's **personal AI supercomputer** — a ~6-inch desktop cube built on the **GB10 Grace Blackwell Superchip**, with **128 GB coherent unified CPU/GPU memory**, Blackwell GPU with **4th-gen RT cores**, and ConnectX-7 networking that pairs two boxes for 405B-parameter inference. Sits between consumer RTX workstations and DGX-class data-centre hardware as the "everything fits on your desk" tier ([DGX Spark Hardware Overview](../sources/nvidia-dgx-spark-hardware-overview.md)).

## One-line definition
The developer-desk training and simulation box that complements [Jetson Thor](jetson-thor.md) — same Blackwell generation, same 128 GB / 273 GB/s memory, but **with RT cores**, so it can run [Isaac Sim](nvidia-isaac-sim.md) / [Isaac Lab](nvidia-isaac-lab.md) that Thor cannot.

## Hardware ([DGX Spark Hardware Overview](../sources/nvidia-dgx-spark-hardware-overview.md))

### GB10 Grace Blackwell Superchip
| Spec | Value |
|---|---|
| CPU | 20-core ARM (10× Cortex-X925 + 10× Cortex-A725) |
| GPU | NVIDIA Blackwell, 6,144 CUDA cores, 5th-gen Tensor Cores, **4th-gen RT Cores**, 2 copy engines |
| Memory | 128 GB LPDDR5X **unified**, 256-bit, 4266 MHz, 273 GB/s |
| Memory channels | 16× 256-bit LPDDR5X 8533 |
| Storage | 1 TB or 4 TB self-encrypting NVMe M.2 |
| Networking | 10 GbE RJ-45, **ConnectX-7 Smart NIC**, Wi-Fi 7, Bluetooth 5.4 |
| AI throughput | Up to **1,000 TOPS / 1 PFLOP FP4 sparse** |
| Model capacity | Up to **200B parameters** (single box), **405B paired** via ConnectX-7 |
| Dimensions | 150 × 150 × 50.5 mm, 1.2 kg |
| Power | 240 W external PSU; SoC TDP 140 W |

### The "unified memory" advantage
CPU and GPU share the full 128 GB coherently — no host-to-VRAM staging, no PCIe bottleneck. The result: **large models load directly into a single addressable pool**. This is the architectural feature that lets a desktop box fine-tune a 70B-parameter model and inference a 200B-parameter model — both well beyond consumer RTX 4090 / 5090 VRAM (24–32 GB).

## What DGX Spark is for

- **Fine-tuning** AI models up to **70B parameters** (NVIDIA's stated supported envelope).
- **Inference** of AI models up to **200B parameters** single-box, **405B parameters** paired.
- **Robot policy training**: full [Isaac Sim](nvidia-isaac-sim.md) / [Isaac Lab](nvidia-isaac-lab.md) workflows including the RTX-rendered viewport, RL with massive environment vectorization, [GR00T](nvidia-groot.md) fine-tuning. RT cores are the gating capability vs [Jetson Thor](jetson-thor.md) ([Isaac Sim and Isaac Lab on Jetson AGX Thor — RS DesignSpark](../sources/rs-designspark-isaac-sim-on-thor.md)).
- **Omniverse / NuRec / synthetic data generation** — anything that needs the RTX renderer.
- **CUDA-X / NIM** development across the same software stack DGX-class data-centre hardware uses.

## What DGX Spark is **not**

- Not a **pretraining** machine for frontier LLMs. 1 PFLOP FP4 is fast, but pretraining a 70B-from-scratch model still wants a DGX cluster.
- Not an **on-robot** part. 240 W external PSU, desktop form factor, no automotive / ruggedized envelope — for the robot's brain, use [Jetson Thor](jetson-thor.md).

## Position in the NVIDIA AI hardware lineup

| Tier | Part | Memory | RT cores? | Train? | Sim (Isaac Sim)? | Deploy on robot? |
|---|---|---|---|---|---|---|
| Robot brain | [Jetson Thor](jetson-thor.md) | 128 GB | ❌ | Inference/edge fine-tune | ❌ | ✅ |
| Personal supercomputer | **DGX Spark** | 128 GB unified | ✅ | Up to 70B fine-tune | ✅ | ❌ |
| Consumer workstation | RTX 4090 / 5090 / 6000 Ada | 24–48 GB | ✅ | Small/medium | ✅ | ❌ |
| Data centre | DGX B200 / GB200 | 192 GB+ HBM | ✅ | Frontier pretraining | ✅ | ❌ |

See [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) for the synthesis.

## Software stack

DGX Spark runs **DGX OS** (Ubuntu-derived) with the full NVIDIA AI stack: CUDA, cuDNN, TensorRT, NIM, Triton, NeMo, BioNeMo, Omniverse / Isaac Sim / Isaac Lab. Because the underlying GB10 is ARM64, software needs ARM-compatible builds — most NVIDIA-shipped containers are already multi-arch.

## Comparison to Jetson Thor at a glance

| Spec | DGX Spark | Jetson Thor T5000 |
|---|---|---|
| GPU CUDA cores | 6,144 | 2,560 |
| RT cores | ✅ 4th-gen | ❌ |
| FP4 sparse | 1,000 TOPS | 2,070 TFLOPS |
| Memory | 128 GB unified | 128 GB |
| Mem bandwidth | 273 GB/s | 273 GB/s |
| CPU | 20-core ARM (Cortex X925/A725) | 14-core ARM Neoverse-V3AE |
| Power | 240 W PSU | 40–130 W module |
| Form factor | Desktop cube | Robot-mountable SoM |
| Network | 10 GbE + ConnectX-7 | Embedded I/O |
| Price | ~mid-four-figures (varies by storage) | $3,499 dev kit |

Note: Thor's FP4-sparse headline is **about 2× higher** than DGX Spark's — the Jetson GPU is denser per CUDA-core for tensor math, while Spark has more cores plus RT hardware and the wider 20-core CPU. They are **complementary**, not redundant.

## Related
- [Jetson Thor](jetson-thor.md) — paired on-robot deploy target.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md), [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — primary training workloads.
- [NVIDIA Brev](nvidia-brev.md) — cloud-equivalent path when you don't own a Spark.
- [NVIDIA GR00T](nvidia-groot.md) — typical VLA fine-tuning workload.
- [NVIDIA](nvidia.md) — vendor.

## Open questions
- Real-world Isaac Lab steps-per-second on Spark vs an RTX 5090 vs an H100.
- 70B fine-tune wall-clock estimates (LoRA vs full).
- Compatibility status of third-party ARM64-incompatible CUDA tooling.
- Spark's pricing tiers across the 1 TB vs 4 TB SKUs through different channels.

## Mentioned in
- [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)
- [NVIDIA DGX Spark Hardware Overview](../sources/nvidia-dgx-spark-hardware-overview.md)
- [Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor](../sources/rs-designspark-isaac-sim-on-thor.md)
