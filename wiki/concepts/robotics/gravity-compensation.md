---
title: Gravity compensation
type: concept
created: 2026-11-16
updated: 2026-11-16
sources: 1
tags: [gravity-compensation, inverse-dynamics, rnea, torque-control, feedforward, quasi-direct-drive, backdrivability, hand-guiding, kinesthetic-teaching, model-identification, mit-mode]
---

# Gravity compensation

## Definition

**Gravity compensation** commands each joint with the torque needed to hold the arm against gravity in its current pose, **τ_g(q)**. With that torque as feedforward and little or no position stiffness, the arm "floats": it stays where it is put and moves freely when pushed. τ_g(q) comes from the robot's rigid-body model (link masses, centres of mass, joint axes and offsets) through inverse dynamics with zero velocity and acceleration. In practice that means an RNEA call, or a library's generalized-gravity function, as in [Pinocchio](../../entities/pinocchio.md) ([Holoscan 5 tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)).

The full control law in the reference implementation is **gravity feedforward plus light stiffness and damping**: τ = τ_g(q) + K_p(q_ref − q) + K_d(q̇_ref − q̇), with K_p = 1.5 and K_d = 1.0 by default. That is a soft [impedance](impedance-control.md) controller whose spring is centred on wherever gravity comp lets the arm settle.

## Why it matters

- **It checks the robot model.** Position control hides model errors, because a stiff servo just pushes through them. Under gravity comp, a wrong mass, axis sign, offset or link length shows up at once as an arm that **sags or rises as the pose changes** ([tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)). It is the cheapest validation of the URDF that sim-to-real and model-based control both depend on.
- **It enables hand-guided teaching.** Kinesthetic demonstration, where the user moves the arm itself rather than a leader arm, needs the arm to hold its own weight while yielding to a hand. It is an alternative data-collection path to leader/follower teleop for [imitation learning](../learning/imitation-learning.md).
- **It is the base of every compliant controller.** Impedance, admittance and [operational-space control](operational-space-control.md) all assume the gravity term is cancelled. Errors in τ_g show up as steady-state pose offsets in a soft controller.
- **It is a safety primitive for co-bots.** It lets the arm yield to contact instead of fighting it ([collaborative robots](collaborative-robots.md)).

## Hardware precondition: torque you can command and feel

Gravity comp needs actuators that take a **torque command** and are **backdrivable** enough for a hand to move them. High-ratio hobby servos fail both tests. They accept only position commands, and gearbox friction swamps the hand's force. That rules out the [FeeTech](../../entities/feetech.md)-class arms ([SO-ARM101](../../entities/so-arm101.md), [XLeRobot](../../entities/xlerobot.md)). **Quasi-direct-drive** CAN actuators ([Damiao](../../entities/damiao.md), [Robstride](../../entities/robstride.md)) pass both, which is why the [reBot Arm B601](../../entities/rebot-arm-b601.md) is the cheapest arm in the wiki shown doing it ([tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)). Research arms (Franka, [OpenArm](../../entities/openarm.md)) do it as standard.

## Where the loop runs, and why timing claims need care

On QDD motors with an **MIT-style command** (position, velocity, K_p, K_d and feedforward torque in one frame), the PD part closes **inside the motor driver**. The host only refreshes τ_g and the setpoint. Host jitter then means a slightly stale gravity term, not an unstable loop. It becomes critical only when the host closes a torque loop itself. Bus bandwidth can dominate either way: seven motors on 1 Mbit/s CAN use most of a 2.5 ms cycle on frames alone (estimate on the [source page](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md#reading-the-latency-table-against-the-budget)).

## On the cheaper tier

For a FeeTech-servo arm, see [Can the SO-101 do gravity compensation?](../../syntheses/projects/so101-gravity-compensation.md). The answer is partly: admittance-style hand guiding and URDF validation by static-load fitting work, but true weightless feel does not, because of the 1:345 gearbox.

## Key references

- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) — a full reference implementation on a $1.5k arm, with latency measurements.

## Related concepts

- [Impedance and admittance control](impedance-control.md) — gravity comp is its feedforward term
- [Operational space control](operational-space-control.md) — the task-space formulation, which also cancels gravity
- [Collaborative robots](collaborative-robots.md) — hand-guiding as a co-bot feature
- [Control abstraction levels](control-abstraction-levels.md) — learned policies sending pose targets into a compliant, gravity-compensated arm
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — the same URDF fidelity matters for both

## Current state

Textbook control, solved on research arms. It is newly reachable at the hobby-to-prosumer tier, because QDD actuators have reached ~$1.5k arms. Commercial runtimes now ship it as a demo ([Holoscan 5](../../entities/nvidia-holoscan.md)). The wiki has **no measurement of friction or backdrive torque** on any affordable arm, so it can't yet say how "weightless" the cheaper tier really feels.

## Mentioned in

- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)
