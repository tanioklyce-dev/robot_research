---
source_url: https://github.com/unitreerobotics/unifolm-wla
collected: 2026-09-28
published: 2026-09-28
author: Unitree Robotics
companion_urls:
  - https://huggingface.co/unitreerobotics/UnifoLM-WLA-1.0-Base (config.yaml, dataset_statistics.json, file listing via HF API)
  - https://github.com/unitreerobotics/unifolm-wla/blob/main/docs/robot_action_state_processing_en.md
  - https://github.com/unitreerobotics/unifolm-wla/blob/main/model_server/action_server_wbc_msgpack_unitree.py
  - GitHub commits API (LICENSE history), Hugging Face commits API (ER-1, WMA-0-Dual, WLA-1.0-Base)
license: Apache-2.0 (repo LICENSE since 2026-09-20; HF cards apache-2.0)
note: Follow-up capture 17 days after the 2026-09-11 launch capture (raw/2026-09-11-unifolm-wla-1-project-page.md), recording the policy-weight release and the relicensing. Sections 1–3 are verbatim; sections 4–7 are excerpts and API listings as retrieved on 2026-09-28.
---

# UnifoLM-WLA-1.0-Base release — capture 2026-09-28

## 1. GitHub README (main @ 2026-09-28, after merge of PR #11 "init_wla_1_0")

# UnifoLM-WLA-1.0
<div align="right"><a href="README.md"><kbd>English</kbd></a> | <a href="README_zh.md"><kbd>简体中文</kbd></a></div>
<div align="center">

