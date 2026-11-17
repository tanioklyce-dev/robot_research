---
title: NVIDIA Holoscan
type: entity
subtype: software-framework
created: 2026-11-16
updated: 2026-11-16
sources: 8
tags: [holoscan, gxf, holomq, iceoryx2, cuda-13, jetpack-7, hsdk, holoscan-5, holoscan-sensor-bridge, nvidia, real-time, sensor-processing, robot-control, edge-ai, isaac-os, jetson, igx, medical-devices]
---

**NVIDIA Holoscan** — NVIDIA's real-time sensor-processing and edge-AI runtime. It is a graph of **operators** connected by ports, compiled and executed with explicit threading. It began in medical devices (endoscopy and ultrasound reference designs, under Clara) and was extended with **robot control in Holoscan 5** (2026-10-20, [launch blog](../sources/nvidia-holoscan-5-launch.md)). The platform has five parts: the **Holoscan SDK (HSDK)**; the **Holoscan Sensor Bridge (HSB)**, an NVIDIA FPGA IP that brings sensors over Ethernet with direct GPU delivery; **DAQIRI**, network data acquisition for scientific instruments; **Holoscan Modules** (5 packages, 16 operators: Camera, Vision, Inference, Visualization, Multimedia); and **Reference Designs** (ultrasound, and endoscopy under NDA early access). Docs: [nvidia-holoscan.github.io](https://nvidia-holoscan.github.io/); code: [github.com/nvidia-holoscan](https://github.com/nvidia-holoscan).

## HSDK 5.0: a rewrite, not an upgrade

HSDK 5.0 is *"a ground-up rewrite of the Holoscan SDK runtime and API"*. It is **not source- or binary-compatible with 4.x** ([release notes](../sources/holoscan-sdk-5-0-release-notes.md)). **GXF is gone**, replaced by **HoloMQ** (iceoryx2 v0.9.3 shared-memory pub/sub with CUDA VMM IPC for zero-copy GPU buffers across processes). The user-selected scheduler is gone too, replaced by compiler-planned partitions ([launch blog](../sources/nvidia-holoscan-5-launch.md)). Isaac ROS dropped GXF in the same quarter (NITROS sun-set in 4.5.0, then removed in 5.0 in favour of `rosidl::Buffer`). **NVIDIA's two robotics runtimes now use different zero-copy transports**, and no source documents a bridge between them.

**Requirements** ([release notes](../sources/holoscan-sdk-5-0-release-notes.md)): **CUDA 13 only**, Ubuntu 24.04, Ampere or newer, Python ≥ 3.12, CMake ≥ 4.0 for C++. On Jetson it needs **JetPack 7**, tested on **JetPack 7.2.1** for AGX Thor, AGX Orin and Orin Nano. **JetPack 6 is not supported**, and **Orin NX is not on the tested list**. DGX Spark, IGX Thor, GH200 and GB200 are tested too.

**Stability tiers**: only basic graph and operator authoring, scalar ports and error handling are **Stable**. Tensor APIs are **Beta**, **plan inspection is Prototype**, and Green Context placement is a developer preview. In other words, the "transparent runtime" headline rests on a Prototype feature.

**Timing semantics**: `max_start_delay` bounds how late `compute()` *starts*. It *"does not bound compute completion or preempt a callback."* This is soft real-time with visible violations, not a hard guarantee.

## Programming model (HSDK 5)

From the [reBot gravity-compensation tutorial](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) and the [launch blog](../sources/nvidia-holoscan-5-launch.md):

- **Operators** implement `setup()` (declare ports), `contract()` (declare when to run: `OnClock(period)` or `OnEach(input)`) and `compute()`. `start()` and `stop()` are lifecycle hooks, and `hsdk.Param` declares tunable parameters with ranges.
- **Graphs** wire operator ports with `add_flow`. Each flow has a queue depth and a policy (`DROP_OLDEST` for control).
- **Partitions** pin a chain of operators onto **one runtime-owned thread**. A partition can be bound to a CPU core, a **CUDA green context**, or a **CUDA graph**. Control and perception are meant to be separate partitions or graphs in one process.
- **Compile before run**: `hsdk.compile(graph)` returns an inspectable plan, so misconfiguration fails before actuators are enabled.
- **Built-in NVTX** instrumentation, so Nsight Systems sees operator execution and message transfer without added code.
- Python and C++ APIs are equivalent. The heavy kernels (Pinocchio, CUDA) run natively from either.

