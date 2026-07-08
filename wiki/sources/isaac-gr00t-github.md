---
title: Isaac-GR00T GitHub (NVIDIA/Isaac-GR00T)
type: source
url: https://github.com/NVIDIA/Isaac-GR00T
author: NVIDIA GEAR
published: 2025-03 (repo public with N1); N1.7 GA 2026-04-18 per README
ingested: 2026-07-04 (N1.7-EA-era README); re-ingested 2026-07-07 (N1.7 GA README)
format: github-repo
license: Apache 2.0 (code); NVIDIA Open Model License (weights)
tags: [groot, isaac-gr00t, vla, nvidia, gear, lerobot, finetuning, embodiment-tags, cosmos-reason, jetson, dgx-spark]
---

## Summary

The official open-source codebase for the [GR00T](../entities/nvidia-groot.md) VLA line. Ships the model, a LeRobot-v2-based data pipeline, fine-tuning + inference scripts, and a ZMQ server/client deployment stack. **Apache-2.0 code** (weights under the NVIDIA Open Model License); ~**7.5k stars / 1.3k forks**. Current release: **GR00T N1.7 General Availability** (README dates GA to **2026-04-18**); base `nvidia/GR00T-N1.7-3B`, N1.5/N1.6 on release branches. Also now advertises the **[LeRobot](../entities/lerobot.md) integration** ("available as `groot` policy type") announced in the [2026-07-07 HF blog](nvidia-isaac-teleop-gr00t17-lerobot-blog.md). This is the concrete "how to actually run/fine-tune GR00T" source behind the [GR00T N1 paper](groot-n1-paper.md) and the [N1.5](groot-n1_5.md)/[N1.6](groot-n1_6.md) research pages.

> [!warning] Contradiction — EA vs GA timeline
> The wiki's **2026-07-04 ingest of this repo recorded N1.7 as "Early Access"**; the README as of **2026-07-07 states "GR00T N1.7 General Availability (April 18, 2026)"** — a date *before* that ingest. Either the README's GA labeling/changelog was added between 07-04 and 07-07 (with a backdated GA date), or the EA framing captured on 07-04 was already stale. The [GR00T entity](../entities/nvidia-groot.md) timeline now treats 2026-04-18 as the repo GA date and 2026-07-07 as the LeRobot-integration announcement.

## Key claims

### Model versions & checkpoints
- **N1.7 GA** (default): base `nvidia/GR00T-N1.7-3B`; finetuned variants `nvidia/GR00T-N1.7-LIBERO` (`LIBERO_PANDA`), `-DROID` (`OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT`), `-SimplerEnv-Bridge` (`SIMPLER_ENV_WIDOWX`), `-SimplerEnv-Fractal` (`SIMPLER_ENV_GOOGLE`). HF collection: `nvidia/gr00t-n17`. (Distinct from the LeRobot-trained LIBERO checkpoints `nvidia/gr00t17-lerobot-libero_*-640` in the [LeRobot blog](nvidia-isaac-teleop-gr00t17-lerobot-blog.md).)
- **N1.6**: `n1.6-release` branch. **N1.5**: `n1.5-release` branch (["no longer supported"](nvidia-isaac-teleop-gr00t17-lerobot-blog.md)). Base model **3B params** throughout.
- **N1.7's four headline changes** (README "What's New"): (1) **relative-EEF action space** for cross-embodiment generalization; (2) **20K hours of [EgoScale](egoscale-paper.md) human-video pretraining**; (3) backbone swap **Eagle → Cosmos-Reason2-2B (Qwen3-VL architecture)** with flexible resolution; (4) **capacity expansion — state/action dimensions 29 → 132, action horizon 16 → 40**.

### Fine-tuning & inference workflow
- **Inference**: 1 GPU, 16 GB+ VRAM (RTX 4090 / L40 / H100 / Jetson AGX Thor / Orin / DGX Spark). **Fine-tuning**: 1+ GPUs, 40 GB+ VRAM (H100 or L40 recommended); `launch_finetune.py` single/multi-GPU.
- **Data format**: "a flavor of the **LeRobot v2** dataset format" + an added `meta/modality.json` (state/action/video key mapping). Bundled demo datasets: `droid_sample` (3 eps), `libero_demo` (5 eps), `simplerenv_bridge_sample`, `simplerenv_fractal_sample`, and `cube_to_bowl_5` (custom-embodiment example).
- **Embodiment tags** drive cross-embodiment support: `LIBERO_PANDA`, `OXE_DROID_RELATIVE_EEF_RELATIVE_JOINT`, `SIMPLER_ENV_WIDOWX`, `SIMPLER_ENV_GOOGLE`, `UNITREE_G1`, `UNITREE_G1_SONIC` (whole-body via GEAR-SONIC), and **`NEW_EMBODIMENT`** for custom robots (SO-100 example).
- Supported benchmarks/embodiments: LIBERO (Franka), SimplerEnv (Google Robot + WidowX), DROID, RoboCasa + RoboCasa-GR1, RoboLab sim, SO-100 custom workflow.
- Typical fine-tune 2,000–10,000 steps; users may see 5–6% run-to-run variance from non-deterministic image augmentation.

