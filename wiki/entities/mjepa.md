---
title: MJEPA
type: entity
subtype: model
created: 2026-10-24
updated: 2026-10-24
sources: 1
tags: [mjepa, jepa, audio-visual, multimodal, self-supervised, meta-fair, shared-encoder]
---

# MJEPA

**MJEPA** is a [JEPA](../concepts/world-models/jepa.md) for **audio + video with one shared encoder**, trained only with masked latent prediction, both within and across modalities. It is by Teotia, [Bardes](adrien-bardes.md), Rabbat, Chopra, Muckley and Ballas (FAIR / NYU), arXiv 2606.25225, 2026-06-23 ([paper](../sources/mjepa-audio-visual-paper.md)).

## Key results ([paper](../sources/mjepa-audio-visual-paper.md))
- **A shared encoder without cross-modal prediction underperforms unimodal baselines.** With cross-modal prediction, each modality improves the other.
- **Frozen ViT-g (1B) results:**
  - AudioSet-20K: > 6.8 mAP over the best prior frozen baseline.
  - ESC-50 96.9%, above fully fine-tuned models.
  - K400 85.0 / SSv2 73.9 against [V-JEPA 2](v-jepa-2.md) ViT-g's 86.6 / 75.3, with ~10× less video.

## Why it matters here
It is the first single-encoder multimodal JEPA in the wiki. Its negative result (sharing hurts without a cross-signal predictive term) is the one to carry over to a vision + proprioception robot encoder, which the authors name as future work.

## Related
- [V-JEPA 2](v-jepa-2.md) — the video recipe it extends
- [Adrien Bardes](adrien-bardes.md)

## Mentioned in
- [MJEPA paper](../sources/mjepa-audio-visual-paper.md)
