---
title: Jetson Orin Nano Developer Kit — Software Setup (NVIDIA Developer)
type: source
url: https://developer.nvidia.com/embedded/learn/jetson-orin-nano-devkit-user-guide/software_setup.html
author: NVIDIA Corporation
published: undated (Developer Kit user guide)
ingested: 2026-05-16
tags: [jetson, jetson-orin-nano, nvidia, setup, sdk-manager, recovery-mode]
---

## Summary
NVIDIA's official software-setup chapter of the Jetson Orin Nano Developer Kit user guide. Covers two paths to get software onto the kit: (1) flashed microSD card (delegates first-boot details to a separate *Getting Started* page) and (2) NVIDIA SDK Manager on a Linux x86_64 host, with the kit in force-recovery mode connected over USB-C. Establishes host requirements and the recovery-mode jumper procedure.

## Key claims

### microSD path
- "You can start using Jetson Orin Nano Developer Kit right away by simply inserting a flashed microSD card and power it on."
- The specific image filename, download URL, and Etcher/flash steps are not in this chapter — they live in *Getting Started with Jetson Orin Nano Developer Kit*.

### SDK Manager path — host requirements
- **Ubuntu Desktop 20.04 on x86_64** (host machine).
- **System memory**: 8 GB minimum.
- **Free disk space**: 25 GB minimum.

### SDK Manager path — recovery-mode procedure
- "Connect NVIDIA Jetson Orin Nano Developer Kit to the PC with a USB Type-C cable. While shorting the `FC REC` pin and `GND` pin of the 12-pin header under the module, insert the power supply plug into the DC jack."

### SDK Manager path — component selection
- To flash the L4T image only: select **Jetson OS** component.
- To install runtime SDK libraries (CUDA, cuDNN, TensorRT, etc.): deselect **Jetson OS** and select **Jetson SDK Components**.

### What this page does NOT cover
- NVMe-specific install / SSD boot steps.
- QSPI bootloader prerequisites.
- Specific JetPack / L4T version numbers.
- Power-supply warnings.

## Entities mentioned
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [JetPack](../entities/jetpack.md)
- [Jetson Linux](../entities/jetson-linux.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- None directly — this is an operational reference.

## Open questions
- The page's silence on NVMe boot means the *user-facing* documentation for SSD setup on the Orin Nano lives elsewhere (release notes, developer guide, or community posts). Worth identifying the canonical NVMe-boot doc.
- Host-OS support: this page lists 20.04 only; later SDK Manager releases support 22.04 — version-by-version host compatibility deserves its own ingest.