### Architecture & components
- "combination of vision-language foundation model and diffusion transformer head that denoises continuous actions."
- Inference service: [ZeroMQ](../entities/zeromq.md) server/client; PyTorch-eager / TensorRT / ONNX inference modes; `torchcodec` as the sole video-decoding backend (**FFmpeg 4–7 only; FFmpeg 8 unsupported**).
- The `nvidia/Cosmos-Reason2-2B` backbone is a **gated HF model** — HF authentication required at install; repo clones with `--recurse-submodules` + Git LFS for parquet demo data.

### Platform / dependency matrix (updated at GA)
- **dGPU x86_64**: Python 3.12, CUDA 12.8. **DGX Spark (aarch64)**: Python 3.12, CUDA 13.0. **Jetson AGX Thor**: Python 3.12, CUDA 13.0. **Jetson Orin**: Python 3.10, CUDA 12.6. Platform setup scripts under `scripts/deployment/` (Spark / Thor / Orin).
- Key deps: PyTorch 2.7-line, flash-attention, TensorRT, torchcodec + FFmpeg, LeRobot v2; `uv` for dependency management (`uv sync --python 3.12`).
- *(Delta from the 07-04 ingest: x86_64 and Thor moved from Python 3.10 → 3.12; Thor from CUDA 12.6 → 13.0 — Thor now matches the DGX Spark toolchain.)*

### Whole-body humanoid
- Whole-body [Unitree G1](../entities/unitree-g1.md) control via the `UNITREE_G1_SONIC` tag + the **[GEAR-SONIC](../entities/gear-sonic.md)** controller — language-conditioned coordinated manipulation + locomotion end-to-end.

## Entities mentioned
- [NVIDIA GR00T](../entities/nvidia-groot.md) — the model this repo serves. [NVIDIA GEAR](../entities/nvidia-gear.md) — maintainer.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — Cosmos-Reason2-2B (N1.7 backbone, gated on HF). [LeRobot](../entities/lerobot.md) — dataset format base + `groot` policy type. [Open X-Embodiment](../entities/open-x-embodiment.md), [DROID](../entities/droid.md), [LIBERO](../entities/libero.md), [SimplerEnv](../entities/simplerenv.md), [RoboCasa](../entities/robocasa.md).
- [Unitree G1](../entities/unitree-g1.md), [Franka Panda](../entities/franka-panda.md) (LIBERO), [SO-ARM101](../entities/so-arm101.md) (SO-100 custom example), [GEAR-SONIC](../entities/gear-sonic.md).
- Compute: [Jetson Thor](../entities/jetson-thor.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md), [DGX Spark](../entities/dgx-spark.md).

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the reference open VLA fine-tuning stack.
- [Imitation learning](../concepts/learning/imitation-learning.md) — LeRobot-format demos → fine-tune → deploy loop.
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — N1.7's 20K-hour EgoScale human-video pretraining.

## Open questions
- ~~N1.7 is Early Access — a full N1.7 paper/model card would deepen the backbone + EgoScale-integration story.~~ **N1.7 is GA (README: 2026-04-18)** — but there is still **no N1.7 research page/paper**; the 29→132 state/action-dim and 16→40 action-horizon expansion is currently README-only with no ablation or benchmark context beyond the [LeRobot-blog LIBERO table](nvidia-isaac-teleop-gr00t17-lerobot-blog.md).
- The EA→GA timeline discrepancy (see contradiction callout) — worth checking the repo's release/commit history if precision matters.
- GEAR-SONIC whole-body controller — see [entity](../entities/gear-sonic.md) and the [SONIC paper](sonic-paper.md); RoboLab sim and RoboCasa-GR1 workflows not yet detailed in the wiki.
- "RoboLab" — first appearance of this benchmark name in the wiki; unclear what it is (NVIDIA-internal sim?).
