---
title: "3Blue1Brown — How might LLMs store facts | Deep Learning Chapter 7 (Aug 2024)"
type: source
url: https://www.3blue1brown.com/lessons/mlp
author: Grant Sanderson (3Blue1Brown); text adaptation by Justin Sun
affiliation: 3Blue1Brown (independent educational-video channel)
published: 2024-08-31
ingested: 2026-05-14
tags: [mlp, ffn, transformer, llm, gpt-3, superposition, johnson-lindenstrauss, interpretability, video, pedagogical, 3blue1brown, curriculum-module-1, curriculum-module-3]
---

> [!note] Ingest depth
> Source-page metadata gathered from the 3Blue1Brown lesson page itself (web-text adaptation of the video, with embedded clips + interactive questions). The lesson is part of 3Blue1Brown's *Deep Learning* video series. This ingest is **summary-level**, referencing the page's key claims and pedagogical structure rather than reproducing the diagrams.

## Summary

**"How might LLMs store facts | Deep Learning Chapter 7"** — Grant Sanderson (3Blue1Brown), with text adaptation by Justin Sun. Published **2024-08-31**. Chapter 7 of 3Blue1Brown's *Deep Learning* video series, specifically the **MLP / feed-forward block** inside a transformer LLM and the hypothesis that those MLPs are where **factual knowledge** is stored (e.g., "Michael Jordan plays basketball").

The lesson covers:

