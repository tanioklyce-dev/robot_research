---
title: "Attention Is All You Need (Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin, NeurIPS 2017)"
type: source
url: https://arxiv.org/abs/1706.03762
local_path: raw/1706.03762v7.pdf
author: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
affiliation: Google Brain, Google Research (Gomez at U Toronto)
published: 2017-06-12 (v1, arxiv); NeurIPS 2017 (Long Beach); v7 2023-08-02
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
tags: [transformer, attention, self-attention, multi-head, positional-encoding, vaswani, google-brain, foundational, neurips-2017, sequence-modeling]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/1706.03762v7.pdf`, 15 pages). Pages 1–10 read in full (architecture, attention math, positional encoding, complexity table, training setup, results, ablations). Pages 11–15 are references + appendix attention-visualizations, skimmed.

## Summary

**"Attention Is All You Need"** — Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin (Google Brain / Google Research; NeurIPS 2017, arxiv 1706.03762). The paper that introduces the **Transformer**: a sequence-transduction architecture built **entirely on attention**, with no recurrence and no convolution. It is the most-cited NN architecture paper of the 2010s and the foundation of essentially every modern large model — [LLMs](../glossary.md#llm), [ViTs](../glossary.md#vit), [VLA action heads](../concepts/vla-models.md), [JEPA](../concepts/jepa.md) predictors, [behavior transformers](bet-paper.md), [diffusion-policy](diffusion-policy-paper.md) backbones — all descend from this design.

**Headline results.** On WMT 2014 EN→DE the big Transformer reached **28.4 BLEU**, +2.0 over the previous best (including ensembles). On EN→FR, **41.8 BLEU** state-of-the-art among single models, at <1/4 the training cost of the previous SOTA. Trained on 8× P100 GPUs: base in 12 hours, big in 3.5 days. The Transformer also generalized to **English constituency parsing** (Section 6.3), suggesting the architecture was not specific to translation.

**Why it matters to this wiki.** Every architecture in the curriculum past Module 3 is either a transformer or contains transformer blocks. Specifically:

- **[ViT](../glossary.md#vit)** — applies the encoder stack to image patches; backbone of every [DINO](../entities/dinov3.md)-line and [JEPA](../concepts/jepa.md) encoder.
- **[LLMs](../glossary.md#llm)** — decoder-only transformers.
- **[VLAs](../concepts/vla-models.md)** — VLM (transformer) + action head (often a transformer).
- **JEPA predictors** — AR transformers operating on latent tokens (e.g. [LeWM](../entities/leworldmodel.md), [V-JEPA 2-AC](../entities/v-jepa-2.md)).
- **[Behavior Transformer / VQ-BeT](bet-paper.md)** — decoder-only transformer policies.

The paper is the **canonical reference for the [Transformer glossary entry](../glossary.md#transformer)** and for any time the wiki says "self-attention," "multi-head attention," "positional encoding," or "encoder-decoder."

## Abstract (verbatim)

> "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data."

## The architecture (Section 3, Figure 1)

The Transformer is an **encoder–decoder** stack of `N = 6` identical layers on each side, with `d_model = 512`, `d_ff = 2048` inside the FFN.

### Encoder layer
Two sub-layers per layer, each wrapped with **residual connection + LayerNorm**:

1. **Multi-head self-attention** — every position attends to every other position.
2. **Position-wise feed-forward** — `FFN(x) = max(0, xW_1 + b_1) W_2 + b_2`; equivalent to two 1×1 convolutions.

`LayerNorm(x + Sublayer(x))` is the post-norm form used in the original paper. (Pre-norm — `x + Sublayer(LayerNorm(x))` — became the default in later work.)

### Decoder layer
Three sub-layers per layer:

1. **Masked multi-head self-attention** — same as encoder, but masking future positions (set softmax inputs to −∞) to preserve the auto-regressive property.
2. **Encoder–decoder attention** ("cross-attention") — queries from the decoder, keys/values from the encoder output. This is how the decoder consults the source sequence.
3. **Position-wise FFN**.

### Scaled Dot-Product Attention (Section 3.2.1)

```
Attention(Q, K, V) = softmax( Q K^T / sqrt(d_k) ) V
```

Q, K, V are matrices of shape `(seq_len, d_k)` or `(seq_len, d_v)`. The **`1/sqrt(d_k)` scaling** is the paper's key innovation over prior dot-product attention: at large `d_k`, raw dot products grow with variance `d_k`, pushing softmax into low-gradient regions. The scaling pulls the variance back to 1.

### Multi-Head Attention (Section 3.2.2)

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) · W_O
head_i = Attention(Q W_Q^i, K W_K^i, V W_V^i)
```

In the paper: `h = 8` heads, `d_k = d_v = d_model / h = 64`. Total cost is comparable to single-head with full dimensionality, but each head can specialize on a different subspace.

