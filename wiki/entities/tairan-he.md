---
title: Tairan He
type: entity
subtype: person
created: 2026-08-29
updated: 2026-08-29
sources: 4
tags: [tairan-he, cmu, nvidia-gear, humanoid, whole-body-control, teleoperation, h2o, hover, asap]
---

**Tairan He** — CMU researcher (LeCAR Lab, with [Guanya Shi](../concepts/robotics/whole-body-control.md) and Changliu Liu), with NVIDIA affiliation on the later work. **Co-first author of four of the five papers in this wiki's humanoid whole-body-control corpus** — [H2O](../sources/h2o-paper.md), [OmniH2O](../sources/omnih2o-paper.md), [ASAP](../sources/asap-paper.md) and [HOVER](../sources/hover-paper.md).

That makes him to humanoid WBC roughly what [Deepak Pathak](deepak-pathak.md) is to quadruped adaptation in this wiki: the single author whose name traces the whole arc.

## The four papers, and what each attacks

The set is unusually well-organized — read together they are four distinct cuts at *"the robot is not the human, and the simulator is not the world."*

| Paper | Year | The gap it attacks |
|---|---|---|
| [H2O](../sources/h2o-paper.md) | 2024 | **Infeasible data** — filter motions the robot physically cannot do |
| [OmniH2O](../sources/omnih2o-paper.md) | 2024 | **Interface fragmentation** — kinematic pose as one universal command channel |
| [HOVER](../sources/hover-paper.md) | 2024 | **Mode fragmentation** — one distilled policy covering every control mode |
| [ASAP](../sources/asap-paper.md) | 2025 | **Dynamics mismatch** — a residual action model that corrects the simulator |

Three of the four are built on **privileged oracle-to-student distillation**; ASAP is the exception, and instead corrects the simulator itself. See [humanoid WBC lineage](../syntheses/rl/humanoid-wbc-lineage.md).

## Why it matters in this wiki

- **He is the bridge from academic humanoid control into [NVIDIA GEAR](nvidia-gear.md).** [HOVER](../sources/hover-paper.md) and [ASAP](../sources/asap-paper.md) put him alongside Jim Fan and Yuke Zhu, and [GEAR](nvidia-gear.md)'s later SONIC line builds on exactly this foundation.
- **The consistency of the collaborator set** — Zhengyi Luo, Wenli Xiao, Kris Kitani, Changliu Liu, Guanya Shi recur across all four — is why the papers compose instead of overlapping. This is one research program published in instalments, not four separate attempts.

## Related

- [NVIDIA GEAR](nvidia-gear.md) — his industrial affiliation on HOVER and ASAP.
- [Unitree H1](unitree-h1.md) / [Unitree G1](unitree-g1.md) — the platforms (H1 for the H2O line, G1 for ASAP).
- [Whole-body control](../concepts/robotics/whole-body-control.md) — the concept his work anchors.
- [Deepak Pathak](deepak-pathak.md) — the equivalent through-line author on the quadruped side.

## Mentioned in

- [H2O](../sources/h2o-paper.md) — co-first author.
- [OmniH2O](../sources/omnih2o-paper.md) — co-first author.
- [HOVER](../sources/hover-paper.md) — co-first author.
- [ASAP](../sources/asap-paper.md) — co-first author.

## Open questions / TBD

- **Current affiliation** — CMU, NVIDIA, or both, as of 2026, is not established here.
- **Co-authors without pages**: Guanya Shi, Changliu Liu, Kris Kitani, Zhengyi Luo and Wenli Xiao all appear in three or more of these ingested sources.
