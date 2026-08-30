---
title: Distributed representations (learned embeddings)
type: concept
created: 2026-08-30
updated: 2026-08-30
sources: 5
tags: [distributed-representations, word2vec, cbow, skip-gram, negative-sampling, embeddings, word-embeddings, lookup-table, curse-of-dimensionality, tokenization, bengio, foundational]
---

**A distributed representation** encodes an item as a **pattern of activity across many units** rather than as a single dedicated unit. Its opposite is a **local** (or "one-hot", "symbolic") representation, where each item owns one unit and no two items share anything.

The practical form this takes in every model in this wiki: a **learned lookup table** `C`, a `|V| × m` matrix mapping each of `|V|` discrete symbols to a vector in `R^m`, with `m ≪ |V|`, whose entries are **free parameters trained by gradient descent alongside the task that consumes them**. Row `i` is the item's embedding.

## Why it exists: the discrete-space generalization problem

The argument is [Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md) §1, and it is worth stating precisely because the wiki uses "curse of dimensionality" loosely elsewhere:

- For **continuous** inputs, generalization is cheap. Smooth function classes have local smoothness, so a model that fits `f(x)` also approximately fits `f(x + ε)`.
- For **discrete** inputs there is no such structure. Any change to a discrete variable can change the target arbitrarily, and when the alphabet is large, **every observation is nearly maximally far from every other in Hamming distance.** A joint model over 10 words from a 100,000-word vocabulary has `100000^10 − 1 ≈ 10^50 − 1` free parameters, and the test sequence is almost certainly one you never saw.

A one-hot representation makes this concrete: `cat` and `dog` are exactly as dissimilar as `cat` and `the`. Nothing learned about one can transfer to the other.

The fix is not to generalize better over the discrete space but to **manufacture a continuous space in which smoothness is available**, and learn the map into it. Then a smooth probability function over embeddings transfers mass automatically: `The cat is walking in the bedroom` raises the likelihood of `A dog was running in a room`, and of a combinatorial number of other neighbors, because the words sit near each other and the function is smooth. Bengio et al.'s phrasing — fighting the curse of dimensionality "with its own weapons" — is that **each training example informs the model about an exponential number of unseen ones.**

The counting argument is the other half. A count-based model over `n`-grams needs parameters exponential in `n`; a model factored through `C` needs `|V|(1 + nm + h) + h(1 + (n−1)m)` — **linear in vocabulary size and linear in context length.**

## The two properties that matter downstream

1. **Similarity becomes a metric, and it is learned.** The embedding space acquires a geometry nobody specified, driven only by the task objective. This is what makes embeddings reusable — the geometry survives being taken out of the model that produced it.
2. **The table is jointly trained, not fitted separately.** [Bengio et al.](../../sources/bengio2003-neural-probabilistic-language-model.md) tried the alternative — fixing word features to the principal components of co-occurrence counts, in the style of Latent Semantic Indexing — and report it **unsuccessful**. Joint training with the consuming task is load-bearing, not a convenience. That finding recurs whenever this wiki compares a frozen pretrained encoder against one tuned with its policy.

## Where it shows up in this wiki

Every one of these is `C` with a different alphabet substituted for words:

