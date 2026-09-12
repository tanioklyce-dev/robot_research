---
title: LeHome — A Simulation Environment for Deformable Object Manipulation in Household Scenarios (Li … Wu; ICRA 2026)
type: source
url: https://arxiv.org/abs/2604.22363
fetch_url: https://arxiv.org/pdf/2604.22363v1
author: Zeyi Li, Yushi Yang, Shawn Xie, Kyle Xu, Tianxing Chen, Yuran Wang, Zhenhao Shen, Yan Shen, Yue Chen, Wenjun Li, Yukun Zheng, Chaorui Zhang, Siyi Lin, Fei Teng, Hongjun Yang, Ming Chen, Steve Xie, Ruihai Wu
published: 2026-04-24
ingested: 2026-09-11
venue: ICRA 2026 (arXiv v1; 8 pp.)
local_path: raw/2604.22363v1.pdf
sha256: 8db2a9d6de7ab45aec98067e346680969957b93ad62dd91a1d902feaacb8dc9f
format: pdf
tags: [lehome, simulator, deformable-objects, garments, household, lerobot, xlerobot, lekiwi, isaac-sim, pbd, fem, action-graph, domain-randomization, sim-to-real, co-training, smolvla, pi0, act, diffusion-policy, peking-university, lightwheel]
---

## Summary

The simulator behind the [LeHome Challenge](../entities/lehome-challenge-2026.md), from Peking University, CASIA, Lightwheel and HKU. Its claim is coverage: six classes of deformable object — liquids, gaseous fluids (flame), granular, linear (cable, rope), thin shells (garments, posters), volumetric (sausage, cutlet) — each mapped to the physics that suits it (PBD, FEM, Eulerian flow, or rigid-chain approximations), inside furnished bedroom/kitchen/living-room/washroom scenes, with an **Action Graph** of event-response nodes for mechanisms physics alone does not produce (a knife *splitting* a sausage into two new meshes). It supports Franka and UR but is built around the **low-cost LeRobot family — LeRobot, LeKiwi, [XLeRobot](../entities/xlerobot.md)** — with keyboard, joystick and leader-follower teleop and a domain-randomization-plus-replay data pipeline. The evidence is modest: four policies on six tasks in sim with 50 demos each, and a real dual-arm LeRobot experiment where **sim + 10 real demos lifts average success from ~15% to ~50%.**

> [!warning] This is not the challenge-protocol primary the backlog expected
> The [backlog](../backlog.md) filed this paper as "the organisers' primary for the success checker, the keypoint conditions, and the unseen-garment protocol." It is not. The ICRA paper describes the simulator and a six-task benchmark; the challenge's garment-keypoint success checker, seen/unseen split, real-final scoring and bonus are **not in it**. Those remain sourced only through the winner's [tech report](larchenko-learning-to-fold-tech-report.md). Whether the organisers published the protocol elsewhere is an open item.

## Key claims

### Simulator (§III)

- **Physics per category:** liquid → PBD; flame → Omniverse Flow sparse-voxel Eulerian simulation; fine granules → PBD, coarse (coffee beans) → rigid bodies; linear → multi-rigid-body chain *or* FEM; thin shell → PBD where wrinkling matters (garments), FEM otherwise (posters); volumetric → FEM with elastic/elastoplastic models. Built on Omniverse/Isaac (implied by Flow; not stated outright).
- **Action Graph:** On-Trigger → Computation → State-Update nodes; the sausage cut is collision trigger → mesh segmentation along the blade plane → two new objects with copied physics and textures. Claimed properties: modular, controllable, extensible.
- **Robots and teleop:** LeRobot single-arm, LeKiwi and XLeRobot mobile, bimanual; keyboard/joystick joint-space, leader-follower, and hybrid arm-plus-base control for mobile robots.
- **Domain randomization:** initial pose, lighting, tabletop texture, visual material at episode start; then **trajectory replay** under new appearance with object positions fixed, filtered by task-specific success detectors.
- Table I positions LeHome against RoboTwin 2.0, DexGarmentLab, BEHAVIOR-1K, LIBERO, RLBench and RoboCasa on nine features; only LeHome ticks all nine (household scenes, photorealism, food deformation, flame/particles, fluids, garments, articulation, multi-material, teleop, low-cost robot).

### Simulation benchmark (Table II; 50 demos per task, 100 trials)

| Task | ACT | Diffusion Policy | SmolVLA | π0 |
|---|---:|---:|---:|---:|
| Fold Garment | 45 | 30 | **70** | 44 |
| Assemble Burger | **78** | 35 | 40 | 39 |
| Fling Garment | 25 | 20 | **36** | 14 |
| Cut Sausage | 77 | **93** | 90 | 75 |
| Pour Coffee | **80** | 30 | 40 | 40 |
| Wipe Surface | 60 | 30 | 60 | 60 |

Flinging is hard for everyone; the language-conditioned VLAs win only the garment tasks; ACT wins the rigid-ish ones.

### Real-world co-training (Table III; dual-arm LeRobot, 10 real demos)

| Task | ACT real-only → sim+real | SmolVLA real-only → sim+real |
|---|---|---|
| Fold Garment | 2/10 → 5/10 | 2/10 → 4/10 |
| Assemble Burger | 2/10 → 4/10 | 1/10 → 4/10 |
| Wipe Surface | 1/10 → 7/10 | 1/10 → 6/10 |

"On average, the success rate improves from about 15% to about 50%." Ten trials per cell.

## Reading it against the wiki

- **The low-cost-robot commitment is the interesting choice.** A simulator that ships XLeRobot and LeKiwi as first-class embodiments is the first the wiki has seen aimed at the [LeRobot](../entities/lerobot.md) tier rather than Franka; it is the reason the LeHome Challenge could run on SO-ARM101-class hardware.
- **The co-training result is the practitioner's number**, and it matches [Larchenko](larchenko-learning-to-fold-tech-report.md)'s experience from the other side: sim helps most when real data is ~10 episodes. Ten trials per cell means each entry has a ±15-point band ([audit](../syntheses/platforms/vla-success-rate-audit.md)); the *direction* holds across six cells, the magnitudes do not individually.
- **Garment simulation fidelity is asserted, not measured.** No sim-vs-real dynamics comparison is given for cloth; the wiki's [sim-to-real](../concepts/learning/sim-to-real-transfer.md) page already carries Larchenko's renderer-overfit diagnostics for this exact simulator, which is the closer look.

## Entities mentioned

- [LeHome Challenge 2026](../entities/lehome-challenge-2026.md), [XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md), [LeRobot](../entities/lerobot.md), [SmolVLA](../entities/smolvla.md), [π0](../entities/pi-zero.md), [Diffusion Policy](../entities/diffusion-policy.md), [RoboTwin](../entities/robotwin.md), [LIBERO](../entities/libero.md), [BEHAVIOR-1K](../entities/behavior-benchmark.md) (comparison table).
- Lightwheel (commercial simulation partner; no page).

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [world-model simulators](../concepts/world-models/world-model-simulators.md) (the physics-engine side), [imitation learning](../concepts/learning/imitation-learning.md).

## Open questions

- Where the challenge protocol is documented, if anywhere beyond competitor reports.
- Cloth-parameter identification against real garments — none reported.
- The underlying engine and rendering stack are never named explicitly.
