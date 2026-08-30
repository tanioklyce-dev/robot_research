---
title: Dzmitry Bahdanau
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 4
tags: [person, attention, alignment, mila, jacobs-university, machine-translation]
---

**Dzmitry Bahdanau** — first author of the attention paper. At the time a visiting student from **Jacobs University Bremen** working with [Cho](kyunghyun-cho.md) and [Bengio](yoshua-bengio.md) at Université de Montréal; later Mila / ServiceNow Research, and an adjunct at McGill.

## Role in the wiki's lineage

- **[Learning Phrase Representations using RNN Encoder–Decoder](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md)** (EMNLP 2014, June) — **fourth author**, on the architecture he would overturn three months later. Worth knowing when reading the attention paper: he did not find the encoder bottleneck from outside, he helped build the thing that had it.
- **[Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md)** (ICLR 2015, arXiv Sept 2014) — first author. The paper that names the fixed-length-vector bottleneck in [seq2seq](../sources/sutskever2014-sequence-to-sequence-learning.md) and removes it with a learned, normalized, differentiable weighting over all encoder states — *"a mechanism of attention in the decoder."*

Everything [Vaswani et al. 2017](../sources/attention-is-all-you-need.md) kept came from here. Everything it changed — dot-product scoring instead of a feedforward scorer, keys separated from values, multiple heads, self- rather than cross-attention — is engineering on this mechanism. The wiki's [attention source page](../sources/attention-is-all-you-need.md) opened its lineage block with his name for months before the paper itself was ingested.

- **[On the Properties of Neural Machine Translation](../sources/cho2014b-properties-of-neural-machine-translation.md)** (SSST-8, Sept 2014) — third author, "research done while visiting Université de Montréal." The companion analysis paper, posted **two days after** his own attention paper.

> [!note] Where the idea came from, in his own words
> Per the email [Karpathy reads on stage](../sources/karpathy-software-3-and-transformer-history-lecture.md): he tried and abandoned ideas about "cursors that traverse the sequences," then thought of letting the decoder **learn where to put the cursor**, "certainly inspired by translation exercises that learning English in my middle school involved — your gaze shifts back and forth between source and target sequence as you translate." Expressed as a softmax and a weighted average, it **"worked from the very first try."** The name *attention* was [Bengio](yoshua-bengio.md)'s, added on a final pass.

## Mentioned in

- [Cho et al. 2014 — Learning Phrase Representations using RNN Encoder–Decoder](../sources/cho2014-rnn-encoder-decoder-phrase-representations.md) — fourth author.
- [Bahdanau, Cho & Bengio 2014 — Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md) — first author.
- [Cho et al. 2014b — On the Properties of Neural Machine Translation](../sources/cho2014b-properties-of-neural-machine-translation.md) — third author.
- [Karpathy — Software 3.0 and the history of the Transformer](../sources/karpathy-software-3-and-transformer-history-lecture.md) — his email on the origin of attention.
- [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis).

## Open questions / TBD

- His later work (neural module networks, compositional generalization, BabyAI, LLM agents at ServiceNow) is out of scope unless a source lands. **BabyAI** is the one closest to this wiki's interests — a grounded instruction-following environment, adjacent to the [agents](../concepts/agents/llm-agent-architecture.md) thread.
