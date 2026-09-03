---
title: "A Simple Framework for Contrastive Learning of Visual Representations — SimCLR (Chen et al., 2020)"
type: source
url: https://arxiv.org/abs/2002.05709
fetch_url: https://arxiv.org/pdf/2002.05709v3
local_path: raw/2002.05709v3.pdf
sha256: e1b10db76adeb0d21a014b9abcf42f6a6af928540c223f010fa1d8c293d9d105
author: "Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton (Google Research, Brain Team)"
published: 2020-02-13
venue: "ICML 2020 (arXiv v3, 2020-07-01)"
format: paper (PDF, 20 pp.)
tags: [simclr, contrastive-learning, nt-xent, projector, augmentation, batch-size, self-supervised, foundational]
ingested: 2026-09-03
---

## Summary

**The paper that made contrastive SSL simple, and the source of three facts this wiki had been quoting from other people's reproductions.** SimCLR strips the field's architectural machinery — memory banks, specialized receptive fields, patch-splitting pipelines — down to: two augmented views, an encoder, a small MLP projection head, and a normalized temperature-scaled cross-entropy loss over in-batch negatives. 76.5% ImageNet linear top-1 with ResNet-50(4×); 69.3% with a plain ResNet-50, a 7% relative improvement on the prior state of the art.

The reason to read the primary is that its two most-cited results — **why colour distortion is mandatory** and **why you use the layer before the projector** — are usually paraphrased, and both are measured here with mechanisms attached.

## Key claims

**NT-Xent.** For a batch of N images augmented twice, treat the other 2(N−1) views as negatives; no explicit negative sampling and no memory bank. `ℓ_{i,j} = −log[ exp(sim(z_i,z_j)/τ) / Σ_k 1[k≠i] exp(sim(z_i,z_k)/τ) ]` over ℓ2-normalized embeddings. They name it *"normalized temperature-scaled cross entropy"* and note it was already used by Sohn 2016, Wu et al. 2018 and [CPC](cpc-paper.md) — consistent with [the Cookbook's lineage](ssl-cookbook.md).

### Augmentation composition, and the colour-histogram shortcut

The headline ablation (Fig. 5) applies transformations singly and in pairs, to one branch only. **No single transformation suffices**, even though the model can nearly perfectly solve the contrastive task with one. Composition is what works, and one pair stands out: **random cropping + colour distortion** (~56 vs 2.6–33.9 for most cells).

The mechanism is the part worth carrying, because three later papers repeat it:

> Most patches from an image share a similar colour distribution, and **colour histograms alone suffice to distinguish images** (Fig. 6). *"Neural nets may exploit this shortcut to solve the predictive task. Therefore, it is critical to compose cropping with colour distortion in order to learn generalizable features."*

And a second finding that is easy to miss: **contrastive learning wants stronger augmentation than supervised learning does.** Sweeping colour-distortion strength, SimCLR goes **59.6 → 63.2 → 64.5** (with blur) while the *supervised* baseline on the same augmentations goes **77.0 → 75.7 → 75.4** — the augmentation that helps one *hurts* the other. **AutoAugment**, a policy found by supervised search, underperforms plain crop + strong colour for SimCLR (61.1 vs 64.5).

> [!note] This is the origin of a claim the wiki has been sourcing secondhand
> The colour-histogram shortcut is the reason [BYOL](byol-paper.md) gives for its own robustness, the reason [the Cookbook](ssl-cookbook.md) gives for colour distortion being mandatory, and the reason [MAE](mae-paper.md) contrasts itself with augmentation-dependent methods. All three describe it; **this is where it is measured.**

### The projector, and *why* the layer before it is better

Nonlinear projection beats linear by **+3%** and beats no projection by **>10%**. Then the finding everyone uses: **`h` (before the projector) is >10% better than `z = g(h)` (after)**, regardless of output dimension.

The mechanism is measured rather than asserted (Table 3): train an MLP on each representation to predict which augmentation was applied.

| Predict | chance | from `h` | from `g(h)` |
|---|---:|---:|---:|
| Colour vs grayscale | 80 | 99.3 | 97.4 |
| **Rotation** | 25 | **67.6** | **25.6** |
| Original vs corrupted | 50 | 99.5 | 59.6 |
| Original vs Sobel-filtered | 50 | 96.6 | 56.3 |

**`g(h)` is trained to be invariant, so it discards exactly the information the invariance targets** — rotation drops to chance. `h` retains it. This is the concrete basis for the Cookbook's *Guillotine Regularization* framing and for why every method since keeps the backbone and throws the projector away.

### Batch size — and the footnote that undercuts the folklore

Larger batches and longer training both help *"compared to its supervised counterpart"* — but §5.2 states the limit plainly: **"with more training steps/epochs, the gaps between different batch sizes decrease or disappear."** And footnote 10: *"a **square root learning rate scaling** can improve performance of ones with small batch sizes"* (Fig. B.1).

> [!warning] SimCLR's own paper says the large-batch requirement is a short-schedule artifact
> This wiki asserted a standing large-batch cost for contrastive methods, derived from CPC's MI bound, and [corrected it](../concepts/learning/contrastive-learning.md) after [the Cookbook](ssl-cookbook.md) called that "misleading." The primary is stronger than the correction: the batch-size gap **closes with training length**, in SimCLR's own §5.2, in 2020. What propagated for a decade was the 100-epoch ablation table, not the sentence underneath it.

Other implementation facts worth having: **LARS at all batch sizes**; **Global BN** — aggregating batch-norm statistics across devices, because positives computed on the same device let the model *"exploit the local information leakage to improve prediction accuracy without improving representations"* (a shortcut of the same family as the colour histogram); ~1.5 h on 128 TPU v3 cores for ResNet-50, batch 4096, 100 epochs.

**Bigger models benefit more from unsupervised than supervised learning** — the gap to the supervised baseline *shrinks* as model size grows, which is the scaling argument every later SSL paper inherits.

## Results

| | Params (M) | Top-1 | Top-5 |
|---|---:|---:|---:|
| MoCo, ResNet-50 | 24 | 60.6 | — |
| CPC v2, ResNet-50 | 24 | 63.8 | 85.3 |
| **SimCLR, ResNet-50** | 24 | **69.3** | 89.0 |
| SimCLR, ResNet-50 (4×) | 375 | **76.5** | 93.2 |

Semi-supervised with **1% of labels**: 75.5 top-5 (ResNet-50) → **85.8** (4×), against a 48.4 supervised baseline.

## Entities mentioned

- [SimCLR](../entities/simclr.md) — the method's entity page.
- Google Research, Brain Team — all four authors, including **Geoffrey Hinton**.
- [MoCo](../entities/moco.md) · [CPC](cpc-paper.md) — the baselines it displaced.

## Concepts touched

- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) — **the canonical instantiation**.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — the projector's information-discarding measurement.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) · [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md).

## Open questions

- **What is the colour-histogram shortcut's analogue in robotics?** SimCLR's insight is that a *dataset-specific low-level statistic* solved the pretext task and capped the representation. Robot data has obvious candidates — lighting, camera pose, background, time-of-day — and this wiki has no source that has looked for one. The [financial case](../concepts/economics/financial-time-series-augmentations.md) is the same failure in another domain, found by derivation rather than by ablation.
- **Table 3's protocol is a general-purpose diagnostic and is barely used.** *"Train a probe to predict which augmentation was applied"* measures what the invariance actually destroyed, in one number per augmentation. It would say directly what a JEPA's or a world model's latent has thrown away.
- **Global BN is a shortcut-elimination fix that has no analogue in most reimplementations.** Worth knowing when a distributed SSL run scores suspiciously well.
