---
title: "History-Guided Video Diffusion (DFoT paper)"
type: source
url: https://arxiv.org/abs/2502.06764
author: Kiwhan Song*, Boyuan Chen* (MIT), Max Simchowitz (CMU), Yilun Du (Harvard), Russ Tedrake, Vincent Sitzmann (MIT)
published: 2025-02-10 (arXiv v1); v2 2025-07-24; ICML 2025 (PMLR 267)
ingested: 2026-07-08
venue: ICML 2025
local_path: raw/Tedrake_GuidedDiffusion_2502.06764v2.pdf
format: paper PDF (39 pp)
tags: [video-diffusion, diffusion-forcing, dfot, history-guidance, cfg, world-model, long-video, imitation-learning, mit, tedrake, sitzmann]
---

# History-Guided Video Diffusion (DFoT paper)

## Summary

MIT/CMU/Harvard paper ([Tedrake](../entities/russ-tedrake.md) + Sitzmann senior) asking: can *history* — variable-length, arbitrary subsets, even frequency-filtered versions of prior frames — serve as the guidance signal for video diffusion, the way text prompts do in CFG? Standard architectures can't (fixed-size conditioning), and the obvious fix (framewise binary dropout) degrades quality. Their answer is the **Diffusion Forcing Transformer (DFoT)**: extend Diffusion Forcing's "noising-as-masking" (per-frame independent noise levels) from causal state-space models to **non-causal transformers**, so history frames are just frames at noise level 0 and the unconditional score is "all history fully noised." This unlocks **History Guidance (HG)** — a family of sampling-time score compositions — and the headline capabilities: **FVD 4.3 on Kinetics-600** (matching MAGVIT-v2, on par with industry models trained with ~10× compute), **862-frame stable rollout from a single image** on RealEstate10K, and a **physical-robot imitation result (83% success)** that composes long-term memory with reactivity at sampling time when no training episode contained both.

## Key claims

**Method**
- **DFoT training**: every frame gets an independent noise level `k_t ∈ [0,1]`; the DiT denoises all frames jointly ("noise as masking"). Conditioning on any history subset = setting those frames' noise to 0 at sampling. No separate history encoder, no AdaLN conditioning path. Theoretically justified as optimizing a reweighted **ELBO** (Thm 4.1).
- Works with existing architectures (DiT, U-ViT), and **existing video models can be fine-tuned into DFoT at ~12.5% of original training cost** with comparable results — i.e. HG is retrofit-able onto foundation VDMs.
- **History Guidance family** (score composition at sampling, Eq. 5):
  - **HG-v (vanilla)** — CFG with arbitrary-length history; big quality/consistency gains but goes *static* at high ω (copies the last frame).
  - **HG-t (temporal)** — compose scores from different history windows (long + short, or several short overlapping); fixes OOD-history blowups by keeping each score in-distribution (compositional-generative-models lineage, Du & Kaelbling 2024).
  - **HG-f (fractional)** — condition on *partially noised* history = **low-pass-filtered history** ("diffusion is spectral autoregression", Dieleman 2024); restores motion dynamics lost to HG-v without sacrificing consistency.

**Results**
- Kinetics-600 (128²): DFoT-from-scratch **FVD 4.3 ± 0.1** — beats same-architecture baselines (standard diffusion 4.8, binary-dropout 6.4, full-sequence+reconstruction-guidance 95.5) and matches MAGVIT-v2 (4.3); W.A.L.T (3.3) leads only with industry compute. 64-frame sliding-window rollout: HG-f best **FVD 170.4** vs 208 unguided / 247.5 SD / 1040 FS.
- **Binary dropout is the wrong way to get flexible history** — the ablation motivating the whole training objective (token-utilization argument: only |G| frames contribute loss).
- RealEstate10K: robust interpolation under **OOD camera rotations** where baselines produce incoherent frames (HG-t splits OOD history into in-distribution subsequences). Minecraft long-context: FVD 97.63 → **79.19** via long+short score blending.
- **Ultra-long rollout**: 862 frames from one image (RE10K navigation, ~54× the training clip length), with consistent indoor→outdoor transitions — "prior methods roll out dozens of frames" in this setup.

**The robotics result (Task 3, Appendix D.4)**
- "Fruit Swapping" imitation task (adapted from Diffusion Forcing) on a **physical robot**: needs long-term memory (which object went where) *and* short-term reactivity (recover from disturbances); **every training episode contains one behavior but never both**. HG-t composes a full-history score (memory) with a single-frame score (reactivity) at sampling time → **83% success; baselines fail completely**. A rare concrete demo of **sampling-time compositionality substituting for training-data coverage** — directly relevant to the "edge cases via composition, not more data" question in robot learning.

## Entities mentioned

- [Russ Tedrake](../entities/russ-tedrake.md) — senior author (with Vincent Sitzmann); the MIT-academic thread of his portfolio, distinct from the [TRI LBM](tri-lbm-paper.md) line but sharing the diffusion substrate. Yilun Du (Harvard; also a [Diffusion Policy](../entities/diffusion-policy.md) co-author), Max Simchowitz (CMU), Boyuan Chen + Kiwhan Song (MIT, co-first).
- Lineage: **Diffusion Forcing** (Chen et al., NeurIPS 2024 — same group; no wiki page yet), CausVid (causal-transformer scaling of DF).

## Concepts touched

- [World-model simulators](../concepts/world-models/world-model-simulators.md) — long-horizon stable video rollout is the core enabler for video-as-simulator; DFoT's 862-frame result is a stability datapoint.
- [World-action models](../concepts/world-models/world-action-model.md) — the Minecraft action-conditioned navigation setting; HG as a sampling-time knob for such models.
- [VLA models](../concepts/learning/vla-models.md) / [Imitation learning](../concepts/learning/imitation-learning.md) — the Fruit-Swapping compositional-IL result.
- [Diffusion policy](../entities/diffusion-policy.md)-adjacent diffusion machinery (score composition, CFG) applied to video rather than actions.

## Open questions

- Whether HG transfers to the frontier video/world models the wiki tracks ([Cosmos 3](../entities/nvidia-cosmos.md), DreamDojo/Predict2.5) — the 12.5%-cost fine-tune path makes that concrete; no public uptake ingested yet.
- **Diffusion Forcing** (the 2024 ancestor) has no wiki page despite now being load-bearing for two ingested lines (DFoT; CausVid citation) — candidate ingest.
- How the 83% Fruit-Swapping result generalizes beyond one task — is sampling-time behavior composition a real alternative to multitask pretraining (the [TRI LBM](tri-lbm-paper.md) answer) or complementary?
- Connection to Tedrake's stealth startup direction (he argues video backbones win for long context — this paper is his group's evidence base for controllable long-context video).
