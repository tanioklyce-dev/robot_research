---
title: "Efficient Estimation of Word Representations in Vector Space (Mikolov, Chen, Corrado, Dean, ICLR Workshop 2013)"
type: source
url: https://arxiv.org/abs/1301.3781
local_path: raw/1301.3781v3.pdf
sha256: a44d7e22d2005752271c9cc1929c6462d4c8270916b063977992a883e3a54362
author: Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
affiliation: Google Inc., Mountain View
venue: "ICLR 2013 Workshop track; arXiv 1301.3781"
published: 2013-01-16 (v1); v3 2013-09-07
ingested: 2026-08-30
tags: [word2vec, word-embeddings, cbow, skip-gram, distributed-representations, analogy, mikolov, google, hierarchical-softmax, foundational, scaling]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/1301.3781v3.pdf`, 12 pages), pages 1–11 in full; references skimmed. All eight tables re-extracted in layout mode. This is **word2vec paper 1 of 2** — see [Mikolov et al. 2013b (NIPS)](mikolov2013-distributed-representations-words-phrases.md) for negative sampling, subsampling and phrases. Neither paper is complete on its own; together they are "word2vec."

## Summary

**"Efficient Estimation of Word Representations in Vector Space"** — Mikolov, Chen, Corrado & Dean (Google; ICLR 2013 workshop track). The paper that introduced **CBOW** and **Skip-gram**, the **analogy benchmark**, and the practice of treating word vectors as a **standalone artifact** rather than a byproduct of a language model.

Its move is subtraction. [Bengio et al. 2003](bengio2003-neural-probabilistic-language-model.md) established the architecture — embedding table `C`, non-linear hidden layer, softmax — and this paper walks through its cost model (§2.1) to find the term worth deleting. With hierarchical softmax already collapsing the output layer from `H × V` to `H × log₂(V)`, the dominating cost becomes `N × D × H`: **the non-linear hidden layer.** So they remove it. What remains is a log-linear model, and the argument is explicitly a trade: the simpler model "might not be able to represent the data as precisely as neural networks, but can possibly be trained on much more data efficiently."

That trade is the whole paper, and it pays. Against a feedforward NNLM at 100 dimensions on 6B words — 50.8% analogy accuracy for **14 days × 180 CPU cores** — Skip-gram at 1000 dimensions on the same 6B words reaches **65.6% in 2.5 days × 125 cores**. Better representations, roughly an order of magnitude less compute.

**Why it matters to this wiki.** Two things, only one of which is the architecture:

1. **It is the evidence that a learned embedding geometry means something.** [Distributed representations](../concepts/learning/distributed-representations.md) argues that the similarity metric is learned rather than specified; this paper is where the field first *measured* what got learned, via `vector("biggest") − vector("big") + vector("small") ≈ vector("smallest")`. Until this benchmark existed, embedding quality was argued from cherry-picked nearest-neighbour tables — a methodological complaint the paper opens §4 with.
2. **It is where embeddings become a product.** §7 reports releasing multi-threaded C code and 1.4M pretrained entity vectors trained on 100B+ words. The 2003 paper's embeddings were internal to one model on one corpus; these were downloadable. That distribution step, not the architecture, is why "word2vec" is a household word and "NPLM" is not.

## Abstract (verbatim)

> "We propose two novel model architectures for computing continuous vector representations of words from very large data sets. The quality of these representations is measured in a word similarity task, and the results are compared to the previously best performing techniques based on different types of neural networks. We observe large improvements in accuracy at much lower computational cost, i.e. it takes less than a day to learn high quality word vectors from a 1.6 billion words data set. Furthermore, we show that these vectors provide state-of-the-art performance on our test set for measuring syntactic and semantic word similarities."

## The cost model (§2) — the paper's actual argument

Training complexity is `O = E × T × Q` (epochs × training words × per-example cost), with `E = 3–50` and `T` up to 1B. Per-architecture `Q`:

| Model | `Q` | Dominating term after hierarchical softmax |
|---|---|---|
| **NNLM** ([Bengio 2003](bengio2003-neural-probabilistic-language-model.md)) | `N×D + N×D×H + H×V` | `N × D × H` — the hidden layer |
| **RNNLM** | `H×H + H×V` | `H × H` — the recurrent matrix |
| **CBOW** | `N×D + D×log₂(V)` | the softmax tree |
| **Skip-gram** | `C×(D + D×log₂(V))` | the softmax tree, `C` times over |

The `H × V` output term is handled with **hierarchical softmax over a Huffman binary tree**: frequent words get short codes, so the expected number of evaluated nodes is about `log₂(unigram-perplexity(V))` rather than `log₂(V)` — roughly a 2× further speedup at `V = 1M`.

> [!note] The point the cost table is making
> Hierarchical softmax was already known and already applied. Its consequence is what this paper noticed: **once the output layer is cheap, the hidden layer is the bottleneck** — and a hidden layer is the one component of the NNLM that has no role in producing the embedding itself. Removing it makes the softmax efficiency load-bearing, which the paper says explicitly: the new architectures "do not have hidden layers and thus depend heavily on the efficiency of the softmax normalization." That dependency is what [paper 2](mikolov2013-distributed-representations-words-phrases.md) then attacks with negative sampling.

## The two architectures (§3)

**CBOW (Continuous Bag-of-Words).** Predict the current word from its context. Projections of all context words are **averaged** into one vector — hence "bag of words," order is discarded. Uses **four history and four future words** (word2vec is not causal; it sees the future, which a language model cannot).

**Skip-gram.** The inverse: predict the surrounding words from the current word. For each training word, sample `R ∈ [1, C]` and use `R` words each side as labels, giving `R × 2` classifications. `C = 10` in the experiments. Sampling `R` rather than fixing it is a **distance weighting in disguise** — distant words are used less often, so they contribute less, without an explicit weight term.

Both are log-linear: no non-linearity anywhere between input and output.

## Results

### The benchmark (§4.1)

**Semantic-Syntactic Word Relationship test set**: 5 semantic + 9 syntactic relation types, **8,869 semantic + 10,675 syntactic = 19,544 questions**, built by hand-listing similar word pairs and then crossing pairs within a type. Single-token words only. Scoring is **exact match on the single nearest vector by cosine** — synonyms count as errors, so 100% is unreachable.

> [!warning] The caveat inside the field's most-repeated result
> The search that produces the answer **discards the input question words**. `vec("king") − vec("man") + vec("woman")` returns `queen` only because `king`, `man` and `woman` are excluded from the nearest-neighbour search. Stated in one clause in §4 ("we discard the input question words during this search") and again in [paper 2](mikolov2013-distributed-representations-words-phrases.md) §3, and almost universally dropped when the result is repeated. It matters: the query vector's nearest neighbour is usually one of the inputs, so the exclusion is not a detail of the protocol but part of what makes it work. Cite the analogy result as evidence of *linear structure in the embedding space*, which it is, and not as evidence that the model performs the analogy, which it is not quite.

### Architecture comparison (Table 3 — 640-d, same 320M-word data)

| Architecture | Semantic [%] | Syntactic [%] | MSR relatedness |
|---|---|---|---|
| RNNLM | 9 | 36 | 35 |
| NNLM | 23 | 53 | 47 |
| **CBOW** | 24 | **64** | 61 |
| **Skip-gram** | **55** | 59 | 56 |

**The split is the finding.** CBOW wins syntax; Skip-gram wins semantics, by a factor of 2.3 over CBOW and 6 over the RNNLM. Averaging the context (CBOW) preserves local morphological signal; predicting outward from a single word (Skip-gram) forces each word's vector to carry information about the *company it keeps at range*, which is what a semantic relation is.

### Against everything published at the time (Table 4)

| Model | Dim | Train words | Semantic | Syntactic | Total |
|---|---|---|---|---|---|
| Collobert-Weston NNLM | 50 | 660M | 9.3 | 12.3 | 11.0 |
| Turian NNLM | 200 | 37M | 1.4 | 2.2 | 1.8 |
| Mnih NNLM | 100 | 37M | 3.3 | 13.2 | 8.8 |
| Mikolov RNNLM | 640 | 320M | 8.6 | 36.5 | 24.6 |
| Huang NNLM | 50 | 990M | 13.3 | 11.6 | 12.3 |
| Our NNLM | 100 | 6B | 34.2 | 64.5 | 50.8 |
| CBOW | 300 | 783M | 15.5 | 53.1 | 36.1 |
| **Skip-gram** | 300 | 783M | **50.0** | 55.9 | **53.3** |

Note the row that is easy to miss: **"Our NNLM" at 50.8% is a Bengio-style architecture, and it beats CBOW.** The new architectures do not win by being better models. They win by being cheap enough to train at a scale the better model cannot reach — Table 6 makes this explicit.

### The scaling result (Tables 2, 5, 6)

Table 2 (CBOW, 30k-vocab subset) sweeps dimensionality against data:

| Dim \ Train words | 24M | 49M | 98M | 196M | 391M | 783M |
|---|---|---|---|---|---|---|
| 50 | 13.4 | 15.7 | 18.6 | 19.1 | 22.5 | 23.2 |
| 100 | 19.4 | 23.1 | 27.8 | 28.7 | 33.4 | 32.2 |
| 300 | 23.2 | 29.2 | 35.3 | 38.6 | 43.7 | 45.9 |
| 600 | 24.0 | 30.1 | 36.5 | 40.8 | 46.6 | **50.4** |

**Neither axis alone works.** Going 50 → 600 dimensions at 24M words buys 10.6 points; going 24M → 783M words at 50 dimensions buys 9.8. Doing both buys 37. The paper's warning is aimed at contemporary practice: it was then common to train on large corpora with vectors of 50–100 dimensions, which the top two rows show saturating. This is a **compute-allocation** finding of the same shape as later scaling-law work, five years early and stated without the formalism.

Table 5 adds the training-budget version: **one epoch over 2× the data beats three epochs over 1×** (Skip-gram 300d: 53.8 on 1.6B × 1 epoch vs 53.3 on 783M × 3 epochs, and faster). Fresh data beats revisited data at equal cost.

Table 6, on DistBelief, is the headline efficiency claim:

| Model | Dim | Train words | Total acc. | Training cost |
|---|---|---|---|---|
| NNLM | 100 | 6B | 50.8 | **14 days × 180 cores** |
| CBOW | 1000 | 6B | 63.7 | 2 days × 140 cores |
| **Skip-gram** | 1000 | 6B | **65.6** | **2.5 days × 125 cores** |

### Sentence completion (Table 7)

On the MSR Sentence Completion Challenge, Skip-gram alone scores **48.0%** — worse than LSA similarity (49) and well under the RNNLM state of the art (55.4). Combined with RNNLMs it sets a new best at **58.9%**.

> [!note] The honest reading of Table 7
> Skip-gram is a *representation learner*, not a language model, and on a task that requires scoring a whole sentence it loses to models that are. Its value there is as a **complementary signal** in an ensemble — structurally the same finding as [Bengio et al. 2003](bengio2003-neural-probabilistic-language-model.md)'s "mixing with the trigram always helps." Two papers a decade apart, both reporting that their neural model's errors are uncorrelated with the incumbent's.

## Where the examples fail (Table 8)

Table 8 lists relationship examples from the best 300-d Skip-gram model. The paper notes it would score "only about 60%" under exact match — and the misses are in the table:

| Relationship | Given | Model output | Correct |
|---|---|---|---|
| `big − bigger` | `small` | **larger** | smaller |
| `copper − Cu` | `uranium` | **plutonium** | U |
| `Microsoft − Ballmer` | `IBM` | **McNealy** | Palmisano (McNealy was Sun) |
| `Japan − sushi` | `France` | **tapas** | (tapas is Spanish) |

Worth reading closely rather than skipping. The failure mode is consistent: the model returns something in the **right semantic neighbourhood and the wrong slot** — a metal for a metal, a tech CEO for a tech CEO, a national small-plate cuisine for another. That is exactly what you would predict from a geometry with no notion of *which* relation is being applied; the offset vector points in a plausible direction and lands near, not on. It is also the clearest available illustration for the wiki's recurring point that a learned metric encodes similarity without encoding **structure**.

## Training and infrastructure

- **Corpus**: Google News, ~6B tokens, vocabulary capped at the 1M most frequent words.
- **Optimization**: SGD + backprop, 3 epochs (later 1), initial learning rate **0.025** decayed linearly to zero.
- **Distributed**: DistBelief, **50–100 model replicas**, mini-batch asynchronous gradient descent, **Adagrad** adaptive learning rate. Roughly the same asynchronous-parameter-server design [Bengio et al. 2003](bengio2003-neural-probabilistic-language-model.md) §3.1 improvised on a 40-CPU Myrinet cluster, now a production system.
- **§7 follow-up**: single-machine multi-threaded C++ released, "billions of words per hour"; 1.4M named-entity vectors trained on 100B+ words published. This is `code.google.com/p/word2vec`.

## Entities mentioned

- **[Tomas Mikolov](../entities/tomas-mikolov.md)** — first author; the RNNLM work he is comparing against (Tables 3, 4, 7) is also his, from his Brno PhD.
- **[Jeff Dean](../entities/jeff-dean.md)** — co-author; DistBelief is his group's system, and the compute argument in Table 6 is the reason his name is on this paper.
- Kai Chen, Greg Corrado — co-authors, Google. No wiki pages.
- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — reference [1]; the NNLM whose hidden layer this paper deletes.
- **Geoff Zweig** — thanked for the MSR syntactic test set; co-author of the companion NAACL 2013 analogy paper, not ingested.
- **Collobert & Weston, Turian, Mnih, Huang** — the published-vectors baselines in Table 4.

## Concepts touched

- **[Distributed representations](../concepts/learning/distributed-representations.md)** — this paper is its scaling and measurement chapter.
- **[Perplexity](../glossary.md#perplexity)**, **[n-gram](../glossary.md#n-gram)**, **[hierarchical softmax](../glossary.md#hierarchical-softmax)**, **[CBOW](../glossary.md#cbow)**, **[Skip-gram](../glossary.md#skip-gram)**.
- **Scaling** — the dimensionality × data interaction in Table 2, and "one epoch on 2× data beats three on 1×."

## Open questions / TBD

- **Mikolov, Yih & Zweig (NAACL 2013), *Linguistic Regularities in Continuous Space Word Representations*** — the paper that actually introduced the offset method on RNNLM vectors, cited here as [20]. Un-ingested; it is the true origin of the analogy technique this paper popularized.
- **Levy & Goldberg's later analyses** — that Skip-gram with negative sampling implicitly factorizes a shifted PMI matrix, and that the analogy protocol's input-exclusion does much of the work — are the standard critical follow-ups and are not in this wiki.
- **The syntactic/semantic split between CBOW and Skip-gram** has no explanation offered here beyond the architectural asymmetry. Whether it survives at modern scale is untested in this wiki.
