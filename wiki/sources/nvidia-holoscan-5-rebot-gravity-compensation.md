---
title: "Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5"
type: source
url: https://developer.nvidia.com/blog/make-a-robot-arm-feel-weightless-with-nvidia-holoscan-5/
author: "Jay Carlson and Ansley Dunn (NVIDIA)"
published: 2026-11-09
ingested: 2026-11-16
local_path: raw/2026-11-09-nvidia-holoscan-5-rebot-gravity-compensation.md
sha256: 6cb4e198257215f95bf9f42e8554a1a2d04c656be52861591f8941a6cc438f32
format: vendor technical blog post (tutorial)
tags: [nvidia, holoscan, holoscan-5, hsdk-5, real-time-control, gravity-compensation, impedance-control, torque-control, pinocchio, rnea, inverse-dynamics, rebot-arm, b601-dm, seeed-studio, damiao, motorbridge, nsight-systems, nvtx, latency, jitter, cpu-pinning, jetson-thor, jetson-orin-nano, isaac-ros, vendor-source]
---

# Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5

## Summary

A [NVIDIA](../entities/nvidia.md) tutorial that uses the robot-control path added in **[Holoscan](../entities/nvidia-holoscan.md) 5** to run a [gravity-compensation](../concepts/robotics/gravity-compensation.md) loop on a [Seeed reBot Arm B601-DM](../entities/rebot-arm-b601.md). The loop has three operators. One reads joint state on a 400 Hz clock. One computes gravity torque with [Pinocchio](../entities/pinocchio.md). One sends commands to the motors through Seeed's `motorbridge` library. All three share one Holoscan **partition** (one thread), with depth-1 drop-oldest queues. Profiling with Nsight Systems over more than a million cycles per run shows host-side latency of **7.1 µs p50 / 17.2 µs p99.99 for C++ pinned**, against **93 µs / 143 µs for Python pinned**. Pinning the partition to an isolated core cuts p99.99 by about 5× (C++) and 9.6× (Python).

The post has two purposes. It is the first wiki source that shows what Holoscan's *control* side looks like in code: this was the runtime NVIDIA said Isaac OS ([Isaac ROS § Isaac OS](../entities/isaac-ros.md)) is built on, without showing it. It is also the first source to run the reBot arm in **torque mode** rather than position mode.

## Key claims

**Holoscan 5 as a control runtime** (§"Why Holoscan?")
- Holoscan 5 *"introduced robotic control alongside streamlined sensor processing"* (launched 2026-10-20 per the linked Holoscan blog). The pitch is one programming model for CPU control loops ("10 kHz CPU-centric motor control loops"), GPU throughput and AI inference.
- **Partitions** group chains of operators onto one runtime-owned thread, which avoids cross-thread handoffs and syscalls. A partition can be pinned to a CPU core, a **CUDA green context**, or run as a **CUDA graph**.
- **Contracts** declare when an operator runs: `OnClock(period)` or `OnEach(input)`. Queues are bounded, and `DROP_OLDEST` means stale samples are discarded rather than queued.
- The graph is **compiled to an inspectable plan before it runs**. Configuration errors are caught before the motors are enabled. The post adds that *"agents and developers can quickly iterate on a design without ever deploying to real hardware."*
- **NVTX annotations are built in**, so Nsight Systems shows operator execution and message transfers with no instrumentation code.
- Operators implement `setup()` (ports), `contract()` (trigger) and `compute()` (work), plus optional `start()` and `stop()`. Parameters (`hsdk.Param`) carry ranges.

**The gravity-compensation loop** (§"Express the control loop as three operators")
- `JointStateSourceOp`: `OnClock` every **2.5 ms (400 Hz)**. It reads all seven motors (6 joints + gripper).
- `PinocchioGravityOp`: runs `OnEach` state. It maps the six arm angles into the URDF model, checks limits, and calls `pin.computeGeneralizedGravity`. Default gains are **kp = 1.5, kd = 1.0**, with per-joint `tau_scale` and `joint_direction`.
- `MotorCommandSinkOp`: rejects expired, out-of-order or out-of-range commands, then sends the batch.
- Gravity torque goes into the motor command **as feedforward, alongside position, velocity, stiffness and damping**. That is the motor's MIT-style impedance command (see the [mentor note](#what-the-host-loop-is-and-isnt-doing) below).
- Safety: a **100 ms watchdog** disables the motors and stops the graph if no command batch completes. `stop()` also disables them. Start and finish in the arm's power-off-safe home position, and return it by hand before Ctrl+C.
- Tested on **[Jetson Orin Nano](../entities/jetson-orin-nano.md), [Jetson Thor](../entities/jetson-thor.md), and x86 Ubuntu 24.04**. Python 3.12+. A C++ implementation of the same graph is in the tutorial repo.

