---
title: Jetson Linux (L4T)
type: entity
created: 2026-05-16
updated: 2026-05-16
sources: 3
tags: [nvidia, jetson, l4t, jetson-linux, bsp, linux, ubuntu]
---

# Jetson Linux (L4T)

NVIDIA's **Board Support Package** (BSP) for Jetson modules — the OS layer underneath [JetPack](jetpack.md). Historically branded "Linux for Tegra" (L4T). Provides the rootfs, kernel, bootloader, drivers, and firmware; everything sits on top via JetPack components.

## Current release — R36.5

As of late 2024 / 2025, **R36.5** is the supported line for Orin-class Jetsons ([Jetson Linux R36.5 release](../sources/nvidia-jetson-linux-r36-5-release.md)):

- **Ubuntu 22.04** rootfs.
- **Linux kernel 5.15**.
- **UEFI bootloader** (replacing the older U-Boot-derived Tegra bootloader chain).
- **OP-TEE** Trusted Execution Environment.
- NVIDIA drivers (GPU, multimedia, camera).

### Supported modules

- All production **Jetson AGX Orin** modules.
- All production **Jetson Orin NX** modules.
- All production **[Jetson Orin Nano](jetson-orin-nano.md)** modules.
- **AGX Orin** and **Orin Nano** Developer Kits.

Xavier-class hardware is on the legacy **R35.x** track and not covered by R36.

## Downloadable BSP components

From the [R36.5 release page](../sources/nvidia-jetson-linux-r36-5-release.md):

- **Driver Package (BSP)** — kernel, drivers, flashing tools.
- **Sample Root Filesystem** — Ubuntu 22.04 rootfs tarball.
- Jetson Linux API Reference.
- BSP and rootfs source packages.
- WebRTC, toolchains, OTA tools, FSKP (Field Secure Key Provisioning) tools.

## Update mechanism

Distributed via NVIDIA's **L4T Debian repository**. Three update tiers ([R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)):

1. **Point release** (36.4 → 36.5): `sudo apt update && sudo apt upgrade`. Covers kernel, drivers, CUDA, multimedia, firmware (~80 packages).
2. **Minor release** (36.2 → 36.3): edit `/etc/apt/sources.list.d/nvidia-l4t-apt-source.list` to point at the new release, then `apt update && apt dist-upgrade`.
3. **Major release** (35.x → 36.x): **NOT supported via apt — full reflash required.**

### What's included in apt updates

- Kernel (`nvidia-l4t-kernel`).
- CUDA (`nvidia-l4t-cuda`).
- Firmware (`nvidia-l4t-firmware`).
- QSPI **bootloader** payloads via `nvidia-l4t-bootloader` (applied to QSPI separately from rootfs).
- Device tree files, graphics libraries (GL/EGL), camera utilities, multimedia packages, system configs.

### Compatibility constraints

- Packages "only verified with the root filesystem shipped in this L4T BSP release."
- Mixing packages across releases is explicitly discouraged.
- Partial upgrades are blocked: the system enforces `nvidia-l4t-core` version-match across all Jetson packages.

## Flashing

Two reference paths to put Jetson Linux on a device:

1. **SDK Manager** — GUI flasher; handles QSPI + rootfs for the standard Dev Kits.
2. **`l4t_initrd_flash.sh`** — CLI flasher inside the BSP archive; supports NVMe as the rootfs target.

See [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md) for the concrete Orin Nano + NVMe procedure.

## Relationship to JetPack

[JetPack](jetpack.md) **bundles Jetson Linux**. JetPack 6.x maps to L4T R36.x; JetPack 5.x mapped to R35.x. The OS layer can be upgraded by itself via apt; the wider JetPack stack (CUDA, TensorRT, etc.) follows the same release cadence and is installed alongside via `nvidia-jetpack`.

## Mentioned in
- [Jetson Orin Nano](jetson-orin-nano.md)
- [JetPack](jetpack.md)
- [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md)
- [NVIDIA](nvidia.md)
- [Jetson Linux R36.5 release](../sources/nvidia-jetson-linux-r36-5-release.md)
- [Jetson Linux R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)
- [JetPack 6.2.2 release](../sources/nvidia-jetpack-6-2-2-release.md)
- [JetPack docs index](../sources/nvidia-jetpack-docs-index.md)
- [NVIDIA Jetson Orin Nano Dev Kit software setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)
