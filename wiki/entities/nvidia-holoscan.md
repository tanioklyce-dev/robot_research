---
title: NVIDIA Holoscan
type: entity
subtype: software-framework
created: 2026-11-16
updated: 2026-11-16
sources: 6
tags: [holoscan, hsdk, holoscan-5, holoscan-sensor-bridge, nvidia, real-time, sensor-processing, robot-control, edge-ai, isaac-os, jetson, igx, medical-devices]
---

**NVIDIA Holoscan** — NVIDIA's real-time sensor-processing and edge-AI runtime. It is a graph of **operators** connected by ports, compiled and executed with explicit threading. It began in medical devices (endoscopy and ultrasound reference designs, under Clara) and was extended with **robot control in Holoscan 5** (2026-10-20). The platform has three parts: the **Holoscan SDK (HSDK)**, the **Holoscan Sensor Bridge (HSB)** for sensor-over-Ethernet I/O, and **DAQIRI**. Docs: [nvidia-holoscan.github.io](https://nvidia-holoscan.github.io/); code: [github.com/nvidia-holoscan](https://github.com/nvidia-holoscan).

## Programming model (HSDK 5)

From the [reBot gravity-compensation tutorial](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md):

- **Operators** implement `setup()` (declare ports), `contract()` (declare when to run: `OnClock(period)` or `OnEach(input)`) and `compute()`. `start()` and `stop()` are lifecycle hooks, and `hsdk.Param` declares tunable parameters with ranges.
- **Graphs** wire operator ports with `add_flow`. Each flow has a queue depth and a policy (`DROP_OLDEST` for control).
- **Partitions** pin a chain of operators onto **one runtime-owned thread**. A partition can be bound to a CPU core, a **CUDA green context**, or a **CUDA graph**. Control and perception are meant to be separate partitions or graphs in one process.
- **Compile before run**: `hsdk.compile(graph)` returns an inspectable plan, so misconfiguration fails before actuators are enabled.
- **Built-in NVTX** instrumentation, so Nsight Systems sees operator execution and message transfer without added code.
- Python and C++ APIs are equivalent. The heavy kernels (Pinocchio, CUDA) run natively from either.

Measured on a 400 Hz three-operator loop: **7.1 µs p50 / 17.2 µs p99.99** (C++, pinned core) and **93 / 143 µs** (Python, pinned). The measurement excludes motor I/O ([source](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)).

## Where it appears in NVIDIA's robotics stack

- **Holoscan Sensor Bridge** is the camera path on [Jetson Thor](jetson-thor.md), which has no onboard CSI connectors. It provides CSI-over-Ethernet in [JetPack 7.0](../sources/nvidia-jetpack-7-thor-whitepaper.md).
- [JetPack 7.2](../sources/nvidia-jetpack-7-2-release.md) bundles **Holoscan 3.9.0**. The HSDK 5.0 tutorial installs from pip wheels instead, so a stock JetPack 7.2 image is two majors behind.
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

- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) — the HSDK 5 control model, end to end, with latency numbers
- [NVIDIA Advances Isaac Platform (GTC Berlin)](../sources/nvidia-isaac-platform-gtc-berlin-2026.md) — Isaac OS "built on Holoscan"
- [JetPack 7.0 for Jetson Thor](../sources/nvidia-jetpack-7-thor-whitepaper.md) — Holoscan Sensor Bridge / CSI-over-Ethernet
- [JetPack 7.2 release](../sources/nvidia-jetpack-7-2-release.md) — bundles Holoscan 3.9.0
- [NVIDIA Halos for Robotics](../sources/nvidia-halos-robotics.md) — Holoscan SensorBridge in Halos OS
- [NVIDIA Jetson Thor carrier board spec](../sources/nvidia-jetson-thor-carrier-board-spec.md) — sensor I/O over Ethernet
