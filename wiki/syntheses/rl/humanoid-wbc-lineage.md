---
title: Humanoid whole-body control lineage — teleoperation first, and why this branch kept its teachers
type: synthesis
created: 2026-08-29
updated: 2026-08-29
tags: [humanoid, whole-body-control, teleoperation, privileged-distillation, h2o, hover, asap, humanplus, history, lineage]
---

# Humanoid whole-body control lineage

Five papers from 2024–25, mostly one CMU group with NVIDIA joining late, plus one independent Stanford system. Companion to the [locomotion adaptation lineage](locomotion-adaptation-lineage.md) — and the comparison between the two is the reason this page exists, because **the two branches of learned legged control moved in opposite architectural directions at the same time.**

## The corpus

| Paper | Lab | Attacks | Mechanism |
|---|---|---|---|
| [H2O](../../sources/h2o-paper.md) (IROS 2024) | CMU | infeasible **data** | privileged imitator filters un-trackable retargeted motions |
| [OmniH2O](../../sources/omnih2o-paper.md) (CoRL 2024) | CMU + SJTU | fragmented **interfaces** | kinematic pose as one universal command channel |
| [HumanPlus](../../sources/humanplus-paper.md) (CoRL 2024) | Stanford | the **whole loop** | shadowing → teleop data → BC from egocentric vision |
| [HOVER](../../sources/hover-paper.md) (2024) | NVIDIA + CMU | fragmented **modes** | multi-mode distillation with mode + sparsity masks |
| [ASAP](../../sources/asap-paper.md) (2025) | CMU + NVIDIA | **dynamics** mismatch | residual *action* model folded into the simulator |

Read as a set, they are four cuts at one sentence: *the robot is not the human, and the simulator is not the world.*

## What is distinctive about this branch

**It started from teleoperation, not autonomy.** The quadruped line asked how a robot handles terrain it was not trained on. The humanoid line asked how a *human* can drive a humanoid well enough to generate data — and treated autonomy as the thing that data later buys. [H2O](../../sources/h2o-paper.md) says so directly: RGB-camera teleoperation could "pave the way for collecting large-scale humanoid data for training autonomous agents." [OmniH2O](../../sources/omnih2o-paper.md) and [HumanPlus](../../sources/humanplus-paper.md), one month apart at different institutions, both close that loop.

**The data is human, so curation is a research contribution.** Everything here runs on retargeted [AMASS](../../entities/amass.md) or equivalent. Because human motion is not humanoid-feasible motion, two papers make *dataset shaping* a headline result rather than preprocessing: H2O deletes infeasible motions with a privileged imitator (worth 4.6 points), OmniH2O deliberately skews the distribution toward standing and squatting so the lower body learns to be stable while the upper body works.

**And the justification for the form factor is load-bearing.** H2O notes that if lower-body tracking is unnecessary, "the robot could opt for designs with better stability, such as a quadruped or wheeled configuration." Whole-body control is the argument for having legs at all.

## The divergence — and a guess at why

By 2025 the quadruped line had **abandoned privileged teachers**: [LocoFormer](../../sources/locoformer-paper.md) trains end-to-end RL with long context and no oracle, and calls the earlier privileged-distillation work myopic. Over exactly the same period, the humanoid line **doubled down on them** — H2O distils to filter data, OmniH2O to reach sparse sensors, HOVER to unify modes, [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) to merge experts. Only ASAP declines, and it substitutes a different privileged object: a learned correction to the simulator.

Two branches, same years, opposite directions. The most plausible reading from what these papers say about themselves:

- **The humanoid reference signal is external and expensive.** Quadruped RL invents its own targets from a reward function; humanoid WBC must *track a specific human motion*. When a well-defined target exists but the deployable sensors cannot see enough to hit it, distillation from something that can see is the natural tool. RMA had the same structure and abandoned it when context got cheap — but a humanoid tracking AMASS still has an oracle worth distilling, because the oracle knows the reference.
- **The action space is much larger.** 19–33 DoF against 12, with balance constraints that punish exploration harshly. End-to-end RL over that, without a teacher, is a far more expensive proposition than LocoFormer's quadruped distribution.
- **[HOVER](../../sources/hover-paper.md) supplies the strongest reason to keep teachers**: its distilled generalist **beats specialist policies in their own modes**, and the authors note that this holds "even when focusing on a single control mode." If distillation is not a compromise but an improvement, there is no pressure to remove it.

> [!note] What would falsify this reading
> A humanoid WBC result that matches distilled controllers using end-to-end RL with long context and no oracle. The [locomotion lineage](locomotion-adaptation-lineage.md) suggests such a paper becomes possible when the compute budget rises far enough — and [ASAP](../../sources/asap-paper.md)'s use of a *learned simulator correction* rather than a teacher is arguably the first step in that direction.

## Corrections this ingest produced

The wiki referenced all five of these papers **secondhand** — as names in [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md), [SONIC](../../sources/sonic-paper.md) and the [GEAR publications page](../../sources/nvidia-gear-publications.md) — before any was ingested. Reading the primaries settled one open question already sitting in the wiki:

**ASAP's global delta-action model does leave motion-dependent error on the table.** ASAP asserts its model is "trained across multiple motions and is not overfitted." [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) later found **per-cluster delta models beat one global model**, because cluster-consistent dynamics fit better. Not a contradiction, but a real refinement — recorded on both [ASAP](../../sources/asap-paper.md) and [whole-body control](../../concepts/robotics/whole-body-control.md).

## Where it connects

- **[Whole-body control](../../concepts/robotics/whole-body-control.md)** — the concept page; these five are now its ingested foundation rather than referenced names.
- **[Locomotion adaptation lineage](locomotion-adaptation-lineage.md)** — the quadruped branch that went the other way.
- **[Tairan He](../../entities/tairan-he.md)** — co-first author on four of the five.
- **[Zipeng Fu](../../entities/zipeng-fu.md)** — HumanPlus co-lead, and the only person in this wiki spanning quadruped locomotion ([RMA](../../sources/rma-paper.md)), mobile manipulation ([Mobile ALOHA](../../sources/mobile-aloha-paper.md)) and humanoid WBC.
- **[NVIDIA GEAR](../../entities/nvidia-gear.md)** — where this academic line joins industry, and what [SONIC](../../sources/sonic-paper.md) builds on.

## Open follow-ups

- **Exbody2** is the one named member of this cluster still uningested.
- **Real-world quantitative results are thin across the board.** H2O's table is simulation; ASAP's extracted tables are simulator-to-simulator; HOVER's comparison is tracking metrics. The [success-rate audit](../platforms/vla-success-rate-audit.md) applies to all of it.
- **Nobody has compared the CMU and Stanford systems directly** — different robots, different datasets, different metrics, one month apart.
- **[AMASS](../../entities/amass.md) has no ingested primary**, despite being the substrate under most of this page.