### Three usages of attention in the architecture
1. **Encoder self-attention** — Q, K, V all from encoder.
2. **Decoder self-attention** — Q, K, V all from decoder (masked).
3. **Encoder–decoder cross-attention** — Q from decoder, K, V from encoder.

## Positional Encoding (Section 3.5)

Without recurrence or convolution, the model has no inherent notion of order. The paper injects position via **sinusoidal positional encodings** added to the input embeddings:

```
PE(pos, 2i)   = sin( pos / 10000^(2i/d_model) )
PE(pos, 2i+1) = cos( pos / 10000^(2i/d_model) )
```

Wavelengths form a geometric progression from `2π` to `10000 · 2π`. Chosen because for any fixed offset `k`, `PE(pos + k)` is a **linear function** of `PE(pos)` — this makes relative-position attention easy to learn. The paper tested learned positional embeddings (Section 6.2, Table 3 row E) and found nearly identical results; sinusoidal was kept on the hypothesis that it would extrapolate to longer sequences than seen at training.

> [!note] Lineage
> Modern descendants — **RoPE** (rotary position embedding), **ALiBi** (linear biases), **axial RoPE** in [DINOv3](../entities/dinov3.md) — all evolved from this position-injection problem. The original sinusoidal scheme is rarely used unchanged in 2026, but the abstraction "position information is added outside the attention mechanism" is still standard.

## Complexity (Section 4 / Table 1)

| Layer type | Complexity per layer | Sequential ops | Max path length |
|---|---|---|---|
| **Self-Attention** | `O(n² · d)` | `O(1)` | `O(1)` |
| Recurrent | `O(n · d²)` | `O(n)` | `O(n)` |
| Convolutional | `O(k · n · d²)` | `O(1)` | `O(log_k n)` |
| Self-Attention (restricted, neighborhood `r`) | `O(r · n · d)` | `O(1)` | `O(n/r)` |

**The key claim:** self-attention has **O(1) maximum path length** — any two positions can interact in a single layer. RNNs have `O(n)` path length, which is the root cause of their long-range dependency learning difficulty. This argument is the paper's analytical case for why attention should replace recurrence.

The `O(n²)` per-layer complexity is a real cost — every later "efficient transformer" (Linformer, Performer, FlashAttention, Mamba) chips at it — but for `n < d` (typical for sentence-level sequences), it is cheaper than the RNN's `O(n · d²)`.

## Training setup (Section 5)

- **Data:** WMT 2014 EN-DE (4.5M sentence pairs, ~37K BPE vocab); WMT 2014 EN-FR (36M, 32K word-piece vocab).
- **Hardware:** 8× NVIDIA P100 GPUs, one machine.
- **Base model:** 100K steps, 0.4 s/step, ~12 hours total.
- **Big model:** 300K steps, 1.0 s/step, ~3.5 days.
- **Optimizer:** Adam, `β₁ = 0.9`, `β₂ = 0.98`, `ε = 1e-9`.
- **LR schedule:** `lr = d_model^(-0.5) · min(step^(-0.5), step · warmup^(-1.5))`, with `warmup = 4000`. The famous **inverse-square-root with warmup** schedule.
- **Regularization:** residual dropout `P_drop = 0.1`; label smoothing `ε_ls = 0.1` (hurts perplexity but helps BLEU).

## Results (Section 6, Table 2)

| Model | EN-DE BLEU | EN-FR BLEU | Training FLOPs |
|---|---|---|---|
| GNMT + RL (ensemble) | 26.30 | 41.16 | 1.8·10²⁰ / 1.1·10²¹ |
| ConvS2S (ensemble) | 26.36 | 41.29 | 7.7·10¹⁹ / 1.2·10²¹ |
| **Transformer (base)** | **27.3** | **38.1** | **3.3·10¹⁸** |
| **Transformer (big)** | **28.4** | **41.8** | **2.3·10¹⁹** |

The big Transformer beats the best previous *ensembles* (single-model vs ensemble) at **~12× less compute** than the previous best ensemble for EN-FR.

### Ablations (Table 3)
- **Attention heads** — `h=1` is 0.9 BLEU worse than the best; quality drops off with too many heads (`h=32`). Default `h=8` was robust.
- **Reducing `d_k`** — hurts quality; "determining compatibility is not easy" (i.e., the dot-product compatibility function benefits from dimensionality).
- **Bigger models** — better.
- **Dropout** — very helpful (rows D).
- **Learned vs sinusoidal positional encoding** — nearly identical results (row E).

### Constituency parsing (Section 6.3, Table 4)

