---
title: "Agentic World Action Models (AW-0) (Liu, Niu, Zhang, Shao, …, Zhu, Wang, Fan, Darrell, 2026)"
type: source
url: https://www.alphaxiv.org/abs/2610.30136
fetch_url: https://arxiv.org/pdf/2610.30136v1
local_path: raw/2610.30136v1.pdf
sha256: 481ac13869d840b0d53ad27ca01e78221f805977e4a935b55b322cb63ee494e2
author: Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Renrui Zhang, Roei Herzig, Yutong Bai, Ken Goldberg, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi "Jim" Fan, Trevor Darrell
published: 2026-10-21
ingested: 2026-10-27
venue: arXiv (cs.RO), v1
format: "paper, ~60 pp (10 main + appendices A–K). Affiliations: UC Berkeley, NVIDIA, U. Penn. Project: agentic-wam.github.io (not inspected). No code/weights release statement in the PDF."
tags: [aw-0, world-action-model, wam, code-as-policy, agentic-robotics, mixture-of-transformers, masked-diffusion, flow-matching, skill-library, cosmos-predict, yam, sharpa-wave, robotwin, egocentric-human-data, hybrid-execution, nvidia-gear, claude-opus, gemini]
---

# Agentic World Action Models (AW-0) (2026-10-21)

## Summary

[AW-0](../entities/aw-0.md) puts a **code expert inside a [world-action model](../concepts/world-models/world-action-model.md)**. A three-expert [mixture-of-transformers](../concepts/learning/mixture-of-experts.md) jointly denoises (i) a short **skill-program slice** (discrete masked diffusion, LLaDA-style, from an SDAR-1.7B backbone with a frozen Qwen3-VL ViT), (ii) **future video** (flow matching, a DiT initialised from [Cosmos-Predict2.5-2B](../entities/nvidia-cosmos.md)), and (iii) a **64-D action chunk** (flow matching, an action DiT trained from scratch). Attention is blockwise causal in the order **code → video → action**, so the program conditions both the imagined future and the actions. **By default the generated code is never executed.** It is a planning representation, a structured chain-of-thought that conditions the action expert. An optional **hybrid mode** executes the code slice [Code-as-Policies](../concepts/agents/code-as-policy.md)-style when it passes validity gates, and otherwise falls back to the action chunk from the same forward pass. Program labels come from an **agentic annotation pipeline**: Gemini 3.1 Pro writes subtask programs against declaration-only primitive APIs, and Claude Code (Opus 4.8) acts as a coordinator that distills a **50-skill library** (23 [YAM](../entities/yam.md), 27 egocentric human). The library is then frozen and the corpus annotated with a cache. Pretraining uses **2,913 h** (1,919 h YAM teleop + 994 h egocentric human video retargeted to 22-DoF hands). Results: **80.8%** clean on [RoboTwin 2.0](../entities/robotwin.md) (best baseline WLA 64.8%), and **71.1** average rubric score on 8 real tasks across YAM grippers and [Sharpa Wave](../entities/sharpa-wave.md) hands, against 46.0 for the best baseline (DreamZero).

## Key claims

