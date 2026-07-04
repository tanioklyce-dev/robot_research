---
title: Galaxea R1 (and R1 Pro)
type: entity
subtype: robot
created: 2026-07-04
updated: 2026-07-04
sources: 2
tags: [galaxea, galaxea-r1, wheeled-humanoid, bimanual, mobile-manipulator, groot]
---

**Galaxea R1** — a full-size **dual-arm humanoid upper body on a three-wheel steering-vector chassis** (wheeled bimanual mobile manipulator) from Galaxea; **24 DOF total** (6 chassis + 4 torso + 14 dual arms/grippers), 0–200 cm operating height, 5 kg payload, up to 550 TOPS onboard ([user guide](../sources/galaxea-r1-user-guide.md)). A **[GR00T N1.6](../sources/groot-n1_6.md) training embodiment** — its **R1 Pro** variant (simulated, on the BEHAVIOR suite) is one of N1.6's added data sources.

## Specs
- 24 DOF: 6 chassis + 4 torso + 14 dual-arm-with-grippers; reach 70 cm/arm (86 with gripper); 5 kg @ 0.5 m.
- Sensors: head + 2 wrist + 5 chassis cameras, 360° LiDAR (optional 2nd). Up to 550 TOPS compute.
- **R1 Pro** variant referenced but not differentiated in the user guide.

## Why it matters in this wiki
- **GR00T data embodiment**: [GR00T N1.6](../sources/groot-n1_6.md) adds "simulated Galaxea R1 Pro on the BEHAVIOR suite" to its pretraining mix (with bimanual [YAM](yam.md), AGiBot Genie1, [Unitree G1](unitree-g1.md)) — placing Galaxea in the cross-embodiment corpus of an NVIDIA foundation model. Fills the "Galaxea R1 Pro" gap flagged during the N1.6 ingest.
- A wheeled-bimanual mobile manipulator in the same broad class as [Stretch](stretch.md) / [Reachy 2](reachy.md), but full-size dual-arm with a torso.

## Related
- [GR00T N1.6](nvidia-groot.md) — uses simulated R1 Pro on BEHAVIOR.
- [YAM](yam.md), [Unitree G1](unitree-g1.md), [AgiBot](agibot.md) — peer N1.6 data embodiments.
- [Stretch](stretch.md), [Reachy](reachy.md) — mobile-manipulator peers.

## Mentioned in
- [Galaxea R1 User Guide](../sources/galaxea-r1-user-guide.md) — primary source.
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — simulated R1 Pro training data.

## Open questions
- R1 vs R1 Pro differences; software stack (ROS 2/SDK), price, availability, battery/runtime.
- Whether the BEHAVIOR-suite R1 Pro is a Galaxea-official or NVIDIA-modified sim asset.
