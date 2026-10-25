---
title: "MJEPA: A Simple and Scalable Joint-Embedding Predictive Architecture for Audio-Visual Learning (Teotia, Bardes, Rabbat, Chopra, Muckley, Ballas, 2026)"
type: source
url: https://arxiv.org/abs/2606.25225
fetch_url: https://arxiv.org/pdf/2606.25225v1
local_path: raw/2606.25225v1.pdf
sha256: 95043d054d2e10dab37d86fd9e5aaf13280ff10800647988a731e8f5148d4b1c
author: Revant Teotia, Adrien Bardes, Michael Rabbat, Sumit Chopra, Matthew Muckley, Nicolas Ballas
published: 2026-06-23
ingested: 2026-10-24
venue: arXiv (cs.CV), v1
format: "paper, 22 pp. Affiliations: FAIR at Meta; NYU (Teotia, Chopra). Muckley and Ballas equal supervision."
tags: [mjepa, jepa, audio-visual, multimodal, self-supervised, v-jepa, shared-encoder, cross-modal-prediction, audioset, kinetics, ssv2, frozen-evaluation]
---

# MJEPA: audio-visual JEPA with one shared encoder (2026-06-23)

## Summary

[MJEPA](../entities/mjepa.md) extends V-JEPA's masked latent prediction to audio + video with **one shared encoder** for audio, video and audio-video inputs, and **only JEPA losses**: no contrastive terms, no reconstruction, no augmentations. Both within-modality and **cross-modal** prediction are used (predict one modality's pooled representation from the other's).
- **Cross-modal prediction is what makes sharing work.** Naively sharing an encoder across modalities **degrades both below their unimodal baselines**, as VATT, XKD and AVSiam also found. With cross-modal prediction, each modality improves the other.
- **Results with frozen features:**
  - A frozen ViT-g beats the best prior frozen AudioSet-20K baseline by **> 6.8 mAP** (audio+video).
  - Beats **fully fine-tuned** models on ESC-50 (96.9%) and FSD50K.
  - K400 85.0 / SSv2 73.9, against V-JEPA 2 ViT-g's 86.6 / 75.3, with **~10× less video data** (AudioSet-2M + VideoMix2M vs VM22M).

## Key claims
- **Architecture:** a single ViT (L 300M or g 1B) over audio spectrogram patches and video tubelets. V-JEPA-style EMA target and stop-gradient; L1 loss on masked tokens. An intra-modal predictor plus a cross-modal predictor on pooled representations.
- **Progressive ablation (§4):** joint encoding → shared encoder → cross-modal prediction → data scaling (AS2M ~5k h paired audio-video, plus VM2M ~2M videos / ~136k h) → model scaling (ViT-L → ViT-g). The paper says each step is necessary.
- **Video (§5.2):** ViT-L trained on AS2M only reaches 75.2 K400 / 58.6 SSv2. Adding VM2M brings ViT-L to 84.7 / 73.3, against V-JEPA 2 ViT-L's 85.1 / 73.7. ViT-g reaches 85.0 / 73.9.
- **Audio:** frozen ViT-g reaches 96.9% on ESC-50. SPEAR and Dasheng still lead overall on some audio tasks with 197k–272k hours of audio, against AudioSet's 5k.
- **Conclusion's outlook:** the same design should extend to other co-occurring streams, *"robotics (e.g., vision, proprioception)"*. This is stated as a direction, not tested.

## Reading notes (wiki inference)
- **The robotics relevance is the negative result.** Sharing an encoder across modalities **hurts** unless there is an explicit cross-modal predictive term. That matches the wiki's broader finding that joint-in-time or cross-signal grounded targets are what keep a latent informative (see [collapse synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md)). A vision + proprioception (+ audio/contact) robot encoder would face the same trade-off. MJEPA's recipe, cross-modal prediction on pooled representations, is a concrete template for it.
- No action conditioning, no planning, no robot data. This is a representation-learning paper in the JEPA family, filed for lineage.

## Entities mentioned
- [MJEPA](../entities/mjepa.md) · [Adrien Bardes](../entities/adrien-bardes.md) · [V-JEPA 2](../entities/v-jepa-2.md) (baseline)

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md): first single-encoder multimodal instance in the wiki.

## Open questions
- Would cross-modal prediction between **vision and proprioception/tactile** give a robot encoder the same positive transfer?
- How does an EMA-teacher multimodal JEPA behave under SIGReg instead (LeJEPA-style), which the LeCun line now prefers?
