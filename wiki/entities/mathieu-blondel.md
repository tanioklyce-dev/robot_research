---
title: Mathieu Blondel
type: entity
subtype: person
created: 2026-05-25
updated: 2026-05-25
sources: 1
tags: [mathieu-blondel, google-deepmind, fenchel-young-loss, sparsemax, structured-prediction, differentiable-programming, jax, author]
---

**Mathieu Blondel** — research scientist at **[Google DeepMind](google-deepmind.md)**. Best known for the **Fenchel-Young loss** framework (unifies cross-entropy / hinge loss / sparsemax loss as instances of one construction), **sparsemax** (a sparser alternative to softmax for attention + classification), and substantial **JAX** ecosystem contributions (JAXopt, optax). Co-author of **"The Elements of Differentiable Programming"** (Blondel & Roulet, Google DeepMind, draft v3 June 2025).

## What we know in this wiki

- **["The Elements of Differentiable Programming"](../sources/blondel-roulet-differentiable-programming.md)** (Blondel & Roulet, Google DeepMind; draft v3, June 2025) — 485-page reference textbook. Co-authored with Vincent Roulet. Free draft on arXiv. The wiki's most comprehensive single mathematical-foundation reference for autodiff, optimization, transformers, flow matching, REINFORCE, reparametrization trick, Gumbel tricks, Fenchel-Young losses, and the rest of the differentiable-programming substrate.

## Why his research matters in this wiki

- **Sparsemax + softmax + smoothed-max operator family** — directly relevant to the wiki's [VLA models](../concepts/learning/vla-models.md) action-head taxonomy. The wiki tracks three action-head families (autoregressive tokens vs DDPM vs flow matching); each is a different choice on the **same Fenchel-Young loss family** Blondel's research formalizes.
- **JAX ecosystem contributions** — JAXopt + optax are widely used inside the [LeRobot](lerobot.md) and Google DeepMind training stacks.
- **Structured prediction + differentiable inference** — Blondel's research-line themes show up directly in chs. 10–13 of the book (inference as differentiation; differentiating through optimization; smoothing by optimization including sparsemax + softmax).

## Background (per public author pages)

- Previously at NTT (Tokyo) and Google Brain (Tokyo); now Google DeepMind.
- Long-running thread: **smoothing + duality + structured prediction** — sparsemax (Martins & Astudillo 2016, with Blondel as a key downstream contributor), Fenchel-Young losses (Blondel et al., AISTATS 2019), Fast Differentiable Sorting and Ranking (Blondel et al., ICML 2020), and the JAXopt / optax + JAX-structured-prediction tools.

## Related

- [Google DeepMind](google-deepmind.md) — affiliation.
- Vincent Roulet — co-author on the differentiable-programming book (no entity yet; Google DeepMind optimization researcher).
- [VLA models](../concepts/learning/vla-models.md) — Blondel's Fenchel-Young loss framework is the unifying view of VLA action heads.
- [Diffusion Policy](diffusion-policy.md), [π0](pi-zero.md), [SmolVLA](smolvla.md) — flow-matching / DDPM-action-head VLAs all sit inside the Fenchel-Young framework.

## Mentioned in

- [The Elements of Differentiable Programming (Blondel & Roulet, 2025)](../sources/blondel-roulet-differentiable-programming.md) — primary source.

## Open questions

- **Sparsemax + Fenchel-Young loss primary papers** — referenced via the book but not ingested directly. If the wiki ever needs a primary source on the structured-prediction lineage Blondel works in, those would be the obvious next ingests.
- **JAXopt + optax entity** — Blondel's framework contributions; not in the wiki.
- **Author personal page / publication list** — not surfaced in this ingest; should be findable via DeepMind staff page.
