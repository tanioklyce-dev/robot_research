---
title: DAgger and interactive imitation
type: concept
created: 2026-11-16
updated: 2026-11-16
sources: 16
tags: [dagger, dataset-aggregation, interactive-imitation, hg-dagger, human-gated, covariate-shift, compounding-error, behavior-cloning, teacher-student, policy-distillation, privileged-learning, sim-to-real, data-flywheel, failure-recovery]
---

# DAgger and interactive imitation

## Definition

**DAgger (Dataset Aggregation)**, from Ross, Gordon and Bagnell (AISTATS 2011, [arXiv 1011.0686](https://arxiv.org/abs/1011.0686)), fixes the central failure of [behavior cloning](imitation-learning.md). A BC policy is trained only on states the expert visited, so its first mistake takes it somewhere it has never seen, and errors **compound across time**. DAgger closes the loop: roll out the current policy, have an expert label the *states the policy actually reached* with the right action, add those to the dataset, retrain, and repeat ([glossary](../../glossary.md#dagger); [curriculum module 6](../../syntheses/curriculum/curriculum-06-imitation-learning.md)). The training distribution then converges toward the policy's own state distribution, the one it will be tested on.

The original paper is not ingested here. The definition above is textbook background, and everything below is how this wiki's sources use the idea.

## One name, four mechanisms

"DAgger" in this wiki's sources covers four different things. They share the loop (act, have something better label where you went, retrain), but they differ in **who the expert is** and **what gets labelled**.

| Family | Expert | What it fixes | Examples |
|---|---|---|---|
| **1. Teacher–student distillation** | A privileged RL policy in simulation | The student can't see what the teacher saw (terrain heights, object state) | [RMA](../../sources/rma-paper.md)'s adaptation module, trained on-policy *"à la DAgger"* because a module trained on clean expert trajectories *"would not be robust to deviations"*. [Egocentric-vision locomotion](../../sources/egocentric-vision-locomotion-paper.md) distils to depth + proprioception with DAgger and truncated BPTT. [HOVER](../../sources/hover-paper.md) is multi-mode distillation with command masks. DextrAH-RGB is distilled into a stereo-RGB student and deployed on [Atlas](../../entities/atlas.md) ([R²D² dexterous digest](../../sources/nvidia-r2d2-dexterous-robots-blog.md)). [Bumblebee](../../sources/bumblebee-experts-to-generalist-wbc.md) distils experts into one WBC transformer. |
| **2. Human-gated correction (HG-DAgger)** | A human who takes over when the policy goes wrong | Recovery from the policy's own failure states, on the real robot | [π\*0.6](../../entities/pistar06.md)'s optional human interventions. [GR00T 2](../../sources/gr00t-2-whitepaper.md)'s assembly: SFT 23–69 → **+DAgger 71–84** → +agent with recovery skills 97–98 of 100. [GR00T N1.6](../../sources/groot-n1_6.md) recommends DAgger for real-world use. |
| **3. Iterative data curation** | The human demonstrator, steered by observed failures | Demo coverage, not on-policy labels: collect *against* failure modes | [X-VLA](../../sources/xvla-paper.md)'s Soft-Fold set: retrain [ACT](../../entities/act.md) every 100 episodes, find its failure modes, collect targeted demos, about 1,200 episodes and 50–60 operator-hours. Recommended for this wiki's own [XLeRobot bring-up](../../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md). |
| **4. A planner or simulator as the expert** | A classical planner, or the true simulator | Failure states labelled automatically, no human | [ToyBlocks](../../sources/allenai-toyblocks-github.md)' **TAMPER**: DAgger with a [TAMP](../robotics/task-and-motion-planning.md) expert, replanning from where the policy failed. **Online World Modeling** ([train–test gap paper](../../sources/train-test-gap-world-models-paper.md)): execute the planner's actions in the real simulator and retrain the world model on the corrected trajectory. [RoboTwin 2.0](../../sources/robotwin2-paper.md) uses a VLM failure localiser in the same loop. |

There is also a fifth, recent reading. **[RoboTTT](../../sources/robottt-paper.md)'s *DAgger Distillation*** keeps the robot's own failed rollout **in context** and trains on the corrections, which is explicitly Algorithm Distillation ([in-context robot learning](in-context-robot-learning.md)). The loop happens inside one episode rather than across training rounds.

> [!note] Why the distinction matters
> Families 1 and 4 are cheap: the expert is software, so labelling is free and the loop can run millions of times. Family 2 costs an operator in the loop for every correction. Family 3 is not DAgger in the strict sense, because no one labels the policy's own states; it is coverage-driven collection. A claim like "trained with DAgger" says little until you know which one.

## Evidence on what it buys

- **Real-robot assembly:** on [GR00T 2](../../sources/gr00t-2-whitepaper.md)'s assembly tasks, adding DAgger to SFT moves 23–69 up to 71–84 of 100. It is the largest single step in the stack, though the last 13–27 points needed an agent with recovery skills.
- **Against RL on the same data:** [HIL-SERL](../../sources/hil-serl-paper.md) uses the same human-takeover mechanic but trains with RL, and beats an **HG-DAgger** baseline on the same human data by **+101% success and 1.8× faster cycle time** across seven tasks ([real-world robot RL](real-world-robot-rl.md)). Its reading: RL optimizes the task reward and self-corrects, while HG-DAgger can only imitate the corrections it was given.
- **Corrections can hurt, or at least fail to help:** in [RT-H](../../sources/rt-h-paper.md), DAgger-style teleoperated corrections (IWR) took RT-2 from 25% to 13%. That drop is **borderline** (p = 0.053, 80 trials, per the source page's own significance check). The solid result is the comparison: corrections given in **language-motion space** reached 63% against IWR's 13% (p < 0.0001). The authors' explanation is that teleop actions sit too far from the base policy's distribution. So the representation the expert corrects in matters as much as the correction.
- **Navigation:** the strong VLN baselines all use DAgger augmentation, and [GA-VLN](../../sources/ga-vln-paper.md) matches them without it ([visual navigation policies](../robotics/visual-navigation-policies.md)).

## Related concepts

- [Imitation learning](imitation-learning.md) — the compounding-error problem DAgger exists to fix
- [Real-world robot RL](real-world-robot-rl.md) — human-gated RL as the alternative to HG-DAgger
- [Sim-to-real transfer](sim-to-real-transfer.md) — teacher–student distillation as the standard two-phase recipe
- [Whole-body control](../robotics/whole-body-control.md) — DAgger distillation of humanoid controllers
- [In-context robot learning](in-context-robot-learning.md) — DAgger Distillation, the in-episode variant
- [Synthetic data flywheel](synthetic-data-flywheel.md) — planner-expert DAgger as a data generator
- [Gradient-based planning](../world-models/gradient-based-planning.md) — Online World Modeling, DAgger applied to the world model rather than the policy

## Current state

DAgger is no longer one algorithm; it is the default *shape* of a robot-learning loop. In 2026 its most common use in this wiki is **teacher–student distillation** from privileged simulation policies, where the expert is free. On real robots, human-gated corrections are the norm for frontier VLAs (π\*0.6, GR00T 2), but [HIL-SERL](../../sources/hil-serl-paper.md) shows RL on the same interventions does better. The open edges are what the expert corrects in (actions vs language-motion, per RT-H), how to get failure states labelled without a human (planners, simulators, VLM localisers), and whether in-context correction (RoboTTT) can replace retraining rounds altogether.

## Mentioned in

> [!note] Curated list — about 25 source pages use the term; the ones below shaped this page.

- [GR00T 2 whitepaper](../../sources/gr00t-2-whitepaper.md) — SFT → DAgger → agent ladder on real assembly
- [HIL-SERL](../../sources/hil-serl-paper.md) — RL beats HG-DAgger on the same human data
- [RT-H](../../sources/rt-h-paper.md) — when teleop corrections hurt
- [X-VLA](../../sources/xvla-paper.md) — DAgger-style iterative curation for cloth folding
- [RMA](../../sources/rma-paper.md), [Egocentric-vision locomotion](../../sources/egocentric-vision-locomotion-paper.md), [HOVER](../../sources/hover-paper.md) — teacher–student distillation
- [ToyBlocks GitHub](../../sources/allenai-toyblocks-github.md) — TAMPER, DAgger with a planner expert
- [Train–test gap in world models](../../sources/train-test-gap-world-models-paper.md) — Online World Modeling
- [RoboTTT](../../sources/robottt-paper.md) — DAgger Distillation in context
- [π\*0.6](../../sources/pistar06-paper.md) — human-gated DAgger in a value-conditioned VLA loop
