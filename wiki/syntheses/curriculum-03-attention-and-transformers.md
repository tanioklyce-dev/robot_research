---
title: Curriculum Module 3 — Sequence models, attention, and transformers
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-3, transformer, attention, self-attention, multi-head-attention, vit, positional-encoding, causal-masking, rnn, lstm]
prereqs: [curriculum-01, curriculum-02]
status: draft
---

> [!note] Curriculum context
> This is **Module 3** of the [Robot-learning curriculum](robot-learning-curriculum.md). Tier 1. Prerequisites: [Module 1](curriculum-01-neural-networks.md) (NN basics) and [Module 2](curriculum-02-cnns.md) (the CNN/ViT comparison only makes sense after CNN).
>
> Heavy load: [LeWM](../entities/leworldmodel.md)'s encoder is a ViT; its predictor is a **causal autoregressive transformer**. [BeT](../entities/bet.md) is a transformer over actions. Every [VLA](curriculum-09-vla.md) is a transformer at the trunk. If transformers are unfamiliar, read carefully.
>
> Acronyms used here are also in the [Glossary](../glossary.md). First-mention links go there.

## Prereq diagnostic

Can you answer these without notes?

1. Write the formula for scaled dot-product attention: `Attention(Q, K, V) = ?`
2. What's the difference between encoder-only, decoder-only, and encoder-decoder transformer architectures? Give one example of each.
3. Why does multi-head attention work better than single-head attention with the same total parameter count?
4. How does ViT differ from a CNN in how it processes a 224×224 image?
5. What does the [CLS] token do in ViT?

If yes to all five, skim and do the anchor exercise. If no to any, read the relevant section.

## What this module is

The transformer family — from attention as an alternative to recurrence to ViT as the dominant 2024–2026 visual backbone. By the end you should be able to:

