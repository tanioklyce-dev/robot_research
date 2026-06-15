---
title: "Signature Verification using a 'Siamese' Time Delay Neural Network (Bromley, Guyon, LeCun, Säckinger, Shah, NIPS 1993)"
type: source
url: https://proceedings.neurips.cc/paper/1993/hash/288cc0ff022877bd3df94bc9360b9c5d-Abstract.html
local_path: raw/NIPS-1993-signature-verification-using-a-siamese-time-delay-neural-network-Paper.pdf
author: Jane Bromley, Isabelle Guyon, Yann LeCun, Eduard Säckinger, Roopak Shah
affiliation: AT&T Bell Laboratories, Holmdel NJ
published: 1993 (NIPS 6 proceedings; AT&T Bell Labs copyright 1994)
ingested: 2026-05-14
tags: [siamese-network, lecun, guyon, bromley, sickinger, att-bell-labs, foundational, historical, signature-verification, joint-embedding, ancestor]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/NIPS-1993-signature-verification-using-a-siamese-time-delay-neural-network-Paper.pdf`, 8 pages). Full read; this is a short conference paper, all sections covered.

## Summary

**The original Siamese network paper.** Bromley, Guyon, LeCun, Säckinger, Shah (AT&T Bell Labs Holmdel; NIPS 6, 1993). Describes a dynamic signature-verification system for a credit-card-tablet device (NCR 5990) where **two identical sub-networks with shared weights** extract feature vectors from two signatures and a joining neuron computes their cosine similarity. Trained with the constraint that **genuine:genuine pairs target cosine = 1.0** and **genuine:forgery pairs target cosine ≈ −1.0**. Verification at inference time: encode the test signature, compare to a stored 80-byte feature-vector template.

The architecture itself — **two weight-tied encoders + a similarity head, trained on pairs** — is **the architectural ancestor of every joint-embedding system in modern SSL**, including:

- **Contrastive SSL** ([SimCLR](../sources/barlow-twins-paper.md), MoCo, BYOL).
- **Anti-collapse SSL** ([Barlow Twins](barlow-twins-paper.md), [VICReg](vicreg-paper.md), [DINOv2](../entities/dinov2.md), [DINOv3](../entities/dinov3.md)).
- **[JEPA](../concepts/world-models/jepa.md)** — joint-embedding *predictive* architectures (the J in JEPA comes from this lineage).
- Face/voice/image-pair verification systems (Schroff/FaceNet 2015, etc.).

The naming is mundane — **"Siamese"** simply refers to the two-conjoined-twin topology of weight-tied sub-networks — but the architectural idea (compare embeddings rather than classify) has had outsized influence. This is the **eponymous original source**.

**Why this matters to the wiki.** The [Welch Labs LeCun explainer](welchlabs-lecun-1b-bet-against-llms.md) walks the lineage **generative-pixel → "why so blurry" → Siamese networks → representation collapse → Barlow Twins → DINO → JEPA**. Until this ingest, the wiki cited the Siamese-network step but had **no primary source** for it. This source page fills that gap and locates the architectural seed of modern joint-embedding SSL — including [LeCun](../entities/yann-lecun.md)'s entire 2020s research program — in **a 1993 Bell Labs paper that LeCun co-authored as a young researcher**.

## Abstract (verbatim)

> "This paper describes an algorithm for verification of signatures written on a pen-input tablet. The algorithm is based on a novel, artificial neural network, called a 'Siamese' neural network. This network consists of two identical sub-networks joined at their outputs. During training the two sub-networks extract features from two signatures, while the joining neuron measures the distance between the two feature vectors. Verification consists of comparing an extracted feature vector with a stored feature vector for the signer. Signatures closer to this stored representation than a chosen threshold are accepted, all other signatures are rejected as forgeries."

## The architecture (Section 4)

The Siamese network has:

- **Two input fields** to compare two patterns.
- **Two identical sub-networks** based on **Time Delay Neural Networks (TDNN)** (Lang & Hinton 1988; Guyon et al. 1990) with **weights tied across the two branches** ("All weights could be learnt, but the two sub-networks were constrained to have identical weights.").
- **A joining neuron** that computes **cosine similarity** between the two output feature vectors.

> [!note] Closest modern analogue
> A modern SimCLR / Barlow Twins / DINO encoder is a Siamese network — two shared-weight branches that produce embeddings of two views of an input, with the loss computed between the embeddings. Only the loss has changed (cosine + binary target → InfoNCE, cross-correlation → I, or self-distillation), not the architectural shape.

### TDNN sub-network details (Architecture 1)

- Input: 8 features × 200 time-steps = 1600 dimensions (resampled signatures).
- Layer 1: 12 × 64 units, receptive field 8 × 11.
- Layer 2: 16 × 19 units, receptive field 12 × 10.
- Compression: time-axis subsampling step of 3.

**Architecture 2** (the one designed for the 80-byte storage constraint) used averaging instead of subsampling and produced a 4 × 19 = 76-dimensional output feature vector. Training used a **modified back-propagation (LeCun 1989)** with the weight-tying constraint enforced.

### Training pairs and targets

- Training set: 982 genuine signatures from 108 signers + 402 forgeries of ~40 of them.
- Up to 7,701 signature pairs: **50% genuine:genuine**, **40% genuine:forgery**, **10% genuine:zero-effort forgery** (other signers' real signatures used as random-forgery negatives).
- Targets: **cos = +1.0** for genuine:genuine, **cos = −0.9 or −1.0** for genuine:forgery.

This is recognizable as a **contrastive-style loss with explicit positive and negative pairs and a fixed cosine target** — a direct ancestor of contrastive InfoNCE-class losses 25 years later, but with a much simpler regression-onto-target setup.

## Inference (Section 5)

At deployment, **only one sub-network is run** — to compute the feature vector for the test signature. That vector is compared to a stored multivariate-normal model built from the user's last 6 signatures' feature vectors (modeled as independent Gaussians per feature). A probability-density test gates accept/reject against a chosen threshold.

The **80-byte constraint** — the project's hard requirement, since signature templates had to fit on a credit-card magnetic stripe — drove the network design. The final system stored 38 floats (1 byte each) for the feature mean + 38 bytes for the sum-of-squares → 76 bytes total, within the 80-byte budget.

## Results (Section 6)

Best result, Network 4 (Architecture 1, large training set, cleaned data):
- **At an 80% forgery-rejection threshold, 95.5% of genuine signatures were accepted** (24 / 532 rejected).
- 97.0% accepted if first/second signatures (warm-up period for users adapting to the pad) were removed.
- Of the 13 remaining rejections, 9 had pen-up trajectories that differed from the user's typical signature.

Surprising finding: **50% of Network 5's outputs were redundant** — the 76-dim feature could be compressed to 38 dims with no loss. Hypothesis offered: forcing genuine:forgery to cosine = −1 effectively *uses fewer dimensions* than the architecture has, since pointing in opposite directions on a sphere is a low-dimensional constraint.

> [!note] Pre-deep-learning era markers
> Training "took a few days on a SPARC 1+." The system was demonstrated to commercial customers at Bell Labs and worked across American, European, and Chinese signatures. No GPU, no SGD, no Adam, no batch norm — just **back-prop with weight tying and pair-wise targets**. The architectural idea worked on hardware that is ~10⁵ slower than a single 2026 GPU.

## Entities mentioned

- **[Yann LeCun](../entities/yann-lecun.md)** — third author. This paper is in his AT&T Bell Labs Holmdel period (LeNet-1 had appeared in 1989; LeNet-5 would follow in 1998). The Siamese-network idea here is **30+ years older than the JEPA program LeCun would later architect at Meta FAIR** — and architecturally continuous with it. The Welch Labs explainer's framing of LeCun's JEPA work as "the natural continuation of the Siamese-network research he started in the 1990s" is literally correct.
- **Isabelle Guyon** — second author; later well known for ML competitions (KDD Cup, NeurIPS competitions). Was at Bell Labs during the same period as LeCun.
- **Jane Bromley** — first author. AT&T Bell Labs.
- **Eduard Säckinger, Roopak Shah** — co-authors.
- **P. Baldi & Y. Chauvin** — cited as having independently proposed a "similar Siamese architecture for fingerprint identification" in 1992. The Siamese idea was apparently in the air at Bell Labs in the early 1990s.
- **AT&T Bell Laboratories** — the institution producing simultaneous foundational work on CNNs (LeNet), Siamese networks (this paper), and statistical learning theory (Vapnik). The pre-2000 ML research mecca.

## Concepts touched
- [Siamese network](../concepts/world-models/siamese-network.md)

- **Siamese networks / Joint-Embedding** — defined here.
- **Weight tying** — the two sub-networks share weights; explicit architectural constraint.
- **Pairwise contrastive training** — genuine:genuine vs genuine:forgery targets are a primitive form of contrastive loss.
- **TDNN (Time Delay Neural Network)** — the sub-network type; predecessor of 1D convolutional networks.
- **[Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md)** — descendant. JEPA's *J* is from this lineage; the *P* (predictive) is what's added.
- **Representation collapse** — interestingly, not a problem for this paper because of the **explicit negative targets** (cos = −1 for genuine:forgery). The collapse problem only emerges in the SSL era when one tries to learn embeddings *without* labels.

## Position in the lineage

```
Bromley, Guyon, LeCun, Säckinger, Shah 1993  ← THIS PAPER
   two TDNNs with shared weights + cosine + ±1 targets
   ↓
