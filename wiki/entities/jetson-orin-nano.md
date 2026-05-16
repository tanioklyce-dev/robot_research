---
title: Jetson Orin Nano
type: entity
created: 2026-05-16
updated: 2026-05-16
sources: 7
tags: [jetson, nvidia, edge-ai, hardware, robotics-compute]
---

# Jetson Orin Nano

NVIDIA's entry-tier edge-AI compute module in the **Jetson Orin** family — Ampere-architecture GPU + ARM Cortex CPU on a small board, designed for robotics, generative AI inference, and embedded vision. The reference platform for the **Jetson Orin Nano Developer Kit** and the underlying compute on multiple wiki-tracked robots (Hiwonder [ROSOrin Pro](rosorin-pro.md), [ROSOrin](rosorin.md), and others).

## Variants

- **Module**: bare SoM (system-on-module) that slots into custom carrier boards. Two production memory tiers: 4 GB (P3767-0004) and 8 GB (P3767-0003). The Developer Kit module with onboard SD card is P3767-0005 ([R36.5 release notes](../sources/nvidia-jetson-linux-r36-5-release-notes.md) §1.1).
- **Developer Kit**: NVIDIA's reference carrier board (**P3768-0000**) for the 8 GB module, with M.2 Key-M NVMe slot, microSD slot, USB-C, USB-A, Gigabit Ethernet, MIPI CSI camera connectors, 12-pin button header (includes FC REC + GND for force-recovery mode), DC barrel jack ([NVIDIA Software Setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)).
- **Sibling on the same carrier**: the P3768-0000 carrier also accepts **Jetson Orin NX** modules (8 GB P3767-0001 / 16 GB P3767-0000) — same flash config (`jetson-orin-nano-devkit.conf`) handles all five SKUs.
- **Custom carrier integrations**: Hiwonder [ROSOrin Pro](rosorin-pro.md) and [ROSOrin](rosorin.md) both ship Orin Nano as one of the compute options ([Hiwonder ROSOrin Pro user manual](../sources/hiwonder-rosorin-pro-user-manual.md)).

## Power modes

R36.5 ships two flash-time power-mode profiles ([R36.5 release notes](../sources/nvidia-jetson-linux-r36-5-release-notes.md) §1.1):

- **Standard** (`jetson-orin-nano-devkit.conf`): factory-default power envelopes.
- **Super Mode** (`jetson-orin-nano-devkit-super.conf`): **25 W** for Orin Nano modules, **40 W** for Orin NX modules, MAXN for all — NVIDIA's "Super Mode" performance unlock. See the *Supported Modes and Power Efficiency* chapter of the Jetson Linux Developer Guide for details.

## Software stack

- **OS / BSP**: [Jetson Linux](jetson-linux.md) — currently the R36.5 line (Ubuntu 22.04 + kernel 5.15 + UEFI + OP-TEE) for Orin-class modules ([Jetson Linux R36.5](../sources/nvidia-jetson-linux-r36-5-release.md)).
- **SDK**: [JetPack](jetpack.md) — bundles Jetson Linux + CUDA + cuDNN + TensorRT + DeepStream + VPI on top. Current production release **JetPack 6.2.2** as of mid-2025 ([JetPack 6.2.2 release page](../sources/nvidia-jetpack-6-2-2-release.md)).
- **No eMMC**: the Orin Nano module has no onboard mass storage. Booting requires microSD or NVMe; on the Dev Kit the M.2 slot is the recommended path. NVMe boot requires a sufficiently new QSPI bootloader — pre-mid-2023 Dev Kits need a bootloader update before NVMe is bootable ([Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md)).

## Setup paths

- **microSD image**: NVIDIA publishes an SD card image (JetPack 6.2.1 / Jetson Linux 36.4.4 base, apt-upgradable to 6.2.2). Flash with Etcher or `dd`, insert, boot.
- **SDK Manager** flashing from a Linux x86_64 host with the kit in force-recovery mode (short FC REC + GND on the 12-pin header, plug in DC power, connect USB-C) — NVIDIA's official host OS is **Ubuntu 20.04** for this workflow ([NVIDIA Software Setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)).
- **Command-line flash** with `l4t_initrd_flash.sh` from the BSP — supports NVMe target directly. See [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md) for the full command.

## Updates

In-place updates use apt against NVIDIA's L4T Debian repository: `apt update && apt upgrade` for point releases; edit `/etc/apt/sources.list.d/nvidia-l4t-apt-source.list` then `apt dist-upgrade` for minor releases. The `nvidia-l4t-bootloader` package carries QSPI bootloader payloads. **Crossing major versions (e.g. 35.x → 36.x) is NOT supported via apt — full reflash required** ([R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)).

## Robotics use cases in the wiki

- [Hiwonder ROSOrin Pro](rosorin-pro.md) — 6-DOF arm + mobile-base humanoid arm kit; Orin Nano is one of four supported compute options ([Hiwonder ROSOrin Pro user manual](../sources/hiwonder-rosorin-pro-user-manual.md)).
- [Hiwonder ROSOrin](rosorin.md) — base mobile-platform variant with the same compute-option matrix.
- See [Robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md) and [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) for where Orin Nano sits in the broader compute landscape.

## Open questions

- Exact module-level performance figures (TOPS, GPU clock, memory bandwidth) are not in any currently-ingested source. A datasheet ingest would let the wiki cite specifics.
- VPI 3.2 in JetPack 6.2.2 ships a native [AprilTags](../concepts/robotics/apriltags.md) detector/pose-estimator — Orin Nano performance vs CPU `apriltag` library and Coral TPU would be a useful comparison.

## Mentioned in
- [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md)
- [LeWM on ROSOrin Pro feasibility](../syntheses/projects/lewm-on-rosorin-pro-feasibility.md)
- [ROSOrin Pro Lego pick-and-place](../syntheses/projects/rosorin-pro-lego-pick-place.md)
- [Robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md)
- [LLM-agent architecture across stacks](../syntheses/agents/llm-agent-architecture-across-stacks.md)
- [Hiwonder ROSOrin Pro user manual](../sources/hiwonder-rosorin-pro-user-manual.md)
- [Hiwonder ROSOrin docs](../sources/hiwonder-rosorin-docs.md)
- [NVIDIA Jetson Orin Nano Dev Kit software setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)
- [JetPack 6.2.2 release](../sources/nvidia-jetpack-6-2-2-release.md)
- [Jetson Linux R36.5 release](../sources/nvidia-jetson-linux-r36-5-release.md)
- [Jetson Linux R36.5 release notes (PDF)](../sources/nvidia-jetson-linux-r36-5-release-notes.md)
- [Jetson Linux R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)
