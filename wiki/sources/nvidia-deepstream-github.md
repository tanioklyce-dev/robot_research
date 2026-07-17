---
title: "NVIDIA DeepStream SDK (NVIDIA/DeepStream)"
type: source
url: https://github.com/NVIDIA/DeepStream
author: NVIDIA
published: 2026-07 (DeepStream 9.1)
ingested: 2026-07-16
license: CC-BY-4.0 (docs) + Apache-2.0 (code) + proprietary binaries (NVIDIA SDK EULA)
tags: [nvidia, deepstream, video-analytics, gstreamer, tensorrt, metropolis, jetson, perception, computer-vision, edge-ai]
---

## Summary

**DeepStream** is NVIDIA's **streaming-analytics SDK** for AI-based video/image understanding — a **GStreamer-based framework** for building **multi-stream, multi-model inference pipelines** on NVIDIA GPUs. It composes hardware-accelerated decode/encode + **TensorRT** inference + object tracking + message-broker output into real-time video-analytics pipelines that run from **edge ([Jetson](../entities/jetson-thor.md)) to data-center dGPU**. DeepStream is the perception substrate under **NVIDIA Metropolis** — the same **Metropolis / Video Search & Summarization (VSS)** layer the wiki already tracks inside the [Halos Outside-In Safety Blueprint](halos-outside-in-safety-github.md).

## Key claims

- **Architecture**: GStreamer at the core; hardware-accelerated video processing (decode/encode), TensorRT-powered NN inference, detection + multi-object tracking, multi-stream pipeline composition, message-broker integrations.
- **Supported hardware**: x86 dGPU (data-center), **Jetson embedded (edge)**, and **SBSA / DGX Spark** (ARM). Requirements (9.1): Ubuntu 24.04, CUDA 13.2, TensorRT 10.16.x, driver 595+.
- **Ecosystem integration**: **[TAO Toolkit](../entities/nvidia.md)** (train/optimize models), **Triton Inference Server** (serving), **NVIDIA Metropolis** (intelligent video analytics platform).
- **Version**: **DeepStream 9.1**, released **July 2026**.
- **License**: dual CC-BY-4.0 (docs) + Apache-2.0 (code); proprietary binaries under NVIDIA's SDK EULA.

## Relevance to robotics / physical AI

DeepStream is a **classical vision-AI pipeline tool**, not a learned-policy system — but it's the production plumbing for **multi-camera synchronized perception**, which is exactly what infrastructure-side robot safety needs. Its direct wiki tie is **[Halos Outside-In](halos-outside-in-safety-github.md)**, whose perception stage runs on **Metropolis VSS** (a DeepStream-lineage pipeline) to watch workers/forklifts and gate an AMR's safe zone. It's also a candidate on-robot perception layer distinct from the [VLA](../concepts/learning/vla-models.md)/policy compute.

## Entities mentioned

- [NVIDIA DeepStream](../entities/nvidia-deepstream.md) — this SDK
- [NVIDIA](../entities/nvidia.md), [Jetson Thor](../entities/jetson-thor.md), TensorRT

## Concepts touched

- (No dedicated "video analytics" concept page yet — see open questions.)

## Open questions

- **DeepStream vs. [Isaac ROS](../entities/isaac-ros.md)** for on-robot perception — where's the boundary? DeepStream is video-analytics-centric (surveillance/IVA heritage); Isaac ROS is robot-perception-centric (VSLAM, nvblox). Worth a synthesis if both keep recurring.
- Confirm the exact Metropolis-VSS ↔ DeepStream relationship (VSS appears to be built atop DeepStream pipelines, but the Halos coverage doesn't say so explicitly).
