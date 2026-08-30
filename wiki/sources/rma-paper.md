---
title: "RMA: Rapid Motor Adaptation for Legged Robots"
type: source
url: https://arxiv.org/abs/2107.04034
local_path: raw/2107.04034v1.pdf
sha256: d8660da881851756287efab24d85f5c629ba97878f70297eb429a8e8a9a57846
author: Ashish Kumar (UC Berkeley), Zipeng Fu (CMU), Deepak Pathak (CMU), Jitendra Malik (UC Berkeley, Facebook)
published: 2021-07-08
ingested: 2026-08-29
venue: RSS 2021 (Robotics: Science and Systems)
format: PDF (15 pp., arXiv:2107.04034v1)
project_page: https://ashish-kmr.github.io/rma-legged-robots/
tags: [rma, locomotion, quadruped, unitree-a1, sim-to-real, domain-randomization, privileged-learning, online-system-identification, adaptation, cmu, berkeley]
---

# RMA: Rapid Motor Adaptation for Legged Robots

## Summary

**The paper that made blind quadrupeds adapt in under a second, and the reference point most adaptive-locomotion work since has argued with.** RMA trains entirely in simulation — no reference trajectories, no predefined foot-trajectory generators, no real-world fine-tuning, and *no simulation calibration* — then deploys on a **[Unitree A1](../entities/unitree-a1.md)** that walks over sand, mud, hiking trails, tall grass and dirt piles **without a single failure**, despite never having seen unstable ground, obstructive vegetation or stairs during training.

The design is two modules. A **base policy** π is trained by RL with **privileged** access to the true environment configuration *e*ₜ (mass, centre of mass, friction, terrain height, motor strength), which an encoder μ compresses into a small **extrinsics vector** *z*ₜ. Since privileged information does not exist at deployment, an **adaptation module** φ is then trained by supervised learning to *estimate* ẑₜ from the robot's own recent state–action history.

The conceptual move worth keeping is what φ predicts. It does **not** regress the physical parameters *e*ₜ, as system identification would. It regresses **z**ₜ — "how the behavior should change" — skipping the physics entirely:

> *"Instead of predicting eₜ, which is the case in typical system identification, we directly estimate the extrinsics zₜ that only encodes how the behavior should change to correct for the given environment vector eₜ."*

This is **online system identification without identifying the system**, from 0.5 seconds of proprioception, and it is why adaptation takes under a second instead of the 4–8 minutes prior adaptation methods needed.

## Key claims

### Architecture and training

- **Base policy π** — 3-layer MLP (hidden 128): state *x*ₜ ∈ ℝ³⁰, previous action *a*ₜ₋₁ ∈ ℝ¹², extrinsics *z*ₜ ∈ ℝ⁸ → 12 target joint angles. Trained with **PPO, 15,000 iterations**, batch 80,000.
- **Environment factor encoder μ** — 3-layer MLP (256, 128) compressing *e*ₜ ∈ ℝ¹⁷ → *z*ₜ ∈ ℝ⁸. Trained jointly with π.
- **Adaptation module φ** — 2-layer MLP embedding to 32-dim, then a **3-layer 1-D CNN over time**, on **k = 50 timesteps = 0.5 s** of history. Trained by supervised regression, MSE(ẑₜ, zₜ).
- **On-policy training for φ** (à la DAgger/Ross et al.) rather than unrolling the expert: a φ trained only on clean expert trajectories *"would not be robust to deviations from the expert trajectory, which will happen often during deployment."* They unroll π using ẑ from a randomly initialized φ and iterate.
- **Asynchronous deployment** — φ at **10 Hz**, π at **100 Hz**, running in parallel with **no central clock**; π simply consumes the most recent ẑₜ. Justified because ẑ changes slowly in the real world, and *"critical for seamless deployment on low-cost robots like A1 with limited on-board compute."*
- Rewards are **bioenergetics-inspired**, over a varied terrain generator — no demonstrations, no motion templates.

### Simulation results (Table II — 3 seeds × 1,000 episodes)

| Method | Success % | TTF | Reward | Distance (m) | Adaptation samples |
|---|---|---|---|---|---|
| Robust (domain randomization) | 62.4 | 0.80 | 4.62 | 1.13 | 0 |
| SysID (predict *e*ₜ directly) | 56.5 | 0.74 | 4.82 | 1.17 | 0 |
| AWR (offline adaptation) | 41.7 | 0.65 | 4.17 | 0.95 | **40,000** |
| RMA w/o adaptation | 52.1 | 0.75 | 4.72 | 1.15 | 0 |
| **RMA** | **73.5** | **0.85** | **5.22** | **1.34** | **0** |
| Expert (oracle *z*ₜ) | 76.2 | 0.86 | 5.23 | 1.35 | 0 |

**RMA lands within 2.7 points of the privileged oracle while using zero adaptation samples.** Two ablations carry the argument: predicting the physics directly (**SysID, 56.5**) is *worse* than predicting the behavioral correction, and the method needing 40k real samples (**AWR, 41.7**) is worst of all. RMA also applies the **lowest torque** and is the **smoothest** of the non-oracle methods.

### Real-world results

