---
title: Tomas Mikolov
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 2
tags: [person, google, brno, word2vec, word-embeddings, rnnlm, skip-gram, distributed-representations]
---

**Tomas Mikolov** — then Google (Mountain View), previously Brno University of Technology, later Facebook AI Research and now at CIIRC ČVUT in Prague. **The author of word2vec.** In this wiki, the person who turned learned word embeddings from a component inside a language model into a downloadable artifact the rest of the field could use.

## Role in the wiki's lineage

Two papers, six months apart, that only work as a pair:

- **[Efficient Estimation of Word Representations in Vector Space](../sources/mikolov2013-efficient-estimation-word-representations.md)** (ICLR workshop 2013) — first author. Introduces **CBOW** and **Skip-gram** by deleting the non-linear hidden layer from [Bengio's NNLM](../sources/bengio2003-neural-probabilistic-language-model.md), and introduces the **analogy benchmark** that made embedding quality measurable rather than anecdotal.
- **[Distributed Representations of Words and Phrases and their Compositionality](../sources/mikolov2013-distributed-representations-words-phrases.md)** (NIPS 2013) — first author. **Negative sampling**, **frequent-word subsampling**, phrase vectors, and the additive-compositionality mechanism argument.

The through-line is a consistent methodological bet: **a worse model trained on far more data beats a better model trained on less.** He makes it explicitly in 2013a §3 — the log-linear models "might not be able to represent the data as precisely as neural networks, but can possibly be trained on much more data efficiently" — and Table 4 of that paper concedes the point honestly, with a Bengio-style NNLM outscoring CBOW at matched data. The architectures win on the compute axis, not the modelling one.

> [!note] He is also his own baseline
> The RNNLM rows he compares against in 2013a (Tables 3, 4, 7) are his own earlier work from his Brno PhD (*Statistical Language Models Based on Neural Networks*, 2012). The RNNLM was state of the art for language modelling and he shows it losing badly on *representation* quality — 24.6% analogy accuracy against Skip-gram's 53.3%. A researcher publishing the result that his own prior line was solving the wrong problem is worth noting.

## The un-ingested third paper

**Mikolov, Yih & Zweig, *Linguistic Regularities in Continuous Space Word Representations* (NAACL 2013)** is where the vector-offset analogy method actually originated, on RNNLM vectors. Both word2vec papers cite it as the source of the technique they then popularized and benchmark. It is not in this wiki, and it is the reason the `king − man + woman` result is often misattributed to word2vec itself.

## Mentioned in

- [Mikolov et al. 2013a — Efficient Estimation of Word Representations in Vector Space](../sources/mikolov2013-efficient-estimation-word-representations.md) — first author.
- [Mikolov et al. 2013b — Distributed Representations of Words and Phrases](../sources/mikolov2013-distributed-representations-words-phrases.md) — first author.

## Open questions / TBD

- His post-Google work (FastText at FAIR, and the complexity/incremental-learning direction at ČVUT) is out of scope unless a source lands. **FastText** — subword-aware embeddings — is the natural next ingest if the wiki ever needs the answer to word2vec's out-of-vocabulary problem.
- The NAACL 2013 analogy paper above.
