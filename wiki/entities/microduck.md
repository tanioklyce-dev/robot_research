---
title: Microduck
type: entity
subtype: robot
created: 2026-08-27
updated: 2026-08-27
sources: 1
tags: [microduck, pollen-robotics, hugging-face, biped, reinforcement-learning, sim-to-real, mjlab, dynamixel, rk3566, consumer-robotics, education]
---

**Vendor page:** [pollen-robotics.com/microduck](https://pollen-robotics.com/microduck/) · **Code:** [`pollen-robotics/microduck`](https://github.com/pollen-robotics/microduck) (runtime, Rust) · [`pollen-robotics/microduck_rl`](https://github.com/pollen-robotics/microduck_rl) (training, Python)

**Microduck** — a 25 cm, sub-800 g bipedal robot from [Pollen Robotics](pollen-robotics.md) ([Hugging Face](hugging-face.md)'s robotics team), announced **2026-08-27** at an introductory **$399**, shipping before Christmas 2026. Pollen's second consumer robot after [Reachy Mini](reachy-mini.md), and the first robot in this wiki whose **complete RL training recipe ships with the product** ([launch bundle](../sources/pollen-robotics-microduck.md)).

Positioning, per the launch post: *"Reachy Mini is a platform for AI that **interacts**, while Microduck is a platform for AI that **acts**."*

## Specs ([press kit](../sources/pollen-robotics-microduck.md))

| | |
|---|---|
| Height / width | 25 cm / 14 cm |
| Weight | under 800 g |
| Actuation | 15 motors (14 servos + beak); [Dynamixel](dynamixel.md) **XL330** class |
| Compute | **Rockchip RK3566** with AI accelerator; **1 GB RAM / 32 GB storage** |
| Control | **50 Hz** onboard policy loop, ONNX |
| Vision | front camera + camera-use indicator LED |
| Depth | **8×8 time-of-flight matrix** (marketed as "LiDAR" — see below) |
| IMUs | 2 — body and head |
| Manipulation | articulated grasping beak |
| Audio | mic + speaker; per-robot generated voice, fixed for the robot's life |
| NFC | 2 antennas (head, beak) |
| Radio | Wi-Fi + Bluetooth |
| Power | removable **NP-F550** camera battery, 2600 mAh, ~1 h |

Four colourways (Cream, Graphite, Lavender, Sky). Add-on packs: charger $39, dev $119, accessory $39.

> [!warning] "LiDAR" is an 8×8 ToF matrix
> The landing page says LiDAR; the press-kit spec table says *"compact LiDAR, an 8×8 time-of-flight matrix"*; the launch blog says *"a small depth sensor."* Budget against **64 depth zones**, not a scanning point cloud. Details in the [source page](../sources/pollen-robotics-microduck.md).

> [!warning] Not open-source *hardware*
> The press kit explicitly asks press not to call it open-source hardware — only the software stack is. The `microduck_rl` README separately states design files are **CC BY-SA-NC** (non-commercial, hence not OSHWA-open). Both are Pollen primaries; see the [source page](../sources/pollen-robotics-microduck.md) for the unresolved framing.

## Shipped behaviours

Seven policies in the box: **walk** (velocity tracking), **sit & stand**, **kick**, **grab** (beak to the floor, scoop, stand), **roller skating** (with skates), **get back up**, and a forward **roulade**. All are published and retrainable.

The RL repo registers **13 task families**, most with Flat/Rough terrain variants and all with a `-Backlash` twin: `Velocity`, `VelStand` (walk + fall-recovery in one policy), `StandUp`, `SitStand`, `GroundPick`, `BallKick` (70 mm / 15 g ball; *the actor is ball-blind*), `Roulade`, and six roller variants including `RollerSlope` and `Spin`.

## Software architecture

- **Training** — [mjlab](mjlab.md) (MuJoCo Warp + `rsl_rl`) with **PPO**; ~1–2 h at 4096 parallel envs for a usable gait on a CUDA GPU, or `--hf-jobs` to run it on **Hugging Face Jobs** with no local GPU. Export to **ONNX**.
- **Runtime** — Rust daemons on the RK3566 driving 15 servos from the ONNX policies at 50 Hz, plus radios, camera, and a health-gated reversible update system. CLI is `robotctl` (`monitor`, `configure`, `update`); `duckctl` drives it from a laptop over Bluetooth with no network.
- **Policy hot-swapping** — every policy shares a **61-dimensional observation contract** (48 proprioception + `twist(3)` + `head_pose(4)` + `body_pose(6)`); unused command slots are zero-padded rather than dropped, so walk / recover / trick brains can take over the robot at any moment.
- **Licence** — Apache-2.0 software. Hardware design files CC BY-SA-NC (per the RL repo).

## Why the sim-to-real work is the interesting part

Microduck's engineering thesis is that at 800 g and hobby-servo scale, **the reality gap lives in the actuator**, not in the renderer:

> "At this scale — tiny servos driving a ~800 g biped — actuator fidelity is most of the sim2real gap, which is why the actuator is modeled down to its voltage control law instead of an ideal PD."

That drives a **BAM M6** model of the XL330 (voltage control law, back-EMF, Coulomb/Stribeck/load-dependent friction), domain randomization over **battery voltage, voltage sag under load, command delay and friction magnitude**, and **backlash simulated as an unactuated hinge in series with each servo** — read *through* by the observations, because the real encoder sits on the output side of the play. See [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md).

## Position in the robot landscape

- **Lineage.** Microduck is the productised descendant of **Open Duck Mini**, the community project by Pollen R&D engineer **Antoine Pirrone** (a credited Microduck author) to build a miniature open-source version of Disney's BDX droid. Pollen's own launch materials do not mention that lineage; it is well attested in the `apirrone/Open_Duck_Mini` repository and the launch press coverage. *Treated here as likely-but-secondary until a Pollen primary confirms it.*
- **Price tier.** $399 sits below the [SO-ARM101](so-arm101.md) leader-follower pair and far below any legged research platform. It is the cheapest legged RL platform in this wiki by a wide margin.
- **Compute tier.** The RK3566 / 1 GB RAM budget is *below* every controller in the wiki's [edge-compute](jetson-thor.md) coverage. Microduck cannot host a [VLA](../concepts/learning/vla-models.md); it is structurally a small-MLP proprioceptive-policy machine.
- **Reset automation as a feature.** The get-back-up policy makes unattended iteration possible on a desk — the standing blocker in [real-world robot RL](../concepts/learning/real-world-robot-rl.md).
- **Multi-robot at hobby cost.** Four units for $1,596 makes [multi-agent RL](../concepts/learning/multi-agent-rl.md) experiments plausible outside a lab.

## Related

- [Pollen Robotics](pollen-robotics.md) — maker
- [Reachy Mini](reachy-mini.md) — sibling: interaction rather than action
- [Reachy 2](reachy.md) — the flagship manipulator
- [mjlab](mjlab.md) — the training framework
- [Dynamixel](dynamixel.md) — the servo lineage modeled by BAM

## Mentioned in

- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md)
