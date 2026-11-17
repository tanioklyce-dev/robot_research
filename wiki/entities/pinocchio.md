---
title: Pinocchio
type: entity
subtype: software-library
created: 2026-11-16
updated: 2026-11-16
sources: 3
tags: [pinocchio, rigid-body-dynamics, rnea, inverse-dynamics, kinematics, urdf, stack-of-tasks, laas-cnrs, inria, model-based-control, pink, c++, python]
---

**Pinocchio** — an open-source C++ library (with Python bindings) for **rigid-body kinematics and dynamics**, from the Stack-of-Tasks community (LAAS-CNRS / INRIA). It loads a robot from **URDF** and provides fast implementations of the standard algorithms: forward kinematics, Jacobians, the **Recursive Newton–Euler Algorithm (RNEA)** for inverse dynamics, and generalized gravity. Docs: [stack-of-tasks.github.io/pinocchio](https://stack-of-tasks.github.io/pinocchio/).

## Role in this wiki

Pinocchio is the **model-based-control backbone** under several affordable-arm stacks. Policy-learning sources rarely mention it, but it is what computes torques when an arm runs in torque mode instead of position mode.

- **Gravity compensation on the reBot B601-DM**: `pin.computeGeneralizedGravity(model, data, q)` runs inside a [Holoscan](nvidia-holoscan.md) operator at 400 Hz, from both Python and C++. Both languages call the same C++ solver ([Holoscan 5 tutorial](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)). See [gravity compensation](../concepts/robotics/gravity-compensation.md).
- **Listed as supported** by Seeed for the [reBot Arm B601](rebot-arm-b601.md) ([product page](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md)).
- **Task-space IK** through **Pink** (a Pinocchio-based QP IK solver) at 100 Hz on the untethered [XLeRobot](xlerobot.md) build ([Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md)).
- Commonly modelled robots include the [Franka Panda](franka-panda.md).

> [!note] Not ingested from a primary
> The library's own docs and papers (Carpentier et al.) have not been ingested. The algorithm list above is general background, and this page's claims about Pinocchio's *use* come from the sources cited.

## Related

- [Gravity compensation](../concepts/robotics/gravity-compensation.md), [Operational space control](../concepts/robotics/operational-space-control.md), [Impedance control](../concepts/robotics/impedance-control.md)
- [NVIDIA Holoscan](nvidia-holoscan.md) — the runtime it was hosted in for the reBot tutorial
- Drake (TRI) — the other model-based-control toolbox in the same niche (no page)

## Mentioned in

- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) — RNEA gravity torques in a 400 Hz loop
- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — listed in the supported software
- [Cutting the Cord: untethered XLeRobot](../sources/cutting-the-cord-untethered-xlerobot.md) — Pinocchio/Pink task-IK
