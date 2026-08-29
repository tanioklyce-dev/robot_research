---
title: FAST — Efficient Action Tokenization for Vision-Language-Action Models (Pertsch et al. 2025)
type: source
url: https://arxiv.org/abs/2501.09747
author: Karl Pertsch, Kyle Stachowicz, Brian Ichter, Danny Driess, Suraj Nair, Quan Vuong, Oier Mees, Chelsea Finn, Sergey Levine (Physical Intelligence / UC Berkeley / Stanford)
published: 2025-01-16
ingested: 2026-07-18
local_path: raw/2501.09747v1.pdf
sha256: 3739b31f5fecdde371509ff5bb13619979734e894a255a9b264253f4cc53934a
venue: arXiv preprint (cs.RO), 2501.09747v1 (RSS 2025)
license: null
format: PDF (19 pages)
tags: [fast, action-tokenization, dct, bpe, vla, autoregressive, discrete-tokens, pi-zero, droid, physical-intelligence]
---

# FAST: Efficient Action Tokenization for Vision-Language-Action Models

## Summary

The [Physical Intelligence](../entities/physical-intelligence.md) paper introducing **[FAST](../entities/fast-action-tokenization.md)** — **F**requency-space **A**ction **S**equence **T**okenization — a **DCT-based compression** scheme for turning continuous robot action chunks into short discrete token sequences. Its core diagnosis: the naïve **per-dimension, per-timestep binning** that prior autoregressive VLAs ([OpenVLA](../entities/openvla.md), RT-2) use **fails completely on high-frequency, dexterous data**, because at high control rates consecutive action tokens become so correlated that each carries near-zero marginal information — so next-token training stalls (the model just copies the last token). FAST compresses actions in the frequency domain first, restoring high-information tokens. It ships **FAST+**, a universal off-the-shelf tokenizer trained on 1M robot trajectories, and shows that **π0-FAST** (autoregressive π0 + FAST) **matches the state-of-the-art π0 diffusion VLA while training up to 5× faster** and scaling to 10k hours of data.

## Key claims

- **The problem — naïve binning breaks at high frequency (§IV).** Prior VLAs discretize each action dimension per timestep into 256 uniform bins → hundreds of tokens per chunk. As control frequency rises, the change per timestep shrinks, so the **marginal information of each token → 0**; a didactic spline-interpolation study shows prediction MSE climbing steeply with sampling rate until the model degenerates to **copying the first action**. This is *why* OpenVLA worked on low-frequency BridgeV2/RT-1 but struggled to fit the higher-frequency DROID dataset.
- **The FAST pipeline (§V-B, Fig. 4).** Normalize actions (1st–99th quantile → [−1, 1], robust to outliers) → apply the **Discrete Cosine Transform (DCT)** per action dimension → **quantize** (scale-and-round; the scale γ trades compression vs. fidelity) → **flatten column-first** (low-frequency components of all dimensions first — gives more stable rollouts than row-first) → **Byte-Pair Encoding (BPE)** to losslessly squash the sparse matrix into dense tokens. Fully analytical + invertible; only **two hyperparameters** (rounding scale = 10, BPE vocab = 1024), both insensitive.
- **Why DCT** — a frequency-space transform (as in JPEG) that packs a smooth signal's information into a few low-frequency coefficients; analytical, fast, and far simpler than learned vector-quantization (VQ/FSQ), which is hyperparameter-sensitive and fails on fine-grained high-frequency control.
- **Compression (Table I).** 1-second chunks, naïve → FAST tokens: BridgeV2 (5 Hz) 35→20 (1.75×); DROID (15 Hz) 105→29 (3.6×); Bussing (20 Hz) 140→28 (5.0×); **Shirt-fold (50 Hz) 700→53 (13.2×)**. Notably FAST lands at **~30 tokens/chunk/arm regardless of frequency** — it tracks the signal's intrinsic complexity, not its sample rate.
- **FAST+ — a universal tokenizer (§V-C).** Trained on **~1M 1-second action chunks** across single-arm, bimanual, and mobile robots with joint- and EE-control action spaces at diverse frequencies. Works **black-box** on any robot's action chunks (competitive with per-dataset-tuned tokenizers); released as a HuggingFace `AutoProcessor` (`physical-intelligence/fast`), usable in ~3 lines, and `.fit()`-able to a new dataset.
- **Results with π0 (§VI).** π0-FAST **matches the π0 flow-matching (diffusion) VLA** across dexterous, long-horizon, and generalization tasks (table bussing, shirt/laundry folding, grocery bagging, toaster) **while training up to 5× faster**, and scales to **10k hours** of cross-embodied data. FAST also enables **the first efficient VLA training on DROID** and the **first zero-shot DROID evaluation in a completely unseen environment** (new table/background/objects/viewpoint), just by language prompting.
- **Architecture-agnostic.** FAST requires **no modification to the pretrained transformer** — unlike regression/diffusion heads it just replaces the action tokens, so it drops into any autoregressive VLA (tested on both π0/PaliGemma-3B and OpenVLA/Prismatic-7B).

## Entities mentioned

- [FAST / π0-FAST](../entities/fast-action-tokenization.md) — the tokenizer + the π0 policy it produces (this is the primary source).
- [π0](../entities/pi-zero.md) — the main VLA backbone; π0-FAST matches π0-diffusion at 5× less training.
- [OpenVLA](../entities/openvla.md) — the naïve-binning baseline whose DROID struggles motivate FAST; a secondary backbone tested.
- [PaliGemma](../entities/paligemma.md) — π0's VLM backbone.
- [DROID](../entities/droid.md) — the high-frequency dataset FAST first makes trainable + zero-shot evaluable.
- [LIBERO](../entities/libero.md) — a simulation benchmark evaluated.
- [Physical Intelligence](../entities/physical-intelligence.md) — the lab; [Karl Pertsch](../entities/karl-pertsch.md), [Sergey Levine](../entities/sergey-levine.md), [Chelsea Finn](../entities/chelsea-finn.md) — authors.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — FAST is the discrete-token / custom-tokenizer branch of the action-head taxonomy.
- [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) — later PI recipe that reuses FAST tokens as the VLM's representation-learning objective inside π0.7 / π*0.6.

## Open questions

- FAST compression is **not fully lossless** (γ trades fidelity for compression); the paper doesn't characterize how the residual reconstruction error bounds ultimate policy precision on the most delicate tasks.
- Alternatives to BPE (Huffman, Lempel-Ziv/gzip-class) for the lossless stage are noted but left to future work.
