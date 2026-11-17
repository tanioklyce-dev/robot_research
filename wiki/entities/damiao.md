---
title: Damiao (DM motors)
type: entity
subtype: organization
created: 2026-08-27
updated: 2026-11-16
sources: 9
tags: [damiao, actuators, quasi-direct-drive, planetary, datasheet, gear-ratio, can-bus, mit-mode, robot-arm, rebot-arm, motors]
---

**Damiao** (达妙 / DM) — Chinese manufacturer of **CAN-bus brushless joint actuators with integrated FOC drivers** for robotics. The range spans true **quasi-direct-drive** parts (DM-J4310 at 10:1, DM-J8009P at 9:1) and conventional **40:1 planetaries** (DM-J4340, DM-J4340P), so "Damiao" and "QDD" are not synonyms. In this wiki, Damiao is the motor lineage behind the **[reBot Arm B601-DM](rebot-arm-b601.md)**, [OpenArm](openarm.md), [YAM](yam.md) and the [UME](ume.md) exoskeleton.

## Datasheet specs (2026-11-16)

From Damiao's own manuals, mirrored by [Enactic](enactic.md):

| Motor | Ratio | QDD? | Rated / peak torque | Rated / peak current | Mass | Used in |
|---|---|---|---|---|---|---|
| [DM-J4310-2EC](../sources/damiao-dm-j4310-2ec-datasheet.md) | **10:1** | yes | 3 / 7 N·m | 2.5 / 7.5 A | ~300 g | reBot wrist + gripper, YAM, OpenArm, UME |
| [DM-J4340-2EC](../sources/damiao-dm-j4340-2ec-datasheet.md) | **40:1** | **no** | 9 / 27 N·m | 2.5 / 8 A | ~362 g | UME; probably the YAM/OpenArm "DM4340" |
| [DM-J4340P-2EC](../sources/damiao-dm-j4340p-2ec-datasheet.md) | **40:1** | **no** | 9 / 27 N·m | 2.5 / 8 A | ~375 g | reBot shoulder pan / lift + elbow |
| [DM-J8009P-2EC](../sources/damiao-dm-j8009p-2ec-datasheet.md) | **9:1** | yes | 20 / 40 N·m | 20 / 50 A | ~930 g | OpenArm high-load joints |

All four use CAN 1 Mbit/s (standard frames), two 14-bit magnetic encoders (absolute output position), a 24 V nominal supply (the 4340 family and the 8009P also accept 48 V), and the same MIT frame (Kp ∈ [0, 500], Kd ∈ [0, 5]). The "P" suffix marks a **crossed-roller output bearing**, not a different reduction.

**Mode register numbering** (0x0A, [J4340P datasheet](../sources/damiao-dm-j4340p-2ec-datasheet.md)): **1 = MIT, 2 = position-speed, 3 = speed, 4 = force-position hybrid** (position-speed with the current command clamped). So the LeRobot / DLI-course DM config (*"ensure mode 2"* for the arm joints, *"mode 4"* for the gripper) runs the arm in **position-speed cascade mode, not MIT**, and the gripper in current-limited hybrid mode. The NVIDIA Holoscan gravity-comp tutorial sends MIT-style frames, i.e. mode 1.

> [!note] Holding torque costs current, and low ratio costs more
> The implied output torque constant is about 1.2 N·m/A for the J4310 and 1.0 N·m/A for the J8009P, against about 3.6 N·m/A for the 40:1 J4340 (rated torque ÷ rated current; my derivation). Holding a pose against gravity, which is what gravity compensation does continuously, takes roughly 3–4× more current per N·m on the QDD parts. That is the engineering reason arms put 40:1 motors at the shoulder and elbow, and it is a heat budget gravity-comp code has to respect.

## Why it belongs in the motor ladder

The wiki tracks two low-cost motor lineages that [LeRobot](lerobot.md) integrates natively — [FeeTech](feetech.md) (hobby tier, STS3215 smart serial bus) and [Dynamixel](dynamixel.md) (education/research tier). **Damiao and [Robstride](robstride.md) are a third, structurally different tier**: planetary-geared brushless actuators (10:1 to 40:1 for Damiao) speaking **CAN at 1 Mbit/s** with an **MIT-style impedance interface** (position + velocity + `kp`/`kd` + feedforward torque per command), rather than a position-only serial servo protocol.

