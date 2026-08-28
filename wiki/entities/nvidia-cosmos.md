---
title: NVIDIA Cosmos
type: entity
subtype: product
created: 2026-05-06
updated: 2026-08-27
sources: 36
tags: [cosmos, world-model, omnimodal, mixture-of-transformers, world-action-model, video-generation, nvidia, foundation-model, edge]
---

NVIDIA's world foundation model and simulation platform for modeling physical environments at scale. Underpins downstream world-model simulators including [Genie Envisioner](genie-envisioner.md) (AGIBOT) and [DreamDojo](../sources/dreamdojo-paper.md) (NVIDIA GEAR). As of **Cosmos 3 (June 2026)** the platform consolidated from a set of separate models into a single **omnimodal world model** (a [world-action model](../concepts/world-models/world-action-model.md)).

## Cosmos 3 (June 2026) — the omni-model

The major release that subsumes the earlier separate Cosmos-Predict / Cosmos-Reason / Cosmos-Transfer / Cosmos-Policy models into **one** [Mixture-of-Transformers](../sources/cosmos-3-technical-report.md) network jointly modeling **language, image, video, audio, and action** for both understanding and generation ([Cosmos 3 technical report](../sources/cosmos-3-technical-report.md), led by [Ming-Yu Liu](ming-yu-liu.md)).

- **Dual-tower MoT**: an autoregressive **reasoner** tower (next-token prediction, initialized from Qwen3-VL) + a diffusion **generator** tower (flow-matching), sharing joint attention. The same model operates as a VLM, T2I/T2V/I2V generator, audio-visual generator, forward-/inverse-dynamics model, or video-action **policy** — no architectural changes between modes.
- **Variants**: **Cosmos3-Edge (4B)**, **Cosmos3-Nano (16B)**, **Cosmos3-Super (64B)** — Nano/Super released under **OpenMDW-1.1** with code, checkpoints, SDG datasets, and the Cosmos-HUE benchmark. Cosmos3-Edge, previously deferred, was **delivered 2026-07-20** ([HF blog](../sources/nvidia-cosmos3-edge-hf-blog.md)) to the [Jetson Thor](jetson-thor.md) lineup as an on-robot embodied foundation model that "can post-train for a specific embodiment in ~a day" ([Thor T3000/T2000 blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md), 2026-07-15).
- **Cosmos 3 Edge, as shipped** ([HF blog](../sources/nvidia-cosmos3-edge-hf-blog.md), 2026-07-20): 4B; **15 Hz real-time control on [Jetson Thor](jetson-thor.md), 32 actions/inference @ 640×360** — the wiki's first 2026-class *edge* rate for a model of this kind (see the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md)). Ships with **Cosmos3-Edge-Policy-DROID** (4B, [DROID](droid.md)-finetuned) plus two **step-distilled 64B Super** models (**50→4 denoising steps, ~25× faster**): I2V **#1 on Artificial Analysis** (2026-07-23), T2I **#2 among open-weight**. Architecture confirmed as **dual-tower** (autoregressive understanding + diffusion generation, shared multimodal attention) with a **unified action representation** across vehicle ego-pose / camera motion / end-effector pose / gripper state, and **bidirectional action flow** (predict effects of actions, or infer actions from visual change). Also **#1 among 4B models on VANTAGE-Bench**. Distillation *recipes* released, not just distilled weights. **Edge license unstated** in the blog (Nano/Super are OpenMDW-1.1).
- **Headline results**: **#1 open-weight Text-to-Image and Image-to-Video** (Artificial Analysis, 2026-05-28); **#1 policy model on [RoboArena](roboarena.md)** real-world leaderboard (2026-05-30) — the *pairwise-preference* leaderboard, so this is an **ordering** claim, not a success rate; how many comparisons back it is unpublished; Cosmos3-Nano-Policy-DROID beats π0.5 on [RoboLab-120](nvidia-robolab.md) (39.7% vs 28.1% under specific instructions) — **rollouts-per-task unpublished; at one rollout per task the 11.6 pp gap would not be statistically separable (p=0.058)**, see the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md). SOTA reasoning in robotics/smart-infra/driving among open + most closed baselines (trails Gemini 3.1 Pro on general + robotics).
- **Central method claim**: **unified action mid-training** across camera / autonomous-vehicle / robot / egocentric embodiments yields a reusable action prior that accelerates adaptation (LIBERO-10 new-embodiment: 24.6% vs 0.0% at 500 post-train iters for mid- vs pre-trained init).
- **Coming to [LeRobot](lerobot.md) "soon"** ([NVIDIA + HF partnership blog, 2026-07-06](../sources/nvidia-hf-lerobot-open-robotics-blog.md)) — pitched for data generation/augmentation, scenario simulation, and policy development "when real-world data is limited or too expensive"; no date, variant, or integration surface announced.

## Cosmos 3 Transfer in practice — the first hands-on recipe

