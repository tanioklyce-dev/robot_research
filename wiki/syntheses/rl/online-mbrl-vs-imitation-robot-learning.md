---
title: "Why online model-based RL lost to imitation/VLAs for robots (2022–2026)"
type: synthesis
created: 2026-07-09
updated: 2026-07-09
tags: [mbrl, dreamer, daydreamer, imitation-learning, vla, world-model, robot-learning, sample-efficiency, generalization, rl]
---

# Why online model-based RL lost to imitation/VLAs for robots (2022–2026)

In 2022, [DayDreamer](../../sources/daydreamer-paper.md) made a striking demonstration: [Dreamer](../../entities/dreamer.md) learning **online, on four real robots, with no simulator** — an A1 quadruped going from lying on its back to walking in **one hour without resets**. It looked like a template for robot learning: skip the simulator, skip the demonstrations, let the robot dream its own trials. Four years later the field's dominant paradigm is the near-opposite — **[imitation learning](../../concepts/learning/imitation-learning.md) at scale** ([Diffusion Policy](../../entities/diffusion-policy.md), [ACT](../../entities/act.md)) and **[VLA](../../concepts/learning/vla-models.md)/[LBM](../../concepts/learning/large-behavior-models.md) foundation models** ([π0](../../entities/pi-zero.md), [GR00T](../../entities/nvidia-groot.md)) pretrained on huge offline datasets. This page asks why, and argues the answer is not that online MBRL failed but that it **optimized the wrong axis for where the value turned out to be**.

> [!note] Scope
> "Won/lost" here means *which paradigm the robot-learning frontier built on*, not which is technically superior. Online MBRL remains excellent at what it targets; the field's objective function changed underneath it. Model-based *ideas* did not lose — see the coda.

## The bet each paradigm made

| | Online MBRL (DayDreamer line) | Imitation / VLA (the winner) |
|---|---|---|
| Scarce resource it optimizes | **Environment interactions** (sample efficiency) | **Human demonstrations / offline data** (leverage a pretrained prior) |
| Where competence comes from | The robot's own trial-and-error, compressed by a world model | Internet + teleop data baked into a base model, then fine-tuned ([Tedrake's "build a bridge"](../../sources/automated-podcast-tedrake-rocket-ship.md)) |
| Unit of deployment | One policy, one robot, one task, learned in place | One model, many tasks, many embodiments, prompted by language |
| What it needs to work | A reward function, a reset-free setup, online compute on the robot | A dataset and a strong base model |

DayDreamer's own framing was that world-model imagination supplies the cheap trials everyone else gets from a simulator — a **sample-efficiency** argument. The winning paradigm sidesteps the question: don't be efficient with online trials, **have almost none** and start from a model that already knows how the world looks and moves.

## Four reasons the imitation/VLA bet paid off

**1. The binding constraint was generalization, not sample efficiency.** MBRL's headline is "learn a good policy in few interactions." But a DayDreamer A1 that walks perfectly has learned *one task on one robot*; it generalizes to a new task or object roughly not at all. The 2023–26 [TRI LBM result](../../sources/tri-lbm-paper.md) reframed the goal: **multitask pretraining is what buys robustness and fast adaptation to new tasks** — exactly the axis online single-task MBRL does not touch. The field discovered it cared more about "works on the 200th task" than "learns the 1st task in an hour."

**2. A reward function is a worse interface than a demonstration.** MBRL needs a reward; robotics rewards are sparse, hand-designed, and hard to specify for dexterous tasks (fold laundry, bus a table). Imitation needs a *demonstration*, which for manipulation is far cheaper to produce than a good reward — and the whole [LeRobot](../../entities/lerobot.md)/teleop tooling stack ([ALOHA](../../entities/aloha.md), leader arms, [Isaac Teleop](../../entities/nvidia-isaac-teleop.md)) drove the cost of demonstrations toward zero. The interface that scaled was the one humans could supply without writing a reward.

**3. The "no simulator, learn on hardware" pitch aged badly against two trends.** DayDreamer's differentiator was skipping the simulator — but (a) sim got dramatically better and cheaper ([Isaac Lab](../../entities/nvidia-isaac-lab.md), massively parallel envs, [sim-to-real](../../concepts/learning/sim-to-real-transfer.md) via domain randomization now "surprisingly turnkey" per [Tedrake](../../sources/automated-podcast-tedrake-rocket-ship.md)), so the sim tax MBRL avoided shrank; and (b) the winning move became pretraining on **data you already have** (internet video, cross-embodiment corpora like [Open X-Embodiment](../../entities/open-x-embodiment.md)) rather than generating trials at all. Online hardware learning is also operationally painful — reset-free is hard, exploration can damage the robot, and per-robot online compute doesn't amortize.

