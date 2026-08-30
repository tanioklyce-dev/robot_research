---
title: "Distributed Representations of Words and Phrases and their Compositionality (Mikolov, Sutskever, Chen, Corrado, Dean, NIPS 2013)"
type: source
url: https://arxiv.org/abs/1310.4546
local_path: raw/1310.4546v1.pdf
sha256: b21848e7b9b6ba1191f8283892a72b5529205bfdeca462403bd69ab6c6f8c6d1
author: Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, Jeffrey Dean
affiliation: Google Inc., Mountain View
venue: "NIPS 2013 (Advances in Neural Information Processing Systems 26); arXiv 1310.4546"
published: 2013-10-16
ingested: 2026-08-30
tags: [word2vec, negative-sampling, nce, subsampling, skip-gram, phrases, compositionality, mikolov, sutskever, google, foundational]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/1310.4546v1.pdf`, 9 pages), pages 1–8 in full; references skimmed. All six tables re-extracted in layout mode. This is **word2vec paper 2 of 2** — see [Mikolov et al. 2013a (ICLR workshop)](mikolov2013-efficient-estimation-word-representations.md) for CBOW / Skip-gram and the analogy benchmark. This paper assumes that one.

## Summary

**"Distributed Representations of Words and Phrases and their Compositionality"** — Mikolov, Sutskever, Chen, Corrado & Dean (Google; NIPS 2013). Four extensions to Skip-gram, of which one became the default and one is under-appreciated:

1. **Negative sampling (NEG)** — a deliberately simplified [NCE](../glossary.md#nce) that replaces the softmax entirely. This is the trick "word2vec" usually refers to.
2. **Subsampling of frequent words** — discard `w` with probability `1 − √(t/f(w))`, `t ≈ 10⁻⁵`. 2–10× speedup *and* better rare-word vectors. The under-appreciated one.
3. **Phrase vectors** — find collocations by a scored bigram statistic, replace them with single tokens, retrain. `vec("Montreal Canadiens") − vec("Montreal") + vec("Toronto") ≈ vec("Toronto Maple Leafs")`.
4. **Additive compositionality** — `vec("Russia") + vec("river") ≈ vec("Volga River")`, with a mechanism argument for why.

Where [paper 1](mikolov2013-efficient-estimation-word-representations.md) removed the hidden layer and left the softmax as the bottleneck, this paper removes the softmax. The result is the version everyone actually ran: an optimized single-machine implementation trains on **more than 100 billion words in one day**.

**Why it matters to this wiki.** Negative sampling is the direct ancestor of **InfoNCE**, and therefore of the contrastive machinery underneath [SSL](../syntheses/curriculum/curriculum-04-self-supervised-learning.md), [IBC](ibc-paper.md)'s energy training, and the collapse-avoidance problem the [JEPA](../concepts/world-models/jepa.md) line spends its time on. The wiki's [NCE glossary entry](../glossary.md#nce) already says "generalizes to InfoNCE in SSL"; this is the paper where the generalization starts, and it starts with an explicit decision to **give up the estimator's consistency guarantee** in exchange for speed.

## Abstract (verbatim)

> "The recently introduced continuous Skip-gram model is an efficient method for learning high-quality distributed vector representations that capture a large number of precise syntactic and semantic word relationships. In this paper we present several extensions that improve both the quality of the vectors and the training speed. By subsampling of the frequent words we obtain significant speedup and also learn more regular word representations. We also describe a simple alternative to the hierarchical softmax called negative sampling. An inherent limitation of word representations is their indifference to word order and their inability to represent idiomatic phrases. For example, the meanings of 'Canada' and 'Air' cannot be easily combined to obtain 'Air Canada'. Motivated by this example, we present a simple method for finding phrases in text, and show that learning good vector representations for millions of phrases is possible."

## The objective, and the problem with it (§2)

Skip-gram maximizes the average log probability of context words given the centre word:

```
(1/T) Σ_t  Σ_{−c ≤ j ≤ c, j≠0}  log p(w_{t+j} | w_t)
p(w_O | w_I) = exp(v'_{w_O}ᵀ v_{w_I}) / Σ_{w=1..W} exp(v'_wᵀ v_{w_I})
```

Each word has **two** vectors: an "input" `v_w` (used when it is the centre word) and an "output" `v'_w` (used when it is a context word). The gradient of the log-probability costs `O(W)` with `W` in the range `10⁵–10⁷`. Same bottleneck [Bengio et al. 2003](bengio2003-neural-probabilistic-language-model.md) measured at 99.7% of compute, ten years on.

### Hierarchical softmax (§2.1)

Binary Huffman tree over the vocabulary; `p(w|w_I)` is a product of `σ(±v'_{n(w,j)}ᵀ v_{w_I})` along the root-to-leaf path, cost `O(log W)`. Introduced by **Morin & Bengio**; tree-construction variants explored by **Mnih & Hinton**. Note the asymmetry it introduces: one vector per *word* plus one per *inner node*, rather than two per word.

