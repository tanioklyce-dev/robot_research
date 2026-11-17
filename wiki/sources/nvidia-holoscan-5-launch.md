---
title: "Introducing Holoscan 5: The Transparent Runtime for Physical AI"
type: source
url: https://nvidia-holoscan.github.io/blog/2026-10-20-holoscan-5-launch/
author: "Jay Carlson (NVIDIA)"
published: 2026-10-20
ingested: 2026-11-16
local_path: raw/2026-10-20-nvidia-holoscan-5-launch-blog.md
sha256: c622c2fc390c86bd6ce32914ce4d0f9d14d134b5e637abc0d5892ddaf7da8adb
format: vendor launch blog post
tags: [nvidia, holoscan, holoscan-5, hsdk-5, holoscan-sensor-bridge, daqiri, holomq, iceoryx2, gxf, cuda-graphs, green-contexts, partitions, temporal-contracts, real-time-control, sensor-processing, agents, medical-devices, ultrasound, endoscopy, vendor-source]
---

# Introducing Holoscan 5: The Transparent Runtime for Physical AI

> [!note] Read with the release notes
> This is the announcement. The **compatibility and platform facts** (CUDA 13 only, JetPack 7.2.1, no JetPack 6, API-stability tiers) are in the primary, [Holoscan SDK 5.0 release notes and platform requirements](holoscan-sdk-5-0-release-notes.md). Cite that page for any install or flashing decision.

## Summary

[NVIDIA](../entities/nvidia.md) relaunches [Holoscan](../entities/nvidia-holoscan.md) as a platform for **real-time sensor processing *and control***, built around one pattern (*"sense, think, act"*) shared by robots, satellites, MRI scanners, ultrasound and endoscopes. It has five parts: **HSDK** (the runtime and APIs), **Holoscan Sensor Bridge** (an FPGA IP that brings sensors over Ethernet with direct GPU delivery), **DAQIRI** (network data acquisition into CPU or GPU memory for scientific instruments), **Holoscan Modules** (5 installable packages, 16 operators), and **Reference Designs** (ultrasound, endoscopy).

The core of the release is **HSDK 5.0, a ground-up runtime rewrite.** **GXF is replaced by HoloMQ** (iceoryx2 shared-memory pub/sub plus CUDA VMM IPC). The user-chosen scheduler is replaced by **compiler-planned partitions**. Ports and parameters become **typed and compile-checked**. Build, plan and run become separate steps, and the plan can be inspected before any device starts. The post pitches HSDK 5.0 as *"the most agent-friendly release of HSDK yet"*: strict types and structured diagnostics are meant to let coding agents wire pipelines correctly *"on the first attempt"*, without hardware.

## Key claims

**One API for control and perception.** Some frameworks *"expose perception through message-driven callbacks and control through a separate controller API with its own update-loop semantics."* This reads as a description of ROS 2 topics plus ros2_control, though the post names neither. HSDK 5.0 uses the same operator lifecycle, typed ports and graph APIs for both. Control and perception can run at different cadences in one graph, using temporal contracts.

**Partitions** (§"Partitions make parallel pipelines natural")
- The unit of concurrency is a **processing chain**, not an operator. *"There is no scheduler to choose."* The compiler groups linear chains, splits at branches and joins, and records the result in the plan (`plan.partitions()`). Partitions can also be named explicitly.
- Each partition gets **one stable CPU thread**, with CPU affinity and scheduling policy available on request, and **one runtime-owned CUDA stream per active GPU**. Handoffs between threads happen only between partitions. Linear GPU chains on one stream skip redundant readiness events and fences.
- **CUDA Graph fusion**: eligible fixed-shape linear GPU regions are captured once and replayed.

**What changes from HSDK 4.x** (table in the post):

| Area | 4.x | 5.0 |
|---|---|---|
| Structure | Application + Fragment | Plain graphs, embeddable in existing code |
| Execution | Pick and configure a scheduler | Compiler-planned partitions |
| Timing | Conditions + queue/scheduler config | Timing declared beside operator logic |
| Connections | String-named ports | Typed ports, rejected at code compile |
| Config | `Parameter<T>` via YAML | Typed, versioned parameter schemas |
| Memory | Operator-configured allocators | Preallocated Tensor pools and bounded queues, visible in the plan |
| CUDA | Operator-facing stream APIs | Partition-owned streams, automatic Tensor ordering |
| Components | Built-in operators | Install only the modules you need |

**Transparency**: compose → `compile(graph)` (graph planning, an immutable plan with structured diagnostics) → `run(plan)` / `run_async(plan)`. NVTX shows compute ranges and message activity in Nsight Systems.

**Hot-path discipline**: C++ errors are values (`holoscan::expected<T, Error>`), not exceptions. `allocate_tensor()` borrows from a pool sized before execution, and **when the pool is exhausted it returns `kResourceExhausted` instead of growing**. `kDropOldest` with depth 1 is the freshest-sample mailbox.

