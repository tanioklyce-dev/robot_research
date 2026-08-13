---
title: The Robot Studio
type: entity
subtype: organization
created: 2026-05-10
updated: 2026-05-28
sources: 3
tags: [the-robot-studio, so-arm, so-arm100, so-arm101, hope-jr-arm, open-hardware, low-cost-arm, lerobot]
---

**The Robot Studio** — open-hardware design group (`TheRobotStudio` on GitHub) responsible for **two of LeRobot's natively-supported arm platforms**: the **[SO-ARM100 / SO-ARM101](so-arm101.md)** lineage (~€225 single / €550 bimanual) and the **[HopeJR-Arm](hope-jr-arm.md)** humanoid arm + hand (~€500) ([LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md), Table 1a + Appendix A). Their designs are the dominant low-cost arms in the [LeRobot](lerobot.md) ecosystem — SO-ARM is used as the default manipulator across [LeKiwi](lekiwi.md), [XLeRobot](xlerobot.md), and similar sub-$1k mobile-manipulator platforms.

## Confirmed designs (LeRobot ICLR 2026 paper, Appendix A)

- **SO-10X (SO-100 / SO-101)** — guide from [Knight et al., 2024](so-arm101.md). [github.com/TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100).
- **HopeJR-Arm** — humanoid arm module. [github.com/TheRobotStudio/HOPEJr](https://github.com/TheRobotStudio/HOPEJr/tree/main/Arm) (BOM at `Arm/BOM.md`).

## Why it matters in this wiki

Without SO-ARM100/101's sub-$500 price point and open-source design, the LeRobot-stack story (LeKiwi + SO-ARM101, XLeRobot's $660 dual-arm) doesn't pencil out. The Robot Studio is effectively the upstream-of-the-upstream of the affordable manipulation tier in this wiki.

## Related

- [SO-ARM101](so-arm101.md) — the primary design
- [HopeJR-Arm](hope-jr-arm.md) — humanoid-arm design
- [LeRobot](lerobot.md) — primary software ecosystem
- [LeKiwi](lekiwi.md) / [XLeRobot](xlerobot.md) — downstream compositions

## Mentioned in

- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — Appendix A lists both SO-10X and HopeJR-Arm as TheRobotStudio designs supported natively by LeRobot.
- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [LeKiwi GitHub](../sources/lekiwi-github.md)

## Open questions / TBD

- Direct ingest of The Robot Studio website / repos — needed to back-fill SO-ARM100/101 specs and the HopeJR-Arm full design.
