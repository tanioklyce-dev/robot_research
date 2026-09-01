---
title: "SimToolReal: An Object-Centric Policy for Zero-Shot Dexterous Tool Manipulation (Kedia, Lum, Bohg & Liu, RSS 2026)"
type: source
url: https://arxiv.org/abs/2602.16863
fetch_url: https://arxiv.org/pdf/2602.16863v1
local_path: raw/simtoolreal_2602.16863.pdf
sha256: a7f9d4b30c2aea84bd4db53272bc8bc8ed4fcbaeab627a688b9675beca53c05f
author: "Kushal Kedia*, Tyler Ga Wei Lum*, Jeannette Bohg†, C. Karen Liu† (*equal contribution, †equal advising)"
affiliations: Cornell University; Stanford University
published: 2026-02-18
venue: Robotics: Science and Systems (RSS) 2026
tags: [simtoolreal, dexterous-manipulation, tool-use, sim-to-real, rl, zero-shot, object-centric, in-hand-manipulation, procedural-generation, dextoolbench, sharpa, kuka, sapg, primary-source]
ingested: 2026-08-31
---

## Summary

> [!note] Presented at the [third World Modeling Workshop](chicago-booth-world-modeling-workshop-2026.md) (Chicago Booth, 2026-08-31, ~03:00) in [Bohg](../entities/jeannette-bohg.md)'s invited talk on world models from a robotics perspective.


**SimToolReal** trains **one** goal-conditioned RL policy in simulation on **procedurally generated tool-like primitives**, then deploys it zero-shot on real tools it has never seen. The reduction that makes this work is stated plainly: **a tool-use task is a sequence of object goal poses.** That replaces per-task reward engineering — the thing that makes sim-to-real RL expensive — with a single universal objective: move any object to any goal pose.

The training objective never mentions hammering, sweeping, or unscrewing. Yet reaching random goal poses on random primitives *induces* the skills tool use needs — grasping thin objects off a flat table, in-hand reorientation into a functional configuration, and holding the grasp through contact. At test time the policy takes a goal sequence extracted from a human RGB-D video and tracks it.

Results: **37% over retargeting and fixed-grasp baselines**, **matching specialist RL policies** trained on the specific object and trajectory, and **120 real-world rollouts across 24 tasks, 12 object instances, and 6 tool categories** — all unseen in training. Hardware is a **22-DoF [Sharpa](../entities/sharpa-wave.md) five-fingered hand on a 7-DoF KUKA iiwa 14** (29 DoF total), at 60 Hz.

> [!note] Why this matters beyond tool use
> The wiki's [sim-to-real](../concepts/learning/sim-to-real-transfer.md) coverage is mostly locomotion, where the "task" is a velocity command and generalization means terrain. This is the manipulation analogue done properly: **the generalization axis is the object**, and the paper shows that a task-agnostic training objective on synthetic geometry transfers to real tools without a single real demonstration of the task. It is also a direct rebuttal to the [teleoperation-data orthodoxy](../concepts/world-models/belief-states-and-mixed-states.md) — the authors' opening argument is that teleoperation is a *poor fit* for dexterous tool data because of the human-to-robot correspondence gap.

## The method

**Problem form.** Learn `aₜ = π_θ(sₜ, oₜ, φ, g)` — proprioception, current object 6D pose, a coarse object descriptor, and a goal pose → joint position targets for arm and hand. Execution is "reach the current goal, advance to the next when `d(oₜ, g) < ε`."

**Reward** (Eq. 1–2): `r = r_smooth + r_grasp + I_grasped · r_goal`, with

`r_goal = max(d* − d(oₜ,g), 0) + B_succ · I[d(oₜ,g) < ε]`

`d*` tracks the **minimum distance achieved so far** and resets on a new goal, so **positive reward is only given for progress** — this is what stops the agent from parking near the goal and farming the dense term. Pose distance is `max_i ‖oₜ,ᵢ − gᵢ‖` over `D = 4` keypoints in the object frame.

**Procedural tools.** Each primitive is a **handle + head**, sampled as cylinders and cuboids of varying dimensions, with **independently randomized densities** for handle and head (hammer heads are denser than handles). Crude, and deliberately so — it spans the structural variation of brushes, spatulas, markers and hammers.

**Object-centric inputs — the sim-to-real move.** The policy gets only what is *reliably measurable at deployment*: the **6D pose** and a **coarse 3D grasp-region bounding box** (center + extents, fixed for the episode). No detailed geometry, no physical parameters. An **LSTM** backbone lets it infer the unobserved properties from interaction history. The authors place this in the lineage of **DexFunc** and [**RMA**](rma-paper.md) — reduce the observation gap by refusing to depend on quantities you cannot estimate.

**Deployment pipeline** (Fig. 3): RGB-D human video → **SAM 3D** for a metric-scale mesh and 3D grasp bounding box → **FoundationPose** for a sequence of 6D goal poses → LSTM policy → joint targets.

## Results

**Zero-shot on DexToolBench** (Fig. 4) — 24 trajectories × 6 categories × 12 instances, 5 trials each = 120 rollouts. Metric is **Task Progress**, the percentage of demonstrated goal poses reached at `ε = 2 cm`. Explicitly *trajectory following, not functional task completion*.

The failure structure is more informative than the headline:

| Failure mode | Share |
|---|---|
| Pose tracking loss | **43.7%** |
| Object drops | 34.5% |
| Incomplete in-hand rotation | 18.2% |
| Grasp failure | 3.6% |

**Nearly half of all failures are perception, not control.** And the policy shows **strong recovery** — on a drop it consistently re-grasps, provided the object stays in the workspace and pose tracking holds.

Difficulty tracks physics as you'd expect: **eraser** and **marker** are easiest (translation-dominated, no in-hand rotation), though the marker's thinness costs grasp reliability and its size invites occlusion. **Thinner is harder** (3 cm spoon spatula > 1 cm flat spatula) and **heavier is harder** (36 g claw hammer > 331 g mallet). **Screwdriver is worst** — it needs functional reorientation *and* continuous spinning.

**Against baselines** (Fig. 5), on sweeping with a brush, two variations:

| Method | V1 (no rotation needed) | V2 (90° tool rotation) |
|---|---|---|
| **SimToolReal** | **98.0%** | **82.7%** |
| Fixed Grasp | 61.0% | 10.8% |
| Kinematic Retargeting | 8.1% | 0% |

Retargeting fails to even grasp — kinematic motion establishes no stable contact. Fixed Grasp works when the arm alone suffices, then **collides with the table** when a 90° rotation is required, because no arm trajectory satisfies the rotation without collision. That is the paper's cleanest argument for in-hand manipulation: **the arm does not have the workspace.**

**Against specialists** (Fig. 6). Specialists trained per-category match SimToolReal on their own training object and trajectory — and collapse under either variation. Change the *trajectory* (same object) and the specialist tracks only the first few lifting goals; change the *object instance* (red brush → blue brush, same trajectory) and it does worse still. **The generalist matches the specialist on the specialist's home turf while also generalizing.**

**The objective is a valid proxy** (Fig. 7). Training reward on random-goal-reaching over primitives and zero-shot Task Progress on DexToolBench rise together across checkpoints. This is the load-bearing validation: it says the synthetic objective is not merely correlated with the real task but *drives* it.

**Ablations** (Fig. 8, 5 seeds). Two components are each individually critical:
- **SAPG instead of PPO** — PPO "suffers from exploration saturation at scale"; SAPG trains separate policies over environment chunks and fuses gradients by importance sampling.
- **Asymmetric critic** — giving the critic privileged simulator state. Forcing it onto the actor's partial observations "severely hinders learning," which is a direct consequence of the task's partial observability.

## Stated limitations

- **Goal tracking ≠ task completion**, especially for high-force interactions. The eval measures pose tracking; whether the nail goes in is a different question.
- **Environment-blind** — conditioning on object pose alone invites collisions in clutter.
- **Rigid tools only** — pose cannot describe scissors.
- **The goal sequence is fixed, never replanned.**

## Entities mentioned

- [Sharpa Wave hand](../entities/sharpa-wave.md) — the 22-DoF hand, donated by Sharpa, who also gave technical support. Same hand the wiki already tracks via [EgoScale](egoscale-paper.md).
- **KUKA iiwa 14** — 7-DoF arm. No wiki page.
- [Jeannette Bohg](../entities/jeannette-bohg.md), **C. Karen Liu** (Stanford), **Kushal Kedia** (Cornell), **Tyler Ga Wei Lum** (Stanford).
- **DexToolBench** — released benchmark: 6 tool categories, 12 instances, 24 trajectories; assets, training and eval code open-sourced at `github.com/tylerlum/simtoolreal`.
- **SAM 3D**, **FoundationPose** — the perception stack; FoundationPose also appears in [GraspGen-X](graspgenx-paper.md).
- **SAPG**, **PPO**, **Asymmetric Critic**, **Isaac Gym** — training stack.
- Funders: Stanford HAI, ONR Young Investigator, NSF, NSERC.

## Concepts touched

- [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md) — the concept page this anchors.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the manipulation-side counterpart to the wiki's locomotion-heavy coverage.
- [RMA](rma-paper.md) — the named ancestor for "infer the unobservable from interaction history rather than measuring it."
- [Six-DoF grasp generation](../concepts/robotics/six-dof-grasp-generation.md) — the fixed-grasp paradigm this argues past.
- [Imitation learning](../concepts/learning/imitation-learning.md) — the alternative the introduction explicitly rejects for this task class.

## Open questions

- **Does the "universal goal-reaching objective" generalize past tools?** Handle-plus-head is a strong prior. Articulated objects, deformables, and multi-object assembly are all outside it, and the follow-up work (**"Play to Perfect"**, mentioned by the authors in talks) targets precision assembly specifically — the regime where this policy's success rate falls off as tolerance tightens.
- **43.7% of failures are pose-tracking loss.** The policy is arguably better than its evaluation shows, and the binding constraint is FoundationPose under occlusion — a perception problem the robot-learning community usually treats as solved infrastructure. Worth comparing against the [Physion-Eval](physion-eval-paper.md) finding that the measurement layer is often the weak link.
- **Would this survive a compression test?** [Vafa et al.](vafa-world-model-implicit.md) find that models trained on random/synthetic coverage recover more structure than models trained on real expert data. SimToolReal is exactly the random-coverage regime, and it beats specialists trained on real trajectories. That is independent corroboration from robotics of a result the wiki so far only has from navigation and Othello — **nobody has connected them**.
