---
title: Dzmitry Bahdanau
type: entity
subtype: person
created: 2026-08-30
updated: 2026-08-30
sources: 2
tags: [person, attention, alignment, mila, jacobs-university, machine-translation]
---

**Dzmitry Bahdanau** — first author of the attention paper. At the time a visiting student from **Jacobs University Bremen** working with [Cho](kyunghyun-cho.md) and [Bengio](yoshua-bengio.md) at Université de Montréal; later Mila / ServiceNow Research, and an adjunct at McGill.

## Role in the wiki's lineage

- **[Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md)** (ICLR 2015) — first author. The paper that names the fixed-length-vector bottleneck in [seq2seq](../sources/sutskever2014-sequence-to-sequence-learning.md) and removes it with a learned, normalized, differentiable weighting over all encoder states — *"a mechanism of attention in the decoder."*

Everything [Vaswani et al. 2017](../sources/attention-is-all-you-need.md) kept came from here. Everything it changed — dot-product scoring instead of a feedforward scorer, keys separated from values, multiple heads, self- rather than cross-attention — is engineering on this mechanism. The wiki's [attention source page](../sources/attention-is-all-you-need.md) opened its lineage block with his name for months before the paper itself was ingested.

## Mentioned in

- [Bahdanau, Cho & Bengio 2014 — Neural Machine Translation by Jointly Learning to Align and Translate](../sources/bahdanau2014-neural-machine-translation-align-translate.md) — first author.
- [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis).

## Open questions / TBD

- His later work (neural module networks, compositional generalization, BabyAI, LLM agents at ServiceNow) is out of scope unless a source lands. **BabyAI** is the one closest to this wiki's interests — a grounded instruction-following environment, adjacent to the [agents](../concepts/agents/llm-agent-architecture.md) thread.
