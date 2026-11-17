---
title: "Damiao DM-J8009P-2EC datasheet (v1.0)"
type: source
url: https://damiao.enactic.ai/en/products/hardware/dm-j8009p-2ec-v1.0
fetch_url: https://damiao.enactic.ai/pdf/products/dm-j8009p-2ec-v1.0-zh.pdf
local_path: raw/damiao-dm-j8009p-2ec-v1.0-datasheet-zh.pdf
sha256: 7f311fbafdaedffc70d4ca16c00e1ad8a7da07d433b2c572a9db0c72ba8738ea
author: "Shenzhen DAMIAO Technology Co., Ltd. (English translation by Enactic)"
published: 2024-08-26
ingested: 2026-11-16
format: vendor datasheet / user manual (Chinese original PDF + Enactic English translation)
license: "Translation site Apache-2.0; no license granted for the documentation itself"
tags: [damiao, dm-j8009p-2ec, actuator, datasheet, gear-ratio, mit-mode, can-bus, torque-control, primary]
---

# Damiao DM-J8009P-2EC datasheet (v1.0)

Damiao's own user manual for the **DM-J8009P-2EC** geared motor with integrated driver, in the Chinese original. [Enactic](../entities/enactic.md), maker of OpenArm, mirrors it at damiao.enactic.ai alongside an English translation (`raw/damiao-dm-j8009p-2ec-v1.0-datasheet-en.mdx`, [enactic/damiao](https://github.com/enactic/damiao) @ `42b460e`). The spec table below was checked against the Chinese PDF. The document is version V1.0, and its revision table gives 2024-08-26 as the first-version date.

## Summary

| Parameter | Value |
|---|---|
| **Reduction ratio** | **9:1** |
| Rated / peak torque | **20 / 40 N·m** |
| Rated / peak current | 20 / 50 A |
| Rated speed / no-load max | 100 rpm / 160 (24 V) / 320 (48 V) rpm |
| Rated voltage | 24 V (24–48 V) |
| Pole pairs; phase L / R | 21; 80 µH / 145 mΩ |
| Size; mass | Ø98 × 61.7 mm; ~930 g |
| Encoders | 2 × 14-bit magnetic, single-turn absolute output position |
| Interfaces | CAN 1 Mbit/s (standard frames) control; UART 921600 bps for parameter setup |
| Control modes | MIT, position-speed, speed |

**Is it QDD?** **Yes.** It is a large-diameter, low-ratio (9:1) motor, and the high-torque QDD option.

**Implied output torque constant:** about **1.0 N·m per amp** (rated torque ÷ rated current). This is my derivation, not a datasheet figure.

## Key claims

- **MIT mode**: one 8-byte CAN frame carries p_des (16 bit), v_des, Kp, Kd and t_ff (12 bit each). The driver turns these into a torque setpoint for its current loop. **Kp ∈ [0, 500], Kd ∈ [0, 5].** Kp = Kd = 0 with t_ff set gives pure torque output, which is the gravity-compensation case. *"When controlling the position, kd cannot be set to 0"*, otherwise the motor vibrates or runs away.
- **Feedback frame** (all modes): position (16-bit), velocity and **torque** (12-bit), plus MOSFET and coil temperatures. Values are linearly mapped over P_MAX / V_MAX / T_MAX ranges set in registers.
- **Protections**: driver over-temperature (120 °C), coil over-temperature (recommended ≤ 100 °C), over- and under-voltage, overcurrent, and a **communication-loss timeout** that drops the motor out of Enable mode. Arm-level watchdogs such as the reBot's 100 ms and YAM's 400 ms are configured on top of this.
- **This datasheet has no register appendix.** The register map (`KT_Value`, `TIMEOUT` 0x09, mode 0x0A, read-only `Gr` gear ratio 0x14, volatile writes with a separate store command, ~10,000 flash cycles) is documented only in the [DM-J4340P-2EC datasheet](damiao-dm-j4340p-2ec-datasheet.md), and presumably applies across the family.

## Where it is used in this wiki

The high-load joints of [OpenArm](../entities/openarm.md) ([docs](openarm-docs.md)).

## Entities mentioned

- [Damiao](../entities/damiao.md), [Enactic](../entities/enactic.md)

## Concepts touched

- [Gravity compensation](../concepts/robotics/gravity-compensation.md), [Impedance control](../concepts/robotics/impedance-control.md)

## Open questions

- **Backdrive torque and friction** are not specified; neither is gearbox backlash. Those are the parameters that decide hand-guiding feel.
- **Continuous vs intermittent rating**: the datasheet gives a rated and a peak value, but no duty cycle or thermal time constant for holding torque at stall.
