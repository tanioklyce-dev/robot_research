---
title: The Welch Labs Illustrated Guide to AI, Volume I
type: source
local_path: raw/WelchLabs_IllustratedGuideToAI_rev_15_feb_4_1.pdf
sha256: ad49a7c3499d8012ecf6cd49c5a53436fdc0faef048b4763e70e899a8780dc41
url: https://www.welchlabs.com/
companion_code: https://github.com/stephencwelch/ai_book
companion_videos: https://www.youtube.com/@WelchLabsVideo
author: Stephen Welch (Welch Labs LLC)
affiliation: Welch Labs LLC, Winston-Salem, NC
published: 2026-02 (Revision V15; written through November 2025)
pages: 376
license: copyrighted (Welch Labs LLC 2026)
ingested: 2026-05-15
tags: [welch-labs, stephen-welch, pedagogical, textbook, ai, neural-networks, perceptron, gradient-descent, backpropagation, deep-learning, alexnet, scaling-laws, mechanistic-interpretability, attention, deepseek, diffusion, image-generation]
---

> [!note] Pedagogical companion, not a research paper
> This is a 376-page **illustrated textbook** by Stephen Welch (creator of [Welch Labs](../entities/welch-labs.md), the YouTube channel), pairing chapter-by-chapter with the Welch Labs YouTube series. Supporting code at [github.com/stephencwelch/ai_book](https://github.com/stephencwelch/ai_book); each chapter has exercises with solutions in the back. The wiki ingests pedagogical companions at section-summary depth (cf. [Sutton & Barto](sutton-barto-rl-textbook.md)) — this page captures structure, the wiki-relevant content, and which chapters feed which existing wiki threads. Volume I; Volume II teased in a footnote of the preface.

## Summary

Stephen Welch's **Illustrated Guide to AI, Volume I** is a deep-dive textbook covering the **core lineage of modern AI** — perceptron → gradient descent → backprop → deep learning → AlexNet → scaling laws → mechanistic interpretability → attention → diffusion. The thesis of the preface: *"the core ideas that make even the largest, most advanced models work are not that complicated, and have been around for a while."* Welch's stated goal is to help readers "find the bottom" of those core ideas — to understand the math and not the marketing.

The book's pedagogical posture is **depth over breadth** (Welch's words). Each chapter pairs with a Welch Labs YouTube video. The book stands alone or complements the videos; supporting code is in the book itself at the end of each chapter and on GitHub. Wide margins are designed for reader annotation. Exercises with solutions in the back.

Two of Welch's previous YouTube videos are already wiki sources: [Welch Labs Perceptron](welchlabs-perceptron.md) (= the video companion to Chapter 1) and [Welch Labs — Yann LeCun's $1B Bet Against LLMs](welchlabs-lecun-1b-bet-against-llms.md). This book is the **canonical printed reference** that those videos belong to.

## Structure — 9 chapters

Each chapter heading is paired with a tagline Welch uses to introduce it. Page numbers are from the book's TOC.

| Ch | Topic | Welch's tagline | Pages | Wiki anchor |
|---|---|---|---:|---|
| **1** | The Perceptron | "ChatGPT is made from 100 million of these" | 13–39 | [welchlabs-perceptron.md](welchlabs-perceptron.md), [siamese-network.md](../concepts/world-models/siamese-network.md) |
| **2** | Gradient Descent | "The misconception that almost stopped AI" | 42–66 | [Curriculum Module 1](../syntheses/curriculum/curriculum-01-neural-networks.md) |
| **3** | Backpropagation | "The F=ma of artificial intelligence" | 67–83 | [Curriculum Module 1](../syntheses/curriculum/curriculum-01-neural-networks.md) |
| **4** | Deep Learning | "The geometry of depth" | 84–106 | [Curriculum Module 1](../syntheses/curriculum/curriculum-01-neural-networks.md) |
| **5** | AlexNet | "The moment we stopped understanding AI" | 107–146 | [Curriculum Module 2 — CNNs](../syntheses/curriculum/curriculum-02-cnns.md) |
| **6** | Neural Scaling Laws | "AI can't cross this line and we don't know why" | 217–244 | [scaling-laws-vla.md](../concepts/learning/scaling-laws-vla.md) |
| **7** | Mechanistic Interpretability | "The dark matter of AI" | 245–268 | [mechanistic-interpretability.md](../concepts/safety/mechanistic-interpretability.md) (new) |
| **8** | Attention | "How DeepSeek rewrote the transformer" | 269–293 | [Curriculum Module 3 — transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md) |
| **9** | Video and Image Generation (Diffusion) | "AI videos are Brownian motion backwards" | 295–344 | [Curriculum Module 5 — generative](../syntheses/curriculum/curriculum-05-generative-models.md), [DreamDojo](dreamdojo-paper.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md) |

