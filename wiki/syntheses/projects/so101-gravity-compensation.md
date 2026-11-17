---
title: Can the SO-101 do gravity compensation?
type: synthesis
created: 2026-11-16
updated: 2026-11-16
tags: [project-scope, so-arm101, feetech, sts3215, gravity-compensation, admittance-control, hand-guiding, kinesthetic-teaching, system-identification, urdf, pinocchio, experiment]
---

# Can the SO-101 do gravity compensation?

**Short answer: partly.** An approximate version can be built on the [SO-ARM101](../../entities/so-arm101.md). It won't feel "weightless" the way the [reBot B601-DM](../../entities/rebot-arm-b601.md) does in [NVIDIA's Holoscan tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md), and the most useful version for this arm is admittance-style hand guiding, not torque feedforward.

This page came out of a query on 2026-11-16. It builds on [Gravity compensation](../../concepts/robotics/gravity-compensation.md), [Impedance and admittance control](../../concepts/robotics/impedance-control.md) and [FeeTech](../../entities/feetech.md).

## Why it is hard on this arm

Gravity compensation needs actuators that **accept a torque command** and are **backdrivable** enough for a hand to move them ([concept page](../../concepts/robotics/gravity-compensation.md#hardware-precondition-torque-you-can-command-and-feel)). The SO-101's FeeTech STS3215 servos are weak on both:

| | reBot B601-DM ([Damiao](../../entities/damiao.md) CAN actuators) | SO-101 (FeeTech STS3215) |
|---|---|---|
| Command interface | MIT-style: position + velocity + kp + kd + **feedforward torque** in one frame | Position commands into a gearbox ([FeeTech](../../entities/feetech.md)) |
| Gearing | **40:1** shoulder/elbow (J4340P), **10:1** wrist (J4310) ([datasheets](../../sources/damiao-dm-j4340p-2ec-datasheet.md)) | **1:345** ([FeeTech](../../entities/feetech.md), via the LeKiwi repo) |
| Backdrivability | Hand-guided under gravity comp ([tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)) | *"Limited due to high resistance under load"* ([Vulcan / Sourccey](../../sources/vulcan-robotics-sourccey-site.md)) |
| Bus | CAN, 1 Mbit/s | Half-duplex UART, 1 Mbaud ([FeeTech](../../entities/feetech.md)) |

Even the reBot's heavy joints are 40:1, about 9× lower than the SO-101's 1:345. At 1:345, gearbox friction and reflected rotor inertia (which scales with the square of the gear ratio) are large compared with the gravity torques you would be cancelling. Even with perfect cancellation, the hand would still feel the friction. **The feel comes from the hardware, not from software.** Gravity comp on the reBot feels weightless because the gearing is low, not because the controller is clever.

> [!note] Unverified actuator details
> The register-level claims below — an open-loop **PWM operating mode**, and readable **present load** and **present current** — come from general knowledge of the STS3215, not from an ingested source. The wiki has no FeeTech datasheet or memory table (see the [backlog](../../backlog.md)). Verify against the primary before building on them. The [Sourccey](../../sources/vulcan-robotics-sourccey-site.md) source does confirm that servo current is readable, since it is used for calibration and limits.

## Three approaches, in order of usefulness

### 1. System identification: validate the URDF (do this first)

The main engineering value of gravity comp is that it **checks the robot model**. Position control hides model errors, and torque control exposes them ([tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)). You can get the same check here without torque control:

1. Put the follower arm in **20–30 static poses** that cover the workspace. Approach each pose from both directions, so friction cancels out on average.
2. At each pose, log the joint angles and each servo's present load (or current).
3. Compute the predicted gravity torque τ_g(q) per joint with [Pinocchio](../../entities/pinocchio.md) from the SO-101 URDF.
4. Fit measured load against τ_g per joint (scale + offset). Look at the residuals.

What it gives you: a per-joint **load-to-torque scale**, which approaches 2 and 3 both need, plus a direct test of the URDF's masses and centres of mass. A poor fit tells you which link is wrong. That matters for any [sim-to-real](../../concepts/learning/sim-to-real-transfer.md) work on this arm, and for the [RoboTwin](five-dof-arms-in-robotwin.md) and Isaac-based plans in this folder.

**Cost:** an afternoon. No firmware changes, no risk to the arm.

### 2. Admittance-style hand guiding (the recommended control mode)

[Impedance control](../../concepts/robotics/impedance-control.md) notes that **admittance suits position-controlled robots**, and that describes the STS3215 exactly. Stay in position mode and close the loop on force:

```
every cycle:
    q            = read joint positions
    load         = read present load            # scaled to N·m by step 1's fit
    tau_ext      = load − tau_g(q)              # what the hand is adding
    tau_ext      = deadband(tau_ext, threshold) # reject sensor noise and friction
    q_target    += K_adm · tau_ext · dt         # move with the push
    write q_target
```

This works *with* the gearbox, because friction no longer has to be overcome by the hand, and it keeps the servos' own position loop in charge. It feels viscous and slightly laggy, not floaty. The deadband is the main tuning knob: too small and the arm creeps under sensor noise, too large and it feels sticky. **This is the version that enables kinesthetic teaching on an SO-101**, an alternative to leader-arm teleop for collecting demonstrations.

### 3. Gravity torque as open-loop PWM (possible, least robust)

Switch to PWM mode and command `pwm = τ_g(q) / k_pwm`, where k_pwm is a per-joint torque-per-PWM constant you calibrate yourself. It roughly holds pose. It is fragile because **PWM sets voltage, not torque**: output drifts with motor temperature, supply voltage and back-EMF at speed. On the reBot, the motor drivers do that compensation internally. The 1:345 gearbox makes it partly moot, since it holds pose by friction anyway. Try it only to learn what a torque-mode controller is up against.

## Loop rate and bus

Six servos share one 1 Mbaud half-duplex UART ([FeeTech](../../entities/feetech.md)). By my estimate, which I haven't measured, a sync read of position and load plus a sync write fits **roughly 100–200 Hz**. That is enough for approach 2, whose dynamics are slow by design. For comparison, the reBot loop runs at 400 Hz on 1 Mbit/s CAN, and there the bus probably sets the ceiling ([tutorial analysis](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md#reading-the-latency-table-against-the-budget)). Measure the achieved rate before tuning K_adm.

The runtime doesn't matter much at this rate. A plain Python loop is enough. [Holoscan](../../entities/nvidia-holoscan.md) 5 would work, but needs JetPack 7.2.1 and CUDA 13 ([requirements](../../sources/holoscan-sdk-5-0-release-notes.md)), which is far more stack than a 6-servo UART loop needs.

## Leader vs follower

Do approaches 1 and 2 on the **follower** arm, the 1:345 variant. Leader arms are reportedly built with lower-ratio servo variants so they are easier to move by hand, but **the wiki does not record this**. Verify it from the SO-101 BOM before relying on it. If true, a leader arm would be the better candidate for approach 3.

## What would change this assessment

- **A FeeTech register table** (primary). It would confirm or rule out the PWM mode and the load/current resolution that approaches 2 and 3 rely on.
- **A backdrive-torque measurement** on any FeeTech arm. Neither this tier nor the Damiao/Robstride tier has one in the wiki ([FeeTech](../../entities/feetech.md#the-tier-above)).
- **Current-sensing noise floor.** If present load is too coarse or too noisy, the admittance deadband has to be large and the feel degrades sharply.

## Related

- [Gravity compensation](../../concepts/robotics/gravity-compensation.md), [Impedance and admittance control](../../concepts/robotics/impedance-control.md)
- [SO-ARM101](../../entities/so-arm101.md), [FeeTech](../../entities/feetech.md), [reBot Arm B601](../../entities/rebot-arm-b601.md)
- [Pinocchio](../../entities/pinocchio.md)
- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) — the CAN-actuator reference this page contrasts with
- [Torque-controllable arms](../platforms/torque-controllable-arms.md) — what to buy if you want gravity comp to feel right