The [Cosmos 3 technical report](../sources/cosmos-3-technical-report.md) says Cosmos 3 *subsumes* the old separate Cosmos-Transfer model. The [Seeed × NVIDIA DLI course](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) shows what that looks like at the command line, and it is the wiki's first source with concrete operating parameters:

- **Transfer is a mode, not a model**: `"model_mode": "video2video"` in the inference spec, taking a source video + control signals + a structured JSON prompt.
- **Control signals**: **Edge** (Canny, auto-computable), **Segmentation** (requires SAM2), **Blur** (auto-computable), **Depth** (requires DepthAnything). Working recipe for robot footage: **edge 0.9 / seg 0.1**, `guidance 3.0`, `control_guidance 1.5`. Only the *ratio* of control weights matters; they should sum to ~1.0. High edge weight is what keeps the robot's geometry from warping — and therefore what makes the original action labels still valid for the restyled video (see [generative data augmentation](../concepts/learning/generative-data-augmentation.md)).
- **VRAM footprint, first published per-variant figures**: **Cosmos3-Nano ≈ 24 GB** (single RTX 4090 / A5000 / **[Jetson AGX Thor](jetson-thor.md)**); **Cosmos3-Super ≈ 80 GB × 4** (4× A100/H100). Nano being single-4090-runnable is the number that decides whether a small lab can use this at all.
- **Recommended frame range is [24, 200]**; longer clips fall back to **chunked autoregressive generation** (`num_video_frames_per_chunk` 57, or 33 under memory pressure, 1 conditional overlap frame), with degraded inter-chunk consistency.
- **Running Nano on Jetson requires a patch.** On L4T R39 + CUDA 13.2 + PyTorch 2.10, `torch.addmm` raises `CUBLAS_STATUS_NOT_INITIALIZED` from `cublasLtMatmulAlgoGetHeuristic`; the workaround monkey-patches `F.linear`/`nn.Linear.forward` into separate `matmul + add`. `--no-use-torch-compile` and `--no-use-cuda-graphs` are **required**, not optional, on ARM.

> [!note] The recipe is documented; the benefit is not
> That course's own augmented output is self-assessed as *"not the best"* (480p, prompt-quality issues), and it never runs the policy-transfer test that would show whether the augmentation improves real success rate. Treat these parameters as a starting point, not a validated configuration.

## Capabilities (pre-Cosmos-3 line)
- Generates physically-plausible video rollouts of dynamic scenes.
- Variants released as "Cosmos-Predict" series — e.g. Cosmos-Predict2-2B-Video2World powers [GE-Sim2](genie-envisioner.md); **Cosmos-Predict2.5** is the backbone of [DreamDojo](../sources/dreamdojo-paper.md) (NVIDIA GEAR, ICML 2026 Spotlight) — a latent video diffusion model with DiT blocks + WAN2.2 tokenizer + flow-matching training, the architectural substrate for generative-video world models.
- Used for autonomous-driving simulation, robot training, games, and metaverse applications requiring high-throughput simulation.

## Cosmos as the GR00T VLM backbone
The [GR00T](nvidia-groot.md) VLA line migrated onto Cosmos across two releases — a concrete instance of the Cosmos *reasoning* tower feeding the GR00T *policy* line:
- **[GR00T N1.6](../sources/groot-n1_6.md)** (Dec 2025) — internal **Cosmos-2B VLM variant** trained on general VL + embodied-reasoning (next-action prediction); replaced the Eagle backbone used through N1.5.
- **[GR00T N1.7 EA](../sources/isaac-gr00t-github.md)** — **Cosmos-Reason2-2B (Qwen3-VL architecture)**, confirmed via the Isaac-GR00T repo. Note Cosmos 3's reasoner tower is itself initialized from Qwen3-VL — the two lines share architectural ancestry.

## Why it matters
Cosmos is the underlying generative video model that's enabling the rise of [World-model simulators](../concepts/world-models/world-model-simulators.md) in agentic robotics — where the simulator is a learned model rather than a physics engine. Sits in **paradigmatic contrast** to the [JEPA](../concepts/world-models/jepa.md) / latent-prediction world-model line ([V-JEPA 2](v-jepa-2.md), [LeWorldModel](leworldmodel.md)) — Cosmos generates pixels; JEPA predicts representations. Cosmos 3 sharpens this: it is the strongest **generative-video-side** demonstration that one pixel-predicting model can also be a competitive real-robot **policy** (see [generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md)), without crossing over to latent-space planning.

