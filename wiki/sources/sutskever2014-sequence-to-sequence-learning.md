---
title: "Sequence to Sequence Learning with Neural Networks (Sutskever, Vinyals, Le, NIPS 2014)"
type: source
url: https://arxiv.org/abs/1409.3215
local_path: raw/1409.3215v3.pdf
sha256: 5c74e1db863e2d61b869c9b0603494b34c41fb05db1a4fa7f9a83d5a42b7350f
author: Ilya Sutskever, Oriol Vinyals, Quoc V. Le
affiliation: Google
venue: "NIPS 2014 (Advances in Neural Information Processing Systems 27); arXiv 1409.3215"
published: 2014-09-10 (v1); v3 2014-12-14
ingested: 2026-08-30
tags: [seq2seq, encoder-decoder, lstm, machine-translation, beam-search, sutskever, google, foundational, nips-2014, action-chunking]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/1409.3215v3.pdf`, 9 pages), pages 1–8 in full; references skimmed. Tables 1–3 and the training-details list re-extracted in layout mode.

## Summary

**"Sequence to Sequence Learning with Neural Networks"** — Sutskever, Vinyals & Le (Google; NIPS 2014). The paper that established the **encoder–decoder** pattern: run one network over the input to produce a **single fixed-dimensional vector**, then condition a second network on that vector to generate the output, one token at a time, until an `<EOS>` symbol.

Concretely: two separate 4-layer LSTMs, 1000 cells per layer, 1000-d word embeddings. The encoder reads the source sentence and its final hidden state — **8,000 real numbers** — is the entire representation of the sentence. The decoder is an LSTM language model whose initial state is that vector.

**Headline result.** On WMT'14 English→French, a 5-LSTM ensemble with beam search reaches **BLEU 34.81** by direct translation, against **33.30** for the phrase-based SMT baseline — *"the first time a pure neural translation system outperforms a phrase-based SMT baseline on a large scale MT task by a sizeable margin."* Using the LSTM to rescore the baseline's 1000-best lists reaches **36.5**, within 0.5 of the best WMT'14 system (37.0).

**Why it matters to this wiki.** Two reasons, and the second is the durable one:

1. **It is the architecture the transformer replaced**, and it names the flaw. Everything the source sentence contains must pass through one fixed-width vector, whatever the sentence's length. [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md) removes that bottleneck with attention; [Vaswani et al. 2017](attention-is-all-you-need.md) discards the recurrence and keeps the attention. Read in sequence, seq2seq is the clearest statement of the problem attention exists to solve.
2. **The pattern outlived the architecture.** "Encode an observation into a latent, autoregressively decode a sequence of outputs, stop on a terminal token" is the shape of a modern robot policy — an [ACT](../entities/act.md)-style action-chunking transformer, a [VLA](../concepts/learning/vla-models.md) emitting action tokens, a [BeT](../entities/bet.md) policy over action bins. The LSTMs are gone; the decomposition is not.

## Abstract (verbatim)

> "Deep Neural Networks (DNNs) are powerful models that have achieved excellent performance on difficult learning tasks. Although DNNs work well whenever large labeled training sets are available, they cannot be used to map sequences to sequences. In this paper, we present a general end-to-end approach to sequence learning that makes minimal assumptions on the sequence structure. Our method uses a multilayered Long Short-Term Memory (LSTM) to map the input sequence to a vector of a fixed dimensionality, and then another deep LSTM to decode the target sequence from the vector. Our main result is that on an English to French translation task from the WMT'14 dataset, the translations produced by the LSTM achieve a BLEU score of 34.8 on the entire test set, where the LSTM's BLEU score was penalized on out-of-vocabulary words. Additionally, the LSTM did not have difficulty on long sentences. For comparison, a phrase-based SMT system achieves a BLEU score of 33.3 on the same dataset. When we used the LSTM to rerank the 1000 hypotheses produced by the aforementioned SMT system, its BLEU score increases to 36.5, which is close to the previous best result on this task. The LSTM also learned sensible phrase and sentence representations that are sensitive to word order and are relatively invariant to the active and the passive voice. Finally, we found that reversing the order of the words in all source sentences (but not target sentences) improved the LSTM's performance markedly, because doing so introduced many short term dependencies between the source and the target sentence which made the optimization problem easier."

## The model (§2)

```
p(y_1, …, y_{T'} | x_1, …, x_T) = Π_{t=1..T'}  p(y_t | v, y_1, …, y_{t−1})
```

where `v` is the encoder LSTM's final hidden state. Each `p(y_t | ·)` is a softmax over the full target vocabulary. `<EOS>` lets the model define a distribution over sequences of *any* length — the mechanism that makes variable-length output possible at all.

Three departures from the naive version, all reported as necessary:

1. **Two separate LSTMs**, encoder and decoder, rather than one shared. More parameters at negligible compute cost, and it makes multi-language training natural.
   - Note a quieter divergence from [Cho et al. 2014a](cho2014-rnn-encoder-decoder-phrase-representations.md), published three months earlier with the same decomposition: **there, `c` is supplied at every decoder step**; here it is only the decoder's initial hidden state, after which the source summary must survive inside the recurrence. That makes this the *more* bottlenecked of the two designs, and it is the one [attention](bahdanau2014-neural-machine-translation-align-translate.md) is usually said to fix.
2. **Depth.** Four layers; "each additional layer reduced perplexity by nearly 10%." Shallow LSTMs were significantly worse.
3. **Reverse the source sentence** (not the target). `a,b,c → α,β,γ` becomes `c,b,a → α,β,γ`.

### The reversal trick (§3.3)

**Test perplexity 5.8 → 4.7; BLEU 25.9 → 30.6.** A ~4.7 BLEU gain from reordering the input, with no change to the model.

The explanation offered: the *average* distance between corresponding source and target words is unchanged, but the **minimal time lag** collapses — the first source words now sit adjacent to the first target words, so backpropagation can "establish communication" between the sequences early in training and bootstrap from there.

> [!note] What the reversal trick actually tells you
> The authors expected reversal to help early target words and hurt late ones. Instead, reversed models did **better on long sentences** (§3.7), which they read as better memory utilization.
>
> The honest structural reading: **reversal is a symptom-level fix for the fixed-vector bottleneck.** It does not add capacity or change what the representation can hold; it makes an optimization problem tractable that the architecture had made hard. A year later, attention removed the need for it entirely. The transferable lesson — a data transformation that shortens the credit-assignment path can be worth more than an architectural change, and is much cheaper to try — is one of the more useful things in the paper, and it is a lesson about *optimization*, not about language.

## Training and infrastructure (§3.4–3.5)

- **Data**: WMT'14 En→Fr, 12M sentence pairs, 348M French / 304M English words. Vocabulary **160,000 source / 80,000 target**; everything else → `UNK`. The 34.81 is penalized on those OOV words.
- **Model**: 384M parameters, of which **64M are recurrent** (32M encoder + 32M decoder) — the rest is embeddings and the naive 80k softmax.
- **Init**: uniform `[−0.08, 0.08]`.
- **Optimizer**: plain SGD, **no momentum**, fixed learning rate **0.7**; after 5 epochs, halve every half-epoch; 7.5 epochs total.
- **Gradient clipping**: with `g` the gradient divided by 128 and `s = ‖g‖₂`, if `s > 5` then `g ← 5g/s`. LSTMs do not vanish but they do explode.
- **Length-bucketed minibatches** — sorting so a batch holds similar-length sentences gave a **2× speedup**, purely by not wasting computation on padding.
- **Hardware**: 8-GPU machine — one LSTM layer per GPU (4), the remaining 4 parallelizing the softmax (each multiplying by a 1000×20000 matrix). 1,700 words/s on one GPU → **6,300 words/s**. **~10 days** of training.

## Results (§3.6)

### Direct translation (Table 1)

| Method | BLEU (ntst14) |
|---|---|
| Bahdanau et al. | 28.45 |
| **Baseline SMT** | **33.30** |
| Single forward LSTM, beam 12 | 26.17 |
| Single **reversed** LSTM, beam 12 | 30.59 |
| Ensemble of 5 reversed, beam 1 | 33.00 |
| Ensemble of 2 reversed, beam 12 | 33.27 |
| Ensemble of 5 reversed, beam 2 | 34.50 |
| **Ensemble of 5 reversed, beam 12** | **34.81** |

### Rescoring (Table 2)

| Method | BLEU |
|---|---|
| Baseline SMT | 33.30 |
| Cho et al. | 34.54 |
| **Best WMT'14 result** | **37.0** |
| Rescore 1000-best, single forward LSTM | 35.61 |
| Rescore 1000-best, single reversed LSTM | 35.85 |
| Rescore 1000-best, ensemble of 5 reversed | 36.5 |
| *Oracle rescoring of the 1000-best* | *~45* |

Three things the tables say that the abstract does not:

- **A beam of 1 nearly suffices.** The 5-model ensemble scores 33.00 with greedy decoding and 34.50 at beam 2 — most of the search benefit arrives immediately. The paper notes an ensemble of 5 at beam 2 is *cheaper* than a single model at beam 12, and scores 4 points higher. Ensembling bought more than search.
- **Reversal (30.59 vs 26.17) is worth more than a 5× ensemble** (single reversed 30.59 → ensemble 34.81 is +4.2; forward → reversed is +4.4).
- **The oracle line is the honest ceiling.** Perfect selection from the SMT system's own 1000-best lists would score ~45 against the 36.5 achieved. Most of the available quality was in the candidate list and unreachable by rescoring — which is the argument for end-to-end generation over reranking, made against the paper's own best number.

> [!warning] The Bahdanau comparison in Table 1 is a snapshot, not a verdict
> Table 1's first row reports [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md) at **28.45**, well below this paper's 34.81. Both are arXiv-2014. Attention lost this round and won the decade: the fixed-vector architecture that beat it here is the one that disappeared, and the mechanism that scored 28.45 is in every model in this wiki. A contemporaneous benchmark comparison is evidence about two systems on one test set, not about which idea generalizes.

### Sentence representations (§3.8, Figure 2)

A 2-D PCA of encoder hidden states clusters phrases **by meaning**, with clusters sensitive to word order (`John admires Mary` vs `Mary admires John` separate cleanly) and largely invariant to active/passive voice (`I gave her a card in the garden` sits near `She was given a card by me in the garden`). Order-sensitivity is precisely what a bag-of-words model — including [CBOW](mikolov2013-efficient-estimation-word-representations.md) — cannot produce. This is the first sentence-level embedding result in the wiki's lineage.

### Long sentences (§3.7, Figure 3)

No degradation below 35 words; only minor degradation on the longest. Presented as the surprise of the paper, given contemporaries' failures. It is a *result about reversal*, not about fixed-vector encoding — which Bahdanau's length curves shortly made clear.

## Position in the lineage

```
Bengio et al. 2003 — the embedding table, fixed context window
   ↓
Mikolov et al. 2013 — embeddings as a standalone artifact, at scale
   ↓
Sutskever, Vinyals & Le 2014 — variable-length in, variable-length out
   │   encoder → ONE fixed vector → autoregressive decoder + <EOS>
   │   the bottleneck is the design; reversing the source is the workaround
   ↓
Bahdanau, Cho & Bengio 2014 — replace the single vector with a weighted
   │   read over all encoder states (attention). Bottleneck removed.
   ↓
Vaswani et al. 2017 — keep the attention, delete the recurrence
   ↓
Every encoder-decoder in this wiki:
- ACT / action-chunking policies (encode obs → decode an action sequence)
- VLA action heads emitting token sequences
- JEPA predictors (encode → predict in latent → no decoder at all)
```

## Robotics relevance

The reason this belongs in a robotics wiki is the **decomposition**, not the LSTM. An action-chunking policy is a seq2seq model: encode the current observation into a latent, decode a horizon of actions autoregressively, stop at a fixed length or a terminal token. [ACT](../entities/act.md) does this with a CVAE and a transformer; [VQ-BeT](../entities/vq-bet.md) does it over a codebook; a [VLA](../concepts/learning/vla-models.md) does it over text-like action tokens.

The transferable warning is the bottleneck. Whenever a policy compresses its observation into **one fixed-width latent** and decodes a long horizon from it, this paper's failure mode is available: the later the output, the more it depends on information the latent had no room for. Attention is the standard fix in language; in robot policies the analogue is cross-attention to observation tokens rather than conditioning on a pooled feature. Worth checking which side of that line any given architecture in this wiki sits on.

## Entities mentioned

- **[Ilya Sutskever](../entities/ilya-sutskever.md)** — first author; also second author of [word2vec paper 2](mikolov2013-distributed-representations-words-phrases.md) the previous year.
- **Oriol Vinyals** — co-author; later on AlphaStar / Gemini at DeepMind. No wiki page.
- **Quoc V. Le** — co-author, Google Brain. No wiki page.
- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — via the Bahdanau et al. row in Table 1, and the NNLM reference.
- **[Kyunghyun Cho](../entities/kyunghyun-cho.md)** — cited throughout as the concurrent [RNN Encoder–Decoder](cho2014-rnn-encoder-decoder-phrase-representations.md) work (June 2014, three months earlier), which used the same decomposition as a *feature inside* an SMT system rather than end to end. Table 2 reports it at 34.54 against this paper's 34.81.
- Kalchbrenner & Blunsom (first to map a whole sentence to a vector), Graves (differentiable attention) — cited precursors, not ingested.

## Concepts touched

- **[LSTM](../glossary.md#lstm)**, **[RNN](../glossary.md#rnn)** — the architecture, and [Module 3 §1](../syntheses/curriculum/curriculum-03-attention-and-transformers.md).
- **[Beam search](../glossary.md#beam-search)** — the decoder, added to the glossary by this ingest.
- **Encoder–decoder** — [Module 3 §8](../syntheses/curriculum/curriculum-03-attention-and-transformers.md) covers the three transformer shapes; this is where the shape comes from.
- **[Distributed representations](../concepts/learning/distributed-representations.md)** — extended here from words to whole sentences.

## Open questions / TBD

- **Where the wiki's policies sit on the bottleneck question** — which action-chunking architectures condition on a pooled latent versus cross-attending to observation tokens — is a synthesis worth writing and is not written.
- ~~Cho et al. 2014 (the GRU / RNN encoder-decoder paper) is an un-ingested precursor.~~ **Resolved 2026-08-30** — [ingested](cho2014-rnn-encoder-decoder-phrase-representations.md). **Kalchbrenner & Blunsom 2013** (first to map a whole sentence to a vector) remains un-ingested.
