---
title: "Neural Machine Translation by Jointly Learning to Align and Translate (Bahdanau, Cho, Bengio, ICLR 2015)"
type: source
url: https://arxiv.org/abs/1409.0473
local_path: raw/1409.0473v7.pdf
sha256: 84801c8410da51b449d379d2fa4939a416123f2c93991077a680f863026022a7
author: Dzmitry Bahdanau, KyungHyun Cho, Yoshua Bengio
affiliation: Jacobs University Bremen; Université de Montréal (Bengio, CIFAR Senior Fellow)
venue: "ICLR 2015 (conference track); arXiv 1409.0473"
published: 2014-09-01 (v1); ICLR 2015; v7 2016-05-19
ingested: 2026-08-30
tags: [attention, alignment, soft-alignment, encoder-decoder, bidirectional-rnn, machine-translation, bahdanau, cho, bengio, foundational, iclr-2015]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/1409.0473v7.pdf`, 15 pages). Pages 1–8 read in full (motivation, model, experiments, quantitative and qualitative results); pages 9–15 are references and Appendices A–C (architecture detail, training procedure, extra sample translations), skimmed. Table 1 re-extracted in layout mode.

## Summary

**"Neural Machine Translation by Jointly Learning to Align and Translate"** — Bahdanau, Cho & Bengio (Jacobs University Bremen + Université de Montréal; ICLR 2015, arXiv Sept 2014). **The attention paper.** It identifies the flaw in the [seq2seq](sutskever2014-sequence-to-sequence-learning.md) encoder–decoder and removes it.

The diagnosis, stated as a conjecture in the abstract: *"the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture."* Everything about the source sentence must be squeezed into one vector before any target word is generated, and Cho et al. had already shown basic encoder–decoder quality collapsing as input length grows.

The fix: **let the decoder read the encoder's whole output, and learn where to look.** Encode the source with a **bidirectional RNN** into one annotation per source position. Then, for each target word `i`, compute a **different context vector**:

```
c_i = Σ_j α_ij h_j                       (weighted read over ALL source annotations)
α_ij = softmax_j( e_ij )                 (weights sum to 1)
e_ij = a(s_{i−1}, h_j)                   (alignment model: a small feedforward net)
```

`a` is trained jointly with everything else by backpropagation. The whole idea is in one sentence of §3.1: *"unlike in traditional machine translation, the alignment is not considered to be a latent variable. Instead, the alignment model directly computes a soft alignment, which allows the gradient of the cost function to be backpropagated through it."*

This is where the word enters the field: *"Intuitively, this implements a mechanism of **attention** in the decoder."*

**Why it matters to this wiki.** [Attention Is All You Need](attention-is-all-you-need.md) is the wiki's most load-bearing architecture source, and its lineage block opens with "Bahdanau et al. 2014 (attention for NMT, attached to RNN)" — until now an unsourced name. This is that paper. Everything the transformer kept, it got from here: a learned, normalized, differentiable weighting over a set of encoder states, computed per output position. Everything the transformer changed — dropping recurrence, the scoring function, separating keys from values, multiple heads — is downstream engineering on this mechanism.

## Abstract (verbatim)

> "Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encode a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition."

## The mechanism (§3)

### What it replaces

In [seq2seq](sutskever2014-sequence-to-sequence-learning.md), `c = q({h_1 … h_Tx}) = h_T` — the last hidden state, one vector, shared by every decoding step. Here the decoder state is `s_i = f(s_{i−1}, y_{i−1}, c_i)`, **with a distinct `c_i` per target word.**

Footnote 2 makes the generalization explicit and is the sentence the whole subsequent field rests on: encoding into a fixed-length vector *"is not necessary, and even it may be beneficial to have a variable-length vector."*

### The three pieces

1. **Bidirectional RNN encoder** (Schuster & Paliwal 1997). Forward RNN over `x_1…x_Tx`, backward RNN over `x_Tx…x_1`; annotation `h_j = [→h_j ; ←h_j]`. Because RNNs over-represent recent input, `h_j` is *focused on the words around `x_j`* while still summarizing both directions. This is what makes a per-position read meaningful — with a unidirectional encoder, `h_j` would be a prefix summary, not a position representation.
2. **Alignment model** `e_ij = a(s_{i−1}, h_j)` — a **feedforward network** taking the decoder's previous state and one annotation, jointly trained.
3. **Softmax normalization** into weights `α_ij`, then `c_i = Σ_j α_ij h_j`.

The probabilistic reading the paper offers: `α_ij` is the probability that target word `y_i` is aligned to source word `x_j`, so `c_i` is the **expected annotation** under that alignment distribution.

> [!note] The conceptual unlock, stated plainly
> Classical statistical MT treated word alignment as a **latent variable**, inferred with EM in a separate stage from the translation model. This paper's move is to make alignment a **soft, differentiable weighting computed inside the network**, so it is trained by the same backprop pass as everything else and needs no separate inference procedure or supervision.
>
> That is the reusable idea, and it is bigger than translation: *replace a discrete latent structure requiring its own inference algorithm with a normalized differentiable weighting, and let end-to-end gradients discover it.* Soft attention over image patches, over memory slots, over retrieved documents, over an observation set in a robot policy — all the same trade. The cost is that nothing guarantees the weights mean what you hope; §5.2.1's alignment plots are an *inspection* of an emergent quantity, not a supervised output.

### Mapping onto modern vocabulary

In [Vaswani et al. 2017](attention-is-all-you-need.md) terms: `s_{i−1}` is the **query**, and each `h_j` serves as **both key and value**. The transformer's changes are (a) separating keys from values via learned projections, (b) replacing the feedforward scorer with a **scaled dot product** (a matmul, hence parallelizable on a GPU — this is the change that mattered for scale), (c) multiple heads, and (d) using it for *self*-attention, not only encoder–decoder cross-attention.

Note also what this paper already pays: computing every `e_ij` costs **O(T_x × T_y)** scorer evaluations. The quadratic attention cost that FlashAttention, Linformer and every efficient-transformer paper attacks is introduced here, in 2014, and was cheap enough not to be worth mentioning.

## Experimental setup (§4)

- **Data**: WMT'14 English→French. 850M words of parallel corpora (Europarl 61M, news commentary 5.5M, UN 421M, two crawls at 90M and 272.5M) reduced to **348M words** by Axelrod data selection. Dev = news-test-2012 + 2013; test = **news-test-2014, 3003 sentences**.
- **Vocabulary**: shortlist of the **30,000 most frequent words** per language; everything else → `[UNK]`. No lowercasing or stemming.
- **Models**: `RNNencdec` (the Cho et al. baseline) and `RNNsearch` (this paper), each trained twice — on sentences up to **30** words and up to **50**.
- **Sizes**: RNNsearch encoder 1000 hidden units *per direction*, decoder 1000; a maxout hidden layer computes each output probability. "Hidden unit" always means the **gated hidden unit** — the GRU, from Cho et al. 2014a.
- **Optimization**: minibatch SGD with **Adadelta**, minibatches of 80 sentences, **~5 days** of training. Beam search for decoding.

## Results (§5.1, Table 1)

| Model | All | No UNK |
|---|---|---|
| RNNencdec-30 | 13.93 | 24.19 |
| **RNNsearch-30** | **21.50** | **31.44** |
| RNNencdec-50 | 17.82 | 26.71 |
| **RNNsearch-50** | **26.75** | **34.16** |
| **RNNsearch-50★** | **28.45** | **36.15** |
| Moses (phrase-based SMT) | 33.30 | 35.63 |

(★ = trained longer, until dev-set performance stopped improving.)

Four readings:

- **On the no-UNK subset, RNNsearch-50★ beats Moses: 36.15 vs 35.63.** The abstract's cautious "comparable to the existing state-of-the-art phrase-based system" is the honest framing of a narrow win on a filtered subset — but the comparison is if anything *unfavourable* to the neural model, since Moses additionally uses a **418M-word monolingual corpus** that RNNsearch never sees.
- **The `All` column is dominated by the vocabulary limit, not the architecture.** A 30k shortlist on WMT'14 means a lot of `[UNK]`, and the gap between the two columns (26.75 → 34.16 for RNNsearch-50) is almost entirely that. Both this paper and [seq2seq](sutskever2014-sequence-to-sequence-learning.md) are fighting the same open-vocabulary problem with a frequency cutoff; subword tokenization (BPE, Sennrich et al. 2016) is what actually solved it, and it is not in this wiki.
- **RNNsearch-30 (21.50) beats RNNencdec-50 (17.82).** Attention trained on shorter sentences beats no-attention trained on longer ones. The clean statement that the gain is mechanism, not data.
- **Attention buys more than depth or scale did.** +7.6 BLEU (RNNencdec-30 → RNNsearch-30) at matched data and roughly matched size.

### The length curve (Figure 2) — the paper's real evidence

RNNencdec's BLEU **drops sharply** as sentence length grows. RNNsearch-30 and -50 are far flatter, and **RNNsearch-50 shows no deterioration at all beyond length 50**.

This is the figure that proves the conjecture rather than merely winning the benchmark. It is also the direct rebuttal to [seq2seq §3.7](sutskever2014-sequence-to-sequence-learning.md)'s "surprisingly, the LSTM did not suffer on long sentences" — Sutskever et al. bought length robustness with the source-reversal trick, a workaround for the bottleneck; this paper removes the bottleneck, and gets the same robustness structurally.

## The alignment plots (§5.2.1, Figure 3)

Visualizing `α_ij` as a grayscale matrix gives a soft alignment between source and target words — an interpretable artifact that fell out of the mechanism unasked. English–French alignment is largely monotonic, so the matrices are strongly diagonal, with informative departures:

- **[European Economic Area] → [zone économique européenne].** The model aligns `zone` with `Area` — **jumping over two words** — then walks back one word at a time to complete the phrase. Adjective–noun order differs between the languages and the attention weights show the model handling it.
- **Soft beats hard, demonstrated concretely.** `[the man] → [l' homme]`: a hard alignment maps `the → l'`, but choosing between `le / la / les / l'` requires the *following* word. The soft alignment attends to both `the` and `man` and gets it right. Hard alignment also needs `[NULL]` tokens to handle length mismatches; soft alignment does not.

§5.2.2 gives long-sentence translations where RNNencdec-50 stays correct for roughly 30 words and then **drifts into fluent, wrong text** — replacing "based on his status as a health care worker at a hospital" with "based on his state of health," and in another example losing the closing quotation mark. RNNsearch-50 translates both correctly.

> [!note] Why the drift example is worth remembering
> RNNencdec does not degrade into noise; it degrades into **fluent output that has stopped being conditioned on the input.** Once the fixed vector's information about the later source content is exhausted, the decoder is a language model running free. That failure signature — locally plausible, globally unmoored, no drop in confidence — is the same one that shows up in long-horizon robot policies conditioned on a single pooled observation latent, and in LLM hallucination. It is a property of decoding from an under-informative conditioning vector, not of language.

## Position in the lineage

```
Bengio et al. 2003 — learned embedding table, fixed context window
   ↓
Mikolov et al. 2013 — embeddings as a reusable artifact, at scale
   ↓
Sutskever, Vinyals & Le 2014 — encoder → ONE fixed vector → AR decoder
   │   fixed-vector bottleneck; source-reversal as the workaround
   ↓
Bahdanau, Cho & Bengio 2014  (this paper)
   │   bidirectional encoder → per-target-word weighted read over all states
   │   alignment made soft and differentiable instead of latent
   │   "a mechanism of attention in the decoder"
   ↓
Vaswani et al. 2017 — keep attention, delete recurrence; dot-product scoring,
   │   K/V separation, multi-head, self-attention
   ↓
Everything in this wiki past Module 3
```

See [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md) for the full arc.

## Entities mentioned

- **[Dzmitry Bahdanau](../entities/dzmitry-bahdanau.md)** — first author; then a visiting student from Jacobs University Bremen.
- **[Kyunghyun Cho](../entities/kyunghyun-cho.md)** — second author; the RNNencdec baseline and the GRU are his.
- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — senior author. This closes the wiki's largest Bengio gap: he is the senior author of *both* [the paper that created the embedding table](bengio2003-neural-probabilistic-language-model.md) and the paper that created attention, eleven years apart.
- **[Ilya Sutskever](../entities/ilya-sutskever.md)** — via the [seq2seq](sutskever2014-sequence-to-sequence-learning.md) baseline this paper is positioned against.
- Schuster & Paliwal (bidirectional RNN), Zeiler (Adadelta), Goodfellow et al. (maxout), Kalchbrenner & Blunsom, Graves — cited, none ingested.

## Concepts touched

- **[Attention](../glossary.md#attention)** / **[cross-attention](../glossary.md#ca)** — originates here.
- **[Soft alignment](../glossary.md#soft-alignment)** — added to the glossary by this ingest.
- **[RNN](../glossary.md#rnn)**, **[GRU](../glossary.md#gru)**, **[beam search](../glossary.md#beam-search)**.
- **Encoder–decoder** — [Module 3 §8](../syntheses/curriculum/curriculum-03-attention-and-transformers.md).

## Open questions / TBD

- **Luong et al. 2015** (dot-product and general attention scoring, the bridge from this paper's additive scorer to Vaswani's) is un-ingested and is the missing intermediate step.
- **Sennrich et al. 2016 (BPE)** — the fix for the `[UNK]` problem that dominates Table 1's `All` column, and the reason modern models have no vocabulary shortlist. Not in the wiki.
- **Whether attention weights are explanations.** §5.2.1 reads the `α_ij` matrices as alignments and they are persuasive. A later literature ("Attention is not Explanation" / "Attention is not not Explanation," 2019) disputes how much interpretive weight they carry. The wiki cites attention maps nowhere as evidence yet, but should know the argument exists before it does.
