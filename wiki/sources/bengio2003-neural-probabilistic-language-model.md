---
title: "A Neural Probabilistic Language Model (Bengio, Ducharme, Vincent, Jauvin, JMLR 2003)"
type: source
url: https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.html
fetch_url: https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf
local_path: raw/jmlr-2003-bengio-neural-probabilistic-language-model.pdf
sha256: 0bddf9a608d62da449a6413d86cbf6e8b206212595efe0e0a14da0d79d5f4976
author: Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Jauvin
affiliation: Département d'Informatique et Recherche Opérationnelle, Centre de Recherche Mathématiques, Université de Montréal
venue: "Journal of Machine Learning Research 3 (2003) 1137–1155; submitted 4/02, published 2/03"
published: 2003-02
ingested: 2026-08-30
tags: [language-model, word-embeddings, distributed-representations, curse-of-dimensionality, bengio, montreal, jmlr-2003, foundational, n-gram, perplexity, softmax, energy-based]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/jmlr-2003-bengio-neural-probabilistic-language-model.pdf`, 19 pages, JMLR pp. 1137–1155). Pages 1–17 read in full (motivation, architecture, parallel implementation, experiments, extensions, conclusion). Pages 17–19 are references, skimmed. Both results tables were re-extracted in layout mode to recover column alignment.

## Summary

**"A Neural Probabilistic Language Model"** — Bengio, Ducharme, Vincent & Jauvin (Université de Montréal; JMLR 3:1137–1155, 2003; the NIPS 2000 workshop version predates it). **The paper that introduced learned word embeddings and the neural language model.** Its thesis: statistical language modeling fails because of the **curse of dimensionality** over a discrete space — with a 100,000-word vocabulary, a joint model over 10 consecutive words has `100000^10 − 1 ≈ 10^50 − 1` free parameters, and any two word sequences are nearly maximally far apart in Hamming distance. `n`-gram models dodge this by gluing together short overlapping fragments seen in training, which generalizes only to sequences made of *seen* fragments.

The proposal is three sentences long and has not changed since:

1. Associate each word in the vocabulary with a **distributed feature vector** in `R^m` (`m` = 30, 60, or 100 here, against `|V|` ≈ 17,000).
2. Express the joint probability of a word sequence in terms of those feature vectors.
3. **Learn the feature vectors and the probability function simultaneously**, by maximum likelihood.

Generalization then comes for free from smoothness: because the probability function is a smooth function of the feature vectors, seeing *"The cat is walking in the bedroom"* raises the probability of *"A dog was running in a room"* — and of a combinatorial number of other neighbors in sentence space — provided `dog`/`cat`, `the`/`a`, `bedroom`/`room` land near each other. §1.1 states this as fighting "the curse of dimensionality with its own weapons: each training sentence informs the model about a combinatorial number of other sentences."

**Headline results.** On the Brown corpus, test perplexity **252** for the best neural model versus **336** for a deleted-interpolation trigram (33% worse) and **312** for the best `n`-gram of any kind (a 500-class class-based trigram, 24% worse). On AP News (14M words), **109** versus **117** for the best modified-Kneser-Ney back-off. The neural model also benefits from *longer* context where the `n`-grams do not.

**Why it matters to this wiki.** This is where the embedding table comes from. Every model in this wiki that maps a discrete symbol to a learned vector — LLM token embeddings, [VLA](../concepts/learning/vla-models.md) action tokenizers, [VQ-BeT](../entities/vq-bet.md)'s codebook, [latent action tokens](../concepts/learning/latent-action-tokens.md), the `[CLS]` token in a [ViT](../glossary.md#vit) — is running the mapping `C` defined in §2 of this paper. It is the direct ancestor of word2vec (2013), and through it of the entire "pretrain representations, then use them" program. It is also the paper that made **softmax over a large vocabulary** the central computational problem of language modeling, and then listed, in §5.2, most of the ways the field would go on to solve it.

> [!note] Provenance
> Fetched from JMLR's canonical PDF (`fetch_url` above) on 2026-08-30, not from a secondary summary. JMLR volume 3 is a static archive and unlikely to be revised in place, but the `fetch_url` is set so `check_source_drift.py --check` covers it anyway.

## Abstract (verbatim)

> "A goal of statistical language modeling is to learn the joint probability function of sequences of words in a language. This is intrinsically difficult because of the *curse of dimensionality*: a word sequence on which the model will be tested is likely to be different from all the word sequences seen during training. Traditional but very successful approaches based on n-grams obtain generalization by concatenating very short overlapping sequences seen in the training set. We propose to fight the curse of dimensionality by learning a distributed representation for words which allows each training sentence to inform the model about an exponential number of semantically neighboring sentences. The model learns simultaneously (1) a distributed representation for each word along with (2) the probability function for word sequences, expressed in terms of these representations. Generalization is obtained because a sequence of words that has never been seen before gets high probability if it is made of words that are similar (in the sense of having a nearby representation) to words forming an already seen sentence. Training such large models (with millions of parameters) within a reasonable time is itself a significant challenge. We report on experiments using neural networks for the probability function, showing on two text corpora that the proposed approach significantly improves on state-of-the-art n-gram models, and that the proposed approach allows to take advantage of longer contexts."

## The problem it names (§1)

A language model factorizes as `P̂(w_1^T) = Π_t P̂(w_t | w_1^{t-1})`. `n`-grams approximate the conditioning set by truncation, `P̂(w_t | w_1^{t-1}) ≈ P̂(w_t | w_{t-n+1}^{t-1})`, and handle unseen combinations by backing off to shorter contexts ([Katz 1987](https://doi.org/10.1109/TASSP.1987.1165125)) or interpolating them (Jelinek & Mercer 1980).

The paper's diagnosis of that family, in §1, is two-pronged and worth keeping separate:

1. **Context length.** Trigrams see two words. Even reported 5-grams mostly fall back to shorter contexts because of data scarcity (their footnote 1).
2. **No notion of word similarity.** The generative story behind a back-off `n`-gram is "glue together short, frequently-seen fragments." Nothing in it can transfer mass from `cat` to `dog`.

Their framing of generalization is the useful one: think of probability mass initially concentrated on training points and then spread into a surrounding volume. *"In high dimensions, it is crucial to distribute probability mass where it matters rather than uniformly in all directions around each training point."* The contribution is a different — and learned — choice of where "it matters."

> [!note] The continuous/discrete asymmetry — an [inductive-bias](../concepts/learning/inductive-bias.md) argument
> §1's opening argument is the one to carry forward: for **continuous** variables, generalization comes cheaply because smooth function classes (MLPs, Gaussian mixtures) have local smoothness we can exploit. For **discrete** spaces there is no such structure — any change to a discrete variable can change the target arbitrarily, and with large alphabets every observation is nearly maximally far from every other. The whole paper is a device for *manufacturing* a continuous space in which smoothness is available. That reframing recurs whenever this wiki discretizes something (action bins, VQ codebooks) and then has to reintroduce a metric.

## The model (§2)

Decompose `f(w_t, …, w_{t−n+1}) = P̂(w_t | w_1^{t−1})` into two mappings:

1. **`C`** — a `|V| × m` matrix of free parameters. Row `i` is the feature vector `C(i) ∈ R^m` for word `i`. This is a lookup table, and it is the paper's central object.
2. **`g`** — maps the concatenated feature vectors of the context to a distribution over the next word.

Shared across all context positions: **the same `C` is applied to every input word.** The paper is explicit that this parameter sharing across time is the difference from their earlier (Bengio & Bengio 2000) work on joint distributions over heterogeneous discrete variables.

The concrete network:

```
x = ( C(w_{t−1}), C(w_{t−2}), …, C(w_{t−n+1}) )      # concatenated context features
y = b + W x + U tanh( d + H x )                      # (equation 1)
P̂(w_t | context) = exp(y_{w_t}) / Σ_i exp(y_i)       # softmax
```

- `h` — hidden units; `m` — features per word; `n` — model order (context is `n−1` words).
- `W` (`|V| × (n−1)m`) are **optional direct connections** from the word-feature layer straight to the output; set to 0 to remove them.
- `U` (`|V| × h`) hidden-to-output, `H` (`h × (n−1)m`) hidden weights, `b`/`d` biases.
- `θ = (b, d, W, U, H, C)`.

Two hidden layers in effect: the **word-features layer `C`, which is deliberately linear** (a non-linearity there "would not add anything useful"), and the ordinary `tanh` layer.

**Parameter count: `|V|(1 + nm + h) + h(1 + (n−1)m)`, dominated by `|V|(nm + h)`.** The point being made is that this is **linear in `|V|` and linear in `n`** — against the `n`-gram's exponential blow-up. The paper notes the scaling in `n` could be made sub-linear with a time-delay or recurrent network, and does not do it.

Training is plain **stochastic gradient ascent** on the penalized log-likelihood `L = (1/T) Σ_t log f(·; θ) + R(θ)`, with `R` a weight decay applied to network weights and `C` but not to biases. Note their aside: with weight decay on `W` and `H` but not on `C`, in theory `W`/`H` could collapse to zero while `C` blows up — they report not observing it.

**Mixture with a trigram.** Reported throughout as a separate axis (`mix` column in the tables): averaging the neural network's output probabilities with an interpolated trigram's, at fixed weight 0.5, *always* helps. Their reading — the two model families make their errors in different places — is the first appearance in this wiki's lineage of "the neural model and the count model are complementary," which is still true of retrieval-augmented and hybrid systems.

## The compute problem, and the 2003 answer (§3)

The parameter count scales nicely; the **computation does not**, and the reason is specific: an `n`-gram can produce `P(w_t | context)` for one word without touching the rest of the vocabulary, because normalization is done at training time. The neural model must evaluate the whole output layer to normalize.

They quantify it for the AP News architecture (`|V| = 17,964`, `h = 60`, `n = 6`, `m = 100`): **≈ 99.7% of the per-example arithmetic is the output layer's weighted sums.** That single number is why the next fifteen years of language-modeling systems work went into the softmax.

Their answer was parallelism, on two platform types:

- **Data-parallel (shared-memory).** Each processor takes a different subset of examples and writes updates into shared memory. Their first, lock-based implementation was "extremely slow" — most cycles spent waiting on write locks. They switched to an **asynchronous, unsynchronized** version where updates are sometimes silently overwritten by other processors, and report the resulting noise did not measurably slow training. (This is Hogwild!, eight years before Hogwild!.)
- **Parameter-parallel (cluster).** Exchanging ~100 MB of parameters over a LAN per step is impossible, so they partition the **output units** across CPUs. Each CPU owns a contiguous block of the vocabulary, computes unnormalized scores for it, and the machines exchange only (1) the softmax normalization constant, via an MPI `Allreduce`, and (2) the gradients w.r.t. the hidden layer `a` and the word-feature layer `x`. All CPUs redundantly duplicate the pre-output computation — which is 0.3% of the work, so it doesn't matter. Communication overhead measured at **1/15 of total epoch time** — "almost perfect speed-up."

Hardware: **32 dual-CPU 1.2 GHz Athlon machines on a Myrinet network, using MPI.** For slow networks they sketch a mini-batch variant that trades convergence rate for communication latency.

> [!note] The compute anecdote worth remembering
> The AP News result — 5 epochs over 14M words — took **about three weeks on 40 CPUs**, and they never saw overfitting because they could not afford to run longer. The best model in the paper is undertrained for budget reasons. The idea was not compute-feasible at its own publication date; it needed roughly a decade of hardware.

## Experiments (§4)

**Brown corpus** — 1,181,041 words. 800,000 train / 200,000 validation / 181,041 test. 47,578 distinct tokens (case-sensitive, punctuation and paragraph marks included); words with frequency ≤ 3 merged into one symbol, giving `|V| = 16,383`.

**AP News (1995–1996)** — 13,994,528 train / 963,138 validation / 963,071 test. 148,721 distinct words reduced to `|V| = 17,964` by keeping the most frequent, lower-casing, and mapping numerics, rare words, and proper nouns to special symbols.

Optimization: initial learning rate `ε_0 = 10^−3`, decayed as `ε_t = ε_0 / (1 + rt)` with `r = 10^−8` and `t` the number of updates. Weight decay `10^−4` (Brown) and `10^−5` (AP). Early stopping on validation, needed only on Brown. Word features **randomly initialized** — they explicitly suspect knowledge-based initialization would do better, and never test it.

Metric throughout is **perplexity**, the geometric mean of `1/P̂(w_t | w_1^{t−1})` — equivalently `exp` of average negative log-likelihood. End-of-sentence tokens get no special status, for the neural model and the baselines alike; all tokens are averaged the same way. Back-off baselines computed with the SRILM toolkit (Stolcke 2002).

### Table 1 — Brown corpus

| Model | `n` | `c` | `h` | `m` | direct | mix | train | valid | **test** |
|---|---|---|---|---|---|---|---|---|---|
| MLP1 | 5 | | 50 | 60 | yes | no | 182 | 284 | 268 |
| MLP2 | 5 | | 50 | 60 | yes | yes | | 275 | 257 |
| MLP3 | 5 | | 0 | 60 | yes | no | 201 | 327 | 310 |
| MLP4 | 5 | | 0 | 60 | yes | yes | | 286 | 272 |
| MLP5 | 5 | | 50 | 30 | yes | no | 209 | 296 | 279 |
| MLP6 | 5 | | 50 | 30 | yes | yes | | 273 | 259 |
| MLP7 | 3 | | 50 | 30 | yes | no | 210 | 309 | 293 |
| MLP8 | 3 | | 50 | 30 | yes | yes | | 284 | 270 |
| MLP9 | 5 | | 100 | 30 | no | no | 175 | 280 | 276 |
| **MLP10** | 5 | | 100 | 30 | no | yes | | **265** | **252** |
| Deleted interpolation | 3 | | | | | | 31 | 352 | 336 |
| Kneser-Ney back-off | 3 | | | | | | | 334 | 323 |
| Kneser-Ney back-off | 4 | | | | | | | 332 | 321 |
| Kneser-Ney back-off | 5 | | | | | | | 332 | 321 |
| class-based back-off | 3 | 150 | | | | | | 348 | 334 |
| class-based back-off | 3 | 200 | | | | | | 354 | 340 |
| **class-based back-off** | 3 | **500** | | | | | | 326 | **312** |
| class-based back-off | 3 | 1000 | | | | | | 335 | 319 |
| class-based back-off | 3 | 2000 | | | | | | 343 | 326 |
| class-based back-off | 4 | 500 | | | | | | 327 | 312 |
| class-based back-off | 5 | 500 | | | | | | 327 | 312 |

(`c` = number of word classes for class-based `n`-grams; `m` = word-feature dimension for MLPs. All back-off models are **modified** Kneser-Ney, which the authors note beat standard back-off substantially.)

**336 / 252 = 1.33** (33% above the best-validation neural model) and **312 / 252 = 1.24** (24% above, versus the best `n`-gram of any kind).

Four readings the table supports:

- **Hidden units matter.** MLP3/MLP4 (`h = 0`) are 42 and 15 perplexity worse than their `h = 50` counterparts. The linear embedding layer alone is not enough.
- **Longer context helps the neural model and not the `n`-grams.** MLP7 (`n = 3`) → MLP5 (`n = 5`) improves 293 → 279; Kneser-Ney flatlines at 323/321/321 going from trigram to 5-gram. This is the paper's second headline claim and it is visible directly in the table.
- **Mixing with the trigram always helps** — every `mix = yes` row beats its `mix = no` twin.
- **Direct connections are a wash on quality, and a real difference in training time.** MLP9/MLP10 (no direct connections) reach the *lowest* perplexities but took 20 epochs instead of 10. The authors' hedge is worth quoting: direct connections "provide a bit more capacity and faster learning of the 'linear' part of the mapping," while removing them makes the hidden units "a tight bottleneck which might force better generalization." They explicitly decline to call it.

> [!note] The `n`-gram train-perplexity row
> Deleted interpolation trains to perplexity **31** and tests at **336** — an order of magnitude gap. The best neural model's train/valid gap is far smaller (MLP9: 175/280). The count model is memorizing; the neural model, on 800k words, is not. That contrast is the paper's cleanest single piece of evidence and it goes unremarked in the text.

### Table 2 — AP News corpus

| Model | `n` | `h` | `m` | direct | mix | valid | **test** |
|---|---|---|---|---|---|---|---|
| **MLP10** | 6 | 60 | 100 | yes | yes | 104 | **109** |
| Deleted interpolation | 3 | | | | | 126 | 132 |
| Back-off KN | 3 | | | | | 121 | 127 |
| Back-off KN | 4 | | | | | 113 | 119 |
| Back-off KN | 5 | | | | | 112 | 117 |

Class-based models did not help here; the high-order modified Kneser-Ney was the best count baseline. Only **5 epochs** were run (≈ three weeks, 40 CPUs) and no overfitting was visible on validation.

> [!note] Arithmetic check on the "8%" claim
> §4.2 states the AP News gap as "about 8%". The table gives 117 vs 109, which is **7.3%** relative to the neural model (6.8% relative to the `n`-gram). The Brown figures (24% and 33%) reproduce exactly. The 8% is a rounding of the 7.3%, not a different comparison — but the §6 conclusion widens it further to "differences between 10 and 20% in perplexity," which **neither table supports** for AP News. Cite the tables, not the conclusion paragraph.

## §5.1 — The energy-minimization variant

A variant the authors implemented and reported on separately. Following Hinton's products of experts (2000), give the **output** word a feature vector too — not just the inputs — and have the network emit a scalar energy:

```
E(w_{t−n+1}, …, w_t) = v · tanh( d + H x ) + Σ_{i=0}^{n−1} b_{w_{t−i}}
x = ( C(w_t), C(w_{t−1}), …, C(w_{t−n+1}) )          # note C(w_t) is now in the input
P̂(w_t | context) = e^{−E(…, w_t)} / Σ_i e^{−E(…, i)}
```

Low energy ↔ likely subsequence. In the products-of-experts reading, each hidden unit `j` is an expert contributing `v_j tanh(d_j + H_j x)`. The paper points out that because they factorize the sequence probability into per-element conditionals, **the gradient stays tractable** — unlike products-of-HMMs, which need contrastive divergence. It also frames the architecture as an extension of **maximum-entropy models** (Berger et al. 1996) in which the basis functions are learned jointly with their linear combination rather than selected greedily in an outer loop.

Two things follow from it:

- **Out-of-vocabulary words get a probability.** For an unseen word `j` in context, initialize `C(j) ← Σ_{i∈V} C(i) P̂(i | w_{t−n+1}^{t−1})` — a probability-weighted convex combination of the feature vectors of words that *could* have appeared there — then renormalize over the enlarged vocabulary. A neat trick, and one that only exists because the output side has an embedding.
- **A 100× training speed-up** via importance sampling, in the companion paper (Bengio & Senécal, AISTATS 2003).

This connects the paper to the wiki's [energy-based models](../concepts/learning/energy-based-models.md) thread from an unexpected direction: it is the **earliest EBM-for-sequences construction in this wiki**, and it is Bengio's, not [LeCun](../entities/yann-lecun.md)'s. It also foreshadows tied input/output embeddings, standard in LLMs two decades later.

## §5.2 — The future-work list, which is the field's next fifteen years

Reading this section in 2026 is the reason to read the paper. Six items:

1. **Decompose into sub-networks via word clustering** — smaller, faster networks.
2. **Tree-structured conditional probability**, a network per node, classes at internal nodes and words at leaves, for a **`|V| / log|V|` speed-up** → **hierarchical softmax**, and the standard trick in word2vec.
3. **Propagate gradients from only a subset of output words**, chosen by a fast model such as a trigram, or by where the trigram is weak; if coupled to a speech recognizer, only acoustically ambiguous words need scoring. Plus importance sampling (Bengio & Senécal 2003) → **negative sampling / sampled softmax / NCE**.
4. **Introduce prior knowledge** — WordNet, parts of speech, stochastic grammars — and capture longer-term context "by introducing more structure and parameter sharing in the neural network, e.g. using time-delay or **recurrent** neural networks," noting that a multi-layer network need not recompute overlapping windows → **RNN-LM (Mikolov 2010), and the sliding-window inefficiency argument that later motivates the KV cache**.
5. **Interpret the learned word representations**, starting with `m = 2` for plottability, with the caveat that "more meaningful representations will require large training corpora" → **word2vec's analogy structure (2013), t-SNE embedding plots, and every mechanistic-interpretability probe since**.
6. **Polysemy** — "each word is associated with a single point in a continuous semantic space," which the authors say is probably wrong, and they are "investigating extensions of this model in which each word is associated with multiple points in that space, each associated with the different senses of the word" → **contextual embeddings: ELMo, BERT, and the entire premise that a token's representation should depend on its context**.

Items 2, 3, 5 and 6 name, in 2003, four of the largest subsequent results in the field. The one thing not on the list is **attention** — and item 4's answer to long context is recurrence, which is exactly the answer [Vaswani et al. 2017](attention-is-all-you-need.md) would discard.

## What the paper does not have

- **No attention, and no recurrence in the actual model.** The context window is fixed at `n − 1` = 2 to 5 words. Everything about long-range dependency is deferred to future work.
- **No transfer.** The embeddings are trained end-to-end for one task on one corpus and used for that task. The "pretrain the representation, then reuse it elsewhere" move — which is the whole value of embeddings today — is not proposed. word2vec's contribution was substantially this.
- **No scale, and no scaling claim.** Largest vocabulary is ~18,000 words; largest corpus 14M words; largest model well under 10M parameters. Nothing in the paper predicts that the same recipe keeps improving for six more orders of magnitude.
- **No subword tokenization.** Rare words are merged into a single symbol or dropped by frequency; proper nouns are mapped to one token. BPE/WordPiece exists to make that hack unnecessary.
- **No efficient softmax.** Identified as the bottleneck (99.7% of compute), quantified, addressed with a cluster, and left to future work.

## Entities mentioned

- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — first author; Université de Montréal.
- **Réjean Ducharme, Christian Jauvin** — co-authors, Université de Montréal. No wiki pages; this is their principal appearance in the wiki's lineage.
- **Pascal Vincent** — co-author; later first author of the denoising-autoencoder line and a long-running Bengio collaborator, subsequently at Meta FAIR. No wiki page yet.
- **[Geoffrey Hinton](../entities/geoffrey-hinton.md)** — cited three ways: the 1986 distributed-representations-of-concepts paper as the acknowledged origin of the idea; products of experts / contrastive divergence (2000) as the framing for §5.1; and thanked in the acknowledgments.
- **[Yann LeCun](../entities/yann-lecun.md)** — thanked in the acknowledgments (with Léon Bottou and Hinton); *Efficient BackProp* (LeCun et al. 1998) cited for the batch-vs-stochastic-gradient argument in §3.2.
- **Jürgen Schmidhuber** — cited for neural character-level text compression (1996), a direct precursor.
- **Jeffrey Elman** — *Finding Structure in Time* (1990), cited as connectionist prior art on distributed representations for symbolic data.

## Concepts touched

- **[Distributed representations](../concepts/learning/distributed-representations.md)** — the concept page this ingest creates; this paper is its primary reference for the learned-embedding form.
- **[Energy-based models](../concepts/learning/energy-based-models.md)** — §5.1's energy-minimization variant, the earliest EBM-for-sequences construction in the wiki.
- **[Embedding / Latent](../glossary.md#embedding--latent)** — the glossary's substrate notion; `C` is its origin.
- **[Perplexity](../glossary.md#perplexity)** — defined operationally here (geometric mean of `1/P̂`), added to the glossary by this ingest.
- **[VLA models](../concepts/learning/vla-models.md)** / **[latent action tokens](../concepts/learning/latent-action-tokens.md)** — descendants: a discrete action vocabulary with a learned lookup table is exactly `C` with actions substituted for words.
- **[Inductive bias](../concepts/learning/inductive-bias.md)** — the whole paper is one, and an unusually instructive one because the bias is *not* architectural: they manufacture a continuous space in which smoothness becomes a usable assumption, rather than constraining the model.
- **Curse of dimensionality** — the paper's organizing frame; used loosely elsewhere in the wiki, defined precisely here.

## Position in the lineage

```
Hinton 1986 (distributed representations of concepts)
Elman 1990 (finding structure in time)
Bengio & Bengio 2000 (NN for joint distributions over discrete variables)
   ↓
