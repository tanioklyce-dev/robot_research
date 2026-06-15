---
title: "Mobile ALOHA project page (mobile-aloha.github.io)"
type: source
url: https://mobile-aloha.github.io
author: Zipeng Fu, Tony Z. Zhao, Chelsea Finn (Stanford)
published: 2024-01
ingested: 2026-05-25
tags: [mobile-aloha, aloha, act, act-plus-plus, stanford, project-page, primary-source, tutorial, hardware-code, ml-code]
---

## Summary

Canonical Mobile ALOHA **project page** — companion to the [Mobile ALOHA paper](mobile-aloha-paper.md). Adds three things the paper PDF doesn't ship:

1. **The reproducibility recipe** — a Google-Docs tutorial covering 3D printing, assembly, and software installation.
2. **The actual code repositories** — split across `MarkFzp/mobile-aloha` (hardware) and `MarkFzp/act-plus-plus` (ML). The ML codebase is named **ACT++**, an evolution of the original [ACT](../entities/act.md).
3. **Author homepages and the dataset drop** — direct links to Fu, Zhao, Finn personal sites and the Google Drive datasets.

## Key claims (artifacts beyond the paper)

| Artifact | Link |
| --- | --- |
| Paper PDF | https://mobile-aloha.github.io/resources/mobile-aloha.pdf (also ingested at `raw/mobile-aloha.pdf`) |
| arXiv | https://arxiv.org/abs/2401.02117 |
| **Tutorial** (build + install) | https://docs.google.com/document/d/1_3yhWjodSNNYlpxkRCPIlvIAaQ76Nqk2wsqhnEVM6Dc |
| **Datasets** (Google Drive) | https://drive.google.com/drive/folders/1FP5eakcxQrsHyiWBRDsMRvUfSxeykiDc |
| **Hardware code** | https://github.com/MarkFzp/mobile-aloha |
| **ML code (ACT++)** | https://github.com/MarkFzp/act-plus-plus |
| Author: Zipeng Fu | https://zipengfu.github.io/ |
| Author: Tony Z. Zhao | https://tonyzhaozh.github.io/ |
| Author: Chelsea Finn | https://ai.stanford.edu/~cbfinn/ |

> [!note] MarkFzp = Zipeng Fu's GitHub handle
> Both code repos live under `MarkFzp` (Zipeng Fu's personal GitHub). The hardware repo is the build-it-yourself BOM + assembly + driver code; the ML repo is the policy-training code (ACT++).

### Page sections (per the project page itself)

- Team
- Abstract
- Autonomous Skills (video grid)
- Teleoperation (video grid)
- Robustness and Repeatability (video grid)
- Failures (video grid — unusual for a project page; shows failure modes alongside successes)
- Acknowledgements
- BibTeX

### What "ACT++" is (inferred from the repo name + paper §6.1)

The Mobile ALOHA paper describes its ML stack as "ACT [104]" plus additional pieces — base-action support (16-dim action vector with 2 base-vel dims appended), co-training with static ALOHA data, and the action-chunk delay-shift trick for mobile-base velocity-control delay. The `act-plus-plus` repo name suggests these mobile-specific extensions are bundled as a successor to the original ACT codebase. See [ACT++ entity](../entities/act-plus-plus.md).

## Entities mentioned

- [Mobile ALOHA + ALOHA platform line](../entities/aloha.md) — the project this page documents.
- [ACT](../entities/act.md) — the original IL method.
- [ACT++](../entities/act-plus-plus.md) — the mobile-extended ML codebase named on this page.
- [Tony Z. Zhao](../entities/tony-zhao.md), [Zipeng Fu](../entities/zipeng-fu.md), [Chelsea Finn](../entities/chelsea-finn.md) — author entities.
- [ViperX 300](../entities/viperx-300.md) — hardware substrate.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — the IL method documented across the page.

## Open questions

- **Repo activity vs the 2024 paper** — both `MarkFzp/mobile-aloha` and `MarkFzp/act-plus-plus` were the canonical references in 2024; whether they've been maintained since, or whether downstream forks (e.g. via [LeRobot](../entities/lerobot.md)) have taken over, is worth checking.
- **Tutorial doc currency** — the Google Doc tutorial isn't versioned; the wiki should re-check it on any future downstream-of-Mobile-ALOHA ingest (e.g. [Grievous](../entities/grievous.md)).
- **Dataset Google Drive sizing** — not enumerated on the project page; would need a fresh visit to confirm.

## Why this matters

Companion to the [Mobile ALOHA paper](mobile-aloha-paper.md): the paper is the what/why, this is the operational where (URLs to the code, tutorial, datasets, author pages). Also surfaces **ACT++** as a distinct codebase artifact deserving its own entity.
