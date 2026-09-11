---
title: UnifoLM-WMA-0 — A World-Model-Action Framework under the UnifoLM Family (project page + repo)
type: source
url: https://unigen-x.github.io/unifolm-world-model-action.github.io/
author: Unitree Robotics
published: 2025-09-15
ingested: 2026-09-11
format: web (project page + GitHub README + training config + HF model card; no paper)
local_path: raw/2025-09-15-unifolm-wma-0-project-page.md
sha256: 183b3dac4c744cfb0fb40dd72de9175f5ec8d60a810cc604d244e57e7ca9c852
license: CC BY-NC-SA 4.0
tags: [unifolm, unifolm-wma-0, unitree, world-action-model, world-model, video-diffusion, dynamicrafter, diffusion-policy, open-x-embodiment, unitree-z1, unitree-g1, china, non-commercial]
---

## Summary

**UnifoLM-WMA-0** (15 Sep 2025) is [Unitree](../entities/unitree.md)'s first open **world-model–action** release and the ancestor of [UnifoLM-WLA-1.0](unifolm-wla-1-project-page.md). It is a **DynamiCrafter** image-to-video latent-diffusion model, fine-tuned first on [Open X-Embodiment](../entities/open-x-embodiment.md) and then on five Unitree datasets, with a **Diffusion-Policy-style 1-D UNet action head** attached to the video model's features. The world model runs in two modes: **decision-making** (predict the future interaction, let the action head read it) and **simulation** (render the outcome of a given action sequence, as an interactive data engine). Demos on a [Unitree Z1](../entities/unitree-z1.md) arm (single and dual) and a [G1](../entities/unitree-g1.md) with gripper; the top-right inset in every demo is the model's predicted future video. **There are no numbers anywhere** — no success rates, no video metrics, no ablation of the world model's contribution. Training, inference and deployment code are released; weights are CC BY-NC-SA and the Base checkpoint is gated on Hugging Face.

## Key claims

### Architecture (from `configs/train/config.yaml`, not the page)

- **Backbone: DynamiCrafter** (Xing et al. 2023) — `LatentVisualDiffusion` with a KL autoencoder, frozen **OpenCLIP** text and image embedders, and a Resampler for image conditioning; the README's acknowledgement names DynamiCrafter, Diffusion Policy, ACT and HPT as code sources. Video at **320×512**, latent 40×64, **16 frames per clip at frame stride 2**, temporal conv + temporal self-attention. Main-view camera only.
- **Action head: `ConditionalUnet1D`** (Diffusion Policy's head) with **horizon 16 = the video's temporal length**, DDIM scheduler, EMA, a ResNet multi-image observation encoder, and a state–action token projector (`SATokenProjector`) that injects proprioception and actions into the diffusion stream. Max **16-D state / 16-D action** by default.
- **Two-mode training.** Step 1: fine-tune the video model on Open-X. Step 2: post-train in decision-making mode on the downstream dataset. Step 3: post-train in simulation mode. `decision_making_only: True` skips step 3. The **Base** checkpoint is after step 1; **Dual** is after steps 2–3 on the five Unitree datasets.
- **Deployment** is server/client over an SSH tunnel; the documented G1 run is `--action_horizon 16 --exe_steps 16 --observation_horizon 2 --control_freq 15` — **15 Hz control, executing full 16-step chunks open-loop** (~1.07 s per chunk).

### Data

- Five Unitree open datasets: Z1_StackBox, Z1_DualArm_StackBox (v1, v2), Z1_DualArm_Cleanup_Pencils, G1_Pack_Camera (`G1_Dex1_MountCameraRedGripper`), all LeRobot v2.1. Plus four "extra" G1 DiverseManip sets (single/dual arm, 256² and 128²) offered for world-model training, ~30 s episodes.
- Open-X for the base fine-tune — no subset or hour count given.

### What the page shows and what it does not

- Shown: **action-controllable generation** (given an image and a future action sequence, generate the video) side-by-side with ground truth; **long-term interactive generation** for long-horizon tasks; four real-robot deployments with the predicted-future inset.
- Not shown: any quantitative result, a baseline policy without the world model, an ablation of decision-making mode, generation quality metrics, or compute. The claim that predicting the future "further optimizes decision-making performance" is unsupported on the page.

## Reading it from 2026-09

- **WMA-0 is an early, small instance of the [video-action model](../concepts/world-models/world-action-model.md) shape** — video-diffusion backbone, diffusion inverse-dynamics-style action head reading its features — three months before [mimic-video](mimic-video-paper.md) named the class and on a **2023-vintage** backbone rather than Cosmos-Predict2. Unlike mimic-video, it *does* generate the video, in the loop, on the robot.
- **Unitree then abandoned pixel generation.** [WLA-1.0](unifolm-wla-1-project-page.md) replaces this entire world model with VQ-tokenized optical-flow masks of the future dynamic region inside a VLM. Read together, the two pages are a vendor concluding — with no published ablation either time — that a generative world model was not paying for itself at policy time. That aligns with mimic-video's finding that best policy performance comes at pure noise, no decoding.
- The 16-frame / 16-action alignment at 15 Hz is the same "one action per predicted frame" coupling the [WAM taxonomy](../concepts/world-models/world-action-model.md) formalizes (`aₜ` = the transition `vₜ₋₁ → vₜ`).

## Entities mentioned

- [Unitree](../entities/unitree.md), [UnifoLM](../entities/unifolm.md), [Unitree G1](../entities/unitree-g1.md), [Unitree Z1](../entities/unitree-z1.md).
- [Open X-Embodiment](../entities/open-x-embodiment.md) — base fine-tune corpus.
- [LeRobot](../entities/lerobot.md) — data format (v2.1).

## Concepts touched

- [World-action model](../concepts/world-models/world-action-model.md), [world-model simulators](../concepts/world-models/world-model-simulators.md) (Paradigm A), [world model](../concepts/world-models/world-model.md).
- [Diffusion Policy](../entities/diffusion-policy.md) — the action head.
- [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md) — the stated "simulation engine" purpose, never demonstrated with a trained-on-synthetic result.

## Open questions

- Any measured benefit of decision-making mode over the same diffusion head without the video model?
- Why the Base checkpoint is gated while Dual is open.
- Whether WLA-1.0's ≈2,500 h includes these five datasets (almost certainly) and whether any WMA-0 component survives in it (the page suggests none).
