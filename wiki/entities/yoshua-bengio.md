---
title: Yoshua Bengio
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 8
tags: [person, montreal, mila, turing-award, attention, nmt, distributed-representations, word-embeddings, language-model, deep-learning]
---

**Yoshua Bengio** — Université de Montréal; founder and scientific director of **Mila** (Quebec AI Institute); Turing Award 2018 (with [LeCun](yann-lecun.md) and [Hinton](geoffrey-hinton.md)). The third of the connectionist trio, and the one whose contribution to this wiki is the most narrowly identifiable: **he is where the learned embedding table comes from.**

In this wiki he is the senior author at **both ends of the lineage that produced the Transformer**, eleven years apart: [A Neural Probabilistic Language Model](../sources/bengio2003-neural-probabilistic-language-model.md) (2003), which created the embedding table, and [Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md) (2014), which created attention. He also **named** attention — the mechanism's working title was *RNNsearch*, and "attention" was his suggestion on a final pass over the paper ([per Bahdanau, relayed by Karpathy](../sources/karpathy-software-3-and-transformer-history-lecture.md)).

## Role in the wiki's lineage

- **[Bengio et al. 2003 — A Neural Probabilistic Language Model](../sources/bengio2003-neural-probabilistic-language-model.md)** — first author. The `|V| × m` lookup matrix `C`, trained by SGD alongside the MLP that consumes it; the curse-of-dimensionality framing of why `n`-grams cannot generalize across words; and the §5.2 future-work list that names hierarchical softmax, sampled/negative-sampling training, embedding interpretability, and contextual (polysemy-aware) representations years before each was built. See [distributed representations](../concepts/learning/distributed-representations.md).
- **The energy-based branch.** §5.1 of the same paper builds an **energy-minimization variant** — output word gets its own feature vector, network emits a scalar energy, products-of-experts framing after [Hinton](geoffrey-hinton.md) 2000. It is the earliest [EBM](../concepts/learning/energy-based-models.md)-for-sequences construction in this wiki, and it is Bengio's rather than [LeCun](yann-lecun.md)'s — a useful corrective to the wiki's otherwise LeCun-centric EBM thread.
- **[Bahdanau, Cho & Bengio 2014 — Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md)** — senior author. Identifies the fixed-length-vector bottleneck in [seq2seq](../sources/sutskever2014-sequence-to-sequence-learning.md) and removes it with a soft, differentiable alignment. See [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md).
- **[Cho et al. 2014 — Learning Phrase Representations using RNN Encoder–Decoder](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md)** — senior author. The encoder–decoder and the GRU, three months before his group published the paper diagnosing the encoder–decoder's central flaw. Reference [1] of that paper is his own 2003 NPLM.
- **[Cho et al. 2014b — On the Properties of Neural Machine Translation](../sources/cho2014b-properties-of-neural-machine-translation.md)** — senior author on the analysis paper too. Across 2014 his name is on the architecture, the fix, and the measurement.
- **Hierarchical softmax** — Morin & Bengio is the origin, cited by both [word2vec](../sources/mikolov2013-distributed-representations-words-phrases.md) papers; and [NPLM §5.2](../sources/bengio2003-neural-probabilistic-language-model.md) item 2 proposes the tree-structured output layer as future work, estimating the speed-up at `|V|/log|V|`.
- **Cited-through work not separately ingested** — Bengio & Bengio (2000) on neural models of joint distributions over discrete variables, the direct predecessor architecture; Bengio & Senécal (2003) on importance-sampling training, the 100× speed-up companion; Bengio (2002) on tree-structured / hierarchical output layers.

## Not covered here

His post-2015 work — GANs-adjacent generative modeling, consciousness-prior / System-2 work, and his AI-safety and governance activity (chair of the International AI Safety Report) — is out of scope unless a source lands.

## Mentioned in

- [Bengio, Ducharme, Vincent & Jauvin 2003 — A Neural Probabilistic Language Model](../sources/bengio2003-neural-probabilistic-language-model.md) — first author.
- [fast.ai — Practical Deep Learning for Coders](../sources/fastai-practical-deep-learning.md) — as co-author of the Goodfellow/Bengio/Courville *Deep Learning* textbook.
- [Bahdanau, Cho & Bengio 2014 — Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md) — senior author; named the mechanism.
- [Cho et al. 2014 — Learning Phrase Representations using RNN Encoder–Decoder](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md) — senior author.
- [Cho et al. 2014b — On the Properties of Neural Machine Translation](../sources/cho2014b-properties-of-neural-machine-translation.md) — senior author.
- [Mikolov et al. 2013a](../sources/mikolov2013-efficient-estimation-word-representations.md) / [2013b](../sources/mikolov2013-distributed-representations-words-phrases.md) — reference [1] in both; Morin & Bengio hierarchical softmax.
- [Karpathy — Software 3.0 and the history of the Transformer](../sources/karpathy-software-3-and-transformer-history-lecture.md) — credited on stage with choosing the word "attention."
- [Curriculum Module 1 — Neural networks](../syntheses/curriculum/curriculum-01-neural-networks.md) (synthesis, not source) — same textbook, in the reading list.
- [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis).

## Open questions / TBD

- ~~Bahdanau, Cho & Bengio 2014 is the single missing source connecting him to the transformer lineage.~~ **Resolved 2026-08-30** — ingested.
- ~~Cho et al. 2014a (the GRU / RNN Encoder–Decoder paper) remains un-ingested.~~ **Resolved 2026-08-30** — [ingested](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md); he is senior author on that one too. **Cho et al. 2014b** is now the remaining gap.
- Mila as an institution has no entity page; only worth adding if a Mila-affiliated robotics or world-model source lands.
