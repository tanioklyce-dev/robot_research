---
title: "Welch Labs — ChatGPT is made from 100 million of these [The Perceptron] (YouTube, Feb 2025)"
type: source
url: https://www.youtube.com/watch?v=l-9ALe3U-Fg
author: Welch Labs (Stephen Welch)
affiliation: Welch Labs (independent educational-video channel)
published: 2025-02 — submitted to Hacker News 2025-02-12; covered by Frank's World of Data Science 2025-02-03
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
tags: [perceptron, welch-labs, video, pedagogical, rosenblatt, mark-i, history, mlp, llm, gpt-3, curriculum-module-1]
---

> [!note] Ingest depth
> Source-page metadata gathered from the YouTube URL, Frank's World 2025-02-03 coverage, FlowingData 2025-02-25 writeup, and the Hacker News 43023227 thread (posted 2025-02-12). YouTube WebFetch returns only the footer — duration / chapter timestamps not captured here. Ingest is **summary-level**, not a verbatim transcript; the video itself is the canonical source.

## Summary

**"ChatGPT is made from 100 million of these [The Perceptron]"** — Welch Labs / Stephen Welch (YouTube, posted February 2025). A pedagogical explainer that walks from **Frank Rosenblatt's 1957 perceptron** and the **Mark I Perceptron** (1958, 20×20 photocell input grid, hardware learning machine at Cornell Aeronautical Laboratory) through the **XOR / non-linear-separability** roadblock of Minsky & Papert 1969, to the **multilayer perceptron + backpropagation** that revived the field in the 1980s, and finally to the **~100M-perceptron-equivalent scale** at which models like GPT-3 emerge. The video frames the entire 70-year arc of feedforward neural networks as "the perceptron, repeated and scaled."

