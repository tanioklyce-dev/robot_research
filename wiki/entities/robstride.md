---
title: Robstride (RS motors)
type: entity
subtype: organization
created: 2026-08-27
updated: 2026-08-27
sources: 2
tags: [robstride, actuators, quasi-direct-drive, can-bus, socketcan, mit-mode, rebot-arm, motors]
---

**Robstride** (RS) — Chinese manufacturer of **quasi-direct-drive CAN-bus actuators**, best known in the hobby/research robotics world for high-torque joint modules. In this wiki, Robstride is the motor lineage behind the **[reBot Arm B601-RS](rebot-arm-b601.md)**, the higher-spec sibling of the [Damiao](damiao.md)-based B601-DM.

## Parts used in the reBot B601-RS

| Motor | Count |
|---|---|
| **ROBSTRIDE 06** | 3 (proximal joints) |
| **ROBSTRIDE 00** | 4 (wrist + gripper) |

Arm bus: **48 V 15 A**, CAN at 1 Mbit/s ([DLI course §1.4](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md)).

## Why the RS arm outperforms the DM arm

The Robstride build reaches **2.5 kg rated / 5 kg maximum payload and < 0.1 mm repeatability**, against 1.5 kg and 0.2 mm for the Damiao build — at the cost of ~1.8 kg more mass and a **48 V** supply instead of 24 V. Doubling the bus voltage is the direct route to more torque at speed from the same motor size, so the spec gap is consistent with the power spec rather than a marketing artefact.

Notably the RS arm's [LeRobot](lerobot.md) config exposes a full **MIT impedance gain set per joint** — `mit_kp` 150/150/50/50/50/50 and `mit_kd` 10/10/10/5/4/4 across shoulder → wrist, plus separate `gripper_mit_kp 12.0 / kd 0.05 / torque_limit 8.0` — where the DM config in the same course shows no gripper-torque parameters. The RS path is the one the course actually exercises end to end.

## Integration notes

- Addressed by LeRobot as `seeed_b601_rs_follower` with `--robot.can_adapter=socketcan` on **`can0`** — i.e. a standard Linux SocketCAN interface (`ip link set can0 type can bitrate 1000000 restart-ms 100`), not a vendor USB protocol. This is the cleaner integration of the two.
- Motor CAN ID pairs observed in the course: `(1,253) … (7,253)` — a shared receive ID of 253, unlike Damiao's per-joint offset pairing.
- On [JetPack 7.2](jetson-linux.md), bringing up the USB-CAN adapter requires **out-of-tree `gs_usb.ko` / `peak_usb.ko` modules** that JetPack does not ship — see the [course page](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md).

## Open questions

- **No primary Robstride datasheet is ingested.** Torque, gear ratio, encoder resolution, and thermal limits for the 00 and 06 modules are unknown here; the specs above are all secondary, from Seeed's spec table.
- Whether "ROBSTRIDE 00" and "06" map to the vendor's RS00/RS06 product numbering is assumed, not verified.

## Related

- [Damiao](damiao.md) — the sibling CAN-actuator lineage; the other B601 variant
- [FeeTech](feetech.md) / [Dynamixel](dynamixel.md) — the serial-bus tiers below
- [reBot Arm B601](rebot-arm-b601.md) — the arm

## Mentioned in

- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — the RS spec table, MIT gain set, SocketCAN path
- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — The actuator line in the **B601-RS** variant (754 mm / 2.5 kg / <0.1 mm at 48 V), against [Damiao](damiao.md) in the DM.
