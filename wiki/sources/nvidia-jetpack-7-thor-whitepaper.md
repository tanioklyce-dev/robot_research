---
title: "JetPack 7.0 for Jetson Thor — software stack reference (NVIDIA)"
type: source
url: https://forums.developer.nvidia.com/t/jetpack-7-0-jetson-linux-38-2-for-nvidia-jetson-thor-is-now-live/343128
secondary_urls:
  - https://developer.nvidia.com/blog/unlock-faster-smarter-edge-models-with-7x-gen-ai-performance-on-nvidia-jetson-agx-thor/
  - https://developer.nvidia.com/embedded/jetpack
  - https://docs.nvidia.com/jetson/archives/r38.2/ReleaseNotes/Jetson_Linux_Release_Notes_r38.2.pdf
author: NVIDIA Developer (forum announcement) + NVIDIA Technical Blog
published: 2025-08-25 (release announcement); 2025-10-15 (generative-AI performance blog)
ingested: 2026-05-17
tags: [jetpack-7, jetson-linux-38, jetson-thor, cuda-13, tensorrt-10, blackwell, mig, real-time-kernel, sbsa, holoscan, nvfp4, llama, deepseek]
---

> [!note] Ingest depth and provenance
> **No formal "JetPack 7 for Jetson Thor white paper" PDF exists** — the [Jetson Thor launch newsroom page](nvidia-jetson-thor-launch-newsroom.md) refers to a whitepaper that NVIDIA never published under that exact name. This source page fills the gap by combining the two authoritative NVIDIA primary materials:
>
> 1. **JetPack 7.0 / Jetson Linux 38.2 release announcement** on NVIDIA Developer Forums (2025-08-25) — the canonical software-stack contents.
> 2. **"Unlock Faster, Smarter Edge Models with 7x Gen AI Performance on NVIDIA Jetson AGX Thor"** technical blog (2025-10-15) — the post-launch performance evolution + quantization story.
>
> Together these cover what a whitepaper would: kernel, OS, library versions, real-time + MIG features, and quantified generative-AI throughput on Thor. Treat as **derived-primary** — verbatim numbers from NVIDIA, but extracted from two posts rather than one consolidated document.

## Summary

JetPack 7.0 is the **Thor-only launch SDK** (parallel to the JetPack 6.x line that continues to serve Orin-class modules). It's a **cloud-native, SBSA-aligned ARM server-style** software stack: Ubuntu 24.04 LTS root filesystem on Linux kernel 6.8, CUDA 13 / cuDNN 9.12 / TensorRT 10.13, with **Multi-Instance GPU (MIG)**, an **NVIDIA-optimized preemptible real-time kernel**, and **CSI-over-Ethernet (CoE) via Holoscan Sensor Bridge**. The post-launch story is the **7× generative-AI throughput improvement** between August and September 2025, driven by **NVFP4** (Blackwell's 4-bit floating point) and speculative decoding.

This page is the canonical wiki reference for **what JetPack 7 actually contains** and **what Thor can do at the AI-workload level** as of late 2025.

## Release facts (forum announcement)

- **Release date**: **2025-08-25** — same day as the [Jetson Thor launch newsroom announcement](nvidia-jetson-thor-launch-newsroom.md).
- **Hardware supported**: [Jetson AGX Thor Developer Kit](../entities/jetson-thor.md) + the Thor-based **T5000 module**.

## Core software stack (verbatim from forum)

| Component | Version |
| --- | --- |
| Linux kernel | **6.8** |
| Userspace base | **Ubuntu 24.04 LTS** |
| CUDA | **13** |
| cuDNN | **9.12** |
| TensorRT | **10.13** |

Note: this **overrides** the prior wiki claim ([jetpack.md](../entities/jetpack.md)) that JetPack 7 paired with Jetson Linux R37.x. The actual pairing is **Jetson Linux 38.2** (the R38 line, distinct from the R36.x line that backs JetPack 6).

## Architectural commitments

- **SBSA alignment** — JetPack 7.0 implements **Server Base System Architecture**, the ARM-industry standard that positions Thor as a server-class platform rather than a bespoke embedded SoC. This is the structural move that lets Thor run cloud-native software unchanged.
- **NVIDIA optimized preemptible real-time kernel** — ships in the release; previously a custom-build feature on Orin.
- **Multi-Instance GPU (MIG)** — Thor's Blackwell GPU can be partitioned into isolated instances for multi-workload deployment. New on Jetson (was previously a data-center feature).
- **Cloud-native, modular** — explicit framing in the forum post.