**Architecture (§2, App. A)**
- Three experts, each with its own QKV/O projections, norms and FFNs. They share attention at every layer: bidirectional within an expert, blockwise causal across experts in the order code → video → action (§2.1).
- Code: SDAR-1.7B embeddings, norms, FFNs and vocab head are **frozen**; only the MoT attention projections and modulation are trained. Frozen Qwen3-VL-2B vision tower + trainable merger; 70 visual tokens/view × 3 views. 512-token instruction+program training budget, 128-token canvas at inference (App. A).
- Video: Cosmos-Predict2.5-2B DiT with its VAE **swapped for a frozen Wan2.2 VAE** (48 channels), 9 frames at stride 4, 3 views at 224×320. Action: DiT, horizon 32. Video and action experts get Cosmos-Reason1 language embeddings via cross-attention (App. A, Table 5).
- Unified 64-D state–action space: 2 × (9-D EE pose + 22 hand joints + 1 gripper). Unused dims are zeroed. Actions are EE deltas relative to the chunk's first frame, with absolute gripper or hand-joint targets (App. A).
- **Noise resampling for predictive guidance** (Eq. 5–6): video noise is drawn from 0.5 × the pretrained high-noise Beta(7,1) distribution + 0.5 × uniform. The video loss is importance-weighted toward the pretrained distribution and the action/code losses toward uniform, so that video features stay informative for action prediction.
- **Code memory cache**: the slices generated so far are compressed into K learnable memory slots and fed back as prefix tokens. During training the true slices are replaced by the model's own predictions with probability p (§2.3).

**Data and training (§2.4, App. B)**
- Pretraining corpus: 73,101 YAM episodes (279 tasks, 1,919.3 h, 30 Hz, 3 cams) + 175,541 egocentric human episodes (327 tasks, 993.9 h, single head cam replicated into the three slots). Total 248,642 episodes and **2.08M subtask slices** (Table 7).
- Pretraining runs on 48 H100s (6 nodes), effective batch 2,592, **one epoch**. GPU-hours are not reported. Post-training: 100 demos/task, 20 epochs (App. A).
- Annotation pipeline (§2.3, Fig. 3): sample one episode per task → Gemini 3.1 Pro writes programs → a Claude Code coordinator distills and admits skills → freeze library → re-annotate. The rest of the corpus reuses a cached program when **"contact and motion evidence"** matches, and is newly annotated otherwise. Annotation cost is not reported.

**Simulation, RoboTwin 2.0 (§3.1, Table 1)** — 50 clean demos/task × 50 tasks, 50 rollouts/task

| Method | Clean | Random | Avg |
|---|---|---|---|
| π0.5 | 54.9 | **27.7** | 41.3 |
| DreamZero | 33.6 | 17.6 | 25.6 |
| EgoScale | 26.2 | 2.9 | 14.5 |
| WLA (Yang et al. 2026) | 64.8 | 3.6 | 34.2 |
| **AW-0** | **80.8** | 20.6 | **50.7** |
| AW-0 (hybrid) | 63.1 | 29.2 | 46.2 |

- Under randomization, the default AW-0 **loses to π0.5** (20.6 vs 27.7). The authors attribute this to pixel-level OOD prediction.
- Hybrid mode keeps 46% of its clean score under randomization, against 25% for default mode. It costs 17.7 points in the clean setting. **The hybrid model was trained on different demonstrations**: CaP-generated programs written by Claude Opus 4.8 on CaP-X-style primitives, following [ASPIRE](../entities/aspire.md) (§3.1). Execution mode and training data are therefore confounded.

**Real world (§3.2, Table 2)** — 100 demos/task, **3 training seeds × 16 rollouts**, randomized initial poses, rubric (partial-credit) scores

| | Arrange Fruits | Pack Backpack | Replace Lightbulb | Fold Towels | Fruits w/ Tong | Deal Poker | Flip Scoreboard | Solve Cube | Avg |
|---|---|---|---|---|---|---|---|---|---|
| π0.5 | 70.8 | 49.7 | 63.8 | 81.7 | 7.3 | 13.1 | 26.3 | 36.1 | 43.6 |
| DreamZero | 53.3 | 36.7 | 67.4 | 79.8 | 22.6 | 37.1 | 28.4 | 42.5 | 46.0 |
| EgoScale | 37.5 | 27.3 | 60.2 | 53.3 | 17.6 | 25.6 | 40.8 | 24.9 | 35.9 |
| WLA | 39.6 | 29.6 | 56.0 | 74.6 | 14.2 | 22.9 | 29.7 | 52.3 | 39.9 |
| **AW-0** | **91.7** | **64.6** | **75.0** | **84.4** | **54.2** | **58.3** | **68.8** | **72.1** | **71.1** |

