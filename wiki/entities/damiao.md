---
title: Damiao (DM motors)
type: entity
subtype: organization
created: 2026-08-27
updated: 2026-08-27
sources: 2
tags: [damiao, actuators, quasi-direct-drive, can-bus, mit-mode, robot-arm, rebot-arm, motors]
---

**Damiao** (达妙 / DM) — Chinese manufacturer of **quasi-direct-drive CAN-bus actuators** for robotics. In this wiki, Damiao is the motor lineage behind the **[reBot Arm B601-DM](rebot-arm-b601.md)**.

## Why it belongs in the motor ladder

The wiki tracks two low-cost motor lineages that [LeRobot](lerobot.md) integrates natively — [FeeTech](feetech.md) (hobby tier, STS3215 smart serial bus) and [Dynamixel](dynamixel.md) (education/research tier). **Damiao and [Robstride](robstride.md) are a third, structurally different tier**: planetary quasi-direct-drive actuators speaking **CAN at 1 Mbit/s** with an **MIT-style impedance interface** (position + velocity + `kp`/`kd` + feedforward torque per command), rather than a position-only serial servo protocol.

That difference is the reason a $1,499 arm can claim 0.2 mm repeatability and be a credible platform for contact-rich manipulation: MIT mode gives you torque-level control and (in principle) backdrivability, which position-only smart servos do not.

## Parts used in the reBot B601-DM

| Motor | Count | Role |
|---|---|---|
| **DM-J4340P-2EC** | 3 | High-torque, low-noise — the proximal joints (shoulder pan / lift / elbow) |
| **DM-J4310-2EC** | 4 | Wrist flex / yaw / roll + gripper |

Arm bus: DC 24 V 10 A, CAN at 1 Mbit/s, seven nodes ([product page](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md)).

## Tooling and integration notes

- **Motor IDs are set from a Windows-only GUI**, `DM_Tools_v1.8.0.1.exe`, over a **USB-CAN adapter board** plus an XT30 (2+2) signal-power separation board. The [DLI course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) requires a dual-boot machine for this step alone — Linux for everything else, Windows for the motor tool.
- LeRobot addresses the DM arm as `seeed_b601_dm_follower` with `--robot.can_adapter=damiao` on `/dev/ttyACM0` at 921600 baud, i.e. through Damiao's own USB-CAN protocol rather than SocketCAN. (The Robstride variant uses SocketCAN `can0` instead.)
- Observed motor CAN ID pairs from the course calibration log: `(1,17) (2,18) (3,19) (4,20) (5,21) (6,22) (7,23)` — a send/receive ID pair per joint, offset by 16.
- Damiao operating modes appear as `ensure mode 2` for the arm joints and `mode 4` for the gripper in the DM path (vs `mode 1` throughout on Robstride) — the two vendors do not share a mode numbering.

## Open questions

- **Backdrivability is unmeasured** anywhere in the wiki's sources. It is the property that would most differentiate this tier from FeeTech, and nobody has published a number.
- **No torque, gear-ratio, or thermal specs** appear on the Seeed listing — only the part numbers. The primary Damiao datasheets have not been ingested.

## Related

- [Robstride](robstride.md) — the sibling CAN-actuator lineage; the other B601 variant
- [FeeTech](feetech.md) / [Dynamixel](dynamixel.md) — the two serial-bus tiers below
- [reBot Arm B601](rebot-arm-b601.md) — the arm

## Mentioned in

- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — the DM part numbers and bus spec
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — motor-ID setup, LeRobot `damiao` adapter, CAN ID pairs
