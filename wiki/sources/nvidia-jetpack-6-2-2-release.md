---
title: NVIDIA JetPack SDK 6.2.2 release page
type: source
url: https://developer.nvidia.com/embedded/jetpack-sdk-622
author: NVIDIA Corporation
published: 2025 (release page)
ingested: 2026-05-16
tags: [jetson, jetpack, jetpack-6, l4t, r36-5, cuda, tensorrt, apriltag]
---

## Summary
Release page for **JetPack 6.2.2**, "the latest production release of JetPack 6." Bundles Jetson Linux 36.5 (kernel 5.15, Ubuntu 22.04 rootfs) and the standard Orin AI stack: CUDA 12.6.10, cuDNN 9.3.0, TensorRT 10.3.0, DeepStream 7.1, VPI 3.2, DLA 3.14. New since prior 6.x: a built-in **AprilTag Detector and Pose Estimator** in VPI, Dynamic Remap and Recursive Gaussian Filter, expanded PVA backend support (up to 5× speedup), and Hardware Security Module (HSM) support for boot-image signing. Three install paths: SD-card image (Orin Nano starts at 6.2.1 then apt-upgrades to 6.2.2), SDK Manager, or `apt install nvidia-jetpack`.

## Key claims

### Bundled versions
- Jetson Linux: **36.5** (kernel 5.15, Ubuntu 22.04 rootfs)
- CUDA **12.6.10**
- cuDNN **9.3.0**
- TensorRT **10.3.0**
- DeepStream **7.1**
- VPI **3.2**
- DLA **3.14**

### New features vs prior 6.x
- **AprilTag Detector and Pose Estimator** in VPI — NVIDIA's first-party, GPU/PVA-accelerated AprilTag pipeline. Significant for [AprilTags](../concepts/robotics/apriltags.md) consumers (FRC teams, research robots).
- Dynamic Remap.
- Recursive Gaussian Filter.
- Expanded PVA backend support — "Up-to 5X speed up of PVA backends."
- HSM support for boot image signing (security hardening).

### Install paths
- **SD card image** (Orin Nano): NVIDIA ships a JetPack 6.2.1 / Jetson Linux 36.4.4 SD image; users apt-upgrade to 6.2.2 after first boot.
- **SDK Manager** flashing for all Jetson Orin platforms.
- **Debian package**: `sudo apt install nvidia-jetpack` on a running Jetson.

### Supported hardware
- Jetson Orin Nano Developer Kit and Jetson AGX Orin Developer Kit are explicitly called out.
- Broader Jetson Orin family (Orin NX modules etc.) implied; the release-notes PDF would be authoritative.

### Cross-references shown on the page
- [JetPack Documentation index](https://docs.nvidia.com/jetson/jetpack/index.html) — see [JetPack docs index](nvidia-jetpack-docs-index.md).
- [Jetson Linux 36.5 Release Notes](https://docs.nvidia.com/jetson/archives/r36.5/ReleaseNotes/Jetson_Linux_Release_Notes_r36.5.pdf).
- [JetPack 6.2.1 SD card image download](https://developer.nvidia.com/downloads/embedded/L4T/r36_Release_v4.4/jp62-r1-orin-nano-sd-card-image.zip).

## Entities mentioned
- [JetPack](../entities/jetpack.md)
- [Jetson Linux](../entities/jetson-linux.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- [AprilTags](../concepts/robotics/apriltags.md) — JetPack 6.2.2 ships a first-party AprilTag detector/pose-estimator in VPI.

## Open questions
- Release date not explicit on the page; needs the release-notes PDF to pin.
- VPI AprilTag detector: which tag families (16h5, 25h9, 36h11)? Pose-estimation accuracy vs apriltag-library reference? Worth a dedicated ingest of the VPI AprilTag docs.
- Does the 6.2.2 apt upgrade from 6.2.1 cover the QSPI bootloader, or only userspace? (Cross-reference with [R36.5 update mechanism](nvidia-jetson-linux-r36-5-update-mechanism.md).)
