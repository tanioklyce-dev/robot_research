---
title: "What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction (Yeom et al., 2026)"
type: source
url: https://arxiv.org/abs/2606.07687
local_path: raw/2606.07687.pdf
author: Jewon Yeom, Hanseul Kim, Jeongjae Park, Sungmok Jung, Jaejin Lee, Taesup Kim
affiliations: Graduate School of Data Science, Seoul National University
venue: Preprint (arXiv 2606.07687v1)
published: 2026-06-05
ingested: 2026-08-08
license: CC BY 4.0
tags: [jepa, world-model, evaluation, inverse-dynamics, representation-learning, libero, v-jepa-2, probe, action-relevance, vla]
---

## Summary

**The mechanism behind [WorldArena](worldarena-paper.md)'s headline, measured one level down — and this one spans both world-model families.** WorldArena showed that video quality doesn't predict planning utility at the *system* level for pixel predictors (r = 0.360). This paper shows the same dissociation at the *representation* level, across eight encoder families including JEPA, using a single shared instrument: a frozen-feature **inverse-dynamics probe** that asks whether you can recover the action that produced a transition.

The result: **pixel-prediction quality and action recoverability are largely orthogonal.** Backbones with nearly identical reconstruction quality (~20 dB PSNR) span frozen action R² from near zero to 0.46, and the highest-PSNR models — SDXL VAE and the [Cosmos](../entities/nvidia-cosmos.md)-1 tokenizer — post the *lowest* action R², at or below zero.

This is the wiki's answer to the incommensurability problem the [WorldArena cluster](../syntheses/world-models/what-world-models-are-measurably-good-for.md) exposed. A shared probe protocol, held fixed while only the encoder varies, puts latent predictors and pixel generators on one axis for the first time.

## Key claims

### Setup

- **Instrument**: a common inverse-dynamics head `g(f(o_t), f(o_{t+1})) → â_t` added during world-model training or fine-tuning, then **discarded**; the frozen trunk is probed with an MLP `[D→256→128→7]` (3,000 steps, 3 seeds). Chosen over forward dynamics, temporal contrastive, and single-frame action prediction via ablation — inverse dynamics gives the largest lift under matched compute.
- **Benchmark**: [LIBERO](../entities/libero.md), 7-DoF actions, on a **task-OOD split** — 104 training tasks, **26 held out entirely** from world-model training. Probes trained on 400 episodes, evaluated on 200 held-out-task episodes. Cross-checked on [Metaworld](../entities/metaworld.md) and CALVIN.
- **Eight encoder families**: V-JEPA 2 / V-JEPA 2.1 (latent prediction), VideoMAE (pixel MAE), Web-DINO and SigLIP 2 (image SSL), SDXL VAE and Cosmos-1 tokenizer (pixel reconstruction), LAPA (latent action quantization), a from-scratch pixel-diffusion model, and a **Dreamer 4** reproduction.
- To place encoder-only backbones on the same axes as pixel generators, a 17M-parameter decoder is trained on each frozen representation purely to yield a comparable PSNR.

### Pixel fidelity does not predict action structure

At PSNR ≈ 20 dB, frozen action R² spans **−0.01 to +0.46**; models with similarly poor action structure differ by almost **14 dB** in PSNR. "Optimizing for visual fidelity alone encourages representations that preserve appearance and texture without organizing latent space around controllable aspects of the environment."

> [!note] This dissociation is older than the wiki recorded
> The paper credits **Tian, Finn & Wu (ICLR 2023)**, "A control-centric benchmark for video prediction," with first showing that perceptual metrics rank video predictors differently from control success. The insight predates [WorldArena](worldarena-paper.md) by three years; what 2026 added was scale and a system-level version.

### The inverse-dynamics lift, by family (LIBERO task-OOD, action R²)

| Family | Backbone | Params | Frozen | +ID | Δ |
|---|---|---:|---:|---:|---:|
| Video + JEPA prediction | **V-JEPA 2 ViT-L** | 304M | 0.40 | **0.85** | **+0.45** |
| Video + JEPA prediction | V-JEPA 2.1 ViT-B | 87M | 0.44 | 0.82 | +0.38 |
| Video + pixel MAE | VideoMAE V1 ViT-L | 304M | 0.46 | 0.75 | +0.29 |
| Latent action quantization | LAPA-LAQ-OpenX | 344M | 0.41 | 0.51 | +0.10 |
| Pixel diffusion | DIFF (LIBERO-native) | 91M | 0.43 | 0.57 | +0.14 |
| Image SSL | Web-DINO ViT-L | 304M | −0.01 | 0.16 | +0.17 |
| Image SSL | SigLIP 2 ViT-L | 316M | 0.05 | 0.17 | +0.12 |
| Pixel reconstruction | SDXL VAE | 34M | −0.55 | −0.41 | +0.14 |
| Pixel reconstruction | **Cosmos-1 tokenizer** | 34M | −0.36 | −0.29 | +0.07 |
| Shortcut-forcing dynamics | Dreamer 4 | 64–276M | −0.04 | −0.04 | **0.00** |

Three readings:

1. **The ID loss is a multiplier, not a manufacturer.** It amplifies temporally predictive structure already present — +0.45 on V-JEPA, exactly **0.00** on Dreamer 4. "Inverse dynamics cannot manufacture temporal structure absent from the representation."
2. **Capacity is not the explanation.** V-JEPA 2.1 ViT-B at **87M** (+ID 0.82) beats the 91M pixel-diffusion model (0.57) by 0.25, and scaling Dreamer 4 from 64M to 276M leaves it flat at −0.04.
3. **Frozen R² doesn't separate the top families** — video SSL, pixel diffusion, and latent-action quantization all cluster in [0.40, 0.46]. Separation appears only under adaptation, so what matters is "not the amount of action information at initialization but how readily the latent space supports action-oriented adaptation."