The video sits as the **pedagogical prequel** to [Welch Labs — Yann LeCun's $1B Bet Against LLMs](welchlabs-lecun-1b-bet-against-llms.md) (May 2026), which the wiki already tracks. The two together form a Welch-Labs two-part introduction: perceptron → MLP → LLM → "*why is LLM so blurry and how does JEPA propose to fix it?*"

## Why it matters to this wiki

- **Direct pedagogical fit for [Curriculum Module 1 — Neural networks and training](../syntheses/curriculum-01-neural-networks.md).** Module 1's prereq diagnostic ("write the gradient of MSE w.r.t. a single-layer MLP from memory") is the formal version of the intuition this video builds. Recommended as a 20–30 min orientation video for readers who want history-and-intuition before the math.
- **Closes the historical lineage** before Bromley/LeCun 1993 ([Siamese network](bromley1993-siamese-signature-verification.md)), Barlow Twins ([2021](barlow-twins-paper.md)), VICReg ([2022](vicreg-paper.md)), DINOv3 ([2025](dinov3-paper.md)), LeWM ([2026](leworldmodel-paper.md)) — every architecture in this wiki ultimately reduces to "a stack of perceptron-like units."
- **Pairs with [Welch Labs — Yann LeCun's $1B Bet Against LLMs](welchlabs-lecun-1b-bet-against-llms.md)** as a Welch-Labs sequence: this video sets up "why MLPs at scale," the LeCun video argues "but MLPs at scale aren't enough, you need JEPA."
- **This video is the companion to Chapter 1 of [The Welch Labs Illustrated Guide to AI, Vol I](welchlabs-illustrated-guide-to-ai.md)** ([Stephen Welch](../entities/stephen-welch.md), [Welch Labs](../entities/welch-labs.md), Feb 2026, 376 pp) — the printed deep-dive version of the perceptron material, with code + exercises.

## Key claims (per the linked coverage and FlowingData summary)

- **Perceptron = single linear classifier with a step / threshold activation.** Learns weights via the LMS-style perceptron learning rule (Rosenblatt 1957). Implementable as a hardware machine — Mark I (1958).
- **XOR / non-linear separability roadblock (Minsky & Papert 1969).** A single-layer perceptron cannot represent the XOR function — a result that contributed to the "first AI winter." The video frames this as the central conceptual obstacle of the 1960s–1970s.
- **Resolution via multilayer perceptrons + backpropagation.** A *stack* of perceptrons with non-linearities between layers can represent XOR (and any continuous function — universal approximation). Backpropagation (Rumelhart, Hinton, Williams 1986) makes training such stacks tractable.
- **Modern LLMs as scaled-up perceptron stacks.** GPT-3 has ~175B parameters; the MLP / feed-forward blocks inside its transformer layers are conceptually "perceptron stacks." Welch Labs' framing: **"~100 million perceptron-like units"** linked together is the order-of-magnitude argument for ChatGPT's scale. (The exact count depends on how you count "a perceptron" — see Open questions.)

## Entities mentioned

- **Frank Rosenblatt** (1928–1971) — psychologist at Cornell Aeronautical Laboratory; invented the perceptron learning rule (1957) and the Mark I Perceptron hardware (1958). Not yet a wiki entity page.
- **Mark I Perceptron** — 20×20 photocell input grid, hardware-implemented learning machine; the first AI hardware system to learn from examples. Not yet a wiki entity page; candidate stub if the wiki picks up a "history of neural networks" thread.
- **Minsky & Papert** — *Perceptrons* (MIT Press 1969), the book that proved the XOR limitation and contributed to the first AI winter.
- **Rumelhart, Hinton, Williams** — backpropagation (1986). Already implicit in [LeCun's lineage](lecun2022-path-towards-ami.md) — LeCun was a graduate student in this scene.
- **[Welch Labs / Stephen Welch](welchlabs-lecun-1b-bet-against-llms.md)** — already documented in the wiki as the author of the LeCun-bet video; this is the prequel.

## Concepts touched

- **[Perceptron](https://en.wikipedia.org/wiki/Perceptron)** — the canonical single-layer linear classifier with threshold activation. Not yet a wiki concept page; would be a useful Module-1-adjacent stub.
- **Multilayer perceptron (MLP)** — stack of perceptrons with non-linearities. The FFN inside every transformer block is an MLP. See also [3Blue1Brown — MLP in LLMs](3blue1brown-mlp-in-llms.md) for the modern-LLM-internals perspective on MLPs as fact-storage.
- **XOR / non-linear separability** — the central pedagogical obstacle the video resolves.
- **Universal approximation theorem** — the theoretical justification for "MLPs can represent anything." Implicit in the video's framing.
- **Backpropagation** — the training algorithm that made MLPs practical.

## Curriculum hookup

This is a strong **recommended-viewing** entry for the top of [Curriculum Module 1 — Neural networks and training](../syntheses/curriculum-01-neural-networks.md). Module 1's existing recommended-reading list points at primary-source / textbook material; this video is the popular-explainer companion for readers who want history and intuition first. Suggested placement: under the existing `> [!note] Video overview — recommended before starting` callout pattern used in [Robot-learning curriculum](../syntheses/robot-learning-curriculum.md) (which already has a Welch-Labs video callout pointing at the LeCun video).

## Position in the lineage

```
1957  Rosenblatt — perceptron learning rule
1958  Mark I Perceptron (hardware, Cornell Aeronautical Lab)
1969  Minsky & Papert — Perceptrons (XOR roadblock; first AI winter)
1986  Rumelhart, Hinton, Williams — backpropagation
1989  LeCun — CNN on MNIST (perceptrons applied to vision)
1993  Bromley, Guyon, LeCun — Siamese networks (joint-embedding architecture; see source page)
...
2017  Vaswani et al. — Transformer (MLPs + self-attention)
2020  Dosovitskiy et al. — ViT (transformer on image patches)
2020  GPT-3 — 175B params; ~ "100M perceptron-equivalent units"
2025  this video — pedagogical retrospective
2026  LeCun — "the path forward is JEPA, not scaled MLPs" (Welch Labs follow-up)
```

## Open questions / TBD

- **The "100 million perceptrons" count.** The video's framing is rhetorical — depending on how you count, GPT-3 has ~12B "neurons" / "perceptron-like units" or ~175B parameters. The number 100M is closer to GPT-2's parameter count (~117M small variant). Worth re-verifying against the actual video transcript.
- **Whether to break out a `concepts/perceptron.md` page.** Currently the wiki's MLP-class concepts are implicit in Module 1 + glossary entries. A standalone perceptron concept page would hub from this video + the 3Blue1Brown lesson + Module 1.
- **Mark I Perceptron entity stub.** The Mark I is sometimes cited as the *first* hardware AI system; a one-paragraph entity stub would make future "history of robotics + AI hardware" syntheses easier.
- **Source-of-truth video transcript.** This source page is summary-level; a follow-up pass watching the video end-to-end with timestamps would let us cite specific claims more precisely (especially the "100M" framing).
