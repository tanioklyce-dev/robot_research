---
title: NVIDIA DGX Spark — Hardware Overview (docs)
type: source
subtype: official-docs
url: https://docs.nvidia.com/dgx/dgx-spark/hardware.html
author: NVIDIA
published: 2025
ingested: 2026-05-16
tags: [dgx-spark, gb10, grace-blackwell, workstation, unified-memory]
---

# NVIDIA DGX Spark — Hardware Overview

The canonical NVIDIA-docs page for **DGX Spark** hardware specs. Source-of-truth for CPU/GPU/memory/networking numbers.

## Summary

DGX Spark is a desktop-form-factor "personal AI supercomputer" built on the **GB10 Grace Blackwell Superchip**. **128 GB LPDDR5X unified memory** (CPU + GPU coherent), **6,144-CUDA-core Blackwell GPU with 4th-gen RT cores** and 5th-gen Tensor Cores, **20-core ARM CPU** (10 Cortex-X925 + 10 Cortex-A725), **ConnectX-7** networking that lets two boxes pair for **405B-parameter models**. Headline AI throughput: **up to 1 PFLOP FP4 sparse / 1,000 TOPS**. 240 W external PSU, 1.2 kg, ~6-inch cube.

## Key claims — verbatim

### GB10 SOC
- "20-core Arm processor (10 Cortex-X925 + 10 Cortex-A725)"
- TDP 140 W

### GPU
- "NVIDIA Blackwell Architecture with 5th Generation Tensor Cores, 4th Generation RT Cores"
- 6,144 CUDA cores
- 2 Copy Engines

### Memory
- "128 GB LPDDR5x unified system memory, 256-bit interface, 4266 MHz, 273 GB/s bandwidth"
- 16 memory channels (256-bit) LPDDR5X 8533

### Storage
- "1 TB or 4 TB NVMe M.2 with self-encryption"

### Networking
- "1× RJ-45 (10 GbE), ConnectX-7 Smart NIC, Wi-Fi 7, Bluetooth 5.4"

### AI performance
- "Up to 1,000 TOPS (trillion operations per second) inference and up to 1 PFLOP (petaFLOP) at FP4 precision with sparsity"
- "AI models up to 200 billion parameters" (single box)
- Two-box ConnectX-7 pairing → up to 405B parameters (confirmed elsewhere in NVIDIA's DGX Spark messaging; not directly stated on this hardware-overview page).

### Physical / power
- "150 mm (L) × 150 mm (W) × 50.5 mm (H)", "1.2 kg (2.6 lbs)"
- "240 W external power supply"; ~100 W allocated to system components beyond the SOC.

## Entities mentioned
- [NVIDIA DGX Spark](../entities/dgx-spark.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- Coherent unified CPU/GPU memory — eliminates the host→VRAM staging that bottlenecks large-model loading on consumer GPUs.
- RT cores as the gating hardware for Isaac Sim / Omniverse RTX viewports — see [Isaac Sim and Isaac Lab on Jetson AGX Thor](rs-designspark-isaac-sim-on-thor.md).

## Open questions
- Discrete FP8 / FP16 / FP32 throughput numbers (page does not list).
- Sustained vs peak FP4 — the 1 PFLOP figure is sparse-tensor headline.
- Real-world fine-tune wall-clock times for 70B vs 200B-parameter models.
