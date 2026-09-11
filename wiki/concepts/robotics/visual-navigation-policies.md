---
title: Visual navigation policies (GNM → ViNT → NoMaD → LogoNav)
type: concept
created: 2026-09-11
updated: 2026-09-11
sources: 2
tags: [navigation, visual-navigation, goal-conditioned, topological-memory, gnm, vint, nomad, logonav, omnivla, berkeley, rail, cross-embodiment, sidewalk-robot]
---

# Visual navigation policies

**Visual navigation policies** are end-to-end networks that map a monocular camera stream and a goal — a **goal image**, a **relative 2-D pose / GPS waypoint**, or (latest) language — to short-horizon velocity or pose commands, with no map, LiDAR, or explicit localization. The dominant open line is Berkeley RAIL's ([Shah](../../entities/dhruv-shah.md), [Hirose](../../entities/noriaki-hirose.md), [Levine](../../entities/sergey-levine.md)), which the wiki entered through [MBRA](../../sources/mbra-paper.md); this page records the lineage as that paper states it and should be treated as a scaffold until the earlier papers are ingested.

## The lineage (per MBRA's related work and references)

| Model | Year | Goal | Contribution |
|---|---|---|---|
| **GNM** — General Navigation Model (Shah, Sridhar, Bhorkar, Hirose, Levine; ICRA 2023) | 2023 | image | one policy across many robots by training on a mixture of ~60 h of curated datasets (RECON, GO Stanford, CoryHall, TartanDrive, HuRoN, Seattle, SCAND) — the **GNM mixture** every successor co-trains on |
| **ViNT** — Visual Navigation Transformer (Shah, Sridhar, Dashora, Stachowicz, Black, Hirose, Levine; CoRL 2023) | 2023 | image | Transformer "foundation model" for navigation; predicts pose chunks, uses a PD controller to velocities; the **goal-conditioned policy (GCP)** baseline MBRA compares against |
| **NoMaD** — goal-masked diffusion (Sridhar, Shah, Glossop, Levine; ICRA 2024) | 2024 | image or none | one diffusion policy for goal-reaching *and* exploration; sample many trajectories and pick |
| **MBRA / LogoNav** ([paper](../../sources/mbra-paper.md); RA-L 2025) | 2025 | **GPS waypoint** (~50 m) | relabel 700 h of noisy crowdsourced data with a model-based expert, then distill; 300+ m routes, six countries |
| **OmniVLA** (Hirose, Glossop, Shah, Levine; arXiv 2509.19480) | 2025 | image / pose / **language** | omni-modal VLA for navigation; not ingested |

Adjacent RAIL work the same papers cite: RECON (latent-goal exploration), ViKiNG (kilometer-scale with geographic hints), FastRLAP (RL for high-speed driving), SELFI and "lifelong improvement in the wild" (RL fine-tuning of navigation models), SACSoN (social navigation), ExAug (geometric augmentation — the model-based objective MBRA reuses), LeLaN (language-conditioned policy from in-the-wild video — the 100 h YouTube set MBRA relabels). CityWalker (Feng's group, CVPR 2025) is the parallel "learn urban navigation from web video" line.

## Structural facts that recur

- **Short horizon + topological memory.** Image-goal policies reach ~3 m; longer routes are a chain of subgoal images recorded at ~1 Hz during a teleoperated pass, with the policy localizing to the nearest node ([MBRA](../../sources/mbra-paper.md) §V-A). LogoNav's contribution is to replace this with GPS subgoals ~80 m apart.
- **3 Hz, 8-step chunks** is the shared discretization of the GNM lineage; MBRA keeps it for comparability.
- **The data ceiling was ~75 h per dataset and "dozens of hours" in total** until FrodoBots-2K (2,000 h) — which is why the noisy-label problem, not architecture, became the 2025 question.
- **Cross-embodiment is cheap here.** A 2-D velocity/pose action space transfers between wheeled rovers and a quadruped with a per-robot conversion layer; MBRA's Table III moves the same policy to a Go1 and a VizBot without adaptation. This is the navigation-side counterpart to the manipulation [cross-embodiment](../learning/soft-prompt-cross-embodiment.md) problem, and much easier.

## Where it meets the rest of the wiki

- **Evaluation.** The [Earth Rover Challenge](../../sources/earth-rover-challenge-frodobots-2k.md) is the standing multi-city benchmark for exactly this class, scoring AI as a fraction of the best human teleoperator; MBRA's six-country deployment is the research-side version. Both live on the [robot policy evaluation](robot-policy-evaluation.md) page.
- **Data.** The [crowdsourcing](../learning/crowdsourced-robot-training-data.md) page's newest lesson — crowdsourced *actions* may be worth nothing — comes from this line.
- **Learning from video.** MBRA's forward-model labeling is the model-based alternative to the inverse-dynamics labeling used across the wiki's video-to-action thread ([latent action tokens](../learning/latent-action-tokens.md), [DreamDojo](../../sources/dreamdojo-paper.md)); its ablation is the one place the two are compared under heavy noise.

## Key references

- [MBRA / LogoNav](../../sources/mbra-paper.md) — the ingested primary.
- [Earth Rover Challenge site + FrodoBots-2K card](../../sources/earth-rover-challenge-frodobots-2k.md) — data and benchmark.
- GNM, ViNT, NoMaD, OmniVLA — **not ingested**; cited above from MBRA's reference list.

## Related concepts

- [Robot policy evaluation](robot-policy-evaluation.md), [visual relocalization and mapping](visual-relocalization-and-mapping.md), [motion planning](motion-planning.md), [imitation learning](../learning/imitation-learning.md), [crowdsourced robot training data](../learning/crowdsourced-robot-training-data.md).

## Mentioned in

- [MBRA paper](../../sources/mbra-paper.md)
- [Earth Rover Challenge site + FrodoBots-2K card](../../sources/earth-rover-challenge-frodobots-2k.md)
