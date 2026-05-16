---
title: Jetson Linux R36.5 — Software Packages and the Update Mechanism
type: source
url: https://docs.nvidia.com/jetson/archives/r36.5/DeveloperGuide/SD/SoftwarePackagesAndTheUpdateMechanism.html
author: NVIDIA Corporation
published: 2024 (R36.5 Developer Guide archive)
ingested: 2026-05-16
tags: [jetson, jetson-linux, l4t, r36-5, apt, ota, updates]
---

## Summary
Developer-Guide chapter explaining how Jetson Linux 36.5 distributes and updates its system software through NVIDIA's Debian repositories. Defines the scope of `apt`-based updates (kernel, drivers, firmware, CUDA, multimedia, configs — 80+ packages), distinguishes point releases (apt upgrade) from minor releases (edit sources.list + apt dist-upgrade), and draws a hard line: **35.x → 36.x is NOT supported via apt**; that transition requires a full reflash. Also notes that the `nvidia-l4t-bootloader` package handles QSPI bootloader payloads separately from rootfs.

## Key claims

### What apt updates cover
- "OTA updates may include changes to the firmware in the QSPI flash memory, as well as the Linux userspace and kernel driver packages."
- 80+ packages including `nvidia-l4t-kernel`, `nvidia-l4t-cuda`, `nvidia-l4t-firmware`, graphics libs (GL/EGL), camera utilities, multimedia packages, device tree files, system configs.

### Update commands

**Point release** (e.g. 36.4 → 36.5):
```bash
sudo apt update
apt list --upgradable        # see what's available
sudo apt upgrade
```

**Minor release** (e.g. 36.2 → 36.3):
- Edit `/etc/apt/sources.list.d/nvidia-l4t-apt-source.list` to point at the new release.
- Then:
```bash
sudo apt update
sudo apt dist-upgrade
```

### What apt does NOT cover
- Major-release migrations: "Upgrading from release 35.x to release 36.x is not supported." → full reflash required.
- Image-based OTA (separate mechanism) supports A/B rootfs partitions; apt updates do not have a rollback path.

### Bootloader / QSPI
- The `nvidia-l4t-bootloader` package carries Tegra bootloader update payloads. Bootloader updates flow through apt but are applied to QSPI separately from rootfs package installs.

### Compatibility constraints (warnings)
- "These packages are only verified with the root filesystem shipped in this L4T BSP release."
- Do not install OTA packages on non-Jetson-Linux Ubuntu installs.
- "NVIDIA advises against installing a combination of packages from different releases."
- The system enforces `nvidia-l4t-core` version-match across all Jetson packages — partial upgrades are blocked.

## Entities mentioned
- [Jetson Linux](../entities/jetson-linux.md)
- [JetPack](../entities/jetpack.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- None directly — operational reference.

## Open questions
- The page does not enumerate which exact QSPI-firmware payloads ship in `nvidia-l4t-bootloader` for R36.5. Worth pulling from the release notes.
- For [Jetson Orin Nano](../entities/jetson-orin-nano.md) specifically: is bootloader update through apt sufficient to enable NVMe boot on pre-mid-2023 dev kits, or is an SDK-Manager reflash still required? (Cross-reference with [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md).)
