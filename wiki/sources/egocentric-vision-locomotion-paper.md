---
title: "Legged Locomotion in Challenging Terrains using Egocentric Vision"
type: source
url: https://arxiv.org/abs/2211.07638
local_path: raw/2211.07638v1.pdf
sha256: 42f9f9cd4087c85e6aaf6a910726fe7945886b5bf01dfed83b7fc3b603ddc60e
author: Ananye Agarwal (CMU), Ashish Kumar (UC Berkeley), Jitendra Malik (UC Berkeley), Deepak Pathak (CMU) — equal contribution / equal advising
published: 2022-11-14
ingested: 2026-08-29
venue: CoRL 2022 (6th Conference on Robot Learning, Auckland); PMLR v205
format: PDF (17 pp., arXiv:2211.07638v1)
project_page: https://vision-locomotion.github.io
tags: [egocentric-vision, locomotion, quadruped, unitree-a1, depth-camera, privileged-distillation, scandots, dagger, sim-to-real, isaacgym, legged-gym, cmu, berkeley]
---

# Legged Locomotion in Challenging Terrains using Egocentric Vision

## Summary

**The answer to the limitation [RMA](rma-paper.md) closed on.** RMA ended by saying a blind robot fails on stairs and rocks and that *"we need to use not just proprioception but also exteroception with an onboard vision sensor."* One year later, three of its four authors published exactly that.

This is claimed as the **first end-to-end locomotion system to traverse stairs, curbs, stepping stones and gaps** from a **single front-facing depth camera** — no elevation map, no foothold planner, no metric localization, no MPC. Depth and proprioception go in, target joint angles come out at 50 Hz, in one feedforward pass on the robot's onboard compute.

The design argument is biological and load-bearing. Humans do not look at the ground beneath their feet; they look a few steps ahead and hold a **short-term memory** that persists until the foot arrives. A forward-facing camera on a quadruped has the same problem in a sharper form — **it structurally cannot see under the robot's own hind feet** — so memory is not an optimization, it is a requirement of the sensor placement. The policy is recurrent for that reason.

## Key claims

### The two-phase recipe, and why it exists

Rendering depth slows simulation by an order of magnitude, so direct RL would need billions of samples. Instead:

- **Phase 1 — RL with a cheap proxy.** Train with PPO on **scandots**: (x, y) points in the robot's frame at which terrain height is queried. Cheap to compute, and geometrically equivalent to what depth would reveal. Privileged environment parameters *e*ₜ are available here too.
- **Phase 2 — supervised distillation to onboard sensing.** Distil into a policy that sees only **egocentric depth + proprioception**, trained with **DAgger** and truncated BPTT (N = 24), minimizing MSE against phase-1 actions.

Because supervised learning is orders of magnitude more sample-efficient than RL, **the whole system trains on a single GPU in a few days.**

> [!note] The recipe is [RMA](rma-paper.md)'s, with a different privileged signal
> RMA distilled *privileged physics* (mass, friction, motor strength) into an extrinsics vector estimated from proprioceptive history. This paper distils *privileged geometry* (scandots) into a terrain latent estimated from depth history. **Same two-phase privileged-teacher structure, one layer up the sensory stack** — and the paper offers an explicit "RMA architecture" variant that reuses the phase-1 base policy unchanged and trains only the latent estimators.

### A formal guarantee for the distillation (Theorem 2.1)

The stated risk is that scandots might carry information depth cannot recover, making phase 2 unachievable. The paper bounds it: if the phase-1 policy is ε-close to optimal and the phase-2 policy is η-close to phase 1 in action space, and *R*, *P* are Lipschitz, then

**|V*(s) − V^π₂(f(s))| < (2εγ + ηc)/(1 − γ)**

The practical consequence is a *design rule* rather than a theorem to admire: **choose the scandot layout and the camera field of view such that phase-2 loss is low**, and near-optimality follows. Rare to see a distillation step in a robotics paper given an explicit bound at all.

### Architectures

Two, both trained with PPO + BPTT truncated at 24 steps:

- **Monolithic** — scandots → MLP → γₜ; then `GRU(xₜ, γₜ, u_cmd) → aₜ`. In phase 2 a ConvNet encodes depth into the same GRU.
- **RMA-style** — an MLP controller with memory pushed into its inputs: `γₜ = GRU(mₜ)`, `zₜ = MLP(eₜ)`, `aₜ = MLP(xₜ, γₜ, zₜ, u_cmd)`. Phase 2 **freezes the base policy** and trains only the estimators: vision latent γ̂ from depth+proprioception, extrinsics ẑ from proprioception alone.

No gait priors, no predefined foot trajectories, no motion-capture datasets — rewards penalize energy plus hardware damage, and gaits are left to emerge.

### Simulation results (Table 1 — one policy across all terrains)

Average forward displacement / mean time-to-fall:

| Terrain | RMA-arch | Monolithic | Noisy elevation map | Blind |
|---|---|---|---|---|
| Slopes | 43.98 | 44.09 | 36.14 | 34.72 |
| **Stepping stones** | **18.83** | **20.72** | **1.09** | **1.02** |
| Stairs | 31.24 | **42.40** | 6.74 | 16.64 |
| Discrete obstacles | 40.13 | 28.64 | 29.08 | 32.41 |
| **Total** | **134.18** | **135.85** | 73.05 | 84.79 |

**Stepping stones is the terrain that separates the methods: ~20 m against ~1 m.** Blind and noisy-elevation-map baselines cannot locate the stones at all, while slopes are nearly solvable without vision — a clean demonstration that "does vision help?" is the wrong question, and "help with *what*?" is the right one. Overall the vision policies beat both baselines by **60–90%**.

