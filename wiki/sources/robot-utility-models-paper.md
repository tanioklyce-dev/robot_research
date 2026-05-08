---
title: Robot Utility Models Paper
type: source
url: https://arxiv.org/abs/2409.05865
local_path: raw/robot_utility_models_2409.05865v1.pdf
author: Haritheja Etukuru, Norihito Naka, Zijin Hu, Seungjae Lee, Julian Mehu, Aaron Edsinger, Chris Paxton, Soumith Chintala, Lerrel Pinto, Nur Muhammad "Mahi" Shafiullah
affiliations: NYU, Hello Robot Inc., Meta Inc.
published: 2024-09-09
ingested: 2026-05-08
tags: [rum, robot-utility-models, behavior-cloning, vq-bet, diffusion-policy, stretch, stick-v2, mllm, real-robot]
---

## Summary
Full-paper companion to the [[robot-utility-models-website|RUM project page]]. Introduces **Robot Utility Models (RUMs)** — five task-specific zero-shot manipulation policies (door opening, drawer opening, reorientation, tissue pickup, bag pickup) deployable with **no fine-tuning** across novel environments. **2,950 real-world rollouts** across homes in NYC, Jersey City, and Pittsburgh produce a **90% average success rate**: 74.4% from the raw policy + 15.6% from an mLLM-driven retry mechanism. Headline lessons emphasize **training data over training algorithm** and **diversity over quantity**.

## Key claims (paper-body details beyond what the project page summarizes)

### Model architecture
- Best policy classes: **VQ-BeT** (Lee et al. 2024) and **Diffusion Policy** (Chi et al. 2023). VQ-BeT narrowly outperforms DP at full data scale; DP wins at smaller scale.
- Baselines tested on 2 tasks: **ACT** (Zhao et al. 2023b) and **MLP-BC** — close behind, not far off, supporting the "data > algorithm" headline.
- All policies share a **ResNet34 vision encoder initialized from the HPR encoder** of [[robot-utility-models|Dobb·E]] (Shafiullah et al. 2023) + a transformer-based policy trunk.
- VQ-BeT specifics: data subsampled to **3.75 Hz**, **6 most recent frames** of history, predicts **relative 6D end-effector pose** + absolute gripper opening in `[0,1]`.
- 500 epochs of training on **2× Nvidia A100 GPUs**; 24–48 hr per model.

### Data collection — Stick-v2
- iPhone Pro + a **$25 bill of materials**. 3D-printed chassis with cable-driven trigger, flexible fingers, wrist-mounted iPhone.
- **60 Hz RGB+depth** video; **100 Hz 6D pose** via ARKit.
- **Gripper aperture** estimated by an **RGB-based predictor model** trained from images.
- **No SLAM, no calibration.** Works in textureless scenes (flat walls, ceilings, corners) where SLAM-based tools fail.

### Datasets per task
- ~1,000 demonstrations per task on ~40 environments (~25 demos per env on average).
- Door opening: 1,200 demos; drawer opening: 525 demos.
- Door-opening dataset seeded with the Homes of New York dataset from prior Dobb·E work.

### Real-world experimental scale
- **2,950 robot rollouts** total.
- 25 novel evaluation environments (5 per task) — never seen during training.
- 10 trials per environment; retrying timeout at 10 tries (avg 1.31 tries to success).

### Headline numbers
- **90% average success** on 25 novel environments overall.
- Per-task base success (no retrying): Reorientation 68%, Drawer opening 76%, Door opening 76%, Tissue pickup 80%, Bag pickup 84% (VQ-BeT). Average **74.4%**.
- Retrying with gpt-4o-2024-05-13 adds **+15.6%** average → 90%.
- mLLM critique uses every-other-frame summaries from head or wrist camera; per-task verification prompt.

### Cross-embodiment transfer (Stretch → UFactory xArm 7)
- Tissue pickup: **80% → 70%** (-10pt).
- Bag pickup: **84% → 76%** (-8pt).
- Custom 3D-printed end-effector designed to mount on standard robot arms (xArm, [[franka-panda|Franka Panda]]).
- Wrist-camera-agnostic: tested on iPhone Pro and Intel RealSense D405 (Stretch Edition 3 default).

### Data ablations (the recipe insights)
1. **Data > algorithm.** VQ-BeT and Diffusion Policy land within ~5pt; ACT and MLP-BC ~10–15pt below. The paper's framing: training data is significantly more important than training algorithm.
2. **Diversity > quantity.** Diverse-data setting (25 demos × many envs) beats concentrated-data setting (200 demos × few envs). Strongest effect on reorientation (68% vs 18%).
3. **Expert > non-expert.** Expert data outperforms non-expert in all tasks. **Co-training expert + non-expert sometimes *reduces* performance** — counter to common practice (Zhao et al. 2023b; Khazatsky et al. 2024).

## Entities mentioned
- [[robot-utility-models|Robot Utility Models]]
- [[stretch|Stretch]] / [[hello-robot|Hello Robot]] — primary deployment platform.
- [[franka-panda|Franka Panda]] — referenced as alternative deployment target (custom end-effector mountable).
- [[lerrel-pinto|Lerrel Pinto]] — co-senior author (NYU).
- [[meta-fair|Meta]] — Soumith Chintala affiliation; Meta Inc.
- xArm 7 (UFactory) — cross-embodiment transfer target (no entity page yet).
- gpt-4o (OpenAI) — mLLM critic (no entity page yet).

## Concepts touched
- [[imitation-learning|Imitation learning]] — multi-modal BC framework.
- Cross-embodiment transfer.
- Mobile manipulation.
- [[vla-models|VLA-adjacent generalist policies]] — RUMs deliberately are *not* language-conditioned.
- Self-critique / introspection — mLLM-as-verifier loop.

## Open questions
- The paper claims data > algorithm but the experimental scope is 5 tasks × 1k demos. Does the conclusion hold at larger task counts or larger per-task scale?
- mLLM-critique false-positive rate is ~5% across tasks. What happens to error compounding when tasks chain?
- xArm 7 cross-embodiment is tested on 2 of 5 tasks (tissue + bag). Door / drawer opening transfer not measured.
- The "co-training expert + non-expert hurts" finding contradicts mainstream practice — would benefit from independent reproduction.

## Why this matters in this wiki
This paper is the **most rigorous example in the wiki of "low-cost robot + learned-from-data zero-shot policy"** as a deployment shape. It's the closest architectural precedent for the [[lewm-on-rosorin-pro-feasibility|LeWM-on-ROSOrin-Pro feasibility analysis]] — different paradigm (BC, not JEPA), but the same engineering shape: collect ~1,000 demos per task on a commodity-priced robot, train, deploy zero-shot. The paper's "diversity > quantity" lesson is also a useful guidepost for any data-collection effort on educational hardware.

## Code & artifacts
- Project page: https://robotutilitymodels.com/
- Code: github.com/haritheja-e/robot-utility-models
- Dataset (~473 MB): hosted on Cloudflare R2 (link on project page)
- Data diversity visualizer: https://robotutilitymodels.com/data_diversity/
- DOI: https://doi.org/10.48550/arXiv.2409.05865
