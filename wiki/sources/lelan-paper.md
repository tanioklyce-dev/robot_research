---
title: LeLaN — Learning a Language-Conditioned Navigation Policy from In-the-Wild Videos (Hirose, Glossop, Sridhar, Shah, Mees, Levine; CoRL 2024)
type: source
url: https://arxiv.org/abs/2410.03603
fetch_url: https://arxiv.org/pdf/2410.03603v1
author: Noriaki Hirose, Catherine Glossop, Ajay Sridhar, Dhruv Shah, Oier Mees, Sergey Levine
published: 2024-10-04
ingested: 2026-09-11
venue: CoRL 2024 (arXiv v1; 23 pp.)
local_path: raw/2410.03603v1.pdf
sha256: 8e9886d57bfe2c484fc70686c759941c600f314f088c8771d4e11a85718c9f6f
format: pdf
tags: [lelan, navigation, language-conditioned, object-navigation, in-the-wild-video, youtube, synthetic-labels, vlm-labeling, nomad, action-free, jetson-orin, berkeley, rail, unitree-go1, last-mile]
---

## Summary

The paper that produced the **LeLaN mixture** every later RAIL navigation model trains on, and the first in the line to make **both the language labels and the actions synthetic**. Object navigation needs data of robots driving *toward things*, which teleoperated corpora almost never contain ("traveling only down the center corridors and rarely heading toward objects"). LeLaN manufactures it from **action-free egocentric video**: Segment Anything crops candidate objects, CogVLM describes each crop, GPT-3.5-turbo turns descriptions into "Go to X" prompts, a monocular depth model (Metric3D or Depth360) gives each object a 3-D pose, and a fine-tuned [NoMaD](nomad-paper.md) supplies a collision-avoiding trajectory toward the crop. Applied to **~130 h** — 31 h of indoor robot data, **82.5 h of YouTube tours from 32 countries**, and 15.7 h of hand-held fisheye walking in 11 cities — it yields **20M+ prompts**. A small policy (frozen CLIP text encoder, ResNet-FiLM, EfficientNet-B0 history, Transformer; **54 ms on a Jetson Orin**) trained on it reaches **89%** over 1,050 real trials against 67% for the best baseline, is far more robust to noisy prompts and moving targets, and drives a [Unitree Go1](../entities/unitree-go1.md) and three camera rigs unchanged.

## Key claims

### The labeling pipeline (§3.1)

- **Language:** SAM → crops → open-source VLM (CogVLM) description → GPT-3.5-turbo confidence filter and prompt generation. Closed VLMs were too slow and costly at submission time; open ones gave poor prompts directly, hence the two-stage split.
- **Pose:** depth estimate → point cloud → SAM mask → median point = object pose.
- **Actions:** NoMaD, fine-tuned to accept an *image crop* as its goal (50% of batches), generates the trajectory toward the object. This becomes a distillation target J_col; the base objective is J_pose (reach the projected object pose through a **differentiable kinematic model**) + J_smooth, with J_col masked within 1 m of the target because NoMaD's avoidance otherwise prevents arrival.
- **Data (Table 1):** Indoor (GS2, GS4, SACSoN) 31.0 h / 111K images / 594K objects / 3.4M prompts; YouTube 82.5 h / 594K images / 3.3M objects / **14.6M prompts**; human walking 15.7 h / 113K images / 535K objects / 2.3M prompts. Video sampled at 2 fps.

### Results (Table 2; 150 trials per method, 28 objects, 5 environments)

| Method | Total | Simple | Noisy prompts | Multi-object | Dynamic target | Inference (Orin) |
|---|---:|---:|---:|---:|---:|---:|
| OpenFMNav (+planner) | 0.43 | 0.38 | 0.46 | 0.31 | 0.00 | 22.0 s (initial only) |
| OWL-ViT + ViNT | 0.47 | 0.48 | 0.47 | 0.22 | 0.33 | 0.33 s |
| CoW (+planner) | 0.58 | 0.73 | 0.51 | 0.43 | 0.17 | 0.22 s |
| OWL-v2 + ZoeDepth (+planner) | 0.67 | 0.73 | 0.63 | 0.62 | 0.00 | 2.82 s |
| LeLaN, indoor data only | 0.65 | 0.63 | 0.66 | 0.64 | 0.67 | 0.054 s |
| LeLaN, +20% YT, +43.5% HW | 0.85 | 0.91 | 0.82 | 0.70 | 0.83 | 0.054 s |
| **LeLaN, full** | **0.89** | **0.91** | **0.88** | **0.81** | **0.83** | **0.054 s** |

- **Collision (Table 3, 15 trials):** with obstacles, LeLaN without J_col **0.13**, with J_col **0.60**, best baseline 0.40; *without* obstacles, J_col costs accuracy (0.77 vs 0.89) — the distilled avoidance and the reaching objective compete.
- **Data ablation (Fig. 5):** indoor and human-walking data saturate around **100K frames**; the YouTube set keeps improving past **500K frames** — "the broad distribution of environments and objects… is the key reason."
- **Cross-embodiment (§4.3):** Go1 with a fisheye camera; the wheeled robot with fisheye, narrow-FOV, and elevated spherical cameras — all navigate to targets; qualitative only.
- **Architecture (Appendix C):** CLIP visual encoders (ViT-B/32, RN50) are *worse* than a from-scratch ResNet-FiLM (MSE 1.69 / 1.67 vs 1.29 / 1.20) — "visual features from the CLIP visual encoder are insufficient to derive time-series velocity commands because they do not include geometric information."

### Limitations (§5)

Cannot resolve duplicates by spatial language ("go to the leftmost door"); collision avoidance "remains a challenging task." Scope is **last-mile** navigation with the target in view, paired with topological memory and an OWL-v2 node scorer for longer routes (Appendix J).

## Reading it against the wiki

- **The actions are synthetic here too.** [MBRA](mbra-paper.md) relabels bad human actions; LeLaN goes further and never has human actions at all — NoMaD plus a depth model generates them. The [OmniVLA](omnivla-paper.md) data table now reads correctly: the LeLaN mixture's 128.7 h carries NoMaD-generated actions and LLM-generated language. The [navigation-lineage](../concepts/robotics/visual-navigation-policies.md) observation that growth past ~100 h is entirely model-labeled data starts here, a year before MBRA.
- **YouTube is the only source that did not saturate.** The ablation is the cleanest datapoint in the wiki for *why* the line later took on 8,680 h of dashcam video: diversity, not hours.
- **Generic visual pretraining loses again**, now with a stated mechanism — CLIP features lack the geometry a velocity policy needs. Same finding as GNM, ViNT and OmniVLA, from the encoder side.
- **Label quality was never measured.** No human audit of the VLM prompts; [CAST](cast-paper.md) later measures its own hindsight labels at ~60% correct, which is the number to assume here too.

## Entities mentioned

- [Noriaki Hirose](../entities/noriaki-hirose.md), [Dhruv Shah](../entities/dhruv-shah.md), [Sergey Levine](../entities/sergey-levine.md); Catherine Glossop, Ajay Sridhar, Oier Mees.
- [Unitree Go1](../entities/unitree-go1.md) — cross-embodiment test; NoMaD — the action generator; CoW, OWL-ViT/OWL-v2 — baselines.

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md), [crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) (action-free video made usable), [cross-embodiment](../concepts/learning/cross-embodiment.md), [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md).

## Open questions

- What fraction of the 20M prompts are correct; no audit.
- Whether the YouTube gain is diversity of *scenes* or of *objects* — the ablation cannot separate them.
