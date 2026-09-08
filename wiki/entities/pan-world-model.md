---
title: PAN (Physical, Agentic, Nested) world model
type: entity
subtype: model
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [world-model, glp, generative-latent-prediction, llm-backbone, diffusion, discrete-tokens, mbzuai, previewed]
---

**PAN** — *Physical, Agentic, and Nested* world model from [MBZUAI](mbzuai.md) / CMU ([Xing](eric-xing.md), Deng, Hou, and the Xiang et al. team), the named instantiation of the [Generative Latent Prediction](../concepts/world-models/generative-latent-prediction.md) architecture. **This wiki has only the preview** in [Critique of World Model](../sources/critique-of-world-model-paper.md) §5; the results paper is arXiv 2511.09057 (Nov 2025), un-ingested. Treat every line below as a *design statement*, not a measured property.

## Architecture as previewed

- **Sensory encoder h** — two pathways: a **tokenizer** mapping raw signals into a hierarchical, extensible vocabulary (VQ-VAE-style abstract tokens plus natural-language words), and an **embedder** producing continuous latents for low-level detail. The token path is *"stateful by construction."*
- **World-model backbone f** — an **enhanced LLM** (reasons over language tokens and the learned conceptual vocabulary) plus a **diffusion-based next-embedding predictor** for fast, sub-verbal perceptual dynamics; a **Learned Switch** picks the pathway per step. Factorised as hierarchical state inference × switch-based next-state prediction.
- **Multimodal decoder g** — reconstructs the next observation across *all* sensory channels (the essay lists sound, temperature, motion, pain, text) for generative supervision and for external consumers.
- **Training** — pretrain modules separately by self-supervision (LLM on text, diffusion on video), then align/integrate with multimodal data; discrete components may use RL-style gradient-free updates.
- **Agent** — a *PAN-agent* consults a **cache of precomputed simulations** at decision time rather than re-planning (the essay's alternative to both reactive RL policies and per-step MPC).

## Motivating use case

A multi-day **mountaineering expedition**: gear selection and route planning at the top, foot placement and rope handling at the bottom, teammate coordination in between. The essay's data-efficiency claim rests on this stratification — *"travel book for trail guide and map reading, indoor video for rock climbing and gear usage."*

## What the wiki cannot yet say

No numbers, no benchmark, no ablation. The essay itself says the details *"will be provided in a separate dedicated manuscript."* The open question for this wiki is whether PAN reports the one thing that would test the GLP thesis: a decision-relevant error a latent-trained world model misses and a generative one catches.

## Related

- [Generative Latent Prediction](../concepts/world-models/generative-latent-prediction.md) — the architecture class.
- [JEPA](../concepts/world-models/jepa.md) — the architecture PAN is positioned against.
- [NVIDIA Cosmos](nvidia-cosmos.md), [Genie 3](genie-3.md) — the generative-video systems the essay says PAN inherits *validation* from.

## Mentioned in

- [Critique of World Model](../sources/critique-of-world-model-paper.md) — §5 preview.
