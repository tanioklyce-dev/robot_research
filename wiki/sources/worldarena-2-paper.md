---
title: "WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform"
type: source
url: https://arxiv.org/abs/2605.17912
local_path: raw/2605.17912.pdf
author: Yu Shang, Yinzhou Tang, Yiding Ma, Zhuohang Li, Lei Jin, Weikang Su, Xin Jin, Zhaolu Wang, Ziyou Wang, Xin Zhang, Haisheng Su, Weizhen He, Wei Wu, Haoyi Duan, Gordon Wetzstein, Xihui Liu, Dhruv Shah, Zhaoxiang Zhang, Zhibo Chen, Jun Zhu, Yonghong Tian, Tat-Seng Chua, Wenwu Zhu, Chen Gao, Yong Li
venue: Preprint (arXiv 2605.17912v1)
published: 2026-05-18
ingested: 2026-08-08
license: CC BY 4.0
tags: [benchmark, world-model, evaluation, visuotactile, model-based-rl, sim-to-real, aloha, libero, robotwin]
---

## Summary

Three months after [WorldArena](worldarena-paper.md), the same group extends it along the three axes where the original was weakest: **modality** (vision → visuotactile), **functionality** (offline roles → world model as an **online interactive RL environment**), and **platform** (one simulator → [RoboTwin 2.0](../entities/robotwin.md) + [LIBERO](../entities/libero.md) + a **real AgileX Split-Type [ALOHA](../entities/aloha.md)**). 12 models.

The headline is a **sim-to-real usability gap** that is worse than the sim-to-real gap the wiki already tracks for policies. Perceptual rankings transfer across platforms reasonably well; **functional rankings do not survive contact with a real robot** — most models score 0% on real-world tasks.

The author list picks up Stanford (Haoyi Duan, **Gordon Wetzstein**) — notable because Duan is also first author of **WorldScore**, one of the benchmarks the [HAI brief](hai-world-model-spatial-intelligence-brief.md) names, which was itself co-authored by [Fei-Fei Li](../entities/fei-fei-li.md) and Jiajun Wu. The brief's benchmark list and its own byline overlap more than the brief says.

## Key claims

### Modality — visuotactile world models

Built on the **UniVTAC** simulator. The contribution is a *standardized tactile injection pipeline* that upgrades any vision-only video world model without architectural surgery: a **tactile VAE** encoding deformation maps into the existing video latent space, a **two-stream** model denoising video and tactile prediction synchronously, and an **action diffusion head** that consumes past states/actions plus predicted visuotactile latents to emit future actions.

Two contact-rich tasks, *Insert HDMI* and *Lift Bottle*:

| Model | Tactile PSNR ↑ | SSIM ↑ | Insert HDMI | Lift Bottle | Avg |
|---|---:|---:|---:|---:|---:|
| ACT (baseline, tactile tokenizer) | — | — | 20% | **80%** | 50% |
| **Wan 2.2** | **21.26** | **0.746** | **100%** | 0% | 50% |
| Vidar | 13.97 | 0.278 | 70% | 0% | 35% |
| Genie Envisioner | 13.36 | 0.456 | **0%** | **0%** | **0%** |

Two findings worth separating. First, **the general-purpose video model beats the embodied specialists at tactile prediction** — "general-purpose world models retain richer cross-modal knowledge priors that align more effectively with tactile modalities." Second, the counter-intuitive one: on *Lift Bottle* the plain **ACT baseline gets 80% while every world model gets 0%**, because that task needs sustained force control over a long horizon and "the long-horizon planning capability of current world models remains limited."

> [!warning] Genie Envisioner scores 0/0
> Second independent result in this cluster placing it at the bottom. See [Genie Envisioner](../entities/genie-envisioner.md).

### Functionality — world model as an online RL environment

The genuinely new role. Rather than evaluating frozen policies, the world model *replaces the simulator* in an RL loop: world-model environment + reward model + policy + optimizer, trained to convergence, then the optimized policy is deployed and measured. Formalized as a POMDP where the learned `P̂_ϕ(o_{t+1}|o_t,a_t)` stands in for the true transition kernel.

π0.5 success rates on RoboTwin 2.0 (proxy-based reward column):

