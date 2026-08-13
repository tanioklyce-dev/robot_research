---
title: Moo Jin Kim
type: entity
subtype: person
created: 2026-07-27
updated: 2026-07-27
sources: 1
tags: [person, stanford, vla, openvla, openvla-oft, roboarena, evaluation]
---

**Moo Jin Kim** — Stanford PhD researcher in robot learning; first author of **[OpenVLA](openvla.md)** and **[OpenVLA-OFT](openvla-oft.md)**, and a co-author on **[RoboArena](roboarena.md)**. Works in [Chelsea Finn](chelsea-finn.md)'s and Percy Liang's orbit at Stanford.

## Work in this wiki

- **[OpenVLA](openvla.md)** — the open 7B VLA that became the field's default open baseline, and the model nearly every later VLA reports against.
- **[OpenVLA-OFT](openvla-oft.md)** ([paper](../sources/openvla-oft-paper.md), arXiv 2502.19645, RSS 2025; with [Chelsea Finn](chelsea-finn.md) and Percy Liang) — the "Optimized Fine-Tuning" recipe: **parallel decoding + action chunking + continuous L1 head**, lifting OpenVLA's LIBERO **76.5 → 97.1** *on the same weights* at **26× throughput**, and running real bimanual [ALOHA](aloha.md) at **25 Hz**. A controlled study of three fine-tuning axes rather than a new architecture — which is why the **+20.6 pp recipe effect** survives the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) while the model's *rank* among the 96.5–98.1 cluster does not.
- **[RoboArena](roboarena.md)** ([paper](../sources/roboarena-paper.md), CoRL 2025) — one of 32 authors on the distributed pairwise-preference evaluation network.

## The through-line

Kim's three wiki appearances trace an arc from **building** to **measuring**: OpenVLA (a model), OpenVLA-OFT (a controlled study of what actually makes VLAs better), and RoboArena (a protocol for telling whether any of it is real). The middle one already had the character of an evaluation paper — its contribution is an ablation, not an architecture.

## Related
- [Chelsea Finn](chelsea-finn.md) — co-author on OpenVLA-OFT and RoboArena.
- [Karl Pertsch](karl-pertsch.md) — co-author across the OpenVLA / DROID / RoboArena cluster.
- [Sergey Levine](sergey-levine.md) — co-author on OpenVLA and RoboArena.
- **Percy Liang** — Stanford; OpenVLA-OFT and RoboArena co-author. No entity page.

## Mentioned in
- [OpenVLA-OFT paper](../sources/openvla-oft-paper.md) — first author
- [RoboArena paper](../sources/roboarena-paper.md) — co-author
- [OpenVLA](openvla.md) — first author of the original
