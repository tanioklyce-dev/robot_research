---
title: "AMI Labs Intelligence Hub — Research page (The French Tech Journal tracker)"
type: source
url: https://ami.frenchtechjournal.com/research
local_path: raw/2026-10-24-ami-labs-intelligence-hub-research.txt
sha256: 2bca649426a38045b158b8d93ff77663aa67cb9c505fbed31811ae1a150511de
author: The French Tech Journal (third-party publication; not AMI Labs)
published: 2026-10-24
ingested: 2026-10-24
venue: ami.frenchtechjournal.com — "AMI Labs Intelligence Hub, powered by The French Tech Journal"
format: "rolling web page; no publication date (`published` is the capture date). The /team and /docs pages were captured alongside. Paper blurbs are Semantic-Scholar-style auto-summaries."
tags: [ami-labs, lecun, tracker, secondary, publication-list, jepa, world-model, aggregator, french-tech-journal]
---

# AMI Labs Intelligence Hub — Research (The French Tech Journal)

> [!warning] A third-party tracker, and an author-matched feed
> This is **not an AMI Labs page**. It is a hub run by *The French Tech Journal* that lists *"the latest papers from the AMI Labs team."* The list is evidently built by **matching author names** against a roster and linking Semantic Scholar entries:
> - It includes papers on DXA medical imaging, music transcription, Rust code verification, antibody design and **UV degradation in solar cells**.
> - Many entries are LeCun's NYU co-authorships with no AMI byline.
> - At least one is likely a **name collision**: the solar-cell paper attributed to a "Xuefeng Hu".
>
> **Inclusion here does not mean a paper is AMI Labs work.** For that, check the paper's own affiliation line, as the wiki does on the [AMI Labs](../entities/ami-labs.md) page.

## Summary

The page is a reverse-chronological feed of about 40 papers (2026-06 to 2026-10-14) by people the tracker associates with [AMI Labs](../entities/ami-labs.md). Two are "highlighted" with editorial write-ups:
- **Patch Policy** (2026-08-05, Meta-FAIR / Courant / AMI Labs byline);
- **Interpreting Physics in Video World Models** (Garrido, Rabbat; 2026-02-04, Meta FAIR).

The /team page lists **six co-founders**. The /docs page holds one document: LeCun's April 2026 Brown Lemley Lecture deck.

Its value to the wiki is as a **discovery feed** for the JEPA/world-model line. It is not a source for affiliation, roles or results.

## Key claims

### Co-founder roster (/team; unverified, secondary)
| Name | Role (as listed) | Base |
|---|---|---|
| Alexandre LeBrun | CEO & co-founder | Paris |
| Laurent Solly | COO & co-founder (12 yrs Meta, VP Europe) | Paris |
| Michael Rabbat | VP of World Models & co-founder (ex-FAIR Montreal director) | Montreal |
| Pascale Fung | Chief Research & Innovation Officer & co-founder (ex-FAIR senior director) | Paris |
| Saining Xie | **Chief Science Officer** & co-founder (NYU Courant) | New York |
| Yann LeCun | Executive Chairman & co-founder | Paris / New York |

> [!note] Saining Xie as CSO is still unconfirmed by a primary
> The wiki's [AMI Labs page](../entities/ami-labs.md) (from the MIT Technology Review interview) records LeCun declining to confirm Xie as chief scientist in January 2026. This tracker lists him as CSO, without citation. Treat it as reported, not established.

### World-model and robotics papers on the feed, against wiki coverage (2026-10-24)

| Paper (date on feed) | In wiki? |
|---|---|
| [LeHami: Symplectic Latent Dynamics for World Models](lehami-symplectic-latent-dynamics-paper.md) (10-11) | **Yes**, ingested today |
| [Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models](preserving-unstable-modes-inverse-dynamics-paper.md) (10-06) | **Yes** (ingested 2026-10-24). Feed summary: exact action reconstruction makes the encoder injective on the finite-horizon reachable subspace, with convergence to the controllable unstable subspace. **A theory paper for the inverse-dynamics barrier in the [collapse synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md)** |
| [H-JEPA (hierarchical)](h-jepa-hierarchical-world-models-paper.md) (10-05) | Yes |
| [AD-E2E-JEPA](ad-e2e-jepa-autonomous-driving-paper.md) (09-28) | Yes |
| LeVJEPA (08-27), LpWM (08-24), AdaJEPA (06-30), SkyJEPA (06-22), Causal-JEPA, Music-JEPA, HP-JEPA, Patch Policy | Yes (entity or source pages exist) |
| [Interpreting Physics in Video World Models](interpreting-physics-video-world-models-paper.md) (Garrido, Rabbat; 02-04) | **Yes** (ingested 2026-10-24). Interpretability of how V-JEPA 2 represents physical variables |
| [MJEPA](mjepa-audio-visual-paper.md) audio-visual JEPA (Bardes, Rabbat; 06-23) | **Yes** (ingested 2026-10-24) |
| *Purify Before You Align*, *The Lattice of Transition Laws* (Jiatao Gu; 10-14, 10-08) | No (generative modelling; lower priority) |

## Entities mentioned
- [AMI Labs](../entities/ami-labs.md) · [Yann LeCun](../entities/yann-lecun.md) · [LeHami](../entities/lehami.md)

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md) and [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md), via the unstable-modes paper it surfaces.

## Open questions
- Who maintains the roster, and on what evidence are non-founders (Jiatao Gu, Chen Wei, Julia Kempe, Tengyu Ma, Xinyi Wan …) linked as "team"? None of their AMI affiliations is verified here.
- The **Brown Lemley Lecture deck** (April 2026), linked as an "official AMI Labs public document": now [ingested](lecun-brown-lemley-lecture-2026.md). No primary host found.