[Project Page](https://unigen-x.github.io/unifolm-wla.github.io/) | [Models](https://huggingface.co/collections/unitreerobotics/unifolm-wla-10) | [Datasets](https://huggingface.co/collections/unitreerobotics/unifolm-wla-10)

<p align="center">
  <a href="https://www.youtube.com/watch?v=GHySQMMrIa4">
    <img src="assets/unifolm-wla-en-cover.png" alt="UnifoLM-WLA-1.0 video" width="800">
  </a>
</p>

</div>

UnifoLM-WLA-1.0 is Unitree Robotics' comprehensively upgraded, next-generation general-purpose humanoid robot foundation model with 6B parameters. Built on large-scale general multimodal perception and understanding data and interaction-centric world modeling, it substantially advances spatial perception and understanding, achieving leading results across multiple embodied reasoning benchmarks. Trained on approximately 2,500 hours of high-quality real-robot data, a single model coordinates 64 tasks spanning desktop manipulation and whole-body manipulation. It supports two-finger grippers and multiple five-finger dexterous hands, with strong generalization across tasks and end effectors.

## 📋 Table of Contents

- [News](#-news)
- [Open-Source Plan](#-open-source-plan)
- [Robot Action, State, and Statistics Processing Specification](docs/robot_action_state_processing_en.md)
- [Train and Evaluate an Action Expert](docs/train_action_expert_en.md)
  - [Installation](docs/train_action_expert_en.md#installation)
  - [Evaluating a Checkpoint](docs/train_action_expert_en.md#evaluating-a-checkpoint)
  - [Model Server](docs/train_action_expert_en.md#model-server)
  - [Fine-tuning the UnifoLM-WLA-1.0-Base Action Expert](docs/train_action_expert_en.md#fine-tuning-the-unifolm-wla-10-base-action-expert)
  - [Training from Scratch](docs/train_action_expert_en.md#training-from-scratch)
- [Citation](#citation)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## 🔥 News
- Sep 28, 2026: 🚀 we released the [UnifoLM-WLA-1.0-Base](https://huggingface.co/unitreerobotics/UnifoLM-WLA-1.0-Base) and fine-tuning code.
- Sep 20, 2026: 🚀 we released the model modules and training action expert code
- Sep 11, 2026: 🚀 we released the model weights of [UnifoLM-ER-1](https://huggingface.co/unitreerobotics/UnifoLM-ER-1)
- Sep 11, 2026: 🚀 we released the model weights of [UnifoLM-ER-Flow](https://huggingface.co/unitreerobotics/UnifoLM-ER-Flow)

## 📑 Open-Source Plan

- **Code**
  - [x] [Code for training action experts based on UnifoLM-ER models](docs/train_action_expert_en.md#training-from-scratch)
  - [x] [Code for fine-tuning based on UnifoLM-WLA-1.0-Base](docs/train_action_expert_en.md#fine-tuning-the-unifolm-wla-10-base-action-expert)
  - [ ] Code for LoRA fine-tuning
- **Models**
  - [x] [**UnifoLM-ER-1**](https://huggingface.co/unitreerobotics/UnifoLM-ER-1)
  - [x] [**UnifoLM-ER-Flow**](https://huggingface.co/unitreerobotics/UnifoLM-ER-Flow)
  - [x] [**UnifoLM-WLA-1.0-Base**](https://huggingface.co/unitreerobotics/UnifoLM-WLA-1.0-Base)
- **Datasets**
  - [x] [**UniBot-V1 Challenge Dataset**](https://huggingface.co/collections/unitreerobotics/unibot-v1-challenge-dataset)
  - [x] [**UnifoLM-WBT-Dataset**](https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset)
  - [x] [**UnifoLM-Dex1-Dataset**](https://huggingface.co/collections/unitreerobotics/unifolm-g1-dex1-dataset)

## 📘 Technical Documentation

- [Robot Action, State, and Statistics Processing Specification](docs/robot_action_state_processing_en.md)
- [Train and Evaluate an Action Expert](docs/train_action_expert_en.md)

## Citation

```bibtex
@misc{unifolm-wla-1.0,
  author = {Unitree},
  title  = {UnifoLM-WLA-1.0: One Model Driven, Whole-Body Coordination},
  year   = {2026},
}
```

## Acknowledgements

This project is built upon and continues the work of
[starVLA](https://github.com/starVLA/starVLA) and
[Qwen-Image](https://github.com/QwenLM/Qwen-Image). We sincerely thank their
authors and contributors for making their work publicly available.

## License

Except where otherwise noted, this project is released under the
[Apache License 2.0](LICENSE). Third-party components remain subject to their
original licenses. See [NOTICE](NOTICE) and
[THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) for attribution and details.

## 2. Hugging Face `unitreerobotics/UnifoLM-WLA-1.0-Base` — file listing (HF API)

createdAt 2026-09-28T03:58:58Z · lastModified 2026-09-28T05:07:37Z · gated: false · card license: apache-2.0
Model card README.md is 28 bytes: YAML front matter `license: apache-2.0` and nothing else.

| file | bytes |
|---|---:|
| checkpoints/model.safetensors | 12,458,898,964 |
| config.yaml | 1,069 |
| dataset_statistics.json | 10,635 (top-level keys: UnifoLM_G1_Dex1, UnifoLM_WBT) |
| tokenizer/tokenizer.json | 11,664,434 |
| tokenizer/{chat_template.jinja, config.json, generation_config.json, preprocessor_config.json, processor_config.json, tokenizer_config.json} | small |

## 3. config.yaml (verbatim)

```yaml
datasets:
  vla_data: {}
framework:
  action_model:
    action_dim: 54
    action_horizon: 30
    action_model_type: DiT-L
    add_pos_embed: true
    attention_head_dim: 48
    diffusion_model_cfg:
      attention_head_dim: 48
      cross_attention_dim: 2560
      dropout: 0.2
      final_dropout: true
      input_embedding_dim: 1536
      interleave_self_attention: true
      norm_type: ada_norm
      num_attention_heads: 32
      num_layers: 16
      output_dim: 1024
      positional_embeddings: null
    embodiment_types:
    - unitree
    hidden_size: 1024
    input_embedding_dim: 1536
    max_delay: 10
    max_seq_len: 1024
    noise_beta_alpha: 1.5
    noise_beta_beta: 1.0
    noise_s: 0.999
    num_attention_heads: 32
    num_inference_timesteps: 4
    num_timestep_buckets: 1000
    repeated_diffusion_steps: 4
    state_dim: 0
  name: QwenMMDiT
  qwenvl:
    attn_implementation: flash_attention_2
    base_vlm: ./tokenizer
  robot_state_projector:
    enabled: true
    input_dim: 120
    load_from: null
    projector_hidden_size: null
trainer: {}
```

## 4. Action/state spec — excerpts (docs/robot_action_state_processing_en.md)

## Abstract

This specification maps data from different robot embodiments into a unified action space and a unified state space:

- each future action is represented by a 54-dimensional vector;
- each current state is represented by a 60-dimensional vector;
- Boolean masks identify the modules that are actually available;
- the robot-state projector receives 120 dimensions by concatenating the 60-dimensional state and its 60-dimensional validity mask;
- end-effector and base-pose actions are represented as SE(3) transforms relative to the current state;
- all other actions retain the control semantics defined by their source dataset;
- relative-pose actions use global Z-score normalization by default;
- ordinary actions and states use 1st/99th-percentile normalization by default;
- statistics from different tasks of the same robot embodiment are merged with equal task weights, after which left/right end-effector statistics may optionally be merged.

The terms **must**, **should**, and **must not** express requirements for reproducing this data-processing pipeline.

---


## 3. Unified Action Representation

### 3.1 54-dimensional action layout

| Slice | Dim. | Module | Semantics | Canonical representation |
|---|---:|---|---|---|
| `[0:6]` | 6 | Left end effector | Future pose relative to the current left end-effector state | Relative xyz + rotation vector |
| `[6:7]` | 1 | Left gripper | Future gripper command | Raw scalar; optionally binarized after normalization |
| `[7:13]` | 6 | Left dexterous hand | Future hand-control command | First 6 raw action components |
| `[13:19]` | 6 | Right end effector | Future pose relative to the current right end-effector state | Relative xyz + rotation vector |
| `[19:20]` | 1 | Right gripper | Future gripper command | Raw scalar; optionally binarized after normalization |
| `[20:26]` | 6 | Right dexterous hand | Future hand-control command | First 6 raw action components |
| `[26:29]` | 3 | Waist | Future waist action | First 3 action components |
| `[29:32]` | 3 | Torso | Future torso action | First 3 action components |
| `[32:34]` | 2 | Base translation | Future base linear-velocity command | `vx, vy` |
| `[34:35]` | 1 | Base rotation | Future base yaw-rate command | `omega_z` |
| `[35:41]` | 6 | Base pose | Future pose relative to the current base state | Relative xyz + rotation vector |
| `[41:42]` | 1 | Height | Future height command | Scalar |
| `[42:48]` | 6 | Left leg | Future left-leg joint action | First 6 action components |
| `[48:54]` | 6 | Right leg | Future right-leg joint action | First 6 action components |


### 3.3 Non-pose actions

The following action modules are read directly from the future action sequence and do not undergo SE(3) relative-pose conversion:

- grippers;
- left and right dexterous hands;
- waist;
- torso;
- base velocity;
- height;
- left and right legs.

These fields may represent absolute targets, velocity commands, or precomputed increments, depending on the source dataset. Every dataset mapped to the same unified slot must use the same physical control semantics.


### 4.5 Model-facing 120-dimensional projector input

The canonical robot state remains the 60-dimensional vector $\mathbf s_t$. When
the robot-state projector is enabled, the model concatenates this state with its
slot-aligned 60-dimensional validity mask:

```math
\mathbf r_t
=
\mathbf s_t\mathbin\Vert\mathbf m^s
\in\mathbb R^{120}.
```

Therefore, a model configuration such as `robot_state_dim = 120` or
`robot_state_projector.input_dim = 120` means:

- dimensions `[0:60]`: the normalized robot state $\mathbf s_t$;
- dimensions `[60:120]`: the state-validity mask $\mathbf m^s$, cast to the
  projector's numerical type.

The second 60 dimensions are not additional physical state variables. They tell
the shared projector which state slots are present for the current robot
embodiment. The 54-dimensional action mask is not part of this 120-dimensional
projector input.

---


### dataset_statistics.json — action slots with non-identity normalization (offset ≠ 0 or scale ≠ 1), computed at capture

- UnifoLM_G1_Dex1: [0:7] L-EEF+L-gripper, [13:20] R-EEF+R-gripper, [26:29] waist, [32:35] base vx/vy/ωz, [41] height, [42:54] legs
- UnifoLM_WBT: [0:6] L-EEF, [7:13] L-hand, [13:19] R-EEF, [20:26] R-hand, [26:29] waist, [32:35] base vx/vy/ωz, [35:41] base pose, [41] height, [42:54] legs
- Torso [29:32] identity in both.

## 5. Model server docstring excerpt (model_server/action_server_wbc_msgpack_unitree.py)

#!/usr/bin/env python3
# Copyright 2025 unifolm_wla community. All rights reserved.
# Licensed under the MIT License.
"""Unitree G1 msgpack/websocket action server.

Speaks the exact protocol of
(``WebsocketClientPolicy``):

  - On connect, the server immediately sends msgpack-packed ``metadata``. The
    client reads it as ``self._server_metadata`` and drives what obs keys it
    will send from ``metadata["data_keys"]``.
  - Each request is a msgpack dict ``{"type": <str>, ...}``. ``get_action``
    carries ``{"obs": {...}}`` and expects an action dict back; the other
    lifecycle types (``policy_reset`` / ``episode_end`` / ...) are no-ops for
    this stateless inference server.

Observation keys the client sends (declared in ``metadata["data_keys"]``):
    observation.images.cam_left_high     -> head_left camera   (H,W,3) uint8 BGR
    observation.images.cam_left_wrist    -> left  wrist camera
    observation.images.cam_right_wrist   -> right wrist camera
    observation.state.left_ee_6d         -> (9,) xyz + rot6d (first two cols)
    observation.state.right_ee_6d        -> (9,) xyz + rot6d
    observation.state.left_gripper       -> (1,)
    observation.state.right_gripper      -> (1,)
    observation.state.lower_body         -> (15,) left_leg(6)+right_leg(6)+waist(3)

Each obs value may carry a leading time/batch axis ((T,...) or (1,...)); the
server uses the LAST frame.

Action keys returned (whole predicted chunk, UNNORMALIZED, ABSOLUTE). Each key
carries a leading batch axis of 1:
    action.left_ee_rpy    (1, T, 6)  xyz + rpy, composed onto the current left EE
    action.right_ee_rpy   (1, T, 6)  xyz + rpy, composed onto the current right EE
    action.left_gripper   (1, T, 1)
    action.right_gripper  (1, T, 1)
    action.lower_body     (1, T, 15) left_leg(6)+right_leg(6)+waist(3)
    action.base_command   (1, T, 4)  vx, vy, vw, height
    action.pivot          (1, T, 7)  vx, vy, vw, yaw, pitch, roll, height
        vx/vy/vw/height are the same 4 values as base_command; yaw/pitch/roll
        come from the waist (lower_body last 3, ordered yaw,roll,pitch) remapped
        into pivot's yaw,pitch,roll order.

The EE state the client sends is ALREADY xyz+rot6d (the state layout the model
was trained on: STATE_SLICES["*_xyz_rot6d"]), so it is placed straight into the
unified state -- NOT run through map_state's pose_to_xyz_rot6d_from_format
(which expects a 6/7-dim rpy/quat pose). The rot6d convention (first two matrix
columns, [R00,R10,R20,R01,R11,R21]) matches se3_utils.matrix_to_rot6d exactly.


413:        description="unifolm_wla Unitree G1 msgpack/websocket action server (unitree_rl_wbc client protocol)",

## 6. License history

GitHub `unitreerobotics/unifolm-wla`, commits touching LICENSE:
- 03b7a388 · 2026-09-11T08:30:55Z · "add license" — text begins "Attribution-NonCommercial-ShareAlike 4.0 International / Copyright (c) 2016-2025 HangZhou YuShu TECHNOLOGY CO.,LTD."
- c3718187 · 2026-09-20T05:05:55Z · "upd licence" — LICENSE modified (now Apache License 2.0; GitHub API spdx_id Apache-2.0); NOTICE and THIRD_PARTY_LICENSES.md added; README, README_zh, pyproject.toml modified.

Hugging Face commit history:
- UnifoLM-ER-1: 2026-09-11T08:32:18Z "Upload LICENSE" → 14:37:42Z "Update README.md" → 14:40:32Z "Delete LICENSE". Card license now apache-2.0.
- UnifoLM-ER-Flow: lastModified 2026-09-11T14:41:41Z; card license apache-2.0.
- UnifoLM-WMA-0-Dual: 2026-09-13T12:00:51Z "Update README.md" → 12:01:25Z "Delete LICENSE". Card license apache-2.0.
- UnifoLM-WMA-0-Base: card license apache-2.0; gated: auto.
- GitHub `unitreerobotics/unifolm-world-model-action`: LICENSE unchanged since 2025-09-12 "init commit" — still CC BY-NC-SA 4.0 text (GitHub spdx NOASSERTION).

## 7. HF collections (unitreerobotics), as listed 2026-09-28

- unifolm-wla-10 — 4 items, updated 2026-09-28
- unifolm-wbt-dataset (UnifoLM_WBT_Dataset) — 58 items, updated 2026-09-19; e.g. G1_WBT_Inspire_Collect_Clothes_MainCamOnly, G1_WBT_Brainco_Collect_Plates_Into_Dishwasher
- unifolm-g1-dex1-dataset (UnifoLM_G1_Dex1_Dataset) — 72 items, updated 2026-09-24; e.g. G1_Dex1_Wipe_Table, G1_Dex1_Stack_Block
- unibot-v1-challenge-dataset — updated 2026-09-11

## 8. Dataset license spot-check (HF API cardData.license, 3 datasets sampled)

- unitreerobotics/G1_Dex1_Wipe_Table — apache-2.0 (lastModified 2026-09-23)
- unitreerobotics/G1_WBT_Inspire_Collect_Clothes_MainCamOnly — apache-2.0 (lastModified 2026-03-27)
- unitreerobotics/G1_Dex1_HangCup (UniBot-V1) — no license field in card (lastModified 2026-06-30)