**Modules**: Camera (V4L2, SIPL and Argus capture), Vision (9 operators: demosaic, resize, crop, remap, normalize, NMS, …), Inference (TensorRT, multi-model), Visualization (Holoviz), Multimedia (NVDEC H.264/HEVC).

**Reference designs**: **Ultrasound** (TI acquisition electronics + HSB + GPU beamforming, closed-loop transmit settings; *"an evaluation reference, not a clinically validated device"*), and **Endoscopy** (MIPI → FPGA capture → GPU imaging/AI → camera-clocked display, with an FPGA live-image fallback; **NDA early access**).

**Agent loop**: compose → build → compile the graph → inspect diagnostics (which have stable identifiers) → revise, all off-hardware. Agents can also generate operator tests that run against the real runtime. *"Hardware testing still establishes device integration, application behavior, latency, and jitter."*

## Analysis

### NVIDIA is leaving GXF on both of its robotics stacks at once

GXF (the Graph Execution Framework) was the common substrate under HSDK 4.x and under [Isaac ROS](../entities/isaac-ros.md)'s NITROS. Within one quarter, NVIDIA removed it from both:

- **Isaac ROS 4.5.0 (2026-07-06)** *"sun-set GXF in NITROS"*. **Isaac ROS 5.0 (2026-09-21)** removed NITROS and moved accelerated memory to ROS 2's upstream `rosidl::Buffer` ([release notes](isaac-ros-release-notes-and-platforms.md), [5.0 blog](nvidia-isaac-ros-5-0-blog.md)).
- **HSDK 5.0 (2026-10-20)** replaces GXF with **HoloMQ** (this post).

So the two stacks now use **different zero-copy GPU transports**: ROS-native `rosidl::Buffer` on one side, iceoryx2/CUDA-VMM HoloMQ on the other. That is the concrete version of the open question on the [Isaac ROS page](../entities/isaac-ros.md) about how Isaac OS relates to Isaac ROS. Bridging a Holoscan graph to a ROS 2 graph now means crossing transports, and neither source documents that bridge. The [gravity-comp tutorial](nvidia-holoscan-5-rebot-gravity-compensation.md) says Isaac ROS *"provides reusable Holoscan operators"*. **Which HSDK major those operators target is unstated**, and 5.0 is not source- or binary-compatible with 4.x.

### The headline features are not all stable

The launch post sells the inspectable plan and green-context placement. The [release notes](holoscan-sdk-5-0-release-notes.md) tier them: **plan inspection is Prototype, Tensor APIs are Beta, CUDA Green Context placement is a developer preview.** Only basic in-process graph and operator authoring, scalar ports and error handling are Stable across 5.x. Anyone adopting it should expect churn in exactly the features the post leads with.

### "Deterministic" means bounded start, not hard real-time

The real-time primitive the release notes describe is `Contract::max_start_delay(...)`, which bounds how late `compute()` may *start*. It *"does not bound compute completion or preempt a callback."* Together with core pinning and preallocated pools, this lowers jitter and makes deadline violations visible, but it gives no completion guarantee. The [reBot tutorial](nvidia-holoscan-5-rebot-gravity-compensation.md) measured p99.999 tails, and those numbers, not a guarantee, are what to rely on.

### Agents as a named audience

This is the first runtime launch in the wiki that names **coding agents as a primary user** and shapes the API around them (typed ports, versioned schemas, stable diagnostic identifiers, installation skills). The same pattern appears in Isaac ROS 5.0 shipping [Agent Skills](../concepts/agents/agent-skills.md). It is a design bet that rigid, compiler-checked interfaces suit agent-written systems code better than flexible ones.

## Entities mentioned

- [NVIDIA Holoscan](../entities/nvidia-holoscan.md), [NVIDIA](../entities/nvidia.md)
- [Isaac ROS](../entities/isaac-ros.md) — the parallel GXF exit
- [Jetson Thor](../entities/jetson-thor.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md), [DGX Spark](../entities/dgx-spark.md) — tested platforms (per the release notes)

## Concepts touched

- [Heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md) — partitions on CPU cores, green contexts on SM slices, one memory
- [Agent skills](../concepts/agents/agent-skills.md) — agent-oriented API design
- [Gravity compensation](../concepts/robotics/gravity-compensation.md) — the first published control demo on this runtime

## Open questions

- **Which HSDK major do Isaac ROS's Holoscan operators target**, and is there a supported HoloMQ ↔ `rosidl::Buffer` bridge?
- **Is Isaac OS HSDK 5 plus Isaac operators**, or something more? This post does not mention Isaac OS, although it shipped one day before GTC Berlin announced it.
- **Will plan inspection reach Stable within 5.x?** It is the feature the "transparent runtime" claim depends on.
- **Benchmarks**: the release notes point to dated runtime and channel benchmark pages, which have not been ingested.
