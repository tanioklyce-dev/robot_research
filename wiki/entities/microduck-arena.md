---
title: Microduck Arena
type: entity
subtype: benchmark
created: 2026-10-24
updated: 2026-10-24
sources: 2
tags: [microduck-arena, microduck, pollen-robotics, hugging-face, leaderboard, benchmark, evaluation, reproducibility, onnx]
---

# Microduck Arena

**Microduck Arena** — [Pollen Robotics](pollen-robotics.md)' public **simulation leaderboard** for [Microduck](microduck.md) locomotion policies. It runs as a Hugging Face Space ([`pollen-robotics/microduck-arena`](https://huggingface.co/spaces/pollen-robotics/microduck-arena)) from the GitHub repo of the same name. Entrants submit an ONNX policy and the Space races it server-side on fixed courses ([repo](../sources/microduck-arena-github.md)).

## How it works ([repo](../sources/microduck-arena-github.md))
- **Contract**: 61-D observation in, 14-D action out, ≤64 MiB. This is the same check the robot's `robotd` applies, so *"a policy the Arena accepts will load there too."* Any training stack qualifies: Pollen's [mjlab](mjlab.md) recipe, or [Isaac Lab](nvidia-isaac-lab.md)'s since 2026-10 ([NVIDIA/HF tutorial](../sources/hf-nvidia-microduck-isaac-lab-sim-to-real.md)).
- **Events**: `sprint-2m` (legs, 0.25 m/s), `roller-sprint-2m` (rollers, 0.6 m/s) and `hill-climb-1m5` (8° slope), plus timeline-driven "stage" events.
- **Scoring**: mean finish time over **five perturbed starts**, with failures counted at the time limit, so consistency beats occasional speed. The replay shown is the median run.
- **Provenance**: policies live in the entrant's own Hub repo and are raced at a pinned revision. The board can be rebuilt by **re-racing**, never by trusting stored times.

## Why it is interesting
The Arena treats **simulator reproducibility as a first-class engineering problem**. Pollen states the servo model is chaotic enough that runs diverge across CPU architectures within seconds of sim time. So only the Space's x86_64 times count, and the Space's build **fails if a golden run doesn't reproduce**. That is a candid admission of what high-fidelity, friction-heavy [actuator modelling](../concepts/learning/actuator-fidelity-sim2real.md) costs. Most benchmarks in this wiki report numbers without saying where they would stop reproducing.

It is also the first **community leaderboard attached to a purchasable robot** in this wiki, with season points, podiums and auto-rendered social clips (HF Jobs, about a cent each).

> [!note] A measured baseline, not a flattering one
> The shipped reference policy tracks about **44%** of commanded velocity and does not walk below about **0.2 m/s** commanded, and Pollen says both figures are measured ([repo](../sources/microduck-arena-github.md)).

## Open questions
- What physics engine the Arena rig (vendored from `pollen-robotics/microduck-simulator`) runs.
- Whether Arena rank predicts real-robot performance.
- How Isaac-Lab-trained walkers score here compared with mjlab-trained ones. It is a ready-made cross-simulator transfer test that nobody has published.

## Related
- [Microduck](microduck.md) — the robot
- [Pollen Robotics](pollen-robotics.md), [Hugging Face](hugging-face.md) — maker and host
- [mjlab](mjlab.md) — the Arena's native training stack (`Mjlab-Sprint2m-MicroDuck`)
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — second stack whose exports qualify

## Mentioned in
- [pollen-robotics/microduck-arena — README and guide](../sources/microduck-arena-github.md)
- [Train in Simulation, Deploy on a Real Robot: Microduck with Isaac Lab 3.0](../sources/hf-nvidia-microduck-isaac-lab-sim-to-real.md) — points Isaac Lab users at the Arena for comparison.
