---
title: "TuragaLab/flybody (GitHub)"
type: source
subtype: code-repository
url: https://github.com/TuragaLab/flybody
author: Vaxenburg et al. (TuragaLab + Google DeepMind)
published: 2024-2025
ingested: 2026-05-08
license: Apache-2.0
tags: [flybody, mujoco, dm-control, drosophila, deep-rl, dmpo, acme, ray, open-source]
---

## Summary

Official open-source release of [flybody](../entities/flybody.md) — the anatomically detailed *Drosophila melanogaster* body model + RL training infrastructure described in [Vaxenburg et al. 2025](flybody-paper.md). Apache-2.0 licensed; jointly maintained by HHMI Janelia (Turaga lab) and Google DeepMind. Downloadable XML body model, dm_control task environments, and Ray-distributed DMPO training scripts.

## Key contents

### Body model files
- **`fruitfly.xml`** — the standalone MuJoCo XML body model. Drag-and-drop into MuJoCo's `simulate` viewer for interactive inspection.
- **`floor.xml`** — minimal floor scene wrapping the body.

### Task environments (dm_control format)
- **Walking imitation** — 59-dimensional action space.
- **Flight imitation** — wing pattern generator + MLP corrective signal.
- **Vision-guided flight** — bumps + trench tasks with simulated eye cameras.
- Random-policy rollout example: `env.step(action)` over the dm_control TimeStep interface.

### Training stack
- **`mujoco`**, **`dm_control`** — core physics + environment glue.
- **TensorFlow + Acme** — DMPO agent (optional ML extension). Acme is DeepMind's RL research framework.
- **Ray** — distributed actor-learner parallelism (optional Ray extension).
- "Distributed RL training script…uses Ray to parallelize the DMPO agent training."

### Install
- Conda-based, **Python 3.10**. Three install tiers: core (model only), `+ml` (TF + Acme), `+ray` (distributed training).

## Entities mentioned

- [flybody](../entities/flybody.md) — the simulator/body model itself.
- [HHMI Janelia](../entities/hhmi-janelia.md) — TuragaLab home.
- [Google DeepMind](../entities/google-deepmind.md) — co-developer; DMPO and Acme upstream.
- [MuJoCo](../entities/mujoco.md) — physics engine.
- [DM Control](../entities/dm-control.md) — environment / control API.

## Concepts touched

- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — the open-source artifact for fly biomechanics.
- [Imitation learning](../concepts/learning/imitation-learning.md) — DMPO imitation against real-fly kinematics.

## Open questions

- **No FlyWire/connectome integration in the repo.** Brain-side wiring is acknowledged in the paper's Discussion but not part of the released code.
- **No MJX port** advertised in the README. Training is CPU-distributed via Ray, not GPU-batched via MJX.
- **Pretrained policy weights** — the README references pretrained controllers but availability and reproducibility status are not nailed down here; would benefit from a deeper repo dive.
