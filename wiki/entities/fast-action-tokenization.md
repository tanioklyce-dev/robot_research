---
title: FAST (action tokenization) / π0-FAST
type: entity
subtype: method
created: 2026-07-17
updated: 2026-07-25
sources: 5
tags: [fast, action-tokenization, dct, bpe, vla, discrete-tokens, autoregressive, physical-intelligence, pi-zero, molmoact2, open-data]
---

# FAST (action tokenization) / π0-FAST

**FAST** — **F**requency-space **A**ction **S**equence **T**okenization (Pertsch, Stachowicz, Ichter, Driess, Nair, Vuong, Mees, [Finn](chelsea-finn.md), [Levine](sergey-levine.md); [paper](../sources/fast-paper.md), arXiv 2501.09747, RSS 2025) — is a **[Physical Intelligence](physical-intelligence.md)** scheme that turns continuous robot action chunks into short discrete token sequences via **Discrete Cosine Transform (DCT) compression** + Byte-Pair Encoding. **π0-FAST** is the autoregressive [π0](pi-zero.md) policy trained on FAST tokens.

## Why it matters in this wiki

FAST is the discrete-token approach that recurs on two fronts across the wiki:

1. **As a baseline model** — π0-FAST appears in nearly every 2025–2026 VLA comparison ([VLA-0](vla-0.md), [OpenVLA-OFT](openvla-oft.md), [Cosmos 3](../sources/cosmos-3-technical-report.md)) as the autoregressive-discrete-token point of reference.
2. **As a component inside better VLAs** — the [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) recipe used by [π0.7](pi07.md) and [π*0.6](pistar06.md) supervises the VLM backbone with **FAST tokens** (next-token prediction) while a flow-matching expert does the continuous control. So FAST lives on inside the current PI flagships even though π0-FAST itself is a weaker standalone policy.

Its central insight ([FAST paper](../sources/fast-paper.md)): **naïve per-dimension/per-timestep binning fails on high-frequency data** because consecutive action tokens become highly correlated → each carries near-zero marginal information → next-token training stalls (the model degenerates to copying the last token). This is why OpenVLA fit low-frequency BridgeV2/RT-1 but struggled on DROID. Compressing in the frequency domain first restores high-information tokens.

## The FAST pipeline

Normalize actions (quantile-based, robust to outliers) → **DCT** per action dimension → **quantize** (scale-and-round; the scale γ trades compression vs. fidelity) → **flatten column-first** (low-frequency components first → more stable rollouts) → **BPE** to squash the sparse coefficient matrix into dense tokens. Fully analytical + invertible; only two (insensitive) hyperparameters — DCT rounding scale (10), BPE vocab (1024). Requires **no change to the pretrained transformer**, so it drops into any autoregressive VLA (tested on π0/PaliGemma-3B and OpenVLA/Prismatic-7B).

**FAST+** = a **universal** tokenizer trained on **~1M cross-embodied action chunks**; works black-box on any robot's 1-second chunks, released as a HuggingFace `AutoProcessor` (`physical-intelligence/fast`).

**MolmoAct2-FAST Tokenizer** — **also called `OpenFAST`** (the [MolmoAct2 paper](../sources/molmoact2-paper.md)'s arXiv abstract and the `allenai/MolmoAct2-Pretrain` model card use that name; the PDF body and blog use MolmoAct2-FAST — see the [naming table](../sources/molmoact2-paper.md)). Released as **`allenai/MolmoAct2-FAST-Tokenizer`**, self-described as *"a reimplementation of physical-intelligence/fast using fully open-sourced data."* ([MolmoAct2 paper](../sources/molmoact2-paper.md), §4.1.1) = [Ai2](ai2.md)'s **open-weight AND open-data** reimplementation of FAST for [MolmoAct2](molmoact2.md). Same principle (frequency transform → quantize → BPE → **2048-token vocab**, 1 s / 32-D padded chunks), but its contribution is **transparency**: FAST+'s released weights are not paired with a fully specified training distribution, so MolmoAct2-FAST releases both the weights **and** the exact mixture — 1M subsampled sequences across **five embodiments** ([YAM](yam.md) 30% / SO-100/101 30% / [DROID](droid.md) Franka 30% + BC-Z, Bridge, RT-1), spanning absolute-joint and delta-end-effector control. Fills the reproducibility gap in the original FAST release.

## Reported numbers (from ingested sources)

- **Compression** ([FAST paper](../sources/fast-paper.md), Table I; 1 s chunks, naïve→FAST): BridgeV2 (5 Hz) 35→20; DROID (15 Hz) 105→29; Bussing (20 Hz) 140→28; **Shirt-fold (50 Hz) 700→53 (13.2×)** — FAST lands at ~30 tokens/chunk/arm **regardless of frequency**.
- **π0-FAST vs π0-diffusion** ([FAST paper](../sources/fast-paper.md)): **matches** the SOTA π0 flow-matching VLA on dexterous/long-horizon tasks while **training up to 5× faster**; scales to 10k hours; enables the **first zero-shot DROID eval** in an unseen environment.
- **LIBERO** ([KI paper](../sources/knowledge-insulation-paper.md), Table 1): π0-FAST Spatial 96.4 / Object 96.8 / Goal 88.6 / **Long 60.2** — the weak Long score exposes autoregressive FAST decoding's cost; [KI](../concepts/learning/knowledge-insulation.md) (same team) lifts Long to 85.8.
- **RoboLab-120** ([Cosmos 3 report](../sources/cosmos-3-technical-report.md)): π0-FAST **14.9%** avg vs Cosmos3-Nano 39.7 / π0.5 28.1 / π0 3.5.
- **Inference speed** ([KI paper](../sources/knowledge-insulation-paper.md) §4): ~**750 ms** to decode a 1 s chunk on an RTX 4090 (~1.3 Hz) — the autoregressive-decoding cost that motivates flow-matching experts and [OpenVLA-OFT](openvla-oft.md)'s parallel decoding.

## Related

- [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) — uses FAST tokens to supervise the VLM backbone; the reason FAST persists inside [π0.7](pi07.md) / [π*0.6](pistar06.md).
- [π0](pi-zero.md) — the base VLA; π0-FAST = π0 + FAST tokenization.
- [OpenVLA-OFT](openvla-oft.md) / [VLA-0](vla-0.md) — the parallel-decoding and action-as-text alternatives to FAST's autoregressive-discrete-token approach.
- [DROID](droid.md) — the high-frequency dataset FAST first makes trainable.
- [MolmoAct2](molmoact2.md) — the open-data MolmoAct2-FAST reimplementation; FAST tokens as the discrete pre-training objective before the flow-matching expert.
- [VLA models](../concepts/learning/vla-models.md) — action-head taxonomy.

## Mentioned in

- [FAST paper](../sources/fast-paper.md) — the introducing primary source.
- [VLA-0 paper](../sources/vla-0-paper.md) — π0-FAST as a custom-architecture / discrete-token baseline.
- [Cosmos 3 technical report](../sources/cosmos-3-technical-report.md) — π0-FAST as a RoboLab-120 baseline.
- [π0.7 paper](../sources/pi07-paper.md) / [π*0.6 paper](../sources/pistar06-paper.md) — FAST tokens inside the Knowledge Insulation recipe.
- [Knowledge Insulation paper](../sources/knowledge-insulation-paper.md) — uses FAST as the discrete representation-learning objective; finds it beats naïve tokenization for that role.
- [MolmoAct2 paper (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — the open-weight/open-data MolmoAct2-FAST Tokenizer.
