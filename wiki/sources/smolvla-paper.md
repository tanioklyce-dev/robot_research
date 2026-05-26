---
title: "SmolVLA: A vision-language-action model for affordable and efficient robotics (Shukor et al., June 2025)"
type: source
url: https://arxiv.org/abs/2506.01844
local_path: raw/2506.01844v1.pdf
author: "Mustafa Shukor*, Dana Aubakirova*, Francesco Capuano*, Pepijn Kooijmans, Steven Palma, Adil Zouitine, Michel Aractingi, Caroline Pascal, Martino Russi, Andres Marafioti, Simon Alibert, Matthieu Cord, Thomas Wolf, Remi Cadene*"
affiliations: Hugging Face, Sorbonne University, valeo.ai, École Normale Supérieure Paris-Saclay
published: 2025-06-02
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
tags: [smolvla, vla, vision-language-action, flow-matching, hugging-face, lerobot, smolvlm-2, async-inference, community-datasets, so-arm100, so-arm101, primary-source]
---

## Summary

**SmolVLA** — a **compact, efficient, community-trained VLA** from the Hugging Face LeRobot team (Shukor, Aubakirova, Capuano, …, Wolf, Cadene; June 2025). Three contributions: (1) **a lightweight architecture** built on the SmolVLM-2 backbone with **interleaved cross-attention + causal self-attention** in the flow-matching action expert; (2) **pretraining on fewer than 30k episodes from 481 community-contributed HF datasets** — roughly an order of magnitude less data than prior VLAs; (3) **an asynchronous inference stack** that decouples action execution from observation processing, enabling responsive control even when policy inference runs on a remote server.

Headline result: **SmolVLA 0.45 B beats [π0](../entities/pi-zero.md) 3.5 B by +16.6 pts on real-world SO-100 multi-task** (78.3% vs 61.7% average across pick-place + stacking + sorting) — and ties or beats [OpenVLA 7B](../concepts/learning/vla-models.md), Octo, and Diffusion Policy on LIBERO and Meta-World simulation benchmarks. This is the wiki's **clearest evidence that "smaller model + community data" can beat "bigger model + 10k hours of corporate teleop"** in the affordable-robot tier.

## Architecture (paper §3.1)

### Backbone — SmolVLM-2

