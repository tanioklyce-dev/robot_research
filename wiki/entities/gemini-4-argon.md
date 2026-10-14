---
title: Gemini 4 Argon
type: entity
subtype: model
created: 2026-10-13
updated: 2026-10-13
sources: 1
tags: [gemini-4-argon, gemini, google-deepmind, frontier-model, embodied-reasoning, erqa, code-as-policy, real-to-sim, mujoco, physical-agi]
---

**Gemini 4 Argon** (`gemini-4-argon`) is Google's Gemini 4-generation frontier model, launched 2026-10-13. Google presents it as a general model that is also a **"general-purpose physical reasoning model"** for the whole robotics lifecycle ([Argon robotics blog](../sources/gemini-4-argon-robotics-blog.md)). It is **not part of the [Gemini Robotics](gemini-robotics.md) line** and does not emit motor actions. It reaches robots by writing code, calling primitives, authoring simulations, and prompting other models.

## Capabilities (vendor-stated)

- **ERQA 87%** "using pure reasoning", stated to beat every other frontier model. No competitor table is given. The highest ERQA figures elsewhere in the wiki are 77.7 and 65.2 for frontier API models in [Unitree's tests](../sources/unifolm-wla-1-project-page.md), measured on a different harness.
- **Control through code**: a [code-as-policies](../concepts/agents/code-as-policy.md) primitive API reached by `curl`, with a calibrated, annotated wrist image. The model chooses its own call granularity, from coarse to fine visual servoing. [Spot](spot.md) mobile manipulation uses a skill and a "2-agent verification swarm."
- **Simulation authoring**: MuJoCo / [mujoco_warp](mujoco-warp.md) twins built from robot logs (matched on fingertip contact force), from egocentric human video (retargeted to a 76-DoF humanoid) and from a paper sketch ([Apollo 2](apptronik-apollo.md) throw). See [real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md).
- **Data work**: four-level hindsight annotation, with fumbles downweighted 0.15–0.25× for BC; dense value/progress estimation on [UMI](umi.md) video; **sim data generation that lifts an unnamed VLA from 56% to 75% real success** (n not given).
- **Hardware self-improvement** on an [SO-101](so-arm101.md): 58.9 → 22.9 → 17.4 s over three iterations.
- **Video world-model steering**: iterative prompting of Google's "Gemini Omni" world model.

## Access
Google AI Studio (AI Ultra), the paid Gemini API (Interactions API), and Google Antigravity (AI Ultra).

## Position in the landscape

- **A general model takes the orchestrator slot.** In July 2026, Google billed [Gemini Robotics ER 2](gemini-robotics.md) as "the robot's high-level brain." Three months later a general frontier model reports a higher embodied-reasoning score than any ER figure the wiki holds and demonstrates orchestration, simulation and labeling besides. The ER line is not mentioned. This repeats the [CaP lineage](../concepts/agents/code-as-policy.md)'s recurring pattern, in which general models absorb what specialised wrappers did. The source does not say whether ER 2 is being superseded.
- **The bet is code + simulation, not end-to-end actions.** Every Argon hardware demo runs through a primitive API. Google's own [VLA](gemini-robotics.md) remains the action path. Argon makes the data, environments and evaluations that feed it.

> [!note] Demonstrations, not evaluations
> Every claim above except ERQA comes from a single showcased run. See the [source page](../sources/gemini-4-argon-robotics-blog.md#reading-it-critically).

## Related
- [Gemini Robotics](gemini-robotics.md) — the robot-specific family Argon sits beside.
- [Google DeepMind](google-deepmind.md) · [MuJoCo](mujoco.md)
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) · [Code world model](../concepts/world-models/code-world-model.md): writing executable environments, here as MuJoCo XML instead of OpenSpiel Python.

## Mentioned in
- [Gemini 4 Argon for Robotics (Google Developers Blog)](../sources/gemini-4-argon-robotics-blog.md)

## Open questions
- ERQA competitor numbers and harness; any manipulation success rates with n.
- The relationship to Gemini Robotics ER 2 and to the VLA line (distillation source?).
- Model size, price, latency.
