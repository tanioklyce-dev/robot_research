---
title: "An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale (Dosovitskiy et al., ICLR 2021)"
type: source
url: https://arxiv.org/abs/2010.11929
local_path: raw/2010.11929v2.pdf
author: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby
affiliation: Google Research, Brain Team
published: 2020-10-22 (v1 arxiv); ICLR 2021; v2 2021-06-03
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
tags: [vit, vision-transformer, transformer, attention, patches, classification, imagenet, jft-300m, foundational, iclr-2021, google-research]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2010.11929v2.pdf`, 22 pages). Pages 1–9 (main paper: method, experiments, scaling study, attention probing, self-supervision teaser) read in full. Pages 10–22 (references + Appendix A multi-head self-attention; Appendix B hyperparameters; Appendix C–E ablations, augmentation, head types, position-embedding variants, attention-distance figures) skimmed for the position-embedding and inductive-bias details cited below.

## Summary

**"An Image Is Worth 16x16 Words"** — Dosovitskiy, Beyer, Kolesnikov, Weissenborn, Zhai, Unterthiner, Dehghani, Minderer, Heigold, Gelly, Uszkoreit, Houlsby (Google Research, Brain Team; ICLR 2021, arxiv 2010.11929). The paper that introduces the **Vision Transformer (ViT)**: split an image into a grid of non-overlapping patches (16×16 or 14×14 pixels), flatten + linearly project each patch into a token, prepend a learnable `[CLS]` token, add learned 1D positional embeddings, and feed the resulting sequence through a standard [transformer](attention-is-all-you-need.md) encoder — *no convolutions anywhere*. The `[CLS]` token's final-layer output is the image representation; a small MLP / linear head reads off the class.

**Headline result.** Pre-trained on JFT-300M (303M images, 18K classes), ViT-H/14 reaches **88.55% ImageNet top-1**, 90.72% on ImageNet-ReaL, 94.55% CIFAR-100, and **77.63% on the 19-task VTAB suite** — matching or beating contemporary ResNet-based state of the art (BiT-L, Noisy Student) at **2–4× less pre-training compute**. The smaller ViT-L/16 pre-trained on the *public* ImageNet-21k (14M images, 21K classes) is "trainable in ~30 days on a cloud TPUv3 with 8 cores" — making the architecture accessible outside Google.

**The central empirical claim.** *Large-scale training trumps inductive bias.* CNNs bake in locality, two-dimensional neighborhood structure, and translation equivariance at every layer; ViT has none of that — its self-attention layers are global, only the MLPs are local. On mid-sized datasets (ImageNet alone, ~1.3M images), ViT underperforms ResNets of comparable size, exactly because of the missing inductive bias. But at ImageNet-21k scale (14M images) the gap closes, and at JFT-300M scale (303M images) ViT overtakes — and ResNets *plateau* while ViT *keeps improving*. This is the data-scaling argument that drove the entire 2021–2026 transition of vision foundation models from CNN backbones to ViT backbones.

**Why it matters to this wiki.** Every visual [encoder](../glossary.md#encoder) downstream of Module 2 in the [robot-learning curriculum](../syntheses/curriculum/robot-learning-curriculum.md) — [DINOv2](../entities/dinov2.md), [DINOv3](../entities/dinov3.md), [V-JEPA 2](../entities/v-jepa-2.md), [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [DINO-world](../entities/dino-world.md), [JEPA-WMs](../entities/jepa-wms.md), [PLDM](../sources/pldm-paper.md), [LeJEPA](../sources/lejepa-paper.md) — is a ViT, and most of them are descended specifically from the patch tokenization + learned positional embedding + `[CLS]` recipe in this paper. The wiki was tracking ViT via the [glossary entry](../glossary.md#vit) and many downstream sources; this ingest fills in the primary reference.

## Abstract (verbatim, §0)

> "While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train."

## The architecture (Section 3, Figure 1)

The Vision Transformer is the [Vaswani et al. 2017](attention-is-all-you-need.md) **encoder stack**, unmodified, applied to a sequence of image-patch tokens. The contribution is the **tokenization recipe**, not a new transformer block.

### Patch tokenization (Eq. 1)

```
x ∈ R^{H×W×C}                # input image
x_p ∈ R^{N × (P²·C)}          # N = HW/P²  non-overlapping P×P patches, each flattened
z_0 = [ x_class ; x_p^1 E ; x_p^2 E ; ... ; x_p^N E ] + E_pos
E ∈ R^{(P²·C) × D},  E_pos ∈ R^{(N+1) × D}
```

- Patch size `P`: 14 or 16 (denoted ViT-L/16, ViT-H/14, etc.). Smaller patches → longer sequence → more compute. Sequence length is `N+1` (+1 for the `[CLS]` token), inversely proportional to `P²`.
- `E` is a single shared **trainable linear projection** that maps each `P²·C`-dim flattened patch to a `D`-dim token. This is the entire "stem" of the model — no convolutional preprocessing, no patch overlap.
- `x_class` is a **learnable `[CLS]` token** prepended to the sequence, in the spirit of BERT's `[CLS]`. Its final-layer output `z_L^0` (after a final LayerNorm) is the image representation `y` (Eq. 4) and the only token the classification head reads.
- `E_pos` is a **learned 1D position embedding** added element-wise to the token sequence. The authors tested 2D-aware embeddings (Appendix D.4) and found nearly no benefit — the model learns 2D image topology in the embeddings anyway (Figure 7, center: closer patches → more similar position embeddings; row–column structure emerges).

### Transformer block (Eq. 2, 3)

```
z'_ℓ = MSA(LN(z_{ℓ-1})) + z_{ℓ-1}            ℓ = 1..L
z_ℓ  = MLP(LN(z'_ℓ))    + z'_ℓ                ℓ = 1..L
y    = LN(z_L^0)
```

- **Pre-norm:** LayerNorm is applied *before* MSA/MLP (cf. the original Transformer's post-norm; see the source page for [Vaswani et al. 2017](attention-is-all-you-need.md)). ViT uses pre-norm because at the depth/width regimes considered, pre-norm is more training-stable.
- **MLP:** two linear layers with a **GELU** nonlinearity in between (`d_ff = 4 × d_model`).
- **Multi-head self-attention (MSA):** standard scaled dot-product attention with `h` heads (Appendix A walks through the math, identical to Vaswani et al.).

### Model variants (Table 1, §4.1)

Hyperparameter conventions are borrowed from BERT:

| Model | Layers L | d_model | MLP d_ff | Heads h | Params |
|---|---|---|---|---|---|
| **ViT-Base** | 12 | 768 | 3072 | 12 | 86M |
| **ViT-Large** | 24 | 1024 | 4096 | 16 | 307M |
| **ViT-Huge** | 32 | 1280 | 5120 | 16 | 632M |

Naming convention: `ViT-L/16` = Large variant with 16×16 patches. Modern descendants extend this in both directions — ViT-S/14, ViT-g/14 (1.1B, [DINOv2](../entities/dinov2.md)), ViT-7B/16 ([DINOv3](../entities/dinov3.md)) — but the ViT-B / ViT-L / ViT-H sizes from this paper are still the workhorse research sizes.

### Hybrid architecture (§3.1, end)

As an alternative to raw image patches, the input sequence can be formed from feature maps of a CNN (e.g., ResNet50 stage 4 output). The paper studies this "hybrid" variant in the scaling experiments (Figure 5). The finding: **hybrids beat pure ViT at small compute budgets, but the gap vanishes at large compute** — i.e., the CNN inductive bias is helpful when data is small but unnecessary when data is large.

## Fine-tuning and higher resolution (§3.2)

ViT pre-trained on JFT-300M / ImageNet-21k is fine-tuned on downstream tasks by:

1. Removing the pre-trained MLP head; attaching a zero-initialized `D × K` linear layer for `K` downstream classes.
2. Fine-tuning at **higher resolution** than pre-training (e.g., pretrained at 224, fine-tuned at 384/512). The patch size is *kept fixed*, so the effective sequence length grows.
3. **Pre-trained positional embeddings are 2D-interpolated** to fit the new spatial grid — the only point at which 2D image structure is manually injected.

This recipe — "ViT pretrain low-res → fine-tune high-res with positional-embedding interpolation" — propagated into essentially every later ViT-based recipe ([DINOv2](../entities/dinov2.md), [DINOv3](../entities/dinov3.md), [V-JEPA 2](../entities/v-jepa-2.md), etc.).

## The headline results (§4.2, Table 2)

JFT-300M pretrained, fine-tuned at 384 (ViT-L/16) / 518 (ViT-H/14):

| Benchmark | Ours-JFT ViT-H/14 | Ours-JFT ViT-L/16 | Ours-I21k ViT-L/16 | BiT-L ResNet152x4 | Noisy Student EffNet-L2 |
|---|---|---|---|---|---|
| ImageNet | **88.55** ±0.04 | 87.76 ±0.03 | 85.30 ±0.02 | 87.54 ±0.02 | 88.4 / 88.5 |
| ImageNet ReaL | **90.72** ±0.05 | 90.54 ±0.03 | 88.62 ±0.05 | 90.54 | 90.55 |
| CIFAR-10 | **99.50** ±0.06 | 99.42 ±0.03 | 99.15 ±0.03 | 99.37 ±0.06 | — |
| CIFAR-100 | **94.55** ±0.04 | 93.90 ±0.05 | 93.25 ±0.05 | 93.51 ±0.08 | — |
| Oxford-IIIT Pets | **97.56** ±0.03 | 97.32 ±0.11 | 94.67 ±0.15 | 96.62 ±0.23 | — |
| Oxford Flowers-102 | 99.68 ±0.02 | **99.74** ±0.00 | 99.61 ±0.02 | 99.63 ±0.03 | — |
| VTAB (19 tasks) | **77.63** ±0.23 | 76.28 ±0.46 | 72.72 ±0.21 | 76.29 ±1.70 | — |
| **TPUv3-core-days** | **2.5k** | 0.68k | 0.23k | 9.9k | 12.3k |

- ViT-H/14 sets new state-of-the-art on every benchmark *except* Flowers-102, while using **~4× less compute** than BiT-L and **~5× less compute** than Noisy Student.
- ViT-L/16 on ImageNet-21k (public dataset, trainable in ~30 days on cloud TPUv3 8-core) hits 85.30% ImageNet — already competitive without the proprietary JFT-300M.

## Pre-training data requirements (§4.3, Figures 3 & 4)

The paper's central empirical study:

1. **Pretrain on ImageNet (1.3M) / ImageNet-21k (14M) / JFT-300M (303M); fine-tune on ImageNet.** Figure 3.
   - ImageNet pretraining: ViT-Large *underperforms* ViT-Base (overfitting) despite moderate regularization. BiT ResNets beat ViTs.
   - ImageNet-21k pretraining: ViT-Base / ViT-Large roughly match BiT ResNets.
   - JFT-300M pretraining: ViT-H/14 wins; larger ViTs > smaller ViTs; ViT > BiT.

2. **Pretrain on random 9M / 30M / 90M / 300M JFT subsets; few-shot linear-probe ImageNet.** Figure 4.
   - At 9M, ResNet50 outperforms ViT-B/32.
   - Above 90M, ViT overtakes ResNet of comparable cost.
   - Crucially: **ResNets plateau; ViTs do not** — within the range tried.

This is the data-scaling argument that drove the field's transition to ViTs as the default vision backbone over 2021–2024.

## Scaling study (§4.4, Figure 5)

7 ResNets × 6 ViTs × 5 hybrids, all pre-trained on JFT-300M for 7 or 14 epochs, evaluated by transfer accuracy on 5 downstream tasks:

- **ViT dominates ResNet on the compute/accuracy frontier.** At fixed transfer accuracy, ViT uses ~2–4× less pre-training compute.
- **Hybrids beat pure ViT at small budgets**, but the gap vanishes at large budgets. The CNN inductive bias helps in the small-compute regime, not the large-compute regime.
- **ViTs do not saturate within the tried range** — motivates further scaling. This is the empirical seed of the "scale is all you need" / scaling-laws era for vision.

## Inspecting the Vision Transformer (§4.5, Figures 6 & 7)

The authors probe ViT internals to argue it learns plausible representations:

- **Patch embedding filters (Figure 7, left):** PCA of the learned linear projection `E` yields "plausible basis functions for low-dimensional representation of the fine structure within each patch" — qualitatively similar to Gabor-like filters / first-layer CNN filters.
- **Position embeddings (Figure 7, center):** Closer patches → more similar position embeddings; row/column structure emerges; sinusoidal structure visible at larger grids. **Validates the choice not to bake in 2D-aware positional encoding** — the model learns 2D topology from the data.
- **Attention distance (Figure 7, right; Figure 6):** The mean attention distance (analogue of CNN receptive field) shows that **some heads attend globally even in the lowest layers**; other heads attend locally and concentrate near the diagonal — analogous to early convolutional layers. Hybrid ViTs (CNN stem → ViT) have *less* of this local-attention behavior in early layers, consistent with "the CNN stem already covered locality." Attention distance grows monotonically with depth; the model attends to *semantically relevant* image regions for classification (Figure 6).

## Self-supervision teaser (§4.6)

> "Self-supervised ViT holds promise for the future."

The authors run a small **masked patch prediction** experiment — analogous to BERT's masked-language modeling — on ViT-B/16 with ImageNet. Result: pre-trained with this self-supervised signal, ViT-B/16 reaches 79.9% ImageNet top-1 (vs 77.9% from-scratch supervised on ImageNet) — a +2% improvement and a 4% gap below supervised JFT-300M pretraining. **This is the seed of the entire SSL-on-ViT line** that became [BEiT](https://arxiv.org/abs/2106.08254) (2021), [MAE](https://arxiv.org/abs/2111.06377) (2021), [DINO](https://arxiv.org/abs/2104.14294) (2021), [iBOT](https://arxiv.org/abs/2111.07832) (2021), [DINOv2](../entities/dinov2.md) (2023), and ultimately [DINOv3](../entities/dinov3.md) (2025). The paper does not pursue this direction further — it is parked explicitly as future work.

## Training setup (Appendix B, Table 3)

| Models | Dataset | Epochs | Base LR | LR decay | Weight decay | Dropout |
|---|---|---|---|---|---|---|
| ViT-B/{16,32} | JFT-300M | 7 | 8·10⁻⁴ | linear | 0.1 | 0.0 |
| ViT-L/32 | JFT-300M | 7 | 6·10⁻⁴ | linear | 0.1 | 0.0 |
| ViT-L/16 | JFT-300M | 7 / 14 | 4·10⁻⁴ | linear | 0.1 | 0.0 |
| ViT-H/14 | JFT-300M | 14 | 3·10⁻⁴ | linear | 0.1 | 0.0 |
| ViT-{B,L}/16 | ImageNet-21k | 30 / 90 | 10⁻³ | linear | 0.03 | 0.1 |
| ViT-∗ | ImageNet | 300 | 3·10⁻³ | cosine | 0.3 | 0.1 |

- **Optimizer:** Adam (β₁=0.9, β₂=0.999), batch 4096, weight decay 0.1 (high!), LR warmup 10k steps.
- **From-scratch on ImageNet:** strong regularization (weight decay 0.3, dropout 0.1, label smoothing, gradient clipping at global norm 1) is *essential* — the architecture has no built-in regularization from inductive bias.
- **Fine-tuning:** SGD with momentum 0.9, batch 512, resolution 384–518, Polyak averaging.

## What the paper did not include

- **No SSL deep dive.** The masked-patch-prediction experiment is a teaser, not a contribution. The whole DINO / MAE / DINOv2 / DINOv3 line that became the dominant use of ViT was *future work* at the time of this paper.
- **No object detection / segmentation / dense prediction.** ViT here is a classification-only architecture. DETR (Carion et al. 2020, cited) handled detection; Swin / DeiT / dense-prediction adaptations came later. (See [DINOv3](../entities/dinov3.md) for the most recent state of dense prediction on top of ViT backbones.)
- **No video / 3D / multi-modal experiments.** Video ViT (ViViT, Arnab et al. 2021), V-JEPA, multi-modal CLIP / SigLIP — all post-this-paper.
- **No discussion of computational cost at very large `N`.** The `O(N²)` patch-attention cost is real and is what FlashAttention, Mamba-style state-space models, and tile-based attention later tried to mitigate. The paper sidesteps the issue by keeping `N` ≤ ~256 (16×16 patches on 224 / 384 input).
- **The "scaling laws" framing.** ViT scales monotonically (Figure 5, "ViTs do not saturate"), but the paper does not characterize the scaling curves quantitatively — that was done in Kaplan et al. 2020 for LLMs and later replicated for vision in Zhai et al. 2022 ("Scaling Vision Transformers").

## Entities mentioned

- **[Google Research, Brain Team](../entities/google-deepmind.md)** — primary affiliation. All 12 authors were Brain Team in 2020; the team has since folded into Google DeepMind.
- **Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Neil Houlsby** — equal technical contribution + equal advising (footnote ∗,†). Beyer, Kolesnikov, Zhai later moved to OpenAI / scaled-vision research; Dosovitskiy moved to Inceptive then Google; Houlsby founded Inceptive then moved back to Google DeepMind.
- **[Vaswani et al. 2017](attention-is-all-you-need.md)** — the Transformer paper, cited as the architectural foundation; this paper changes only the input pipeline.
- **BERT (Devlin et al. 2019)** — the `[CLS]` token convention and the model-size hyperparameters (Base / Large) come from BERT. Cited.
- **BiT (Kolesnikov et al. 2020), Noisy Student (Xie et al. 2020), EfficientNet-L2** — the CNN baselines beaten in Table 2. BiT is the same authors' prior work on transferring large ResNets pre-trained on JFT-300M.
- **JFT-300M (Sun et al. 2017)** — Google's proprietary 303M-image, 18K-class dataset. The paper's results depend critically on it; ImageNet-21k (Deng et al. 2009 superset) is the public fallback that gets within ~2% on ImageNet.

(None of the author entities have wiki pages yet — they are wiki-relevant primarily as the ViT architects, not as recurring contributors to wiki-tracked research lines. Federico Baldassarre on [DINOv3](../entities/dinov3.md) / [DINO-world](../entities/dino-world.md) is the closest existing entity, two steps downstream architecturally.)

## Concepts touched

- **[ViT](../glossary.md#vit)** — defined here; glossary entry is essentially a one-line summary of this paper's recipe.
- **[Transformer](../glossary.md#transformer)** — applied unchanged from [Vaswani et al. 2017](attention-is-all-you-need.md).
- **[Self-attention](../glossary.md#sa)**, **[Multi-head attention](../glossary.md#mha)** — inherited.
- **[Encoder](../glossary.md#encoder)** — ViT is encoder-only; the `[CLS]` output is the image embedding consumed by all downstream tasks.
- **Patch tokenization** — the conceptual innovation of this paper; not yet broken out as a glossary entry but referenced from many wiki source pages.
- **[Joint-Embedding Predictive Architecture (JEPA)](../concepts/world-models/jepa.md)** — every JEPA encoder in this wiki is a ViT (V-JEPA 1/2/2.1, DINO-WM, DINO-world, JEPA-WMs, LeWM, LeJEPA, PLDM).
- **Scaling / data-scaling laws for vision** — Figure 4 is one of the earliest controlled studies showing CNN-vs-ViT crossover as data scales; precursor to Zhai et al. 2022.

## Position in the lineage

```
Vaswani et al. 2017 (Transformer — encoder–decoder for NMT)
   ↓                                              ↘
BERT 2018 (encoder-only MLM)                    GPT-1 2018 (decoder-only LM)
   ↓                                              ↘
[CLS] + pretrain–finetune recipe          (decoder-only thread → GPT-2/3/4/Claude/Llama)
   ↓
"An Image Is Worth 16x16 Words" 2020 (THIS PAPER) — patch tokenization + [CLS] over transformer encoder
   ↓
   ├── DeiT 2020 (Touvron — data-efficient ViT)
   ├── Swin 2021 (Liu — hierarchical / shifted-window ViT)
   ├── DINO 2021 → DINOv2 2023 → DINOv3 2025 (SSL on ViT)
   ├── MAE 2021 (He — masked autoencoder on ViT)
   ├── BEiT 2021 (Bao — discrete VAE + masked tokens on ViT)
   ├── CLIP 2021 (Radford — ViT image encoder + text encoder, contrastive)
   ├── ViViT 2021 → V-JEPA / V-JEPA 2 / V-JEPA 2.1 (video ViT + JEPA SSL)
   └── ViT-as-backbone for every dense-prediction stack post-2021
        (DETR detection, Mask2Former segmentation, ViT-Adapter, etc.)
```

This wiki touches the descendants on three branches: the **DINO line** ([DINOv2](../entities/dinov2.md), [DINOv3](../entities/dinov3.md)), the **JEPA line** ([V-JEPA 2](../entities/v-jepa-2.md), [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [DINO-world](../entities/dino-world.md), [JEPA-WMs](../entities/jepa-wms.md), [PLDM](pldm-paper.md), [LeJEPA](lejepa-paper.md), [VLA-JEPA](vla-jepa-paper.md)), and the **action-policy line** where ViT is the visual encoder feeding a downstream policy ([Diffusion Policy](diffusion-policy-paper.md), [BeT](bet-paper.md), [π0](pi-zero-paper.md), [UMI](umi-paper.md), [Robot Utility Models](robot-utility-models-paper.md)).

## Curriculum hookup

This is the **canonical reference for [ViT in Curriculum Module 3 — Sequence models, attention, and transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)**. Module 3 already cites this paper twice — once in the "vision transformer recipe" section, once as the ViT primary source for the "Recommended reading" list. The wiki was carrying ViT entirely via the [glossary entry](../glossary.md#vit) and the many downstream sources that depend on it; this ingest closes the gap and is the natural primary-source companion to the [Vaswani et al. 2017](attention-is-all-you-need.md) ingest of 2026-05-14.

Module 3's anchor exercise ("tiny transformer on PushT 8×8 patches with attention-map visualization") is essentially a from-scratch ViT-mini. Reading §3 of this paper alongside `model.py` in [karpathy/nanoGPT](karpathy-nanogpt.md) gives the reader the encoder-only ↔ decoder-only contrast at the implementation level.

## Open questions / TBD

- **Patch overlap.** The paper uses *non-overlapping* patches (stride = patch size). Several later works experimented with overlapping patches / convolutional stems (e.g., CvT, CoAtNet); the trade-off (more tokens, more locality bias, more compute) is rarely covered in the wiki. Worth a one-line glossary mention or an entry in [DINOv3](../entities/dinov3.md)-context.
- **Positional encoding alternatives.** The paper's choice of *learned 1D* embeddings was deliberately minimalist. Modern descendants — RoPE, axial RoPE (used in [DINOv3](../entities/dinov3.md)), ALiBi, learned 2D, sin/cos 2D — are not yet broken out as a wiki page. A short "positional encoding for vision" glossary subsection or concept page would help future ingests.
- **Self-supervised ViT.** The §4.6 teaser was the seed of DINO / MAE / DINOv2 / DINOv3 / JEPA. The wiki has those downstream papers but does not have **DINO (Caron et al. 2021)** or **MAE (He et al. 2021)** as ingested sources — they are the missing middle of the ViT → DINOv3 lineage. Logged as candidate future ingests.
- **Hybrid architectures.** Section §4.4's finding that hybrids beat pure ViT at small compute and converge at large compute is the implicit justification for *not* using hybrids in modern foundation models (DINOv3, V-JEPA 2). Worth confirming whether any wiki-tracked paper actually re-tests this trade-off at modern scales.
- **`[CLS]` vs averaged patch features.** The paper uses `[CLS]` for classification (Eq. 4). DINOv2 / DINOv3 / V-JEPA 2 use combinations (`[CLS]` + average-pooled patch features, or just patch features for dense tasks). The trade-offs aren't discussed in this paper and would be useful for a future "ViT-output-head" concept page.
