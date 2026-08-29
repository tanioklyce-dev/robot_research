---
title: "Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research (Soldaini et al. 2024)"
type: source
url: https://arxiv.org/abs/2402.00159
local_path: raw/2402.00159.pdf
sha256: 8c8ca17ecf6a7a7cde309daba7badbca32012c9f67decc87d3f54d28aaa43429
author: Luca Soldaini, Rodney Kinney, Akshita Bhagia, Dustin Schwenk, … (Allen Institute for AI / Ai2)
published: 2024-01-31
ingested: 2026-07-24
venue: "ACL 2024 (arXiv:2402.00159, v2 2024-06-06); Ai2"
tags: [dolma, pretraining-corpus, dataset, open-data, ai2, data-curation, language-model]
---

# Dolma: an Open Corpus of Three Trillion Tokens

## Summary

Dolma is the **open pretraining corpus** the [Allen Institute for AI](../entities/ai2.md) built and released so that language-model pretraining can be studied *scientifically* — the data half of the [OLMo](../entities/olmo.md) "truly open" program. Its thesis mirrors OLMo's: pretraining corpora are almost never disclosed (commercial models hide them; even "open" models ship weights without data), so no one can study **how data shapes model capabilities**. Dolma answers with **3 trillion tokens**, extensive documentation, curation ablations, and — crucially — an **open-source curation toolkit** so the pipeline itself is reproducible.

## Key claims

- **Scale & composition.** **3T tokens across >4B documents from 6 sources**, curated down from **~200 TB of raw text**: **web** (Common Crawl, ~2,479B tokens — the bulk), **code** (GitHub ~411B), **social media** (Reddit ~89B), **scientific papers**, **public-domain books**, and **encyclopedic** (Wikipedia). English.
- **Curation is the science.** The paper runs ablations on **intermediate states** of the corpus to report what actually matters: **deduplication**, **quality filtering** (KenLM perplexity "Wikipedia-likeness" buckets — high 21.9% / medium 28.5% / low 49.6%), and heuristic filtering combining **Gopher rules + one C4 heuristic**. Explicitly flags that "quality filter" is a misnomer (it filters *toward a distribution*, not toward objective quality).
- **The toolkit is the reusable artifact.** The **open-source data-curation toolkit** (dedup, taggers, mixing) is released so others can reproduce Dolma or build new corpora — arguably more valuable long-term than the static dump.
- **Open access.** Corpus on HuggingFace, toolkit on GitHub, under a **permissive data license (ODC-BY)** — the data foundation every [OLMo](../entities/olmo.md) / [OLMoE](../entities/olmoe.md) model trains on.

## Entities mentioned

- [Dolma](../entities/dolma.md) — the corpus (this source's subject).
- [OLMo](../entities/olmo.md) / [OLMoE](../entities/olmoe.md) — the models trained on Dolma.
- [Ai2](../entities/ai2.md) — the lab.

## Concepts touched

- Data curation for LM pretraining (dedup / quality filtering / mixing) — no dedicated concept page yet; a candidate if the data-centric thread grows.

## Open questions

- Dolma is **English-only** and 2024-vintage; the OLMo 2 mid-training mix (**Dolmino**) is its specialized successor ([OLMo 2](olmo-2-paper.md)).
- How much of OLMo's competitiveness is Dolma vs architecture/recipe? The OLMo papers argue data quality is load-bearing, but a clean attribution isn't isolated here.