(First four tasks: YAM parallel grippers. Last four: Tianji torso + two 22-DoF Sharpa Wave hands.)
- The authors' reading: the VLA baseline (π0.5) is strong on semantics, the WAM baseline (DreamZero) on contact-rich dynamics (Lightbulb, Poker), and AW-0 combines both.
- Hybrid execution on Fold and Stack Towels: **90.6 vs 84.4** for action chunks only (one task). Qualitatively, the code channel handles approach and stacking order, and direct actions handle dexterous folding (App. G.3).

**Ablations (§3.3)**
- **Code expert and attention order** (Fig. 5): w/o code → V→C→A → **C→V→A** improves in that order. Letting code condition the *video* is what helps, not only letting it read the video.
- **ViT vs VAE features for the code expert** (Table 3): 71.1 vs 55.6. ViT wins on all 8 tasks. Reconstruction latents do not support skill selection.
- **Label content** (Fig. 7): full programs beat comment-free code on 8/8 tasks, code without skills on 8/8 (Deal Poker 58.3 vs 42.0), and **natural-language subgoals on 7/8**.
- **Joint denoising vs autoregressive code** (Table 4, Fig. 6): 71.1 vs 54.5. Latency on an RTX 5090 is **0.23 s vs 0.55 s**; without code it is 0.19 s, so the code expert costs +0.04 s (+21%) for +38 points over the w/o-code variant (32.9).

**Code quality (App. F)**: the pretrained code expert reaches 89.7% teacher-forced token accuracy and an 87.5% parse rate, but **entity F1 0.534, primitive F1 0.365**, and only 29.2% of programs call a skill. Shuffling the images raises code loss by 1.774, so the code is visually grounded. The authors say precise arguments "remain areas for improvement".

**Hybrid arbitration (App. I)**: the generated slice is run **without repair**, in order, through a stage gate (not already done, not regressing, fewer than R failures), a dependency gate (every variable it reads is defined), syntax/whitelist/vacuity gates, and a skip-hopeless-retry gate. When code execution is *attempted*, the action chunk is discarded even if the code raises an exception.

**Failure cases (App. H)**: grasping the basket rim instead of the fruit, dragging the backpack over while pulling the zipper, an off-axis lightbulb, closed tong tips poking the pear, cards slipping during a hand-to-hand handover, a fingertip sliding off a card edge. All are contact or geometry failures. None is a planning failure.

## Reading notes (wiki inference)

- **The inversion that matters.** In the [code-as-policy](../concepts/agents/code-as-policy.md) lineage (CaP → CaP-X → ASPIRE → RPG), code is the *actuator* and learned policies are callable tools. AW-0 flips this: code is an *internal planning token stream* inside a learned policy, and execution is optional. Its own Related Work says so ("we instead bring code inside an end-to-end model"). The related-work authorship overlaps (Goldberg, Wang, Fan and Zhu are on CaP-X), so this reads as the GEAR/Berkeley code-as-policy group building the end-to-end half itself rather than an outside rebuttal.
- **Why code beats subgoal text is only half-answered.** Structure (skills, call syntax) beats language subgoals on 7/8 tasks, and comments help on top. But the code labels come from a frontier-model pipeline with a curated skill vocabulary. Some of the gain may come from **better-segmented, more consistent annotations** rather than from the code form itself. No ablation holds the segmentation fixed and varies only the surface form.
- **The randomized result undercuts the "visual foresight" story.** The default model loses to π0.5 under domain randomization. The WAM's pixel-level prediction is the thing that breaks, and the executable-code channel is what partly rescues it. This matches the [WAM page's](../concepts/world-models/world-action-model.md) running theme that pixel fidelity is not what policies need. It also matches the ViT-vs-VAE ablation: reconstruction latents are poor *semantic* features.
- **Rubric scores, not success rates**, on the real robots. The 3-seed × 16-rollout protocol is better-disclosed than most. All baselines get the same post-training demos. Baselines are not pretrained on AW-0's 2,913 h corpus, though, so the comparison mixes architecture with pretraining data.
- **Cost is unreported again**, on two axes: pretraining GPU-hours and frontier-model annotation spend. The code-as-policy page's standing open question ("nobody reports cost") now extends to the *training-time* use of agents.
- **Name collision**: the **WLA** baseline here is Yang et al. 2026 (SJTU-DENG-Lab, autoregressive subtask + subgoal image + action). It is **not** Unitree's [UnifoLM-WLA-1.0](unifolm-wla-1-project-page.md).

