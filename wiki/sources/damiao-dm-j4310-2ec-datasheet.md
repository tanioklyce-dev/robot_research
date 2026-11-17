---
title: "Damiao DM-J4310-2EC datasheet (v1.1)"
type: source
url: https://damiao.enactic.ai/en/products/hardware/dm-j4310-2ec-v1.1
fetch_url: https://damiao.enactic.ai/pdf/products/dm-j4310-2ec-v1.1-zh.pdf
local_path: raw/damiao-dm-j4310-2ec-v1.1-datasheet-zh.pdf
sha256: aad2c3ae95932393c87b4d149a4009c8e93af727df8d787472de807e2703d68e
author: "Shenzhen DAMIAO Technology Co., Ltd. (English translation by Enactic)"
published: 2023-11-16
ingested: 2026-11-16
format: vendor datasheet / user manual (Chinese original PDF + Enactic English translation)
license: "Translation site Apache-2.0; no license granted for the documentation itself"
tags: [damiao, dm-j4310-2ec, actuator, datasheet, gear-ratio, mit-mode, can-bus, torque-control, primary]
---

# Damiao DM-J4310-2EC datasheet (v1.1)

Damiao's own user manual for the **DM-J4310-2EC** geared motor with integrated driver, in the Chinese original. [Enactic](../entities/enactic.md), maker of OpenArm, mirrors it at damiao.enactic.ai alongside an English translation (`raw/damiao-dm-j4310-2ec-v1.1-datasheet-en.mdx`, [enactic/damiao](https://github.com/enactic/damiao) @ `42b460e`). The spec table below was checked against the Chinese PDF. The document is version V1.1, and its revision table gives 2023-11-16 as the first-version date.

## Summary

| Parameter | Value |
|---|---|
| **Reduction ratio** | **10:1** |
| Rated / peak torque | **3 / 7 N·m** |
| Rated / peak current | 2.5 / 7.5 A |
| Rated speed / no-load max | 120 rpm / 200 rpm |
| Rated voltage | 24 V |
| Pole pairs; phase L / R | 14; 340 µH / 650 mΩ |
| Size; mass | Ø56 × 46 mm; ~300 g |
| Encoders | 2 × 14-bit magnetic, single-turn absolute output position |
| Interfaces | CAN 1 Mbit/s (standard frames) control; UART 921600 bps for parameter setup |
| Control modes | MIT, position-speed, speed |

**Is it QDD?** **Yes — this is the QDD part.** At 10:1 it is the only low-ratio motor in the 40-series family.

**Implied output torque constant:** about **1.2 N·m per amp** (rated torque ÷ rated current). This is my derivation, not a datasheet figure.

## Key claims

- **MIT mode**: one 8-byte CAN frame carries p_des (16 bit), v_des, Kp, Kd and t_ff (12 bit each). The driver turns these into a torque setpoint for its current loop. **Kp ∈ [0, 500], Kd ∈ [0, 5].** Kp = Kd = 0 with t_ff set gives pure torque output, which is the gravity-compensation case. *"When controlling the position, kd cannot be set to 0"*, otherwise the motor vibrates or runs away.
- **Feedback frame** (all modes): position (16-bit), velocity and **torque** (12-bit), plus MOSFET and coil temperatures. Values are linearly mapped over P_MAX / V_MAX / T_MAX ranges set in registers.
- **Protections**: driver over-temperature (120 °C), coil over-temperature (recommended ≤ 100 °C), over- and under-voltage, overcurrent, and a **communication-loss timeout** that drops the motor out of Enable mode. Arm-level watchdogs such as the reBot's 100 ms and YAM's 400 ms are configured on top of this.
- **This datasheet has no register appendix.** The register map (`KT_Value`, `TIMEOUT` 0x09, mode 0x0A, read-only `Gr` gear ratio 0x14, volatile writes with a separate store command, ~10,000 flash cycles) is documented only in the [DM-J4340P-2EC datasheet](damiao-dm-j4340p-2ec-datasheet.md), and presumably applies across the family.

## Where it is used in this wiki

The wrist joints and gripper of the [reBot B601-DM](../entities/rebot-arm-b601.md) (×4), [YAM](../entities/yam.md) (×3), [OpenArm](../entities/openarm.md), and the [UME](../entities/ume.md) exoskeleton (×8).

## Entities mentioned

- [Damiao](../entities/damiao.md), [Enactic](../entities/enactic.md)

## Concepts touched

- [Gravity compensation](../concepts/robotics/gravity-compensation.md), [Impedance control](../concepts/robotics/impedance-control.md)

## Open questions

- **Backdrive torque and friction** are not specified; neither is gearbox backlash. Those are the parameters that decide hand-guiding feel.
- **Continuous vs intermittent rating**: the datasheet gives a rated and a peak value, but no duty cycle or thermal time constant for holding torque at stall.
