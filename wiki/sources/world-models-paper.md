---
title: "World Models (Ha & Schmidhuber, 2018)"
type: source
url: https://arxiv.org/abs/1803.10122
author: David Ha, Jürgen Schmidhuber
published: 2018-03-27 (arXiv; interactive version at worldmodels.github.io)
ingested: 2026-07-09
venue: NeurIPS 2018
local_path: raw/worldmodels_1803.10122v4.pdf
sha256: b0c1e30aab53efd28ddf61d661f680150918d4d03b77bae62bc52d62dbd76cce
format: paper PDF (21 pp)
tags: [world-model, mbrl, vae, mdn-rnn, learning-in-dream, evolution-strategies, foundational]
---

# World Models (Ha & Schmidhuber, 2018)

## Summary

**The founding paper of the modern world-model genre** — the "Ha & Schmidhuber 2018" the wiki has been citing by name without a source page. Architecture **V-M-C**: a **[VAE](../concepts/learning/variational-autoencoder.md)** (V, 4.3M params) compresses frames to latent `z`; an **MDN-RNN** (M, 422K) models `P(z_{t+1} | a_t, z_t, h_t)` as a mixture of Gaussians; and a deliberately tiny linear **controller** (C, 867 params) acts on `[z_t, h_t]`, trained with **CMA-ES** (evolution, not gradients). Two headline results: **solving CarRacing-v0** (first agent to reach the 900-average threshold, from pixels), and — the idea that named the genre — **training the policy entirely inside the model's own "hallucinated dream"** of VizDoom, with a temperature parameter τ to control dream stochasticity and prevent policy exploitation of model errors, then transferring back to the real environment.

## Key claims

- Separation of concerns: big unsupervised world model + tiny reward-trained controller — "train large model to learn the world, small controller to act in it."
- **Learning inside the dream** (VizDoom Take Cover): the policy never sees the real environment during training; τ (mixture temperature) trades dream difficulty against exploitability — the first practical treatment of the model-exploitation problem that all later MBRL (Dreamer's imagination, [DIAMOND](diamond-paper.md)) inherits.
- CarRacing-v0 solved (>900 avg over 100 trials) from pixels; the V-only ablation shows the RNN's temporal compression is what buys performance.
- Explicitly framed via cognitive science (mental models, Forrester) — the framing every later world-model paper repeats.

## Entities mentioned

- [Dreamer](../entities/dreamer.md) — direct descendant ([PlaNet](planet-paper.md) → Dreamer line replaces V-M-C with jointly-trained RSSM + actor-critic in imagination).
- David Ha, Jürgen Schmidhuber — no entity pages (Ha recurs across the wiki's generative line; candidate person page).

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — **the origin source**.
- [Variational autoencoder](../concepts/learning/variational-autoencoder.md) — the V model; a canonical VAE application.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — the dream-training idea is this concept's seed.
- [Latent space](../concepts/world-models/latent-space.md) — policy operates on `[z, h]`, not pixels.

## Open questions

- None substantive — historical anchor ingest. (David Ha person page if the generative line keeps growing.)
