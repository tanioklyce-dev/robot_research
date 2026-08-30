---
title: Sim-to-real transfer
type: concept
created: 2026-05-06
updated: 2026-08-27
sources: 63
tags: [sim-to-real, domain-gap, rl, simulation, real-to-sim, r2s2r]
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
- **[Generative appearance transfer](generative-data-augmentation.md)** — restyle *real* episodes into new scenes with a video-to-video model, keeping the trajectory (and therefore the action labels) intact. Attacks background overfitting without touching the simulator at all.
- **Constraining reality instead** — build a light-controlled enclosure so the physical workspace matches the simulated one. Cheap, effective, and it narrows generalization by exactly as much as it narrows the input distribution (see below).

> [!note] The two directions are opposites, and people use both
> The [Seeed DLI course](../../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) requires a **"Lightbox"** — a light-controlled workspace with fixed cameras, built so the real scene matches the [Isaac Sim](../../entities/nvidia-isaac-sim.md) assets — *and* generatively diversifies its training backgrounds with [Cosmos](../../entities/nvidia-cosmos.md) Transfer. One move narrows the real distribution to meet the simulator; the other widens the training distribution to cover reality. Constraining what you *record* while diversifying what you *train on* is defensible, but no source in the wiki has tested whether the augmentation recovers the generalization the enclosure gave up. Good open experiment.

## Two-phase privileged distillation (the locomotion recipe)

A pattern this wiki now holds three instances of, and the workhorse of learned locomotion sim-to-real:

1. **Phase 1** — train with RL in simulation using a **privileged signal that exists only in the simulator**: true physics parameters ([RMA](../../sources/rma-paper.md): mass, friction, motor strength) or true terrain geometry ([egocentric vision](../../sources/egocentric-vision-locomotion-paper.md): "scandots," height queried at points under the robot).
2. **Phase 2** — **distil** into a policy restricted to onboard sensing, by supervised regression (DAgger) onto the phase-1 policy's actions or latents.

Why it works: the privileged signal makes phase 1 an easy RL problem, and supervised learning is orders of magnitude more sample-efficient than RL, so phase 2 is cheap — the vision system trains **on a single GPU in a few days** where end-to-end RL on rendered depth would need billions of samples.

The vision paper also supplies a **bound** (its Thm 2.1): if phase 2 is η-close to phase 1 in action space and the dynamics and reward are Lipschitz, phase-2 return is near-optimal. The usable form is a design rule — *choose the privileged signal and the sensor's field of view so that phase-2 loss can be driven low* — since a privileged signal carrying information the real sensor cannot recover makes the distillation unachievable in principle.

> [!note] The recipe's own successor abandons it
> [LocoFormer](../../sources/locoformer-paper.md) (2025) uses **no privileged teacher at all**, buying the same adaptivity with long context and scale. Worth watching as a signal about where this technique sits: it is a way to make RL tractable under a compute constraint, and it becomes less necessary as the constraint relaxes.

## Quantified gap (2025)

The [Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) provides the clearest independent measurement of the gap:

| Setting | Benchmark | Top result |
|---|---|---|
| Controlled simulation (short-horizon) | RLBench | **89.4%** (EquAct, Jan 2026) |
| Real household environments (long-horizon) | [BEHAVIOR-1K](../../entities/behavior-benchmark.md) full task success | **12.4%** (2025 Challenge winner) |

The 89.4% vs. 12.4% contrast is the canonical sim-to-real gap for household manipulation as of 2025. RLBench tests 18 short-horizon tasks in a controlled simulator; BEHAVIOR-1K's 1,000 tasks come from surveys of what households actually want robots to do.

## The inverted approach: build the simulator from the task

[Real-to-sim-to-real (R2S2R)](../robotics/real-to-sim-to-real.md) reverses the starting point of everything above. Classical sim-to-real begins with a general-purpose authored simulator and asks how to close the gap; R2S2R begins with a **specific real task**, reconstructs it as an interactive world aligned in appearance *and* dynamics, trains and screens policies there, and returns to hardware.

[World Labs / SceniX](../../sources/world-labs-r2s2r.md) claim policies trained with **zero real-world training data** transferring directly to ALOHA, YAM, RB-Y1, Flexiv and xArm across contact-rich tasks including deformable cables — the interaction class where the classical techniques on this page perform worst. Two things the reconstructed world supplies that hardware cannot: training **without resetting the environment after every trial**, and supervision on **"outcomes under alternative actions"**, which is counterfactual and unobtainable on real hardware by construction.

> [!note] Its own authors say it is a mixture, not a replacement
> Asked about [Sergey Levine](../../entities/sergey-levine.md)'s position that simulation always deviates and real collection is essential, [Yunzhu Li](../../entities/yunzhu-li.md) answers **"they don't contradict with each other"**: a simulator "doesn't necessarily have to be pure physics — it can be a combination between both physics and also learning," physics-weighted early for consistency and structure, shifting "towards more learning-based modeling of the environments" as deployment data accumulates ([a16z conversation](../../sources/a16z-worldlabs-scenix-conversation.md)). R2S2R is a **data flywheel with a physics prior**. The blog post's "zero real-world training data" headline oversells what its authors claim in conversation.