- **In the wild** (Fig. 1): sand, mud, hiking trails, tall grass, dirt pile — **no failures across all trials**. **70%** success descending stairs on a hiking trail; **80%** across a cement pile and pebbles. None of these terrain types were in training.
- **Oily plastic sheet, with the feet also wrapped in plastic: 90% success.**
- **Step-down 15 cm: 80%.** Memory-foam mattress and uneven foam: **100%** — the A1's own factory controller **fails** on uneven foam.
- **Payload: RMA carries 12 kg — 100% of the robot's body weight.** The stock controller starts sagging at 8 kg; RMA-without-adaptation stops moving above 8 kg (though it rarely falls).

### The extrinsics vector is legible

In the oily-patch trial, components z₁ and z₅ **shift at the moment of slip** and then **stay shifted** even after the gait period recovers — the vector goes on encoding "this surface is slippery" rather than relaxing back. A rare case of a learned latent whose behavior can be read directly off a plot against a physical event.

### Stated limitations (the authors')

The robot is **blind** — proprioception only. *"Larger perturbations such as sudden falls while going downstairs, or due to multiple leg obstructions from rocks, sometimes lead to failures."* They name exteroception/vision as the necessary next step.

> [!note] This limitation was answered, by the same group, one year later
> **[Legged Locomotion in Challenging Terrains using Egocentric Vision](egocentric-vision-locomotion-paper.md)** (Agarwal, Kumar, Malik & Pathak, CoRL 2022 — ingested 2026-08-29) adds a single front-facing depth camera and takes upstairs from RMA's blind failure to **100%**. It reuses RMA's two-phase privileged-distillation recipe with *geometry* (scandots) as the privileged signal instead of physics, and even offers an explicit "RMA architecture" variant that freezes the phase-1 base policy.

## Why this matters in this wiki

> [!note] RMA and [LocoFormer](locoformer-paper.md) are the same author, four years apart, arguing opposite ways
> Both are [Deepak Pathak](../entities/deepak-pathak.md) papers about a legged robot adapting online without weight updates. The design philosophies are close to inverted, and the pair is the cleanest illustration in this wiki of the field's broader arc from engineered structure to scale.
>
> | | **RMA** (2021) | **[LocoFormer](locoformer-paper.md)** (2025) |
> |---|---|---|
> | Adaptation horizon | **0.5 s** (k=50) | **~18 s**, spanning trial boundaries |
> | Structure | Two modules, hand-designed | One policy, no adaptation module |
> | Supervision | **Privileged teacher** + supervised distillation | End-to-end RL only |
> | Body scope | **One robot** (A1), varied terrain | **Ten unseen robots**, incl. wheeled |
> | Adapts to | Terrain, payload, friction | **Morphology** — locked knees, cut-off legs |
> | Failure recovery | Within a trial | **Across trials** — learns from falls |
>
> LocoFormer explicitly classes RMA-style controllers as **"myopic,"** adapting over *"a few hundred milliseconds"* — which is a fair description of k=50 at 100 Hz, and is precisely the design choice RMA made deliberately for the compute budget of a cheap robot. What changed between the papers is not the goal but what a policy is allowed to cost.
>
> The trade is visible in both directions. RMA runs its adaptation module at **10 Hz on an A1's onboard compute**; LocoFormer's authors list resource intensity as their first stated limitation.

- **First serious locomotion primary in this wiki**, together with LocoFormer — closing part of the gap the [awesome-physical-ai analysis](awesome-physical-ai-github.md) named (the RMA / legged_gym / H2O corpus).
- **The privileged-teacher-then-distill recipe** here — train with ground-truth simulator state, then regress it from observable history — became a standard sim-to-real pattern well beyond locomotion. This page is the wiki's reference for it.

## Entities mentioned

- [Ashish Kumar](../entities/ashish-kumar.md) — first author.
- [Deepak Pathak](../entities/deepak-pathak.md) — co-author; later co-author of [LocoFormer](locoformer-paper.md) and CEO of [Skild AI](../entities/skild-ai.md).
- [Zipeng Fu](../entities/zipeng-fu.md) — co-author, then at CMU. The wiki knows him for [Mobile ALOHA](mobile-aloha-paper.md) (Stanford, manipulation); RMA is his earlier locomotion work.
- [Unitree A1](../entities/unitree-a1.md) — the deployment platform; also used with a depth camera in the [vision follow-up](egocentric-vision-locomotion-paper.md), and controlled zero-shot by [LocoFormer](locoformer-paper.md).

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — trained wholly in sim, deployed with no calibration and no fine-tuning.
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the **prehistory** of the experience-conditioned mode: same goal, fixed 0.5 s window and an explicit module instead of long context.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — adaptation with no gradient steps at deployment.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — the AWR baseline (40k real samples, 41.7%) is the case against learning in the real world here.

- [Locomotion adaptation lineage](../syntheses/rl/locomotion-adaptation-lineage.md) — where this paper sits in the 2021→2025 arc from engineered structure to scale.
## Open questions

- **No [Unitree A1](../entities/unitree-a1.md) entity page** — the platform appears in both locomotion primaries and has no page.
- **Jitendra Malik has no entity page**, despite appearing here and in [DreamDojo](dreamdojo-paper.md).
- **Was the extrinsics dimension (8) tuned?** No ablation on |z| is reported, though it is the whole information bottleneck.
- ~~The vision follow-up is uningested~~ — **[ingested 2026-08-29](egocentric-vision-locomotion-paper.md)**; it completes the arc.
- **Success is defined per-setup** and real-world trials run **5 per condition** (2 when failure was obvious, to protect the hardware). Honest and clearly stated, but far below what the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) would want.
