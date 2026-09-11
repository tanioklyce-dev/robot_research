---
title: UnifoLM (Unitree foundation-model family)
type: entity
subtype: model
created: 2026-09-11
updated: 2026-09-11
sources: 3
tags: [unifolm, unitree, vla, world-action-model, embodied-reasoning, humanoid, unitree-g1, qwen3-vl, china, open-weights, non-commercial]
---

# UnifoLM

**UnifoLM** is [Unitree](unitree.md)'s family of robot foundation models, published under the `unitreerobotics` Hugging Face org and the `UniGen-X` GitHub pages org. The current head is **UnifoLM-WLA-1.0** (announced 2026-09-11), a 6B humanoid policy built as a three-stage stack; the shipped artifacts on launch day are the two 4.4B **embodied-reasoning** backbones beneath it, not the policy ([project page](../sources/unifolm-wla-1-project-page.md)).

## The three generations

| Generation | Date | Shape | Status |
|---|---|---|---|
| **WMA-0** (World-Model-Action) | 2025-09 | **DynamiCrafter** (2023 image-to-video latent diffusion) fine-tuned on Open-X then five Unitree Z1/G1 sets, with a Diffusion-Policy 1-D UNet action head; *decision-making* mode feeds predicted future interaction to the head, *simulation* mode renders outcomes of actions; 320×512, 16 frames = 16 actions, 15 Hz open-loop chunks ([page](../sources/unifolm-wma-0-project-page.md)) | code + weights (`-Base` gated, `-Dual` open); **no numbers** |
| **VLA-Base / VLM-Base / VLA-Libero** | 2026-01 | Conventional VLA checkpoints | weights on HF; undocumented on the current page |
| **WLA-1.0** | 2026-09 | ER-1 (Qwen3-VL-4B + 5M embodied samples) → ER-Flow (+ optical-flow mask tokens, + RVQ action tokens) → 6B policy with MMDiT flow-matching expert behind a stop-gradient | **ER-1 and ER-Flow released; policy, post-train code and two datasets pending** |

All from the [project page](../sources/unifolm-wla-1-project-page.md) and the HF org listing.

## What is distinctive

- **The "world" target got sparser each generation.** WMA-0 generated future *video*; WLA-1.0's world component predicts a **VQ-tokenized optical-flow mask** — *where* the scene will change, not what it will look like — as ordinary tokens inside the VLM. This is Unitree's implicit answer to what a policy-side world model needs to preserve: the moving region. See [world-action model](../concepts/world-models/world-action-model.md).
- **Actions tokenized per body-part group.** Three residual-VQ codebooks — end-effector pose, end-effector joints (gripper or five-finger hand), lower body — with shared timesteps. The lower-body stream is what makes the same weights drive "whole-body manipulation" on the [G1](unitree-g1.md); how it meets the G1's balance controller is not stated ([whole-body control](../concepts/robotics/whole-body-control.md)).
- **Otherwise the π0.5 recipe.** Discrete tokens to train the backbone, continuous flow-matching expert to act, stop-gradient between them, general-VLM co-training — the [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) pattern, uncredited.
- **An ER backbone that leads open models on 7 of 16 benchmarks** (Where2Place 82.0 and EmbSpatial 88.9 best overall) while **regressing below its own Qwen3-VL-4B base on MME, MMMU, RealWorldQA and VSI-Bench** — see the [source page](../sources/unifolm-wla-1-project-page.md) and [embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md).

## Data

≈2,500 h of real-robot data, including the Unitree open datasets and **[HIW-500](hiw-500.md)** ([BitRobot](bitrobot.md); 500+ h of G1 whole-body teleop in 12 real homes, CC BY 4.0 — the one permissively licensed ingredient). Released with WLA-1.0: the **UniBot-V1 Challenge Dataset**, 32 `G1_Dex1_*` tabletop tasks. The 14-item `UnifoLM_WBT_Dataset` (whole-body teleop) collection has been on HF since May 2026.

## License

**CC BY-NC-SA 4.0** on the repo and both released checkpoints — research use only. This puts UnifoLM in a different column from [MolmoAct2](molmoact2.md) (fully open) and [GR00T](nvidia-groot.md) on the [deployability landscape](../syntheses/platforms/vla-deployability-landscape.md).

## Open questions

- Nothing on the policy is measurable yet: no success rates, baselines, ablation of ER-Flow vs ER-1, inference rate, or hardware.
- Whether the prior VLA-Base generation and WLA-1.0 share data or code is undocumented.

## Mentioned in

- [UnifoLM-WLA-1.0 project page](../sources/unifolm-wla-1-project-page.md)
- [UnifoLM-WMA-0 project page](../sources/unifolm-wma-0-project-page.md) — the first generation; architecture from its training config.
- [HIW-500 dataset page](../sources/bitrobot-hiw-500-dataset-page.md) — the in-the-wild ingredient of WLA-1.0's data mix.
