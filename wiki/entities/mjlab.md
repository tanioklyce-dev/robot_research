---
title: mjlab
type: entity
subtype: product
created: 2026-08-27
updated: 2026-08-27
sources: 1
tags: [mjlab, mujoco, mujoco-warp, rsl-rl, ppo, rl, sim-to-real, locomotion, training-framework]
---

**Repo:** [`mujocolab/mjlab`](https://github.com/mujocolab/mjlab)

**mjlab** — an RL training framework built on **MuJoCo Warp** with **`rsl_rl`** as the algorithm library (PPO). It occupies the same niche as [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — massively parallel GPU environments, task-config registry, train/play/export CLI — but on the MuJoCo side of the fence rather than the PhysX/Newton side.

> [!note] Thin page
> Entered the wiki as the training substrate under [Microduck](microduck.md) ([launch bundle](../sources/pollen-robotics-microduck.md)). mjlab's own repo and docs have not been ingested; everything below is observed through the `microduck_rl` codebase.

## Position among MuJoCo training stacks

| | Backend | Algorithms | Origin |
|---|---|---|---|
| **mjlab** | MuJoCo **Warp** | `rsl_rl` (PPO) | mujocolab |
| [MuJoCo Playground](mujoco-playground.md) | MuJoCo **MJX** (JAX), optional Warp/[Newton](newton-physics-engine.md) | Brax PPO/SAC | Google DeepMind |
| [Isaac Lab](nvidia-isaac-lab.md) | PhysX / Newton | rsl_rl, RL-Games, SKRL | NVIDIA |

The naming convention in `microduck_rl` (`Mjlab-Velocity-Flat-MicroDuck`, env-cfg modules per task family, `ENABLE_*` domain-randomization toggles, `train` / `play` / `export.py` entry points) is recognisably **Isaac Lab's ergonomics ported onto MuJoCo Warp** — which is what makes it a plausible landing spot for teams who want Isaac Lab's structure without the NVIDIA stack.

## Observed capabilities ([via Microduck](../sources/pollen-robotics-microduck.md))

- CUDA GPU required; **4096 parallel envs** is the working default, ~1–2 h to a usable biped gait.
- Custom actuator classes are first-class — `microduck_rl` subclasses the actuator to implement the [BAM](dynamixel.md) voltage-level model plus friction domain randomization.
- MJCF-native, so Onshape → `onshape-to-robot` → MJCF is a supported authoring path, and per-task collision-geometry variants of the same robot are just different XML files.
- **ONNX export with the observation normalizer baked into the graph** — the deploy artefact is self-contained.
- Runs headless on **Hugging Face Jobs** (`microduck_rl` ships the submission wrapper), which makes a GPU-less laptop a viable development machine for GPU-scale RL.

## Related

- [MuJoCo Warp](mujoco-warp.md) — the GPU physics backend it runs on
- [MuJoCo](mujoco.md) — the physics engine
- [MuJoCo Playground](mujoco-playground.md) — the DeepMind equivalent
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — the structural template
- [Microduck](microduck.md) — the first shipped consumer robot in this wiki trained on it
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)

## Mentioned in

- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md)
