---
title: Dolma (open pretraining corpus)
type: entity
subtype: dataset
created: 2026-07-24
updated: 2026-07-24
sources: 4
tags: [dolma, pretraining-corpus, dataset, open-data, ai2, data-curation]
---

# Dolma (open pretraining corpus)

**Dolma** is the [Allen Institute for AI](ai2.md)'s **open pretraining corpus** —
**3 trillion tokens** of English text released with full documentation and an
**open-source curation toolkit** ([Soldaini et al. 2024](../sources/dolma-paper.md)).
It is the **data half** of the [OLMo](olmo.md) "truly open" program: the corpus
every [OLMo](olmo.md) / [OLMoE](olmoe.md) model trains on, and the thing that makes
those models *scientifically reproducible* rather than merely open-weight.

## Key facts

- **3T tokens across >4B documents from 6 sources**, curated from **~200 TB** raw:
  **web** (Common Crawl, the bulk), **code** (GitHub), **social media** (Reddit),
  **scientific papers**, **public-domain books**, **encyclopedic** (Wikipedia).
- **Curation ablations** on intermediate corpus states: **deduplication**,
  **quality filtering** (KenLM perplexity "Wikipedia-likeness" buckets),
  **Gopher + C4** heuristics — the paper's finding is that curation choices, not
  just scale, drive capability.
- **The toolkit is the durable artifact:** an open-source dedup/tagging/mixing
  pipeline so anyone can reproduce Dolma or build a new corpus.
- **Permissive data license (ODC-BY);** on HuggingFace, toolkit on GitHub.
- **Successor:** the **Dolmino Mix 1124** specialized mid-training data in
  [OLMo 2](../sources/olmo-2-paper.md).

## Why it matters in this wiki

Dolma is the concrete answer to "open model" skepticism: it's the **inspectable
training data** under [OLMo](olmo.md)/[OLMoE](olmoe.md), the layer that
open-weights-only releases (Llama, Qwen, Mixtral) don't provide. It anchors the
wiki's **data-centric / reproducibility** thread alongside PixMo (the vision-side
open-data effort under [Molmo](molmo.md)).

## Related

- [OLMo](olmo.md) / [OLMoE](olmoe.md) — the models trained on Dolma.
- [Ai2](ai2.md) — the lab that built it.

## Mentioned in

- [Dolma paper (Soldaini et al. 2024)](../sources/dolma-paper.md) — the primary source.
- [OLMo paper (Groeneveld et al. 2024)](../sources/olmo-paper.md) — releases Dolma as OLMo's corpus.
- [OLMo 2 (2 OLMo 2 Furious)](../sources/olmo-2-paper.md) — adds the Dolmino mid-training mix.