**Why gravity-comp first** (§"Starting off with gravity-comp")
- Gravity comp is a **model sanity check**. *"Position-control examples can mask problems with joint axes, offsets, link placements, masses, and moments"*. Torque control exposes those errors at once, as an arm that sags or pushes upward as its pose changes.
- Most low-cost arms use *"highly-geared hobby servos, which are only suitable for positional control."* The reBot's **quasi-direct-drive** actuators give the torque bandwidth needed for haptic or co-bot work.
  - > [!warning] Only partly true (checked 2026-11-16)
    > Per Damiao's datasheets, the B601-DM's shoulder and elbow motors (DM-J4340P-2EC) are **40:1** ([datasheet](damiao-dm-j4340p-2ec-datasheet.md)). Only the wrist and gripper DM-J4310s (10:1) are QDD ([datasheet](damiao-dm-j4310-2ec-datasheet.md)). The demo shows that gravity comp and hand-guiding work anyway, but through 40:1 gearing at the joints carrying most of the load.

**Measured latency** (§"Pinning cores", Table 2). Latency is measured from entry into the first operator to entry into the last, so **motor-command transmission is excluded**. Each run kept more than a million cycles, the first 10 s were excluded, and outliers were retained:

| Implementation | p50 (µs) | p99.99 (µs) | p99.999 (µs) |
|---|---|---|---|
| C++ pinned | 7.1 | 17.2 | 20.7 |
| C++ unpinned | 15.3 | 86.6 | 133.4 |
| Python pinned | 93.0 | 142.6 | 1,014.0 |
| Python unpinned | 113.8 | 1,373.5 | 3,134.1 |

- Pinning used the deployment API plus a **temporary cgroup reserving two physical cores (with SMT siblings)**. No kernel rebuild, boot parameters (`isolcpus`) or reboot was needed, but interrupts, timers and some kernel threads still ran on those cores.
- Both versions call Pinocchio's C++ solver. Python's extra cost is interpreter execution, allocation and the GIL. The C++ path *"still allocates memory and is not a zero-syscall pipeline."*
- For GPU perception that takes milliseconds, CPU micro-overheads matter less, and Python remains practical *"provided that the pipeline elements are implemented in CUDA."*

**Beyond gravity comp** (§"From gravity compensation to a full control stack")
- A second example in the repo adds **kinematics and [impedance control](../concepts/robotics/impedance-control.md)** as reusable operators. A goal pose can be injected *"for example from a learned policy"* while the arm stays compliant (Video 3: Cartesian position hold).
- For perception, the post points to Holoscan's vision module and **[Isaac ROS](../entities/isaac-ros.md), which "provides reusable Holoscan operators and reference applications such as [GR00T](../entities/nvidia-groot.md) inference."**

## Analysis

### What the host loop is and isn't doing

> [!note] Mentor reading — not stated in the post
> The command carries **position, velocity, stiffness, damping and feedforward torque**. That is the [Damiao](../entities/damiao.md) **MIT mode** the [reBot page](../entities/rebot-arm-b601.md) already records. In MIT mode the **PD (impedance) loop closes inside each motor's driver**, at the driver's own rate. The 400 Hz host loop only refreshes the gravity feedforward and the setpoint. So the post's argument that *"thread handoffs can add phase lag and jitter that cause the robot to become unstable"* applies only weakly to this demo. A late host cycle gives a slightly stale gravity term, not a stale feedback loop. The argument holds in full for a host-side torque loop (raw current control, or the Cartesian impedance example if it closes the loop on the host). The post doesn't say which the second example does.

### Reading the latency table against the budget

