---
title: "On the Properties of Neural Machine Translation: Encoder–Decoder Approaches (Cho, van Merriënboer, Bahdanau, Bengio, SSST-8 2014)"
type: source
url: https://arxiv.org/abs/1409.1259
local_path: raw/1409.1259v2.pdf
sha256: 0a947ddd0fa96198d776f6a9f5e59f37b0965e9658eea41e4b574c25f2842528
author: Kyunghyun Cho, Bart van Merriënboer, Dzmitry Bahdanau, Yoshua Bengio
affiliation: Université de Montréal; Jacobs University Bremen (Bahdanau, visiting Montréal); Bengio CIFAR Senior Fellow
venue: "SSST-8, Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation (Doha, Oct 2014); arXiv 1409.1259"
published: 2014-09-03 (v1); v2 2014-10-07
ingested: 2026-08-30
tags: [encoder-decoder, sentence-length, unknown-words, inductive-bias, grconv, unsupervised-parsing, machine-translation, cho, bahdanau, bengio, analysis-paper]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/1409.1259v2.pdf`, 9 pages), pages 1–8 in full; references skimmed. Table 1 re-extracted in layout mode. Figures 4–6 are plots and a parse-tree visualization, described from their captions and the surrounding text.

## Summary

**"On the Properties of Neural Machine Translation: Encoder–Decoder Approaches"** — Cho, van Merriënboer, Bahdanau & Bengio (Montréal + Jacobs Bremen; SSST-8 workshop, Oct 2014). **The measurement behind the attention paper's conjecture**, and the source this wiki had been asserting without holding.

It is an **analysis paper**, not an architecture paper — unusual for 2014 and the reason it is worth reading. Its stated aim, in the authors' own words in §4.2, is *"to understand the **inductive bias** of the encoder–decoder approach on the translation performance measured by BLEU"* — the wiki's [inductive bias](../concepts/learning/inductive-bias.md) page could take this as its motto.

Two findings and one side contribution:

1. **Quality collapses with source-sentence length.** Both models do well on short sentences and "suffer significantly as the length of the sentences increases."
2. **Quality collapses with the number of unknown words**, which at a 30k vocabulary is a large share of real sentences.
3. **grConv** — a *gated recursive convolutional* encoder, introduced here, which turns out to perform **unsupervised parsing**: its gating coefficients form a tree over the source sentence with no syntactic supervision.

**Why it matters to this wiki.** [Bahdanau, Cho & Bengio](bahdanau2014-neural-machine-translation-align-translate.md) open with *"Cho et al. (2014b) showed that indeed the performance of a basic encoder–decoder deteriorates rapidly as the length of an input sentence increases."* That sentence is the empirical foundation of attention, and until now the wiki repeated it on faith. It is now sourced — **and reading the primary changes the story in two ways the secondary citation does not convey.**

> [!warning] The paper's own conclusion blames the **decoder**, not the fixed-length vector
> §5.1 offers the familiar hypothesis: *"The most obvious explanatory hypothesis is that the fixed-length vector representation does not have enough capacity to encode a long sentence with complicated structure and meaning. In order to encode a variable-length sequence, a neural network may 'sacrifice' some of the important topics in the input sentence in order to remember others."*
>
> But §6 reaches a **different** conclusion from the full evidence: *"Despite the radical difference in the architecture between RNN and grConv which were used as an encoder, **both models suffer from the curse of sentence length. This suggests that it may be due to the lack of representational power in the decoder.**"*
>
> That is a real distinction, and it is the payoff of having tested two structurally unrelated encoders. If swapping a recurrent encoder for a recursive-convolutional one changes nothing, the encoder is not obviously the culprit. [Attention](bahdanau2014-neural-machine-translation-align-translate.md) is usually narrated as "the fixed vector was the bottleneck, so it was removed" — this paper's authors, on their own data, leaned the other way. Attention arguably splits the difference: it changes neither encoder nor decoder in isolation but the **interface between them**, giving the decoder per-step access to everything the encoder produced. Cite this paper for the *measurement*; do not cite it as endorsing the fixed-vector diagnosis.

> [!note] It postdates the paper it motivates — by two days
> arXiv submission dates: [Bahdanau, Cho & Bengio](bahdanau2014-neural-machine-translation-align-translate.md) is **1 Sep 2014** (1409.0473); this paper is **3 Sep 2014** (1409.1259). The "prior finding" was posted *after* the fix.
>
> They are **concurrent companion papers from overlapping author lists** — Cho and Bahdanau and Bengio are on both — not a sequential discover-then-solve. The tidy narrative (someone measured a flaw, then someone else fixed it) is a retrospective artifact of citation order. What actually happened is one group diagnosing and repairing simultaneously, and choosing which paper to frame as analysis and which as architecture. Worth remembering whenever a lineage looks too clean; see [From n-grams to attention](../syntheses/sequence-models/language-model-to-transformer-lineage.md).

## Abstract (verbatim)

> "Neural machine translation is a relatively new approach to statistical machine translation based purely on neural networks. The neural machine translation models often consist of an encoder and a decoder. The encoder extracts a fixed-length representation from a variable-length input sentence, and the decoder generates a correct translation from this representation. In this paper, we focus on analyzing the properties of the neural machine translation using two models; RNN Encoder–Decoder and a newly proposed gated recursive convolutional neural network. We show that the neural machine translation performs relatively well on short sentences without unknown words, but its performance degrades rapidly as the length of the sentence and the number of unknown words increase. Furthermore, we find that the proposed gated recursive convolutional network learns a grammatical structure of a sentence automatically."

## The two encoders (§2)

Both models share a **decoder**: an RNN with the gated hidden unit from [Cho et al. 2014a](cho2014-rnn-encoder-decoder-phrase-representations.md) — the [GRU](../glossary.md#gru). Only the encoder differs, which is what makes the comparison informative.

**RNNenc** — the [RNN Encoder–Decoder](cho2014-rnn-encoder-decoder-phrase-representations.md), unchanged.

**grConv (gated recursive convolutional neural network)** — a binary convolutional network whose weights are applied **recursively** up a tree until a single fixed-length vector remains. At each level:

```
h(t)_j = ω_c · h̃(t)_j  +  ω_l · h(t−1)_{j−1}  +  ω_r · h(t−1)_j
h̃(t)_j = φ( W_l h(t)_{j−1} + W_r h(t)_j )
(ω_c, ω_l, ω_r) = softmax( G_l h(t)_{j−1} + G_r h(t)_j )
```

The three gate weights sum to 1, so each node **chooses** between a freshly computed activation, passing up its left child, or passing up its right child. In the hard-decision limit the network "adapts to the input and forms a tree-like structure" — the authors call it "a kind of unsupervised parsing."

### The grConv parse (Figure 6)

Given *"Obama is the President of the United States."*, the learned gating structure (edges with `ω > 0.1`) merges **"of the United States"** with **"is the President of"**, then combines that with **"Obama is"** and the final period — which the paper notes "is well correlated with our intuition."

> [!note] The side result is the more surprising one
> A model trained **only** on translation, with no syntactic supervision of any kind, produces a constituent structure a linguist would broadly recognize. The 2014 framing is modest — "we leave the further investigation of the structure learned by this model for future research" — but this is an early instance of a claim that recurs constantly afterward: **linguistic structure emerges as a byproduct of a sufficiently constrained prediction objective.** The modern descendants are BERT probing studies and mechanistic-interpretability circuit work. The architecture died; the observation did not.
>
> Note the honest framing, too: they report grConv as **losing** to RNNenc on BLEU and still argue the structural property is worth pursuing. A negative headline result with an interesting side finding, published as such.

## Experimental setup (§4)

- **Data**: the same 348M-word Axelrod-selected WMT'14 subset as [Cho et al. 2014a](cho2014-rnn-encoder-decoder-phrase-representations.md) and [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md) No monolingual data for the neural models. Evaluated on `news-test2012/2013/2014`, 3000 lines each.
- **Vocabulary**: the **30,000 most frequent words** in each language; the rest → `[UNK]`.
- **Training-length cap**: only sentence pairs where **both sides are ≤ 30 words**, for computational efficiency.
- **Models**: RNNenc 1000 hidden units with `tanh`; grConv 2000 hidden neurons with a rectifier. **620-dimensional word embeddings** in both, trained jointly.
- **Optimizer**: minibatch SGD with **AdaDelta**; orthogonal init of the transition matrix with spectral radius 1 (RNNenc) / 0.4 (grConv).
- **Budget**: both trained ~**110 hours** — 846,322 updates for RNNenc against **296,144** for grConv. **Neither was trained to convergence.**
- **Decoding**: beam search, beam width **10**, with two details that matter: hypotheses containing an unknown word are **excluded**, and log-probability is **length-normalized** to stop the decoder favouring short translations.

## Results (§5.1, Table 1)

### (a) All lengths

| Model | Development | **Test** |
|---|---|---|
| RNNenc | 13.15 | **13.92** |
| grConv | 9.97 | 9.97 |
| Moses | 30.64 | **33.30** |
| Moses + RNNenc ★ | 31.48 | 34.64 |
| Moses + LSTM ° | 32 | 35.65 |
| *— sentences with no unknown words —* | | |
| RNNenc | 21.01 | **23.45** |
| grConv | 17.19 | 18.22 |
| Moses | 32.77 | **35.63** |

(★ from [Cho et al. 2014a](cho2014-rnn-encoder-decoder-phrase-representations.md); ° from [Sutskever et al. 2014](sutskever2014-sequence-to-sequence-learning.md).)

### (b) 10–20 words

| Model | Development | **Test** |
|---|---|---|
| RNNenc | 19.12 | **20.99** |
| grConv | 16.60 | 17.50 |
| Moses | 28.92 | **32.00** |
| *— no unknown words —* | | |
| RNNenc | 24.73 | **27.03** |
| grConv | 21.74 | 22.94 |
| Moses | 32.20 | **35.40** |

And in the text: restricting **both** source and reference to 10–20 words *and* excluding unknown words gives **27.81 (RNNenc) vs 33.08 (Moses)** on test.

### What the numbers say

**The unrestricted gap is enormous — 13.92 vs 33.30 — and most of it is not about length.** Removing unknown-word sentences alone lifts RNNenc from 13.92 to 23.45, nearly ten BLEU. **The 30k vocabulary is doing more damage than the sentence-length effect the paper is named for.** That is the paper's second finding (Figure 4c) and it is arguably the bigger one; it is also the problem subword tokenization would later erase entirely, and BPE remains un-ingested here.

Stack the two restrictions and the gap narrows to 27.81 vs 33.08 — still a loss, but a different order of failure.

### Figure 5 — the contrast that makes it damning

Plotted against sentence length, **Moses' BLEU goes *up***: "the conventional system trained on the same dataset tends to get a higher BLEU score on longer sentences." The neural models' goes down.

This is what turns a limitation into a diagnosis. If everything degraded on long sentences, that would be a property of the task — long sentences are harder to score, or BLEU behaves oddly on them. **The incumbent improving where the challenger collapses localizes the failure in the architecture.** Worth copying as an evaluation habit: a degradation curve is only interpretable against a baseline's curve on the same axis.

## Caveats worth carrying

> [!warning] Training was capped at 30 words, and the headline claim is about longer sentences
> Models saw only pairs where both sides are ≤ 30 words. Measuring degradation **beyond** 30 words therefore mixes two effects: limited representational capacity, and plain **length extrapolation beyond the training distribution**. The paper partly anticipates this — *"we observed a similar trend even when we used sentences of up to 50 words to train these models"* — which helps, though no numbers are given for that run.
>
> The distinction matters for how the result transfers. "A fixed vector cannot hold a long sentence" is a capacity claim; "a model degrades outside its training length distribution" is a much more general and less interesting one. This experiment does not cleanly separate them.

- **grConv received a third of the gradient updates** (296k vs 846k) at equal wall-clock. Their own footnote 5 flags it: "Longer training may change the result, but for a fair comparison we chose to compare models which were trained for an equal amount of time." Equal-time rather than equal-steps is a defensible choice, stated openly — but it weakens "grConv loses to RNNenc," and therefore weakens the "both encoders fail identically, so blame the decoder" inference the conclusion rests on.
- **Neither model trained to convergence.**
- **Beam search excludes hypotheses containing `[UNK]`**, which interacts with the vocabulary finding: the decoder is forbidden from taking the escape hatch the training data gave it.

> [!warning] Contradiction inside the paper: the translation direction
> §1 ends *"We evaluate these two models on the task of translation **from French to English**."* §4.1 opens *"We evaluate the encoder–decoder models on the task of **English-to-French** translation."*
>
> **English→French is correct.** The Moses baseline of 30.64 / 33.30 is the WMT'14 En→Fr number carried over from [Cho et al. 2014a](cho2014-rnn-encoder-decoder-phrase-representations.md), and matched by [seq2seq](sutskever2014-sequence-to-sequence-learning.md) and [Bahdanau et al.](bahdanau2014-neural-machine-translation-align-translate.md) on the same task. The §1 sentence is an error.

## What this changes in the wiki

The [attention page](bahdanau2014-neural-machine-translation-align-translate.md) carried a warning that its central conjecture rested on an un-held source. That warning can now be replaced by a citation — with the two refinements above attached: the authors' own conclusion points at the **decoder**, and the two papers are **concurrent**, not sequential.

## Entities mentioned

- **[Kyunghyun Cho](../entities/kyunghyun-cho.md)** — first author; third paper of his 2014 trilogy in this wiki.
- **[Dzmitry Bahdanau](../entities/dzmitry-bahdanau.md)** — third author, "research done while visiting Université de Montréal"; two days after his own attention paper hit arXiv.
- **[Yoshua Bengio](../entities/yoshua-bengio.md)** — senior author.
- Bart van Merriënboer — co-author, Montréal.
- **[Ilya Sutskever](../entities/ilya-sutskever.md)** — the Moses+LSTM row in Table 1 is [seq2seq](sutskever2014-sequence-to-sequence-learning.md)'s rescoring result.
- Kalchbrenner & Blunsom, Moses, AdaDelta (Zeiler) — cited, not ingested.

## Concepts touched

- **[Inductive bias](../concepts/learning/inductive-bias.md)** — the paper's own framing of what it is measuring (§4.2).
- **Encoder–decoder** — [Module 3 §1.2](../syntheses/curriculum/curriculum-03-attention-and-transformers.md).
- **[Attention](../glossary.md#attention)** — the mechanism this measurement is used to motivate.
- **[GRU](../glossary.md#gru)** — the shared decoder cell.
- **[Beam search](../glossary.md#beam-search)** — with `UNK` exclusion and length normalization.

## Open questions / TBD

- **Was the decoder ever the answer?** The paper's §6 hypothesis — that the shared failure across two unrelated encoders implicates the decoder — was, as far as this ingest can tell, never directly tested. Attention changed the interface and the question was dropped rather than settled.
- **BPE / subword tokenization (Sennrich et al. 2016)** is un-ingested and is the fix for what Figure 4(c) measures — the second finding of this paper, and arguably the larger one.
- **grConv** appears to have no descendants. Unsupervised structure induction as a byproduct of a translation objective is a live idea; this particular architecture is not.
- **The 30-word training cap** leaves capacity and length-extrapolation confounded. A clean version of this experiment — train at long lengths, evaluate the capacity claim in isolation — does not appear to exist.
