---
title: "RK3566 Edge AI Robot: Microduck Robotics Control Case Study (KickPi)"
type: source
url: https://www.kickpi.com/rk3566-edge-ai-robot-microduck-case-study/
author: KickPi (byline Winnie Wang)
published: 2026-09-04
ingested: 2026-09-13
local_path: raw/2026-09-04-kickpi-rk3566-microduck-case-study.html
sha256: fcc1ee978eaad408ff0b200c3d28a9bcbbf5bfbb95c3f779ca128759b5c1a63a
tags: [kickpi, microduck, rk3566, rockchip, odm, secondary-source, edge-ai, control-loop, case-study, marketing]
format: ODM blog "case study" (~1,000 words), written from Microduck's public documentation
---

# RK3566 Edge AI Robot: Microduck Robotics Control Case Study (KickPi)

## Summary

A Rockchip-board ODM's marketing piece that reads [Microduck](../entities/microduck.md)'s public docs ("according to the project information … the analyzed project") and re-presents them as a case for KickPi's RK3566/RK3568 custom-mainboard business. Everything substantive in it is already in the wiki from the [Pollen primaries](pollen-robotics-microduck.md) and the [runtime repo](microduck-runtime-repo.md): 25 cm / 800 g, RK3566, **15 servos on a 50 Hz loop**, MuJoCo + PPO → ONNX, a multi-daemon Linux runtime with OTA. Its framing — *"AI performance is not the only metric. Stable and predictable control-loop execution is equally important"* and *"hardware design should focus on the complete control loop"* — is sound and matches the wiki's [control-rate](../syntheses/platforms/control-rate-ladder.md) reading of Microduck. Ingested for two reasons: it adds one hardware detail the wiki had not recorded (the IMU named as an **LSM6DSV16X presented as a Dynamixel bus device**, unverified here), and it is a clean specimen of how a secondary compresses a primary — it **invents a "servo daemon" that does not exist** (the runtime's central design point is that *one* process owns the motors), omits every measured number (the 0.8 TOPS NPU, the 25.7 ms detector, the 1 GB RAM), and lets its own 2 / 4 GB ODM offerings sit next to the robot's 1 GB.

## Claims, checked against the primaries

| KickPi says | Primary says | Verdict |
|---|---|---|
| ~25 cm, ~800 g, RK3566 main controller | 25 cm, <800 g, RK3566, 1 GB RAM ([press kit](pollen-robotics-microduck.md)) | ✓ (RAM omitted) |
| 15 servos, 50 Hz control loop, ~20 ms per cycle | 15 motors, 14 policy-driven + beak; 50 Hz tick, `MissedTickBehavior::Skip` ([runtime](microduck-runtime-repo.md)) | ✓ |
| "MuJoCo simulation → PPO → ONNX → RK3566" | [mjlab](../entities/mjlab.md) (MuJoCo Warp) + `rsl_rl` PPO, ~1–2 h at 4,096 envs; ONNX `obs[1,61] → actions[1,14]` | ✓ (tooling simplified) |
| Policy inputs: IMU, joint position, joint velocity, target motion | `gyro(3) + projected_gravity(3) + joint_pos(14) + joint_vel(14) + last_action(14) + command(13)` | ✓ (last-action omitted) |
| IMU integrated with the Dynamixel servo bus; part **LSM6DSV16X** | one `sync_read` covers "IMU board + 15 servos, registers 124–136" — so the bus integration is confirmed; **the part number appears in none of the four design docs checked** | bus ✓, part **unverified** |
| Runtime services: "control daemon, servo daemon, camera daemon, wireless services, update daemon" | **seven** daemons — `robotd` (the *only* motor writer), `configd`, `updaterd`, `btd`, `padd`, `mediad`, `tofd` | ✗ — **no separate servo daemon**; the paraphrase contradicts the design's safety argument |
| OTA "update mechanisms and deployment processes" | signed whole-directory release swaps, **health-gated with automatic rollback**, boot counter | ✓ (the interesting part omitted) |
| "AI acceleration capabilities" | NPU measured at **0.8 TOPS INT8, one core**; `yolo11n`@320 p50 25.7 ms; the policy is a ~794 KB ONNX MLP | vague; no number survives |
| ODM board options "2GB/4GB RAM, eMMC, RS485/CAN…" | Microduck: 1 GB / 32 GB | KickPi's catalogue, not the robot |

Not mentioned at all: the actuator-fidelity sim-to-real thesis, the fall-prediction detector, the borrow-checker safety boundary, the 8×8 ToF, BLE multi-robot substrate, the $399 price, Pollen or Hugging Face by name beyond a link to `microduck.net`.

## Why it is worth one page

- **Secondary-source specimen.** Same pattern as the [explainx Gemma 4 piece](explainx-gemma-4-open-duck-mini.md) and the [Geniatech comparison](geniatech-rk1828-vs-orin-nx-vs-hailo-8.md): the noun phrases survive, the numbers and the argument do not, and one structural fact gets inverted. The "servo daemon" error is instructive because the primary spends a whole design doc on why there must *not* be one.
- **Cross-source note on the RK3566's ceiling.** KickPi pitches the RK3566 as an edge-AI robot SoC. The wiki can now bound that: it is not in [rknn-llm](rknn-llm-github.md)'s platform list (RK3588 / 3576 / 3562 / RV1126B), so no on-device LLM path exists for it through Rockchip's SDK, and its NPU is one core at 0.8 TOPS. It is exactly what Microduck uses it for — a proprioceptive-MLP controller with a small detector — and nothing above that.

## Entities mentioned
- [Microduck](../entities/microduck.md) · [Pollen Robotics](../entities/pollen-robotics.md) (implicit) · [Rockchip](../entities/rockchip.md) · [KickPi](../entities/kickpi.md) (new) · [Dynamixel](../entities/dynamixel.md)

## Concepts touched
- [Onboard robot service architecture](../concepts/robotics/onboard-robot-service-architecture.md) — the daemon split it misdescribes.
- [Heterogeneous edge SoCs and the shared-memory budget](../concepts/robotics/heterogeneous-edge-soc.md) — the RK3566 as the bottom rung.

## Open questions
- Is the IMU actually an ST **LSM6DSV16X**, and is it a Dynamixel-protocol device on the bus or bridged by the IMU board's MCU? Check the `microduck` repo's hardware or `robotd` docs beyond the four checked.
