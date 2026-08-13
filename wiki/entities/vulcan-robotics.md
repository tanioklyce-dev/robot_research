---
title: Vulcan Robotics
type: entity
subtype: company
created: 2026-08-13
updated: 2026-08-13
sources: 3
tags: [vulcan-robotics, sourccey, startup, open-hardware, household-robot, lerobot, xvla, cern-ohl]
---

**Vulcan Robotics** — US startup founded by [Nick Maselli](nick-maselli.md), building [Sourccey](sourccey.md), an open-source personal home robot. Site: [vulcanrobotics.ai](https://vulcanrobotics.ai/). GitHub org: [`vulcan-forge`](https://github.com/vulcan-forge). Discord and Twitter communities; store listed as "Coming Soon."

Positioning: *"the open-source personal robot for physical AI and robotics development"* — a dual pitch at families (laundry, table setting, cleaning) and at developers (teleoperate → record → train → rollout on [LeRobot](lerobot.md)).

## What is known

- **Founder**: Nick Maselli. No other named team members published.
- **Funding**: none disclosed.
- **Location**: US; city not published.
- **Business model**: hardware sales (store not yet live, **no price published**) plus **rented compute** — "rented compute is planned for users who need stronger training or inference" ([specs page](../sources/vulcan-robotics-sourccey-site.md)). The compute-rental line is the more interesting half: it concedes that the robot's advertised AI does not run on the robot, and turns that into a recurring-revenue surface.
- **Timeline**: open-source the platform Aug 2026; ship Sep 2026; SLAM tooling Oct 2026; developer collaboration tools Nov 2026; "autonomous integrations" early 2027; "full autonomy across core household tasks" 2028.

## Repositories (`vulcan-forge`, verified 2026-08-13)

| Repo | License | Stars | Last push |
|---|---|---|---|
| `sourccey-desktop` | none | 18 | 2026-07-24 |
| [`sourccey-hardware`](../sources/sourccey-hardware-repo.md) | **CERN-OHL-S-2.0** | 16 | 2026-07-10 |
| `lerobot-vulcan` | Apache-2.0 | 12 | 2026-08-09 |
| `lerobot-robot-sourccey` | Apache-2.0 | 1 | 2026-08-09 |
| `dimos-vulcan` | — | 1 | 2026-07-03 |
| `lerobot` (upstream mirror) | Apache-2.0 | 3 | 2025-11-17 |
| `jetson-orin-gpio-patch` (archived) | — | 0 | 2025-04-24 |

Two things stand out. **Hardware is copyleft while software is permissive** — CERN-OHL-S-2.0 obliges anyone distributing a modified Sourccey design to publish their sources, which is the opposite of the [SO-ARM101](so-arm101.md) / [LeKiwi](lekiwi.md) / [XLeRobot](xlerobot.md) Apache-2.0 norm. And the **advertised "Electrical" repository does not exist**; the docs page names four repos and the org publishes three.

`dimos-vulcan` is a fork of `dimensionalOS/dimos` — **[DimOS](dimos.md)**, now ingested ([source](../sources/dimos-github.md)): an Apache-2.0 agentic robotics middleware from [Dimensional Inc.](dimensional-inc.md) with 3,874 stars, five interchangeable transports, and an MCP-based agent layer. Whether Vulcan intends it as a [Sourccey](sourccey.md) layer is still unclear — the fork has one star and was last pushed 2026-07-03 — but the fit is legible: DimOS's shipped capability set (2D-LiDAR SLAM, spatial memory, Quest teleop → [LeRobot](lerobot.md) dataset export) maps almost exactly onto Sourccey's Oct–Nov 2026 roadmap items, and Sourccey's own stack currently has no navigation layer at all.

## Approach

Vulcan's engineering choices read as a coherent cost thesis rather than a set of compromises:

- **PLA on a $700 desktop printer** instead of machined or injection-moulded parts — self-manufacturable, self-repairable, and the stated safety mechanism ("low-mass PLA parts reduce injury risk").
- **[FeeTech](feetech.md) smart servos** on one 1 Mbaud UART bus — the cheapest credible actuator lineage, and the one [LeRobot](lerobot.md) speaks natively.
- **[Raspberry Pi 5](raspberry-pi-5.md), not Jetson** — the archived `jetson-orin-gpio-patch` (Apr 2025) suggests Jetson was on the table earlier. Choosing the Pi caps BOM cost and pushes inference off-board, which the compute-rental plan then monetizes.
- **Open-loop wheels, no encoders** — saves cost and complexity now, and is the choice most in tension with the published roadmap (see [Sourccey](sourccey.md)).
- **Ship a working policy** — four [X-VLA](x-vla.md) laundry-folding micromodels out of the box. Nobody else in this tier does this.

> [!note] "Open source" is currently narrower than the marketing
> As of 2026-08-13: the hardware repo is a CAD dump (115 STEP files, no BOM/wiring/URDF/STLs), both documentation pages read "will be available soon," the Electrical repo is missing, and the STL claim made on the site and repeated in press coverage is not borne out by the repository. The August 2026 open-source milestone is the current month — this assessment should be re-checked rather than treated as settled.

## Related

- [Sourccey](sourccey.md) — the product
- [Nick Maselli](nick-maselli.md) — founder
- [X-VLA](x-vla.md) — the shipped policy
- [LeRobot](lerobot.md) — the framework
- [XLeRobot](xlerobot.md), [LeKiwi](lekiwi.md), [The Robot Studio](the-robot-studio.md) — the ecosystem it enters
- [DimOS](dimos.md) / [Dimensional Inc.](dimensional-inc.md) — forked as `dimos-vulcan`; a parallel open-source-plus-hosted-service business model
- [Sensori Robotics](sensori-robotics.md) — the other "open designs, sold as a supported product" position in this wiki

## Mentioned in

- [Vulcan Robotics — Sourccey product site](../sources/vulcan-robotics-sourccey-site.md)
- [sourccey-hardware GitHub repository](../sources/sourccey-hardware-repo.md)
- [Sourccey vs XLeRobot](../syntheses/platforms/sourccey-vs-xlerobot.md)