| Training environment | Click bell | Adjust bottle |
|---|---:|---:|
| SFT (no RL) | 43.75 | 55.08 |
| **Real simulator RL** | **87.30** | **78.90** |
| WoVR | **75.00** | 67.19 |
| Ctrl-World | 69.53 | **70.70** |
| RoboScape | 68.75 | 60.74 |
| Cosmos-Predict-2.5 (action) | 67.38 | 63.48 |
| OpenSora | 56.25 | 60.16 |
| IRASim | 53.13 | 61.33 |
| iVideoGPT | 52.53 | 56.25 |

**This is the best result in the cluster for the pro-world-model case.** Every world model beats SFT; the top ones close roughly two-thirds of the gap to simulator-based RL (75.00 vs 87.30 on click bell). WoVR wins the short-horizon task, Ctrl-World the long-horizon one. The weak performers (OpenSora, IRASim, iVideoGPT) are limited by video-generation quality.

Reward-model ablation: **proxy-based** (ResNet on observation + instruction) is the most robust, beating VLM-based (Qwen-3.5, not fine-tuned for the task) and similarity-based (which inherits the world model's own prediction error).

### Platform — cross-embodiment sim-to-real

Data-engine and action-planner success rates across RoboTwin 2.0, LIBERO, and a real AgileX ALOHA (*pour water*, *wipe table*):

| Model | RoboTwin DE (T1/T2) | RoboTwin AP (T1/T2) | LIBERO DE / AP | **Real DE (T1/T2)** | **Real AP (T1/T2)** |
|---|---|---|---|---|---|
| GigaWorld | 2 / 13 | 6 / 19 | 0 / 0 | **0 / 0** | **0 / 0** |
| Genie Envisioner | 7 / 21 | 10 / 20 | 2 / 6 | 0 / 0 | 0 / 20 |
| TesserAct | 1 / 35 | 1 / 35 | 34 / 38 | 0 / 0 | 0 / 30 |
| Vidar | 13 / 53 | 2 / 19 | 22 / 14 | 40 / 0 | 30 / 10 |
| Wan 2.2 | 15 / 41 | 12 / 20 | 10 / 24 | 10 / 0 | 10 / 0 |
| CogVideoX | 3 / 28 | 8 / 16 | 0 / 2 | 10 / 10 | 0 / 50 |

Findings:

- **As a data engine, no world model matches real demonstration data, and the gap widens from simulation to reality.**
- Perceptual dimensions transfer: visual quality, motion quality, physics adherence, and 3D accuracy correlate strongly across platforms. **Content consistency and controllability do not** — "greater domain sensitivity in semantic and instruction-level alignment."
- **Functional rankings correlate between the two simulators and then "drop greatly" against real-world performance.** The paper's conclusion is blunt: "simulation performance — whether perceptual or functional — is not a reliable proxy for real-world deployment and physical evaluation remains indispensable."
- Single-simulator benchmarks are "susceptible to overfitting, leading to artificially inflated rankings" — a self-critique of WorldArena 1.0.

## Entities mentioned

- [RoboTwin 2.0](../entities/robotwin.md) · [LIBERO](../entities/libero.md) · [ALOHA](../entities/aloha.md) · [π0.5](../entities/pi-zero-5.md) · [Ctrl-World](../entities/ctrl-world.md) · [Genie Envisioner](../entities/genie-envisioner.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [ACT](../entities/act.md) · [WorldArena](../entities/worldarena.md) · [Fei-Fei Li](../entities/fei-fei-li.md)

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) · [world-model simulators](../concepts/world-models/world-model-simulators.md)
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the cross-platform result belongs here as much as anywhere.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the RL-environment role is a learned-model alternative to on-hardware RL.

## Open questions

- **The RL result and the planner result point opposite ways.** As an RL *environment* a world model gets a policy to within two-thirds of simulator-trained performance; as an *action planner* it loses to that same policy class by 3–4×. The distinction — learned dynamics are good enough to *shape* a policy, not to *be* one — is the most useful thing in the cluster and neither paper develops it.
- **Real-world numbers are mostly 0 with a few 10–50% outliers on two tasks.** At these sample sizes those outliers are barely distinguishable from noise; no confidence intervals are reported.
- **WoVR and RoboScape appear only in the RL table** with no entry in the perceptual leaderboard, so their strong showing can't be cross-checked against video quality.
- No cost or wall-clock accounting anywhere — RL inside a video world model should be expensive, and the paper doesn't say.
