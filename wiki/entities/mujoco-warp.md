---
title: MuJoCo Warp
type: entity
subtype: product
created: 2026-08-27
updated: 2026-08-27
sources: 0
tags: [mujoco-warp, mjwarp, mujoco, newton, gpu-simulation, nvidia-warp, google-deepmind, nvidia, rl, mjlab]
---

**Repo:** [`google-deepmind/mujoco_warp`](https://github.com/google-deepmind/mujoco_warp) — Apache-2.0, 1,420★, created 2025-03-17 · `pip install mujoco-warp` · [docs](https://mujoco.readthedocs.io/en/latest/mjwarp/index.html)

**MuJoCo Warp (MJWarp)** — a **GPU-accelerated implementation of [MuJoCo](mujoco.md)** built on NVIDIA Warp, *"designed for NVIDIA hardware… high-throughput, accurate simulation for robotics research."* Requires an NVIDIA GPU for fast simulation but supports CPU for development and debugging.

> [!note] Jointly maintained, and part of Newton
> *"MJWarp is maintained by **Google DeepMind** and **NVIDIA** as part of the [Newton](newton-physics-engine.md) project."* That places it in an unusual position: it is simultaneously **MuJoCo's GPU backend** and **a component of NVIDIA's Newton physics engine** — so the DeepMind and NVIDIA simulator lines that this wiki otherwise tracks as competing stacks share this piece.

## Why it exists alongside MJX

[MuJoCo](mujoco.md) already had a GPU story in **MJX**, the JAX-accelerated variant that [MuJoCo Playground](mujoco-playground.md) is built on. MJWarp is the second attempt, on NVIDIA Warp rather than JAX, and it is the one the newer stacks have adopted:

| | Backend | Built on it |
|---|---|---|
| **MJX** | JAX | [MuJoCo Playground](mujoco-playground.md) (Brax PPO/SAC) |
| **MJWarp** | NVIDIA Warp | **[mjlab](mjlab.md)** (`rsl_rl` PPO), Newton |

Capability breadth is claimed well past rigid-body: *"rigid bodies with contacts, soft bodies, cloth, signed distance fields, and more."* Nightly public benchmarks are published, with [Unitree G1](unitree-g1.md) flat-terrain and heightfield locomotion among the reference scenes — a hint at where the maintainers expect it to be used.

## Where it shows up in this wiki

- **[mjlab](mjlab.md)** is *"Isaac Lab API, powered by MuJoCo-Warp, for RL and robotics research"* — the repo's own description. So the [Isaac Lab](nvidia-isaac-lab.md) ergonomics that mjlab offers sit directly on MJWarp.
- **[Microduck](microduck.md)**'s seven shipped policies were trained through that chain: MJWarp → mjlab → PPO → ONNX → a 50 Hz loop on an RK3566. This is the wiki's only case of a **shipping consumer robot** whose policies trace back to MJWarp, and the whole training stack is public.
- **[Newton](newton-physics-engine.md)** — MJWarp is a component, which is how [MuJoCo Playground](mujoco-playground.md) also came to list Newton as an optional backend.

## Related

- [MuJoCo](mujoco.md) — the simulator it accelerates
- [MuJoCo Playground](mujoco-playground.md) — the MJX-based sibling
- [Newton physics engine](newton-physics-engine.md) — the project it is part of
- [mjlab](mjlab.md) — the RL framework built on it
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — the API mjlab reimplements over MJWarp
- [Microduck](microduck.md) — shipped policies trained on this stack

## Mentioned in

- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md) — the training substrate under [mjlab](mjlab.md); ~1–2 h at 4096 parallel envs for a usable biped gait.

## Open questions

- **No throughput numbers ingested.** Nightly benchmarks are published by the project; nothing in this wiki quotes steps/sec for MJWarp against MJX or [Isaac Lab](nvidia-isaac-lab.md), which is the comparison anyone choosing a stack actually needs.
- **Why the field moved off MJX** for new work ([mjlab](mjlab.md), Newton) is undocumented here — JAX-vs-Warp ergonomics, contact-model differences, or NVIDIA's involvement are all plausible and none is sourced.
