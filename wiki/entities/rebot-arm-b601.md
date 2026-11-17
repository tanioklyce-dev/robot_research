---
title: reBot Arm B601
type: entity
subtype: robot
created: 2026-08-27
updated: 2026-11-16
sources: 5
tags: [rebot-arm, gravity-compensation, torque-control, holoscan, motorbridge, b601-dm, b601-rs, seeed-studio, robot-arm, damiao, robstride, can-bus, open-hardware, lerobot, isaac-sim, groot, jetson-thor]
---

**reBot Arm B601** — [Seeed Studio](seeed-studio.md)'s fully open-source **6+1-DOF benchtop manipulator** built on CAN-bus brushless joint actuators (marketed as quasi-direct-drive; on the DM variant that holds only at the wrist, see below), sold in two motor variants (**DM** and **RS**) and marketed as a sim-to-real / [VLA](../concepts/learning/vla-models.md) development platform. Product page: [reBot Arm B601-DM Bundle with Jetson Thor](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle-with-Jetson-Thor.html). Open-source files under [Seeed-Studio on GitHub](https://github.com/Seeed-Studio).

## Where it sits in this wiki's platform ladder

The B601 fills a **gap the wiki previously had no entry in**. The affordable tier here is FeeTech-servo arms — [SO-ARM101](so-arm101.md), [LeKiwi](lekiwi.md), [XLeRobot](xlerobot.md) — at $100–$700, using [FeeTech](feetech.md) STS3215 smart serial-bus servos with documented backdrivability limits and position-only recording. The research tier starts around $20k. The B601 is **$1,499 bare** with real CAN actuators, 0.1–0.2 mm repeatability, and 48 V/24 V power — an order of magnitude more capable than an SO-ARM101 and an order of magnitude cheaper than a Franka.

Its software story is what makes it wiki-relevant rather than just another arm: it is addressed **natively from [LeRobot](lerobot.md)** (as `seeed_b601_dm_follower` / `seeed_b601_rs_follower`), it ships an [Isaac Sim](nvidia-isaac-sim.md) model, and Seeed publishes a full [NVIDIA DLI course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) taking it through [Cosmos](nvidia-cosmos.md) augmentation and [GR00T 1.7](nvidia-groot.md) fine-tuning to TensorRT on [Jetson](jetson-thor.md).

## Variants

| | **B601-DM** ("Versatile Robotics") | **B601-RS** ("High Performance") |
|---|---|---|
| Actuators | [Damiao](damiao.md) DM-J4340P-2EC ×3 + DM-J4310-2EC ×4 | [Robstride](robstride.md) 06 ×3 + 00 ×4 |
| DOF | 6+1 | 6+1 |
| Reach | **767 mm** (607 mm without gripper) | **754 mm** |
| Payload | **1.5 kg** (no gripper, 70% reach) | **2.5 kg** rated / 5 kg max |
| Repeatability | **0.2 mm** | **< 0.1 mm** |
| Weight | ~4.7 kg | 6.5 kg |
| Power | DC **24 V 10 A** | **48 V 15 A** |
| Joint range | J1 ±150°, J2/J3 −220–0°, J4/J5/J6 ±90°, gripper −325–0° | not published on the course spec sheet |
| Operating temp | −20 – 50 °C | −20 – 50 °C |
| LeRobot type | `seeed_b601_dm_follower`, adapter `damiao`, `/dev/ttyACM0` | `seeed_b601_rs_follower`, adapter `socketcan`, `can0` |

Sources: DM from the [product page spec table](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md); RS from the [DLI course §1.4](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md).

> [!warning] The variants are not interchangeable in software
> Beyond the motors, the two arms differ in CAN adapter, device node, motor CAN ID pairing, joint-limit sign convention (DM `elbow_flex (-200, 1)` vs RS `(-0, 200)`), and motor control mode (`mode 2` vs `mode 1`). *Corrected 2026-11-16:* on Damiao, **mode 2 is position-speed, not MIT**. MIT is mode 1 ([J4340P datasheet](../sources/damiao-dm-j4340p-2ec-datasheet.md)). The DM course path therefore runs the arm joints as position-controlled cascades, and the gripper in mode 4 (force-position hybrid). Robstride's numbering is separate and undocumented here. The RS config additionally exposes gripper impedance gains (`gripper_mit_kp 12.0`, `kd 0.05`, `torque_limit 8.0`) that the DM config does not. **Commands copied from the course will not work verbatim on a DM arm** — the course is written against the RS while its motor-setup section links DM hardware; see the contradiction callout on the [course page](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md).

## Pricing (captured 2026-08-27)

| Configuration | Price |
|---|---|
| B601-DM, assembled, no power supply | **$1,499** |
| Power adapter kit | $59 |
| + [Jetson AGX Thor Developer Kit](jetson-thor.md) | +$5,499 (**$7,057** bundle subtotal, ~$6,916 after 2% off) |
| [Star Arm 102](star-arm-102.md) leader arm (for teleop) | $200 |
| 6-inch G-clamp (**required** to mount to a bench) | $14.70 |