Note also that the **noisy elevation map baseline is worse than blind on stairs** (6.74 vs 16.64). A degraded map is not merely less useful than a good one; it can be worse than no map.

### Real-world results (Fig. 4)

| Task | This work | Blind |
|---|---|---|
| Upstairs (17 cm × 30 cm) | **100%** (13 stairs) | **0%** (2.2 stairs) |
| Downstairs (17 cm × 30 cm) | **100%** (13) | **100%** (13) — *see below* |
| Stepping stones (30 cm wide, 15 cm apart) | **94%** (9.4 stones) | **0%** |
| Gaps (26 cm apart) | **100%** | **0%** |

> [!warning] The blind baseline "succeeds" at downstairs by falling down them
> Blind scores 100% on descent — but *"it learns to fall on every step and stabilize, leading to a very high impact gait,"* and **the robot dislocated its rear right hip during those trials.** A success-rate table records this as a tie. It is not a tie. This is the sharpest concrete example in this wiki of why a scalar success metric can invert the engineering conclusion, and it belongs next to the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md).

**Urban deployment**: stairs up to **24 cm high / 28 cm deep**, and curbs and obstacles up to **26 cm — nearly the robot's own height**. Clearing those requires an **emergent hip-abduction move**, because the A1 is too small to fit a leg between its body and the step. The paper attributes the discovery to the tabula-rasa gait approach: it is not in any motion dataset, so a prior-driven method would not have found it.

When the robot misses a step — which happens, since it is recalling terrain it can no longer see — the paper reports *"impressive recovery behaviour"* rather than failure.

### Hardware and deployment

[Unitree A1](../entities/unitree-a1.md), 12 actuated joints, front-facing **Intel RealSense** in the head; onboard compute is an **UPboard plus a Jetson NX**. Policy at **50 Hz**, low-level PD at **400 Hz**. Depth arrives every **100 ± 20 ms** at 480×848 and is cropped, hole-filled and downsampled to **58×87** before the backbone; the compressed embedding crosses a **UDP socket** with **10 ± 10 ms latency, which phase 2 explicitly trains against**. Simulation is **IsaacGym** with the **legged_gym** library.

That latency handling is the detail that makes the system real: the policy is trained to tolerate the asynchrony and the camera dropouts it will actually meet.

## Why this matters in this wiki

> [!note] The arc is now complete: RMA → vision → LocoFormer
> Three papers, overlapping authors, 2021 → 2025, and the wiki holds all of them.
>
> | | [RMA](rma-paper.md) 2021 | **This paper** 2022 | [LocoFormer](locoformer-paper.md) 2025 |
> |---|---|---|---|
> | Senses | Proprioception only | **+ egocentric depth** | Proprioception |
> | Privileged teacher | Physics (*e*ₜ) | **Geometry (scandots)** | **None** |
> | Memory | 0.5 s CNN window | **GRU, task-length** | **~18 s attention, across trials** |
> | Generalizes over | Terrain, payload | **Terrain geometry** | **Bodies** |
> | Structure | Two modules | Two modules | **One policy** |
>
> The first two papers are the same recipe applied at different levels of the sensor stack, and both depend on a **privileged simulator signal** that has no real-world counterpart. LocoFormer then discards the teacher entirely and buys the same adaptivity with context length and scale. Read together, they are a compact history of the field trading engineered structure for compute — and this middle paper is where the structure is at its most elaborate and most effective.

- **It resolves a limitation this wiki had already recorded.** RMA's conclusion named blindness as the binding constraint; this is the follow-up, and it closes the loop cleanly.
- **The scandots trick generalizes well beyond locomotion**: when the expensive modality is the bottleneck to RL, train on a cheap geometric proxy and distil. Filed under [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md).

## Entities mentioned

- [Ananye Agarwal](../entities/ananye-agarwal.md) — co-first author; later a [LocoFormer](locoformer-paper.md) co-author.
- [Ashish Kumar](../entities/ashish-kumar.md) — co-first author; also first author of [RMA](rma-paper.md).
- [Deepak Pathak](../entities/deepak-pathak.md) — co-advisor; the third of his papers in this wiki.
- [Unitree A1](../entities/unitree-a1.md) — platform, here with a depth camera added.
- [Jetson Xavier NX](../entities/jetson-xavier-nx.md) — the onboard compute running the policy at 50 Hz.
- [Isaac Gym](../entities/isaac-gym.md) — training simulator (now deprecated); its cheap-physics/expensive-rendering asymmetry is what forces the two-phase recipe.
- [legged_gym](../entities/legged-gym.md) — the training library, and the source of the terrain curriculum this paper adopts.

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — privileged-teacher distillation, plus explicitly training against measured sensor latency and dropouts.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — the recurrent terrain memory, in contrast to RMA's fixed window.
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — a waypoint between RMA's fixed 0.5 s window and LocoFormer's long context.

- [Locomotion adaptation lineage](../syntheses/rl/locomotion-adaptation-lineage.md) — where this paper sits in the 2021→2025 arc from engineered structure to scale.
## Open questions

- **Which architecture wins is unresolved** — monolithic leads on stairs (42.4 vs 31.2), the RMA variant on discrete obstacles (40.1 vs 28.6), and totals are within 1%. The paper does not adjudicate.
- **Real-world trial counts are small** and the stepping-stone 94% is over a limited course; see the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md).
- ~~Ananye Agarwal has no entity page~~ — **filed 2026-08-29** ([Ananye Agarwal](../entities/ananye-agarwal.md)). **[Ashish Kumar](../entities/ashish-kumar.md)** now has one too. **Jitendra Malik** — co-author here, on [RMA](rma-paper.md), and in [DreamDojo](dreamdojo-paper.md) — does not.
