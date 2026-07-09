---
title: "Why online model-based RL lost to imitation for robots (2022→2026)"
type: synthesis
created: 2026-07-09
updated: 2026-07-09
tags: [mbrl, dreamer, daydreamer, imitation-learning, vla, lbm, world-model, sim-to-real, deployment, rl-history]
---

# Why online model-based RL lost to imitation for robots (2022→2026)

In 2022, [DayDreamer](../../sources/daydreamer-paper.md) demonstrated the thing model-based RL had promised for years: a real quadruped learning to walk **in one hour, online, on hardware, with no simulator, no demonstrations, and no resets** — plus visual pick-and-place on two arms. It looked like the opening of an era. Instead, by 2026 essentially every serious robot-learning effort the wiki tracks — [GR00T](../../entities/nvidia-groot.md), [π0/π0.7/π*0.6](../../entities/pi-zero.md), [TRI's LBMs](../../concepts/learning/large-behavior-models.md), the whole [LeRobot](../../entities/lerobot.md) ecosystem — is **imitation-first**: pretrain on demonstrations, fine-tune on demonstrations, deploy a frozen policy. Online world-model RL on robots all but vanished from the frontier. This page reconstructs why, from ingested sources.

> [!note] Scope
> "Won/lost" here means *which paradigm the robot-learning frontier built on*, not which is technically superior. Online MBRL remains excellent at what it targets; the field's objective function changed underneath it. Model-based *ideas* did not lose — see "where world models actually went."

## The short answer

Online MBRL solved the wrong bottleneck. Its selling point was **sample efficiency of reward-driven learning** — but the field's binding constraints turned out to be **task specification, semantic generality, deployment safety, and data economics**, and imitation attacks all four directly. Meanwhile MBRL's home turf (locomotion) was captured by a *different* trick, and world models themselves survived by moving up the stack.

## Five forces

### 1. The interface problem: rewards don't scale to household semantics

DayDreamer's tasks had natural reward signals (forward velocity, object-at-goal). The tasks the field actually wanted — "set the breakfast table," "install the bike rotor" ([TRI LBM](../../sources/tri-lbm-paper.md)), open-vocabulary tabletop work ([GR00T 1.7 in LeRobot](../../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)) — have **no writable reward function**, but they have cheap demonstrations. Imitation replaces reward engineering with teleoperation, and the VLM backbone gives language conditioning for free ([N1.5's language-following jump 46.6%→93.3%](../../sources/groot-n1_5.md)). A reward-driven learner has no comparable language story: the 2022-era world model takes actions and pixels; it cannot be *told* anything.

### 2. Foundation-model economics: bridge-building beats from-scratch

[Tedrake's reframe](../../sources/automated-podcast-tedrake-rocket-ship.md): robot learning starts from a base model that already carries world knowledge, and the data problem is **"building a bridge"** from that common sense to one new output — actions. Online MBRL is the opposite bet: learn dynamics *from scratch, per robot, per environment*, from the robot's own experience. That made sense pre-foundation-models. After [OXE](../../entities/open-x-embodiment.md), 20K-hour egocentric corpora ([EgoScale](../../sources/egoscale-paper.md)), and VLM/video backbones, the amortization math is brutal: a [TRI LBM](../../sources/tri-lbm-paper.md) fine-tune needs **3–5× less data per new task** *because of* multitask pretraining, and a hackathon team fine-tunes GR00T on [150–300 episodes](../../sources/seeed-embodied-ai-hackathon-2025-recap.md). DayDreamer's one hour is genuinely impressive — and it buys **one task on one robot**, with none of it transferring.

### 3. Locomotion was captured by parallel simulation, not world models

DayDreamer's flagship domain fell to a different attack within the same two years: **massively parallel GPU simulation + domain randomization + model-free PPO** ([Isaac Lab](../../entities/nvidia-isaac-lab.md)/legged-gym-style). As Tedrake put it, domain randomization over stairs and bumps was "**somehow good enough** to make a robot walk over almost anything in the real world — not expected it would be that easy" ([podcast](../../sources/automated-podcast-tedrake-rocket-ship.md)); humanoid locomotion is now "surprisingly turnkey" ([GEAR-SONIC](../../entities/gear-sonic.md) being the wiki's exemplar). When a simulator gives you millions of free samples in parallel, MBRL's sample-efficiency argument evaporates — and its *wall-clock* cost becomes the liability ([S5WM](../../sources/s5wm-paper.md) exists precisely because the world model made training 4× slower than it needed to be).

### 4. Deployment operations: exploration on hardware doesn't certify

