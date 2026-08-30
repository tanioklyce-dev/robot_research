---
title: "Not All Language Model Features Are One-Dimensionally Linear (Engels, Michaud, Liao, Gurnee, Tegmark, ICLR 2025)"
type: source
url: https://arxiv.org/abs/2405.14860
local_path: raw/2405.14860v3.pdf
sha256: 7deac9292ce973801611fee3f07478731f982088b52ae70a55e5f5e146476cb6
author: Joshua Engels, Eric J. Michaud, Isaac Liao, Wes Gurnee, Max Tegmark
affiliation: MIT; MIT & IAIFI (Michaud, Tegmark)
venue: "ICLR 2025; arXiv 2405.14860 (v1 2024-05-23)"
published: 2024-05-23 (v1); ICLR 2025
ingested: 2026-08-30
tags: [mechanistic-interpretability, linear-representation-hypothesis, neural-geometry, multi-dimensional-features, sparse-autoencoders, circular-features, mit, tegmark, iclr-2025]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2405.14860v3.pdf`, 32 pages incl. appendices). Sections 1–6 read in full; appendices (formal proofs, additional intervention plots, attention-head patching) skimmed. Ingested specifically to provide an **independent** check on [Goodfire](../entities/goodfire.md)'s neural-geometry claims.

## Summary

**"Not All Language Model Features Are One-Dimensionally Linear"** — Engels, Michaud, Liao, Gurnee & Tegmark (MIT / IAIFI; ICLR 2025, arXiv May 2024). **The independent, peer-reviewed challenge to the linear representation hypothesis**, and the reason the wiki should treat curved and multi-dimensional feature geometry as a real finding rather than one vendor's product category.

The **linear representation hypothesis (LRH)** as they state it has two parts: (1) all representations in pretrained LLMs lie along one-dimensional lines, and (2) model states are a sparse sum of those representations. **This paper attacks part (1).**

Its contributions, in order:

1. A **rigorous definition of an irreducible multi-dimensional feature** — one that cannot be decomposed into either *independent* or *non-co-occurring* lower-dimensional features. This is what makes the claim falsifiable rather than an appeal to pictures.
2. A **scalable automatic search** for such features, built on sparse autoencoders — clustering SAE dictionary elements and testing each cluster against the irreducibility measures.
3. **Circular representations of days of the week, months of the year, and years of the 20th century**, found automatically in GPT-2-small (layer 7) and Mistral 7B.
4. **Causal evidence**: intervention experiments on Mistral 7B and Llama 3 8B showing the models *use* those circles to solve modular-arithmetic-in-disguise tasks.

**Why it matters to this wiki.** The [mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) page describes SAEs and directional feature steering as the field's state of the art. This paper establishes — independently of any commercial interest, 18 months before [Goodfire's](../entities/goodfire.md) neural-geometry posts, at ICLR — that **some concepts are not directions**, and that treating them as directions loses the computation. See [neural geometry](../concepts/safety/neural-geometry.md).

## Abstract (verbatim)

> "Recent work has proposed that language models perform computation by manipulating one-dimensional representations of concepts ('features') in activation space. In contrast, we explore whether some language model representations may be inherently multi-dimensional. We begin by developing a rigorous definition of irreducible multi-dimensional features based on whether they can be decomposed into either independent or non-co-occurring lower-dimensional features. Motivated by these definitions, we design a scalable method that uses sparse autoencoders to automatically find multi-dimensional features in GPT-2 and Mistral 7B. These auto-discovered features include strikingly interpretable examples, e.g. circular features representing days of the week and months of the year. We identify tasks where these exact circles are used to solve computational problems involving modular arithmetic in days of the week and months of the year. Next, we provide evidence that these circular features are indeed the fundamental unit of computation in these tasks with intervention experiments on Mistral 7B and Llama 3 8B, and we examine the continuity of the days of the week feature in Mistral 7B. Overall, our work argues that understanding multi-dimensional features is necessary to mechanistically decompose some model behaviors."

## The two research lines it joins

The framing in §1 is worth keeping because it explains why this took until 2024:

- **Toy-model work** had already found multi-dimensional structure — lattices (Michaud et al.), **circles in modular arithmetic** (Liu et al. 2022; Nanda et al. 2023) — and reverse-engineered the algorithms operating on them.
- **Large-model work** had found *one-dimensional* representations of high-level concepts (Gurnee & Tegmark; Marks & Tegmark; Bricken et al.), which is where the LRH came from.

"For the most part, these two directions have been disconnected." Bricken et al. *speculated* about feature manifolds; Yedidia and Gould et al. found "intriguing hints" of circular representations. This paper is the bridge: it takes the toy-model geometry seriously at frontier scale and finds it.

## The method (§4)

The move that makes it work: **use SAEs to find the thing SAEs are accused of missing.** Rather than assuming features are dictionary elements, they **cluster** SAE dictionary elements and ask whether a cluster is irreducible, by two relaxed statistical measures — an **ε-mixture index** (can the cluster be split into non-co-occurring parts?) and a **separability index** (can it be split into independent parts?).

The circular day/month/year clusters of Figure 1 rank **9th, 28th and 15th of 1000 clusters** by the product of those two measures — i.e. the automatic test surfaces them near the top without being told what to look for. That is the paper's methodological claim: the tests find interpretable irreducible features, not just any features.

## The causal experiments (§5) — the part that matters

Two prompts:

- **Weekdays**: *"Let's do some day of the week math. Two days from Monday is"* — 7 days × 7 durations = **49 prompts**.
- **Months**: *"Let's do some calendar math. Four months from January is"* — 12 × 12 = **144 prompts**.

| Model | Weekdays | Months |
|---|---|---|
| Llama 3 8B | 29 / 49 | **143 / 144** |
| Mistral 7B | 31 / 49 | 125 / 144 |
| GPT-2 | 8 / 49 | 10 / 144 |

> [!note] A detail worth its own line
> Both large models get **trivial accuracy on plain modular arithmetic** — "5 + 3 (mod 7) ≡" — while solving the *semantically dressed* version of exactly the same problem. And GPT-2 **has** the circular representations and still cannot use them. Representation and competence come apart in both directions: possessing the right geometry is not sufficient, and failing the abstract task does not mean the model lacks the structure.

**The intervention result.** Patching only the **2-D circular subspace** has "almost the same intervention effect as patching the entire layer" in early layers, and usually beats patching the top PCA dimensions. Interventions fall off at layers 15–17, which appendix patching explains: that is where `α` gets copied to the final token.

They also run **off-distribution interventions** — sweeping a grid of `(r, θ)` positions *inside* the circle rather than on its circumference, `r ∈ [0, 0.1, …, 2]`, `θ` over 100 steps — and read off the resulting top logit. This is the experiment that distinguishes "the circle is a real coordinate system the model reads" from "the circle is a projection artifact."

## Limitations (their own, §6)

Unusually candid, and worth quoting because they bound the claim:

> "It is unclear why we did not find more interpretable multi-dimensional features. We are unsure if we are failing to interpret some of the high-scoring multi-dimensional features, if most multi-dimensional features lie in dimensions higher than two, if our clustering technique is not powerful enough to find some features, or if there are truly not that many."

And: the irreducibility definitions are **purely statistical, not intervention-based**, and had to be relaxed to hold in practice, "resulting in measures that return a possibly subjective 'degree' of reducibility."

So the honest summary is: **multi-dimensional features exist and are causally load-bearing where found; how common they are is unknown.** This does *not* establish that the LRH is generally false — it establishes that it is not universally true, which is enough to matter.

## Relation to Goodfire's neural-geometry line

Goodfire's *The World Inside Neural Networks* (May 2026) makes the stronger and more general claim — that concepts commonly live on **curved manifolds**, demonstrated across language, vision, genomics and an image-action RL model, with manifold-following steering beating linear steering. This paper is the **narrower, earlier, independently peer-reviewed** version: specific circular features, specific tasks, causal interventions.

> [!note] Provenance, because the wiki flagged this
> An earlier version of the [Goodfire research index](goodfire-research-index.md) page cautioned that the manifold critique was "one lab's largely self-published line" with a commercial interest. **That caution was too strong and has been corrected.** The critique predates Goodfire's posts by 18 months, comes from MIT, and was published at ICLR 2025.
>
> Note also that **Eric J. Michaud is a co-author here**, and his later *Understanding Sparse Autoencoder Scaling in the Presence of Feature Manifolds* appears in Goodfire's corpus as a link post — so the two lines are connected, not independent replications of each other. The correct reading: an academic finding that Goodfire has built a product category around, which is a normal and unremarkable trajectory.

## Entities mentioned

- **Max Tegmark**, **Wes Gurnee**, **Eric J. Michaud**, Joshua Engels, Isaac Liao — MIT / IAIFI. No wiki pages.
- Models: **GPT-2**, **Mistral 7B**, **Llama 3 8B**.
- Anthropic (Bricken et al., the SAE and feature-manifold speculation) — see [Anthropic](../entities/anthropic.md).

## Concepts touched

- **[Neural geometry](../concepts/safety/neural-geometry.md)** — this is its founding independent source.
- **[Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md)** — the linear-features framing it qualifies.
- **[SAE](../glossary.md#sae)** — used as the *search tool* for non-linear structure, which is the neat part.
- **[Distributed representations](../concepts/learning/distributed-representations.md)** — the learned-geometry question, one level up.

## Open questions / TBD

- **No robotics analogue exists.** Every result here is language. Whether a robot policy's latent encodes a continuous physical quantity — object x-position, gripper aperture — as a *smooth manifold* or a set of per-demonstration clusters is untested anywhere in this wiki, and is the sharpest available operationalization of "did the policy generalize or memorize." See [the proposed experiment](../syntheses/projects/latent-inspection-policy-collapse.md).
- **How common are multi-dimensional features?** Explicitly unresolved by the authors.
- **Michaud et al. 2025** (SAE scaling in the presence of feature manifolds) is the follow-up and is un-ingested.
