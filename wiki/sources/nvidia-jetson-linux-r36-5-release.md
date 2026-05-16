---
title: NVIDIA Jetson Linux R36.5 release page
type: source
url: https://developer.nvidia.com/embedded/jetson-linux-r365
author: NVIDIA Corporation
published: 2024 (release page)
ingested: 2026-05-16
tags: [jetson, jetson-linux, l4t, r36-5, bsp]
---

## Summary
Release landing page for **Jetson Linux R36.5**, NVIDIA's L4T BSP for Orin-class Jetsons. Ubuntu 22.04 rootfs, Linux kernel 5.15, UEFI bootloader, OP-TEE TEE, NVIDIA drivers. Supports all production Jetson AGX Orin, Orin NX, and Orin Nano modules plus the AGX Orin and Orin Nano Developer Kits. Page is primarily a download index; release-content highlights are limited to "fixes for known issues and security vulnerabilities" — the substantive changes live in the release-notes PDF.

## Key claims

### Platform
- Ubuntu **22.04**-based root filesystem.
- Linux Kernel **5.15**.
- **UEFI bootloader**.
- **OP-TEE** Trusted Execution Environment.

### Supported modules
- All production **Jetson AGX Orin** modules.
- All production **Jetson Orin NX** modules.
- All production **Jetson Orin Nano** modules.
- **AGX Orin** and **Orin Nano** Developer Kits.

### Downloadable components listed
- Driver Package (BSP).
- Sample Root Filesystem.
- Jetson Linux API Reference.
- BSP source package.
- Root-filesystem source package.
- WebRTC, toolchains, OTA tools, FSKP tools.

### What's new
- "Fixes for known issues and security vulnerabilities." (No feature-comparison detail on the page itself.)

## Entities mentioned
- [Jetson Linux](../entities/jetson-linux.md)
- [JetPack](../entities/jetpack.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- None directly.

## Open questions
- Exact release date and CUDA/TensorRT bundle versions are not on this page — pull from the [release-notes PDF](https://docs.nvidia.com/jetson/archives/r36.5/ReleaseNotes/Jetson_Linux_Release_Notes_r36.5.pdf) if those become load-bearing.
- The page implies but does not enumerate compatibility with **Jetson AGX Xavier** / **Xavier NX** — R36.x is Orin-only; Xavier-class lifecycle is on the older 35.x track. Worth confirming in a dedicated ingest.
