---
title: Open Duck Mini
type: entity
subtype: robot
created: 2026-08-27
updated: 2026-08-27
sources: 2
tags: [open-duck-mini, antoine-pirrone, bdx-droid, biped, open-source, 3d-printed, rl, pollen-robotics, microduck, gemma4]
---

**Repo:** [`apirrone/Open_Duck_Mini`](https://github.com/apirrone/Open_Duck_Mini) — *"Making a mini version of the BDX droid."* Apache-2.0, **3,546 stars**, last pushed 2026-01-31.

**Open Duck Mini (ODM)** — an open-source, 3D-printable bipedal robot by **Antoine Pirrone**, built as a miniature of Disney's **BDX droid**, **~35 cm tall with legs extended**. The direct ancestor of [Microduck](microduck.md), and the robot Google chose as the vehicle for its on-device Gemma 4 demo at I/O 2026.

The repo is candid about its own state: *"This project is still a work in progress"*, assembly guide *"TODO"*, and the alpha *"is not very easy to build, has some mechanical problems (**too much play at some joints**)."*

## Build

| | |
|---|---|
| Height | ~35 cm, legs extended |
| Cost | v2 target *"aiming for ~$500"* (repo, Dec 2024); secondary coverage says ~$400 — **unsettled** |
| Servos | **Dynamixel XC330-M288-T** in the legs — switched up from XL330-M288-T, *"more expensive, but way more powerful"* |
| Onboard compute | **Raspberry Pi Zero 2W** ([Open_Duck_Mini_Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime)) |
| CAD | Onshape, public documents |
| Licence | Apache-2.0; STL + BOM published |

> [!note] The Pi 5 in the Gemma demo is not the robot's brain
> ODM's locomotion runtime targets a **Pi Zero 2W**. The Raspberry Pi 5 and [Jetson Orin Nano](jetson-orin-nano.md) in the Google I/O demo were carrying the **LLM**, not the control loop. Two different computers doing two different jobs — a distinction the [secondary coverage](../sources/explainx-gemma-4-open-duck-mini.md) collapses by listing "Raspberry Pi 5 (8GB) recommended" as the project's compute.

## The Open Duck Project's RL lineage

Pirrone maintains a small ecosystem beyond the main repo:

- **[Open_Duck_Playground](https://github.com/apirrone/Open_Duck_Playground)** (177 stars) — *"Open Duck Project's Mujoco playground RL environments"*
- **[Open_Duck_reference_motion_generator](https://github.com/apirrone/Open_Duck_reference_motion_generator)** (113 stars)
- **[Open_Duck_Mini_Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime)** (154 stars)

The training substrate migrated across three generations: **Isaac Gym + [AWD](https://github.com/rimim/AWD)** (v1, with sim2sim Isaac to MuJoCo) then **[MuJoCo Playground](mujoco-playground.md)** (Open_Duck_Playground) then **[mjlab](mjlab.md)** (Microduck). Actuator identification used **Rhoban's [BAM](https://github.com/Rhoban/bam)** from the start.

## The Microduck lineage, now primary-confirmed

The [Microduck launch ingest](../sources/pollen-robotics-microduck.md) recorded the Open Duck Mini connection as *likely-but-secondary*, because no Pollen primary mentions it. Two primaries now close most of that gap:

- **GitHub** lists `apirrone` as **Antoine Pirrone**, company **Pollen Robotics**, *"R&D Engineer at @pollen-robotics"*, and a member of **team Rhoban**.
- Pirrone is a **credited author of the [Microduck launch post](../sources/pollen-robotics-microduck.md)**.

A third piece closes it further. **Pollen's own repo names Pirrone's personal repo as the provenance of the shipped policies**: `policies/README.md` in [`pollen-robotics/microduck`](../sources/microduck-runtime-repo.md) states the ONNX files were *"copied from `apirrone/microduck_runtime` at commit `5f3b314`."* And Pirrone's GitHub account currently holds `microduck_app`, `microduck_sounds`, `microduck_kinematics_rs`, `microduck_pet_detect` and `microduck_maploc_rs`, pushed July–August 2026, sitting directly alongside `Open_Duck_Mini_Runtime`.

So the descent is **documented through the shared author's repositories and Pollen's own provenance table**, not merely inferred from press coverage. What is still absent is any Pollen *marketing* acknowledgement — no launch material names Open Duck Mini.

> [!note] Rhoban closes a loop
> Pirrone's membership of **team Rhoban** explains an otherwise-unremarked dependency: `microduck_rl` models its servos with **BAM**, *"better actuator models, by Rhoban"*, and exports MJCF via Rhoban's `onshape-to-robot`. The [actuator-fidelity](../concepts/learning/actuator-fidelity-sim2real.md) approach that makes Microduck's sim-to-real work arrives through the same person as the robot's shape.

## Versus Microduck

| | Open Duck Mini v2 | [Microduck](microduck.md) |
|---|---|---|
| Form | **~35 cm** (repo) | 25 cm |
| Acquisition | 3D-print + source parts (~$400–500) | **$399 assembled** |
| Hardware files | published (STL, BOM) | **not** open-source hardware; design files CC BY-SA-NC |
| Software | Apache-2.0 | Apache-2.0 |
| Control compute | **Raspberry Pi Zero 2W** | fixed: Rockchip RK3566 |
| Beak | decorative | **articulated gripper** |
| Servos | Dynamixel **XC330** (legs) | Dynamixel **XL330** |
| Training | Isaac Gym/AWD, then MuJoCo Playground | [mjlab](mjlab.md) (MuJoCo Warp) |
| Policies | community | 7 shipped, published + retrainable |

Pollen's own framing of the price is the honest summary: same rough cost, **no printer required**.

> [!note] A mechanical complaint became a simulated phenomenon
> ODM's README lists *"too much play at some joints"* among the alpha's mechanical problems. [Microduck](microduck.md)'s RL stack models **±1° of gear play as an unactuated hinge in series with every servo**, with observations reading *through* the backlash ([actuator fidelity](../concepts/learning/actuator-fidelity-sim2real.md)). The defect the predecessor apologised for is the thing the successor trains against — the more durable answer, since the play does not go away at this price point.

## The Gemma 4 demo (Google I/O 2026)

Two ODM v2 units ran **Gemma 4 E2B entirely on-device** — one on a Raspberry Pi 5, one on a [Jetson Orin Nano](jetson-orin-nano.md) — with microphone, camera, speaker and LED antennas, at Google's *"Gemma Playground"* installation ([Google's post](https://x.com/googlegemma/status/2057142732494352689); [Google for Developers video](https://www.youtube.com/watch?v=pLwB_63yUBY)). One duck named itself *"Autumn"* — ODM, phonetically.

Worth noting what it was **not**: the ducks did not walk. Walking is listed as a *next step*, so the highest-profile Open Duck Mini appearance to date used it as a conversational head — on a robot whose upstream purpose is legged RL. The two halves of the duck story, locomotion and language, have not yet met on the same machine.

Performance reality-check, from [Google's own LiteRT benchmarks](../sources/gemma-4-e2b-model-card.md): on a Pi 5 the model decodes at **7.6 tok/s**, so a ~45-token spoken answer takes about **six seconds**; the Orin Nano's GPU does it in under two. The [secondary coverage](../sources/explainx-gemma-4-open-duck-mini.md) calls both ducks *"very snappy"* and distinguishes neither.

## Related

- [Microduck](microduck.md) — the commercial descendant
- [Pollen Robotics](pollen-robotics.md) — Pirrone's employer
- [Gemma 4](gemma4.md) — the on-device model in the I/O demo
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md) — the Rhoban BAM lineage

## Mentioned in

- [Gemma 4 Powers Open Duck Mini (explainx.ai)](../sources/explainx-gemma-4-open-duck-mini.md) — the I/O demo, with corrections.
- [Gemma 4 E2B model card + LiteRT benchmarks](../sources/gemma-4-e2b-model-card.md) — what the demo hardware actually delivers.
