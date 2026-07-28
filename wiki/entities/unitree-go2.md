---
title: Unitree Go2
type: entity
subtype: robot
created: 2026-07-27
updated: 2026-07-27
sources: 1
tags: [unitree-go2, quadruped, robot-dog, china, affordable, edu, project-fetch]
---

**Unitree Go2** — Unitree Robotics' consumer/education-tier quadruped ("robot dog"), released 2023. The cheap end of the quadruped market and the most likely robot in Anthropic's [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) uplift study. Sits opposite [Spot](spot.md) in the same way [Unitree G1](unitree-g1.md) sits opposite the $90k+ humanoids: an order of magnitude cheaper, sold direct, and consequently the default quadruped in hobbyist and university work.

> [!warning] Attribution caveat
> Anthropic's [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) post refers only to a **"quadruped robodog"** and never names a manufacturer or model. Multiple secondary outlets covering the experiment identify it as a **Go2**, and the post's description (manufacturer-supplied handheld controller, onboard **video + lidar**, unlockable pre-programmed dance/backflip/bipedal-stance routines, several connection methods with inconsistent online documentation) matches the Go2 well. Treat the identification as **reported, not primary-sourced**. Everything in the Specs section below comes from vendor/secondary material rather than an ingested primary source.

## Specs (vendor/secondary, un-ingested)

- ~15 kg, quadruped; top speed in the ~11 mph / 5 m/s range on the higher tiers.
- **Onboard lidar** (4D LIDAR L1 on most SKUs) + front-facing camera — the two sensors Project Fetch's Phase 2 required teams to read.
- Tiered SKUs: **Air / Pro / EDU**, with the EDU tier adding onboard compute (Jetson-class, ~40 TOPS on some configurations) and unlocked low-level joint control. Price spans roughly **$1.6k (Air) to ~$17k (EDU)** — the SKU used in Project Fetch is unknown.
- Ships pre-programmed behaviors (dance, bipedal stance, backflip on higher tiers) that Project Fetch participants unlocked as "outtakes."

## Why it appears in this wiki

The Go2 is the concrete instance of a claim Project Fetch makes in the abstract: **the hard part of touching unfamiliar robot hardware is the connection layer, not the control problem.** In that experiment the largest measured uplift was in establishing laptop↔robot communication and pulling sensor data — the Claude-less team was actively **misled by inaccurate online documentation** and dropped the simplest connection method, and spent one person's entire day extracting lidar. That is a property of the *SDK and its documentation*, not of quadruped locomotion, and it is the tax any cheap-tier platform with a fast-moving, thinly-documented API imposes.

## Position vs other quadrupeds in this wiki

- **[Spot](spot.md)** (Boston Dynamics) — the industrial/commercial reference quadruped: mature Python/gRPC **Spot SDK**, Autowalk, optional arm, ~$75k+. Where Spot's SDK is the thing that makes it programmable, the Go2's is the thing Project Fetch suggests you fight.
- **[Unitree G1](unitree-g1.md) / [H1](unitree-h1.md)** — the same vendor's humanoid line, and the wiki's much better-covered Unitree platforms (G1 is the de-facto benchmark robot for learned [whole-body control](../concepts/robotics/whole-body-control.md)).
- The wiki has **no ingested primary source on any quadruped platform** — Spot is grounded in a Boston Dynamics blog post and the Go2 only in a policy article that doesn't name it. See the [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md), which flags quadrupeds as an underrepresented tier.

## Related
- Unitree Robotics — manufacturer (**no entity page yet**; the wiki has G1, H1, and Go2 but not the parent company).
- [Spot](spot.md) — the commercial-tier quadruped contrast.
- [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) — the only ingested source that uses it.

## Mentioned in
- [Project Fetch: Can Claude train a robot dog?](../sources/anthropic-project-fetch-robot-dog.md) — as an unnamed "quadruped robodog"; identification is secondary.
