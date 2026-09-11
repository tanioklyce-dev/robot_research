---
title: Visual navigation policies (GNM → ViNT → NoMaD → LogoNav → OmniVLA)
type: concept
created: 2026-09-11
updated: 2026-09-11
sources: 6
tags: [navigation, visual-navigation, goal-conditioned, topological-memory, gnm, vint, nomad, logonav, omnivla, berkeley, rail, cross-embodiment, sidewalk-robot, normalized-actions, modality-dropout]
---

# Visual navigation policies

**Visual navigation policies** are end-to-end networks that map a monocular camera stream and a goal — a **goal image**, a **relative 2-D pose / GPS waypoint**, or **language** — to short-horizon waypoint or velocity commands, with no map, LiDAR, or explicit localization. The dominant open line is Berkeley RAIL's ([Shah](../../entities/dhruv-shah.md), [Hirose](../../entities/noriaki-hirose.md), [Levine](../../entities/sergey-levine.md)), 2022–2025, now fully ingested.

## The lineage

| Model | Venue | Params / data | Goal | What it added | Headline number |
|---|---|---|---|---|---|
| **[GNM](../../sources/gnm-paper.md)** | ICRA 2023 | MobileNetv2 / 60–70 h, 6 robots | image | **normalized waypoint action space** + **embodiment context** (k = 5 past frames) → one policy drives any ground robot | LoCoBot 0.96 vs 0.62 single-robot; drives a Tello quadrotor with no aerial data |
| **[ViNT](../../sources/vint-paper.md)** | CoRL 2023 oral | 31M Transformer / >100 h, 8 robots | image (+ soft-prompt adaptation to GPS, routing) | goal-fusion token; **318M subgoal-image diffusion** + physical search for exploration; fine-tune in <1 h; emergent road/hallway preference | 1.27 km GPS-guided, 0.95 success; Go1 zero-shot 45 m |
| **[NoMaD](../../sources/nomad-paper.md)** | ICRA 2024 | 19M / GNM + SACSoN >100 h | image or **none** | **goal masking** + **action diffusion** — one policy explores and goal-reaches; deletes the image-diffusion subgoal model | exploration 98% / 0.2 collisions vs 77% / 1.7 at 335M |
| **[MBRA / LogoNav](../../sources/mbra-paper.md)** | RA-L 2025 | EfficientNet+Transformer / +700 h FrodoBots | **GPS pose (~50 m)** | **model-based relabeling** of noisy crowdsourced actions; 300+ m routes | 0.857 vs 0.619 GS; raw-action imitation 0.000 |
| **[OmniVLA](../../sources/omnivla-paper.md)** | arXiv 2025-09 | OpenVLA 7B (LoRA) / 9,500 h, 10 platforms (91% BDD-V dashcam) | image, pose, **language**, any combination | **modality dropout**; composed "where + how" goals; satellite adaptation by swapping one encoder | language 0.73 vs 0.43; composed task 0.80; 50M edge model ties on pose/image |

Adjacent RAIL work the papers cite: RECON and ViKiNG (latent-goal exploration; kilometer-scale with geographic hints), FastRLAP / SELFI / lifelong-improvement (RL on navigation models), SACSoN (social navigation data), ExAug (the forward-model objective MBRA reuses), LeLaN (language policy from in-the-wild video, NoMaD-labeled), CAST / CounterfactualVLA (counterfactual language labels). CityWalker (Feng, CVPR 2025) is the parallel web-video line; NaVILA the legged-robot VLA that OmniVLA found prompt-incompatible.

## Structural facts that recur