Measured on a 400 Hz three-operator loop: **7.1 µs p50 / 17.2 µs p99.99** (C++, pinned core) and **93 / 143 µs** (Python, pinned). The measurement excludes motor I/O ([source](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)).

## Where it appears in NVIDIA's robotics stack

- **Holoscan Sensor Bridge** is the camera path on [Jetson Thor](jetson-thor.md), which has no onboard CSI connectors. It provides CSI-over-Ethernet in [JetPack 7.0](../sources/nvidia-jetpack-7-thor-whitepaper.md).
- [JetPack 7.2](../sources/nvidia-jetpack-7-2-release.md) bundles **Holoscan 3.9.0**, two majors behind. HSDK 5.0 installs separately (pip wheels, Debian `sbsa` packages, or the NGC container `holoscan:v5.0.0-cuda13`) and is tested on **JetPack 7.2.1** ([release notes](../sources/holoscan-sdk-5-0-release-notes.md)).
- **[NVIDIA Halos](nvidia-halos.md)** OS includes Holoscan SensorBridge in its safety stack ([Halos for Robotics](../sources/nvidia-halos-robotics.md)).
- **Isaac OS**, announced at GTC Berlin (2026-10-21), is *"an open source runtime framework built on NVIDIA Holoscan"* for *"deterministic, real-time performance"* ([release](../sources/nvidia-isaac-platform-gtc-berlin-2026.md)). Holoscan 5's control path (partitions, clocked contracts, core pinning) is presumably the "deterministic, real-time" substrate meant. No source yet confirms the layering.
- [Isaac ROS](isaac-ros.md) *"provides reusable Holoscan operators and reference applications such as GR00T inference"* ([tutorial](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)). This is the first wiki source to state that Isaac ROS ships Holoscan operators.

## Assessment

> [!note] What is and isn't shown
> The control-runtime claims are concrete and backed by measurement, but only for a **400 Hz loop on a 7-motor CAN arm**, where the bus (not the runtime) probably sets the ceiling. The "10 kHz motor control" framing is untested here. The obvious comparison is **ros2_control**, the incumbent real-time loop in the ROS world, and no source in the wiki makes it.

## Related

- [Isaac ROS](isaac-ros.md) — ROS 2 perception packages; ships Holoscan operators
- [Jetson Thor](jetson-thor.md), [Jetson Orin Nano](jetson-orin-nano.md) — tested targets
- [NVIDIA Halos](nvidia-halos.md) — safety stack that includes HSB
- [Pinocchio](pinocchio.md) — the dynamics library in the reference control loop
- [Gravity compensation](../concepts/robotics/gravity-compensation.md), [Impedance control](../concepts/robotics/impedance-control.md)
- [Heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md) — CPU-pinned control next to GPU work on one die
- [NVIDIA robot AI stack](../syntheses/platforms/nvidia-robot-ai-stack.md)

## Mentioned in

- [Introducing Holoscan 5](../sources/nvidia-holoscan-5-launch.md) — the launch: platform components, the 4.x → 5.0 change table, partitions, GXF → HoloMQ, the agent-oriented design
- [Holoscan SDK 5.0 release notes and platform requirements](../sources/holoscan-sdk-5-0-release-notes.md) — **compatibility primary**: CUDA 13, JetPack 7.2.1, no JetPack 6, stability tiers, breaking changes
- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) — the HSDK 5 control model, end to end, with latency numbers
- [NVIDIA Advances Isaac Platform (GTC Berlin)](../sources/nvidia-isaac-platform-gtc-berlin-2026.md) — Isaac OS "built on Holoscan"
- [JetPack 7.0 for Jetson Thor](../sources/nvidia-jetpack-7-thor-whitepaper.md) — Holoscan Sensor Bridge / CSI-over-Ethernet
- [JetPack 7.2 release](../sources/nvidia-jetpack-7-2-release.md) — bundles Holoscan 3.9.0
- [NVIDIA Halos for Robotics](../sources/nvidia-halos-robotics.md) — Holoscan SensorBridge in Halos OS
- [NVIDIA Jetson Thor carrier board spec](../sources/nvidia-jetson-thor-carrier-board-spec.md) — sensor I/O over Ethernet