## Entities mentioned
- [AW-0](../entities/aw-0.md) (new)
- [NVIDIA GEAR Lab](../entities/nvidia-gear.md), [NVIDIA](../entities/nvidia.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md) (Cosmos-Predict2.5-2B video init; Cosmos-Reason1 embeddings)
- [Jim Fan](../entities/jim-fan.md), [Yuke Zhu](../entities/yuke-zhu.md), [Guanzhi Wang](../entities/guanzhi-wang.md), [Ken Goldberg](../entities/ken-goldberg.md)
- [YAM](../entities/yam.md), [Sharpa Wave](../entities/sharpa-wave.md)
- [RoboTwin 2.0](../entities/robotwin.md)
- [CaP-X](../entities/cap-x.md), [ASPIRE](../entities/aspire.md) (hybrid-mode demo generation)
- [Physical Intelligence](../entities/physical-intelligence.md) (π0.5 baseline), [Qwen](../entities/qwen.md) (Qwen3-VL ViT), [Anthropic](../entities/anthropic.md) (Claude Code / Opus 4.8 as annotation coordinator), [Google DeepMind](../entities/google-deepmind.md) (Gemini 3.1 Pro annotator)
- Baselines without wiki pages: DreamZero (NVIDIA GEAR WAM), WLA (Yang et al. 2026). Pretraining backbones without pages: SDAR-1.7B, Wan2.2 VAE. Tianji torso.

## Concepts touched
- [World-action model](../concepts/world-models/world-action-model.md)
- [Code as policy](../concepts/agents/code-as-policy.md)
- [Agent skills](../concepts/agents/agent-skills.md)
- [Mixture of experts / MoT](../concepts/learning/mixture-of-experts.md)
- [VLA models](../concepts/learning/vla-models.md)

## Related sources
- [EgoScale paper](egoscale-paper.md) — baseline; same Sharpa Wave hand; overlapping NVIDIA authorship.
- [CaP-X paper](cap-x-paper.md), [ASPIRE paper](aspire-paper.md), [RPG paper](rpg-guided-self-improvement-paper.md) — the execute-the-code lineage this paper internalizes.
- [Cosmos 3 technical report](cosmos-3-technical-report.md) — the other MoT WAM in the wiki.
- [DreamDojo paper](dreamdojo-paper.md) — sibling GEAR Dream* line; DreamZero (baseline) has no source page.
- [RoboTwin 2.0 paper](robotwin2-paper.md).

## Open questions
- Does the code help because of its *form*, or because the agentic pipeline produces cleaner subtask segmentation? A control with identically segmented language subgoals would separate the two.
- Hybrid-mode robustness in sim is confounded with different (CaP-generated) training demos. What does hybrid execution do on the *same* post-trained model in sim?
- How does the frozen 50-skill library cope with a downstream task whose motions are not in it? The cache falls back to fresh annotation, but the vocabulary is frozen.
- With entity F1 0.53 and primitive F1 0.37 offline, how often does the hybrid mode actually pass the gates on real hardware? The paper reports no gate-pass rate.
- Pretraining compute and annotation token spend.
- Release status: no code, weights or dataset statement in the PDF.
