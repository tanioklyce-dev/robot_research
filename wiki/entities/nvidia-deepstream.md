---
title: NVIDIA DeepStream
type: entity
subtype: software
created: 2026-07-16
updated: 2026-07-16
sources: 1
tags: [nvidia, deepstream, video-analytics, gstreamer, tensorrt, metropolis, jetson, perception, computer-vision, edge-ai]
---

# NVIDIA DeepStream

**DeepStream** — NVIDIA's **streaming-analytics SDK** for AI video/image understanding: a **GStreamer-based** framework for building **multi-stream, multi-model inference pipelines** on NVIDIA GPUs, from edge [Jetson](jetson-thor.md) to data-center dGPU.

## What it does

Composes hardware-accelerated **decode/encode** + **TensorRT** inference + object detection/tracking + message-broker output into real-time **intelligent video analytics (IVA)** pipelines. It's the perception plumbing under the **NVIDIA Metropolis** platform (and the Metropolis **VSS** used by [Halos Outside-In](nvidia-halos.md)).

## Facts

- **Version**: DeepStream **9.1** (July 2026). Requirements: Ubuntu 24.04, CUDA 13.2, TensorRT 10.16.x, driver 595+.
- **Hardware**: x86 dGPU, **Jetson** (edge), SBSA / DGX Spark (ARM).
- **Ecosystem**: NVIDIA TAO (training), Triton (serving), Metropolis (IVA platform).
- **License**: CC-BY-4.0 (docs) + Apache-2.0 (code) + proprietary binaries under NVIDIA SDK EULA.

## Relevance to robotics

A **classical vision-AI pipeline** (not a learned policy) — the production tool for **multi-camera synchronized perception**. Its wiki tie is **infrastructure-side safety**: [Halos Outside-In](nvidia-halos.md)'s perception stage runs on Metropolis VSS (DeepStream lineage) to track workers/forklifts and gate an AMR's safe zone. Distinct from [Isaac ROS](isaac-ros.md) (robot-centric perception: VSLAM, nvblox) — see the DeepStream source's open question on where the boundary sits.

## Mentioned in

- [NVIDIA DeepStream SDK (GitHub)](../sources/nvidia-deepstream-github.md)

## Related

- [NVIDIA](nvidia.md), [Jetson Thor](jetson-thor.md), TensorRT
- [NVIDIA Halos](nvidia-halos.md) — consumes Metropolis-VSS (DeepStream-lineage) perception for Outside-In safety
