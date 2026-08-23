---
title: Nori Robotics
type: entity
subtype: company
created: 2026-08-23
updated: 2026-08-23
sources: 2
tags: [nori, consumer-robotics, home-robot, y-combinator, san-francisco, startup, data-flywheel]
---

**Nori Robotics** — San Francisco startup, founded 2026, **Y Combinator Summer 2026**, **5 people**. Builds the **[NORI A3](nori-a3.md)**, a bimanual mobile home manipulator sold at **$1,688** with a stated Fall 2026 ship window ([product site](../sources/nori-robotics-site.md), [YC profile](../sources/nori-robotics-yc-profile.md)).

Founder: **Antonio Sitong Li** — Columbia, Computer Science and Architecture; prior research on **teaching robots tasks from VR demonstrations**; a computer-vision patent; previously co-founded Truely ([YC profile](../sources/nori-robotics-yc-profile.md)).

## The thesis

Nori is not primarily selling a robot. Its stated strategy is to **break the robotics data bottleneck by subsidising the collector**: put cheap bimanual manipulators into homes globally, harvest the demonstrations owners produce, and train generalist policies on the result. The **Skills Marketplace** ("train your Nori at home, share its skills anywhere") is the mechanism. Market sizing offered: $1.2 B in the US at 0.5% penetration of households and businesses ([YC profile](../sources/nori-robotics-yc-profile.md)).

That makes Nori the first company in this wiki whose consumer product is explicitly framed as a **data-collection instrument**. [Dobb-E](dobb-e.md) and [Robot Utility Models](robot-utility-models.md) made the same argument academically with a $25 reacher-grabber rig; [Sourccey](sourccey.md) ships policies *to* owners; Nori proposes to harvest them *from* owners at $1,688 a unit.

## Traction

- First robot deployed and **>$300,000 in sales within 6 weeks of launch** ([YC profile](../sources/nori-robotics-yc-profile.md)) — roughly 178 units at list, though whether that is pre-orders or deliveries is unstated.
- Secondary coverage reports a first unit shipping **21 July 2026**, against the site's "ships Fall 2026." See the [product site](../sources/nori-robotics-site.md) for the contradiction.

## Position against the rest of the sub-$2k tier

| | Price published | Compute | Policy at launch | Openness |
|---|---|---|---|---|
| **Nori A3** | **$1,688, no deposit** | [Pi 5](raspberry-pi-5.md) 4 GB | none named; "train it yourself" | none stated |
| [Sourccey](sourccey.md) | undisclosed | [Pi 5](raspberry-pi-5.md) | [X-VLA](x-vla.md) laundry micromodels preinstalled | CERN-OHL-S hardware, Apache software |
| [Zeroth M1](zeroth-m1.md) | $2,499 | — | — | — |
| [XLeRobot](xlerobot.md) | $660 BOM | Pi 4/5 optional | you bring [LeRobot](lerobot.md) | fully open |

Nori's differentiators are the **complete published price with no deposit** — still rare in this tier, as the [consumer robotics value chain](../syntheses/society/consumer-robotics-value-chain.md) analysis found — and **US assembly**. Its conspicuous gap is **openness**: no repository, no licence, no named model, no API in either primary.

> [!note] The Pi 5 4 GB is the binding constraint
> Nothing at 0.9 B parameters and up runs on it. The "Nori Lab" laptop app is therefore almost certainly where inference happens, making the A3 a **thin client** — the same architecture as stock [XLeRobot](xlerobot.md) and [Sourccey](sourccey.md), and unremarkable at the price, but undisclosed in both primaries. See the [YC profile source page](../sources/nori-robotics-yc-profile.md).

## Mentioned in
- [Nori Robotics — NORI A3 product site](../sources/nori-robotics-site.md)
- [Nori Robotics — Y Combinator company profile (S26)](../sources/nori-robotics-yc-profile.md)