- **Transformer FFN block architecture** — two linear projections (up-projection to a wider dimension `4 × d_model`, then down-projection back to `d_model`) with a **ReLU** activation in between. The standard `MLP(x) = W_down · ReLU(W_up · x + b_up) + b_down` pattern.
- **Forward pass mechanics** — input vector is up-projected, gated by ReLU, then down-projected back. In a 175B-parameter GPT-3, the MLP blocks hold **~2/3 of all parameters**.
- **Feature representation via directions** — directions in the high-dimensional embedding space encode semantic features; individual neurons in the up-projected hidden layer fire when specific features are present.
- **Superposition** — the **Johnson–Lindenstrauss lemma**: in an `n`-dimensional space you can fit *exponentially many* nearly-orthogonal directions, not just `n` strictly orthogonal ones. This is the geometric basis for the observation that real neurons in trained LLMs are not "one feature per neuron" — features are encoded in low-cosine-similarity directions that pack densely.
- **Why individual neurons are hard to interpret** — combining ReLU + superposition, the natural unit of "what does this neuron mean" is *not* the neuron but a *direction* in feature space. This is the foundation of the modern mechanistic-interpretability program (Anthropic's SAE work, the "Toy Models of Superposition" lineage).

## Why it matters to this wiki

- **Direct pedagogical fit for [Curriculum Module 3 — Sequence models, attention, and transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md).** Module 3 covers the transformer block at the architectural level (LN → MSA → residual → LN → MLP → residual) but does not unpack the MLP's role in detail; this lesson is the natural exit-ramp video for "what is the MLP block actually *doing* inside a transformer?"
- **Bridges Module 1 and Module 3.** Module 1 builds the MLP from scratch (perceptron → MLP → backprop), Module 3 uses MLP as one of two sublayers inside a transformer block. This lesson is the conceptual bridge: "the MLP block in a transformer is a *stack of perceptrons doing fact lookup*."
- **Companion to [Welch Labs — Perceptron](welchlabs-perceptron.md).** Welch Labs covers MLPs at the *scale-up* level ("100M perceptrons make a ChatGPT"); 3Blue1Brown covers MLPs at the *mechanistic* level ("here's what the perceptron stack is actually computing inside GPT-3"). The two videos together give Module 1+3 readers complementary intuition.
- **Foundation for interpretability literature** — superposition + Johnson–Lindenstrauss are the conceptual basis for sparse-autoencoder feature decomposition (Anthropic, Bricken et al. 2023), which is increasingly relevant to AI-safety / alignment work the wiki tracks (see [Claude's Constitution](claudes-constitution.md), [AI safety and alignment](../concepts/safety/ai-safety-alignment.md)).

## Key claims (transcribed from the lesson page)

- **MLP architecture inside transformer:** `MLP(x) = W_down · ReLU(W_up · x + b_up) + b_down`, with `W_up: d × 4d`, `W_down: 4d × d`. The 4× hidden width is the standard transformer ratio.
- **Forward pass interpretation:** Each row of `W_up` represents a direction in embedding space; the ReLU thresholds out rows whose dot product with the input is negative; `W_down` then composes the surviving signals back into the residual stream.
- **GPT-3 parameter accounting:** ~2/3 of GPT-3's 175B parameters live in MLP blocks (the rest in attention's Q/K/V/O matrices + embedding/unembedding). The arithmetic: each transformer layer has 4·d² (MLP up) + 4·d² (MLP down) + 4·d² (attention Q+K+V+O) = 12·d² parameters, of which 8·d² (2/3) is MLP.
- **Fact-storage hypothesis:** The MLP block functions as a *key–value lookup table* in the residual stream. The up-projection rows are keys; activation patterns identify which keys are present; the down-projection rows are values that get written back to the residual stream.
- **Superposition (Johnson–Lindenstrauss):** In dimension `n`, you can pack exponentially many vectors that are all within `(1 ± ε)` of orthogonal — so a `d`-dimensional MLP hidden layer can encode far more than `d` features, at the cost of interference between features (which the model learns to manage).
- **Implication for interpretability:** Individual neurons in a trained LLM rarely correspond to single clean features. The natural unit is *directions*, not neurons. This is the foundation of the sparse-autoencoder (SAE) interpretability program.

## Entities mentioned

- **[Grant Sanderson / 3Blue1Brown](https://www.3blue1brown.com)** — the channel; not yet a wiki entity page. Sanderson's *Essence of Linear Algebra*, *Essence of Calculus*, and *Deep Learning* series are widely-recommended math/ML primers; a one-line entity stub could absorb future references.
- **GPT-3 (OpenAI, 2020)** — referenced for parameter accounting. Not yet a wiki entity.
- **Anthropic / mechanistic interpretability community** — implicit in the superposition framing; the Bricken et al. 2023 "Toy Models of Superposition" paper and the SAE feature-decomposition line are the natural follow-ups.

## Concepts touched

- **Multilayer perceptron (MLP)** — the FFN block inside every transformer. Not yet a wiki concept page; candidate stub.
- **Superposition / Johnson–Lindenstrauss** — the geometric phenomenon underlying high-dimensional feature packing. Foundational for interpretability.
- **Key–value lookup as MLP interpretation** — the framing that "MLP rows are keys + values." Related to the **Geva et al. 2021** "Transformer Feed-Forward Layers Are Key-Value Memories" paper (not in the wiki; candidate ingest).
- **Mechanistic interpretability** — the broader research program; the wiki touches it via [Claude's Constitution](claudes-constitution.md) and the [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) concept page but does not yet have a dedicated entry point.

## Curriculum hookup

Recommended-viewing pointer for **two** curriculum modules:

- **[Curriculum Module 1 — Neural networks and training](../syntheses/curriculum/curriculum-01-neural-networks.md)** — at the "MLP as universal approximator" section. Pairs with [Welch Labs — Perceptron](welchlabs-perceptron.md) as the popular-video reading list.
- **[Curriculum Module 3 — Sequence models, attention, and transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)** — at the "transformer block: MSA + MLP" section. Strongest exit-ramp video for "what the MLP block does inside a transformer."

Note: the URL `/lessons/mlp` is somewhat misleading — the lesson is specifically about MLPs *inside transformers* and fact storage, not a general MLP primer. The 3Blue1Brown *Deep Learning* series has Chapter 1 (vanilla NN intro) and Chapter 4 (backpropagation) for those purposes.

## Position in the 3Blue1Brown Deep Learning series

```
Ch 1: Vanilla NN intro (image classification, MLP basics)
Ch 2: Gradient descent
Ch 3: Backpropagation
Ch 4: Backpropagation calculus
Ch 5: How transformers work (attention block)
Ch 6: How attention works in detail (Q, K, V, dot product)
Ch 7: How might LLMs store facts (THIS LESSON — MLP block inside transformer)
Ch 8: How large language models work (overview)
```

The full 3Blue1Brown Deep Learning series is a strong **popular companion** to the curriculum's Tier 1–2 modules. This page tracks only Ch 7 (the lesson the user submitted); the other chapters are equally pertinent and could be ingested as a single "3Blue1Brown Deep Learning series" source page if the wiki picks up more 3B1B references.

## Open questions / TBD

- **The Geva et al. 2021 "Feed-Forward Layers Are Key-Value Memories" paper** — the academic source for the fact-storage interpretation 3B1B builds on. Candidate ingest if the wiki picks up an interpretability thread.
- **Bricken et al. 2023 — "Toy Models of Superposition"** (Anthropic) — the canonical superposition / SAE paper. Candidate ingest for the AI-safety thread.
- **A `concepts/mlp.md` page** — would unify Module 1 (perceptron stack), Module 3 (FFN inside transformer), and this lesson's fact-storage framing. Defer until a third MLP-focused source surfaces.
- **The other 3B1B Deep Learning chapters (Ch 1, 3, 5, 6, 8)** — strong candidates for a combined "3Blue1Brown — Deep Learning series" ingest page rather than per-chapter pages, if the wiki wants more 3B1B coverage.
- **An entity stub for 3Blue1Brown / Grant Sanderson** — would let future ingests attach cleanly without re-introducing the channel each time.
