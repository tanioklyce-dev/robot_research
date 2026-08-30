---
title: Geoffrey Hinton
type: entity
subtype: person
created: 2026-07-06
updated: 2026-08-30
sources: 5
tags: [person, toronto, wake-sleep, helmholtz-machine, backpropagation, turing-award, deep-learning]
---

**Geoffrey Hinton** — University of Toronto (emeritus) / formerly Google Brain; Turing Award 2018 (with LeCun and Bengio), Nobel Prize in Physics 2024. The central figure of the connectionist program: backpropagation popularization (Rumelhart, Hinton & Williams 1986), Boltzmann machines, the [wake-sleep algorithm](../sources/wake-sleep-paper.md) and Helmholtz machine, deep belief networks, dropout, RMSprop, AlexNet (as Krizhevsky & Sutskever's advisor), and distillation. In this wiki he appears primarily as the origin of the **recognition-model / generative-model** decomposition that became the [VAE](../concepts/learning/variational-autoencoder.md) encoder–decoder.

## Role in the wiki's generative-models lineage

- **[Wake-sleep](../sources/wake-sleep-paper.md)** (Hinton, Dayan, Frey, Neal — *Science* 1995) — first author. Introduced the jointly-trained bottom-up recognition network + top-down generative network, the MDL/free-energy objective, and the "Helmholtz machine" framing. Both VAE papers position themselves directly against it: [Kingma & Welling](../sources/vae-paper.md) call it the only prior online method for the same model class; [Rezende et al.](../sources/stochastic-backpropagation-paper.md) beat it 86.6 vs 91.3 nats on binarized MNIST and diagnose its inconsistent two-objective training.
- **Precursors cited through the wiki's sources**: non-linear Gaussian belief networks (Frey & Hinton 1999, a DLGM special case), deep Boltzmann machine recognition models (Salakhutdinov & Larochelle 2010, cited in the [VAE Paper](../sources/vae-paper.md) §4), DBNs (benchmark line in [Rezende et al.](../sources/stochastic-backpropagation-paper.md) table 1), and **RMSprop** (Coursera lecture heuristic — the optimizer Rezende et al. train with).
- **Cited-through in the embedding lineage**: [Bengio et al. 2003](../sources/bengio2003-neural-probabilistic-language-model.md) credits *Learning distributed representations of concepts* (Hinton 1986) as the origin of the idea it scales up, frames its §5.1 energy-minimization variant on **products of experts / contrastive divergence** (Hinton 2000), and thanks him in the acknowledgments. His products-of-HMMs work with Brown (2000) is the tractability contrast that paper draws — a product over whole-sequence experts needs approximate gradients, while Bengio's per-element factorization does not.
- **Pedagogical thread**: appears in the [Welch Labs perceptron video](../sources/welchlabs-perceptron.md) and [curriculum Module 1](../syntheses/curriculum/curriculum-01-neural-networks.md) backprop-history material.

## Mentioned in

- [Wake-Sleep Paper](../sources/wake-sleep-paper.md) — first author.
- [VAE Paper (Kingma & Welling)](../sources/vae-paper.md) — wake-sleep as the positioning baseline.
- [Stochastic Backpropagation Paper (Rezende et al.)](../sources/stochastic-backpropagation-paper.md) — wake-sleep baseline; NLGBN special case; RMSprop.
- [Bengio et al. 2003 — A Neural Probabilistic Language Model](../sources/bengio2003-neural-probabilistic-language-model.md) — distributed representations (1986) as the acknowledged origin; products of experts as the §5.1 framing; acknowledgments.
- [Welch Labs — The Perceptron video](../sources/welchlabs-perceptron.md)
- [Curriculum Module 1 — Neural networks](../syntheses/curriculum/curriculum-01-neural-networks.md) (synthesis, not source)

## Open questions / TBD

- His post-2023 AI-risk advocacy period is out of scope for this wiki unless a safety-thread source lands.
- Boltzmann machines / DBNs have no concept page; only worth adding if an energy-based-history ingest happens (would slot next to [EBMs](../concepts/learning/energy-based-models.md)). The [NPLM](../sources/bengio2003-neural-probabilistic-language-model.md) §5.1 ingest brought products-of-experts into the wiki by citation only — the 2000 tech report itself is not ingested.
