---
title: HopeJR-Arm
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-05-28
sources: 2
tags: [hope-jr-arm, robot-arm, humanoid-arm, lerobot, the-robot-studio, hackathon-prize]
---

**HopeJR-Arm** — open-source **humanoid arm + hand** module from [The Robot Studio](the-robot-studio.md), supported natively by [LeRobot](lerobot.md). Listed in the [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) (Table 1a) at **~€500**, positioning it as a low-cost humanoid arm tier between the SO-100 (~€225) and Koch-v1.1 (~€670). Awarded as the **premium-tier hardware prize** at the [LeRobot Worldwide Hackathon 2025](lerobot-worldwide-hackathon-2025.md).

## Provenance

- **Vendor/design**: [The Robot Studio](the-robot-studio.md) (TheRobotStudio org on GitHub).
- **BOM**: [github.com/TheRobotStudio/HOPEJr/blob/main/Arm/BOM.md](https://github.com/TheRobotStudio/HOPEJr/blob/main/Arm/BOM.md) (cited in [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) Appendix A).
- **Citation**: "TheRobotStudio, 2025 — HOPEJr/Arm: Robotic Arm Module of HOPEJr."

## Position in the LeRobot platform tier

| Tier | Platforms | Cost range |
|---|---|---|
| Cheapest tabletop | SO-100, LeKiwi | €225–€230 |
| **Humanoid arm + hand** | **HopeJR-Arm** | **~€500** |
| Mid manipulator | Koch-v1.1 | ~€670 |
| Premium bimanual | ALOHA-2 | ~€21k |

## Related

- [The Robot Studio](the-robot-studio.md) — vendor / design authority (confirmed via ICLR 2026 paper Appendix A)
- [LeRobot Worldwide Hackathon 2025](lerobot-worldwide-hackathon-2025.md) — context where it first appeared in this wiki
- [LeKiwi](lekiwi.md) — co-awarded as the base for top-3 hackathon winners
- [SO-ARM101](so-arm101.md) — lower-tier arm in the same prize structure

## Mentioned in

- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — Table 1a + Appendix A BOM citation; first authoritative source.
- [LeRobot Worldwide Hackathon 2025 — All Winners (HF Space)](../sources/lerobot-worldwide-hackathon-2025-winners.md)

## Open questions / TBD

- Specs (DOF, reach, payload, motor class) — not in ICLR 2026 paper; would need direct BOM ingest.
- Whether the hand and arm are sold separately or as a unit.
