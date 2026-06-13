---
title: Jetson Orin Nano
type: entity
created: 2026-05-16
updated: 2026-06-13
sources: 10
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

R36.5 ships three flash-time power-mode profiles ([R36.5 release notes](../sources/nvidia-jetson-linux-r36-5-release-notes.md) §1.1, [Platform Power and Performance — Orin series](../sources/nvidia-jetson-platform-power-performance-orin.md)):

- **Standard** (`jetson-orin-nano-devkit.conf`): factory-default envelopes (4GB → 10W default; 8GB → 15W default). Cannot enter the 25W or MAXN_SUPER profiles.
- **Super Mode** (`jetson-orin-nano-devkit-super.conf`): unlocks **25 W** and **MAXN_SUPER** (peak 1728 MHz CPU / 1020 MHz GPU / 3199 MHz memory). NVIDIA's performance unlock for Orin Nano.
- **Super + maxn-thermal** (`jetson-orin-nano-devkit-super-maxn.conf`): Super profiles with more conservative thermal settings for sustained MAXN_SUPER workloads — the recommended choice if the application will sit at peak performance for prolonged periods.

> [!warning]
> Super Mode is hardware-locked at **flash time**. A module flashed with the standard config physically cannot reach the 25W or MAXN_SUPER profiles — reflashing with the `-super` variant is the only path to unlock them ([Platform Power and Performance — Orin series](../sources/nvidia-jetson-platform-power-performance-orin.md)).

### 8GB module (P3767-0003) — headline figures

| Mode | Power | CPU max | GPU max | Memory max |
|---|---|---|---|---|
| Standard 15W (default) | 15 W | 1510 MHz / 6 cores | 625 MHz | 2133 MHz |
| Standard 7W | 7 W | 960 MHz / 4 cores | 408 MHz | 2133 MHz |
| Super 15W | 15 W | 1498 MHz / 6 cores | 612 MHz | 2133 MHz |
| Super 25W | 25 W | 1344 MHz / 6 cores | 918 MHz | 3199 MHz |
| **Super MAXN_SUPER** | n/a | **1728 MHz / 6 cores** | **1020 MHz** | **3199 MHz** |

Step from default 15W to Super 25W: **+47% GPU clock, +50% memory clock** (CPU clock drops slightly). Full peak only at MAXN_SUPER.

### Runtime switching

```bash
sudo /usr/sbin/nvpmodel -m <mode-id>   # set
sudo /usr/sbin/nvpmodel -q             # query
```

Mode persists across reboots and SC7. **Mode IDs are not portable across module variants** — always cross-reference per module.

## Measured performance & robotics deployment

- **Module figures (Super):** **67 INT8 TOPS, 102 GB/s memory bandwidth, 7–25 W** ([Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md)) — the first ingested source to pin these numbers.
- **On-edge policy latency** (Orin Nano, MAXN SUPER, FP16, end-to-end camera→action; [same source](../sources/cutting-the-cord-untethered-xlerobot.md)): **ACT 36 ms → 27.8 Hz** (reactive control ✅); **Diffusion Policy 540 ms → 1.8 Hz**; **SmolVLA-450M 714 ms → 1.4 Hz** (diffusion/flow-matching action heads are the bottleneck, *not* the VLM). No thermal throttling after 30 min continuous SmolVLA (max 54.6 °C).
- **First measured onboard-XLeRobot build:** Correll lab's untethered [XLeRobot](xlerobot.md) embeds the Orin Nano Super ($249) with ~60 W of power headroom on a 288 Wh pack — the **validated default** in the [Jetson onboard-compute comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md).
- **Containerized LeRobot path:** NVIDIA's archived [Jetson AI Lab LeRobot tutorial](../sources/nvidia-jetson-ai-lab-lerobot.md) lists Orin Nano **8 GB** as a supported (but caveated) target for running the full LeRobot teleop→train→eval loop via the `dustynv/lerobot` [jetson-containers](jetson-containers.md) image — the 8 GB tier is the tight one for onboard ACT training.

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

- ~~Exact module-level performance figures (TOPS, GPU clock, memory bandwidth) are not in any currently-ingested source.~~ **Resolved** for the Super tier: **67 INT8 TOPS / 102 GB/s / 7–25 W** ([Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md)). An NVIDIA datasheet ingest would still add per-mode TOPS.
- VPI 3.2 in JetPack 6.2.2 ships a native [AprilTags](../concepts/robotics/apriltags.md) detector/pose-estimator — Orin Nano performance vs CPU `apriltag` library and Coral TPU would be a useful comparison.

## Mentioned in
- [Cutting the Cord (Shaw et al., 2026)](../sources/cutting-the-cord-untethered-xlerobot.md) — measured onboard-XLeRobot build + 67-TOPS / on-edge-VLA-latency numbers.
- [NVIDIA Jetson AI Lab — HuggingFace LeRobot (archived)](../sources/nvidia-jetson-ai-lab-lerobot.md) — Orin Nano 8 GB as a containerized LeRobot target.
- [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — Orin Nano vs AGX Orin vs Thor.
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
- [Platform Power and Performance — Orin series](../sources/nvidia-jetson-platform-power-performance-orin.md)
