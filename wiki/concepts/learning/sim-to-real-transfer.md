---
title: Sim-to-real transfer
type: concept
created: 2026-05-06
updated: 2026-08-13
sources: 41
tags: [sim-to-real, domain-gap, rl, simulation]
---

**Sim-to-real transfer** is the practice of training a robot policy in simulation and deploying it on a physical robot with little or no fine-tuning. The "reality gap" — differences between sim physics, sensor noise, lighting, dynamics — is the central obstacle.

## Why it matters
Real-robot data collection is slow and expensive. Simulation gives unlimited cheap training time. The whole agentic-robotics stack assumes that policies trained in simulators (Isaac Lab, MuJoCo Playground, Genesis, Genie Sim) will generalize to real robots — so the quality of sim-to-real determines whether simulation investment pays off.

## Historical lineage
The problem predates the deep-learning era under the name **simulation bias**: [Kober, Bagnell & Peters 2013](../../sources/kober-rl-robotics-survey-2013.md) (§6) describe policies exploiting model errors as "analogous to overfitting," note that direct sim-to-real transfer had been demonstrated in only a handful of cases, and catalogue the mitigation that became domain randomization — **artificial noise injection** (Jakobi et al. 1995; Atkeson 1998). Their observation that transfer works better for *self-stabilizing* tasks still explains much of the locomotion-vs-manipulation transfer asymmetry.

