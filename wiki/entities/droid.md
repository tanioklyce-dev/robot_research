---
title: DROID
type: entity
subtype: dataset
created: 2026-05-07
updated: 2026-07-25
sources: 20
tags: [droid, dataset, teleoperation, franka, robot-data, stanford, berkeley, oxe, molmoact2]
---

**DROID — Distributed Robot Interaction Dataset.** Large-scale **real-robot teleoperation dataset** of Franka Panda manipulation collected across diverse real-world environments. Designed as a step beyond [RUM](robot-utility-models.md)-class single-platform corpora and the **[Open X-Embodiment (OXE)](open-x-embodiment.md)** aggregated multi-platform corpus, by emphasizing **scene diversity** rather than embodiment diversity. (DROID is **also a constituent of OXE** — DROID = the Franka-Panda-only subset; OXE = the 22-embodiment umbrella.) Released April 2024 by a 13-institution consortium led by Alexander Khazatsky and Karl Pertsch, with Chelsea Finn and Sergey Levine senior. Project page: https://droid-dataset.github.io/. Primary paper: arxiv 2403.12945.

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

- **[V-JEPA 2](v-jepa-2.md)** ([paper](../sources/v-jepa-2-paper.md)) — V-JEPA 2-AC post-trained on **62 hr of unlabeled DROID robot videos** (a subset of the full 350 hr); zero-shot Franka manipulation in two new labs followed.
- **[JEPA-WMs](jepa-wms.md)** ([paper](../sources/jepa-wms-paper.md)) — uses the **raw DROID dataset in stereo HD (8.7 TB)** or **non-stereo HD-only video (5.6 TB)** as one of the training/eval data sources alongside RoboCasa, Metaworld, and a real Franka.

This makes DROID the single most reused real-robot dataset in the JEPA literature ingested here. It also features in the [sim-heavy vs real-data paths synthesis](../syntheses/simulators/sim-heavy-vs-real-data-paths.md) as the substrate for the "observation-pretraining + small real teleop" path to generalist policies — without DROID, V-JEPA 2's "62 hr → zero-shot Franka" existence proof would not exist.

## Distribution
- **TensorFlow Datasets**: `gs://gresearch/robotics`.
- **Hardware code (data-collection rig)**: https://github.com/droid-dataset/droid
- **Policy-learning baselines**: https://github.com/droid-dataset/droid_policy_learning
- **Updated annotations on HuggingFace**: https://huggingface.co/KarlP/droid

## Authors and institutions
13 institutions; lead authors **Alexander Khazatsky** and **Karl Pertsch**. Senior authors **Chelsea Finn** and **Sergey Levine**. Stanford and Berkeley lead, with collaborators across North America, Asia, and Europe.

## Open questions / TBD
- DROID **paper itself** ([DROID Paper](../sources/droid-paper.md), arxiv 2403.12945) now filed (2026-05-16). License confirmed **CC BY 4.0**.
- The Dec 2024 + Apr 2025 update deltas are not documented here; if the dataset has materially grown or changed task mix, this entity should reflect that.
- The "+22% / +17%" OXE-vs-DROID claim is from the project page; not yet cross-verified against the paper body's numerical tables.

## Derived / filtered subsets
- **MolmoAct2-DROID Dataset** ([MolmoAct2 paper](../sources/molmoact2-paper.md), §3.3) — [Ai2](ai2.md)'s **quality-filtered** subset for [MolmoAct2](molmoact2.md): **74,604 episodes, 17.76M frames**. Uses the HuggingFace supplementary annotations (`KarlP/droid`) — extended language instructions (3 per episode for 95% of the 75k successful episodes) + the idle-frame filter (keeps only ≥1s contiguous non-idle segments) — then **re-annotates language** with an open VLM. Motivation: raw DROID contains idle segments, failed attempts, and repetitive instructions. MolmoAct2-DROID is fine-tuned into a checkpoint that deploys **zero-shot on Franka**, beating π0.5-DROID (real-world 87.1% vs runner-up 48.4%).

## Related
- Franka Panda — single robot platform across the dataset.
- [MolmoAct2](molmoact2.md) — releases MolmoAct2-DROID, a quality-filtered Franka subset; SOTA zero-shot DROID deployment.
- [V-JEPA 2](v-jepa-2.md) — primary JEPA consumer.
- [JEPA-WMs](jepa-wms.md) — secondary JEPA consumer; uses the raw dataset.
- [Robot Utility Models](robot-utility-models.md) — alternative real-robot data philosophy (mobile-manipulation, single embodiment, Stretch).
- [Sim-heavy vs real-data paths synthesis](../syntheses/simulators/sim-heavy-vs-real-data-paths.md) — DROID is the empirical anchor of path C (observation pretraining + small real teleop).
- [Why JEPA research skips the simulator stack](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) — DROID's role in JEPA-for-robotics evaluations is part of why JEPA work has been able to skip / fragment sim use.

## Mentioned in
- [Cosmos 3 Edge (HF blog)](../sources/nvidia-cosmos3-edge-hf-blog.md) — **Cosmos3-Edge-Policy-DROID** (4B), a DROID-finetuned manipulation policy shipped for on-robot deployment.
- [FAST paper](../sources/fast-paper.md) — DROID's higher control frequency is what naïve action binning fails on; **FAST is what first makes efficient VLA training on DROID practical**, and enables the first **zero-shot DROID evaluation** in a completely unseen environment (language-prompted, no fine-tuning).
- [DROID Paper](../sources/droid-paper.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [MolmoAct2 paper (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — the quality-filtered MolmoAct2-DROID subset + zero-shot deployment.