### How much of the win is JEPA specifically?

A partial deflation of the JEPA story, and the most useful thing here for the wiki's [JEPA](../concepts/world-models/jepa.md) thread. Decomposing at matched ~300M scale:

- **Natural-video temporal context** explains most of the gap over image-only SSL (Web-DINO +ID reaches only 0.16).
- **The JEPA feature-level predictive objective adds ~0.10 R²** over pixel-level masked autoencoding (V-JEPA 2 +ID 0.85 vs VideoMAE +ID 0.75).

So: video pretraining is the big lever, latent prediction is a real but smaller second one.

> [!warning] But do not group V-JEPA with image-only "semantic SSL"
> Web-DINO and SigLIP 2 stay at **0.16–0.17** after ID tuning, clustered with reconstruction encoders, and a λ sweep across five orders of magnitude leaves them in a 0.1-wide band — "the limitation is representational rather than optimization-related." Directly relevant to [DINO-WM](../entities/dino-wm.md), which builds a world model on a frozen image-SSL encoder.

### The advantage is concentrated on rotation

Translation and gripper state are recoverable from relatively weak features. **Rotation is the axis that separates the families**: Web-DINO and SigLIP produce *negative* rotation R² even after ID supervision, and the pixel-reconstruction models show the same rotation-specific collapse while preserving translation. Only V-JEPA sustains all three simultaneously — "the dimension requiring physically coherent latent dynamics."

**Per-layer probe of V-JEPA 2 ViT-L**: frozen action R² peaks at **layer 14 (0.51)** and decays monotonically to **layer 22 (0.39)**; the ID fine-tune lifts the final four layers by **+0.25 to +0.32**, moving the peak to layer 21. The JEPA objective pushes action-readout quality *away* from the final layers — an "emerge-then-degrade" profile matching what Joseph et al. report for physical-variable decoding. Practical consequence: **if you take features off the last layer of a V-JEPA trunk, you are sampling near its worst point for action decoding.**

### Robustness

Frozen pretrained encoders are catastrophically appearance-coupled; ID supervision changes what survives distribution shift.

| Backbone | Clean | Noise 0.15 | Blur 11 |
|---|---:|---:|---:|
| V-JEPA 2 ViT-L **frozen** | 0.40 | −1.18 | **−4.66** |
| V-JEPA 2 ViT-L **+ID** | 0.85 | **0.66** | 0.56 |
| VideoMAE V1 ViT-L +ID | 0.75 | 0.11 | 0.55 |
| SDXL VAE +ID | −0.41 | −2.20 | −2.02 |
| Dreamer 4 (either) | −0.04 | −0.04 | −0.04 |

V-JEPA +ID beats VideoMAE +ID at matched clean performance under noise (0.66 vs 0.11) — "consistent with predictive latent objectives being less pixel-tied." Pixel-reconstruction models get *more* negative as perturbation strengthens, "still prioritizing appearance even after action supervision."

### CALVIN masks the effect

The cross-benchmark ranking largely holds (Spearman ρ = +0.88 between LIBERO and Metaworld; V-JEPA+ID tops Metaworld at 0.59 and CALVIN at 0.88). **CALVIN is the exception**: image-only SSL reaches 0.77–0.81 there, because its four fixed tabletop environments let static per-frame appearance substitute for temporal context. A probe-budget control rules out a data-scaling artifact.

A benchmark-design warning in the same family as [LIBERO-PRO](libero-pro-paper.md)'s: **a static-environment benchmark can hide the very property you are trying to measure.**

## Entities mentioned

- [V-JEPA 2](../entities/v-jepa-2.md) · [DINO-WM](../entities/dino-wm.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) (Cosmos-1 tokenizer) · [Dreamer](../entities/dreamer.md) (Dreamer 4 reproduction) · [LIBERO](../entities/libero.md) · [Metaworld](../entities/metaworld.md) · [DINOv2](../entities/dinov2.md)-lineage image SSL (Web-DINO)
- [SigLIP 2](../entities/siglip.md) — image-SSL encoder; 0.17 action R² after ID tuning and **negative** on rotation.

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the shared-probe instrument.
- [JEPA](../concepts/world-models/jepa.md) — the ~0.10 attribution, the rotation finding, the per-layer profile.
- [Latent space](../concepts/world-models/latent-space.md) · [world model](../concepts/world-models/world-model.md) · [VLA models](../concepts/learning/vla-models.md) (the frozen front-end choice).

## Open questions

- **Entirely in simulation**, and the authors say so: LIBERO, CALVIN, Metaworld only. Sim-to-real transfer of the action-recoverability trends is untested.
- **Probe ≠ policy.** The paper measures representation quality via held-out action recovery, not closed-loop success. It states the two are "correlated but not identical" and scopes real-robot evaluation to follow-up. So this does not directly close the loop to WorldArena's system-level numbers — it explains them.
- **The Dreamer 4 result rests on a reproduction**, since no official implementation was public. A −0.04 flatline across a 4× capacity range is a strong claim to rest on a reimplementation.
- **Does the layer-14 peak generalize?** If action signal reliably peaks mid-trunk in JEPA encoders, every downstream VLA using final-layer V-JEPA features is leaving measurable performance on the table. Nobody has tested that on a policy.
