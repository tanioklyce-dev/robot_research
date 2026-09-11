---
title: Unitree Go1
type: entity
subtype: robot
created: 2026-09-11
updated: 2026-09-11
sources: 3
tags: [unitree-go1, quadruped, robot-dog, china, affordable, edu, navigation, cross-embodiment]
---

**Unitree Go1** — [Unitree](unitree.md)'s 2021 consumer/education quadruped, the generation between the research-workhorse [A1](unitree-a1.md) and the current [Go2](unitree-go2.md). In this wiki it is the **quadruped the Berkeley RAIL navigation line uses to show cross-embodiment transfer**: a wheeled-robot-trained policy driven onto a legged body with no Go1 training data.

## Specs (vendor page, not ingested as a source)

From [unitree.com/go1](https://www.unitree.com/go1), three tiers:

| | Go1 Air | Go1 Pro | Go1 Edu |
|---|---|---|---|
| Price (listed) | $2,700 | $3,500 | contact sales |
| Top speed | 2.5 m/s | 3.5 m/s | 3.7 m/s (limit ~5 m/s) |
| Payload | ~4 kg (limit ~10) | ~4 kg | ~6 kg |
| "Super-sensing" stereo camera pairs | 1 | 5 | 5 |
| Compute | 1 × Nano-class | 3 × Nano-class | 2 × Nano + 1 Nano or NX |
| Python / scientific API, foot force sensors, 4G, optional 2D/3D lidar | — | — | ● |

- 12 joint motors (body/thigh 23.7 N·m, knee 35.55 N·m peak); joint ranges body ±49°, thigh −39–257°, shank −161 to −51°. The vendor's "world record" 4.7 m/s figure is a limit test, not an operating speed.
- Only the **Edu** tier exposes the programming interfaces research needs; that is the SKU in every paper below.

## In this wiki

- **[ViNT](../sources/vint-paper.md)** (CoRL 2023) — first appearance: the 31M navigation transformer drives a Go1 zero-shot for **45 m** maximum displacement without intervention, vs 8 m for GNM and 12 m for a single-robot model, with no quadruped data in training.
- **[MBRA / LogoNav](../sources/mbra-paper.md)** (RA-L 2025) — the same LogoNav policy as on the wheeled Earth Rover reaches **0.80** goal success outdoors on a Go1 (vs 0.30 for the GCP-relabeled baseline), 10 trials, ≤100 m, "without any adaptation."
- **[OmniVLA](../sources/omnivla-paper.md)** (2025) — follows natural-language instructions on a Go1 out of the box; cameras are re-mounted per robot and the policy runs off-board.
- Named as the quadruped reference alongside [Spot](spot.md) on that page.

## Why it matters here

Navigation transfer to the Go1 is cheap because the policy's action is a normalized 2-D waypoint chunk and Unitree's locomotion controller absorbs the legs — the same [control-abstraction](../concepts/robotics/control-abstraction-levels.md) split that makes humanoid VLAs emit WBC commands. None of the three papers reports what the Go1's onboard controller was told, only that "action conversion is internally applied."

## Mentioned in

- [ViNT paper](../sources/vint-paper.md)
- [MBRA paper](../sources/mbra-paper.md)
- [OmniVLA paper](../sources/omnivla-paper.md)
