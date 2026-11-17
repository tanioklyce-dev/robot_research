---
title: "Holoscan SDK 5.0 — release notes and platform requirements"
type: source
url: https://github.com/nvidia-holoscan/holoscan-sdk/releases/tag/v5.0.0
author: "NVIDIA Holoscan team"
published: 2026-10-21
ingested: 2026-11-16
local_path: raw/2026-10-21-holoscan-sdk-5-0-release-notes.md
sha256: 140b2f15bd6bbf30705fb4f8e7837595dd58e2a65db1d4a45f2b4bc099050857
format: GitHub release notes + docs installation page (combined capture)
tags: [nvidia, holoscan, hsdk-5, release-notes, compatibility, cuda-13, jetpack-7, jetpack-7-2-1, ubuntu-24-04, orin, thor, igx, dgx-spark, api-stability, holomq, iceoryx2, breaking-changes, primary]
---

# Holoscan SDK 5.0 — release notes and platform requirements

The **compatibility primary** for [Holoscan](../entities/nvidia-holoscan.md) 5. The raw file combines two NVIDIA documents: the **v5.0.0 GitHub release body** (published 2026-10-21 03:30 UTC) and the **SDK installation page's prerequisites and tested-platform sections**, captured 2026-11-16. The announcement is the [Holoscan 5 launch blog](nvidia-holoscan-5-launch.md).

> [!note] Fingerprint caveat
> The sealed hash covers the combined extracted text, not either upstream document. There is no `fetch_url`. The docs install page is the likelier of the two to be revised in place, so re-capture it before relying on the tested-platform table for a flashing decision.

## Summary

HSDK 5.0 is *"a ground-up rewrite of the Holoscan SDK runtime and API"*, and **neither source- nor binary-compatible with 4.x**. It needs **CUDA 13, Ubuntu 24.04, an Ampere-or-newer GPU and Python ≥ 3.12**. On Jetson it needs **JetPack 7**, and it is tested on **JetPack 7.2.1** for AGX Thor, AGX Orin and Orin Nano. **JetPack 6 and IGX OS 1.x are not supported.**

## Key claims

### Platform requirements (installation page)

| Requirement | Value |
|---|---|
| OS | Ubuntu 24.04 (bare-metal support limited to it) |
| CUDA | **13 only**; driver R580+. *"A single CUDA 13 software stack for discrete and integrated GPUs"*, with no separate iGPU package |
| GPU | Ampere or newer |
| Python | 3.12+ (abi3 wheels for 3.12–3.14, `manylinux_2_39`) |
| CMake (C++) | **4.0+**. Ubuntu 24.04 ships 3.28, so install via snap, pipx or Kitware |
| Jetson / IGX | **JetPack 7** or **IGX OS 2+**. *"JetPack 6 and earlier are not supported."* |

**Tested platforms:**

| Platform | OS |
|---|---|
| x86_64 (RTX 6000 Ada, RTX PRO 6000 Blackwell) | Ubuntu 24.04, R610 |
| [Jetson AGX Thor](../entities/jetson-thor.md) | **JetPack 7.2.1** |
| [Jetson AGX Orin](../entities/jetson-agx-orin.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md) | **JetPack 7.2.1** |
| IGX Thor 5000 / 7000 | IGX OS 2.0 |
| [DGX Spark](../entities/dgx-spark.md) | DGX OS 7.6.0 |
| GH200, GB200 | Ubuntu 24.04, R610 |

Install channels: NGC container `nvcr.io/nvidia/clara-holoscan/holoscan:v5.0.0-cuda13`, Debian packages (arm64 = `sbsa`, covering both servers and Jetson), `pip install holoscan==5.0.0` (CUDA 13 component wheels: core, vision, visualization, inference), or source.

### API stability tiers (release notes)

- **Stable across 5.x**: basic in-process graph and operator authoring, ordinary scalar ports, named Python port lookup, structured error handling.
- **Beta**: trigger resolution when a contract is omitted, clock selection, automatic queue and resource derivation, and **all Tensor declarations, ownership, output specs and pools**.
- **Prototype**: **plan inspection**, resolved-defaults reports, typed records and report formats.
- **Developer preview**: CUDA Green Context placement (manual, exact named partitions only, never automatic).
- Source stability does **not** promise binary compatibility between packages or interoperability of channels and schemas across versions.

### Features worth knowing