An online learner **explores on the physical robot** — near furniture, objects, and eventually people. Everything the wiki has ingested about deployment points the other way: [ISO 13482-style certification](../../concepts/robotics/robot-safety-standards.md) assumes fixed, verifiable behavior (already hard for a *frozen* learned policy; harder still for one that changes overnight); [TRI's evaluation methodology](../../sources/tri-lbm-paper.md) (blind randomized A/B, 50+ rollouts per task) presumes a static policy to measure; and the commercial deploy loop (train → validate → ship checkpoints to [Thor](../../entities/jetson-thor.md)) has no slot for on-robot weight updates. Imitation's train-offline/deploy-frozen shape fit the industry; online RL's shape didn't.

### 5. The tooling flywheel went to demonstrations

The $100 [SO-101](../../entities/so-arm101.md) leader arm, [UMI](../../entities/umi.md) grippers, [Isaac Teleop](../../entities/nvidia-isaac-teleop.md)'s XR pipeline, `LeRobotDataset` + the HF Hub — an entire commodity infrastructure emerged for **collecting and sharing demonstrations**, with community-scale network effects ([worldwide hackathons](../../entities/lerobot-worldwide-hackathon-2025.md), 16K+ datasets). Nothing comparable emerged for on-robot RL: DayDreamer shipped async actor/learner infrastructure, but there was no data flywheel — online experience is consumed where it's produced, so nothing compounds across the community.

## Where world models actually went

The *models* won even as the *training loop* lost. World models re-entered robot learning up the stack:

- **As policy backbones/objectives** — [Cosmos 3's policy mode](../../sources/cosmos-3-technical-report.md) tops RoboArena; [FLARE](../../concepts/world-models/flare.md)'s latent-WM loss trains GR00T N1.5; [V-JEPA 2](../../entities/v-jepa-2.md)-AC plans from latents; Tedrake argues video backbones win for long context ([DFoT](../../sources/history-guided-video-diffusion-paper.md) being his group's evidence).
- **As data generators** — [DreamGen's neural trajectories](../../sources/dreamgen-paper.md) (827 h of GR00T N1's pyramid), Cosmos-3-for-LeRobot's stated purpose ([NVIDIA↔HF partnership](../../sources/nvidia-hf-lerobot-open-robotics-blog.md)).
- **As simulators/engines** — the [world-model-simulators](../../concepts/world-models/world-model-simulators.md) line; [DIAMOND](../../sources/diamond-paper.md)'s CS:GO neural game engine at research scale.
- **And RL itself returned — but offline, on top of imitation**: [π*0.6's RECAP](../../sources/pistar06-paper.md) (offline RL pretraining + advantage-conditioned improvement from deployment data + human interventions) is 2025–26's "learning from experience," with the exploration problem tamed by an IL foundation and human gates. That is the synthesis position: **not** imitation *versus* RL, but RL as a **post-training** layer on an imitation-pretrained policy — the from-scratch online learner is the part that lost, not the model-based idea.

## What online MBRL still owns

- **Agile control with a clean reward.** Where a reward *is* specifiable and dynamics are fast and contact-rich — legged locomotion, drone racing — RL in sim remains SOTA, and [S5WM](../../sources/s5wm-paper.md) (real racing quadrotors, [Scaramuzza](../../concepts/robotics/agentic-uavs.md) lab) shows the frontier there is now wall-clock, not sample count.
- **New embodiment, no usable prior, expensive interaction.** When there's nothing to pretrain from and a simulator is unavailable, MBRL's core sample-efficiency pitch still holds — DayDreamer's actual sweet spot.

## Related

- [DayDreamer](../../sources/daydreamer-paper.md) — the 2022 high-water mark this page interrogates.
- [Dreamer / DreamerV3](../../entities/dreamer.md) — the algorithm family; [Danijar Hafner](../../entities/danijar-hafner.md) — its through-line.
- [TRI LBM paper](../../sources/tri-lbm-paper.md) — multitask-pretraining-buys-robustness, and the static-policy evaluation methodology.
- [Automated Podcast — Tedrake](../../sources/automated-podcast-tedrake-rocket-ship.md) — the "build a bridge" data reframe and "deployment is the milestone."
- [VLA models](../../concepts/learning/vla-models.md) / [Large behavior models](../../concepts/learning/large-behavior-models.md) — the winning paradigm.
- [Imitation learning](../../concepts/learning/imitation-learning.md) — its substrate, incl. the RL-as-post-training coda ([π*0.6](../../entities/pistar06.md)).
- [Robot safety standards](../../concepts/robotics/robot-safety-standards.md) — why on-robot exploration doesn't fit the certification model.
- [World model](../../concepts/world-models/world-model.md) — where the model-based machinery migrated.
- [Atari RL lineage](atari-rl-lineage.md) — the "the benchmark moved on, the toolbox stayed" companion, one level down.

## Open questions

- Does the pretrain-then-RL stack eventually re-privilege *online* interaction (RL post-training is the fastest-growing piece)? MBRL-for-post-training — a world model to imagine fine-tuning rollouts — is an under-explored corner.
- Does a video/world-model-backbone LBM (Tedrake's stated bet) beat VLM-backbone VLAs — i.e. does the world model win as the *policy* backbone after all?
- Is there a real-robot task class where DayDreamer-style online MBRL is still the best answer in 2026, or has sim + pretraining swallowed all of it?
