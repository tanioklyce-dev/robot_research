---
title: Isaac-GR00T GitHub (NVIDIA/Isaac-GR00T)
type: source
url: https://github.com/NVIDIA/Isaac-GR00T
author: NVIDIA GEAR
published: 2025-03 (repo public with N1); N1.7 EA current
ingested: 2026-07-04
format: github-repo
license: Apache 2.0 (code); NVIDIA Open Model License (weights)
tags: [groot, isaac-gr00t, vla, nvidia, gear, lerobot, finetuning, embodiment-tags, cosmos-reason, jetson, dgx-spark]
---

## Summary

The official open-source codebase for the [GR00T](../entities/nvidia-groot.md) VLA line. Ships the model, a LeRobot-v2-based data pipeline, fine-tuning + inference scripts, and a ZMQ server/client deployment stack. **Apache-2.0 code** (weights under the NVIDIA Open Model License); ~**7.5k stars / 1.3k forks**. The current default is **GR00T N1.7 Early Access** (`nvidia/GR00T-N1.7-3B`); N1.5 and N1.6 live on dedicated release branches. This is the concrete "how to actually run/fine-tune GR00T" source behind the [GR00T N1 paper](groot-n1-paper.md) and the [N1.5](groot-n1_5.md)/[N1.6](groot-n1_6.md) research pages.

## Key claims

### Model versions & checkpoints
- **N1.7 EA** (default): base `nvidia/GR00T-N1.7-3B`; finetuned variants `nvidia/GR00T-N1.7-LIBERO`, `-DROID`, `-SimplerEnv-Bridge`, `-SimplerEnv-Fractal`.
- **N1.6**: `n1.6-release` branch. **N1.5**: `n1.5-release` branch. Base model **3B params** throughout.
- **N1.7 backbone = Cosmos-Reason2-2B (Qwen3-VL architecture), replacing the Eagle backbone used through N1.6** — confirms the version progression Eagle (N1/N1.5) → Cosmos-2B (N1.6) → Cosmos-Reason2-2B (N1.7).
- N1.7 pretraining adds **~20K hours of EgoScale human-video data** (see [EgoScale](egoscale-paper.md)) alongside diverse robot demos; introduces a **relative end-effector action space shared across robot and human embodiments**.

### Fine-tuning & inference workflow
- **Inference**: 1 GPU, 16 GB+ VRAM (RTX 4090 / L40 / H100). **Fine-tuning**: 1+ GPUs, 40 GB+ VRAM (H100 or L40 recommended).
- **Data format**: "a flavor of the **LeRobot v2** dataset format" + an added `meta/modality.json` (state/action/video key mapping). Demo datasets bundled (`demo_data/droid_sample`, `demo_data/libero_demo`).
- **Embodiment tags** drive cross-embodiment support: `LIBERO_PANDA`, `OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT`, `SIMPLER_ENV_WIDOWX`, `SIMPLER_ENV_GOOGLE`, `UNITREE_G1`, `UNITREE_G1_SONIC` (whole-body via GEAR-SONIC), and **`NEW_EMBODIMENT`** for custom robots (SO-100 example). Default action horizon **8 steps**.
- Typical fine-tune 2,000–10,000 steps; users may see 5–6% run-to-run variance from non-deterministic image augmentation.

### Architecture & components
- "combination of vision-language foundation model and diffusion transformer head that denoises continuous actions."
- Inference service: ZMQ server/client; PyTorch-eager / TensorRT / ONNX inference modes; `torchcodec` as the sole video-decoding backend.

### Platform / dependency matrix
- **dGPU x86_64**: Python 3.10, CUDA 12.8. **DGX Spark (aarch64)**: Python 3.12, CUDA 13.0. **Jetson AGX Thor**: Python 3.10, CUDA 12.6. **Jetson Orin**: Python 3.10, CUDA 12.6.
- Key deps: PyTorch 2.7 (Triton 3.3.1), flash-attention 2.7.4, TensorRT, torchcodec + FFmpeg, LeRobot v2; `uv` for dependency management.

### Whole-body humanoid
- N1.7 supports whole-body [Unitree G1](../entities/unitree-g1.md) control via the `UNITREE_G1_SONIC` tag + the **GEAR-SONIC** controller — language-conditioned coordinated manipulation + locomotion end-to-end.

## Entities mentioned
- [NVIDIA GR00T](../entities/nvidia-groot.md) — the model this repo serves. [NVIDIA GEAR](../entities/nvidia-gear.md) — maintainer.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — Cosmos-Reason2-2B (N1.7 backbone). [LeRobot](../entities/lerobot.md) — dataset format base. [Open X-Embodiment](../entities/open-x-embodiment.md), [DROID](../entities/droid.md), [LIBERO](../entities/libero.md), [SimplerEnv](../entities/simplerenv.md), [Metaworld](../entities/metaworld.md)-adjacent benches.
- [Unitree G1](../entities/unitree-g1.md), [Franka Panda](../entities/franka-panda.md) (LIBERO), [SO-ARM101](../entities/so-arm101.md) (SO-100 custom example).
- Compute: [Jetson Thor](../entities/jetson-thor.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md), [DGX Spark](../entities/dgx-spark.md).

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the reference open VLA fine-tuning stack.
- [Imitation learning](../concepts/learning/imitation-learning.md) — LeRobot-format demos → fine-tune → deploy loop.
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — N1.7's 20K-hour EgoScale human-video pretraining.

## Open questions
- N1.7 is Early Access — a full N1.7 paper/model card would deepen the backbone + EgoScale-integration story (currently sourced via [EgoScale](egoscale-paper.md) + this repo).
- GEAR-SONIC whole-body controller — referenced but not separately documented; the whole-body-humanoid direction N1.6/N1.7 open up.
