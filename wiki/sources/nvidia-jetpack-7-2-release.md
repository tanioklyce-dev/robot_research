---
title: "NVIDIA JetPack 7.2 with Jetson Linux 39.2 — release page"
type: source
url: https://developer.nvidia.com/embedded/jetpack/downloads/archive-7.2
author: NVIDIA
published: 2026-06-02
ingested: 2026-08-16
venue: NVIDIA Developer — JetPack SDK Downloads and Notes
format: web page (curl + tag extraction; WebFetch returns a summary only)
tags: [jetpack, jetpack-7, jetson-linux, l4t, r39-2, jetson-orin, jetson-thor, cuda, tensorrt, isaac-ros, sbsa, yocto, flashing, deepstream, holoscan]
---

# JetPack 7.2 with Jetson Linux 39.2

## Summary

The release that **ends the JetPack 6 / JetPack 7 split**: *"Adds support for the Jetson Orin product family within JetPack 7 releases."* Dated **2026-06-02** (Jetson Linux 39.2), it puts AGX Orin, Orin NX and Orin Nano on the same **Ubuntu 24.04 / kernel 6.8 / CUDA 13.2.1** stack as Jetson Thor, with a **unified ISO-based installer for both Orin and Thor developer kits**.

This is the primary source behind the wiki's [2026-08-16 JetPack correction](../syntheses/platforms/jetson-onboard-compute-xlerobot.md), which had been made from secondary reporting. It confirms the correction and **fixes one number in it** — see below.

## Key claims (verbatim highlights)

- *"Adds support for the Jetson Orin product family within JetPack 7 releases."*
- *"Introduces a unified ISO-based installation method for both Jetson Orin and Jetson Thor developer kits."*
- *"**There is no more SD Card image for Jetson Orin Nano Developer Kit.** Use the unified ISO image to flash the developer kit using a USB stick."*
- *"The manual flashing instructions have slightly changed because of Thor using SBSA architecture. Please follow the manual flashing instructions carefully."*
- *"Adds support for **Jetson AGX Orin 32GB Super Mode (MAXN_SUPER) increasing performance from 200 TOPS to 241 TOPS**."*
- *"Enables **Multi-Instance GPU (MIG) on Jetson Thor T5000** as a technology preview feature."*
- *"Introduces native support for single-command **NemoClaw** installation on developer kits"* and *"Jetson agent skills helping build, configure, optimize and measure performance of the BSP and OSS AI models."*
- *"Includes **Jetson SIPL API Package v2.0.0**, expanding SIPL camera support and introducing a unified camera framework for **GMSL and CoE** use cases."*
- Official **Yocto** recipes via the OE4T GitHub repository; downloadable Yocto images for **AGX Thor, AGX Orin and Orin Nano** (no Orin NX image listed).

**Supported hardware**, as listed: Jetson AGX Thor Developer Kit · Jetson T5000 · Jetson T4000 · **Jetson Orin Family** (not broken out by SKU on this page).

### Component versions

| | |
|---|---|
| Jetson Linux | **39.2** |
| Kernel | **6.8** |
| Distro | **L4T Ubuntu 24.04** (also "Canonical Ubuntu 24.04 for Jetson") |
| CUDA | **13.2.1** |
| cuDNN | 9.20.0 |
| TensorRT | **10.16.2** |
| VPI | 4.1.3 · PVA 2.9.1 |
| Vulkan | 1.4 (Vulkan SC 1.0) · OpenGL 4.6 · GLES 3.2 · EGL 1.5 |
| **OpenWF Display** | **Not supported** |
| V4L2 | 1.22.1 |
| DeepStream | **9.1** |
| Holoscan | 3.9.0 |
| **Isaac ROS** | **"Coming soon"** |
| Jetson Platform Services | **N/A** |
| Container Toolkit | 1.19 (with ISO image) |
| Nsight Systems | 2026.3 |

## The three things that change a build

> [!warning] Isaac ROS is listed as "Coming soon" on JetPack 7.2
> NVIDIA's own SDK table for this release shows **Isaac ROS as not yet available**, and Jetson Platform Services as **N/A**. For a ROS-based robot this is the decisive line in the whole release: **moving an Orin to JetPack 7.2 today means giving up Isaac ROS until it ships.** The wiki's [onboard-compute page](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) describes the Thor tier as "JetPack 7 / Isaac ROS 4"; that pairing is a *roadmap*, not a shipping combination as of this page. Anyone on Isaac ROS should stay on JetPack 6 / L4T 36.x until the status changes.

