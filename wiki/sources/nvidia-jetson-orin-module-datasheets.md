---
title: NVIDIA Jetson Orin module datasheets (AGX Orin DS-10662, Orin NX DS-10712)
type: source
url: https://developer.nvidia.com/downloads/jetson-orin-nx-module-series-data-sheet
author: NVIDIA Corporation
affiliation: NVIDIA
published: 2024-12 (Orin NX DS-10712-001 v1.5; AGX Orin DS-10662-001 v1.1/v1.2, 2022)
ingested: 2026-08-29
venue: NVIDIA product datasheet
format: pdf
tags: [jetson, jetson-agx-orin, jetson-orin-nx, nvidia, rt-cores, ray-tracing, ampere, gpu-architecture, dla, datasheet, primary]
---

> [!note] Two documents, one source page
> **AGX Orin DS-10662-001** and **Orin NX DS-10712-001** carry *identical* GPU-architecture language in their Functional Description chapters, and this page cites that shared passage plus the per-SKU figures each adds. Filed as one page rather than two near-duplicates. Extracted with `pypdf` (see the wiki's PDF-extraction note — `pdftotext` is unreliable in this environment).

## Why this source exists

**NVIDIA's Jetson product-comparison web page — the table every spec in this wiki was built from — does not mention RT cores at all.** No RT row, no ray-tracing row. Reading only that table, you would conclude Orin has no ray-tracing hardware. The datasheets say otherwise, in the Functional Description chapter that the marketing table summarises away.

That makes this a **counter-example to the usual failure mode**: normally the secondary omits what the primary has. Here NVIDIA's *own* summary page omits what NVIDIA's *own* datasheet documents — because the summary is pitched at AI/robotics buyers, and RT cores are a graphics feature. **Absence from a spec table is not absence from the silicon.**

## Key claims

### RT cores are present on Orin, one per TPC

Verbatim, and identical in both datasheets:

> "Tensor cores perform matrix multiplies to greatly accelerate DL inferencing. **The RTcore unit assists Ray Tracing by accelerating Bounding Volume Hierarchy (BVH) traversal and intersection of scene geometry during Ray Tracing.** There are multiple texture processing clusters (TPC) units within a graphics processing cluster (GPC). **Each TPC includes two SMs, a Polymorph Engine, two Texture Units, and a Ray Tracing core (RTcore).** Each GPC includes a Raster Engine (ROP), which can access all of memory."

The AGX Orin datasheet also lists "Modern Graphics features: • **Ray Tracing** • DL Inferencing • Mesh Shaders • Sampler Feedback • Variable Rate Shading."

### Per-SKU GPC / TPC counts — AGX Orin only

From the AGX Orin datasheet's spec summary:

| SKU | GPU config | → RT cores (1/TPC) |
|---|---|---|
| **AGX Orin 64 GB** | **2 GPC \| 8 TPC** | **8** |
| **AGX Orin 32 GB** | **2 GPC \| 7 TPC** | **7** |

Also stated there: AGX Orin 64 GB "Up to 170 INT8 Sparse TOPS or 85 FP16 TFLOPS (Tensor Cores) | Up to 5.32 FP32 TFLOPS or 10.649 FP16 TFLOPS (CUDA cores)"; 32 GB "Up to 108 INT8 Sparse TOPS or 54 FP16 TFLOPS (Tensor Cores) | Up to 3.365 FP32 TFLOPS."

> [!warning] The Orin NX datasheet does **not** publish a GPC/TPC count
> It carries the same "each TPC includes… a Ray Tracing core" architecture text but no per-SKU TPC figure. So **the Orin NX RT-core count is not stated by any primary found.** Arithmetic suggests 4 (1024 CUDA cores ÷ 128 per SM = 8 SMs ÷ 2 SMs per TPC = 4 TPC), but that is **inference, not a published figure** — and the same datasheet's SM description is internally sloppy ("four separate processing blocks, each with its own… 128 CUDA cores," which would imply 512 cores/SM), so the divisor is not safe to lean on.

### Dense INT8 totals — corroboration for the DLA-share finding

The Orin NX datasheet states module-level totals:

> "increases up to **157 (Sparse) INT8 TOPs and 78 (Dense) INT8 TOPs** on Jetson Orin NX 16GB, and up to **117 (S) and 58 (D)** on Jetson Orin NX 8GB"

These reconcile exactly with the per-unit breakdown on NVIDIA's comparison page:

| | GPU dense | DLA dense | Sum | Datasheet total |
|---|---|---|---|---|
| Orin NX 16 GB | 38 | 40 | **78** | **78** ✓ |
| Orin NX 8 GB | 38 | 20 | **58** | **58** ✓ |

**This is independent confirmation of the wiki's DLA-share arithmetic** ([Jetson Orin NX](../entities/jetson-orin-nx.md)) — and it hands us the honest whole-module dense number directly from a primary: **78 dense INT8 TOPS on a part sold as 157**, i.e. **50%**. It also re-confirms the 8 GB's single DLA (20 dense = half the 16 GB's 40).

## Entities mentioned

- [Jetson AGX Orin](../entities/jetson-agx-orin.md) · [Jetson Orin NX](../entities/jetson-orin-nx.md) · [Jetson Orin Nano](../entities/jetson-orin-nano.md) · [NVIDIA](../entities/nvidia.md)

## Concepts touched

- Ray tracing as a **geometric query**, not only a rendering technique — BVH traversal and ray–primitive intersection are the same operations behind simulated lidar/radar and visibility checks.

## Open questions

- **Orin NX RT-core count** — unpublished; see the warning above.
- **Is the RT hardware reachable on Tegra?** OptiX is widely reported as unsupported on Jetson, leaving Vulkan Ray Tracing as the path. **No primary found either way** — treat as unverified.
- **Does anything in the robotics stack use Orin's RT cores?** [Isaac Sim](../entities/nvidia-isaac-sim.md)'s RTX lidar is ray-traced, but Isaac Sim does not run on Jetson. Whether any on-robot workload touches these units is unknown, and they are 8 units on the largest SKU — unlikely to matter either way.
- **Thor (Blackwell)** — RT-core configuration not checked.
