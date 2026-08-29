---
title: "Kinova Jaco assistive robotic arm (product page + user guide)"
type: source
url: https://assistive.kinovarobotics.com/product/jaco-robotic-arm
author: Kinova inc.
published: ~2021 (user guide R05; product line launched 2010)
ingested: 2026-07-09
format: product page + official user-guide PDF (53 pp)
local_path: raw/kinova-jaco-user-guide-r05.pdf
sha256: f6fd605ce7d82f0f32a150b94d03ad39a19b3c16eaa6294a938957b95bde1c67
tags: [kinova, jaco, assistive-robotics, wheelchair, robotic-arm, medical-device, commercial-product]
---

> [!note] Ingest depth
> The product page itself is a JavaScript SPA that serves no static content, so the substantive ingest is the **official Jaco user guide R05** (PDF, 53 pp, © 2021 Kinova), downloaded from the same domain into `raw/kinova-jaco-user-guide-r05.pdf`, supplemented by press coverage for company history and pricing ([IEEE Spectrum startup profile](https://spectrum.ieee.org/startup-spotlight-kinova), [Radio Canada Intl 2016](https://www.rcinet.ca/en/2016/08/11/kinova-robotics-jaco-robotic-arms/), [Wikipedia: Kinova](https://en.wikipedia.org/wiki/Kinova)).

## Summary

The **Jaco** is [Kinova](../entities/kinova.md)'s commercial wheelchair-mounted assistive robotic arm — per its own user guide, "a medical device intended to be used on wheelchairs for people with functional limitations or upper body disabilities," supporting eating and drinking, personal hygiene, medication management, leisure, work, school, and personal safety (guide p. 9). It is a six-segment, carbon-fiber arm with a 2- or 3-finger gripper, controlled *in Cartesian space* (the user steers the hand; joint motions are solved automatically) through the wheelchair's own drive controls or a Kinova joystick. Launched in 2010 and priced around **US$35,000**, it is the assistive-robotics field's longest-standing commercial manipulation product — and the arm behind the wiki's ingested [in-home robot feeding work](nanavati2025-feeding-out-of-lab.md) (research edition).

## Key claims

**Specifications (user guide pp. 10–11, Table 1):**

- Total weight **5.2 kg** (2-finger gripper) / **5.4 kg** (3-finger); reach **90 cm**; materials: carbon-fiber links, aluminum actuators.
- Payload: **1.6 kg continuous** at minimum-to-mid reach (≤45 cm from actuator #2), **1.3 kg temporary** at mid-to-full reach (p. 13, "Normal use definition"). Sustained holds near max reach/load cause actuator heating; the joystick blinks red as an overheat warning (p. 14).
- Max linear end-effector speed **20 cm/s**; joint range ±27.7 turns (software-limited); **24 VDC** (runs off the wheelchair's power); average power **25 W** (5 W standby), peak 100 W; gripper force 25 N (2-finger) / 40 N (3-finger); IPX2 water resistance; stated expected lifespan **5 years**.

**Control model (guide pp. 11–12):**

- Control is **Cartesian, not joint-space** — "the user only controls movements of the robot hand. The different joints are piloted automatically." Four user-facing modes: **translation** (hand position, kept parallel to the wheelchair seat frame), **wrist** (orientation about a fixed hand-center reference point), **drinking** (wrist rotation with the reference point offset to tip a glass against the user's mouth without spilling — a task-specific mode baked into the firmware), and **finger** (grip open/close).
- Input hardware: Kinova joystick or a **Universal Interface Control Box** that connects to the user's existing wheelchair drive controls (8-pin port, guide p. 10); accessories include an OLED status display and a powered lift arm with swing-away mechanism (guide pp. 24–45). USB is for configuration/maintenance only — day-to-day use requires no computer.

**Product/company context (press + Wikipedia):**

- Kinova was founded **2006** in Boisbriand, Quebec by **Charles Deguire** and Louis-Joseph Caron L'Écuyer. The arm is named for Deguire's uncle **Jacques "Jaco" Forest**, who lived with muscular dystrophy and built himself a makeshift mechanical arm; three of Deguire's uncles had the disease ([IEEE Spectrum](https://spectrum.ieee.org/startup-spotlight-kinova)).
- First wheelchair-mountable version ~2009; commercial launch **2010** ([Wikipedia](https://en.wikipedia.org/wiki/Kinova)). Price ~**US$35,000**; Kinova concentrates on markets with **insurance reimbursement codes** — notably Germany and the Netherlands (the first customer was Dutch) — while in the US the arm is largely an out-of-pocket purchase ([Digital Trends](https://www.digitaltrends.com/cool-tech/kinova-robotics-wheelchair-robot-arm/), [RCI 2016](https://www.rcinet.ca/en/2016/08/11/kinova-robotics-jaco-robotic-arms/)).
- Kinova also sells the Jaco lineage as **research manipulators** (Gen2, then the Gen3 line) — the form in which it appears throughout academic assistive robotics, including the wiki's [Nanavati 2025 feeding system](nanavati2025-feeding-out-of-lab.md) (~$50k research configuration).

## Entities mentioned

- **[Kinova](../entities/kinova.md)** — manufacturer.
- **[Kinova Jaco](../entities/kinova-jaco.md)** — the arm itself.

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — Jaco is the field's longest-standing commercial manipulation product; arm-only counterpart to [Stretch](../entities/stretch.md)'s mobile-manipulator approach.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — Jaco is positioned as a **medical device** (its guide's own framing), i.e. the medical-device regulatory pathway rather than the ISO 13482 personal-care-robot pathway; a live example of the certification-route question that page discusses.

## Open questions

- Exact regulatory classification per market (CE class, FDA status) — the user guide asserts "medical device" but doesn't state classes; worth verifying if the wiki's safety-standards thread needs it.
- Current (2026) pricing and reimbursement map — the $35k figure and Germany/Netherlands coverage reporting date from ~2016–2019.
- Sales volume / installed base — no public numbers found in this pass.
- How the assistive Jaco (4 fixed control modes, no API in normal use) relates firmware-wise to the research Gen2/Gen3 line (full API) — relevant if a project ever wants to run learned policies on the assistive configuration.