Bengio et al. 2003 — A Neural Probabilistic Language Model  (this paper)
   │   learned embedding table C + MLP + softmax; §5.2 names what comes next
   ↓
Mikolov 2010 (RNN-LM)                    ← §5.2 item 4
Hierarchical softmax / NCE / sampling    ← §5.2 items 2, 3
word2vec 2013 (embeddings as a reusable artifact; analogy structure)  ← §5.2 item 5
   ↓
Attention Is All You Need 2017 (attention replaces recurrence; embedding table survives unchanged)
   ↓
BERT / ELMo (contextual embeddings)      ← §5.2 item 6
GPT-line LLMs
   ↓
Everything in this wiki with a token embedding:
- LLM trunks inside every VLA
- VQ-BeT codebooks, latent action tokens
- discrete action bins in RT-2-style VLAs
- ViT patch projections (the continuous-input analogue of C)
```

The through-line is narrow and exact: **`C` never went away.** Attention replaced the `g` half of this paper's decomposition. The `C` half — a learned `|V| × m` lookup table trained jointly with the task — is unchanged in 2026, up to tying it with the output layer and swapping words for subwords.

## Curriculum hookup

Belongs in **[Module 3 — Sequence models, attention, and transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)**, §1 ("Sequence models before attention"), which currently starts at RNNs and so skips the origin of the embedding table that §2 onward silently assumes. Also relevant to **[Module 1](../syntheses/curriculum/curriculum-01-neural-networks.md)** as an unusually legible worked example: an MLP, a softmax, SGD with a decayed learning rate, weight decay, early stopping, and a train/valid/test split — with every hyperparameter and every number reported.

## Open questions / TBD

- **word2vec (Mikolov et al. 2013) is not ingested**, and it is the missing link between this paper and modern practice — specifically the move from "embeddings are a byproduct of an LM" to "embeddings are the product." A short ingest would close the largest gap in the wiki's representation-learning lineage.
- **The `m = 2` interpretability experiment in §5.2 item 5 was never run in this paper.** Its eventual answer (the `king − man + woman` analogy structure) is one of the field's most-repeated results and the wiki has no source for it.
- **Whether the mixture-with-a-trigram finding has a modern analogue.** Averaging a parametric model with a count-based one always helped here; the modern descendants are retrieval augmentation and `k`NN-LM. Untracked in this wiki.
- **The Hogwild!-before-Hogwild! observation in §3.1** — lossy asynchronous SGD updates costing nothing measurable — predates Niu et al. 2011 by eight years and is uncited by it as far as this ingest can tell. Worth a check if a distributed-training thread ever opens here.
