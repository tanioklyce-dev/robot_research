---
title: Isaac ROS — Release Notes and Supported Platforms (docs)
type: source
url: https://nvidia-isaac-ros.github.io/releases/index.html
fetch_url: https://nvidia-isaac-ros.github.io/releases/index.html
local_path: raw/2026-09-27-isaac-ros-release-notes-and-platforms.txt
sha256: 3995d0333c559b36e36d25e4ab384da8d2c69dd7c4070e042509ef432f755f0d
author: NVIDIA Corporation
published: 2026-09-21 (Isaac ROS 5.0.0, latest entry at re-capture; 4.5.0 / 2026-07-06 at first ingest)
ingested: 2026-08-17
recaptured: 2026-09-27
venue: NVIDIA Isaac ROS documentation
tags: [isaac-ros, nvidia, ros2, jetson, thor, orin, jetpack, dgx-spark, jazzy, lyrical, nitros, rosidl-buffer, compatibility]
---

> [!warning] Superseded headline — Orin is back (Isaac ROS 4.6.0, 2026-08-18)
> This page was first ingested **2026-08-17** from the 4.5.0 state and headlined *"Isaac ROS 4.x is not an Orin product."* That was accurate that day and **false the next**: **4.6.0 (2026-08-18) "Added support for Jetson Orin" and "Added support for JetPack 7.2"**, and the 5.0.0 supported-platform table lists **"Jetson Thor (T5000 and T4000) and Jetson Orin" on JetPack 7.2**. The original analysis is kept below, marked, because the reasoning error is instructive: "no 4.x release mentions Orin" was read as a *generational break*; it was a **gap between BSPs** — Orin simply had no JetPack 7 until 7.2 (2026-06-02), and Isaac ROS followed ten weeks later. See **[Edition history](#edition-history)**.

## Summary

The Isaac ROS documentation's **release-notes archive** plus the **Supported Platforms** table from its Getting Started page — together the primary for "what hardware and software does Isaac ROS actually run on." Ingested during the 2026-08-17 Jetson version sweep to settle a question the [JetPack 7.2 release page](nvidia-jetpack-7-2-release.md) could only half-answer.

The headline *at first ingest (2026-08-17; superseded next day — see callout above)*: **Isaac ROS 4.x is not an Orin product.** The supported-platform table lists Jetson Thor, x86_64, and DGX Spark — no Orin of any generation, on any JetPack. The last Orin-supporting line is **3.2 (December 2024, updated through Feb 2025)**. This is a considerably stronger statement than the "Isaac ROS: Coming soon" cell on the JetPack 7.2 release page, which reads as a scheduling note and is in fact a generational break.

## Key claims

### Supported Platforms table — current (5.0.0, captured 2026-09-27)

| Platform | Hardware | Software | Storage |
|---|---|---|---|
| **Jetson** | **Jetson Thor (T5000 and T4000) and Jetson Orin** | **JetPack 7.2** | 128+ GB NVMe SSD |
| **x86_64** | Ampere or higher, 8 GB+ | Ubuntu 24.04, **CUDA 13.2+, driver 595+** | 32+ GB |
| **DGX** | DGX Spark | DGX OS 7.2.3 | 32+ GB |

- **ROS support**: *"All Isaac ROS packages are designed and tested to be compatible with **ROS 2 Lyrical**."* Virtual-env / bare-metal installs get ROS 2 Lyrical from a new **Isaac ROS Buildfarm** apt repository.
- Jetson verification: `/etc/nv_tegra_release` should report **`R39 (release), REVISION: 2.0`** (JetPack 7.2 = Jetson Linux r39.2) — on both Thor and AGX Orin.
- The setup guide walks through **AGX Thor and AGX Orin**; the performance page benchmarks **AGX Orin and Orin Nano** among others. Orin NX is covered by "Jetson Orin" but not named.

### Supported Platforms table — as first ingested (4.5.0, 2026-08-17; superseded)

Prefaced with: "The platforms defined in this table are **the only hardware and software combinations that Isaac ROS tests and officially supports.** Users may be able to rely on backward and forward compatibility utilities like `cuda-compat` to use Isaac ROS on other platform versions."

| Platform | Hardware | Software | Storage |
|---|---|---|---|
| **Jetson** | **Jetson Thor (T5000 and T4000)** | **JetPack 7.1** | 128+ GB NVMe SSD |
| **x86_64** | Ampere or higher NVIDIA GPU, 8 GB+ RAM | Ubuntu 24.04, CUDA 13.0+, driver 580+ | 32+ GB |
| **DGX** | DGX Spark | DGX OS 7.2.3 | 32+ GB |

- **ROS support**: "All Isaac ROS packages are designed and tested to be compatible with **ROS 2 Jazzy**." (The 3.x line was Humble.)
- Install verification step: `cat /etc/nv_tegra_release` should report **`R38 (release), REVISION: 4.0`** — i.e. JetPack 7.1 = **Jetson Linux R38.4**, the Thor BSP line, not r39.2.

### Release timeline (release-notes archive)

| Release | Date | Platform-relevant contents |
|---|---|---|
| **5.0.0** | **2026-09-21** | **ROS 2 Lyrical Luth**; Isaac ROS Buildfarm apt repo; **NITROS rebuilt on `rosidl::Buffer` + CUDA buffer backend and the NITROS packages removed** (source-level migration); **Agent Skills** (`isaac-ros-activate`, early-access `migrate-node-to-rosidl-buffer`; more in `nvidia/skills`); `isaac_ros_gpu_partitioning` (CUDA MPS SM shares); `isaac_ros_visual_slam` → `isaac_ros_cuvslam`; teleop `PoseArray` → `NamedPoseArray` |
| **4.6.0** | **2026-08-18** | **"Added support for Jetson Orin"; "Added support for JetPack 7.2"**; Isaac Sim 6.0 recommended (5.0/5.1 legacy); SIPL Hawk GMSL2 stereo; cuVSLAM built from source; Unitree G1 cloud control; G1 AGILE locomotion deploy in Isaac Sim 6.0 |
| **4.5.0** | **2026-07-06** | Sun-setting GXF in NITROS; CUDA streaming for NITROS; cuMotion 1.1.0; **MCAP-to-LeRobot converter**; Unitree G1 recording + GR00T deploy workflows; Fast-FoundationStereo |
| 4.4.0 | 2026-04-30 | `isaac_manipulator` → `isaac_ros_manipulation`; new `isaac_ros_teleop` (XR headset); new `isaac_ros_physical_ai` and `isaac_ros_robots` repos |
| 4.3.0 | 2026-03-23 | `isaac_ros_sipl_camera` — SIPL integration for Camera-over-Ethernet |
| **4.2.0** | **2026-02-19** | **Support for DGX Spark; support for JetPack 7.1; support for Thor T4000 SKU** |
| 4.1.0 | 2026-02-02 | Docker-optional Virtual Environment and Bare Metal modes; nvblox Lidar dynamics |
| **4.0.0** | **2025-10-24** | **Support for Jetson AGX Thor; support for JetPack 7.0 / Ubuntu 24.04 on CUDA 13.0; tested with Isaac Sim 5.1** |
| 3.2 Update 1 | 2025-01-16 | **Support for JetPack 6.2 and Jetson Orin Nano Super** |
| 3.2 | 2024-12-10 | Support for JetPack 6.1 / Ubuntu 22.04 on CUDA 12.6 (only); Isaac Sim 4.2 |
| 3.1 | 2024-09-26 | — |
| 3.0.0 / 3.0.1 | 2024-05-30 / 2024-06-14 | JetPack 6.0 / Ubuntu 22.04 on CUDA 12.2 |

> [!warning] Superseded 2026-08-18 — kept for the record
> The callout below was true of 4.0–4.5 and is **not true of 4.6+**.
>
> **The Orin line ends at Isaac ROS 3.2** *(original text)*
> No 4.x release note mentions Orin, and Orin appears nowhere in the supported-platform table. **An Orin robot's terminal supported Isaac ROS configuration is 3.2 (Update 4) on JetPack 6.1/6.2, Ubuntu 22.04, CUDA 12.6, ROS 2 Humble** — a stack frozen since early 2025. Everything in 4.x (cuMotion 1.1, the manipulation refactor, XR teleop, `isaac_ros_physical_ai`, the MCAP→LeRobot converter, GR00T deploy workflows) is Thor / x86 / DGX Spark only.

### Selected 5.0.0 limitations worth knowing before committing

- **DNN image encoder regression**: *"lower throughput and higher latency than in Isaac ROS 4.6"* on Thor, AGX Orin, DGX Spark and RTX 5070 (nvbugs/6798546).
- **RealSense only in Docker mode** — Virtual Environment and Bare Metal unsupported (nvbugs/6635538).
- **nvblox + RealSense D455 → empty mesh and map** (nvbugs/6786950).
- AGX Orin: `stereo_image_proc` with `backend:=JETSON` and RGB8/BGR8 can terminate with `VPI_ERROR_INVALID_OPERATION` — use the default CUDA backend.
- Orin: Isaac ROS Teleop from the Debian package may fail (experimental CloudXR runtime missing) — set `ISAAC_TELEOP_CLOUDXR_EXP=0`.
- Thor: H.264 encoder may segfault at shutdown with VPI 4.1.4 — `LD_PRELOAD` workaround.
- cuMotion MoveIt examples may fail where upstream robot-vendor packages are not yet certified for Lyrical.
- 4.6.0 carried a manipulation cluster of issues (reach-policy checkpoint load error, stalled pick-and-place goals, UR10e trajectory failures) and **cuVSLAM unsupported on DGX Spark**.

### Selected 4.5.0 limitations (first ingest)

- DNN stereo depth (ESS, FoundationStereo, Fast-FoundationStereo) "may intermittently fail to produce disparity or point cloud output, drop frames, or show no RViz output" with RealSense, ZED, or Isaac Sim, due to a synchronization issue in the decoder node.
- **Fast-FoundationStereo is a research model, not for commercial use**; use FoundationStereo for commercial applications.
- On **DGX Spark**, the H.264 encoder may fail to open the V4L2 encoder device.
- Stale TensorRT engine-cache failures on Thor were *fixed* in 4.5.0 (nvbugs/6032663).
- RealSense SDK stability on JetPack 7 was a 4.x issue addressed by following the RealSense setup tutorial.

## Entities mentioned

- [Jetson AGX Orin](../entities/jetson-agx-orin.md) — absent from the 4.0–4.5 table; supported again from 4.6.0 on JetPack 7.2, and the Orin named in the 5.0 setup guide.
- [Jetson Orin NX](../entities/jetson-orin-nx.md) — absent from 4.0–4.5; covered by "Jetson Orin" from 4.6.0, though never named individually.
- [Isaac ROS](../entities/isaac-ros.md)
- [Isaac ROS NVBlox](../entities/nvblox.md)
- [Jetson Thor](../entities/jetson-thor.md)
- [JetPack](../entities/jetpack.md)
- [DGX Spark](../entities/dgx-spark.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [LeRobot](../entities/lerobot.md) — via the MCAP-to-LeRobot converter in 4.5.0
- [Isaac GR00T](../entities/nvidia-groot.md) — via the G1 deploy workflow
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)
- [ROS 2](../entities/ros2.md)

## Concepts touched

- Platform support matrices as a deployment constraint; the Humble → Jazzy distro break; GPU-accelerated ROS 2 perception.

## Edition history

This is a living docs page with no versioned snapshots; the first ingest kept no local copy, so there is no superseded file to retain — only the text of this page as written on 2026-08-17.

| Captured | Latest entry | Platform table (Jetson row) | ROS 2 |
|---|---|---|---|
| 2026-08-17 | 4.5.0 (2026-07-06) | Thor T5000/T4000 · JetPack 7.1 | Jazzy |
| **2026-09-27** | **5.0.0 (2026-09-21)** | **Thor T5000/T4000 and Jetson Orin · JetPack 7.2** | **Lyrical** |

**What changed and what it touched**: the Orin claim (propagated to [Isaac ROS](../entities/isaac-ros.md), [Jetson Orin NX](../entities/jetson-orin-nx.md), [Jetson AGX Orin](../entities/jetson-agx-orin.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md), [JetPack](../entities/jetpack.md), [Jetson Thor](../entities/jetson-thor.md), [nvblox](../entities/nvblox.md), [the NVIDIA robot-AI stack](../syntheses/platforms/nvidia-robot-ai-stack.md) and [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — all corrected 2026-09-27); the JetPack pin (7.1 → 7.2); the ROS 2 distro (Jazzy → Lyrical); the x86 CUDA floor (13.0 → 13.2); and NITROS (removed).

> [!note] Why this was missed, and what would have caught it
> The 2026-08-17 conclusion was drawn from a primary, correctly read. It went stale **one day later** because it was a claim about a *living* docs page's *future* ("whether NVIDIA re-adds Orin is a product decision with no public commitment"). The page had no `fetch_url`, so the [drift check](../../CLAUDE.md#drift-check) could not see it. It now has one. A negative claim about a vendor's support matrix should be treated as having a shelf life.

## Open questions

- ~~**Will Isaac ROS ever return to Orin under JetPack 7?**~~ — **Yes: 4.6.0, 2026-08-18.** The platform obstacle (no Orin BSP on JetPack 7) was the whole story.
- **Does Orin NX get equal treatment?** Named nowhere individually; covered by "Jetson Orin" on JetPack 7.2. Worth a real install before relying on it.
- **NITROS → `rosidl::Buffer` migration cost** for third-party NITROS consumers.
- **Isaac Perceptor / Nova on Thor** — reported as not yet optimized for AGX Thor in a developer-forum thread about 4.1.0; not stated in the primary, so left as a secondary-sourced rumor.
