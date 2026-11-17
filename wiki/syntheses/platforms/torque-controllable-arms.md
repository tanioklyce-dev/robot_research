---
title: Torque-controllable arms — which motors do gravity compensation, and which arms have them
type: synthesis
created: 2026-11-16
updated: 2026-11-16
tags: [platform-comparison, gravity-compensation, torque-control, actuators, quasi-direct-drive, planetary, harmonic-drive, backdrivability, damiao, robstride, feetech, dynamixel, yam, rebot-arm, openarm, franka, unitree-z1, buying-decision]
---

# Torque-controllable arms

**Which motor type is best for [gravity compensation](../../concepts/robotics/gravity-compensation.md), and which arms in this wiki have it?** This page came out of a query on 2026-11-16, and the gear ratios were then checked against Damiao's own datasheets the same day.

**Short answer:** a **low-ratio brushless actuator commanded by current**, usually called quasi-direct-drive (QDD), at about 10:1 or below. The proven alternative is a **geared joint with a torque sensor** (Franka). In practice the good affordable arms are **hybrids**: 40:1 at the shoulder and elbow, QDD at the wrist, with software friction compensation on top.

## What makes a motor good for gravity comp

1. **Torque is commandable through current.** A brushless motor's torque is close to proportional to current, so the driver can both command and measure torque with no extra sensor. Damiao's drivers turn an MIT frame (p_des, v_des, Kp, Kd, t_ff) into a current setpoint, and setting Kp = Kd = 0 gives pure torque output ([DM-J4340P datasheet](../../sources/damiao-dm-j4340p-2ec-datasheet.md)).
2. **Low reduction means transparency.** Gearbox friction and reflected rotor inertia (which scales with the square of the ratio) rise steeply with ratio. At about 10:1 or below, a hand can move the joint and motor current still reflects external force. See [the SO-101 analysis](../projects/so101-gravity-compensation.md#why-it-is-hard-on-this-arm) for the high-ratio end.
3. **The impedance loop runs in the driver.** With an MIT-style interface, stiffness and damping close at the motor, and the host only refreshes the gravity term ([Holoscan tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)).

**The counter-pressure is heat.** Gravity comp is continuous holding torque. The implied output torque constants, rated torque ÷ rated current (my derivation from the datasheets), make the cost visible:

| Motor | Ratio | Rated / peak torque | ≈ N·m per A | Source |
|---|---|---|---|---|
| Damiao DM-J4310-2EC | 10:1 | 3 / 7 N·m | 1.2 | [datasheet](../../sources/damiao-dm-j4310-2ec-datasheet.md) |
| Damiao DM-J8009P-2EC | 9:1 | 20 / 40 N·m | 1.0 | [datasheet](../../sources/damiao-dm-j8009p-2ec-datasheet.md) |
| Damiao DM-J4340(P)-2EC | 40:1 | 9 / 27 N·m | 3.6 | [J4340](../../sources/damiao-dm-j4340-2ec-datasheet.md), [J4340P](../../sources/damiao-dm-j4340p-2ec-datasheet.md) |

A 40:1 joint holds a given torque on about a third of the current, which means much less I²R heat. **That is why every affordable arm here puts 40:1 at the shoulder**, and why "all-QDD" is rare outside large-motor designs like OpenArm's J8009P joints.

## The actuator ladder

| Actuator type | Ratio | Gravity comp | Examples |
|---|---|---|---|
| Direct drive | 1:1 | Ideal feel; heavy, and hottest when holding a pose | none in the wiki |
| **QDD CAN actuator** | ≤ ~10:1 | **Most transparent at this price**; current is a torque sensor | DM-J4310 (10:1), DM-J8009P (9:1) |
| **Moderate-ratio CAN actuator** | ~40:1 | **Works**, with more friction; benefits from friction compensation | DM-J4340 / J4340P (40:1) |
| Harmonic drive + torque/impedance interface | high | Works if torque is sensed or well estimated | [Franka Panda](../../entities/franka-panda.md) (joint torque sensors), [Unitree Z1](../../entities/unitree-z1.md) |
| Smart serial servo | 1:345 (STS3215) | Poor: position-only, *"limited backdrivability"* | [FeeTech](../../entities/feetech.md); [Dynamixel](../../entities/dynamixel.md) is geared too |

## Arms in this wiki, by fitness for gravity comp

| Arm | Price | DOF | Proximal / distal actuators | Gravity comp evidence |
|---|---|---|---|---|
| [YAM](../../entities/yam.md) (i2RT) | $2,999–$4,999 | 6 | 3× DM4340 (40:1) / 3× DM4310 (10:1) | **Vendor-documented** gravity-comp and zero-gravity modes, with model-based gravity **plus Coulomb-friction compensation** ([docs](../../sources/i2rt-yam-docs.md)) |
| [reBot B601-DM](../../entities/rebot-arm-b601.md) (Seeed) | **$1,499** bare | 6+1 | 3× J4340P (40:1) / 4× J4310 (10:1) | **Demonstrated**: hand-guided gravity comp at 400 Hz ([Holoscan tutorial](../../sources/nvidia-holoscan-5-rebot-gravity-compensation.md)) |
| [reBot B601-RS](../../entities/rebot-arm-b601.md) | not captured | 6+1 | Robstride 06 ×3 / 00 ×4, ratios unknown | Exposes MIT gains per joint; no gravity-comp demo |
| [OpenArm](../../entities/openarm.md) (Enactic) | ~$5,200–$5,400 assembled ($6,500 bimanual) | 7 | J8009P (9:1), DM4340 (40:1), J4310 (10:1) | Bilateral force-feedback teleop; **records joint torque** in its datasets ([docs](../../sources/openarm-docs.md)) |
| [Yuri](../../entities/yuri.md) (Sensori) | not captured | 2× 7 | OpenArm+ | *"Backdrivable joints"*, real-time torque feedback; integrated and supported |
| [Unitree Z1](../../entities/unitree-z1.md) | not captured | 6 | Harmonic reducers, 33 N·m peak | Torque/stiffness/damping commands at 1 kHz, ~0.2 N·m force accuracy; low-stiffness caveat |
| [Franka Panda](../../entities/franka-panda.md) | < €30k | 7 | Harmonic + joint torque sensors | 1 kHz torque control out of the box; the research reference |

**Not suitable as torque-mode arms:** [SO-ARM101](../../entities/so-arm101.md), [LeKiwi](../../entities/lekiwi.md), [XLeRobot](../../entities/xlerobot.md) and [Sourccey](../../entities/sourccey.md), all FeeTech (see [the SO-101 analysis](../projects/so101-gravity-compensation.md) for what is still possible). [AgileX Piper](../../entities/agilex-piper.md) ($2,500) has no force sensor, but [FACTR 2](../../sources/factr-2-paper.md) estimates its external torque from current. [Koch v1.1](../../entities/koch-v1-1.md) uses Dynamixel servos, which support torque control but are geared servos; I'd expect SO-101-class results, unverified.

> [!warning] "Quasi-direct-drive" is a marketing label on half these arms
> Seeed, NVIDIA and the UME paper all call these arms or actuators QDD. Per Damiao's datasheets, the **reBot B601-DM, YAM and UME are 40:1 at their high-torque joints** and QDD only at the wrist. OpenArm's documentation is the one source that says so plainly (*"DM4340… 40:1, not QDD"*). Count gear ratios, not adjectives. Corrected across the wiki on 2026-11-16 (see the [log](../../log.md)).

## Recommendation

- **Gravity comp that works out of the box: YAM.** The vendor ships the mode, including friction compensation, which is the part that makes 40:1 proximal joints feel right. It is also the arm frontier VLA corpora are being collected on ([GR00T 2](../../sources/gr00t-2-whitepaper.md)).
- **Cheapest way to learn torque control: reBot B601-DM ($1,499).** A reference gravity-comp implementation exists. Budget for the power supply and clamp ([product page](../../sources/seeed-rebot-arm-b601-dm-thor-bundle.md)).
- **Most transparent proximal joints, with torque logged: OpenArm.** Its 9:1 J8009P joints are the only big QDD motors in the table.
- **If you already own an SO-101:** use it for admittance-style hand-guiding and URDF validation, not for torque control ([plan](../projects/so101-gravity-compensation.md)).

## What would sharpen this

- **Backdrive-torque and friction measurements** on any of these arms. No source in the wiki has one, and they are the numbers that would actually rank YAM, reBot and OpenArm on feel.
- **Robstride 00 / 06 datasheets**: the RS variant's gear ratios are unknown here.
- A **continuous-stall thermal rating** for the Damiao parts. The datasheets give rated and peak values only, not how long a QDD shoulder can hold a pose.

## Related

- [Gravity compensation](../../concepts/robotics/gravity-compensation.md), [Impedance and admittance control](../../concepts/robotics/impedance-control.md), [Contact-rich manipulation](../../concepts/robotics/contact-rich-manipulation.md)
- [Damiao](../../entities/damiao.md), [Robstride](../../entities/robstride.md), [FeeTech](../../entities/feetech.md), [Dynamixel](../../entities/dynamixel.md)
- [Can the SO-101 do gravity compensation?](../projects/so101-gravity-compensation.md)
- [Robot platforms comparison](robot-platforms-comparison.md)
