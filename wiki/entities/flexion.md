---
title: Flexion Robotics
type: entity
subtype: company
created: 2026-08-13
updated: 2026-08-13
tags: [flexion, humanoid, autonomy-stack, sim2real, reinforcement-learning, isaac-lab, zurich, reflect, niantic-spatial]
sources: 3
---

**Flexion Robotics** — Zürich-based company building *"the **autonomy stack** for humanoid robots — from command to control, from manipulation to locomotion, **across any hardware and task**. Leveraging the power of simulation and reinforcement learning, our software scales to the real world with **minimal human involvement**."* Tagline: *"Complex intelligence for simple human tasks."* [flexion.ai](https://flexion.ai/).

## Position — the software layer, deliberately not the robot

Flexion sells **policies and deployment software**, not hardware, and states hardware-agnosticism as a design goal. That places it in a slot this wiki has few entries for: **[Physical Intelligence](physical-intelligence.md)** is the closest (policies as the product), but PI's route is large-scale real teleoperation while Flexion's is **simulation + RL with minimal human involvement** — an explicitly *data-light* bet against the demonstration-collection economics that dominate this wiki's manipulation coverage.

## What is on the record

| Date | Item |
|---|---|
| 2026-07-20 | **[Niantic Spatial, Flexion, and NVIDIA: Closing the Sim2Real Gap for Humanoids](../sources/niantic-flexion-nvidia-sim2real.md)** — ingested |
| 2026-06-29 | **Flexion Reflect v1.0** — *"The Path Towards Long-Horizon Autonomous Humanoid Work"* — un-ingested |
| 2025-11-20 | **Flexion Reflect v0** — *"Towards Generalizable Robot Autonomy"* — un-ingested |

Hiring in Zürich, including *"Research Engineer — Generative Humanoid Motion Generation."*

## What the ingested source establishes

In the [Niantic/NVIDIA collaboration](../sources/niantic-flexion-nvidia-sim2real.md), Flexion owns the **sim2real half**: an **RGB-only local-navigation policy** taking camera + proprioception + goal-in-own-frame and emitting a **velocity command**, with a **separate pre-trained locomotion policy** below it converting that to motion. Trained by massively parallel RL inside a Gaussian-splat reconstruction on a single GPU; bridged to reality with **domain randomization plus large-scale offline-trained image encoders** that run both in training and onboard at deployment.

**Results**: zero-shot transfer to a real humanoid in a real office, robust to rearranged furniture; and in simulation at **n=1,024 with matched poses**, RGB-in-3DGS **97.8% vs 93.8%** (easy scene) and **75.0% vs 70.9%** (hard) against a depth baseline — both statistically separating.

> [!warning] "Across any hardware and task" versus a site-specific policy
> The site claims hardware- and task-generality. The ingested demonstration is the opposite kind of thing: a policy **deliberately specialised to one building**, trained inside a digital twin of that building, argued for on the grounds that *"specialization unlocks capability."*
>
> These are reconcilable — the *stack* could be general while each *deployed policy* is site-tuned, which is a coherent product story and arguably the point of making capture cheap. But **the wiki should not read the marketing claim as evidenced by the demonstration**; only the site-specific result is on the record.

> [!note] The bet worth watching
> Almost everything else this wiki tracks in manipulation is **data-bound** — [X-VLA](x-vla.md)'s 1,200 curated cloth-folding episodes, [UME](ume.md)'s 26–157 torque-instrumented demos, [π0](pi-zero.md)'s ~10,000 teleoperation hours. Flexion's stated route is **simulation and RL with minimal human involvement**, which if it holds for manipulation rather than just locomotion and navigation would sidestep the bottleneck the rest of the field is fighting. **The ingested evidence covers navigation only** — the easier case, and the one where sim2real has worked for years.

## Related

- [Niantic Spatial](niantic-spatial.md) — supplies the reconstructed training world; [the collaboration](../sources/niantic-flexion-nvidia-sim2real.md)
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) / [Isaac Sim](nvidia-isaac-sim.md) — the simulator
- [Physical Intelligence](physical-intelligence.md) — the other policies-as-product company, betting on real data instead
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) · [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md)

## Open questions

- **Which humanoid?** Never named in the ingested source — no hardware, DoF, or cost.
- **Reflect v0 and v1.0 are un-ingested**, and their titles (*"long-horizon autonomous humanoid work"*, *"generalizable robot autonomy"*) suggest they carry the manipulation and generality claims the navigation demo does not.
- **No real-world success rate anywhere** — the 1,024-rollout rigour is simulation-only; the physical transfer is shown qualitatively.
- **Funding, size, founding** — not established by anything read here.

## Mentioned in

- [Niantic Spatial, Flexion, and NVIDIA: Closing the Sim2Real Gap for Humanoids](../sources/niantic-flexion-nvidia-sim2real.md)