Schroff et al. 2015 (FaceNet, triplet loss)
   ↓
Hadsell et al. 2006 (contrastive loss)
   ↓
SimCLR 2020 (InfoNCE, large negative batches)        ← contrastive branch
MoCo 2020 (momentum encoder + queue)
   ↓                                                    ↓
BYOL 2020 (no negatives, predictor + EMA)               ↓
SimSiam 2020 (no negatives, stop-gradient)              ↓
                                                         ↓
[Barlow Twins 2021](barlow-twins-paper.md)              ← anti-collapse branch
[VICReg 2022](vicreg-paper.md)
[DINO 2021](../entities/dinov2.md) → DINOv2 → [DINOv3](../entities/dinov3.md)
   ↓
[LeCun 2022 — Path Towards AMI](lecun2022-path-towards-ami.md)
   defines JEPA as a Joint-Embedding + Predictor
   ↓
[V-JEPA 2](v-jepa-2-paper.md), [DINO-WM](dino-wm-paper.md), [JEPA-WMs](jepa-wms-paper.md),
[LeWM](leworldmodel-paper.md), [LeJEPA](lejepa-paper.md)  (2024–2026)
```

**One paper, 33 years, an entire field of self-supervised learning.** The wiki's Barlow-Twins-→-LeWM lineage already covers the *anti-collapse SSL* arc; this paper supplies the architectural seed for both the *contrastive* and *anti-collapse* branches that flow from "compare two embeddings produced by a shared encoder."

## Curriculum hookup

This is foundational material for **[Curriculum Module 4 — Self-supervised learning and embeddings](../syntheses/curriculum/curriculum-04-self-supervised-learning.md)** (where joint-embedding architectures are introduced) and **[Module 11 — JEPA in depth](../syntheses/curriculum/curriculum-11-jepa-deep.md)** (where the J in JEPA is unpacked). The Welch Labs popular explainer (recommended on the [JEPA concept page](../concepts/world-models/jepa.md)) hits the Siamese-network step around the 15-minute mark.

## Open questions / TBD

- **When did "Siamese network" first appear as a term?** This paper uses it in scare-quotes in the title — suggesting it is being introduced here. Worth confirming.
- **Isabelle Guyon's later trajectory** — she became a major figure in ML competition design; whether she stayed adjacent to the Siamese-network / joint-embedding line or moved orthogonally is unclear.
- **The Baldi & Chauvin 1992 fingerprint Siamese paper** is the contemporaneous parallel work cited here. Worth checking whether it predates this paper materially and how its design differs.