(References and Index at the end; solutions to exercises in the back.)

## Wiki-relevant chapter content

### Ch 1 — The Perceptron
The 1958 Rosenblatt perceptron framed as the atomic unit of modern AI: "ChatGPT is made from 100 million of these." Walks through the perceptron learning rule, geometric intuition for separability, and the limitations that triggered the first AI winter — direct precursor to the [Siamese network](../concepts/world-models/siamese-network.md) lineage already filed in the wiki. Cites the New York Times' July 7, 1958 announcement of Rosenblatt's perceptron — the same announcement quoted on page 5 of the book: *"creator of the perceptron — the precursor to neural networks — when asked what use his algorithm might have."*

### Ch 6 — Neural Scaling Laws
The "AI can't cross this line and we don't know why" framing. Welch identifies **three neural scaling laws** that hold roughly independent of architecture or learning algorithm:
- **Error vs compute**
- **Error vs model size**
- **Error vs dataset size**

Anchored on **Kaplan et al. 2020** — the OpenAI paper that established power-law scaling for language models. Welch quotes the fitted exponents: compute slope ≈ −0.050, parameter-count slope ≈ −0.076, dataset-size slope ≈ −0.09. The book's framing of the "compute-optimal frontier" is the dashed line in Figure 6.1.

This chapter is the **LLM-side companion** to the wiki's robotics-side [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) hub (seeded by [EgoScale](egoscale-paper.md)). The wiki's scaling-laws concept page references "Hoffmann et al. 2022 / Chinchilla" without an ingested primary; Welch Ch 6 is now the wiki's accessible-pedagogy entry point for that material.

### Ch 7 — Mechanistic Interpretability
**"The dark matter of AI."** Welch frames mechanistic interpretability as the discipline of trying to read concepts and behaviors out of trained models — opening with the canonical "ask ChatGPT to forget a phrase" demonstration. Heavily anchored on:
- **Templeton et al. 2024** — sparse autoencoders for feature extraction (Anthropic, the *Scaling Monosemanticity* paper).
- **Chris Olah** — the field's founder; quoted with the "dark matter of interpretability" analogy (Olah, July 2024). Olah's claim that "we've only been able to extract a tiny portion, likely less than 1%, of the concepts" is the chapter's anchor pessimism.
- **Anthropic's Claude** — the demonstration system. Welch shows the "internal conflict feature steering" example: increase the internal-conflict feature's value and Claude admits it can't forget words.

This chapter is the natural anchor for a new [mechanistic-interpretability](../concepts/safety/mechanistic-interpretability.md) concept page, which the wiki has gestured at via the [Anthropic](../entities/anthropic.md) entity and the [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) concept but never hubbed.

### Ch 8 — Attention
**"How DeepSeek rewrote the transformer."** Opens with January 2025's DeepSeek-R1 release and the Jan-2025 industry shockwave. The chapter's signature deep dive is **Multi-Head Latent Attention (MLA)** from DeepSeek-V2 (Liu et al. 2024, Jun 2024) — a modification to standard transformer attention that *"reduces the size of an important bottleneck called the key-value cache by a factor of 57,"* enabling ~6× faster text generation in DeepSeek's implementation. Critical for reasoning models like R1 that need to generate large numbers of [chain-of-thought](../concepts/learning/chain-of-thought.md) tokens.

Pedagogy progression: token-by-token autoregressive generation → why each next token is a function of all prior tokens → standard multi-head attention → KV cache → MLA's compression trick. Welch's framing: MLA "strikes at the core of the transformer itself" — most DeepSeek innovations are at the margins; this one isn't.

