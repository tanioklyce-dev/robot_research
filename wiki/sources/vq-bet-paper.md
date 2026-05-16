---
title: VQ-BeT — Behavior Generation with Latent Actions (paper)
type: source
url: https://arxiv.org/abs/2403.03181
author: Seungjae Lee, Yibin Wang, Haritheja Etukuru, H. Jin Kim, Nur Muhammad Mahi Shafiullah, Lerrel Pinto
published: 2024-03 (ICML 2024, PMLR 235:26991-27008)
ingested: 2026-05-16
tags: [vq-bet, behavior-cloning, vector-quantization, transformer, nyu, icml-2024]
---

## Summary
The primary [VQ-BeT](../entities/vq-bet.md) paper from NYU's Pinto group, ICML 2024. Direct successor to [BET](../entities/bet.md) (NeurIPS 2022). Replaces BET's **k-means action clustering** with a **hierarchical vector-quantization codebook** that tokenizes continuous actions end-to-end with gradient information, then trains a transformer to autoregressively predict latent action tokens. Evaluated across **seven environments** spanning simulated manipulation, autonomous driving, and robotics — outperforms BET and [Diffusion Policy](../entities/diffusion-policy.md) while running ~**5× faster inference** than diffusion. The strongest performer in the [Robot Utility Models](../sources/robot-utility-models-paper.md) ablation at full data scale, and the headline behavior-cloning method in the NYU-line BC-via-latent-actions agenda.

## Key claims

### Abstract — key framing
The paper frames behavior generation as a multimodal-action problem: continuous, multimodal action distributions plus potential compounding errors. BET's k-means clustering scales poorly to **high-dimensional action spaces** or **long sequences** and lacks gradient information. VQ-BeT addresses both by replacing k-means with a learnable VQ codebook.

### Core technical contribution
- **Hierarchical vector quantization** module that tokenizes continuous actions into discrete latent codes.
- End-to-end trainable (gradient flows through the VQ tokenizer, unlike k-means).
- Transformer autoregressively predicts latent action codes; a small decoder reconstructs continuous actions from latent codes.

### Differentiation from baselines
- **vs BET**: hierarchical VQ replaces k-means clustering. Improved scaling to higher-dimensional actions and longer sequences; learnable end-to-end.
- **vs Diffusion Policy**: comparable or better task performance, with **~5× faster inference** because autoregressive token decoding beats iterative diffusion denoising at sampling time.

### Performance summary
- Evaluated on **7 environments**: simulated manipulation, autonomous driving, robotics.
- "Improves on state-of-the-art models such as BeT and Diffusion Policies, with improved ability to capture behavior modes while accelerating inference speed."
- Specific numeric results not surfaced from abstract — see paper body.

### Author lineage
- **First author Seungjae Lee** — RUM co-author; the VQ-BeT/RUM pairing makes this paper directly relevant to the in-home-deployment work in this wiki.
- **Etukuru, Shafiullah, Pinto** — all also on the [Dobb·E paper](dobb-e-paper.md) and the [RUM paper](robot-utility-models-paper.md). NYU continuity from Dobb·E → RUM → VQ-BeT.

### Release
- Code: <https://github.com/jayLEE0301/vq_bet_official>.
- Project page: <https://sjlee.cc/vq-bet/>.

## Entities mentioned
- [VQ-BeT](../entities/vq-bet.md)
- [BET](../entities/bet.md) — direct predecessor.
- [Diffusion Policy](../entities/diffusion-policy.md) — primary baseline.
- [Robot Utility Models](../entities/robot-utility-models.md) — downstream consumer.
- [Mahi Shafiullah](../entities/mahi-shafiullah.md), [Lerrel Pinto](../entities/lerrel-pinto.md) — co-authors.

## Concepts touched
- [Imitation learning](../concepts/learning/imitation-learning.md) — VQ-BeT is one of the headline BC methods.

## Open questions
- **Codebook size and transformer dimensions** not surfaced from abstract. Reading the paper body is needed if "VQ-BeT capacity scaling vs Diffusion-Policy capacity scaling" becomes a load-bearing comparison.
- **Hierarchy depth** — how many levels of VQ? The abstract says "hierarchical" but doesn't quantify.
- What does "long-range action modeling" buy on top of behavior-mode capture? The two are interrelated but the paper presumably ablates separately.
- 5× speedup is impressive but inference-only — training cost vs Diffusion Policy is the orthogonal axis.