- **VLM**: [SmolVLM-2](https://arxiv.org/abs/2502.02737) (Marafioti et al.) = **SigLIP** vision encoder + **SmolLM2** language decoder, optimized for multi-image/video.
- **Visual-token reduction**: 64 tokens/frame via pixel shuffle; no tiling (faster inference).
- **State**: sensorimotor state projected via a linear layer into a single token in the VLM dimension; concatenated with image + text tokens.
- **Layer skipping**: action expert reads VLM features at **layer N = L/2** (half the LLM layers, halving compute) — exploits the "best features aren't necessarily from the last layer" finding (Bolya et al., Rajasegaran et al.).

### Action expert (flow-matching)

- **Conditional flow-matching transformer** `v_θ` that predicts the vector field `u(A^τ_t | A_t) = ε − A_t` from VLM features + noisy action chunk `A^τ_t = τ A_t + (1−τ) ε`, `ε ~ N(0, I)`.
- **`τ` sampled from a Beta distribution** (following π0).
- **Hidden size = 0.75× VLM** (memory savings).
- **Interleaved cross-attention + causal self-attention** — each action-expert block is either CA (action tokens cross-attend to VLM keys/values) or SA (causal masked, so action tokens attend only to past tokens within the chunk). Empirically: interleaving gives higher success + smoother action chunks vs π0's all-SA or pure-CA designs.

### Total params
- **SmolVLA-450M** (main model): 450 M total, 100 M action expert. Uses first 16 LLM layers.
- Also evaluated at **0.24 B** and **2.25 B** variants.

## Training data (paper §3.2)

- **481 community-contributed HF datasets** filtered by embodiment + episode count + quality + frame coverage.
- **22.9 K episodes / 10.6 M frames total** — paper explicitly notes "at least one order of magnitude smaller than other state-of-the-art."
- Two standardization tricks:
  - **VLM-cleaned task annotations**: `Qwen2.5-VL-3B-Instruct` re-writes ambiguous/empty/noisy task descriptions into concise action-oriented sentences.
  - **Camera-view normalization**: manually mapped each dataset's camera names to a standard `OBS_IMAGE_1 / 2 / 3` = `top / wrist / side` order; future automation noted.

## Asynchronous inference (paper §3.3)

Decouples the standard `predict-chunk → execute-chunk` synchronous loop into:

- **RobotClient** consumes actions from a local queue.
- **PolicyServer** (possibly remote, possibly with GPUs) predicts new chunks.
- When the queue drops below a threshold fraction `g ∈ [0, 1]`, RobotClient sends a new observation to PolicyServer for the next chunk.
- **Observation similarity filter** (joint-space distance threshold ε) drops near-duplicate observations to avoid stalling on a refilling queue.
- New chunks are aggregated with the in-flight queue on overlapping timesteps (`A_t = f(A_{t−1}, Ã_t)`).

### The `g` knob (paper §3.3)

| `g` | Behavior |
|---|---|
| **0 (sequential)** | Drain entire chunk before requesting next → robot idle during inference latency. |
| **0.7 (recommended async)** | Trigger new chunk when 70% of current chunk consumed; ~30% overlap absorbs prediction errors. |
| **1 (compute-intensive)** | Send observation every timestep; maximally reactive but expensive — one forward pass per control tick. |

Analytical result: queue stays non-empty iff `g ≥ E[ℓ_S] / (∆t · n)` where `ℓ_S` = server inference latency, `∆t` = control cycle (33 ms at 30 fps), `n` = chunk size.

## Results (paper §4)

### Simulation (Table 2)

| Benchmark | Policy | Pretrain | Avg Success Rate |
|---|---|---|---|
| **LIBERO** (Spatial/Object/Goal/Long avg) | Diffusion Policy | No | 72.4 |
| | Octo (0.09 B) | Yes | 75.1 |
| | OpenVLA (7 B) | Yes | 76.5 |
| | π0 (PaliGemma-3 B, no robotics pretrain) | No | 71.8 |
| | π0 (3.3 B, robotics-pretrained) | Yes | **86.0** |
| | **SmolVLA-0.24 B** | No | 82.75 |
| | **SmolVLA-0.45 B** | No | 87.3 |
| | **SmolVLA-2.25 B** | No | **88.75** |
| **Meta-World** (Easy/Med/Hard/VeryHard avg) | Diffusion Policy | No | 10.5 |
| | TinyVLA | No | 31.6 |
| | π0 (3.5 B Paligemma) | No | 50.5 |
| | π0 (3.5 B, robotics-pretrained) | Yes | 47.9 |
| | **SmolVLA-0.45 B** | No | 57.3 |
| | **SmolVLA-2.25 B** | No | **68.24** |

### Real-world SO-100 multi-task (Table 3)

| Policy | Pick-Place | Stacking | Sorting | Avg |
|---|---|---|---|---|
| ACT (single-task) | 70 | 50 | 25 | 48.3 |
| π0 (3.5 B, multi-task) | 100 | 40 | 45 | 61.7 |
| **SmolVLA-0.45 B (multi-task)** | 75 | **90** | **70** | **78.3** |

### Real-world SO-101 single-task pick-place-lego (Table 4)

| Policy | In Distribution | Out of Distribution |
|---|---|---|
| ACT | 70 | 40 |
| **SmolVLA-0.45 B** | **90** | **50** |

> [!note] SO-101 is OOD for SmolVLA pretraining
> Paper explicitly: "SmolVLA is **not pretrained on any datasets recorded for the SO101**" — so the SO-101 performance gain is genuine cross-embodiment generalization.

### Effect of pretraining + multitask (paper §4.5)

- Pretraining on community datasets: **51.7 → 78.3** real-world average (+26.6 pts).
- Multitask vs single-task fine-tuning: additional gain on top of that.

## Implementation details (paper §4.3)

- Framework: **[LeRobot](../entities/lerobot.md)**.
- Pretrain: 200 K steps, batch 256, cosine LR (1e-4 → 2.5e-6) with 100-step warmup; AdamW (β = 0.9, 0.95); images resized to 512×512.
- Action chunks: **n = 50** actions per chunk; 10-step flow-matching at inference.
- **Action expert trained, VLM kept frozen** during fine-tuning.
- bfloat16 + `torch.compile()` + HF `accelerate` for multi-GPU.
- **~30 K GPU hours total** for the project.
- Pretrain used 4 GPUs (for batch size); can be trained on a single GPU.

## Baselines (paper §4.4)

- **π0** (3.3 B, [Black et al. 2024](pi-zero-paper.md)) — VLM + flow-matching action expert; PaliGemma backbone; 3 RGB cameras + state + language.
- **ACT** (80 M, [Zhao et al. 2023](mobile-aloha-paper.md)) — encoder-decoder CVAE; ResNet visual encoder; CVAE trained from scratch.

## Hardware (paper §4.2)

- **SO-100, SO-101** ([Cadene et al. 2024](../entities/so-arm101.md)) — Standard Open low-cost 3D-printable 6-DOF arms; **the wiki's [SO-ARM101](../entities/so-arm101.md) entity**.
- **Franka Emika Panda** — for LIBERO sim.
- **Sawyer** — for Meta-World sim.

## Entities mentioned

- [SmolVLA](../entities/smolvla.md) — model entity (new, filed by this ingest).
- [π0](../entities/pi-zero.md) — primary VLA baseline.
- [ACT](../entities/act.md) — second baseline.
- [SO-ARM101](../entities/so-arm101.md) — real-world hardware.
- [LeRobot](../entities/lerobot.md) — framework.
- [Hugging Face](../entities/hugging-face.md) — primary lab (Cadene, Wolf et al.).
- [Remi Cadene](../entities/remi-cadene.md) — co-author and LeRobot lead.
- [DROID](../entities/droid.md) — implicitly compared via π0's training data.
- [Franka Panda](../entities/franka-panda.md) — LIBERO sim platform.
- LIBERO, Meta-World — simulation benchmarks (entities exist as [metaworld.md](../entities/metaworld.md); LIBERO is a known gap — see `libero.md` if present).

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — SmolVLA establishes the affordable-tier reference point.
- [Imitation learning](../concepts/learning/imitation-learning.md) — flow-matching fine-tuning on community demos.
- Flow matching — same head as π0 but with interleaved CA + causal SA (architectural contribution).
- Async inference — practical deployment topic; novel server/client architecture for VLA control.

## Open questions

- **~~Flow matching concept page~~** — **filed 2026-05-25** as [flow-matching.md](../concepts/learning/flow-matching.md) after both π0 and SmolVLA pushed it over the load-bearing threshold.
- **~~LIBERO entity~~** — already exists at [libero.md](../entities/libero.md); the prior wording was stale.
- **Async-inference latency budget on edge hardware** — paper benchmarks on cloud GPU; how the async stack performs with the PolicyServer on a [Jetson Thor](../entities/jetson-thor.md) or [Orin NX](../entities/jetson-thor.md) (Stretch 4 onboard compute, e.g.) is an open empirical question.
- **The 481-community-dataset list** — paper mentions Appendix A.1; this ingest captures the headline numbers but not the per-dataset composition.

## Why this matters

1. **The affordable-VLA reference**. SmolVLA + LeRobot + SO-100/101 is now the canonical sub-$1k VLA stack. The wiki's [XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md), and [Grievous](../entities/grievous.md) hardware lines can all run SmolVLA.
2. **0.45 B beats 3.5 B on real-world SO-100 multi-task by +16.6 pts.** The wiki's first published evidence that **community-data + interleaved-attention + careful inference engineering beats raw param-count + corporate-data** in the affordable-robot tier.
3. **The async-inference stack is the practical-deployment piece** most VLA papers skip — it directly addresses the "robot is idle during inference" failure mode that limits VLA control rate. Now the canonical reference for this pattern.
4. **Closes a long-flagged wiki gap.** SmolVLA was referenced across [LeRobot tutorial](lerobot-robot-learning-tutorial.md), [DreamDojo](dreamdojo-paper.md), [scaling-laws-vla.md](../concepts/learning/scaling-laws-vla.md), and [vla-models.md](../concepts/learning/vla-models.md) without a primary source. Filed.
