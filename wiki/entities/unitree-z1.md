---
title: Unitree Z1
type: entity
subtype: robot
created: 2026-09-11
updated: 2026-09-11
sources: 1
tags: [unitree-z1, unitree, robot-arm, manipulator, 6-dof, force-control, mobile-manipulation, china, affordable]
---

**Unitree Z1** — [Unitree](unitree.md)'s 6-DoF lightweight robotic arm (2022), sold as an on-board manipulator for its quadrupeds (AlienGo, B1) and as a standalone research arm. In this wiki it is the single- and dual-arm platform behind four of the five datasets [UnifoLM-WMA-0](../sources/unifolm-wma-0-project-page.md) was trained and demoed on, before Unitree's model work moved to the [G1](unitree-g1.md).

## Specs (vendor page, not ingested as a source)

From [unitree.com/z1](https://www.unitree.com/z1), two variants:

| | Z1 Air | Z1 Pro |
|---|---|---|
| DoF | 6 | 6 |
| Weight | 4.3 kg | 4.5 kg |
| Payload | 2 kg | ≥3 kg |
| Reach | 740 mm | 740 mm |
| Repeatability | ~0.1 mm | ~0.1 mm |
| Control | position + force; force feedback and collision detection | same |
| Interface / OS | Ethernet; Ubuntu | same |
| Power | 24 V, >20 A, max 500 W | same |

- **Joints:** harmonic-reducer actuators (405 g, Φ65×52 mm, 33 N·m peak, ~0.2 N·m force-control accuracy, 15-bit encoder, ~6 arcmin backlash, 1 kHz control, RS-485), commanded in torque / angle / velocity / stiffness / damping — the same impedance-style interface as Unitree's legged-robot motors. Joint ranges ±150°, 0–180°, −165–0°, ±80°, ±85°, ±160°, all at 180°/s.
- Vendor's own footnote: the low reduction ratios make whole-arm position stiffness low, so "if the control mode is not optimized, there will be large position control error and shaking."
- SDK: `unitreerobotics/z1_sdk` (2022); docs at support.unitree.com.

## In this wiki

- **[UnifoLM-WMA-0](../sources/unifolm-wma-0-project-page.md)** (Sep 2025): Unitree's five open training sets are Z1_StackBox, Z1_DualArm_StackBox (v1, v2), Z1_DualArm_Cleanup_Pencils and one G1 set, all LeRobot v2.1 with Dex1 grippers; three of the four real-robot demos are Z1 (single-arm stack box, dual-arm stack box, dual-arm pencil cleanup), each with the world model's predicted future video inset.
- Its successor generations, [UnifoLM-VLA-Base](unifolm.md) and [WLA-1.0](../sources/unifolm-wla-1-project-page.md), show only the G1 — the Z1 was Unitree's arm-only stepping stone.

## Position

Sits between hobby-tier arms ([SO-ARM101](so-arm101.md), Koch) and research arms ([Franka Panda](franka-panda.md)) — a 3 kg-payload, force-controlled, harmonic-drive arm at a Unitree price point, with the low-stiffness caveat above. The wiki has no ingested price or independent evaluation.

## Open questions

- Price and current availability (the vendor page lists Air and Pro without prices).
- Whether the Z1 datasets are included in WLA-1.0's ≈2,500 h.

## Mentioned in

- [UnifoLM-WMA-0 project page](../sources/unifolm-wma-0-project-page.md)
