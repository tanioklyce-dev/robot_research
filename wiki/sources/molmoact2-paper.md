---
title: "MolmoAct2: Action Reasoning Models for Real-World Deployment (Fang, Duan et al. 2026)"
type: source
url: https://arxiv.org/abs/2605.02881
author: Haoquan Fang, Jiafei Duan, et al. (Allen Institute for AI)
published: 2026-05-08
ingested: 2026-07-25
version_checked: 2026-07-28 (v2 is still latest; no v3)
code: https://github.com/allenai/molmoact2
local_path: raw/2605.02881v2.pdf
sha256: 3029bc601e4d71ebc2e45ce996cbe35649b24eeb26b5925a73c83cb83e7fadad
venue: arXiv preprint (cs.RO)
license: arXiv non-exclusive
format: pdf
tags: [molmoact2, molmoact, vla, vision-language-action, flow-matching, per-layer-kv-conditioning, adaptive-depth, fast-tokenizer, embodied-reasoning, bimanual, yam, droid, so-100, allen-institute, open-source, real-world-deployment]
---

# MolmoAct2: Action Reasoning Models for Real-World Deployment

> [!warning] The arXiv **abstract** uses three component names that appear nowhere in the paper, the blog, or the released repos
> Checked 2026-07-28. **v2 (2026-05-08) is still the latest version — there is no v3.** But the arXiv *abstract metadata* has since been updated with a different naming scheme, while the v2 PDF body was not:
>
> | arXiv abstract | v2 PDF body (127× MolmoAct2, 39× -Think, 31× Molmo2-ER, 20× -FAST) | [Ai2 blog](https://allenai.org/blog/molmoact2) | Released artifact | **Wiki uses** |
> |---|---|---|---|---|
> | `MolmoER` | **Molmo2-ER** | "Molmo 2-ER" | — | **[Molmo2-ER](../entities/molmo2-er.md)** |
> | `MolmoThink` | **MolmoAct2-Think** | "MolmoAct 2-Think" | — | **MolmoAct2-Think** |
> | `OpenFAST` | **MolmoAct2-FAST** | "MolmoAct 2-FAST Tokenizer" | `allenai/MolmoAct2-FAST-Tokenizer` | **[MolmoAct2-FAST](../entities/fast-action-tokenization.md)** |
>
> **The wiki's names match the paper body, the official blog, and the Hugging Face repo IDs** — three of four sources — so they stay. The abstract is the outlier. (arXiv permits abstract metadata edits without a version bump, which would explain it; the cause is not confirmed.)
>
> **`OpenFAST` is a live alias, not just an abstract-only artifact**: the `allenai/MolmoAct2-Pretrain` model card describes actions as represented with *"OpenFAST action tokens."* Treat **OpenFAST ≡ MolmoAct2-FAST**. Anyone searching the wiki for a name they read in the arXiv abstract would otherwise find nothing.

## Released artifacts (added 2026-07-28)

The wiki carried no repo identifiers for this paper. Code: **`github.com/allenai/molmoact2`**. On Hugging Face under `allenai/`: **MolmoAct2**, **MolmoAct2-Pretrain**, **MolmoAct2-LIBERO**, **MolmoAct2-SO100_101**, **MolmoAct2-FAST-Tokenizer**. The FAST tokenizer card describes itself as *"a reimplementation of physical-intelligence/fast using fully open-sourced data"* — which is the precise sense in which it is "open-data [FAST](../entities/fast-action-tokenization.md)."

## Summary

**MolmoAct2** is [Ai2](../entities/ai2.md)'s **fully open** action-reasoning [VLA](../concepts/learning/vla-models.md), the successor to [MolmoAct](../entities/molmoact.md), built for **real-world deployment** rather than benchmark-only performance. The paper's thesis is that today's VLAs each fail one of the deployment criteria — frontier models are **closed**; open-weight ones are **tied to expensive hardware**; reasoning-augmented policies **pay prohibitive latency**; and fine-tuned success rates stay **below the threshold for dependable use**. MolmoAct2 attacks all four by advancing its predecessor along **five axes**: (1) a stronger embodied-reasoning VLM backbone, **[Molmo2-ER](../entities/molmo2-er.md)**; (2) three new open robot datasets across low-to-medium-cost platforms; (3) an open-weight/open-data **MolmoAct2-FAST Tokenizer**; (4) a new architecture that grafts the discrete-token VLM onto a continuous flow-matching action expert via **[per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md)**; and (5) **MolmoAct2-Think**, an [adaptive-depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) variant that re-predicts depth tokens only for scene regions that change between timesteps. In the most extensive empirical study of any open VLA to date (7 sim + real benchmarks), MolmoAct2 beats strong baselines including [π0.5](../entities/pi-zero-6.md), while Molmo2-ER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. Weights, code, and complete training data are all released.

## Key claims

**Molmo2-ER backbone (§2)**
- Fine-tunes **Molmo2** (Clark et al. 2026) — a **4B** VLM using the [Molmo](../entities/molmo.md) architecture (SigLIP2 ViT → connector → LLM) — on a **3.3M-sample embodied-reasoning corpus** spanning six capability pillars: image embodied QA, image pointing, image detection, video embodied QA, multi-image/ego–exo reasoning, and abstract embodied reasoning.
- **Specialize-then-rehearse** two-stage recipe: Stage 1 fine-tunes 20K steps on the embodied corpus + 8% Tulu-3 text; Stage 2 does 1.5K steps interleaving embodied and Molmo2's original multimodal data (sweep finds p=0.5 embodied/general is the best Pareto point).
- **Result:** Molmo2-ER hits **63.8% overall avg** across 13 embodied-reasoning benchmarks — best open-weight on **9 of 13**, beating runner-up Gemini-ER 1.5 Thinking (61.3) by 2.5 points, and **+17 points over its Molmo2 starting point** (46.8). Surpasses **GPT-5** (57.9) and **Gemini 2.5 Pro** (57.1).

**Three new open robot datasets (§3)**
- **MolmoAct2-BimanualYAM Dataset** — **720 hours** of teleoperated bimanual [YAM](../entities/yam.md) trajectories, **34.5k demonstrations** across **28+ real-world tasks** (folding clothes, untangling cables, bussing tables, scanning groceries, packing medication), collected over two months. **The largest open bimanual dataset to date.** Collection setup is entirely off-the-shelf, **total cost under $6,000**; data collection supported by **Cortex AI** with strict failure-retry and no-op-duration protocols.
- **MolmoAct2-SO100/101 Dataset** — curated from **1,222 public LeRobot datasets** (377 community users): 38,059 episodes, 19.8M frames, ~184 hours. Four-stage filter: structural validity → remove eval-style datasets → license/codebase eligibility → **TOPReward quality gate** (Chen et al. 2026).
- **MolmoAct2-DROID Dataset** — quality-filtered Franka subset of [DROID](../entities/droid.md): **74,604 episodes**, 17.76M frames; uses DROID's extended language annotations + idle-frame filter (≥1s non-idle segments).
- **Language re-annotation** shared across all three: an open VLM (Qwen3.5-27B) relabels demonstrations, **doubling unique labels** from 71,121 (22%) to 146,485 (46%) — fixing the repetitive/placeholder ("lerobot_test") annotations endemic to crowd-sourced data.

**MolmoAct2-FAST Tokenizer (§4.1.1)**
- Open-weight, **open-data** implementation of [FAST](../entities/fast-action-tokenization.md) (Pertsch et al. 2025): frequency-domain transform → quantize → BPE → **2048-token action vocabulary**. Compresses **one second of 32-D continuous actions** into a compact discrete sequence.
- Its distinguishing contribution over prior FAST weights is **transparency**: trained on a fully specified mixture of **1M subsampled action sequences across five embodiments** (YAM 30% / SO-100/101 30% / DROID Franka 30% + BC-Z, Bridge, RT-1), covering both absolute-joint and delta-end-effector control. All dims padded to 32-D; 1–99 percentile normalization; grippers handled separately.

**Architecture & training (§4)** — three-stage pipeline:
1. **Pre-training** — adapt Molmo2-ER into a discrete autoregressive robot policy; predict FAST action tokens + 256-way discretized state tokens under the same next-token objective. 200K steps, 64 H100s (~5,760 GPU-hrs), 90% robot / 10% multimodal sampling.
2. **Post-training** — attach a **DiT-style flow-matching action expert** with **the same depth as the VLM (L=36 layers)**. The expert cross-attends, at each layer, to the corresponding **VLM layer's keys and values** ([per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md)) rather than only the final hidden state. Co-trains discrete (LLM) + continuous (flow) losses, `L_post = L_LM + L_flow`; **[knowledge insulation](../concepts/learning/knowledge-insulation.md)** detaches the KV path so the flow loss never back-props through the VLM. **K=4** flow samples per chunk. 100K updates, 64 H100s.
3. **Deployment** — embodiment-specific fine-tuning (K=8 flow samples; **knowledge insulation dropped**, gradients allowed through the VLM; robot-only data).
- **Inference optimization:** cache context-invariant cross-attention states across flow steps + **CUDA Graphs** on the fixed-shape flow loop → MolmoAct2 reaches **55.79 Hz** (2.42× over baseline); the continuous flow path is **3.94× faster** than the discrete autoregressive action path, so continuous is the default deployment mode.

**MolmoAct2-Think — adaptive depth reasoning (§5)**
- Before acting, predicts a compact **discrete depth representation** (Depth Anything V2 → MolmoAct's depth VQ-VAE → **10×10 grid, 128 code values**) that conditions the action expert through per-layer KV conditioning — extending MolmoAct's depth-token idea.
- **The novelty is that depth prediction is adaptive across time.** Exploiting trajectory-level temporal redundancy, it **reuses cached depth codes for static regions** and re-predicts only cells whose RGB patch changes (32×32 patch cosine similarity **< 0.996**). Geometric-reasoning cost scales with **scene change**, not the full 100-token grid.
- Fine-tuning tricks: 10% depth-token noise injection (to handle imperfect inference-time depth) + a learned **per-layer depth gate** (bias init −4) controlling how strongly each expert layer uses the depth prefix.

**Headline results (§6)**
- **[LIBERO](../entities/libero.md):** MolmoAct2 **97.2%** avg, MolmoAct2-Think **98.1%** — the top scores, above [π0.5](../entities/pi-zero-6.md) (96.9), [GR00T N1.7](../entities/nvidia-groot.md) (97.0), and **+10.6 over the predecessor MolmoAct-7B-D** (86.6). 100% on LIBERO-Object.
- **Zero-shot / out-of-the-box (DROID embodiment):** SOTA on the MolmoSpaces & MolmoBot sim benchmarks; **real-world DROID 87.1%**, beating runner-up MolmoBot by **+38.7 points**, all under random camera init and novel objects/scenes.
- **SO-100 real-world zero-shot:** **56.7%**, +11.4 over an in-house π0-SO100/101 — affordable deployment on low-cost robots.
- **RoboEval** (fine-tuned): **44.3%**, +3.8 over π0.5; also produces **shorter, smoother, more stable trajectories** (e.g. ~2× shorter joint path length on Stack Two Blocks).
- **Real-world YAM (8 in-the-wild tasks, 50 trials each):** **50.1%** avg, **+15 over OpenVLA-OFT** — wins 7 of 8 tasks spanning kitchen, study room, pantry, wet labs, and mobile manipulation.
- **OOD robustness** (spatial / lighting / language / distractor): **50.69%**, +10.8 over OpenVLA-OFT (weakest on spatial variance, 26.25%).
- **Ablations:** Molmo2-ER backbone gives **+6.0** on LIBERO-Long over plain Molmo2 (discrete-only, before any action expert); per-layer KV conditioning (95.9) beats hidden-state conditioning (94.0) and per-head KV (94.8); K=8 flow samples best (95.9); full-model co-training beats action-expert-only (93.05).

## Entities mentioned

- [Ai2 (Allen Institute for AI)](../entities/ai2.md) — the lab; radical-openness thread.
- [MolmoAct](../entities/molmoact.md) — the predecessor this work advances.
- [MolmoAct2](../entities/molmoact2.md) — this model.
- [Molmo2-ER](../entities/molmo2-er.md) — the embodied-reasoning VLM backbone.
- [Molmo](../entities/molmo.md) — the VLM lineage (Molmo2 is the base of Molmo2-ER).
- [YAM (i2RT)](../entities/yam.md) — the bimanual data-collection arm.
- [DROID](../entities/droid.md) — the Franka dataset filtered into MolmoAct2-DROID.
- [LIBERO](../entities/libero.md) — the primary sim benchmark.
- [FAST (action tokenization)](../entities/fast-action-tokenization.md) — the tokenizer method reimplemented open-data.
- [π0.5 / π0.6](../entities/pi-zero-6.md), [π0](../entities/pi-zero.md), [OpenVLA-OFT](../entities/openvla-oft.md), [SmolVLA](../entities/smolvla.md), [GR00T N1.7](../entities/nvidia-groot.md), [Cosmos](../entities/nvidia-cosmos.md) — baselines.
- Authors: Haoquan Fang & Jiafei Duan (co-first); advisors Ranjay Krishna, Dieter Fox, Joyce Chai, Zhongzheng Ren, Ali Farhadi. Institutions: Ai2, UW, NUS, UPenn, JHU, Amazon, Cortex AI, Michigan, UNC.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — hybrid discrete+continuous action head.
- [Per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md) — the architectural novelty.
- [Adaptive depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) — MolmoAct2-Think's latency mechanism.
- [Flow matching](../concepts/learning/flow-matching.md) — the DiT-style continuous action expert.
- [Knowledge insulation](../concepts/learning/knowledge-insulation.md) — used in post-training, dropped in fine-tuning.
- [Chain-of-thought](../concepts/learning/chain-of-thought.md) — depth tokens as non-textual "embodied CoT."
- [Imitation learning](../concepts/learning/imitation-learning.md) — the teleoperated-demo data regime.

## Open questions

- **Molmo2 / Molmo2-ER primary (Clark et al. 2026) not yet ingested** — the base VLM's architecture, scale, and data recipe are only summarized here.
- How does the **$6,000 off-the-shelf YAM setup** + released BimanualYAM data change the accessibility calculus for academic labs vs. the expensive-hardware π-series deployments? Worth a platforms/assistive synthesis.
- **Adaptive depth's latency win is viewpoint-dependent** — the paper notes gains are largest in third-person setups (more static background). How does it degrade on egocentric/mobile views where the whole scene moves?
- MolmoAct2-Think still runs at only ~12.7 Hz vs. 55.8 Hz for plain MolmoAct2 — is the +0.9 LIBERO gain worth ~4× the latency for deployment, or is Think a diagnostic/interpretability tool more than a control default?