## Sensor / camera interface

- **CSI / GMSL** via **Argus**.
- **CoE (CSI over Ethernet)** via **SIPL Camera API**, made possible by the **Holoscan Sensor Bridge**.
- Out-of-the-box support for the **Eagle Camera Sensor Module LI-VB1940**.

## Supported AI serving frameworks (from forum)

- **vLLM**
- **SGLang**
- **MLC**
- **llama.cpp**
- **Ollama**
- **Hugging Face Transformers**

## Generative-AI performance trajectory (blog, 2025-10-15)

The blog post's headline claim is a **7× generative-AI throughput increase** from Thor's August launch to mid-September 2025, driven by software/quantization improvements on the same hardware.

| Model | Aug 2025 (launch) | Sept 2025 | With speculative decoding |
| --- | --- | --- | --- |
| Llama 3.3 70B | 12.64 tok/s | **41.5 tok/s** | **88.62 tok/s** (EAGLE-3) |
| DeepSeek R1 70B | 11.5 tok/s | **40.29 tok/s** | — |
| Llama 3.3 W4A16 | 6.27 tok/s | — | **16.19 tok/s** (2.5× uplift) |

All numbers are **single-Thor**, output tokens/sec.

## Quantization formats supported

- **FP8**
- **W4A16** (4-bit weights, 16-bit activations)
- **NVFP4** — Blackwell-generation 4-bit floating point, the load-bearing format for the 7× claim. This is the format underneath Thor's headline FP4-sparse TFLOPS spec.

## Why it matters in this wiki

- **Closes the dangling "JetPack 7 whitepaper" reference** in [Jetson Thor launch newsroom](nvidia-jetson-thor-launch-newsroom.md).
- **Corrects the Jetson Linux pairing** documented on [jetpack.md](../entities/jetpack.md) — it's **R38.2 (kernel 6.8 / Ubuntu 24.04)**, not R37.x. This is a non-trivial bookkeeping fix because R37 vs R38 implies different kernel and userspace versions.
- **Quantifies the FP4 promise** that the [Jetson Thor product page](nvidia-jetson-thor-product-page.md) gave as a peak TFLOPS number. The 7× headline shows the gap between launch-day untuned performance and post-launch software-optimized performance on the same silicon — a useful prior for any "how fast will an LLM run on Thor" question.
- **MIG on Jetson** is genuinely new — the wiki's prior Thor entity didn't mention this. Implications for multi-model deployment on a single Thor (a VLM in one MIG instance, a VLA in another) deserve a follow-up.

## Entities mentioned

- [Jetson Thor](../entities/jetson-thor.md) — the hardware.
- [NVIDIA](../entities/nvidia.md) — vendor.
- [JetPack SDK](../entities/jetpack.md) — the umbrella entity for the SDK line.
- [Jetson Linux (L4T)](../entities/jetson-linux.md) — the BSP layer; gets a new R38.x section after this ingest.

## Concepts touched

- Multi-Instance GPU (MIG) on Jetson — new behavior on the embedded line.
- NVFP4 and W4A16 quantization on Blackwell.
- SBSA as the structural commitment that makes Thor a cloud-native deployment target.

## Open questions / TBD

- **What's the per-MIG-instance perf envelope?** The blog reports single-Thor numbers; no per-instance breakdown.
- **JetPack 7.1 timeline** — referenced in the [forum thread](https://forums.developer.nvidia.com/t/jetpack-7-1-when-will-it-be-released/351191) but not yet released as of this ingest.
- **Isaac ROS 4.0 on Thor specifics** — [jetpack.md](../entities/jetpack.md) names Isaac ROS 4.0 as the Thor-compatible release; neither primary source confirms a specific Isaac ROS version number alongside JetPack 7.0. Worth checking when Isaac ROS 4.0 documentation surfaces.
- **GR00T and Cosmos on Thor** with specific runtime numbers — not in either primary source. The Thor product page suggests both run; this whitepaper-stand-in doesn't quantify.
- **DeepStream, VPI, Holoscan versions** — not enumerated in the forum post the way CUDA / cuDNN / TensorRT are. The release notes PDF on docs.nvidia.com would close this if ingested.