### Negative sampling (§2.2) — the paper's central move

```
log σ(v'_{w_O}ᵀ v_{w_I})  +  Σ_{i=1..k}  E_{w_i ~ P_n(w)} [ log σ(−v'_{w_i}ᵀ v_{w_I}) ]
```

Replace each `log P(w_O|w_I)` term with this. In words: **push the observed context word's vector toward the centre word's, push `k` random words' vectors away.** No normalization over the vocabulary anywhere. `k = 5–20` for small corpora, `2–5` for large ones.

> [!note] The methodological moment worth marking
> NCE (Gutmann & Hyvärinen) is a *principled* estimator — it provably approximately maximizes the log-probability of the softmax, given both noise samples and their numerical probabilities. Negative sampling keeps the samples, drops the probabilities, and thereby drops the guarantee. The paper says so outright: *"while NCE approximately maximizes the log probability of the softmax, this property is not important for our application"* — because "the Skip-gram model is only concerned with learning high-quality vector representations."
>
> This is the template for a pattern that recurs through this wiki: when the model is a **means to a representation** rather than a density estimate, the estimator's statistical properties stop being the thing to optimize, and downstream representation quality becomes the only arbiter. InfoNCE, [Barlow Twins](barlow-twins-paper.md), [VICReg](vicreg-paper.md) and the [JEPA](../concepts/world-models/jepa.md) anti-collapse regularizers all live on the far side of that decision. It also explains why that literature is so empirical: once the guarantee is gone, ablation is the only evidence available.

**The noise distribution is a tuned hyperparameter, not a choice of convenience.** `P_n(w) = U(w)^{3/4} / Z` — the unigram distribution raised to the 3/4 power — "outperformed significantly the unigram and the uniform distributions, for both NCE and NEG, on every task we tried." The exponent is unexplained and, as far as this ingest can tell, never given a principled derivation. It is one of the most-copied magic numbers in ML.

### Subsampling of frequent words (§2.3)

```
P(discard w_i) = 1 − √( t / f(w_i) ),    t ≈ 10⁻⁵
```

Rationale: `France`–`Paris` co-occurrence is informative; `France`–`the` is not, because `the` co-occurs with everything. Aggressively discards words above frequency `t` while preserving frequency *ranking*. Chosen heuristically, and reported to both accelerate training and **improve the vectors of rare words** — the words it never touches. That second effect is the interesting one: removing high-frequency noise from the contexts of rare words is what improves them.

## Results

### Word analogies (Table 1) — 300-d Skip-gram, 1B-word news corpus, vocab 692K

| Method | Time [min] | Syntactic [%] | Semantic [%] | Total [%] |
|---|---|---|---|---|
| NEG-5 | 38 | 63 | 54 | 59 |
| NEG-15 | 97 | 63 | 58 | 61 |
| HS-Huffman | 41 | 53 | 40 | 47 |
| NCE-5 | 38 | 60 | 45 | 53 |
| *with 10⁻⁵ subsampling* | | | | |
| **NEG-5** | **14** | 61 | 58 | 60 |
| **NEG-15** | 36 | 61 | **61** | **61** |
| HS-Huffman | 21 | 52 | 59 | 55 |

Three readings:

- **NEG > NCE > HS** on this task. Negative sampling beats the principled estimator it simplifies (59 vs 53 at `k=5`, equal cost).
- **Subsampling is nearly free accuracy.** NEG-5 goes 38 min → **14 min** and 59 → 60. NEG-15 matches NEG-5's *unsubsampled* time while gaining 2 points.
- **Hierarchical softmax gains most from subsampling** (47 → 55), which is the first hint of the reversal in Table 3.

### Phrases (§4, Tables 2–3)

Collocations scored by `score(w_i, w_j) = (count(w_i w_j) − δ) / (count(w_i) × count(w_j))`, with `δ` a discount suppressing phrases built from rare words; 2–4 passes with a decreasing threshold, allowing multi-word phrases to accrete. Phrase analogy test set: **3,218 examples**, 5 categories (newspapers, NHL/NBA teams, airlines, company executives).

| Method | Dim | No subsampling [%] | 10⁻⁵ subsampling [%] |
|---|---|---|---|
| NEG-5 | 300 | 24 | 27 |
| NEG-15 | 300 | 27 | 42 |
| **HS-Huffman** | 300 | 19 | **47** |

