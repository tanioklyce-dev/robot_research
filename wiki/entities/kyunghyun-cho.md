---
title: Kyunghyun Cho
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 4
tags: [person, gru, attention, encoder-decoder, montreal, nyu, machine-translation, genentech]
---

**Kyunghyun Cho** — then Université de Montréal, now NYU (and Genentech). Co-author of the attention paper, and the originator of the **GRU** and the **RNN Encoder–Decoder** framing that attention was built on top of.

## Role in the wiki's lineage

- **[Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md)** (ICLR 2015) — second author. His own **RNNencdec** is the baseline the paper beats, and his **gated hidden unit** is the recurrent cell both models use: the paper states that "by a 'hidden unit' we always mean the gated hidden unit."
- **[Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md)** (EMNLP 2014) — **first author**. Both of his contributions in one paper: the **RNN Encoder–Decoder**, and the gated unit later called the **GRU** (reset gate + update gate, "motivated by the LSTM unit but much simpler"). Applied not as a translation system but as one feature scoring phrase pairs inside Moses — reaching BLEU 34.64 against the same 33.30 baseline [seq2seq](../sources/sutskever2014-sequence-to-sequence-learning.md) would beat outright three months later with the same decomposition used end to end.
- **[On the Properties of Neural Machine Translation: Encoder–Decoder Approaches](../sources/cho2014b-properties-of-neural-machine-translation.md)** (SSST-8, Sept 2014) — **first author**. The measurement the attention paper's conjecture rests on: quality collapsing with **sentence length** and with **unknown-word count**, against a Moses baseline whose BLEU *rises* with length. Also introduces **grConv**, which performs unsupervised parsing as a byproduct of a translation objective.

> [!note] The baseline author is a co-author of the paper that beats it
> RNNencdec is Cho's architecture, published in June 2014; RNNsearch beats it by 7.6 BLEU at matched data in September, and he is the second author of the paper reporting that. [Bahdanau](dzmitry-bahdanau.md) runs the same loop in reverse — fourth author on the June paper, first author on the September one. **One group, one quarter, propose-then-refute.** Worth noting alongside [Mikolov](tomas-mikolov.md), who published the result that his own RNNLM line was solving the wrong problem. The pattern is healthy and not especially common.

> [!note] Three papers in 2014, and the third one complicates the story
> June: [propose the encoder–decoder and the GRU](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md). 1 September: [co-author the paper that removes its bottleneck](../sources/bahdanau2014-neural-machine-translation-align-translate.md). 3 September: [first-author the analysis that measures the bottleneck](../sources/cho2014b-properties-of-neural-machine-translation.md) — **two days after the fix was published**. And that analysis concludes the problem is likely in the *decoder*, not the fixed-length vector the attention paper targets. Diagnosis and repair were developed concurrently, by the same people, with the two papers disagreeing about the diagnosis.

> [!note] He named neither of his own contributions
> "GRU" does not appear in [the paper that introduces it](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md) — the section is titled *"Hidden Unit that Adaptively Remembers and Forgets."* Nor does "attention" appear in the drafts of [the paper that introduces it](../sources/bahdanau2014-neural-machine-translation-align-translate.md); the working name was *RNNsearch*, and Bengio supplied the word on a final pass. Both mechanisms shipped before the names that made them citable.

## Mentioned in

- [Cho et al. 2014 — Learning Phrase Representations using RNN Encoder–Decoder](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md) — first author; the GRU and the encoder–decoder.
- [Bahdanau, Cho & Bengio 2014 — Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md) — second author.
- [Cho et al. 2014b — On the Properties of Neural Machine Translation](../sources/cho2014b-properties-of-neural-machine-translation.md) — first author; the length and unknown-word measurements, and grConv.
- [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis).
- [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis).

## Open questions / TBD

- ~~Cho et al. 2014a (the GRU / RNN Encoder–Decoder paper) is the most-cited un-ingested source in this wiki's sequence-model lineage.~~ **Resolved 2026-08-30** — [ingested](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md).
- ~~Cho et al. 2014b is the load-bearing gap.~~ **Resolved 2026-08-30** — [ingested](../sources/cho2014b-properties-of-neural-machine-translation.md), and it changed the reading of the attention paper's motivation.
- **Chung et al. 2014** — the empirical GRU-vs-LSTM comparison from the same group; the standard citation for "GRU ≈ LSTM at lower cost."
- His Genentech-era work on ML for biology is out of scope.