- **Normalized waypoints are the whole cross-embodiment trick.** GNM's ablation: normalized waypoints 1.0 / 0.95 vs raw velocities 0.73 / 0.54 vs unnormalized waypoints 0.42 / 0.26. Every successor keeps it, which is why a wheeled-trained policy drives a [Go1](../../entities/unitree-go1.md) with no adaptation — the legs are the robot's own controller's problem. This is the property manipulation lacks, and why it needs [latent action tokens](../learning/latent-action-tokens.md) instead.
- **Short horizon + topological memory.** Image-goal policies reach ~3 m; longer routes chain subgoal images recorded at ~1 Hz, with the policy's predicted temporal distance as the graph edge weight (ViNG → GNM → ViNT → NoMaD → MBRA all use it). LogoNav's contribution is GPS subgoals ~80 m apart instead.
- **3–4 Hz, 5–8 step chunks, 85×64 to 96×96 images, EfficientNet-B0 tokens** — the shared discretization from GNM through OmniVLA-edge. OmniVLA keeps 8 steps at 3 Hz even on a 7B backbone.
- **Data grew 60 h → 100 h → 800 h → 9,500 h**, and almost all of the growth is **relabeled or synthesized actions** (FrodoBots via MBRA, LeLaN via NoMaD, BDD-V via a custom relabeler). The human-labeled core never exceeded ~100 h. The wiki's [crowdsourcing](../learning/crowdsourced-robot-training-data.md) page records the consequence: crowdsourced *actions* were worth zero.
- **Generic visual pretraining keeps losing.** GNM: ImageNet init "improves a bit"; ViNT: ImageNet / SimCLR / VC-1 backbones 0.19–0.22 vs ViNT 0.82 on CARLA; OmniVLA: manipulation-pretrained MiniVLA / SmolVLA far below a 50M navigation model. What transfers is *navigation* data, and, for language only, an LLM.
- **Generation targets, in order of abandonment:** ViNT generated subgoal *images* (318M, often invalid) → NoMaD generated *actions* (19M, 98%) → MBRA relabels actions with a *forward model* → OmniVLA drops any generation. Same direction as the [world-action model](../world-models/world-action-model.md) page's pixels-are-the-wrong-target thread.
- **Dropout as the unification device.** NoMaD's goal mask (p = 0.5) → OmniVLA's modality mask; one model for with-goal and without-goal, then for every goal type.

## Where it meets the rest of the wiki

- **Evaluation.** The [Earth Rover Challenge](../../sources/earth-rover-challenge-frodobots-2k.md) is the standing multi-city benchmark for this class; MBRA's six-country deployment and ViNT's kilometer runs are the research-side versions. Metrics worth keeping: mean progress (GNM), max displacement without intervention (ViNT), SPL (ViNT), coverage rate (MBRA) — all partial-credit, all on the [robot policy evaluation](robot-policy-evaluation.md) page.
- **Soft prompts.** ViNT's swap-the-goal-encoder adaptation (2023) is the task-modality twin of [X-VLA's](../learning/soft-prompt-cross-embodiment.md) per-embodiment soft prompts (2025).
- **Diffusion policies.** NoMaD is the first goal-conditioned [Diffusion Policy](../../entities/diffusion-policy.md) on a real robot, with the autoregressive-collapses-to-the-mean comparison in the same table.
- **VLA backbones.** OmniVLA's edge-vs-7B split is the cleanest evidence for *where* a VLM earns its cost in a policy: out-of-distribution language, not control ([VLA models](../learning/vla-models.md)).

## Key references

- [GNM](../../sources/gnm-paper.md), [ViNT](../../sources/vint-paper.md), [NoMaD](../../sources/nomad-paper.md), [MBRA / LogoNav](../../sources/mbra-paper.md), [OmniVLA](../../sources/omnivla-paper.md) — all ingested.
- [Earth Rover Challenge site + FrodoBots-2K card](../../sources/earth-rover-challenge-frodobots-2k.md) — data and benchmark.

## Related concepts

- [Robot policy evaluation](robot-policy-evaluation.md), [visual relocalization and mapping](visual-relocalization-and-mapping.md), [motion planning](motion-planning.md), [control abstraction levels](control-abstraction-levels.md), [imitation learning](../learning/imitation-learning.md), [crowdsourced robot training data](../learning/crowdsourced-robot-training-data.md), [soft prompts](../learning/soft-prompt-cross-embodiment.md), [latent action tokens](../learning/latent-action-tokens.md).

## Mentioned in

- [GNM paper](../../sources/gnm-paper.md)
- [ViNT paper](../../sources/vint-paper.md)
- [NoMaD paper](../../sources/nomad-paper.md)
- [MBRA paper](../../sources/mbra-paper.md)
- [OmniVLA paper](../../sources/omnivla-paper.md)
- [Earth Rover Challenge site + FrodoBots-2K card](../../sources/earth-rover-challenge-frodobots-2k.md)