## Common techniques
- **Domain randomization** — randomize physics, textures, lighting, friction in sim so the policy learns invariances.
- **Domain adaptation** — fine-tune on a small amount of real data after sim training.
- **High-fidelity rendering** — use photorealistic renderers (Omniverse RTX, Madrona) so vision-based policies see realistic input.
- **High-frequency physics** — match real-robot control rates (e.g. [AGIBOT Genie Sim 3.0](../../entities/agibot-genie-sim.md)'s 1,000 Hz physics).
- **Vision pretraining on real images** — augment sim data with real video to anchor representations.

## Quantified gap (2025)

The [Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) provides the clearest independent measurement of the gap:

| Setting | Benchmark | Top result |
|---|---|---|
| Controlled simulation (short-horizon) | RLBench | **89.4%** (EquAct, Jan 2026) |
| Real household environments (long-horizon) | [BEHAVIOR-1K](../../entities/behavior-benchmark.md) full task success | **12.4%** (2025 Challenge winner) |

The 89.4% vs. 12.4% contrast is the canonical sim-to-real gap for household manipulation as of 2025. RLBench tests 18 short-horizon tasks in a controlled simulator; BEHAVIOR-1K's 1,000 tasks come from surveys of what households actually want robots to do.

## The learned-simulator failure mode: teaching to a flawed test

Classical sim-to-real assumes the simulator is **hand-authored and therefore inspectable** — you can read the friction coefficient that's wrong. Learned simulators break that assumption and add a failure with no pre-2020 analogue: using the same learned model to **train** a system and to **judge** it.

> "If the model understates the risk of skidding in rain, a vehicle trained in that model may learn to drive too fast and still score well when the same flawed model is used to test it. The score would reflect an error in the model, not readiness for a real road." ([HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md), pp. 7–8)

This is not hypothetical in this wiki: [Veo](../../entities/veo.md) is a video foundation model specialized as a **policy-evaluation simulator**, and the Dream* line generates training data for policies alongside it.

**Now measured.** [WorldArena](../../sources/worldarena-paper.md) ran world models as policy evaluators against the RoboTwin simulator's own verdict: both "have consistently higher success rates than those measured in the simulator, suggesting partial overfitting to successful trajectories." The learned evaluator **flatters** what it evaluates. *Ranking* survives ([Ctrl-World](../../entities/ctrl-world.md) at r = 0.986); *levels* do not. Veo reports the opposite sign, so the effect's direction isn't settled — see [world-model evaluation](../world-models/world-model-evaluation.md).

The policy consequence the brief draws: **define how much real-world validation a system requires before deployment regardless of its simulation performance**, and keep oversight running after deployment via monitoring and incident reporting, because even strong tests miss rare conditions.

## The learned-simulator sim-to-real gap is worse than the policy one

[WorldArena 2.0](../../sources/worldarena-2-paper.md) evaluated world models across [RoboTwin 2.0](../../entities/robotwin.md), [LIBERO](../../entities/libero.md), and a **real AgileX Split-Type [ALOHA](../../entities/aloha.md)**, and separated what transfers from what doesn't:

| Transfers across platforms | Doesn't |
|---|---|
| Visual quality, motion quality, physics adherence, 3D accuracy | **Content consistency, controllability** — "greater domain sensitivity in semantic and instruction-level alignment" |
| Functional rankings *between two simulators* | **Functional rankings against a real robot** — correlation "drops greatly"; most models score 0% |

The paper's conclusion: "simulation performance — whether perceptual or functional — is not a reliable proxy for real-world deployment and physical evaluation remains indispensable." It also self-critiques single-simulator benchmarking as "susceptible to overfitting, leading to artificially inflated rankings."

Note the recursion: this is the sim-to-real gap applied *to the simulator itself*. A learned simulator validated in simulation tells you little about a learned simulator used on hardware.

## Domain randomization, measured (RoboTwin 2.0, 2025)

The [RoboTwin 2.0 paper](../../sources/robotwin2-paper.md) is the wiki's cleanest controlled study of what randomization actually buys, because it varies *only* randomization while holding the simulator fixed.

**Randomizing five axes** — clutter, background texture (11,000 filtered Stable-Diffusion textures), lighting, tabletop height, and language instructions:

| Pretraining data | RDT | π0 |
|---|---:|---:|
| none (released weights) | 18.8% | 22.5% |
| **clean** sim data | 14.6% (*worse*) | 24.9% |
| **randomized** sim data | **24.8%** (+31.9% rel.) | **29.1%** (+29.3% rel.) |

Two results worth separating:

1. **Fidelity is not what closed the gap here.** Clean 2.0 data gave no benefit over the released weights. Since higher-fidelity clean simulation *didn't help*, the authors correctly infer the deficit is **not a real-to-sim gap but a robustness gap** — and the whole measured gain came from diversity, not realism. Anyone reading "better simulator closes sim-to-real" into this paper has the wrong lesson.
2. **Randomized pretraining transfers to clean downstream training.** The gain persists when the target task is subsequently trained on clean data only — so randomization is buying a durable property of the representation, not task-specific augmentation.

Real-world confirmation on a COBOT-Magic dual-arm: **10 real demonstrations + 1,000 randomized synthetic trajectories beat 10 real demonstrations alone by +24.4 points averaged**, and **the gains grow with difficulty** — +13.5 in the easiest configuration, **+33.0** in unseen-background-cluttered. Zero-shot synthetic-only beat 10 real demos in both unseen-background configurations. (The paper's headline "367%" is that hardest configuration; see the [source page](../../sources/robotwin2-paper.md).)

> [!note] Randomization compensates for pretraining diversity, not for the simulator
> Pair this with the benchmark table on [RoboTwin 2.0](../../entities/robotwin.md): non-pretrained policies collapse under randomization ([ACT](../../entities/act.md) 29.7 → 1.7, [DP](../../entities/diffusion-policy.md) 28.0 → 0.6) while pretrained VLAs survive (RDT 13.7, π0 16.3). Randomized synthetic data and large-scale VLA pretraining appear to buy **the same property** — robustness to appearance shift — by different routes, and the paper's own diagnosis of why the VLAs still drop 20–30 points is *"limited diversity in pretraining data."*

## Notable claims
- [MuJoCo Playground](../../entities/mujoco-playground.md) demonstrates **zero-shot** transfer from both state and pixel inputs across quadrupeds, humanoids, hands, and arms ([MuJoCo Playground Paper](../../sources/mujoco-playground-paper.md)).
- Tesla Optimus combines sim-to-real with imitation from human teleoperated/wearable-camera video.

## Related
- [VLA models](vla-models.md) — the typical policy class undergoing sim-to-real.
- [World-model simulators](../world-models/world-model-simulators.md) — sidesteps sim-to-real partially by training inside a learned model of reality.
- [World-model evaluation](../world-models/world-model-evaluation.md) — the two failure modes (plausibility trap vs. reality gap) and the compound of both.

## Mentioned in
- [Kober, Bagnell & Peters 2013 — RL in Robotics Survey](../../sources/kober-rl-robotics-survey-2013.md) — simulation bias, noise injection, self-stabilizing transfer.
- [MuJoCo Playground Paper](../../sources/mujoco-playground-paper.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [RoboCasa365 Paper](../../sources/robocasa365-paper.md)
- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)
- [Stanford HAI — AI Index Report 2026](../../sources/stanford-hai-ai-index-2026.md) — the 12.4% [BEHAVIOR-1K](../../entities/behavior-benchmark.md) challenge figure.
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md) — the learned-simulator "teaching to a flawed test" failure mode.
- [BEHAVIOR-1K Paper](../../sources/behavior-1k-paper.md) — the hard, long-horizon end of the gap; end-to-end RL 0.0, real-robot 0–22% ([OmniGibson](../../entities/omnigibson.md) sim).
- [CaP-X paper](../../sources/cap-x-paper.md) — a structurally different transfer story: what crosses the gap is the **code-as-action-space** (perception/control tools fixed across sim and real), not a visuomotor mapping. A 7B coding model RL-trained in sim only reaches 84%/76% on a real [Franka](../../entities/franka-panda.md).
- [ASPIRE paper](../../sources/aspire-paper.md) — transfers **debugging knowledge** across embodiments: sim-discovered skills as in-context guidance cut real-robot token cost ~4× and take drawer opening from 0/20 to 11/20.
- [WorldArena 2.0 paper](../../sources/worldarena-2-paper.md) — cross-platform sim-to-real for world models; perceptual dimensions transfer, functional rankings don't.
- [WorldArena paper](../../sources/worldarena-paper.md) — learned policy evaluators inflate absolute success rates.
