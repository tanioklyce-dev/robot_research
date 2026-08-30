---
title: Kyunghyun Cho
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 1
tags: [person, gru, attention, encoder-decoder, montreal, nyu, machine-translation, genentech]
---

**Kyunghyun Cho** — then Université de Montréal, now NYU (and Genentech). Co-author of the attention paper, and the originator of the **GRU** and the **RNN Encoder–Decoder** framing that attention was built on top of.

## Role in the wiki's lineage

- **[Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md)** (ICLR 2015) — second author. His own **RNNencdec** is the baseline the paper beats, and his **gated hidden unit** is the recurrent cell both models use: the paper states that "by a 'hidden unit' we always mean the gated hidden unit."
- **Cited-through, un-ingested**: Cho et al. 2014a (*Learning Phrase Representations using RNN Encoder–Decoder*) introduced the GRU — which this wiki's [glossary](../glossary.md#gru) already defines — and Cho et al. 2014b supplied the empirical result the attention paper's whole conjecture rests on: that basic encoder–decoder quality **deteriorates rapidly as input length increases**.

> [!note] The baseline author is a co-author of the paper that beats it
> RNNencdec is Cho's architecture; RNNsearch beats it by 7.6 BLEU at matched data, and he is the second author of the paper reporting that. Worth noting alongside [Mikolov](tomas-mikolov.md), who published the result that his own RNNLM line was solving the wrong problem. The pattern is healthy and not especially common.

## Mentioned in

- [Bahdanau, Cho & Bengio 2014 — Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md) — second author.
- [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis).

## Open questions / TBD

- **Cho et al. 2014a** (the GRU / RNN Encoder–Decoder paper) is the most-cited un-ingested source in this wiki's sequence-model lineage — the glossary defines the GRU without a primary source behind it.
- His Genentech-era work on ML for biology is out of scope.
