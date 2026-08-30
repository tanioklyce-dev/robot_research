---
title: "Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation (Cho, van Merriënboer, Gulcehre, Bahdanau, Bougares, Schwenk, Bengio, EMNLP 2014)"
type: source
url: https://arxiv.org/abs/1406.1078
local_path: raw/1406.1078v3.pdf
sha256: 35acfcc574b37588ac0443ac65c9e2fccf794b24df9cf8522d6df5f09b82119c
author: Kyunghyun Cho, Bart van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio
affiliation: Université de Montréal; Jacobs University Bremen (Bahdanau); Université du Maine (Bougares, Schwenk); Bengio CIFAR Senior Fellow
venue: "EMNLP 2014 (Doha); arXiv 1406.1078"
published: 2014-06-03 (v1); v3 2014-09-03
ingested: 2026-08-30
tags: [gru, gated-recurrent-unit, encoder-decoder, rnn, machine-translation, smt, phrase-representations, cho, bengio, bahdanau, foundational, emnlp-2014]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/1406.1078v3.pdf`, 15 pages). Pages 1–10 read in full (architecture, the gated unit, the SMT integration, experiments, qualitative analysis, conclusion); pages 10–15 are references and supplementary architecture detail, skimmed. Tables 1–3 re-extracted in layout mode.

## Summary

**"Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation"** — Cho, van Merriënboer, Gulcehre, Bahdanau, Bougares, Schwenk & Bengio (Montréal + Jacobs Bremen + Le Mans; EMNLP 2014). **The paper this wiki had been citing by proxy three times over** — for the **GRU**, for the **RNN Encoder–Decoder** framing, and as the **RNNencdec baseline** in [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md) Now sourced.

Two contributions, and the second is the one everyone remembers:

1. **The RNN Encoder–Decoder.** One RNN reads a variable-length source into a fixed-length summary vector `c`; a second RNN generates a variable-length target conditioned on it. Trained jointly to maximize `(1/N) Σ log p_θ(y_n | x_n)`.
2. **A new gated recurrent unit** — §2.3, titled *"Hidden Unit that Adaptively Remembers and Forgets"* — with a **reset gate** and an **update gate**, "motivated by the LSTM unit but much simpler to compute and implement."

**Why it matters to this wiki.** It supplies two things the wiki has been using without a primary. The **GRU** appears in the glossary and in [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md), where "hidden unit" always means this unit — its equations are here and nowhere else in the wiki. And the **encoder–decoder decomposition** is the direct ancestor of every encode-then-decode policy in the robotics material, arriving here three months before [seq2seq](sutskever2014-sequence-to-sequence-learning.md) made the same decomposition famous by using it end-to-end.

> [!note] The name "GRU" is not in this paper
> The unit is called "the proposed hidden unit," "a new type of hidden unit," and in the section title "Hidden Unit that Adaptively Remembers and Forgets." **"Gated Recurrent Unit" is a later coinage.** Precisely the same pattern as [attention, whose working name was *RNNsearch*](bahdanau2014-neural-machine-translation-align-translate.md) until Bengio renamed it on a final pass — the mechanism ships before the name that makes it citable. Two for two in this research group, in one year.

## Abstract (verbatim)

> "In this paper, we propose a novel neural network model called RNN Encoder–Decoder that consists of two recurrent neural networks (RNN). One RNN encodes a sequence of symbols into a fixed-length vector representation, and the other decodes the representation into another sequence of symbols. The encoder and decoder of the proposed model are jointly trained to maximize the conditional probability of a target sequence given a source sequence. The performance of a statistical machine translation system is empirically found to improve by using the conditional probabilities of phrase pairs computed by the RNN Encoder–Decoder as an additional feature in the existing log-linear model. Qualitatively, we show that the proposed model learns a semantically and syntactically meaningful representation of linguistic phrases."

## The architecture (§2.2)

The encoder reads symbols one at a time; after the end-of-sequence symbol, "the hidden state of the RNN is a **summary `c` of the whole input sequence**." The decoder then runs:

```
h⟨t⟩             = f( h⟨t−1⟩, y_{t−1}, c )
P(y_t | y_{<t}, c) = g( h⟨t⟩, y_{t−1}, c )
```

> [!note] A real difference from seq2seq, and it matters for the lineage
> **`c` is supplied at every decoder step here** — it enters both the hidden-state update `f` and the output function `g`. [Sutskever, Vinyals & Le](sutskever2014-sequence-to-sequence-learning.md) instead use the summary vector **only as the decoder's initial hidden state**, after which it must survive in the recurrence.
>
> This puts [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md) a **smaller step from this paper than from seq2seq**: their contribution is to replace one fixed `c`, already wired into every step, with a **per-target-word `c_i`** computed by a soft alignment. The plumbing was already there; what changed is what flows through it. Given that Bahdanau is the fourth author here and Cho the second author there, that continuity is not a coincidence.

## The gated unit (§2.3) — the GRU's original equations

```
r_j    = σ( [W_r x]_j + [U_r h⟨t−1⟩]_j )                    (5)   reset gate
z_j    = σ( [W_z x]_j + [U_z h⟨t−1⟩]_j )                    (6)   update gate
h̃⟨t⟩_j = φ( [W x]_j + [U (r ⊙ h⟨t−1⟩)]_j )                  (8)   candidate state
h⟨t⟩_j = z_j · h⟨t−1⟩_j  +  (1 − z_j) · h̃⟨t⟩_j              (7)   the mix
```

> [!warning] The update gate's polarity is inverted relative to modern implementations
> Equation (7) as published has **`z` multiplying the *previous* state**: `z = 1` means *keep `h⟨t−1⟩`*, `z = 0` means *take the candidate*. The paper's prose agrees — "the update gate controls how much information from the previous hidden state will carry over."
>
> Modern GRU implementations (PyTorch `nn.GRU` included) write `h_t = (1 − z) h_{t−1} + z h̃_t`, i.e. **the opposite convention**. The unit is identical up to relabelling, but anyone reading these equations against a modern implementation, or porting between them, will get the gate backwards. Worth knowing before treating the published form as the reference.

What the two gates do, in the authors' framing:

- **Reset gate near 0** forces the hidden state to "ignore the previous hidden state and reset with the current input only," letting the unit "drop any information that is found to be irrelevant later in the future, thus allowing a more compact representation."
- **Update gate** "acts similarly to the memory cell in the LSTM network and helps the RNN to remember long-term information." They also describe it as "an adaptive variant of a leaky-integration unit."

Because the gates are **per-unit**, "each hidden unit will learn to capture dependencies over different time scales" — short-term units end up with frequently-active reset gates, long-term units with mostly-active update gates. **The timescale decomposition is learned per dimension, not designed.**

Against the LSTM: a memory cell plus four gating units, versus **two gates and no separate cell**. Strictly less machinery, and the paper's claim is only that it is "much simpler to compute and implement" — not that it is better.

> [!note] The one-line ablation that carries the section
> *"In our preliminary experiments, we found that it is crucial to use this new unit with gating units. **We were not able to get meaningful result with an oft-used `tanh` unit without any gating.**"*
>
> Not a marginal improvement — the difference between working and not working, on this task at this scale. The gating is load-bearing. (No numbers are given for the ungated run, which is the weakness of the claim.)

## What the model is actually used for (§3) — and it is not translation

**The system does not translate.** It is trained on a **table of phrase pairs** and its scores enter Moses' existing log-linear model as **one more feature** alongside the conventional translation and language-model features. The paper explicitly declines the end-to-end option: replacing the phrase table entirely "requires an expensive sampling procedure to be performed repeatedly," so "in this paper, thus, we only consider rescoring the phrase pairs in the phrase table."

One deliberate design choice worth extracting: **they ignore phrase-pair frequencies when training.** The rationale is that the existing phrase table already encodes frequency, so with fixed model capacity they want it "focused toward learning linguistic regularities… or learning the 'manifold' of plausible translations" rather than re-learning corpus counts. **Deliberately withholding a signal the surrounding system already provides, so the learned component spends its capacity on what the system lacks** — a transferable design principle, and directly relevant to any hybrid learned/classical robot stack.

## Setup and results

- **Data**: WMT'14 En→Fr. Moore–Lewis / Axelrod data selection down to **348M words** for the RNN Encoder–Decoder and 418M for the language model (the same 348M figure as [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md)). Test set `newstest2014`.
- **Vocabulary**: the **15,000 most frequent words** in each language, covering ~93% of the data; the rest → `[UNK]`. Smaller even than Bahdanau's 30k.
- **Model**: 1000 hidden units in encoder and decoder. Input and output matrices **low-rank factorized at rank 100** — "equivalent to learning an embedding of dimension 100 for each word." Decoder output through a deep net with one intermediate layer of **500 maxout units** pooling 2 inputs.
- **Init**: white Gaussian, σ = 0.01, **except recurrent matrices**, initialized from the **left singular vectors** of a Gaussian sample (orthogonal init, following Saxe et al.).
- **Optimizer**: **Adadelta** (ε = 10⁻⁶, ρ = 0.95) + SGD, 64 randomly selected phrase pairs per update, **~3 days** of training.

### Table 1 — BLEU on WMT'14 En→Fr

| Model | dev | **test** |
|---|---|---|
| Baseline (Moses, default settings) | 30.64 | **33.30** |
| Baseline + RNN | 31.20 | **33.87** |
| **Baseline + CSLM + RNN** | 31.48 | **34.64** |
| Baseline + CSLM + RNN + word penalty | 31.50 | 34.54 |

The RNN Encoder–Decoder alone buys **+0.57 BLEU**; adding a neural language model (CSLM) on top reaches **+1.34**. The authors' reading: the two neural components are "not too correlated" and "rather orthogonal," so each can be improved independently.

A small honest negative result is reported and not buried: the **word penalty helped the dev set and not the test set** (31.50 dev, 34.54 test — *below* the 34.64 without it).

> [!note] The number to hold onto
> **33.30 is the same Moses baseline that [seq2seq](sutskever2014-sequence-to-sequence-learning.md) and [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md) both report.** It is the fixed point the three papers are measured against, which makes them directly comparable: this paper reaches **34.64 as a feature inside** the SMT system; seq2seq reaches **34.81 replacing it outright**, three months later, with the same encoder–decoder decomposition. The architecture was not the constraint — the ambition was.

## Qualitative analysis (§4.3–4.4)

**Table 2** compares top-scoring target phrases from the count-based translation model against the RNN Encoder–Decoder. For **long, rare** source phrases the count-based column degenerates visibly — mojibake and truncated fragments like `[?s , qu']`, `[r c⃝ pour la premir¨ere fois]` — while the RNN returns clean, literal translations. The paper's expectation, confirmed: count-based scores are "better estimated for the frequent phrases but badly estimated for rare phrases," and a model trained without frequency information does not inherit that failure. **The clearest illustration in this wiki of what a learned model buys over a count-based one: not average-case accuracy, but tail behaviour.**

The authors also note the RNN "prefers shorter phrases in general," and that many phrase pairs are scored similarly by both while "there were as many other phrase pairs that were scored radically different" (Figure 3).

**Table 3** samples 50 target phrases per source phrase from the model directly — it produces well-formed output "without looking at the actual phrase table," and the generations "do not overlap completely with the target phrases from the phrase table." The conclusion drawn is cautious: it "encourages us to further investigate the possibility of replacing the whole or a part of the phrase table." Three months later, seq2seq did exactly that.

**Figures 4 and 5** — Barnes-Hut-SNE projections. Figure 4 shows **word** embeddings clustering semantically. Figure 5 projects the **phrase** representations (the 1000-d vector `c`) and finds both semantic and syntactic structure: a cluster of time-duration phrases, a cluster of countries and regions, and a separate cluster grouped by syntax rather than meaning.

> [!note] The first sentence-level embedding result in this wiki's lineage
> Figure 5 predates [seq2seq's Figure 2](sutskever2014-sequence-to-sequence-learning.md) (PCA of encoder states clustering by meaning and word order) by three months and makes the same point: **the encoder's summary vector is a learned representation of a whole phrase, with usable structure.** The paper is explicit that the model "is not specifically designed only for the task of machine translation" and looks at these properties as a general finding — a `c` worth having, independent of what decodes it. That is the premise every [JEPA](../concepts/world-models/jepa.md)-family and encode-then-plan architecture in this wiki runs on. See [distributed representations](../concepts/learning/distributed-representations.md).

## Position in the lineage

```
Bengio et al. 2003 — the embedding table (reference [1] here)
Mikolov et al. 2013 — word2vec (cited here for word embeddings)
   ↓
Cho et al., June 2014  (this paper)
   │  RNN Encoder–Decoder + the gated unit later called the GRU
   │  c is fed at EVERY decoder step; used as a feature inside Moses
   ↓
Sutskever, Vinyals & Le, Sept 2014 — same decomposition, end to end,
   │  c only as the decoder's initial state; beats SMT outright
   ↓
Bahdanau, Cho & Bengio, Sept 2014 — replace the single c with a
   │  per-target-word c_i via soft alignment. Attention.
   ↓
Vaswani et al. 2017 — delete the recurrence
```

Full arc: [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md).

> [!note] One group, one year, three papers
> Cho is first author here and second author on the attention paper. **Bahdanau is fourth author here** and first author there. Bengio is senior author on both — and on the 2003 paper both cite. June to September 2014: propose the encoder–decoder, then diagnose its central flaw and remove it. A research group publishing the refutation of its own architecture within one quarter is worth noting as a working pattern, not just a trivia item.

## Entities mentioned

- **[Kyunghyun Cho](../entities/kyunghyun-cho.md)** — first author. This is the paper behind both of his contributions the wiki was citing indirectly.
- **[Dzmitry Bahdanau](../entities/dzmitry-bahdanau.md)** — fourth author, then at Jacobs University Bremen; three months from overturning this architecture.
- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — senior author; reference [1] of this paper is his own [2003 NPLM](bengio2003-neural-probabilistic-language-model.md).
- Bart van Merriënboer, Caglar Gulcehre (Montréal), Fethi Bougares, **Holger Schwenk** (Le Mans) — co-authors; Schwenk's prior feedforward phrase-scoring work is the approach this generalizes to variable length, and the CSLM in Table 1 is his line.
- **[Tomas Mikolov](../entities/tomas-mikolov.md)** — cited for word-embedding extraction.
- Moses, Kalchbrenner & Blunsom, Devlin et al., Zou et al. — the SMT baseline and the neural-MT prior art.

## Concepts touched

- **[GRU](../glossary.md#gru)** — defined here; the glossary entry now has its primary.
- **Encoder–decoder** — [Module 3 §1.2](../syntheses/curriculum/curriculum-03-attention-and-transformers.md).
- **[Distributed representations](../concepts/learning/distributed-representations.md)** — extended to phrases; Figure 5.
- **[RNN](../glossary.md#rnn)**, **[LSTM](../glossary.md#lstm)** — the unit this simplifies.
- **[Beam search](../glossary.md#beam-search)** — not used here; the model scores rather than decodes.

## Open questions / TBD

- **Cho et al. 2014b — *On the Properties of Neural Machine Translation: Encoder–Decoder Approaches*** (arXiv 1409.1259) — the companion paper showing this architecture's quality **degrading rapidly with input length**. It is the empirical result [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md)'s entire conjecture rests on, and the wiki currently states that finding on the attention page **citing a source it does not hold**. The single most load-bearing remaining gap in this lineage.
- **Who first wrote "Gated Recurrent Unit," and where.** The name is universal and is not in this paper; the wiki cannot currently attribute it.
- **The gated-vs-`tanh` ablation is asserted without numbers.** "We were not able to get meaningful result" is the strongest claim in §2.3 and the least evidenced.
- **Chung et al. 2014** (the empirical GRU-vs-LSTM comparison, from the same group) is the standard citation for "GRU ≈ LSTM at lower cost" and is un-ingested.
