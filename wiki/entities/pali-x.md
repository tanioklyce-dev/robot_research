---
title: PaLI-X
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 2
tags: [pali-x, vlm, backbone, google, encoder-decoder, vit]
---

**PaLI-X** — Google's **55B-parameter** vision-language model (Chen et al., 2023); a ViT image encoder feeding an encoder-decoder transformer. The backbone of [RT-2](rt-2.md) and [RT-H](rt-h.md), where the ViT is frozen and the robot task is co-trained into the original PaLI-X mixture.

_Stub._ Notable in this wiki mainly for **scale contrast**: PaLI-X at 55B is roughly **275× the parameter count of [TurboVLA](turbovla.md)** (0.2 B), which reaches top-tier LIBERO with no language model at all. The [RT-H](rt-h.md) result that language *words* beat integer labels may depend on exactly this scale of pretraining — a hypothesis nobody has tested head-to-head.

Sibling of the smaller [PaliGemma](paligemma.md), which backs [π0](pi-zero.md).

## Mentioned in
- [RT-H paper](../sources/rt-h-paper.md)