### Ch 9 — Video and Image Generation (Diffusion)
**"AI videos are Brownian motion backwards."** Welch's framing of diffusion: *"diffusion is remarkably equivalent to the Brownian motion we see as particles diffuse, but with time run backwards, and in high-dimensional space."* The chapter is pedagogy-first, hands-on with **Wan2.1** as the open-source example model (notable: the same Wan family whose **WAN2.2 tokenizer** is the latent-space substrate for [DreamDojo](dreamdojo-paper.md) and [NVIDIA Cosmos](../entities/nvidia-cosmos.md)).

Walks through the noise → transformer → less-noisy-video → repeat denoising loop, then connects it to the physics of Brownian diffusion. Acknowledgment includes **Jonathan Ho** (the [DDPM](ddpm-paper.md) author) and **Preetum Nakkiran** — heavy hitters in the diffusion-theory community.

This chapter is the pedagogical companion to [Curriculum Module 5 — Generative modeling](../syntheses/curriculum/curriculum-05-generative-models.md) (DDPM math walkthrough) and the wiki's video-WM line ([DreamDojo](dreamdojo-paper.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [Genie Envisioner](../entities/genie-envisioner.md)).

## Author + acknowledgments

**Stephen Welch** — based in Winston-Salem, NC. Founder of [Welch Labs](../entities/welch-labs.md). First made a YouTube series on neural networks in 2014 after teaching himself the math for a startup. The book is the printed culmination of ~12 years of public-pedagogy work, plus a Welch Labs YouTube series in 2025–2026.

Illustrations by **Sam Baskin** and **Pranav Gundu** (plus Welch). Acknowledgments include — among many others — **Grant Sanderson** (3Blue1Brown), **Jonathan Ho** (DDPM), **Preetum Nakkiran**, **Juan Benet**. The pedagogy stack is well-connected.

## Position in the wiki

- **Pedagogical companion #1** for the curriculum's Modules 1–3 (neural networks, CNNs, attention/transformers) and Module 5 (generative/diffusion). Pairs with **Sutton & Barto** (RL theory) and **3Blue1Brown** (MLP geometry) as the wiki's three canonical pedagogy primary-sources.
- **Welch Labs**, until this ingest, was represented in the wiki only as a YouTube channel via two video sources. With this book ingested, Welch Labs becomes a substantial **pedagogy publisher** (videos + book + GitHub code + companion exercises) — promotes the brand to its own entity page.
- **Two new concept hubs** seeded by the book that the wiki previously gestured at without filing:
  - **Mechanistic interpretability** (Ch 7) — anchor concept page covering sparse autoencoders, feature steering, Olah's "1% extracted" framing. Adjacent to [AI safety and alignment](../concepts/safety/ai-safety-alignment.md).
  - **DeepSeek + Multi-Head Latent Attention** — not yet entitied. Ch 8's MLA deep-dive is the wiki's first encounter with DeepSeek's architectural contributions; could seed an `entities/deepseek.md` and a `concepts/multi-head-latent-attention.md` if DeepSeek shows up in more sources.
