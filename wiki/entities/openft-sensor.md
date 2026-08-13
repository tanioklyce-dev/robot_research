---
title: OpenFT sensor
type: entity
subtype: hardware-component
created: 2026-08-13
updated: 2026-08-13
tags: [openft, force-torque, hall-effect, open-hardware, sensing, dimensional, dimos, low-cost, jlcpcb]
sources: 1
---

**OpenFT** — an open-source **6-axis force/torque sensor** using **Hall-effect magnetic-displacement sensing** instead of strain gauges: **16 Hall sensors in 4 clusters** track a magnet holder's deflection under load, inverted to 6 axes either geometrically or through a learned **6×16 calibration matrix**. From [Dimensional Inc.](dimensional-inc.md); listed 🟥 experimental in [DimOS](dimos.md)'s hardware matrix. Repo: [github.com/dimensionalOS/openFT-sensor](https://github.com/dimensionalOS/openFT-sensor) ([source page](../sources/openft-sensor-github.md)).

## Why it matters in this wiki

It addresses the wiki's most persistent hardware gap: **the affordable-robot tier records position only.**

| Platform | Force sensing | What its datasets contain |
|---|---|---|
| [Sourccey](sourccey.md) | none (servo current for limits only) | "positional only (observation and commanded position)" |
| [XLeRobot](xlerobot.md) / [SO-ARM101](so-arm101.md) | none | joint position |
| [DimOS](dimos.md) `dataprep` | none | `color_image` + `coordinator_joint_state` |
| [Stretch](stretch.md), [Franka](franka-panda.md), [Yuri](yuri.md) | yes | force/torque available |

Every contact-rich result in this wiki — compliance, insertion, force-modulated grasping, [π*0.6](pistar06.md)-style slip recovery — comes from the bottom row. The cap is not the policy, it is what the cheap platforms can *record*: a kinematics-only dataset caps what a policy trained on it can learn. Sourccey can plausibly learn to fold laundry (kinematically dominated) and cannot plausibly learn to open a stiff drawer.

A working sub-$100 wrist F/T sensor would change what the [LeRobot](lerobot.md)-tier community can record, which is upstream of what it can train. That is why a 2-star repository gets a page.

## Design

- **Principle** — Hall-effect magnetic field displacement. Moves the engineering difficulty out of analog instrumentation (the reason commercial 6-axis units start around $2–5k) and into **calibration**.
- **Two accuracy tiers, explicitly documented**: geometric (no calibration rig, *"assumes ideal geometry,"* fine for relative measurement) vs **calibrated matrix** (least-squares fit against a load cell or reference sensor; *"accounts for cross-coupling"*).
- **Published artifacts**: Gerbers, a **JLCPCB-ready `.xlsx` BOM** for automated assembly, a STEP file for the printed magnet holder, Python drivers, a Dash/Plotly live dashboard, and a calibration guide. USB/serial, 115200 baud, 3-second unloaded zero-bias at startup.

## Caveats

> [!warning] Published, not maintained — and unlicensed
> **2 stars, 0 forks, created and last pushed the same day (2025-12-10)**, no commits since. And despite the README saying "open-source," the repository declares **no license**, which under default copyright grants nothing. Fork-and-own it; don't depend on it.

> [!warning] No specifications at all
> Range, resolution, noise floor, bandwidth, hysteresis, temperature drift, and cost are **all absent**. Without a range and a noise floor it cannot be compared to any commercial part. And the unaddressed risk specific to this sensing principle: **Hall sensors respond to stray magnetic fields and temperature, and a robot wrist is full of servo motors.** Whether the 4-cluster arrangement rejects motor field is the first thing a builder must determine, and the repo is silent on it.

## Related

- [Dimensional Inc.](dimensional-inc.md) / [DimOS](dimos.md) — origin; lists it experimental
- [FeeTech](feetech.md) — the servo lineage whose current-sensing is the current substitute for real force sensing in this tier
- [Sourccey](sourccey.md), [XLeRobot](xlerobot.md), [SO-ARM101](so-arm101.md) — the position-only platforms it would serve

## Mentioned in

- [openFT-sensor GitHub repository](../sources/openft-sensor-github.md)
