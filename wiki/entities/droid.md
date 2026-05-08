---
title: DROID
type: entity
subtype: dataset
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [droid, dataset, teleoperation, franka, robot-data, stanford, berkeley, oxe]
---

**DROID — Distributed Robot Interaction Dataset.** Large-scale **real-robot teleoperation dataset** of Franka Panda manipulation collected across diverse real-world environments. Designed as a step beyond [[robot-utility-models|RUM]]-class single-platform corpora and the Open-X Embodiment aggregated multi-platform corpus, by emphasizing **scene diversity** rather than embodiment diversity. Released April 2024 by a 13-institution consortium led by Alexander Khazatsky and Karl Pertsch, with Chelsea Finn and Sergey Levine senior. Project page: https://droid-dataset.github.io/. Primary paper: arxiv 2403.12945.

## Composition (latest figures)
- **76,000 demonstration trajectories**
- **350 hours of interaction data**
- **564 distinct scenes** across **86 distinct tasks**
- **50 human data collectors**
- **12-month collection period**, with updates released December 2024 and April 2025.
- Long-tail task distribution over a wide range of everyday manipulation objects.

## Hardware
- **Robot**: Franka Panda 7-DOF arm — single embodiment across the entire dataset.
- **Cameras**: two adjustable **ZED 2** stereo cameras (third-person) + one wrist-mounted **ZED Mini** stereo. All views recorded as stereo video.
- **Teleop interface**: **Oculus Quest 2** headset + controllers.

The choice of stereo cameras throughout (rather than mono RGB) makes DROID unusual — it preserves depth information that downstream world models or vision-language-action policies can exploit.

## Comparison to other datasets
The DROID team explicitly compares against:

- **Open-X Embodiment (OXE)** — DROID-trained policies outperform OXE-trained policies by **+22% absolute success rate in-distribution** and **+17% out-of-distribution**. The pitch: scene diversity at fixed embodiment beats embodiment diversity at limited scenes.
- **Bridge V2, RH20T, RT-1** — DROID has "an order of magnitude more scenes" with greater skill diversity than these.

> [!note] The OXE comparison is the load-bearing claim
> The "+22% / +17%" numbers come from the DROID team's own evaluation. Independent reproduction would strengthen the case; the wiki has not ingested an external benchmarking source.

## Why it matters in this wiki
DROID is the **dominant real-robot dataset cited across the JEPA-for-robotics literature**:

- **[[v-jepa-2|V-JEPA 2]]** ([[v-jepa-2-paper|paper]]) — V-JEPA 2-AC post-trained on **62 hr of unlabeled DROID robot videos** (a subset of the full 350 hr); zero-shot Franka manipulation in two new labs followed.
- **[[jepa-wms|JEPA-WMs]]** ([[jepa-wms-paper|paper]]) — uses the **raw DROID dataset in stereo HD (8.7 TB)** or **non-stereo HD-only video (5.6 TB)** as one of the training/eval data sources alongside RoboCasa, Metaworld, and a real Franka.

This makes DROID the single most reused real-robot dataset in the JEPA literature ingested here. It also features in the [[sim-heavy-vs-real-data-paths|sim-heavy vs real-data paths synthesis]] as the substrate for the "observation-pretraining + small real teleop" path to generalist policies — without DROID, V-JEPA 2's "62 hr → zero-shot Franka" existence proof would not exist.

## Distribution
- **TensorFlow Datasets**: `gs://gresearch/robotics`.
- **Hardware code (data-collection rig)**: https://github.com/droid-dataset/droid
- **Policy-learning baselines**: https://github.com/droid-dataset/droid_policy_learning
- **Updated annotations on HuggingFace**: https://huggingface.co/KarlP/droid

## Authors and institutions
13 institutions; lead authors **Alexander Khazatsky** and **Karl Pertsch**. Senior authors **Chelsea Finn** and **Sergey Levine**. Stanford and Berkeley lead, with collaborators across North America, Asia, and Europe.

## Open questions / TBD
- DROID **paper itself** (arxiv 2403.12945) is not yet a source page in this wiki — the entity here is built from the project page; ingesting the paper would let us cite design-decision rationale (why stereo, why Franka-only, why 13-institution distributed collection) directly.
- **License terms** not surfaced from the project page; needs paper-body or repo-LICENSE check before downstream-use claims.
- The Dec 2024 + Apr 2025 update deltas are not documented here; if the dataset has materially grown or changed task mix, this entity should reflect that.

## Related
- Franka Panda — single robot platform across the dataset.
- [[v-jepa-2|V-JEPA 2]] — primary JEPA consumer.
- [[jepa-wms|JEPA-WMs]] — secondary JEPA consumer; uses the raw dataset.
- [[robot-utility-models|Robot Utility Models]] — alternative real-robot data philosophy (mobile-manipulation, single embodiment, Stretch).
- [[sim-heavy-vs-real-data-paths|Sim-heavy vs real-data paths synthesis]] — DROID is the empirical anchor of path C (observation pretraining + small real teleop).
- [[why-jepa-research-skips-the-simulator-stack|Why JEPA research skips the simulator stack]] — DROID's role in JEPA-for-robotics evaluations is part of why JEPA work has been able to skip / fragment sim use.

## Mentioned in
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]