That difference is the reason a $1,499 arm can claim 0.2 mm repeatability and be a credible platform for contact-rich manipulation: MIT mode gives you torque-level control and (in principle) backdrivability, which position-only smart servos do not.

## Parts used in the reBot B601-DM

| Motor | Count | Role |
|---|---|---|
| **DM-J4340P-2EC** | 3 | High-torque, low-noise — the proximal joints (shoulder pan / lift / elbow). **40:1, not QDD** ([datasheet](../sources/damiao-dm-j4340p-2ec-datasheet.md)) |
| **DM-J4310-2EC** | 4 | Wrist flex / yaw / roll + gripper. **10:1, QDD** ([datasheet](../sources/damiao-dm-j4310-2ec-datasheet.md)) |

Arm bus: DC 24 V 10 A, CAN at 1 Mbit/s, seven nodes ([product page](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md)).

## Tooling and integration notes

- **Motor IDs are set from a Windows-only GUI**, `DM_Tools_v1.8.0.1.exe`, over a **USB-CAN adapter board** plus an XT30 (2+2) signal-power separation board. The [DLI course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) requires a dual-boot machine for this step alone — Linux for everything else, Windows for the motor tool.
- LeRobot addresses the DM arm as `seeed_b601_dm_follower` with `--robot.can_adapter=damiao` on `/dev/ttyACM0` at 921600 baud, i.e. through Damiao's own USB-CAN protocol rather than SocketCAN. (The Robstride variant uses SocketCAN `can0` instead.)
- Observed motor CAN ID pairs from the course calibration log: `(1,17) (2,18) (3,19) (4,20) (5,21) (6,22) (7,23)` — a send/receive ID pair per joint, offset by 16.
- Damiao operating modes appear as `ensure mode 2` for the arm joints and `mode 4` for the gripper in the DM path (vs `mode 1` throughout on Robstride). The two vendors do not share a mode numbering. **On Damiao, 2 = position-speed and 4 = force-position hybrid**, so this path is not MIT/impedance mode (see the datasheet table above).

## Open questions

- **Backdrivability is demonstrated but unmeasured.** The [Holoscan 5 tutorial](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) runs DM motors in MIT mode (position, velocity, kp, kd and feedforward torque) for hand-guided gravity compensation on the reBot B601-DM. No source gives backdrive torque or friction.
- ~~**No torque, gear-ratio, or thermal specs**~~ — **resolved 2026-11-16** by the four datasheets above. Still missing: backlash, friction or backdrive torque, and a continuous-stall thermal rating.

## Related

- [Robstride](robstride.md) — the sibling CAN-actuator lineage; the other B601 variant
- [FeeTech](feetech.md) / [Dynamixel](dynamixel.md) — the two serial-bus tiers below
- [reBot Arm B601](rebot-arm-b601.md) — the arm
- [Gravity compensation](../concepts/robotics/gravity-compensation.md) — what MIT mode makes possible at this price (QDD at the wrist, 40:1 at the shoulder)
- [Torque-controllable arms](../syntheses/platforms/torque-controllable-arms.md) — motor-type comparison for gravity compensation

## Mentioned in

- [DM-J4310-2EC](../sources/damiao-dm-j4310-2ec-datasheet.md), [DM-J4340-2EC](../sources/damiao-dm-j4340-2ec-datasheet.md), [DM-J4340P-2EC](../sources/damiao-dm-j4340p-2ec-datasheet.md), [DM-J8009P-2EC](../sources/damiao-dm-j8009p-2ec-datasheet.md) datasheets — **primaries**: gear ratios, torque and current ratings, the MIT frame, the mode register.
- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — the DM part numbers and bus spec
- [Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](../sources/nvidia-holoscan-5-rebot-gravity-compensation.md) — DM motors in MIT-mode torque control via Seeed's `motorbridge`
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — motor-ID setup, LeRobot `damiao` adapter, CAN ID pairs
- [OpenArm documentation](../sources/openarm-docs.md) — the second Damiao-based arm here after the reBot Arm: DM-J4310-2EC / DM4340 / DM-J8009P-2EC per joint (3–20 Nm rated, 7–40 Nm peak), CAN-FD; datasheets hosted by [Enactic](enactic.md) at damiao.enactic.ai.
