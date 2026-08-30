---
title: Jeff Dean
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 2
tags: [person, google, distbelief, tensorflow, infrastructure, word2vec, systems]
---

**Jeff Dean** — Google Senior Fellow; now Chief Scientist, Google DeepMind and Google Research. In this wiki he appears not as a modelling author but as the **infrastructure** half of the word2vec papers: DistBelief, and later TensorFlow, are his group's systems.

## Role in the wiki's lineage

- **[Efficient Estimation of Word Representations in Vector Space](../sources/mikolov2013-efficient-estimation-word-representations.md)** and **[Distributed Representations of Words and Phrases](../sources/mikolov2013-distributed-representations-words-phrases.md)** (2013) — co-author on both.

The reason his name matters to these papers is Table 6 of the first one. The architectural contribution is a *deletion* — remove the hidden layer — and the payoff is only visible at a scale that requires a distributed training system: **DistBelief**, 50–100 asynchronous model replicas with Adagrad, training on 6B words across ~125–180 CPU cores. The 2003 [NPLM](../sources/bengio2003-neural-probabilistic-language-model.md) improvised the same asynchronous-parameter-server idea on a 40-CPU Myrinet cluster and called the resulting lost updates acceptable noise; DistBelief is that idea as production infrastructure a decade later.

> [!note] The wiki's recurring pattern, in one entity
> Twice in this lineage the idea was available before the compute was: [Bengio et al. 2003](../sources/bengio2003-neural-probabilistic-language-model.md) needed three weeks on 40 CPUs for five epochs over 14M words, and listed the fixes it could not afford to build. word2vec is largely those fixes, executed on infrastructure that did not exist in 2003. Who builds the substrate is part of the causal story, not a footnote to it.

## Mentioned in

- [Mikolov et al. 2013a — Efficient Estimation of Word Representations in Vector Space](../sources/mikolov2013-efficient-estimation-word-representations.md)
- [Mikolov et al. 2013b — Distributed Representations of Words and Phrases](../sources/mikolov2013-distributed-representations-words-phrases.md)

## Open questions / TBD

- **DistBelief (Dean et al., NIPS 2012)** and **TensorFlow (2016)** are both un-ingested. DistBelief is the more interesting one for this wiki: it is where asynchronous distributed SGD became standard practice.
- His current DeepMind role connects to [Google DeepMind](google-deepmind.md), which the wiki tracks heavily on the robotics side; no source links the two threads yet.
