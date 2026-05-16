---
title: Tiago
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-05-10
sources: 1
tags: [tiago, pal-robotics, mobile-manipulator, ros, research-platform]
---

**Tiago** — research-grade **mobile manipulator** from [PAL Robotics](https://pal-robotics.com/robot/tiago/) (Barcelona, Spain). Wheeled differential-drive base + extendable torso + one or two 7-DOF arms + RGB-D head sensor. ROS-native. A common European-academic-lab counterpart to the [Stretch](stretch.md) and [Franka Panda](franka-panda.md) platforms.

## In this wiki
Tiago appears in:
- **[Designing Accessible Robot Communication for Blind People (Huh et al. 2026)](../sources/huh2026-accessible-robot-comm.md)** — used as the mobile-manipulator platform in the in-person observational study, paired with a tabletop [Franka Panda](franka-panda.md). Tasks: fetch salt, pour pasta. Chosen for its dual-arm mobile form factor that contrasts with the tabletop Panda.

## Why it matters in this wiki
Tiago is one of the few standard research platforms suited to **room-scale mobile manipulation** in academic settings. Its inclusion in Huh et al. 2026 documents how its sound/motion profile and field-of-view (the robot moving away from the user mid-task) shape the **monitoring problem for blind users** — different from a tabletop arm in ways relevant to accessible-communication design.

## Related
- [Franka Panda](franka-panda.md) — companion tabletop platform in Huh et al. 2026
- [Stretch](stretch.md) — closest research-platform counterpart in US labs
- [Accessible robot communication](../concepts/robotics/accessible-robot-communication.md)

## Mentioned in
- [Designing Accessible Robot Communication](../sources/huh2026-accessible-robot-comm.md)

## Open questions / TBD
- Specific Tiago variant used in Huh et al. 2026 (Tiago Pro vs. Tiago++ vs. Tiago Iron) — not stated.
- Cost / availability data not yet ingested.
