---
title: UnifoLM (Unitree foundation-model family)
type: entity
subtype: model
created: 2026-09-11
updated: 2026-09-28
sources: 3
tags: [unifolm, unitree, vla, world-action-model, embodied-reasoning, humanoid, unitree-g1, qwen3-vl, china, open-weights, apache-2.0]
---

# UnifoLM

**UnifoLM** is [Unitree](unitree.md)'s family of robot foundation models, published under the `unitreerobotics` Hugging Face org and the `UniGen-X` GitHub pages org. The current head is **UnifoLM-WLA-1.0** (announced 2026-09-11), a 6B humanoid policy built as a three-stage stack. On launch day only the two 4.4B **embodied-reasoning** backbones beneath it shipped. The policy followed on **2026-09-28** as `UnifoLM-WLA-1.0-Base`, with fine-tuning code, and everything is now **Apache-2.0** ([source page](../sources/unifolm-wla-1-project-page.md)).

## The three generations

| Generation | Date | Shape | Status |
|---|---|---|---|
| **WMA-0** (World-Model-Action) | 2025-09 | **DynamiCrafter** (2023 image-to-video latent diffusion) fine-tuned on Open-X then five Unitree Z1/G1 sets, with a Diffusion-Policy 1-D UNet action head; *decision-making* mode feeds predicted future interaction to the head, *simulation* mode renders outcomes of actions; 320×512, 16 frames = 16 actions, 15 Hz open-loop chunks ([page](../sources/unifolm-wma-0-project-page.md)) | code + weights (`-Base` gated, `-Dual` open); **no numbers** |
| **VLA-Base / VLM-Base / VLA-Libero** | 2026-01 | Conventional VLA checkpoints | weights on HF; undocumented on the current page |
| **WLA-1.0** | 2026-09 | ER-1 (Qwen3-VL-4B + 5M embodied samples) → ER-Flow (+ optical-flow mask tokens, + RVQ action tokens) → 6B policy with MMDiT flow-matching expert behind a stop-gradient | ER-1 + ER-Flow (09-11); **policy `WLA-1.0-Base` + fine-tune code (09-28)**; LoRA code pending; **no numbers for the policy** |

All from the [project page](../sources/unifolm-wla-1-project-page.md) and the HF org listing.

## What is distinctive

- **The "world" target got sparser each generation.** WMA-0 generated future *video*; WLA-1.0's world component predicts a **VQ-tokenized optical-flow mask** — *where* the scene will change, not what it will look like — as ordinary tokens inside the VLM. This is Unitree's implicit answer to what a policy-side world model needs to preserve: the moving region. See [world-action model](../concepts/world-models/world-action-model.md).
- **Actions tokenized per body-part group.** Three residual-VQ codebooks — end-effector pose, end-effector joints (gripper or five-finger hand), lower body — with shared timesteps. The lower-body stream is what makes the same weights drive "whole-body manipulation" on the [G1](unitree-g1.md); the released server shows how it meets the G1's balance controller: it sends base vx/vy/ω/height commands plus leg and waist joint targets to a `unitree_rl_wbc` RL whole-body-controller client ([whole-body control](../concepts/robotics/whole-body-control.md)). The shipped checkpoint flattens all of this into one masked **54-D action vector with 30-step chunks and 4 denoising steps** ([release details](../sources/unifolm-wla-1-project-page.md#stage-3-as-released--unifolm-wla-10-base-2026-09-28)).
- **Otherwise the π0.5 recipe.** Discrete tokens to train the backbone, continuous flow-matching expert to act, stop-gradient between them, general-VLM co-training — the [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) pattern, uncredited.
- **An ER backbone that leads open models on 7 of 16 benchmarks** (Where2Place 82.0 and EmbSpatial 88.9 best overall) while **regressing below its own Qwen3-VL-4B base on MME, MMMU, RealWorldQA and VSI-Bench** — see the [source page](../sources/unifolm-wla-1-project-page.md) and [embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md).

## Data

≈2,500 h of real-robot data, including the Unitree open datasets and **[HIW-500](hiw-500.md)** ([BitRobot](bitrobot.md); 500+ h of G1 whole-body teleop in 12 real homes, CC BY 4.0 — the one permissively licensed ingredient). Released with WLA-1.0: the **UniBot-V1 Challenge Dataset**, 32 `G1_Dex1_*` tabletop tasks. The `UnifoLM_WBT_Dataset` whole-body-teleop collection has been on HF since May 2026 and had grown to **58** datasets by 2026-09-28. It was joined by a **72**-dataset `UnifoLM_G1_Dex1_Dataset` collection. The released `Base` checkpoint carries normalization stats for exactly these two corpora (G1-Dex1 and WBT), not for HIW-500 or other embodiments.

## License

**Apache-2.0**, as of 2026-09-28, on the `unifolm-wla` repo and every UnifoLM checkpoint on HF (ER-1, ER-Flow, WLA-1.0-Base, WMA-0).

> [!warning] Relicensed after launch. Older wiki text said CC BY-NC-SA
> At launch (2026-09-11) the repo and HF LICENSE files were **CC BY-NC-SA 4.0**. The HF LICENSE files were deleted and the cards set to `apache-2.0` later that day (WMA-0 on 09-13), and the GitHub LICENSE was swapped on 09-20. One inconsistency remains: the WMA-0 GitHub repo (`unifolm-world-model-action`) still carries CC BY-NC-SA text while its HF weights say Apache-2.0. Details in the source page's [Edition history](../sources/unifolm-wla-1-project-page.md#edition-history).

This moves UnifoLM into the permissive column with [MolmoAct2](molmoact2.md) on the [deployability landscape](../syntheses/platforms/vla-deployability-landscape.md). It is also one of the few permissively licensed open policies with a humanoid whole-body action space.

## Open questions

- The policy is now downloadable, but still nothing is measured: no success rates, baselines, ablation of ER-Flow vs ER-1, inference rate, or hardware.
- Whether the prior VLA-Base generation and WLA-1.0 share data or code is undocumented.

## Mentioned in

- [UnifoLM-WLA-1.0 project page](../sources/unifolm-wla-1-project-page.md)
- [UnifoLM-WMA-0 project page](../sources/unifolm-wma-0-project-page.md) — the first generation; architecture from its training config.
- [HIW-500 dataset page](../sources/bitrobot-hiw-500-dataset-page.md) — the in-the-wild ingredient of WLA-1.0's data mix.
