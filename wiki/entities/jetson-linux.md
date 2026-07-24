---
title: Jetson Linux (L4T)
type: entity
created: 2026-05-16
updated: 2026-05-17
sources: 9
tags: [nvidia, jetson, l4t, jetson-linux, bsp, linux, ubuntu, jetson-thor]
---

# Jetson Linux (L4T)

NVIDIA's **Board Support Package** (BSP) for Jetson modules — the OS layer underneath [JetPack](jetpack.md). Historically branded "Linux for Tegra" (L4T). Provides the rootfs, kernel, bootloader, drivers, and firmware; everything sits on top via JetPack components.

## Current release — R36.5

**R36.5** is the supported line for Orin-class Jetsons ([Jetson Linux R36.5 release](../sources/nvidia-jetson-linux-r36-5-release.md), [R36.5 release notes PDF](../sources/nvidia-jetson-linux-r36-5-release-notes.md)). R36.5 is positioned as a **security-focused minor release** that pairs with [JetPack 6.2.2](../sources/nvidia-jetpack-6-2-2-release.md):

- **Ubuntu 22.04** rootfs.
- **Linux kernel 5.15 LTS** (modules under `/lib/modules/5.15.116-release-tegra/`).
- **UEFI bootloader** (replacing the older U-Boot-derived Tegra bootloader chain). UEFI source is maintained publicly on GitHub.
- **OP-TEE** Trusted Execution Environment.
- NVIDIA drivers (GPU, multimedia, camera).
- Cross-compile toolchain: **Bootlin GCC 11.3**.
- Release tag: `jetson_36.5`.
- **Host OS for flashing**: Ubuntu 20.04 OR 22.04 x86_64 (both supported per release notes).

> [!note]
> Under UEFI, the legacy **plugin manager is no longer supported** — peripheral registration (cameras, etc.) must use device tree overlays (`.dtbo`) or the Jetson-IO tool ([release notes §4.2](../sources/nvidia-jetson-linux-r36-5-release-notes.md)).

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
2. **`l4t_initrd_flash.sh`** — CLI flasher inside the BSP archive; supports NVMe / USB / SD as the rootfs target. An intermittent near-completion failure ("Either the device cannot mount the NFS server...") was **fixed in R36.5** ([release notes §3](../sources/nvidia-jetson-linux-r36-5-release-notes.md), issue 4695663).

Each platform has a `.conf` basename used with `flash.sh`:

| Config | Target |
|---|---|
| `jetson-orin-nano-devkit.conf` | Orin Nano 4GB/8GB, SD-Card dev-kit module, Orin NX 8GB/16GB on the P3768-0000 carrier |
| `jetson-orin-nano-devkit-super.conf` | Same modules, **Super Mode** — 25W Orin Nano, 40W Orin NX, MAXN_SUPER ([Platform Power and Performance — Orin series](../sources/nvidia-jetson-platform-power-performance-orin.md)) |
| `jetson-orin-nano-devkit-super-maxn.conf` | Super profiles + conservative thermal config for sustained MAXN_SUPER workloads |
| `jetson-agx-orin-devkit.conf` | AGX Orin dev-kit module + AGX Orin 32GB/64GB on the P3737-0000 carrier |
| `jetson-agx-orin-devkit-industrial.conf` | AGX Orin Industrial (P3701-0008) |

> [!warning]
> **Multi-boot-media versions must match** ([release notes §2.1](../sources/nvidia-jetson-linux-r36-5-release-notes.md), issue 4201479): flashing different BSP versions to USB + NVMe corrupts UEFI overlay partitions and crashes the system.

See [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md) for the concrete Orin Nano + NVMe procedure.

## Relationship to JetPack

[JetPack](jetpack.md) **bundles Jetson Linux**. JetPack 6.x maps to L4T R36.x; JetPack 5.x mapped to R35.x. The OS layer can be upgraded by itself via apt; the wider JetPack stack (CUDA, TensorRT, etc.) follows the same release cadence and is installed alongside via `nvidia-jetpack`.

## R38 line — Jetson Thor track

The Blackwell-generation [Jetson Thor](jetson-thor.md) ships on a separate L4T line, **Jetson Linux 38.2**, bundled with [JetPack 7.0](jetpack.md) at Thor's launch (2025-08-25). Key differences vs the R36.x line ([JetPack 7.0 for Jetson Thor software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md)):

| Axis | R36.x (Orin) | R38.2 (Thor) |
|---|---|---|
| Linux kernel | 5.15 LTS | **6.8** |
| Ubuntu rootfs | 22.04 | **24.04 LTS** |
| Architectural framing | embedded BSP | **SBSA-aligned**, server-class ARM |
| Real-time | not in default kernel | **preemptible real-time kernel** ships in release |
| GPU partitioning | n/a | **Multi-Instance GPU (MIG)** |
| Sensor bridge | CSI / GMSL via Argus | adds **CSI-over-Ethernet** via Holoscan Sensor Bridge |

R36.x continues as the Orin line; R38.2 is Thor-only. The two lines are parallel, not sequential.

## Mentioned in
- [Jetson Orin Nano](jetson-orin-nano.md)
- [JetPack](jetpack.md)
- [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md)
- [NVIDIA](nvidia.md)
- [Jetson Linux R36.5 release](../sources/nvidia-jetson-linux-r36-5-release.md)
- [Jetson Linux R36.5 release notes (PDF)](../sources/nvidia-jetson-linux-r36-5-release-notes.md)
- [Platform Power and Performance — Orin series](../sources/nvidia-jetson-platform-power-performance-orin.md)
- [Jetson Linux R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)
- [JetPack 6.2.2 release](../sources/nvidia-jetpack-6-2-2-release.md)
- [JetPack docs index](../sources/nvidia-jetpack-docs-index.md)
- [NVIDIA Jetson Orin Nano Dev Kit software setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)
- [JetPack 7.0 for Jetson Thor software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md) — primary source for the R38.2 / kernel 6.8 / Ubuntu 24.04 line.
