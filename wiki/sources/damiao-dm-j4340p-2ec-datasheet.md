---
title: "Damiao DM-J4340P-2EC datasheet (v1.0)"
type: source
url: https://damiao.enactic.ai/en/products/hardware/dm-j4340p-2ec-v1.0
fetch_url: https://damiao.enactic.ai/pdf/products/dm-j4340p-2ec-v1.0-zh.pdf
local_path: raw/damiao-dm-j4340p-2ec-v1.0-datasheet-zh.pdf
sha256: 594c43eb091835d1cb8b9c9e8cd878fffbd5c3633e4a136602ce5c74e665016c
author: "Shenzhen DAMIAO Technology Co., Ltd. (English translation by Enactic)"
published: 2023-11-16
ingested: 2026-11-16
format: vendor datasheet / user manual (Chinese original PDF + Enactic English translation)
license: "Translation site Apache-2.0; no license granted for the documentation itself"
tags: [damiao, dm-j4340p-2ec, actuator, datasheet, gear-ratio, mit-mode, can-bus, torque-control, primary]
---

# Damiao DM-J4340P-2EC datasheet (v1.0)

Damiao's own user manual for the **DM-J4340P-2EC** geared motor with integrated driver, in the Chinese original. [Enactic](../entities/enactic.md), maker of OpenArm, mirrors it at damiao.enactic.ai alongside an English translation (`raw/damiao-dm-j4340p-2ec-v1.0-datasheet-en.mdx`, [enactic/damiao](https://github.com/enactic/damiao) @ `42b460e`). The spec table below was checked against the Chinese PDF. The document is version V1.0, and its revision table gives 2023-11-16 as the first-version date.

## Summary

| Parameter | Value |
|---|---|
| **Reduction ratio** | **40:1** |
| Rated / peak torque | **9 / 27 N·m** |
| Rated / peak current | 2.5 / 8 A |
| Rated speed / no-load max | 36 rpm / 52 (24 V) / 100 (48 V) rpm |
| Rated voltage | 24 V or 48 V |
| Pole pairs; phase L / R | 14; 360 µH / 880 mΩ |
| Size; mass | Ø57 × 56.5 mm; ~375 g |
| Encoders | 2 × 14-bit magnetic, single-turn absolute output position |
| Interfaces | CAN 1 Mbit/s (standard frames) control; UART 921600 bps for parameter setup |
| Control modes | MIT, position-speed, speed, **force-position hybrid** |

**Is it QDD?** **No.** It has the same 40:1 reduction as the J4340. The "P" variant adds a **crossed-roller output bearing** (better moment stiffness), a slightly different winding (360 µH / 880 mΩ vs 317 µH / 760 mΩ), and a force-position hybrid mode, which is position-speed control with the current command clamped.

**Implied output torque constant:** about **3.6 N·m per amp** (rated torque ÷ rated current). This is my derivation, not a datasheet figure. The driver also exposes a writable `KT_Value` register.

## Key claims

- **MIT mode**: one 8-byte CAN frame carries p_des (16 bit), v_des, Kp, Kd and t_ff (12 bit each). The driver turns these into a torque setpoint for its current loop. **Kp ∈ [0, 500], Kd ∈ [0, 5].** Kp = Kd = 0 with t_ff set gives pure torque output, which is the gravity-compensation case. *"When controlling the position, kd cannot be set to 0"*, otherwise the motor vibrates or runs away.
- **Feedback frame** (all modes): position (16-bit), velocity and **torque** (12-bit), plus MOSFET and coil temperatures. Values are linearly mapped over P_MAX / V_MAX / T_MAX ranges set in registers.
- **Protections**: driver over-temperature (120 °C), coil over-temperature (recommended ≤ 100 °C), over- and under-voltage, overcurrent, and a **communication-loss timeout** (register `TIMEOUT`, 0x09) that drops the motor out of Enable mode. Arm-level watchdogs such as the reBot's 100 ms and YAM's 400 ms are configured on top of this.
- Parameters written over CAN take effect immediately but are **volatile** until a separate store command. Flash endurance is about 10,000 cycles, so don't store frequently. Mode is register 0x0A, and switching modes clears the command values.
- Registers expose the gear ratio (`Gr`, 0x14, read-only), rotor inertia, phase R/L and pole pairs, so a controller can read the reduction from the motor rather than hard-coding it.

## Where it is used in this wiki

The three proximal joints (shoulder pan, shoulder lift, elbow) of the [reBot B601-DM](../entities/rebot-arm-b601.md) ([product page](seeed-rebot-arm-b601-dm-thor-bundle.md)).

## Entities mentioned

- [Damiao](../entities/damiao.md), [Enactic](../entities/enactic.md)

## Concepts touched

- [Gravity compensation](../concepts/robotics/gravity-compensation.md), [Impedance control](../concepts/robotics/impedance-control.md)

## Open questions

- **Backdrive torque and friction** are not specified; neither is gearbox backlash. Those are the parameters that decide hand-guiding feel.
- **Continuous vs intermittent rating**: the datasheet gives a rated and a peak value, but no duty cycle or thermal time constant for holding torque at stall.
