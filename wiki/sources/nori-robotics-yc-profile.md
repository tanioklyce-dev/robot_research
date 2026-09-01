---
title: Nori Robotics — Y Combinator company profile (S26)
type: source
url: https://www.ycombinator.com/companies/noril1
author: Nori Robotics / Y Combinator
published: 2026-08
ingested: 2026-08-23
format: company profile
tags: [nori, y-combinator, home-robot, consumer-robotics, raspberry-pi-5, data-flywheel, business-model, funding]
---

# Nori Robotics — Y Combinator company profile (S26)

Company-authored profile. Ingested alongside the [product site](nori-robotics-site.md) because it carries three facts the storefront omits and that a buying or comparison decision turns on: the **onboard compute**, the **55 kg lift** figure that secondary coverage has garbled, and the **data-flywheel business thesis** behind the price.

## Summary

Nori Robotics — YC **Summer 2026**, founded 2026, **5 people**, San Francisco. One-liner: *"sub-$2000 humanoid robot you can teach to do anything."* The product is a bimanual mobile manipulator at **$1,688** that ships able to clean rooms, restock shelves and fold clothes, with teachable software on top.

The strategic claim is the interesting part, and it is not a hardware claim: Nori positions the robot as an answer to **the robotics data bottleneck** — deploy cheap units into homes worldwide, and the demonstrations they generate train generalist policies. The market sizing offered is $1.2 B in the US from capturing 0.5% of households and businesses. Traction claimed: **first robot deployed and >$300,000 in sales within 6 weeks of launch.**

## Key claims

**Company**

- YC batch **Summer 2026**; founded 2026; team of **5**; San Francisco.
- Founder: **Antonio Sitong Li** — Columbia, CS + Architecture; research on **VR-based robot task learning** (teaching robots tasks from VR demonstrations); holds a computer-vision patent; previously co-founded Truely.
- Traction: first robot deployed and **>$300 K in sales in 6 weeks**.

**Robot specifications (beyond the product page)**

| | |
|---|---|
| **Degrees of freedom** | **19 DOF** total |
| **Linear lift** | **55 kg** |
| **Arm payload** | 1.5 kg per arm, dual |
| **Compute** | **Raspberry Pi 5, 4 GB module** |
| **Vision** | 4 × 720p @ 30 fps |
| **Audio** | microphone array + speaker, **full-duplex speech** |

**Business model**

- Sell cheap hardware at scale → collect household manipulation data → train generalist policies. The robot is framed as a **data-collection instrument** as much as a product.

## The compute number is the whole story

> [!warning] A Raspberry Pi 5 4 GB cannot run a modern VLA
> This wiki has the numbers to be specific. On a [Pi 5](../entities/raspberry-pi-5.md), [Sourccey](../entities/sourccey.md) — the closest comparable, also Pi-5-hosted — **cannot run the [X-VLA](../entities/x-vla.md)-0.9B policies it ships with**, so inference is off-board. [ACT](../entities/act.md) at ~84 M parameters is the only policy in the wiki's [XLeRobot bring-up analysis](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) that hits control rate on a small onboard board, and that was measured on a **Jetson**, not a Pi. [SmolVLA](../entities/smolvla.md) at 450 M is served off-board from a [DGX Spark](../entities/dgx-spark.md) in that same plan. And **4 GB** is the smallest Pi 5 SKU — it rules out the 8 GB [Hailo](../entities/hailo.md) AI HAT+ 2 pairing that would otherwise be the Pi's route to VLM-class inference.
>
> So the "**Nori Lab** laptop app" on the [product site](nori-robotics-site.md) is not an accessory. It is almost certainly **where the policy runs**. The Pi 5 is a sensor hub and motor controller; the robot is a **thin client** that needs a laptop on the network to think. Nothing in either primary states this, and nothing contradicts it.

This is not a criticism of the design — it is the same architecture as stock [XLeRobot](../entities/xlerobot.md) and [Sourccey](../entities/sourccey.md), and at $1,688 including two 7-DOF arms and a 55 kg lift column, it is the only architecture the BOM permits. It is a criticism of the disclosure: a buyer comparing $1,688 against a $2,499 [Zeroth M1](../entities/zeroth-m1.md) cannot see from either storefront that both are laptop-tethered.

## The data thesis, weighed

Nori's pitch is the [Dobb-E](../entities/dobb-e.md) / [Robot Utility Models](../entities/robot-utility-models.md) argument with a price tag attached: household data is the bottleneck, so subsidise the collector. Two things the profile does not address, both of which this wiki has evidence on:

- **Owner-collected data is not free of quality problems.** The [XLeRobot bring-up plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) identifies **demo quality** — not hardware, not navigation — as the hardest leg of a first policy. [X-VLA](../entities/x-vla.md)'s Soft-Fold dataset needed DAgger-style iteration with an expert retraining every 100 episodes. A marketplace of unvetted home demonstrations is a different distribution from a curated one.
- **Nobody has shown the flywheel closing at this tier.** *(Partly answered 2026-08-31.)* [Scanford](robot-powered-data-flywheels-paper.md) closes one — a two-week library deployment whose self-labeled data lifts a VLM from 32.4% to 71.8% on its own task **and** from 24.8% to 46.6% on general English OCR. But it closes on **perception with an external ground-truth index** (the library catalog), not on manipulation quality, and the tier below still has no instance: [Sourccey](../entities/sourccey.md) ships policies *to* owners; Nori proposes to harvest policies *from* them. The wiki's [consumer robotics value chain](../syntheses/society/consumer-robotics-value-chain.md) analysis notes that service layers are paid on **retention**, and a data flywheel is the most retention-exposed model there is.

## Entities mentioned

- [Nori Robotics](../entities/nori-robotics.md) · [NORI A3](../entities/nori-a3.md) · [Raspberry Pi 5](../entities/raspberry-pi-5.md)

## Concepts touched

- [End-user robot programming](../concepts/robotics/end-user-robot-programming.md)
- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- **19 DOF, itemised?** 7+1 per arm = 16, plus the lift column = 17, plus a head pan/tilt = 19, leaving **zero for the base** — which would make it differential-drive with wheels counted separately, or the arms are 7 DOF with the gripper not counted. Unresolved from the primaries.
- Is the >$300 K figure pre-orders (revenue recognised on shipment) or delivered units? At $1,688 it is ~178 units either way.
- What are the **data rights** attached to a Skills Marketplace upload?
