---
title: "Design and clinical implementation of an open-source bionic leg (Azocar et al., Nature Biomedical Engineering 2020)"
type: source
url: https://www.nature.com/articles/s41551-020-00619-3
fetch_url: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7581510/fullTextXML
local_path: raw/azocar2020-open-source-bionic-leg-PMC7581510.xml
sha256: 4aa189f4c0c4fa4398bcc0429889172e9b61d2dfb44955e73de6f668d36dc651
author: "Alejandro F. Azocar, Luke M. Mooney, Jean-François Duval, Ann M. Simon, Levi J. Hargrove, Elliott J. Rouse (University of Michigan; Dephy; Shirley Ryan AbilityLab; Northwestern University)"
published: 2020-10-05
ingested: 2026-11-16
venue: "Nature Biomedical Engineering 4, 941 (2020); full text from Europe PMC (PMC7581510)"
format: paper (full-text XML)
tags: [prosthetics, bionic-leg, open-source-hardware, powered-prosthesis, series-elastic-actuator, belt-drive, low-gear-ratio, torque-control, impedance-control, raspberry-pi, shirley-ryan-abilitylab, rehabilitation-robotics]
---

# Design and clinical implementation of an open-source bionic leg

## Summary

The **Open-Source Leg (OSL)** is a powered knee-and-ankle prosthesis designed as shared research hardware. The authors' diagnosis is that control strategies for powered legs have each been tested on different custom hardware in constrained labs, so results cannot be compared and few groups can enter the field. The OSL is their answer: a leg anyone can order parts for and build, with open low-level control software, documented at opensourceleg.com. The paper characterizes it on the bench and reports walking, ramp and stair trials with three people with above-knee amputations, run in a rehabilitation hospital ([Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md)).

## Key claims

- **Actuation choice.** Brushless motors *"from the drone industry"*, chosen because their torque density allows low transmission ratios. That permits timing-belt drives in place of harmonic drives or roller screws, which the authors call more expensive and slow to source. They state the ratios are **2–5 times lower than comparable prostheses**; Table 1 lists 49 for the knee against 143 and 176 for other designs.
- **Series elasticity is optional and compact.** Up to six torsional spring disks, each about 100 N·m/rad, stack inside the knee's output pulley, giving a series elastic actuator with no added volume. The ankle has no explicit spring and relies on the foot's compliance.
- **Torque is estimated from motor current.** The authors note that torque sensors of sufficient capacity are large and heavy for a wearable device.
- **Bench performance** (Table 1, Fig. 3): position-control bandwidth 10.7–20.2 Hz and current-control bandwidth 86.8–107.4 Hz. Torque bandwidth was not measured and is expected to be much lower. Position bandwidth is described as about five times that of the biological joint.
- **Mass and cost.** Knee 2,160–2,330 g depending on spring configuration; ankle 1,740 g. **US$10,000–30,000** in prototype quantities, against up to US$100,000 for a commercial powered joint that does not allow control changes.
- **Electronics.** An open-source motor controller and embedded system with built-in position, current and impedance control, an IMU and an encoder, driven from a Raspberry Pi over USB in the recommended configuration.
- **Clinical test.** Three participants with transfemoral amputations, with prior experience of other powered legs, walked a circuit of level ground, ramps and stairs 15–20 times under an impedance-based controller: about 380 analysed steps each for walking and 38 each for ramps and stairs. Current tracking error was 0.5–2.9 A r.m.s. per step against peaks of 5–25 A.

## Analysis

- **The same actuator argument as this wiki's arm material.** High-torque-density motor, low gear ratio, torque inferred from current, optional series spring: this is the reasoning behind [torque-controllable arms](../syntheses/platforms/torque-controllable-arms.md) and [gravity compensation](../concepts/robotics/gravity-compensation.md), applied to a device that carries a person's weight. The paper is a worked example of the trade: low ratios give backdrivability and bandwidth, and cost torque that has to be made up by the motor.
- **Open hardware as a benchmark strategy.** The stated goal is comparability across labs, the same motive as the low-cost arm and benchmark efforts covered elsewhere here. It is a rare case of that strategy in medical robotics.
- **Evidence weight.** A design and characterization paper. Three participants show the leg can be walked on; they do not show clinical benefit, and the paper does not claim it.

## Entities mentioned

- [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md) — clinical testing site and home of two authors

## Concepts touched

- [Gravity compensation](../concepts/robotics/gravity-compensation.md) — current-based torque estimation at low gear ratio
- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- How many groups have built an OSL since 2020, and has it produced the cross-lab comparisons it was designed for?
- How accurate is current-based torque estimation here under load, given belt and bearing friction?