1. Write the scaled-dot-product attention formula and the multi-head attention block in code or on paper.
2. Read any transformer paper's architecture diagram (LN → attn → residual → LN → MLP → residual) and predict parameter counts.
3. Distinguish self-attention from cross-attention; encoder-only from decoder-only.
4. Explain why ViT can be applied to images by patching them, and what the tradeoff vs CNN is.
5. Recognize causal masking in autoregressive models (LeWM's predictor; GPT-line LLMs).

## §1 — Sequence models before attention (briefly)

For context only. **You can largely skip this section if your goal is forward-looking.**

### RNNs

A [recurrent neural network ([RNN](../glossary.md#rnn))](https://en.wikipedia.org/wiki/Recurrent_neural_network) processes a sequence one timestep at a time, maintaining a hidden state:

```
h_t = σ(W_h h_{t-1} + W_x x_t + b)
y_t = W_y h_t
```

**Problems:**
- **Vanishing gradients** — back-propagating through 100+ timesteps multiplies Jacobians; gradients shrink to zero. RNNs can't model long-range dependencies.
- **Sequential** — `h_t` depends on `h_{t-1}`, so you can't parallelize across timesteps. Training is slow.

### LSTMs

[Long Short-Term Memory ([LSTM](../glossary.md#lstm))](https://en.wikipedia.org/wiki/Long_short-term_memory) (Hochreiter & Schmidhuber 1997) — RNN variant with **gating mechanisms** that let the network choose what to remember and what to forget. Solves vanishing gradients for moderate-length sequences (~100 steps). Pre-2018 standard for sequence modeling.

[GRU (Gated Recurrent Unit)](../glossary.md#gru) is a simpler LSTM variant with fewer gates. Same role.

### Why RNNs / LSTMs are superseded

[Vaswani et al. 2017 ("Attention Is All You Need")](https://arxiv.org/abs/1706.03762) showed that **attention alone** (no recurrence) outperforms LSTMs on machine translation and parallelizes much better. By 2018 transformers had eaten BERT-class language tasks; by 2020 they had eaten everything else.

In 2024–2026 robotics: LSTMs appear occasionally (e.g., `LSTM-GMM` baseline in Diffusion Policy), but the curriculum's interesting architectures are all transformer-based.

## §2 — Attention: the core mechanism

The single most important idea in 2017+ deep learning.

### The motivation

A sequence model needs to combine information across many positions. RNNs do this *sequentially* (each step sees the previous step's hidden state). CNNs do this *locally* (each output sees a fixed-size receptive field).

Attention is different: **every position attends directly to every other position.** Long-range dependencies are no harder than short-range ones.

### Scaled dot-product attention

The formula:

```
Attention(Q, K, V)  =  softmax( Q K^T / √d_k ) · V         (Eq. 2.1)
```

where:
- `Q ∈ ℝ^{n × d_k}` — query vectors (`n` positions, `d_k`-dimensional each).
- `K ∈ ℝ^{n × d_k}` — key vectors.
- `V ∈ ℝ^{n × d_v}` — value vectors.
- `softmax` is applied row-wise.

Reading: for each query (row of `Q`), compute its dot product with every key (rows of `K`); these dot products are *attention scores*. Softmax them into a probability distribution; use this distribution to take a weighted average of the value vectors. Each output position is a *weighted combination of all input positions*, with weights determined by query-key similarity.

The `√d_k` scaling prevents the softmax from saturating for large `d_k` (the variance of `Q K^T` grows with `d_k`, so without scaling the softmax becomes one-hot and gradients vanish).

### Self-attention

When `Q`, `K`, `V` are all linear projections of the **same** input sequence `X ∈ ℝ^{n × d_model}`:

```
Q = X W_Q,   K = X W_K,   V = X W_V              W_Q, W_K, W_V ∈ ℝ^{d_model × d_k}
Output = Attention(Q, K, V)                       ∈ ℝ^{n × d_v}
```

Each position attends to all positions of the same sequence. **This is the building block of every transformer.**

### Cross-attention

When `Q` comes from one sequence and `K`, `V` from another:

```
Q = X_dec W_Q,   K = X_enc W_K,   V = X_enc W_V
```

The decoder attends to the encoder. Used in encoder-decoder transformers (translation, image-to-text) and in CFG-style conditioning ([Module 5 §9](curriculum-05-generative-models.md)).

## §3 — Multi-head attention ([MHA](../glossary.md#mha))

Single-head attention has limited expressive capacity: each output is *one* weighted combination of values. Multi-head attention runs `h` separate attention operations in parallel, then concatenates:

```
head_i  =  Attention( X W_Q^i, X W_K^i, X W_V^i )           // i = 1..h
MHA(X)  =  Concat(head_1, ..., head_h) · W_O                // W_O ∈ ℝ^{h·d_v × d_model}
```

Each head can specialize in a different relationship type (syntactic, semantic, positional, etc.). Typical `h = 8` or `16`. Total parameters are similar to a single big attention head, but the parallel structure is empirically much better.

### Why MHA works

Three soft intuitions:

1. **Different heads attend to different things.** Syntactic head, content head, positional head, etc.
2. **Softmax bottlenecks** — softmax in (2.1) can attend strongly to only one position at a time. MHA gives you `h` parallel attendings.
3. **Inductive bias** — splitting the attention space into `h` smaller spaces regularizes the model.

## §4 — The transformer block

The architectural unit. Each transformer block applies:

```
input: x ∈ ℝ^{n × d_model}
y = x + MHA( LN(x) )                                      // attention sublayer with residual
z = y + MLP( LN(y) )                                      // feedforward sublayer with residual
output: z
```

Two sublayers:
- **MHA sublayer** — multi-head self-attention. Mixes information across positions.
- **MLP sublayer** — two-layer feedforward network applied position-wise (the same MLP at every position; no cross-position mixing here). The "feature transformation" sublayer.

Both wrapped in **Layer Norm + residual** (per [Module 1 §5, §6](curriculum-01-neural-networks.md)). This is the modern "pre-norm" transformer; some papers use "post-norm" (`y = LN(x + MHA(x))`). Pre-norm trains more stably.

A transformer model stacks `L` such blocks. Standard sizes:
- **ViT-Tiny**: 12 blocks, `d_model = 192`, ~5M params. Used by [LeWM](../entities/leworldmodel.md).
- **ViT-Base**: 12 blocks, `d_model = 768`, ~86M params.
- **ViT-Large**: 24 blocks, `d_model = 1024`, ~300M params.
- **ViT-Huge / ViT-g**: 32 blocks, `d_model = 1280–1664`, ~600M–2B params. The 1B-param V-JEPA 2 encoder is ViT-g class.

### Why this structure works

Two key properties:

1. **Attention is permutation-equivariant** — without positional encoding, the transformer doesn't know token order. We fix this in §5.
2. **Each block has full receptive field** — every position sees every other position in one block. Compare CNN's receptive field that grows with depth. Transformers can model long-range dependencies in one layer.

## §5 — Positional encoding

Because attention is permutation-equivariant, we need to inject positional information. Three common approaches:

### Sinusoidal positional encoding (Vaswani et al. 2017)

For position `p` and dimension `j`:

```
PE(p, 2j)   = sin( p / 10000^(2j/d_model) )
PE(p, 2j+1) = cos( p / 10000^(2j/d_model) )
```

Add `PE` to the input embedding. No learnable parameters. Generalizes to longer sequences than seen at training.

### Learned positional encoding

`PE = nn.Embedding(max_position, d_model)`. Learnable. Doesn't generalize beyond training length but works fine within it. Used by ViT.

### Rotary Position Embedding (RoPE)

Su et al. 2021. Rotate query and key vectors by position-dependent angles. Generalizes better than learned PE; used by [V-JEPA 2](../entities/v-jepa-2.md) (3D-RoPE for spatial-temporal positions) and many modern LLMs (Llama, Gemma).

## §6 — Causal masking

For **autoregressive** models — those that predict token `t+1` from tokens `1..t` — we need to prevent attention from looking at future tokens. **Causal masking** zeros out the upper triangle of the attention score matrix:

```
mask[i, j]  =  0 if j ≤ i else -∞
scores  =  Q K^T / √d_k + mask
attention_weights  =  softmax(scores)
```

The `-∞` mask becomes 0 after softmax, so position `i` only attends to positions `1..i`.

### Where causal masking appears

- **GPT-line LLMs** — predict next text token. Causal mask applied throughout.
- **[LeWM](../entities/leworldmodel.md)'s predictor** — causal AR transformer over `(z_t, a_t) → z_{t+1}`. The predictor "sees" the current latent and action, predicts the next latent, autoregressively over time.
- **[BeT](../entities/bet.md)** — transformer over actions; causal mask over the action sequence.
- **[Diffusion Policy](../entities/diffusion-policy.md)** — causal masking over the predicted action chunk in some variants.

The general rule: if the model is predicting timestep `t+1` from timesteps `1..t` at inference, causal masking should be present at training so the model doesn't cheat by looking at `t+1` when learning to predict it.

## §7 — Vision Transformer ([ViT](../glossary.md#vit))

[Dosovitskiy et al. 2020 ("An Image Is Worth 16×16 Words")](../sources/vit-paper.md) — applied the transformer directly to images by treating image patches as tokens.

### The recipe

1. **Split the image** into non-overlapping patches. For a 224×224 image and 16×16 patches: 14×14 = 196 patches.
2. **Flatten each patch** into a vector. For a 16×16×3 RGB patch: a 768-dim vector. Linear-project to `d_model` (typically also 768).
3. **Prepend a `[CLS]` token** — a learnable embedding that's also processed by the transformer. Its final-layer output is used as the image-level representation.
4. **Add positional encoding** (learned or sinusoidal; ViT uses learned).
5. **Run through `L` transformer blocks.**
6. **Output:** the `[CLS]` token embedding at the final layer.

### Why this works

- **Patches are tokens.** Each patch's flattened vector is processed as a sequence element. The transformer's self-attention mixes information across all patches in one block — much faster receptive-field growth than CNN.
- **No image-specific inductive bias.** ViT doesn't know about translation equivariance, locality, etc. It learns them from data. Needs **more data** than CNN to do well (ImageNet-1k is borderline; ImageNet-21k or larger works much better).
- **Scales better.** Empirically, ViT scales to billions of parameters more gracefully than CNN. The biggest CNNs are ~600M params; ViT-g is 1B+; V-JEPA 2 trains at 2B parameters.

### The `[CLS]` token

The standard trick for getting a single image-level vector from the transformer. The `[CLS]` token has no input meaning — it's a learnable parameter. After the transformer attends across all patches and the `[CLS]` token, the `[CLS]` final embedding aggregates global information about the image.

[LeWM](../entities/leworldmodel.md) uses ViT-Tiny with the `[CLS]` token + a projection MLP as its encoder. [DINO-WM](../entities/dino-wm.md) uses **all** patch embeddings (not just `[CLS]`) for richer spatial information. Different design choices, different downstream consequences.

### ViT vs CNN — when to pick which

Per [Module 2 §7](curriculum-02-cnns.md):
- CNN wins on small datasets and modest compute.
- ViT wins with large data and large-scale pretraining (DINOv2, CLIP, V-JEPA).

For BC-line robotics in 2026, **ResNet-18 is still the default** because BC's data scales are modest. For JEPA-line, **ViT is the default** because the JEPA pretraining setup loves the scaling properties.

## §8 — Encoder-only vs decoder-only vs encoder-decoder

Three architectural families based on attention pattern:

### Encoder-only (bidirectional)

- All positions attend to all positions. No causal mask.
- Used for: classification, embedding, pretraining-then-fine-tune setups.
- Examples: BERT, ViT (`[CLS]` head), most SSL encoders ([DINOv2](../entities/dinov2.md), V-JEPA encoders).

### Decoder-only (autoregressive)

- Causal mask throughout; each position attends only to past positions.
- Used for: language generation, action generation, any autoregressive prediction.
- Examples: GPT-family LLMs, [LeWM](../entities/leworldmodel.md)'s predictor, [BeT](../entities/bet.md).

### Encoder-decoder

- Encoder: bidirectional. Decoder: autoregressive + cross-attention to encoder.
- Used for: translation, image captioning, encoder-conditioned generation.
- Examples: original Vaswani 2017 transformer (translation), T5, BART, [VLM](../glossary.md#vlm)s (encoder = vision tower, decoder = autoregressive text head).

Most VLAs ([Module 9](curriculum-09-vla.md)) inherit VLM architectures — typically encoder-decoder or decoder-only.

## §9 — Brief on training transformers

Practical tips that aren't in earlier modules:

- **Warmup learning rate** — transformers are sensitive to early training instability. Linear warmup over the first 1k-10k steps before switching to cosine decay.
- **Gradient clipping** — clip gradient norms to ~1.0. Prevents loss spikes from blowing up the training.
- **Mixed-precision training (FP16/BF16)** — essential for transformers at scale. Use PyTorch's `torch.autocast`.
- **Don't use BN** — Layer Norm is the standard. BN doesn't compose with transformer's variable-length sequences.
- **Weight initialization matters** — use Xavier / He initialization tweaked for transformer scale; default PyTorch init is often suboptimal.

## Anchor exercise

> **Patch a 64×64 PushT frame into 8×8 tokens, run them through a 2-layer transformer, inspect attention maps.**

Concrete:

1. **Get the data.** Use the PushT dataset from [LeWM howto](leworldmodel-howto.md) or `diffusion_policy`. Pick ~20 frames at 64×64 resolution.
2. **Patch the image.** 8×8 patches → 8×8 = 64 patches per image. Each patch is 8·8·3 = 192-dim (assuming RGB).
3. **Build a tiny transformer.** 2 blocks, `d_model = 128`, 4 heads. Prepend a `[CLS]` token. Learnable positional encoding. ~50k parameters.
4. **Train.** Goal doesn't matter much — train to reconstruct the PushT state (block position + angle) from the `[CLS]` embedding via a small MLP head. ~1k iterations, AdamW.
5. **Visualize attention.** Pick a few frames; extract the attention weights from the `[CLS]` token to each patch in layer 2; visualize as a heatmap over the original image. **You should see the model attending to the T-block and the pusher.**
6. **Compare to random.** Visualize attention from a randomly-initialized transformer. Should be diffuse.

The point: feel how **attention maps are interpretable** — they tell you where the model is "looking." Compare to a CNN's feature maps (Module 2); the visualizations are different but the role is similar (showing what the model focuses on).

Deeper variant: try patch sizes of 4×4, 8×8, 16×16. Smaller patches = more tokens = slower but more spatial detail. Pick the patch size that matches your task's spatial resolution needs. This is the same trade-off LeWM made when choosing patch-size 14 for its ViT-Tiny.

## Recommended reading

In order:

1. **[Vaswani et al. 2017 — "Attention Is All You Need"](../sources/attention-is-all-you-need.md)** (arxiv 1706.03762) — the original transformer paper. Read the abstract + §3 (model architecture). The math is in §3.2.
2. **Karpathy's [nanoGPT](../sources/karpathy-nanogpt.md)** — a clean 300-line GPT implementation. Read the `model.py`; it's the cleanest transformer implementation I know. *Deprecated November 2025 in favour of [nanochat](../sources/karpathy-nanochat.md)* — but for the *architecture-reading* purpose of this module, `nanoGPT/model.py` is still the simpler and more pedagogical read. Use [nanochat](../sources/karpathy-nanochat.md) when you want to actually train an end-to-end ChatGPT-capability LLM (tokenizer + pretrain + SFT + RL + chat UI for ~$48 on an 8XH100 node).
3. **[Dosovitskiy et al. 2020 — ViT paper](../sources/vit-paper.md)** (arxiv 2010.11929) — the original ViT. Read the abstract + §3 (method). Compare against §4 (their CNN-vs-ViT data-scaling experiments).
4. **The Annotated Transformer** ([rush-nlp.com](http://nlp.seas.harvard.edu/annotated-transformer/)) — Vaswani et al. 2017 rewritten as runnable PyTorch with annotations. Excellent for "I understand it; now show me code."
5. **Lilian Weng — [The Transformer Family](https://lilianweng.github.io/posts/2020-04-07-the-transformer-family/)** — survey of transformer variants. Useful for vocabulary.

## What you should now be able to do

- Write scaled dot-product attention and multi-head attention from memory.
- Read a paper's transformer architecture diagram (LN → attn → residual → LN → MLP → residual) and predict parameter counts and FLOPs.
- Recognize when a model is encoder-only / decoder-only / encoder-decoder from its attention pattern.
- Decide between CNN and ViT for a new task based on dataset size, pretraining availability, and compute budget.
- Understand the [CLS] token role and the patch-tokenization trick.
- Identify causal masking in any AR model.

## Hand-off

Module 3 is foundational for:

- **[Module 4](curriculum-04-self-supervised-learning.md) — SSL** — many SSL methods use transformers as the encoder.
- **[Module 5](curriculum-05-generative-models.md) — Generative models** — transformer-based diffusion (DiT) is a variant of DDPM with a transformer backbone instead of U-Net.
- **[Module 7](curriculum-07-bc-lineage-pusht.md) — BC lineage** — BeT is transformer-based; Diffusion Policy has transformer variants.
- **[Module 9](curriculum-09-vla.md) — VLA** — every VLA's trunk is a transformer.
- **[Module 11](curriculum-11-jepa-deep.md) — JEPA depth** — ViT is the encoder; AR transformer is the predictor.
- **[Module 12](curriculum-12-lewm-deep-dive.md) — LeWM** — the entire architecture is ViT-Tiny encoder + causal AR transformer predictor.

## Related curriculum modules

- **[Module 1](curriculum-01-neural-networks.md)** — prerequisite (LN, residual, MLP).
- **[Module 2](curriculum-02-cnns.md)** — sibling (CNN-vs-ViT axis).
- All Tier 3–5 modules consume transformer machinery.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- **A "transformer training pathologies" page** — learning-rate warmup, gradient clipping, NaN-loss-recovery — would help downstream module readers.
- **DiT (Diffusion Transformer)** — Peebles & Xie 2023, transformer backbone for diffusion instead of U-Net; used by Sora, Stable Diffusion 3. Should be a wiki source page if the curriculum picks up DiT-line work.