- `Contract::max_start_delay(...)` + `on_violation(...)` bounds how late `compute()` may *start*. It *"does not bound compute completion or preempt a callback."* (It was renamed from `deadline(...)`, with no alias.)
- Temporal combinators: `OnEach`, `LatestWithin`, `Skip`. Contracts are verified at compile time.
- **Runtime parameter generations**: parameters can change between activations with a consistent snapshot. There is an **experimental tuner** for iterative parameter search, which is relevant to the gain tuning in the [gravity-comp tutorial](nvidia-holoscan-5-rebot-gravity-compensation.md).
- **Interprocess channels**: HoloMQ is built on **iceoryx2 v0.9.3**, with zero-copy GPU memory across processes. **External channel clients** (plain processes, not operators) attach using only `endpoint-catalog.json`.
- **Cold artifact generation**: emit the deployment bundle (catalog, FlatBuffers schemas, compiled plan) without starting CUDA or transport (`--emit-artifacts`).
- Automatic partitioning by default (`holoscan.partition.source_chain/1`). **Partitions may run callbacks concurrently**, so ordering across partitions can change. `partition(name).include_all()` restores single-owner behaviour.
- SIGINT/SIGTERM handling is managed by default for blocking `run(plan)`. Child processes inherit the blocked signal mask, which is a gotcha for anything that `exec()`s.
- Examples: `slow_fast_fusion` (two-rate), `camera_imu_control`, `external_clients`.

### Breaking changes

Not source- or binary-compatible with 4.x; there are migration guides for C++ and Python. Within the 5.0 line, the notes also record early-access renames that break code (`deadline` → `max_start_delay`; `QueuePolicy::kLatest` removed in favour of `kDropOldest` depth 1; the Tensor port-spec revision; sensor schemas moved to `holoscan::sensor_io`). The private execution-plan schema is v9, with **no reader for older schemas**.

## Analysis

> [!note] JetPack 7.2.1 now has a primary
> The wiki's backlog item *"Verify JetPack 7.2.1 against a primary"* rested on secondary reporting. This NVIDIA docs page names **JetPack 7.2.1** as the tested Jetson release, which confirms the version exists and is the current Holoscan target. The **2026-08-12 release date is still secondary-only.**

> [!warning] Orin NX and the 8 GB question
> **Orin NX is not in the tested-platform list** (AGX Orin and Orin Nano are). It is probably covered in practice, because the JetPack 7 support statement is general. But it is untested, and that matters for the [XLeRobot](../entities/xlerobot.md) Orin NX path. The [JetPack 7.2 release](nvidia-jetpack-7-2-release.md) already leaves Orin NX out of its Yocto images, so this is the second NVIDIA document to skip it.

- **Practical consequence for any Jetson in this wiki:** HSDK 5 means JetPack 7.2.x. A board still on JetPack 6.x (CUDA 12.6, Ubuntu 22.04) cannot run it, either from wheels (glibc 2.39) or in the container. JetPack 7.2 itself bundles **Holoscan 3.9.0** ([release](nvidia-jetpack-7-2-release.md)), so install 5.0 separately and don't use the bundled version.
- Xavier-class boards (Volta) are excluded twice: by the Ampere floor and by the lack of JetPack 7.
- DGX Spark is a tested platform. That makes a Spark-to-Thor development path for Holoscan graphs plausible on one CUDA 13 stack, matching the [Thor vs Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) framing.

## Entities mentioned

- [NVIDIA Holoscan](../entities/nvidia-holoscan.md), [NVIDIA](../entities/nvidia.md)
- [Jetson Thor](../entities/jetson-thor.md), [Jetson AGX Orin](../entities/jetson-agx-orin.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md), [Jetson Orin NX](../entities/jetson-orin-nx.md) (by omission), [DGX Spark](../entities/dgx-spark.md)
- [JetPack](../entities/jetpack.md)

## Concepts touched

- [Heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md) — Green Context SM partitioning on iGPUs

## Open questions

- **Which HSDK major do [Isaac ROS](../entities/isaac-ros.md)'s Holoscan operators target?** The [gravity-comp tutorial](nvidia-holoscan-5-rebot-gravity-compensation.md) says Isaac ROS *"provides reusable Holoscan operators"*. 5.0 is neither source- nor binary-compatible with 4.x, and JetPack 7.2 bundles 3.9.0.

- Is **Orin NX** supported on HSDK 5.0, or only untested?
- Does the **JetPack 7.2.1** release-notes primary exist anywhere NVIDIA links publicly?
- When do the Tensor and plan-inspection APIs leave Beta and Prototype?