- The cycle is **2,500 µs**. Every pinned row, and every p50, is under 6% of it. Framework overhead is **not the bottleneck** at 400 Hz in either language.
- The row that matters is **Python unpinned p99.999 = 3,134 µs**, which is longer than the period. At 400 Hz, a 10⁻⁵ event happens about every **4 minutes**: an occasional overrun on a default Linux setup with no isolation. Pinning brings Python's p99.999 to 1,014 µs (inside the budget, but at 40% of it). This is the practical case for pinning, more than the 5×/9.6× headline.
- **The excluded term is probably the largest.** The DM arm's bus is **CAN at 1 Mbit/s with seven nodes** ([Damiao](../entities/damiao.md)). A standard 8-byte CAN frame is roughly 110–130 bits on the wire. One cycle needs about 14 frames (seven commands and seven replies), which is **≈1.5–1.8 ms of pure bus time**, or 60–70% of the 2.5 ms period. Host compute is two orders of magnitude smaller. This is a back-of-envelope estimate, not a measurement: it ignores the USB-CAN adapter's serial hop and any frame batching. If it is right, **the bus sets the loop's rate ceiling, not the runtime**, and 400 Hz is close to the limit for seven motors on one 1 Mbit/s bus. The end-to-end sense-to-actuate latency is not reported.
- "10 kHz motor control loops" is a statement about the programming model, not something this post demonstrates. Its loop runs at 400 Hz.

### Gaps

- **Video 1** compares Holoscan with *"a custom script runtime"* that isn't described. There is no comparison with the incumbent, **ros2_control**, which is the obvious alternative for this job (see the [NVIDIA stack synthesis](../syntheses/platforms/nvidia-robot-ai-stack.md), "Edge OS / runtime" row).
- The tested platforms include Orin Nano and Thor, but **the table doesn't say which machine it was measured on**.
- Several in-body links in the blog are broken relative links (`http://apps/gravity_compensation.cpp`, `http://docs/cpp-version.md`, `http://python/rebot_gravity.py`, `http://docs/control-policies.md`). The canonical copy is the [Holoscan tutorial page](https://nvidia-holoscan.github.io/tutorials/rebot-gravity-compensation/), which links the real files under [nvidia-holoscan/holoscan-tutorials](https://github.com/nvidia-holoscan/holoscan-tutorials/tree/main/tutorials/rebot-gravity-compensation) (config `rebotarm_dm.yaml`, `technical-guide.md`, a `fetch-urdf.py` script). The tutorial page credits Jay Carlson alone. It labels the release **"HSDK 5.0, part of the Holoscan 5 platform release"**, tutorial version 1.0.0, x86_64 and aarch64.

> [!note] Version numbering
> [JetPack 7.2](nvidia-jetpack-7-2-release.md) bundles **Holoscan 3.9.0**. Holoscan 5 (HSDK 5.0, [launch](nvidia-holoscan-5-launch.md); [requirements](holoscan-sdk-5-0-release-notes.md): CUDA 13, tested on JetPack 7.2.1, no JetPack 6) launched 2026-10-20, so the version on a JetPack 7.2 image is two majors behind this tutorial. That is not a contradiction, but **don't assume the JetPack-bundled Holoscan can run this code**. The tutorial installs from pip wheels (`--only-binary=:all:`) into a venv.

## Entities mentioned

- [NVIDIA Holoscan](../entities/nvidia-holoscan.md) — the runtime
- [NVIDIA](../entities/nvidia.md)
- [reBot Arm B601](../entities/rebot-arm-b601.md) (DM variant) and [Seeed Studio](../entities/seeed-studio.md), which makes the arm and the `motorbridge` library
- [Damiao](../entities/damiao.md) — the arm's actuators (MIT-mode commands)
- [Pinocchio](../entities/pinocchio.md) — the rigid-body dynamics library
- [Jetson Orin Nano](../entities/jetson-orin-nano.md), [Jetson Thor](../entities/jetson-thor.md) — the tested targets
- [Isaac ROS](../entities/isaac-ros.md), [NVIDIA GR00T](../entities/nvidia-groot.md) — the perception and policy layer on top

## Concepts touched

- [Gravity compensation](../concepts/robotics/gravity-compensation.md)
- [Impedance and admittance control](../concepts/robotics/impedance-control.md)
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — a learned policy that injects goal poses into an impedance operator is the "reference interface" pattern
- [Heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md) — CPU-core pinning next to GPU green contexts on one device

## Open questions

- **End-to-end latency including CAN I/O.** This is the number that decides the achievable loop rate, and it is excluded.
- **Which machine produced Table 2?** Orin Nano, Thor or x86 latency would differ substantially.
- **Does the Cartesian impedance example close its loop on the host or in the motors?** That decides whether host jitter matters for it.
- **How does Holoscan 5 relate to Isaac OS and to ros2_control?** The post says nothing about either. Is Isaac OS a distribution of HSDK 5 operators, or a separate layer?
- **reBot backdrivability** is now *demonstrated* qualitatively (hand-guiding under gravity comp) but still not *measured*. Friction and cogging torque per joint would tell us how much of the "weightless" feel is model, and how much is low gearing.
