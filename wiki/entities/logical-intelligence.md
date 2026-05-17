---
title: Logical Intelligence
type: entity
subtype: organization
created: 2026-05-17
updated: 2026-05-17
sources: 1
tags: [logical-intelligence, ebm, energy-based-model, reasoning, lecun, freedman, startup, formal-verification, post-llm]
---

**Logical Intelligence** — AI company commercializing **[energy-based reasoning models](../concepts/learning/energy-based-models.md)** as an alternative-and-complement to large language models. Public launch / "first energy-based reasoning AI model" announcement on **2026-01-21**. Position: "Piloting the World's First Energy-Based Model for Critical Systems." Two products in the wiki:

- **[Aleph](aleph.md)** — agentic orchestration layer; pairs frontier LLMs (GPT-5.2 in the published headline run) with [Kona](kona.md) and the [Lean theorem prover](../concepts/learning/lean-theorem-prover.md). Available today for **formal verification and automated code generation with machine-checkable proofs**. Holds the **[PutnamBench](../concepts/learning/putnambench.md)** leaderboard at 99.4% / 668-of-672 as of May 2026 ([Aleph EBM video](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)).
- **[Kona 1.0](kona.md)** — proprietary **non-autoregressive energy-based reasoning model** (EBRM); in Q1 2026 pilots in energy, advanced manufacturing, and semiconductor verification ([Aleph EBM video](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)).

## Leadership

| Role | Person | Prior |
| --- | --- | --- |
| Founder & CEO | [Eve Bodnia](eve-bodnia.md) | — |
| Founding Chair, Technical Research Board | [Yann LeCun](yann-lecun.md) | Meta Chief AI Scientist; Turing Award 2018 |
| Chief of Mathematics | [Michael Freedman](michael-freedman.md) | Fields Medal 1986 |
| Chief of AI | [Vlad Isenbaev](vlad-isenbaev.md) | Facebook / Cruise / Nuro; ICPC World Champion |
| Chief Strategy Officer | [Patrick Hillmann](patrick-hillmann.md) | Binance CSO |

LeCun and Hillmann joined the leadership team at the **2026-01-21** launch announcement ([Aleph EBM video](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md), citing BusinessWire press release).

## Technical positioning

The company's public framing, paraphrased from the BusinessWire press release and Bodnia interview:

- **Mechanism**: EBMs "map out what is allowed and what is not, then find solutions that stay inside those boundaries." Contrasted with LLMs that "predict statistically likely answers."
- **LeCun's framing** (verbatim from press release): EBMs represent "reasoning and inference by minimizing an energy function."
- **Bodnia's framing** (verbatim from press release): "Kona learns by recognizing and correcting its own mistakes, rather than guessing the most likely answer."
- **Architectural commitment**: reasoning happens in **abstract vector space**, with natural language treated as **optional output**, not the substrate of thought.
- **Scale**: Kona models reported at **16M–200M parameters**, versus hundreds-of-billions for frontier LLMs.

The "verification layer underneath modern AI stacks" framing is the productized form of the older argument in [LeCun's 2022 "Path Towards Autonomous Machine Intelligence" paper](../sources/lecun2022-path-towards-ami.md) — same EBM agenda, applied to **reasoning and constraint satisfaction** rather than to **predictive representation learning** (which is the [JEPA](../concepts/world-models/jepa.md) branch).

## Target industries

From the BusinessWire press release: energy, advanced manufacturing, semiconductor verification, robotics, financial automation, hardware design, verified code generation. From the Bodnia interview summary: chip design, surgical robotics, smart grids, pharmacology. The thread is **zero hallucination tolerance** — domains where statistical plausibility is not an acceptable failure mode.

## Relationship to other LeCun affiliations

LeCun has **two reported post-Meta affiliations** in this wiki:

- **[AMI Labs](ami-labs.md)** — LeCun-as-founder; the executor of his [2022 AMI paper](../sources/lecun2022-path-towards-ami.md) vision (JEPA / world-models / six-module agent). Single secondary source ([Towards AI, 2026-04](../sources/towardsai-lecun-ami-labs.md)). Provisional.
- **Logical Intelligence** — LeCun as Founding Chair of the Technical Research Board, not founder; commercialization of EBMs for reasoning rather than for representation learning.

No source in this wiki addresses whether the two are collaborating, parallel, or independent. Both involve LeCun and both descend from the EBM thread of his 2022 paper.

## Related

- [Yann LeCun](yann-lecun.md) — Founding Chair of Technical Research Board.
- [Eve Bodnia](eve-bodnia.md) — Founder + CEO.
- [Michael Freedman](michael-freedman.md) — Chief of Mathematics.
- [Aleph](aleph.md) — product.
- [Kona](kona.md) — product.
- [Energy-based models](../concepts/learning/energy-based-models.md) — the substrate.
- [AMI Labs](ami-labs.md) — LeCun's other reported post-Meta affiliation.
- [IBC](ibc.md) — the wiki's earlier EBM-line entity (different application: imitation learning).

## Mentioned in

- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)
