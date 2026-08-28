---
title: Kinova Jaco (assistive robotic arm)
type: entity
subtype: robot
created: 2026-07-09
updated: 2026-07-09
sources: 3
tags: [jaco, kinova, assistive-robotics, wheelchair, robotic-arm, medical-device]
---

**Jaco** — [Kinova](kinova.md)'s wheelchair-mounted assistive robotic arm (launched 2010, ~US$35,000): a six-segment carbon-fiber arm with 2- or 3-finger gripper, marketed as a **medical device** for people with upper-body functional limitations. The assistive-robotics field's longest-standing commercial manipulation product, and (in research-edition form) one of its standard academic platforms.

## Capabilities and specs

From the official user guide ([source page](../sources/kinova-jaco-assistive-arm.md), guide pp. 9–14):

- **Form factor:** 5.2–5.4 kg total, 90 cm reach, carbon-fiber links + aluminum actuators; mounts to the power wheelchair and runs off its 24 VDC supply (avg 25 W). Fits under the armrest without widening the chair.
- **Payload:** 1.6 kg continuous (inner half of reach), 1.3 kg temporary at full reach; gripper force 25 N (2-finger) / 40 N (3-finger); max end-effector speed 20 cm/s.
- **Control:** Cartesian — the user steers the *hand*, inverse kinematics is automatic. Four modes: translation, wrist, **drinking** (a task-specific wrist-rotation mode that offsets the reference point so a glass tips against the mouth without spilling), and finger. Input via Kinova joystick or a Universal Interface Control Box that piggybacks on the user's existing wheelchair drive controls — no computer in the loop during use.
- **Intended tasks** (guide p. 9): eating and drinking, personal hygiene, medication management, leisure, work, school, personal safety.

## Deployment model

Sold as a reimbursable medical device in markets with insurance codes (Germany, Netherlands); largely out-of-pocket in the US ([source page](../sources/kinova-jaco-assistive-arm.md)). Expected lifespan 5 years per the guide.

## In research

The Jaco lineage (Gen2 research edition, then Gen3) is standard academic assistive-manipulation hardware. In this wiki: [Nanavati et al. 2025](../sources/nanavati2025-feeding-out-of-lab.md) built their in-home **robot-assisted feeding** system on a Jaco Gen2 6-DOF with a custom force-torque-sensing fork (~$50k) — the only non-[Stretch](stretch.md) platform among the wiki's in-home deployment studies ([long-term in-home deployments](../syntheses/assistive/long-term-in-home-robot-deployments.md)), chosen because a single arm at face height fits feeding better than a mobile manipulator. Its three user-switchable operating modes are a case study in [levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md).

## Position in the platform landscape

The arm-only counterpoint to [Stretch](stretch.md): no mobility, so no fetch tasks, but face-height bimanual-adjacent manipulation from the chair the user already owns — and, unlike any research platform, an actual **reimbursement pathway**. The commercial drinking-mode firmware is a reminder that shipped assistive autonomy in 2010–2026 is *task-specific engineered behavior*, not learned policies ([Stretch platform comparison](../syntheses/assistive/stretch-as-assistive-platform.md)).

> [!note] Naming
> "Jaco" honors Jacques "Jaco" Forest, founder Charles Deguire's uncle, who had muscular dystrophy and built his own makeshift manipulation aid ([source page](../sources/kinova-jaco-assistive-arm.md)).

## Mentioned in

- [Kinova Jaco product page + user guide](../sources/kinova-jaco-assistive-arm.md)
- [Nanavati et al. 2025 — feeding out of the lab](../sources/nanavati2025-feeding-out-of-lab.md)
- [Stretch as the de-facto assistive platform](../syntheses/assistive/stretch-as-assistive-platform.md)
- [Long-term in-home robot deployments](../syntheses/assistive/long-term-in-home-robot-deployments.md)
- [Levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md)

## Open questions / TBD

- Regulatory classification per market (CE class, FDA status) — guide says "medical device" without classes.
- Whether the assistive configuration exposes any API for learned-policy research, or only the fixed control modes.