- **LLM token embeddings** — the trunk of every [VLA](vla-models.md). Unchanged in form since 2003, up to subword tokenization and tying the input table to the output layer.
- **Discrete action bins** — RT-2-style VLAs that emit actions as text tokens are embedding actions through the language model's own table.
- **[VQ-BeT](../../entities/vq-bet.md) codebooks and [latent action tokens](latent-action-tokens.md)** — a learned codebook over action primitives; the codebook *is* an embedding table, and the recurring complaint that latent action tokens are unreadable is a restatement of "the geometry is learned, so nobody specified what the axes mean."
- **[Soft-prompt cross-embodiment conditioning](soft-prompt-cross-embodiment.md)** — a learned vector per data source, injected early. A `|sources| × m` table, trained jointly. The finding that the prompts encode *configuration similarity* rather than dataset identity is exactly property (1) above, observed in a robotics setting.
- **[ViT](../../glossary.md#vit) patch projection** — the continuous-input analogue: a linear map into the same kind of space, with no lookup because the input is already a vector.
- **[Embedding / latent](../../glossary.md#embedding--latent) generally** — the substrate [JEPA](../world-models/jepa.md)-family models predict in. JEPA's bet is that *prediction should happen in this space rather than in the input space*, which presupposes the space is worth having.

> [!note] What the wiki still calls "the tokenization problem"
> Several pages here treat the choice of action vocabulary as a design problem with no clean answer. This concept page is the reason it has no clean answer: a discrete vocabulary buys a tractable softmax and loses the metric, and the embedding table is the machinery for buying the metric back. Whether that works depends on whether the task's objective is rich enough to shape a useful geometry — which is why [LIBERO-PRO](../../sources/libero-pro-paper.md)-style perturbation tests matter more than benchmark scores for judging it.

## What word2vec added, and what it cost

[Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md) established the object. **[word2vec](../../sources/mikolov2013-efficient-estimation-word-representations.md) (2013) made it a product and made its geometry measurable**, which are separate contributions and both matter here.

**Measurable.** Before 2013, embedding quality was argued from cherry-picked nearest-neighbour tables — a complaint Mikolov et al. open their results section with. The **analogy benchmark** (19,544 questions over 5 semantic and 9 syntactic relation types) turned "the geometry means something" from an impression into a number: `vec("biggest") − vec("big") + vec("small")` lands nearest `smallest`. [Figure 2 of the NIPS paper](../../sources/mikolov2013-distributed-representations-words-phrases.md) — country–capital pairs forming parallel offsets in a PCA projection, with no supervision about what a capital is — is the image that convinced the field.

> [!warning] Two caveats that belong with the analogy result every time it is cited
> **The nearest-neighbour search excludes the input words.** `king − man + woman → queen` works partly because `king`, `man` and `woman` are removed from the candidate set; the query vector's true nearest neighbour is usually one of them. Stated in one clause in both papers and dropped almost everywhere else. The result is evidence of **linear structure in the space**, not evidence that the model performs analogical reasoning.
>
> **The published examples include visible failures.** Table 8 of [2013a](../../sources/mikolov2013-efficient-estimation-word-representations.md) offers `big − bigger → small: larger` (should be *smaller*), `copper − Cu → uranium: plutonium`, `Microsoft − Ballmer → IBM: McNealy` (McNealy was Sun), `Japan − sushi → France: tapas` (Spanish). The paper concedes ~60% exact-match on its own showcase table. The failure mode is diagnostic: the model returns something in the **right neighbourhood and the wrong slot** — a metal for a metal, a tech CEO for a tech CEO. A learned metric encodes *similarity* without encoding *which relation is being applied*.

**A product.** The 2003 embeddings were internal to one model on one corpus. word2vec shipped C code and pretrained vectors over 100B+ words, including 1.4M named entities. That distribution step — not the architecture — is why the technique became ubiquitous, and it is the moment the field's default changed from *train a representation for your task* to *download one and fine-tune*.

**The cost of the architecture.** CBOW and Skip-gram get their speed by deleting the NNLM's non-linear hidden layer, and [Table 4](../../sources/mikolov2013-efficient-estimation-word-representations.md) is honest that this is a downgrade: a Bengio-style NNLM at 6B words scores **50.8%**, beating CBOW's 36.1%. The log-linear models win by being cheap enough to train at a scale the better model cannot reach. **The embedding table survived; the model around it was sacrificed to scale.**

### Additive compositionality has a mechanism

`vec("Russia") + vec("river") ≈ vec("Volga River")`; `vec("Vietnam") + vec("capital") ≈ Hanoi`. [The NIPS paper](../../sources/mikolov2013-distributed-representations-words-phrases.md) §5 explains why, and the explanation constrains how far the intuition travels: word vectors enter the softmax **linearly**, so their components are **logarithmically** related to output probabilities; summing vectors therefore corresponds to **multiplying context distributions**, and a product acts as **AND**. Words scored highly by both survive.

This is specific to a log-linear model with a softmax output. It is not a general property of learned embedding spaces, and it should not be assumed of an action codebook or a JEPA latent.

## Key references

- **[Bengio, Ducharme, Vincent & Jauvin 2003 — A Neural Probabilistic Language Model](../../sources/bengio2003-neural-probabilistic-language-model.md)** — the primary reference for the *learned, jointly-trained* form. Proposes the three-step recipe (a feature vector per word; a probability function over feature vectors; learn both at once), reports the LSI-style fixed-features failure, and demonstrates it beating the best `n`-gram language models of its day by 24% perplexity on Brown.
- **[Mikolov et al. 2013a — Efficient Estimation of Word Representations](../../sources/mikolov2013-efficient-estimation-word-representations.md)** — CBOW / Skip-gram, the analogy benchmark, and the dimensionality-vs-data scaling table.
- **[Mikolov et al. 2013b — Distributed Representations of Words and Phrases](../../sources/mikolov2013-distributed-representations-words-phrases.md)** — negative sampling, subsampling, phrase vectors, additive compositionality.
- **[Sutskever, Vinyals & Le 2014 — Sequence to Sequence Learning](../../sources/sutskever2014-sequence-to-sequence-learning.md)** — extends the idea from words to whole **sentences**: the encoder's final state is a sentence embedding, and its PCA clusters by meaning and word order.
- **[Attention Is All You Need (Vaswani et al. 2017)](../../sources/attention-is-all-you-need.md)** — replaced the *consuming* half of the 2003 decomposition and left the embedding table untouched.
- **Hinton 1986**, *Learning distributed representations of concepts* — the idea's origin, cited by Bengio et al. as prior art; not ingested. **Elman 1990**, *Finding structure in time* — likewise.

## Related concepts

- [Energy-based models](energy-based-models.md) — §5.1 of the 2003 paper gives the output word an embedding too and emits a scalar energy; that construction is where tied input/output embeddings come from.
- [Latent action tokens](latent-action-tokens.md), [Soft-prompt cross-embodiment conditioning](soft-prompt-cross-embodiment.md) — robotics-side instances.
- [VLA models](vla-models.md) — the consumers.
- [Latent space](../world-models/latent-space.md) — what the representation is a representation *in*.

## Current state

Settled, and invisible because settled. No modern architecture argues about whether to use a learned embedding table; the arguments moved to what the alphabet should be (subword tokenization, action discretization, VQ codebook size), whether the input and output tables should be tied, and whether the representation should be **contextual** rather than fixed per symbol — the last of which was [Bengio et al.'s own §5.2 item 6](../../sources/bengio2003-neural-probabilistic-language-model.md), listed in 2003 as future work and answered by ELMo/BERT fifteen years later.

The open frontier in this wiki is not language but **action**: what the right vocabulary is for a robot's outputs, and whether a learned table over it produces a geometry that generalizes across embodiments. [Latent action tokens](latent-action-tokens.md) is the current best attempt, with one source and no independent replication.

## Mentioned in

- [Bengio et al. 2003 — A Neural Probabilistic Language Model](../../sources/bengio2003-neural-probabilistic-language-model.md)
- [Mikolov et al. 2013a — Efficient Estimation of Word Representations in Vector Space](../../sources/mikolov2013-efficient-estimation-word-representations.md)
- [Mikolov et al. 2013b — Distributed Representations of Words and Phrases](../../sources/mikolov2013-distributed-representations-words-phrases.md)
- [Sutskever, Vinyals & Le 2014 — Sequence to Sequence Learning](../../sources/sutskever2014-sequence-to-sequence-learning.md)
- [Karpathy — Software 3.0 and the history of the Transformer](../../sources/karpathy-software-3-and-transformer-history-lecture.md) — learned **modality-embedding tokens** for sensor fusion: the same object with sensors as the alphabet.
- [From n-grams to attention](../../syntheses/sequence-models/language-model-to-transformer-lineage.md) (synthesis)

## Open questions / TBD

- ~~word2vec is not ingested.~~ **Resolved 2026-08-30** — both papers ingested.
- **No source here measures embedding geometry in a robotics setting.** The analogy benchmark exists for words and has no action-space analogue anywhere in this wiki. Given that [latent action tokens](latent-action-tokens.md) are criticised for being unreadable, a structured probe of an action codebook's geometry is an obvious and unwritten experiment.
- **Levy & Goldberg (2014)** — Skip-gram-with-negative-sampling as implicit factorization of a shifted PMI matrix — would connect this page to [spectral theory of SSL](spectral-theory-of-ssl.md). The soft-prompt result (prompts cluster by configuration, not by dataset) is the closest thing, and it is one paper.
- **Tied input/output embeddings** — standard in LLMs, foreshadowed by the 2003 §5.1 energy variant, and not covered by any ingested source.
