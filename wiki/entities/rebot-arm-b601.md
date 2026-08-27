---
title: reBot Arm B601
type: entity
subtype: robot
created: 2026-08-27
updated: 2026-08-27
sources: 2
tags: [rebot-arm, b601-dm, b601-rs, seeed-studio, robot-arm, damiao, robstride, can-bus, open-hardware, lerobot, isaac-sim, groot, jetson-thor]
---

**reBot Arm B601** — [Seeed Studio](seeed-studio.md)'s fully open-source **6+1-DOF benchtop manipulator** built on CAN-bus quasi-direct-drive actuators, sold in two motor variants (**DM** and **RS**) and marketed as a sim-to-real / [VLA](../concepts/learning/vla-models.md) development platform. Product page: [reBot Arm B601-DM Bundle with Jetson Thor](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle-with-Jetson-Thor.html). Open-source files under [Seeed-Studio on GitHub](https://github.com/Seeed-Studio).

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
> Beyond the motors, the two arms differ in CAN adapter, device node, motor CAN ID pairing, joint-limit sign convention (DM `elbow_flex (-200, 1)` vs RS `(-0, 200)`), and MIT control mode (`mode 2` vs `mode 1`). The RS config additionally exposes gripper impedance gains (`gripper_mit_kp 12.0`, `kd 0.05`, `torque_limit 8.0`) that the DM config does not. **Commands copied from the course will not work verbatim on a DM arm** — the course is written against the RS while its motor-setup section links DM hardware; see the contradiction callout on the [course page](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md).

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

## Open questions

- **Backdrivability is unmeasured.** Quasi-direct-drive CAN actuators should be far more backdrivable than the FeeTech gearboxes the wiki documents, which would make the B601 the first affordable-tier arm suited to compliant contact tasks and force-feedback teleop — but neither source measures it.
- **No published VLA success rates on this arm.** The DLI course demonstrates autonomous pick-and-place and reports no number.
- **Real end-of-arm payload with gripper at full reach.** The 1.5 kg DM figure is qualified away from both conditions.

## Related

- [Seeed Studio](seeed-studio.md) — vendor
- [Star Arm 102](star-arm-102.md) — the matching leader arm for teleoperation
- [Damiao](damiao.md) / [Robstride](robstride.md) — the two actuator lineages
- [SO-ARM101](so-arm101.md) — the tier below; the LeRobot ecosystem default
- [Jetson Thor](jetson-thor.md) — the bundled compute option
- [NVIDIA GR00T](nvidia-groot.md) — the policy the course targets
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [Generative data augmentation](../concepts/learning/generative-data-augmentation.md)

## Mentioned in

- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — the product page and DM spec table
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — the 19-module DLI course; RS spec table and the full pipeline