Configurable across Assembled/Unassembled, AI compute None/Orin/Thor, and Robot Arm + Gripper / Complete Kit / DIY Kit. **A power supply and a mounting clamp are both separate line items** — the bare $1,499 arm is not a working setup on its own.

## Software support

Vendor-claimed and course-demonstrated: **ROS 1 / ROS 2, MoveIt 1 / MoveIt 2, Python SDK, [LeRobot](lerobot.md), [Isaac Sim](nvidia-isaac-sim.md), Pinocchio**. LeRobot integration is via three Seeed forks (`Seeed-Projects/lerobot`, `lerobot-teleoperator-rebot-arm-102`, `lerobot-robot-seeed-b601`) rather than upstream LeRobot — so **the arm is a fork-tier citizen, not an upstream-supported robot**, which is a maintenance risk worth pricing in.

Documented demos: teleoperated LeRobot data collection → GR00T 1.7 fine-tune → on-Jetson TensorRT inference (the [DLI course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md)); GraspNet-Baseline visual grasping with an [Orbbec](orbbec.md) Gemini 2 RGB-D camera; edge-LLM voice control on Thor.

## Gearing: QDD at the wrist, 40:1 at the shoulder (DM variant, 2026-11-16)

Damiao's datasheets settle a label the wiki had repeated from Seeed and NVIDIA. The **three proximal joints** (shoulder pan, shoulder lift, elbow) use **DM-J4340P-2EC: 40:1, 9 / 27 N·m** ([datasheet](../sources/damiao-dm-j4340p-2ec-datasheet.md)), a conventional planetary and not QDD. The **four distal joints** (wrist ×3 + gripper) use **DM-J4310-2EC: 10:1, 3 / 7 N·m** ([datasheet](../sources/damiao-dm-j4310-2ec-datasheet.md)), which is QDD. So "quasi-direct-drive arm" describes half the joints. The heavy joints, which carry most of the gravity load, are geared 40:1. Gravity compensation and hand-guiding still work on them, as the Holoscan demo shows, but they'll show more friction and reflected inertia than the label implies. The RS variant's [Robstride](robstride.md) gear ratios are not in the wiki.

## Torque mode: gravity compensation under Holoscan 5 (2026-11-09)

NVIDIA's [Holoscan 5 tutorial](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) is the first source to run the B601-**DM** in **torque mode** rather than position mode. A 400 Hz loop reads all seven motors through Seeed's **`motorbridge`** library and computes gravity torque with [Pinocchio](pinocchio.md) from the arm's URDF. It sends feedforward torque plus soft gains (kp 1.5, kd 1.0) in the motors' MIT-style command, so the arm holds its own weight and can be **guided by hand**. A second example adds Cartesian [impedance control](../concepts/robotics/impedance-control.md) with an injectable goal pose, *"for example from a learned policy."* Tested hosts: Jetson Orin Nano, Jetson Thor, x86. Safety: a 100 ms command watchdog, and the arm must start and end in its power-off-safe home pose. See [gravity compensation](../concepts/robotics/gravity-compensation.md).

This answers part of the backdrivability question below. The arm *is* backdrivable enough for hand-guiding under gravity comp, which no [FeeTech](feetech.md)-tier arm in the wiki can do.

## Open questions

- **Backdrivability is demonstrated, not measured.** The [Holoscan tutorial](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) shows hand-guiding under gravity compensation, which no FeeTech arm can do. No source gives friction, cogging or backdrive-torque figures per joint, so how compliant the arm is in contact tasks and force-feedback teleop remains unquantified.
- **No published VLA success rates on this arm.** The DLI course demonstrates autonomous pick-and-place and reports no number.
- **Real end-of-arm payload with gripper at full reach.** The 1.5 kg DM figure is qualified away from both conditions.

## Related

- [Seeed Studio](seeed-studio.md) — vendor
- [Star Arm 102](star-arm-102.md) — the matching leader arm for teleoperation
- [Damiao](damiao.md) / [Robstride](robstride.md) — the two actuator lineages
- [SO-ARM101](so-arm101.md) — the tier below; the LeRobot ecosystem default
- [Jetson Thor](jetson-thor.md) — the bundled compute option
- [NVIDIA GR00T](nvidia-groot.md) — the policy the course targets
- [NVIDIA Holoscan](nvidia-holoscan.md), [Pinocchio](pinocchio.md) — the torque-mode control stack
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [Generative data augmentation](../concepts/learning/generative-data-augmentation.md)

## Mentioned in

- [DM-J4340P-2EC datasheet](../sources/damiao-dm-j4340p-2ec-datasheet.md) / [DM-J4310-2EC datasheet](../sources/damiao-dm-j4310-2ec-datasheet.md) — the DM variant's actual gear ratios (40:1 proximal, 10:1 distal) and the mode numbering.
- [Torque-controllable arms](../syntheses/platforms/torque-controllable-arms.md) — where the B601 sits among arms that can do gravity compensation.

- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — the product page and DM spec table
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — the 19-module DLI course; RS spec table and the full pipeline
- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) — DM variant in torque mode: gravity compensation and impedance control, with latency figures
