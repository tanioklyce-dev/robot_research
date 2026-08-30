---
title: "From n-grams to attention — the lineage that produced the Transformer"
type: synthesis
created: 2026-08-30
updated: 2026-08-30
tags: [lineage, history, language-models, embeddings, attention, transformer, seq2seq, word2vec, sequence-models]
---

> [!note] What this page is
> A six-paper arc, all now ingested as primaries, running 2003 → 2017. It exists because the wiki had the **destination** ([Attention Is All You Need](../../sources/attention-is-all-you-need.md), [ViT](../../sources/vit-paper.md), and every transformer-trunked [VLA](../../concepts/learning/vla-models.md)) in high resolution and the **road** not at all. Written after ingesting the five, and cross-checked against [Karpathy's own telling](../../sources/karpathy-software-3-and-transformer-history-lecture.md) of the same lineage.

## The arc in one table

| Year | Paper | What it added | What it left broken |
|---|---|---|---|
| 2003 | [Bengio, Ducharme, Vincent & Jauvin](../../sources/bengio2003-neural-probabilistic-language-model.md) | The **learned embedding table** `C`; a smooth function over word vectors, beating `n`-grams by 24% perplexity | Fixed 2–5 word context; softmax over `\|V\|` = **99.7% of compute**; embeddings internal to one model |
| 2013a | [Mikolov, Chen, Corrado & Dean](../../sources/mikolov2013-efficient-estimation-word-representations.md) | **Delete the hidden layer** (CBOW / Skip-gram); the **analogy benchmark**; embeddings as a downloadable artifact | Still no order, no context-dependence; softmax still the bottleneck |
| 2013b | [Mikolov, Sutskever, Chen, Corrado & Dean](../../sources/mikolov2013-distributed-representations-words-phrases.md) | **Negative sampling** kills the softmax; subsampling; phrases | One vector per word — polysemy unaddressed |
| 2014a | [Cho, van Merriënboer, Gulcehre, **Bahdanau**, Bougares, Schwenk & Bengio](../../sources/cho2014-rnn-encoder-decoder-phrase-representations.md) | The **RNN Encoder–Decoder**; the gated unit later named the **GRU**. `c` fed at *every* decoder step | Used only as a **feature inside Moses**, not as a translation system; one fixed `c` |
| 2014b | [Sutskever, Vinyals & Le](../../sources/sutskever2014-sequence-to-sequence-learning.md) | Same decomposition **end to end**; beats phrase-based SMT outright | `c` demoted to the decoder's *initial state only* — **more** bottlenecked; patched with a source-reversal trick |
| 2014c | [Bahdanau, Cho & Bengio](../../sources/bahdanau2014-neural-machine-translation-align-translate.md) | **Attention** — a learned, normalized, differentiable read over *all* encoder states | Still recurrent, therefore still sequential and slow |
| 2017 | [Vaswani et al.](../../sources/attention-is-all-you-need.md) | **Delete the recurrence**; dot-product scoring, K/V separation, multi-head, self-attention | `O(n²)`; the bill everything since has been paying |

## The single sentence

**Each paper removes one component of its predecessor and keeps the rest.**

- word2vec removes the NNLM's **hidden layer**.
- Negative sampling removes the **softmax**.
- The GRU removes the LSTM's **memory cell and two of its four gates**.
- Attention removes the **fixed-length bottleneck**.
- The Transformer removes the **recurrence**.

Nobody in this chain adds a big new mechanism except Bahdanau. The rest is subtraction, and each subtraction buys scale.

> [!note] The 2014 papers are three months apart, from two overlapping author lists
> June: [Cho et al.](../../sources/cho2014-rnn-encoder-decoder-phrase-representations.md) propose the encoder–decoder and use it as **one feature inside Moses**, reaching BLEU 34.64 against a 33.30 baseline. September: [Sutskever et al.](../../sources/sutskever2014-sequence-to-sequence-learning.md) use the same decomposition **end to end** and reach 34.81 against the same baseline — the architecture was never the constraint, the ambition was. Also September: [Bahdanau, Cho & Bengio](../../sources/bahdanau2014-neural-machine-translation-align-translate.md) diagnose the fixed vector and remove it.
>
> **Cho is first author on the first and second author on the third; Bahdanau is fourth author on the first and first author on the third.** One group published its own architecture and its own refutation inside a single quarter. Neither paper's headline mechanism was named in it: the GRU is "a hidden unit that adaptively remembers and forgets," and attention was *RNNsearch* until Bengio renamed it.

> [!note] The one thing that never got removed
> `C`, the embedding table, is unchanged from 2003. Same object: a `|V| × m` matrix of free parameters, trained jointly with whatever consumes it. Modern models tie it to the output layer and use subword units, and that is the whole delta in twenty-three years. See [distributed representations](../../concepts/learning/distributed-representations.md).

## Three things this arc actually teaches

### 1. The bottleneck moves, and it is always the thing that touches the vocabulary

Bengio et al. measured it precisely: `|V|(1 + nm + h) + h(1 + (n−1)m)` parameters, of which the output layer is **99.7% of the arithmetic**, and they spent §3 of the paper on a 40-CPU Myrinet cluster to survive it. Every subsequent step in the chain is partly a softmax-avoidance story — hierarchical softmax (Morin & Bengio), Huffman trees, NCE, negative sampling, sampled softmax — and [Bengio's §5.2](../../sources/bengio2003-neural-probabilistic-language-model.md) **listed four of those fixes in 2003 as future work**.

The general lesson is not about softmax. It is that **the expensive operation is the one that must touch every element of a large discrete set**, and the recurring fix is to avoid enumerating it — by tree, by sampling, or by not normalizing at all. Worth carrying into robot action spaces, where the analogous move is choosing whether the action head enumerates a vocabulary.

### 2. Ideas arrive before the compute, and the gap is roughly a decade

[Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md) needed **three weeks on 40 CPUs** for five epochs over 14M words, and never saw overfitting because they could not afford to train longer. The best model in that paper is undertrained for budget reasons.

word2vec is substantially *the fixes Bengio listed*, executed on infrastructure ([DistBelief](../../entities/jeff-dean.md), 50–100 asynchronous replicas) that did not exist in 2003. Note also that Bengio's §3.1 improvised **lossy asynchronous SGD** — processors overwriting each other's updates, reported as harmless noise — eight years before Hogwild! made it a named result.

So the honest reading of "why did word2vec work": not a better idea, a runnable one. [Table 4 of 2013a](../../sources/mikolov2013-efficient-estimation-word-representations.md) concedes it — a Bengio-style NNLM at 6B words scores **50.8%**, beating CBOW's 36.1%. The log-linear models win on the compute axis and lose on the modelling one.

### 3. Winning the benchmark and winning the decade are different events

[seq2seq](../../sources/sutskever2014-sequence-to-sequence-learning.md) Table 1 reports **Bahdanau at 28.45 BLEU against its own 34.81**. Attention lost that comparison outright. Three years later the fixed-vector architecture that beat it was gone and the mechanism that lost was in everything.

Two reasons the benchmark misled, both visible in the papers:

- **seq2seq bought its length robustness with a trick, not a mechanism.** Reversing the source sentence was worth ~4.7 BLEU (25.9 → 30.6) — more than a 5× ensemble — and it is a *data transformation that shortens the credit-assignment path*, not added capacity. [Bahdanau's Figure 2](../../sources/bahdanau2014-neural-machine-translation-align-translate.md), where RNNencdec's BLEU falls off with sentence length and RNNsearch-50's does not, is the mechanism doing structurally what the trick did contingently.
- **Both systems were mostly measuring their vocabulary.** A 30k (Bahdanau) or 80k (seq2seq) shortlist with `[UNK]` for everything else dominates the headline numbers — Bahdanau's RNNsearch-50★ goes **28.45 → 36.15** just by excluding sentences with unknown words, and on that subset it beats Moses. Subword tokenization solved this and is un-ingested here.

The transferable version: **a contemporaneous benchmark comparison is evidence about two systems on one test set.** The property that decided the outcome — attention parallelizes and scales, recurrence does not — was not on the leaderboard.

## Where attention actually came from

Not from theory. Per [Bahdanau's email to Karpathy](../../sources/karpathy-software-3-and-transformer-history-lecture.md), read aloud in the CS25 lecture: he was looking for a way around the encoder bottleneck, tried and abandoned ideas about "cursors that traverse the sequences," and then thought of letting the decoder **learn where to put the cursor** — inspired by his own middle-school English translation exercises, where "your gaze shifts back and forth between source and target sequence as you translate." He expressed the soft search as a softmax and a weighted average, and it "worked from the very first try."

Two footnotes worth keeping:

- **The name was Bengio's**, added on a final pass. The mechanism's working name was **RNNsearch** — still the model name throughout the published paper.
- **The deep idea is not "look at the input."** It is *replace a discrete latent structure that needs its own inference algorithm with a normalized differentiable weighting, and let end-to-end gradients find it.* Classical SMT inferred word alignment with EM in a separate stage. Bahdanau made alignment a soft weight computed inside the network. That trade — give up the explicit latent, gain end-to-end trainability — recurs far outside language.

## What this arc is missing, and it matters

Five papers is not the whole road. Un-ingested, in rough order of how much they would change the picture:

- **Mikolov, Yih & Zweig (NAACL 2013)** — the actual origin of the vector-offset analogy method, which both word2vec papers cite and popularize.
- **Cho et al. 2014b** — *On the Properties of Neural Machine Translation*, the paper that actually **measured** encoder–decoder quality degrading with input length. [Bahdanau et al.](../../sources/bahdanau2014-neural-machine-translation-align-translate.md)'s whole conjecture cites it, and the wiki asserts the finding without holding the source. The most load-bearing gap in this arc.
- **Luong et al. 2015** — dot-product attention scoring, the missing step between Bahdanau's feedforward scorer and Vaswani's matmul.
- **Sennrich et al. 2016 (BPE)** — what actually fixed the `[UNK]` problem distorting every table above.
- **Levy & Goldberg 2014** — Skip-gram-with-negative-sampling as implicit PMI matrix factorization; would connect this arc to [spectral theory of SSL](../../concepts/learning/spectral-theory-of-ssl.md), which has no pre-2020 ancestry.
- **AlexNet (2012)** and **GPT-1/2/3** — the wiki tracks their descendants closely and their origins not at all.

## Why a robotics wiki keeps this page

Three claims, each with a live consequence in this wiki's actual subject matter.

**The embedding table is the unexamined component of every robot policy here.** [VQ-BeT](../../entities/vq-bet.md)'s codebook, [latent action tokens](../../concepts/learning/latent-action-tokens.md), RT-2-style discrete action bins, [soft-prompt embodiment conditioning](../../concepts/learning/soft-prompt-cross-embodiment.md) — all are `C` with actions or embodiments substituted for words. The 2003 finding that **joint training is load-bearing** (fixed LSI-style features failed) and the 2013 finding that **the learned geometry carries real structure** (the analogy result, with its input-exclusion caveat) are the two things known about that object, and neither has been tested on an action vocabulary in any source here.

**The fixed-vector bottleneck has an exact robotics analogue, and it is unaudited.** An action-chunking policy that pools its observation into one latent and decodes a long horizon from it is seq2seq. The failure mode Bahdanau documented — output that stays *fluent and stops being conditioned on the input*, with no drop in confidence — is what that looks like at the end of a long chunk. Which architectures in this wiki cross-attend to observation tokens and which condition on a pooled feature is a question nobody here has asked.

**Scale changes what is worth building in.** The chain's consistent finding — restated by [Karpathy](../../sources/karpathy-software-3-and-transformer-history-lecture.md) as "if you have infinite data you want to encode less and less" and by the [ViT paper](../../sources/vit-paper.md) as data trumping inductive bias — cuts the other way at robot-data scale. Language went from 14M words (2003) to 100B (2013) to internet-scale. Robot manipulation corpora are at [350 hours](../../entities/droid.md) to [20,854](../../sources/egoscale-paper.md). **This lineage is the argument for inductive bias in robot learning, not against it** — the architectures that discarded priors did so after their data grew four orders of magnitude, and robot data has not.

## Related

- [Curriculum Module 3 — Sequence models, attention, and transformers](../curriculum/curriculum-03-attention-and-transformers.md)
- [Distributed representations](../../concepts/learning/distributed-representations.md)
- [Attention Is All You Need](../../sources/attention-is-all-you-need.md) · [ViT](../../sources/vit-paper.md)
- [Cho et al. 2014 — RNN Encoder–Decoder](../../sources/cho2014-rnn-encoder-decoder-phrase-representations.md)
- [Yoshua Bengio](../../entities/yoshua-bengio.md) · [Tomas Mikolov](../../entities/tomas-mikolov.md) · [Ilya Sutskever](../../entities/ilya-sutskever.md) · [Dzmitry Bahdanau](../../entities/dzmitry-bahdanau.md) · [Kyunghyun Cho](../../entities/kyunghyun-cho.md) · [Jeff Dean](../../entities/jeff-dean.md)
