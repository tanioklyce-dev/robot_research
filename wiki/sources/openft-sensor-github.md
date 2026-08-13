---
title: openFT-sensor GitHub repository (dimensionalOS/openFT-sensor)
type: source
url: https://github.com/dimensionalOS/openFT-sensor
author: Dimensional Inc.
published: 2025-12-10 (repo created and last pushed the same day)
ingested: 2026-08-13
license: none declared
tags: [openft, force-torque, hall-effect, open-hardware, sensing, dimensional, dimos, low-cost, tactile]
---

## Summary

**OpenFT** is an open-source **6-axis force/torque sensor** built on **Hall-effect magnetic-field displacement sensing** rather than the strain gauges used in commercial F/T sensors. **16 Hall sensors in 4 clusters** read the displacement of a magnet holder under load; force and torque are recovered either geometrically or through a learned calibration matrix. From [Dimensional Inc.](../entities/dimensional-inc.md), the same org as [DimOS](../entities/dimos.md), where it is listed 🟥 experimental in the hardware matrix.

Ingested because of a pattern this wiki keeps hitting: **the affordable-robot tier records position only**. [Sourccey](../entities/sourccey.md) logs "positional only (observation and commanded position)"; [XLeRobot](../entities/xlerobot.md) and the [SO-ARM101](../entities/so-arm101.md) class have no force sensing beyond servo current; [DimOS](../entities/dimos.md)'s own `dimos dataprep` exports `color_image` + `coordinator_joint_state`. Every contact-rich manipulation result in the wiki comes from hardware that costs an order of magnitude more. A DIY F/T sensor is the cheapest plausible route out of that, which makes this repository interesting well out of proportion to its 2 stars.

## Key claims

- **Sensing principle** — Hall-effect magnetic field displacement. A magnet moves relative to a sensor array as the structure deflects under load; 16 Hall readings across 4 clusters are inverted to 6 axes.
- **Two recovery paths, honestly compared in the README:**

  | | Geometric | Calibrated matrix |
  |---|---|---|
  | Method | sensor geometry + coordinate transforms | learned **6×16 matrix** via least-squares on calibration data |
  | Calibration rig | none | load cell or reference F/T sensor required |
  | Accuracy | *"less accurate, assumes ideal geometry"* | *"much higher… compensates for real-world effects, accounts for cross-coupling"* |
  | Intended use | testing, relative measurements | production, absolute measurements |

- **Fully specified hardware**: Gerber files (or a pre-packaged zip) for PCB fabrication, an **`.xlsx` BOM formatted for JLCPCB automated assembly**, and a STEP file for the 3D-printed magnet holder. Connects over USB/serial.
- **Software**: `ft_driver.py` (geometric), `ft_min_driver.py` (raw), `ft_vis.py` (Dash/Plotly dashboard on `localhost:8050`), and `calc_calibration_matrix.py` plus a `CALIBRATION_GUIDE.md`. Python 3.7+, pyserial, zmq, numpy, pandas, dash, plotly. Default port `/dev/ttyACM0` at 115200 baud; **first 3 seconds unloaded to zero-bias**.

## Analysis

> [!warning] It is more completely published than most "open hardware" in this wiki, and less maintained
> Gerbers + a JLCPCB-ready BOM + STEP + driver + calibration guide is a **genuinely reproducible** package — more than [Sourccey](sourccey-hardware-repo.md) ships (115 STEP files, no BOM, no wiring, no URDF), and roughly what [LeKiwi](lekiwi-github.md) and [SO-ARM101](../entities/so-arm101.md) ship. But it is **2 stars, 0 forks, created and last pushed on the same day (2025-12-10)**, with no commits since. Treat it as a **published design, not a maintained project** — read it as a reference implementation you would fork and own, not as a dependency.

> [!warning] No LICENSE file
> The README says "open-source"; the repository declares **no license**, which under default copyright means no grant of rights at all. This matters more for hardware people intend to sell than for a bench build, but it is the same class of gap as [Sourccey](sourccey-hardware-repo.md)'s missing STLs: the *claim* of openness outrunning the *artifact*. One file fixes it.

> [!note] Why Hall-effect instead of strain gauges
> Strain-gauge F/T sensors need precision machining, careful bonding, temperature compensation, and low-noise instrumentation amplifiers — the reason commercial 6-axis units start around $2–5k. Hall-effect displacement sensing trades that for a PCB, some magnets, and a 3D print, moving the difficulty from analog electronics into **calibration** — which is exactly where the README puts it, with two explicitly different accuracy tiers depending on whether you own a reference load cell. The honest framing of that trade is the best thing in the documentation.
>
> The catch it does not discuss: Hall sensors are **temperature-sensitive and susceptible to nearby ferrous material and stray magnetic fields** — and a robot wrist is full of servo motors, which are magnets. Whether the 4-cluster arrangement rejects motor field is the first question anyone building this should answer, and the repository does not.

> [!note] What this would unlock if it worked
> Every contact-rich finding in this wiki — compliance, insertion, force-modulated grasping, [π*0.6](../entities/pistar06.md)-style recovery from slip — sits on hardware with force sensing. The affordable tier's datasets are kinematics-only, which caps what policies trained on them can learn: [Sourccey](../entities/sourccey.md) can plausibly fold laundry (kinematically dominated) and cannot plausibly learn to open a stiff drawer. A working sub-$100 wrist F/T sensor would change what the [LeRobot](../entities/lerobot.md)-tier community can *record*, which is upstream of what it can train. Unverified, unbenchmarked, and worth someone's weekend.

## Entities mentioned

- [OpenFT sensor](../entities/openft-sensor.md) · [Dimensional Inc.](../entities/dimensional-inc.md) · [DimOS](../entities/dimos.md)
- [Sourccey](../entities/sourccey.md), [XLeRobot](../entities/xlerobot.md), [SO-ARM101](../entities/so-arm101.md) — the position-only platforms this addresses

## Concepts touched

- [End-user robot programming](../concepts/robotics/end-user-robot-programming.md) · [Imitation learning](../concepts/learning/imitation-learning.md)

## Open questions

- **No specifications published**: range, resolution, noise floor, bandwidth, hysteresis, temperature drift, or cost. Without a range and a noise floor this cannot be compared to anything, and none of it appears in the repository.
- **Magnetic interference from servos** — unaddressed, and the single biggest risk for a wrist-mounted application.
- **Has it ever been mounted on a robot?** [DimOS](../entities/dimos.md) lists it 🟥 experimental in the hardware matrix; no integration code, blueprint, or `In[Wrench]` stream is documented.
- **What does calibration actually require?** "A load cell or reference sensor" is the barrier that decides whether this is a $60 project or a $2,000 one.