**4. The LLM-scaling prior transferred, and it favored offline.** The field watched GPT and concluded the recipe is *big model + big offline data + light task adaptation*. VLAs are that recipe ported to robots; online MBRL is not. Investment, talent, and tooling flowed to the paradigm that looked like the thing that was working elsewhere.

## What online MBRL still owns

- **Locomotion / agile control with a clean reward.** Where a reward *is* specifiable and dynamics are fast and contact-rich, model-based (and model-free) RL in sim remains the state of the art — legged locomotion and drone racing. [S5WM](../../sources/s5wm-paper.md) (real agile-quadrotor flight, [Scaramuzza](../../concepts/robotics/agentic-uavs.md) lab) is a 2025 datapoint that the *engineering* frontier there is now wall-clock, not sample count.
- **Sample efficiency when data genuinely can't be pretrained away.** New embodiment, no relevant prior, expensive interaction → MBRL's core pitch still holds.

## Coda: model-based ideas didn't lose — they migrated

The dichotomy is softening from both sides, and the model-based *machinery* is quietly everywhere:

- **World models became the simulator/data-engine, not the policy learner.** The generative-video line ([DreamGen](../../entities/dreamgen.md) neural trajectories, [Cosmos](../../entities/nvidia-cosmos.md), [DIAMOND](../../sources/diamond-paper.md)'s neural game engine) uses learned world models to *generate training data or environments* for imitation/VLA policies — the world model as a data flywheel rather than a thing you plan inside. That is model-based RL's substrate winning under a different job description.
- **RL came back as a *post-training* layer on imitation.** [π*0.6/RECAP](../../entities/pistar06.md) and [HIL-SERL](../../concepts/learning/imitation-learning.md) do offline-RL / advantage-conditioning / human-gated correction *on top of* a pretrained policy — RL as fine-tuning, not as the from-scratch learner. The winning stack is **pretrain-by-imitation, then RL-to-improve**, not RL-from-scratch.
- **[Tedrake's LBM ⊃ VLA taxonomy](../../concepts/learning/large-behavior-models.md)** explicitly keeps a **video/world-model backbone** as a first-class option for the policy — so the next generation of generalist policies may re-absorb world models through the front door.

So the honest summary: **online, from-scratch, single-task MBRL lost the role of "how robots acquire skills"** to offline imitation + foundation-model pretraining, because the field's binding constraint turned out to be generalization-per-dollar-of-human-effort rather than interactions-per-task. But the learned-world-model idea reappeared as the simulator, the data generator, and a candidate policy backbone — it lost the battle it was fighting in 2022 and won three others it wasn't.

## Related

- [DayDreamer](../../sources/daydreamer-paper.md) — the 2022 high-water mark for the online-MBRL-on-robots thesis this page interrogates.
- [Dreamer / DreamerV3](../../entities/dreamer.md) — the algorithm family; [Danijar Hafner](../../entities/danijar-hafner.md) — its through-line.
- [TRI LBM paper](../../sources/tri-lbm-paper.md) — the multitask-pretraining-buys-robustness result that reframed the goal.
- [Automated Podcast — Tedrake](../../sources/automated-podcast-tedrake-rocket-ship.md) — the "build a bridge from a base model" data reframe, and "deployment is the milestone."
- [VLA models](../../concepts/learning/vla-models.md) / [Large behavior models](../../concepts/learning/large-behavior-models.md) — the winning paradigm.
- [Imitation learning](../../concepts/learning/imitation-learning.md) — its substrate, incl. the RL-as-post-training coda ([π*0.6](../../entities/pistar06.md)).
- [World model](../../concepts/world-models/world-model.md) — where the model-based machinery migrated (simulator / data engine).
- [Atari RL lineage](atari-rl-lineage.md) — the "Atari trained the field, the benchmark moved on" companion argument, one abstraction level down.

## Open questions

- Does the pretrain-then-RL stack eventually re-privilege *online* interaction (RL post-training is the fastest-growing piece)? If so, MBRL-for-post-training (world model to imagine fine-tuning rollouts) is an under-explored corner.
- Will a video/world-model-backbone LBM (Tedrake's stated bet) beat VLM-backbone VLAs — i.e. does the world model win as the *policy* backbone after all?
- Is there a real-robot task class where DayDreamer-style online MBRL is still the best answer in 2026, or has sim + pretraining swallowed all of it?
