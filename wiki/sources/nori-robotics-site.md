---
title: Nori Robotics — NORI A3 product site
type: source
url: https://www.norirobotics.com/
author: Nori Robotics
published: 2026-08
ingested: 2026-08-23
format: vendor product page
tags: [nori, home-robot, bimanual, mobile-manipulator, consumer-robotics, affordable-hardware, skills-marketplace, teleoperation, san-francisco]
---

# Nori Robotics — NORI A3 product site

Vendor page for the **[NORI A3](../entities/nori-a3.md)**, a $1,688 bimanual home robot from [Nori Robotics](../entities/nori-robotics.md). Ingested as the **primary** for the A3's published specifications, price and ship date, because secondary coverage of this product is already circulating with a spec error (see the contradiction below).

## Summary

A single-page storefront. Tagline: *"The most capable robot for $1,688."* Positioning is domestic and unglamorous — kitchen help, tidying, fetching from the fridge, loading dishes, folding clothes, pouring ingredients. Two things distinguish it from the rest of the sub-$2k tier this wiki tracks: a **published, complete price with no deposit**, and a **Skills Marketplace** — *"Train your Nori at home, share its skills anywhere"* — which makes user-generated policy sharing a launch feature rather than a roadmap item. Assembled in San Francisco. Ships Fall 2026. Y Combinator-backed.

## Key claims (all quoted from the page)

| | |
|---|---|
| **Price** | **$1,688**, "full price, no deposit" |
| **Availability** | "now shipping fall 2026"; pre-orders open |
| **Arms** | **"7+1 DOF, 1.5 kg payload per-arm"** — bimanual |
| **LiDAR** | 12 m range, 8–12 Hz scan rate, 0.72° angular resolution at 10 Hz |
| **Cameras** | **4 × 720p RGB, up to 30 fps**, on the **grippers, head and neck** |
| **Audio** | speaker + microphone, spoken commands |
| **Battery** | **6–8 hours** |
| **Software** | **"Nori Lab"** — a *laptop* app to "train, operate, and manage your robot" |
| **Marketplace** | Skills Marketplace: train at home, share the skills |
| **Manufacture** | "Based in the USA — Assembled in San Francisco" |
| **Backing** | "YC-backed" |

## What the page does not say

Notably absent, and each of these is decision-grade for anyone comparing against [Sourccey](../entities/sourccey.md), [XLeRobot](../entities/xlerobot.md) or [Zeroth M1](../entities/zeroth-m1.md):

- **No onboard compute is named** anywhere on the page. (The [YC profile](nori-robotics-yc-profile.md) names it: a **Raspberry Pi 5, 4 GB**.)
- **No policy, model, or learning method.** "Train your Nori at home" is the entire description of how a skill comes to exist. No mention of imitation learning, teleoperation rig, demonstration count, or what a "skill" is as an artifact.
- **No autonomy claim, no success rates, no task-completion evidence.** The task list is illustrative, not benchmarked.
- **No height, mass, reach, base type, or wheel configuration.** The renders show a wheeled base with a vertical lifting column; the page never specifies it.
- **No depth sensor.** Four **RGB** cameras and a 2D LiDAR — see the note below.
- **No licence, no repository, no API, no software-update policy.** Contrast [Sourccey](../entities/sourccey.md), which is CERN-OHL-S hardware with named LeRobot repos.
- **No subscription or marketplace revenue terms.**

> [!note] Four RGB cameras and a planar LiDAR is a thin sensing stack for manipulation
> The LiDAR's spec (12 m, 0.72° at 10 Hz) is a 2D navigation scanner. Nothing on the page provides **metric depth at manipulation range** — no stereo pair is claimed, no RGB-D, no ToF. Wrist cameras on both grippers is the right call for imitation learning, and monocular policies do work ([ACT](../entities/act.md), [SmolVLA](../entities/smolvla.md) train on RGB), but it does close off the classical [6-DOF grasping](../concepts/robotics/six-dof-grasp-generation.md) path, which wants a segmented point cloud.

> [!warning] Contradiction — "55 kg" is a lift column, not an arm payload
> Secondary coverage of the A3 launch reports that it "can lift 55 kg." The vendor page states **1.5 kg payload per arm**, and the company's own [YC profile](nori-robotics-yc-profile.md) lists both figures side by side: **55 kg linear lift** and **1.5 kg per arm**. The 55 kg is the **vertical lift column** that raises and lowers the torso — a different mechanism from the arms. Both numbers are true of the robot; the secondary lost the binding. Textbook scope loss: quote 1.5 kg for anything the robot picks up.

> [!warning] Contradiction — ship date
> The page says "**ships fall 2026**." Secondary coverage reports the first unit shipped **21 July 2026**, and the [YC profile](nori-robotics-yc-profile.md) claims a deployed first robot within 6 weeks of launch. Most likely reconciliation: an early/hand-built unit went out ahead of the general Fall window. Not resolvable from either primary.

## Entities mentioned

- [Nori Robotics](../entities/nori-robotics.md) · [NORI A3](../entities/nori-a3.md)

## Concepts touched

- [End-user robot programming](../concepts/robotics/end-user-robot-programming.md) — "train your Nori at home" is an EUP claim with no described interface.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the task list is squarely domestic ADL-adjacent.

## Open questions

- **What is a "skill" in the Skills Marketplace?** A recorded trajectory, a finetuned policy checkpoint, a behaviour-tree config? The answer determines whether the marketplace is a data flywheel, a macro library, or a demo.
- **What runs where?** "Nori Lab" is a laptop app. If inference is off-board on the owner's laptop, the robot is tethered to a running PC on the same network — the same architecture as stock [XLeRobot](../entities/xlerobot.md) and [Sourccey](../entities/sourccey.md), and worth stating plainly to buyers.
- Does the robot function at all with no laptop present?