- **Cross-references to existing video sources**: [Welch Labs Perceptron](welchlabs-perceptron.md) = Ch 1's companion video. [Welch Labs — Yann LeCun's $1B Bet Against LLMs](welchlabs-lecun-1b-bet-against-llms.md) is adjacent (LeCun's JEPA pitch is not covered in Vol I per the TOC — likely belongs in the teased Vol II).

## Entities mentioned

**Already in wiki:**
- [Anthropic](../entities/anthropic.md) — Ch 7 anchored on Claude + Templeton et al. 2024 sparse-autoencoder work.
- [3Blue1Brown / Grant Sanderson](../sources/3blue1brown-mlp-in-llms.md) — acknowledged collaborator.
- [DDPM](../sources/ddpm-paper.md) (Ho et al. 2020) — Jonathan Ho is acknowledged.

**New entities created with this ingest:**
- [Welch Labs](../entities/welch-labs.md) — the pedagogy brand / publisher entity.
- [Stephen Welch](../entities/stephen-welch.md) — author entity.

**Mentioned in the book but not yet entitied** (candidate future entity stubs if these come up in more sources):
- **DeepSeek** — Ch 8 spends ~25 pages on DeepSeek's MLA innovation; R1 is the chapter's narrative anchor.
- **Chris Olah** — Anthropic interpretability lead, quoted in Ch 7.
- **Frank Rosenblatt** — perceptron inventor; Ch 1 anchor.
- **Wan2.1 / WAN model family** — Ch 9's hands-on diffusion example; same family that produces DreamDojo's WAN2.2 tokenizer.

## Concepts touched
- [Neural networks](../syntheses/curriculum/curriculum-01-neural-networks.md) (Curriculum Module 1) — Ch 1–4 perceptron → gradient descent → backprop → depth.
- [CNNs](../syntheses/curriculum/curriculum-02-cnns.md) (Curriculum Module 2) — Ch 5 AlexNet.
- [Attention and transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md) (Curriculum Module 3) — Ch 8 attention + MLA.
- [Generative models](../syntheses/curriculum/curriculum-05-generative-models.md) (Curriculum Module 5) — Ch 9 diffusion.
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — Ch 6 covers the LLM-side scaling laws (Kaplan 2020); the wiki's robotics-VLA scaling-law page now has a pedagogical companion.
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) — Ch 7 is the seed for the new concept page.
- [Chain of thought](../concepts/learning/chain-of-thought.md) — Ch 8 motivates MLA partly by R1's reasoning-token-volume demands.
- [Siamese network](../concepts/world-models/siamese-network.md) — Ch 1 perceptron is the architectural ancestor.

## Open questions / candidate follow-ups

- **Volume II** is teased in the preface footnote (*"And hey, there's always volume 2, right?"*). Likely covers LeCun's JEPA / world-model material that Welch already addressed in his "LeCun's $1B bet against LLMs" video.
- **Templeton et al. 2024 — Scaling Monosemanticity** (Anthropic). The primary mechanistic-interpretability paper Ch 7 anchors on. Candidate primary-source ingest if the wiki picks up the interpretability thread.
- **Kaplan et al. 2020 — Scaling Laws for Neural Language Models** (OpenAI). The primary scaling-law paper Ch 6 anchors on. Candidate primary-source ingest for the [scaling-laws-vla](../concepts/learning/scaling-laws-vla.md) hub.
- **Liu et al. 2024 — DeepSeek-V2 (Multi-Head Latent Attention)**. Ch 8's deep-dive subject. Candidate primary-source ingest; would also seed an `entities/deepseek.md` page.
- **Olah, July 2024 — "Dark Matter of Interpretability"**. Welch quotes this from Olah's writing/talks. Likely a Transformer Circuits Thread post or similar.
- **Hoffmann et al. 2022 — Chinchilla** (DeepMind). The compute-optimal scaling law that Ch 6 may reference; currently flagged as a candidate ingest on the [scaling-laws-vla](../concepts/learning/scaling-laws-vla.md) page.
- **Are there robotics chapters in Vol II?** Vol I is entirely LLM/vision-focused. The wiki's robotics core is not directly served by this book — but the foundational chapters (1–4) are universally relevant.

## Why this is a useful ingest for this wiki

1. **Closes the canonical-pedagogy trifecta**: the wiki now has Sutton & Barto (RL theory), 3Blue1Brown (MLP geometry / visual intuition), and Welch Labs (the full neural-net-to-attention-to-diffusion sweep) as its three durable pedagogical primary sources. Future "what should I read?" queries can route to a clean answer.
2. **Provides an accessible LLM-scaling-law primary source.** The wiki's robotics-VLA scaling-law concept page references Kaplan / Chinchilla without ingested primaries; Welch Ch 6 is the accessible pedagogy-grade entry point.
3. **Seeds the mechanistic-interpretability concept hub.** Ch 7's Anthropic / Olah / sparse-autoencoder framing is the wiki's first proper engagement with this discipline. Adjacent to existing [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) coverage.
4. **Brings DeepSeek's MLA into the wiki's attention/transformer lineage.** The wiki's curriculum Module 3 covers standard MHA but not the 2024–2025 architectural innovations (MLA, GQA, grouped-query attention). Ch 8 is the entry point if the wiki extends here.
5. **Promotes [Welch Labs](../entities/welch-labs.md) to an entity.** With 3 sources (perceptron video, LeCun-bet video, illustrated guide book), Welch Labs is now substantial enough to warrant its own entity page.
