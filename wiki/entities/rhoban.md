---
title: Rhoban
type: entity
subtype: lab
created: 2026-08-27
updated: 2026-08-27
sources: 0
tags: [rhoban, labri, bordeaux, robocup, humanoid, open-source, bam, onshape-to-robot, actuator-modeling]
---

**Site:** [rhoban.com](http://www.rhoban.com/) · **GitHub:** [`Rhoban`](https://github.com/Rhoban) (98 repos)

**Rhoban** — the autonomous-robotics research group of **LaBRI**, the computer science laboratory of **Bordeaux University, ENSEIRB-MATMECA and CNRS**. Self-described interests: *"Humanoid Autonomous Robots, and in particular RoboCup"* plus agricultural robotics. **RoboCup champion four times** (humanoid league); platforms include **SigmaBan** and **UltraBan**, *"a human-sized humanoid robot."* Funded by Bordeaux University (Ambassador / Sysnum IdEx), Région Nouvelle-Aquitaine, ANR, CNRS and ENSEIRB-MATMECA.

> [!note] Why an academic lab has an entity page here
> Rhoban is not ingested as a research subject. It earns a page because **its tooling is load-bearing under other pages in this wiki** — the actuator model that makes [Microduck](microduck.md)'s sim-to-real work, and the CAD-to-simulator path that both [Microduck](microduck.md) and [Open Duck Mini](open-duck-mini.md) use — and because it is the third node in a small **Bordeaux robotics cluster** this wiki keeps running into.

## The tooling that matters here

| Repo | ★ | What it does |
|---|---|---|
| [`onshape-to-robot`](https://github.com/Rhoban/onshape-to-robot) | 594 | Onshape assembly → **URDF, SDF, MuJoCo** via the Onshape API. MIT. The CAD-to-simulator path in `microduck_rl` and Open Duck Mini. |
| [`placo`](https://github.com/Rhoban/placo) | 360 | "Rhoban Planning and Control" |
| [`bam`](https://github.com/Rhoban/bam) | 287 | *"Identify and simulate extended friction models for servo-actuators."* Apache-2.0. |
| [`microban`](https://github.com/Rhoban/microban) | 212 | *"Affordable, fully 3D-printable, 100% open-source humanoid"* |
| [`Plater`](https://github.com/Rhoban/Plater) | 294 | 3D-printer parts placer / plate generator |

### BAM, and why it is the interesting one

**BAM** is the actuator-identification framework behind this wiki's [actuator-fidelity](../concepts/learning/actuator-fidelity-sim2real.md) coverage. Its **M6 model** of the [Dynamixel](dynamixel.md) XL330 — voltage control law, back-EMF, and Coulomb / Stribeck / load-dependent friction — is what `microduck_rl` uses instead of an ideal PD, on the argument that *"at this scale, actuator fidelity is most of the sim2real gap"* ([Microduck launch](../sources/pollen-robotics-microduck.md)).

That a **RoboCup humanoid lab** produced it is not incidental. Kid-size RoboCup humanoids run cheap hobby servos under real dynamic load with no budget for research-grade actuators — precisely the regime where the ideal-PD assumption fails and where identifying the real friction curve pays.

## The Bordeaux cluster

Three organisations in one city keep appearing together in this wiki:

- **Rhoban** — LaBRI / Bordeaux University; BAM, `onshape-to-robot`, RoboCup humanoids.
- **[Pollen Robotics](pollen-robotics.md)** — founded 2016 in Bordeaux by former Inria researchers; [Hugging Face](hugging-face.md)'s robotics team since April 2025.
- **[Open Duck Mini](open-duck-mini.md)** → **[Microduck](microduck.md)** — **Antoine Pirrone** is a Rhoban member *and* a Pollen R&D engineer, and is the connective tissue: the ODM/Microduck lineage carries Rhoban's tooling into a shipping consumer product.

So the actuator model that makes a $399 robot's policies transfer arrives through the same person as the robot's shape. Worth noting for anyone reading the wiki's low-cost-platform cluster as a purely Hugging Face story — a university RoboCup lab supplied a load-bearing piece of it.

## Related

- [Open Duck Mini](open-duck-mini.md) · [Microduck](microduck.md) — downstream users of BAM and `onshape-to-robot`
- [Pollen Robotics](pollen-robotics.md) — Bordeaux neighbour, shares a person
- [Dynamixel](dynamixel.md) — the servo class BAM's M6 model targets
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md) — the concept BAM instantiates
- [MuJoCo](mujoco.md) — one of `onshape-to-robot`'s export targets

## Mentioned in

- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md) — BAM M6 on the XL330; `onshape-to-robot` for MJCF export.
- [Gemma 4 Powers Open Duck Mini (explainx.ai)](../sources/explainx-gemma-4-open-duck-mini.md) — Pirrone's Rhoban membership, via his GitHub profile.

## Open questions

- **No Rhoban publication ingested.** The group has a publications page; the BAM paper in particular would strengthen [actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md) from one worked example to a method with a citation.
- **`placo`** (planning and control) is unexamined and may be relevant to the wiki's [whole-body control](../concepts/robotics/whole-body-control.md) coverage.
- **`microban`** — a 3D-printable open humanoid from the same lab, unassessed here.