| Parser | WSJ-23 F1 |
|---|---|
| Vinyals & Kaiser 2014 (WSJ only) | 88.3 |
| Petrov et al. 2006 | 90.4 |
| Dyer et al. 2016 (WSJ only) | 91.7 |
| **Transformer (4 layers, WSJ only)** | **91.3** |
| **Transformer (4 layers, semi-supervised)** | **92.7** |

The Transformer trained only on 40K WSJ sentences hit 91.3 F1, beating Vinyals/Kaiser RNN seq2seq by 3 points on the same data. **This is the first signal that the architecture generalizes beyond translation** — the seed of the GPT/BERT/ViT explosion that followed.

## What the paper did not include

- **No causal-LM experiments.** The decoder-only / generative-pretraining direction emerged with GPT-1 (Radford et al., 2018) and was not in scope here. The paper is squarely encoder–decoder + supervised seq2seq.
- **No pre-norm.** The post-norm form (`LayerNorm(x + Sublayer(x))`) used in the paper is notoriously unstable at deeper depths; pre-norm + better init was a later fix.
- **No vision experiments.** [ViT (Dosovitskiy et al. 2020)](vit-paper.md) applied the encoder stack to images and is the bridge into this wiki's main subject matter.
- **No claim about scale.** The paper's "big" model is 213M parameters and trains in 3.5 days on 8 P100s. The architecture's scaling-law story — that performance keeps improving with `N`, `d_model`, and data — was discovered later (Kaplan et al. 2020, Chinchilla 2022).

## Entities mentioned

- **Google Brain** (now Google DeepMind) — primary affiliation; first author Ashish Vaswani and the lead architects.
- **Google Research** — co-affiliation.
- **Aidan N. Gomez** — only non-Google author (then at U Toronto); later founder of Cohere.
- The author list is famous for the *"Equal contribution. Listing order is random."* footnote — a deliberate egalitarian convention given the paper's eventual impact.

(None of the author entities have wiki pages yet; the Transformer authors as a cohort are wiki-relevant primarily as the architects of this single paper, not as recurring contributors to wiki-tracked research lines.)

## Concepts touched

- **[Transformer](../glossary.md#transformer)** — defined here; glossary entry already exists.
- **[Self-attention](../glossary.md#sa)** — the central operation; defined here.
- **[Multi-head attention](../glossary.md#mha)** — defined here.
- **[Positional encoding](../glossary.md#positional-encoding)** — the sinusoidal form is from this paper.
- **[ViT](../glossary.md#vit)** — descendant; applies the encoder stack to image patches.
- **[LLM](../glossary.md#llm)** — descendant; decoder-only transformers.
- **Encoder-decoder vs encoder-only vs decoder-only** — the three transformer "shapes" the glossary describes all originate from variations on this paper's design.

## Position in the lineage

```
Bahdanau et al. 2014 (attention for NMT, attached to RNN)
   ↓
"Attention Is All You Need" 2017 (this paper — attention WITHOUT RNN)
   ↓
GPT-1 (2018, decoder-only LM)         ↘
BERT (2018, encoder-only MLM)          → modern foundation models
ViT (2020, encoder on image patches)  ↗
   ↓
Every model in this wiki past Module 3:
- LLMs (GPT, Claude, Llama)
- DINOv2/v3 ViT encoders
- JEPA predictors (LeWM, V-JEPA 2-AC)
- BeT / VQ-BeT policies
- VLA action heads
- Diffusion Policy transformer backbones
```

The Transformer is one of two architectures the curriculum builds out from (the other being the **CNN**, Module 2). Where Module 2 is the spatial-inductive-bias architecture, Module 3 is the **sequence-as-set-of-tokens** architecture. Everything modern is a recombination of those two ideas, often with the transformer subsuming the CNN entirely (ViT).

## Curriculum hookup

This is the primary reference for **[Curriculum Module 3 — Sequence models, attention, and transformers](../syntheses/curriculum-03-attention-and-transformers.md)**. Module 3's content (self-attention, MHA, transformer blocks, positional encoding, causal masking, ViT) is essentially "read this paper and [Dosovitskiy 2020](vit-paper.md)." The wiki was tracking the lineage via the glossary entry and downstream papers; this ingest fills in the primary source.

## Open questions / TBD

- The **ablation table (Table 3)** is the empirical evidence behind many widely-repeated "transformer folklore" claims (e.g., "8 heads is enough"). Worth checking how well those still hold at scales 1000× larger.
- The paper's **constituency-parsing experiment** is rarely cited but historically important — first task generalization signal. Could anchor a synthesis on "when did people realize transformers were a general architecture, not a translation trick?"
- Modern descendants of the **positional-encoding** choice (RoPE, ALiBi, axial RoPE) are not yet ingested as separate sources, despite being foundational for the [DINOv3](../entities/dinov3.md) and modern-LLM stacks.