> [!warning] The ordering reverses between tasks
> On words (Table 1), NEG beats HS by 12 points. On phrases with subsampling (Table 3), **HS beats NEG by 5** — and HS is the *worst* method on the same task without subsampling. The paper's own conclusion is that "the choice of the training algorithm and the hyper-parameter selection is a task specific decision."
>
> This is worth stating plainly because the folklore does not: **"negative sampling is the word2vec method" is wrong.** The best model in this paper uses hierarchical softmax. Reported best: 33B words, HS, 1000 dimensions, whole sentence as context → **72%** on phrase analogies, dropping to **66%** at 6B words.

### Additive compositionality (§5, Table 5)

`vec("Czech") + vec("currency") ≈ koruna`; `vec("Vietnam") + vec("capital") ≈ Hanoi`; `vec("Russian") + vec("river") ≈ Volga River`.

The mechanism argument is the part worth keeping. Word vectors enter the softmax linearly, so a vector's components relate **logarithmically** to the output-layer probabilities. Summing two vectors therefore corresponds to **multiplying their context distributions**, and a product of distributions acts as **AND**: words scored highly by both survive, everything else is suppressed. So "Russian AND river" lands on Volga.

That gives the wiki a concrete, mechanistic answer to *why* arithmetic in an embedding space does anything at all — and it is specific to a log-linear model with a softmax output, not a general property of learned embeddings.

### Figure 2 — country/capital PCA

A 2-D PCA of 1000-d vectors places country–capital pairs as **roughly parallel offsets** (China–Beijing, Russia–Moscow, Spain–Madrid…), with no supervision about what a capital is. This figure, more than the analogy tables, is the image that sold the field on learned geometry.

### Against published vectors (Table 6)

Nearest neighbours of rare words vs Collobert (50-d, **2 months** training), Turian (200-d, few weeks), Mnih (100-d, 7 days), and Skip-Phrase (1000-d, **1 day**, 30B words). For `Havel`, Skip-Phrase returns *Vaclav Havel*, *president*, *Velvet Revolution*; Mnih returns *Podhurst*, *Harlang*, *Agarwal*. The paper attributes the gap to "two to three orders of magnitude more data," at a fraction of the training time.

## What the paper does not do

- **No pretrain-then-finetune.** The vectors are frozen artifacts consumed by downstream systems, not initialization for further training. That step arrives with ELMo/BERT.
- **No contextual representation.** One vector per word (or phrase), so polysemy is unaddressed — precisely [Bengio et al. 2003](bengio2003-neural-probabilistic-language-model.md) §5.2 item 6, still open ten years later. Phrase tokens are a partial workaround: `Air Canada` gets its own vector because it cannot be composed, which is a vocabulary fix, not a representational one.
- **No word order.** CBOW averages; Skip-gram samples within a window. Called out in the abstract as an "inherent limitation."
- **No theory for the 3/4 exponent, the `√(t/f)` form, or the CBOW/Skip-gram semantic-syntactic split.** All three are reported as working and left there.

## Entities mentioned

- **[Tomas Mikolov](../entities/tomas-mikolov.md)** — first author.
- **[Ilya Sutskever](../entities/ilya-sutskever.md)** — second author; the same year as [Sequence to Sequence Learning](sutskever2014-sequence-to-sequence-learning.md).
- **[Jeff Dean](../entities/jeff-dean.md)**, Kai Chen, Greg Corrado — co-authors.
- **[Geoffrey Hinton](../entities/geoffrey-hinton.md)** — cited twice: Rumelhart, Hinton & Williams 1986 as the earliest use of word representations, and Mnih & Hinton 2009 for hierarchical-softmax tree construction.
- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — reference [1] (NPLM), and Morin & Bengio for hierarchical softmax.
- **Gutmann & Hyvärinen** — NCE, the estimator negative sampling simplifies.

## Concepts touched

- **[Distributed representations](../concepts/learning/distributed-representations.md)**, **[NCE](../glossary.md#nce)**, **[negative sampling](../glossary.md#negative-sampling)**, **[hierarchical softmax](../glossary.md#hierarchical-softmax)**, **[Skip-gram](../glossary.md#skip-gram)**.
- **[Energy-based models](../concepts/learning/energy-based-models.md)** — negative sampling is contrastive training with explicit negatives, the same machinery [IBC](ibc-paper.md) uses for policies and the practical pain point [Diffusion Policy](../entities/diffusion-policy.md) cites for abandoning it.
- **[Contrastive learning](../glossary.md#contrastive-learning)** — the SSL line's direct ancestor.

## Open questions / TBD

- **The `U(w)^{3/4}` noise distribution** has no derivation here or, as far as this ingest found, anywhere authoritative. One of ML's most-copied unexplained constants.
- **Levy & Goldberg (2014)**, showing Skip-gram-with-negative-sampling implicitly factorizes a shifted PMI matrix, is the key theoretical follow-up and is not ingested. It would connect this paper to the [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) page, which currently has no pre-2020 ancestry.
- **Whether the HS-beats-NEG-on-phrases reversal has ever been explained.** The paper reports it as a surprise and moves on.
