---
title: AMASS
type: entity
subtype: dataset
created: 2026-08-29
updated: 2026-08-29
sources: 3
tags: [amass, dataset, human-motion, mocap, smpl, retargeting, humanoid, whole-body-control]
---

**AMASS** — a large unified archive of human motion-capture data, expressed in the SMPL body model, and **the substrate almost all learned humanoid whole-body control is built on**. Humanoid policies in this wiki are usually trained to track *retargeted AMASS motions*: AMASS → SMPL → inverse kinematics onto the robot's kinematic tree → a reference trajectory an RL policy learns to follow ([whole-body control](../concepts/robotics/whole-body-control.md)).

Its role is the humanoid field's answer to the robot-data bottleneck: rather than collecting robot demonstrations, **borrow the human motion corpus and pay a retargeting cost.**

## The retargeting cost is the interesting part

Retargeting is not free, and this wiki's sources document two distinct failures it causes:

- **Infeasible motions.** [H2O](../sources/h2o-paper.md) notes that "the significant dynamics discrepancy between humans and humanoids means that some human motions could be infeasible for the humanoid — e.g. cartwheeling, steps wider than the leg lengths of the humanoid." Its **sim-to-data** procedure trains a privileged imitator purely to *find and delete* these, and removing that filter costs 4.6 points of success.
- **Distributional imbalance.** [OmniH2O](../sources/omnih2o-paper.md) found the retargeted distribution has to be deliberately **biased toward standing and squatting**, or the policy never learns to hold the lower body steady while the upper body manipulates.

So a human-motion corpus is not a drop-in robot dataset. It is a *raw material* requiring feasibility filtering and deliberate reweighting — and both papers treat that curation as a first-class contribution rather than preprocessing.

## Related

- [Whole-body control](../concepts/robotics/whole-body-control.md) — where retargeted AMASS is consumed.
- [H2O](../sources/h2o-paper.md) — the feasibility-filtering ("sim-to-data") argument.
- [OmniH2O](../sources/omnih2o-paper.md) — the distribution-shaping argument.

## Mentioned in

- [H2O](../sources/h2o-paper.md) — 10k retargeted sequences; the evaluation corpus.
- [OmniH2O](../sources/omnih2o-paper.md) — large-scale retargeting and augmentation.

## Open questions / TBD

- **No primary ingested.** Everything here comes from papers that *use* AMASS; the dataset's own paper (Mahmood et al., ICCV 2019), size, licence and composition are not established in this wiki.
- **Does [HumanPlus](../sources/humanplus-paper.md)'s "40-hour human motion dataset" overlap AMASS?** Not stated in the ingested text, and it matters for comparing the Stanford and CMU systems.