> [!note] There is a known boot bug on Orin Nano and Orin NX, with a fix you have to apply yourself
> Under "Additional Files": **`overlay_pcie.tbz2`** — *"This overlay fixes an intermittent boot issue caused by initialization failures on some Jetson Orin Nano and Orin NX modules during power cycles or reboots"* (JetPack 7.2 / Jetson Linux 39.2). A robot power-cycles constantly, so an intermittent boot failure on power cycle is close to the worst possible failure mode for an untethered build. **Apply the overlay.**

> [!note] The SD-card era is over for the Orin Nano dev kit
> Confirmed by the primary source, not just by secondary reporting: no SD-card image, unified ISO written to a **USB stick**, which then installs to microSD or NVMe. Manual flashing steps also changed for **SBSA** reasons. See the [flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md), which documents the JetPack 6 flow.

## Correction to the wiki's own correction

The [2026-08-16 correction](../entities/jetpack.md) recorded **CUDA 13.0** for JetPack 7.2, taken from NVIDIA's JetPack landing page. That number belongs to a different sentence: the release notes say *"Jetson Thor now supports a unified **CUDA 13.0 installation across all Arm targets**"* — a statement about **SBSA/Arm-target unification**, not the CUDA version in this bundle. **JetPack 7.2 ships CUDA 13.2.1.** A small error, and a clean illustration of why the primary source was worth ingesting rather than resting on three secondary reports that all agreed with each other.

## Entities mentioned

- [Jetson Orin NX](../entities/jetson-orin-nx.md) — one of the Orin modules JetPack 7.2 extends support to.
- [JetPack](../entities/jetpack.md) — **the page this most directly updates**; its "JetPack 6 and 7 are parallel, not sequential" framing ended here.
- [Jetson Linux](../entities/jetson-linux.md) — r39.2 is the BSP under this release.
- [Jetson Orin Nano](../entities/jetson-orin-nano.md) · [Jetson Thor](../entities/jetson-thor.md) — the two ends of the now-unified line.
- [Isaac ROS](../entities/isaac-ros.md) — listed "coming soon"; the gating item for robotics adoption.
- [NemoClaw](../entities/nemoclaw.md) — single-command install is a named 7.2 feature, which is a notable placement for it.
- Without pages: DeepStream 9.1, Holoscan 3.9.0, Triton (container), OE4T, SIPL.

## Concepts touched

- The Jetson compute ladder — [module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) (the **AGX Orin 32 GB 200 → 241 TOPS** Super Mode bump lands there) and [XLeRobot onboard compute](../syntheses/platforms/jetson-onboard-compute-xlerobot.md).
- [Flashing an Orin Nano](../syntheses/projects/jetson-orin-nano-flash-howto.md) — now a JetPack-6-only procedure.

## Open questions

- **When does Isaac ROS ship for JetPack 7?** This is the single fact that decides whether a ROS robot can move to 7.x at all, and the page says only "coming soon."
- **Which Orin SKUs exactly?** "Jetson Orin Family" is the whole statement; the Yocto image list covers AGX Orin and Orin Nano but **not Orin NX**, while the PCIe overlay names Orin Nano *and* Orin NX. Orin Nano 4 GB and the AGX Orin 32/64 GB split are unaddressed here — the [Jetson Linux 39.2 release notes](https://docs.nvidia.com/jetson/) would settle it and are not ingested.
- **Does JetPack 6 remain a supported production branch, and for how long?** Not stated on this page. Relevant because Isaac ROS currently pins users there.
- **What is the real-world upgrade cost** for a working Orin robot: full reflash, no apt path, changed camera device trees on third-party carriers ([Seeed shipped R39.2.0 for J401/J501 on 2026-06-30](https://forum.seeedstudio.com/t/nvidia-has-officially-announced-jetpack-7-2-june-1-2026-any-plans-for-j401-agx-orin-32gb-support/295471), with a 22-pin CSI spec replacing 24-pin), and Isaac ROS absent. Nobody has written that migration guide.