## Related
- [Cosmos 3 project page](https://research.nvidia.com/labs/cosmos-lab/cosmos3/) — the Cosmos Lab landing page (reviewed 2026-07-16, **re-reviewed 2026-07-21**; content already captured by the ingested [technical report](../sources/cosmos-3-technical-report.md) — no separate source page, to avoid duplication). Canonical citation is **arXiv:2606.02800**; **v4 (2026-06-24) was diffed against the ingested 2026-06-01 lab PDF on 2026-07-21 — no substantive change**, see the version-check callout on the source page. Frames Cosmos 3 as connecting "understanding, generation, simulation, and action through a shared omnimodal world model"; #1 open model on Physical-AI reasoning + generation.
- [RoboLab](nvidia-robolab.md) — the NVIDIA SRL sim benchmark Cosmos 3 policies are scored on (RoboLab-120).
- [Genie Envisioner](genie-envisioner.md) — built on Cosmos-Predict2.
- [NVIDIA](nvidia.md) — vendor.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — adjacent stack components for synthetic data.

## Mentioned in

> [!note] Curated list — **36** source pages link here; the ones below are those that shaped this page.

- [Cosmos 3 Technical Report](../sources/cosmos-3-technical-report.md)
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — Cosmos-2B VLM backbone
- [Isaac-GR00T GitHub](../sources/isaac-gr00t-github.md) — Cosmos-Reason2-2B (N1.7 backbone)
- [Develop Physical AI with NVIDIA Cosmos 3 (HF blog)](../sources/nvidia-cosmos-3-hf-blog.md)
- [NVIDIA + HF LeRobot partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md) — Cosmos 3 coming to LeRobot "soon" (data gen/augmentation for policy training).
- [Jetson Thor T3000/T2000 blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md) — Cosmos 3 Edge (4B) delivered to the Thor edge lineup.
- [Cosmos 3 Edge (HF blog, 2026-07-20)](../sources/nvidia-cosmos3-edge-hf-blog.md) — the Edge launch: 4B, 15 Hz on Thor, Policy-DROID variant, step-distilled Super models.
- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — Cosmos3-Nano Transfer as a data-augmentation step: control weights, VRAM, chunking, and the Jetson cuBLASLt patch.
- [AGIBOT Genie Envisioner 2.0 Announcement](../sources/agibot-genie-envisioner-2-announcement.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [DreamDojo Paper](../sources/dreamdojo-paper.md)

## Cosmos-Predict 2.5 measured — and the text-vs-action natural experiment

[WorldArena](worldarena.md) evaluates Cosmos-Predict 2.5 in **both** a text-conditioned and an action-conditioned variant, which makes it the wiki's cleanest evidence that action conditioning is load-bearing rather than cosmetic:

| | Text-conditioned | Action-conditioned |
|---|---:|---:|
| EWMScore | 50.81 (13th of 14) | **55.90** (6th) |
| Trajectory accuracy | 0.0816 | **0.2945** |
| Instruction following | 0.2664 | **0.5840** |

As a **policy evaluator** it correlates only **r = 0.483** with the RoboTwin simulator's policy ranking, against [Ctrl-World](ctrl-world.md)'s 0.986 — so it is not usable as an evaluation harness. As an **RL environment** it does better, at 67.38 / 63.48 ([WorldArena 2.0](../sources/worldarena-2-paper.md)). ([WorldArena paper](../sources/worldarena-paper.md))

## Mentioned in (additional)

- [WorldArena paper](../sources/worldarena-paper.md) · [WorldArena 2.0 paper](../sources/worldarena-2-paper.md)

## The Cosmos-1 tokenizer as a control representation: lowest measured

Separate from Cosmos-Predict's showing in [WorldArena](worldarena.md), the **Cosmos-1 image tokenizer** was probed as a frozen representation for action recovery and lands near the bottom of eight encoder families: **−0.36 frozen, −0.29 after inverse-dynamics tuning**, and it becomes *more* negative as visual perturbation strengthens — "still prioritizing appearance even after action supervision." It attains among the highest pixel-reconstruction PSNR in the study while posting among the lowest action R² ([action-relevant latents](../sources/action-relevant-latents-paper.md)).

That pairing — top of the pixel-fidelity axis, bottom of the action axis — is the cleanest single illustration in the wiki that **reconstruction quality and control utility are orthogonal**.

## Mentioned in (additional)

- [What Makes Video World Model Latents Action-Relevant](../sources/action-relevant-latents-paper.md)

## Cosmos as a latent space (not a world model)

A third measurement of the Cosmos encoder, this time as the latent space of someone else's diffusion world model on Bridge V2. It behaves like the other reconstruction-aligned encoders: **strong pixel-level scores, weak everything else** — 0.244 consensus VLA success (vs V-JEPA 2.1's 0.362), the **worst CEM action-recovery error in the study at k=4 (0.661)**, and IDM Pearson r of 0.626/0.673 against V-JEPA's 0.829/0.865 ([Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md)).

At larger DiT scale, Cosmos closes much of the *policy-success* gap — better rendering helps a pixel-consuming VLA — but still lags on CEM error, IDM r, and classifier accuracy. The consistent story across three independent studies: **the Cosmos encoder reconstructs well and does not organize its latent space around what actions control.**

## Mentioned in (additional)

- [Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md)
