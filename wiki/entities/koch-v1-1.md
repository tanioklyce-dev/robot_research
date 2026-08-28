---
title: Koch v1.1
type: entity
subtype: robot
created: 2026-08-27
updated: 2026-08-27
sources: 0
tags: [koch-v1-1, lerobot, dynamixel, leader-follower, teleoperation, imitation-learning, low-cost-arm, open-source, dormant]
---

**Repo:** [`jess-moss/koch-v1-1`](https://github.com/jess-moss/koch-v1-1) — Apache-2.0, 727★. **Last pushed 2024-09-17.**

**Koch v1.1** — a low-cost **leader–follower arm pair** for teleoperated demonstration collection, and one of the **8 platforms [LeRobot](lerobot.md) natively supports** ([ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) §3.1, Table 1a). Jess Moss's revision of **Alexander Koch's** original [`low_cost_robot`](https://github.com/AlexanderKoch-Koch/low_cost_robot), built on [Dynamixel](dynamixel.md) servos — which makes it the **Dynamixel-tier price reference** against the [FeeTech](feetech.md)-based [SO-ARM101](so-arm101.md).

## Bill of materials and cost

Both arms are 6-DOF; the leader is a passive-ish teleoperation handle, the follower does the work.

| | Servos | US | EU | UK |
|---|---|---|---|---|
| **Leader** | 6× **XL330-M077-T** | **$199** | 305€ | £222 |
| **Follower** | 2× **XL430-W250-T** + 4× **XL330-M288-T** | **$278** | 368€ | £285 |
| **Pair** | | **$477** | **673€** | **£507** |

Plus a Waveshare serial-bus servo driver board per arm, 5 V and 12 V supplies, a voltage reducer, jumper wires and table clamps. Costs are the repo's own tables and are 2024-dated.

> [!note] "~€670 single" means one leader + one follower
> The [Dynamixel](dynamixel.md) page quotes Koch-v1.1 at "~€670 (single)" against SO-ARM101's "~€225 (single)". Confirmed here: **673€ is the leader+follower pair** — a *single-arm* (mono, not bimanual) setup, which is the LeRobot convention. The ~3× gap over SO-ARM101 at comparable capability is the whole reason SO-10X came to dominate community dataset contributions.

## What v1.1 changed

Per the repo, all assembly ergonomics rather than capability: fixed screw interferences, standardized hole sizes, removed screws fastening into plastic, **added a platform for the leader arm** (so the follower can pick objects off the ground), **removed the need for a soldering iron** and for manually adjusting the voltage converter by swapping the DC converter, added SolidWorks models, a wiring diagram, and assembly videos.

## Status

> [!warning] Dormant since September 2024
> The repository has not been pushed to in roughly two years, while [SO-ARM101](so-arm101.md), [LeKiwi](lekiwi.md) and [XLeRobot](xlerobot.md) have all iterated. Koch v1.1 remains a *supported* LeRobot platform and a citation in the ICLR paper, but it is best read as the **historical Dynamixel-tier reference** rather than a live recommendation. Anyone choosing a first teleop rig today has cheaper, better-maintained options in the FeeTech tier.

## Related

- [LeRobot](lerobot.md) — natively supports it; one of 8 platforms
- [Dynamixel](dynamixel.md) — the servo lineage; Koch is its price-point exemplar
- [SO-ARM101](so-arm101.md) / [FeeTech](feetech.md) — the ~3×-cheaper tier that displaced it
- [LeKiwi](lekiwi.md) — offers a Koch-v1.1 + XL430 alternative motor config
- [Imitation learning](../concepts/learning/imitation-learning.md) — leader–follower teleop is how the demonstrations get collected

## Mentioned in

- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — Table 1a; one of the 8 natively-supported platforms and the Dynamixel price reference.
- [LeKiwi GitHub](../sources/lekiwi-github.md) — Koch v1.1 + XL430 named as an alternative motor configuration.
