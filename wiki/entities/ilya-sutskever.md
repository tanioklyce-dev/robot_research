---
title: Ilya Sutskever
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 5
tags: [person, google, openai, ssi, seq2seq, encoder-decoder, lstm, alexnet, word2vec]
---

**Ilya Sutskever** — Google Brain (2013–2015), co-founder and Chief Scientist of OpenAI (2015–2024), now co-founder of Safe Superintelligence Inc. Previously University of Toronto, where he was [Hinton](geoffrey-hinton.md)'s student and, with Alex Krizhevsky, a co-author of **AlexNet** (2012).

In this wiki he appears at the point where he was doing sequence modelling at Google, on two consecutive papers that bracket the pre-attention era.

## Role in the wiki's lineage

- **[Sequence to Sequence Learning with Neural Networks](../sources/sutskever2014-sequence-to-sequence-learning.md)** (NIPS 2014) — first author. Establishes the **encoder–decoder** pattern: one LSTM compresses the input to a fixed vector, a second decodes the output autoregressively until `<EOS>`. First pure neural system to beat phrase-based SMT on a large-scale translation task (BLEU 34.81 vs 33.30). Also the source of the **reverse-the-source-sentence** trick, worth ~4.7 BLEU with no model change.
- **[Distributed Representations of Words and Phrases](../sources/mikolov2013-distributed-representations-words-phrases.md)** (NIPS 2013) — second author, with [Mikolov](tomas-mikolov.md). Negative sampling and subsampling.

The pairing is the interesting part. In 2013 he helped make *word* representations cheap and good; in 2014 he showed the same machinery could map *sequences* to sequences, and produced the first sentence-level embedding plots in this wiki's lineage ([seq2seq](../sources/sutskever2014-sequence-to-sequence-learning.md) Figure 2, PCA of encoder states clustering by meaning and word order).

> [!note] The architecture he established is the one attention replaced
> seq2seq's fixed-width vector is exactly the bottleneck [Bahdanau, Cho & Bengio](../sources/bahdanau2014-neural-machine-translation-align-translate.md) named and removed, months later and in the same year. seq2seq's own Table 1 reports Bahdanau's system at 28.45 BLEU against its 34.81 — attention lost that benchmark and won the decade. See [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md).

## Not covered here

AlexNet (2012), the OpenAI GPT line, and his post-2024 SSI work are out of scope unless sources land — a notable gap given that every [VLA](../concepts/learning/vla-models.md) in this wiki has a GPT-lineage trunk. His name reaches the wiki's robotics material only indirectly, through architectures.

## Mentioned in

- [Sutskever, Vinyals & Le 2014 — Sequence to Sequence Learning with Neural Networks](../sources/sutskever2014-sequence-to-sequence-learning.md) — first author.
- [Mikolov et al. 2013b — Distributed Representations of Words and Phrases](../sources/mikolov2013-distributed-representations-words-phrases.md) — second author.
- [Geoffrey Hinton](geoffrey-hinton.md) — his doctoral advisor; AlexNet co-author.

## Open questions / TBD

- **AlexNet (Krizhevsky, Sutskever & Hinton 2012)** is un-ingested and is the most-cited paper adjacent to this wiki's [CNN module](../syntheses/curriculum/curriculum-02-cnns.md) without a source page.
- The GPT-line papers (GPT-1/2/3) are likewise absent; the wiki tracks their descendants closely and their origin not at all.