> [!note] It relocates the real-data cost rather than removing it
> "Zero real-world training data" is true of the *policy*. The world is built from real captures of the robot, sensors, environment, objects and demonstrations — the real data moved from policy training into world construction, and the post never quantifies how much capture a task needs. That number is the method's actual cost, and it is the one thing not reported.

Validation is by **matched open-loop execution**: run the same action sequence in sim and reality and compare observations, object responses and outcomes. Open-loop is the right choice — a closed-loop policy corrects for dynamics error as it runs, masking the discrepancy under test.

## The learned-simulator failure mode: teaching to a flawed test

Classical sim-to-real assumes the simulator is **hand-authored and therefore inspectable** — you can read the friction coefficient that's wrong. Learned simulators break that assumption and add a failure with no pre-2020 analogue: using the same learned model to **train** a system and to **judge** it.

> "If the model understates the risk of skidding in rain, a vehicle trained in that model may learn to drive too fast and still score well when the same flawed model is used to test it. The score would reflect an error in the model, not readiness for a real road." ([HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md), pp. 7–8)

This is not hypothetical in this wiki: [Veo](../../entities/veo.md) is a video foundation model specialized as a **policy-evaluation simulator**, and the Dream* line generates training data for policies alongside it.

> [!warning] R2S2R runs directly into this
> The same reconstructed world trains the policy **and** evaluates it — precisely the structure this section warns about. The defenses [World Labs offers](../../sources/world-labs-r2s2r.md) are the right ones in kind (matched open-loop validation; checking that sim ranking matches real ranking on hardware), but are asserted without numbers by the party selling the world. The durable point: a reconstructed world is only as trustworthy as the *independent* real check on it, and that check is the expensive thing the method exists to avoid. The economics push toward validating less as confidence grows.

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

## The actuator-side gap: fidelity beats randomization at small scale

Everything above attacks the gap in the **scene** — textures, lighting, backgrounds, contact parameters. [Microduck](../../entities/microduck.md) makes the opposite case for cheap legged hardware: the gap is in the **motor**.

> "At this scale — tiny servos driving a ~800 g biped — **actuator fidelity is most of the sim2real gap**, which is why the actuator is modeled down to its voltage control law instead of an ideal PD." ([Microduck RL](../../sources/pollen-robotics-microduck.md))

The concrete recipe — **BAM M6** voltage/back-EMF/Stribeck-friction model of the [Dynamixel](../../entities/dynamixel.md) XL330, randomization over **battery voltage, voltage sag under load, command delay and friction**, and **±1° backlash simulated as an unactuated hinge read through by the observations** — is broken out in [Actuator fidelity in sim-to-real](actuator-fidelity-sim2real.md).

Two things make it worth a section here rather than a bullet in "common techniques":

- **It is a claim about where the budget goes, not just another technique.** If actuator fidelity dominates below some mass/cost threshold, then randomizing an *idealised* PD model harder is spending effort in the wrong place — you widen the distribution without moving it onto reality.
- **It is the wiki's first end-to-end published recipe attached to a purchasable robot.** Apache-2.0 training code, a $399 platform, and the seven policies it produced, all released together. Every other sim-to-real source here is a paper, a benchmark, or a vendor claim.

> [!note] Untested outside one robot
> One worked example, vendor-published, no independent replication, and no delivered units as of 2026-08-27. The generalisation — *cheaper robot ⇒ more of the sim-to-real budget belongs in the actuator model* — is a hypothesis this wiki finds plausible, not an established result. The wiki's own low-cost cluster ([SO-ARM101](../../entities/so-arm101.md), [LeKiwi](../../entities/lekiwi.md), [XLeRobot](../../entities/xlerobot.md)) would be the place to test it.

## Notable claims
- [MuJoCo Playground](../../entities/mujoco-playground.md) demonstrates **zero-shot** transfer from both state and pixel inputs across quadrupeds, humanoids, hands, and arms ([MuJoCo Playground Paper](../../sources/mujoco-playground-paper.md)).
- Tesla Optimus combines sim-to-real with imitation from human teleoperated/wearable-camera video.

## Related
- [VLA models](vla-models.md) — the typical policy class undergoing sim-to-real.
- [World-model simulators](../world-models/world-model-simulators.md) — sidesteps sim-to-real partially by training inside a learned model of reality.
- [Actuator fidelity in sim-to-real](actuator-fidelity-sim2real.md) — the actuator-side branch of this page.
- [World-model evaluation](../world-models/world-model-evaluation.md) — the two failure modes (plausibility trap vs. reality gap) and the compound of both.

## Mentioned in

> [!note] Curated list — **63** source pages link here; the ones below are those that shaped this page.

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
- [Microduck — Pollen Robotics launch](../../sources/pollen-robotics-microduck.md) — the actuator-side gap; a full sim2real recipe shipped with a $399 robot.
