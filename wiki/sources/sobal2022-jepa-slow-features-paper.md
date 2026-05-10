---
title: Sobal et al. 2022 — Joint Embedding Predictive Architectures Focus on Slow Features (PLDM precursor)
type: source
url: https://arxiv.org/abs/2211.10831
author: Vlad Sobal, Jyothir S V, Siddhartha Jalagam, Nicolas Carion, Kyunghyun Cho, Yann LeCun
affiliation: Not stated on the arxiv abstract page (NYU + FAIR — Cho/LeCun connection)
published: 2022-11-20 (NeurIPS 2022 SSL Theory and Practice Workshop, short paper)
ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
tags: [pldm, sobal, jepa, slow-features, representation-learning, vicreg, simclr, lecun, precursor]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (PDF not in `raw/`). Filed as the precursor to [PLDM (Sobal et al. 2025)](pldm-paper.md), to close the lineage of "end-to-end JEPA-as-WM" that LeWM critiques.

## Summary

**Sobal et al. 2022** — short paper presented at the NeurIPS 2022 SSL Theory and Practice Workshop. Authors: Vlad Sobal, Jyothir S V, Siddhartha Jalagam, Nicolas Carion, Kyunghyun Cho, Yann LeCun (NYU + FAIR). The **first paper in the PLDM lineage**. Establishes the central representational claim that motivates the entire end-to-end-JEPA-as-WM line: **JEPA representations preferentially encode slowly-varying features.**

The setup: a simple pixel environment with a moving dot and varying background distractors. JEPA models (trained with **VICReg** and **SimCLR** objectives) are compared against reconstruction-based alternatives. The result: JEPA representations selectively encode the dot's location (a slowly-varying feature) — but **fail when the distractor noise is fixed across timesteps**, exposing that the "slow-features" inductive bias depends on temporal variability in the input distribution.

This paper does *not* introduce PLDM as a method (the 2025 paper does that). Its contribution is **diagnostic**: characterizing what JEPA representations actually encode, and exposing a failure mode (fixed-distractor noise) that motivates later work on more robust anti-collapse mechanisms.

## Abstract (verbatim, paraphrased opener)

> "Joint Embedding Predictive Architectures (JEPA) trained with VICReg and SimCLR objectives in the fully offline setting" — investigated for pixel-based environments. The work compares reconstruction-free JEPA approaches against generative alternatives.

(Full abstract not extracted verbatim — the arxiv page summary is paraphrased rather than copied verbatim. PDF ingest would let us quote directly.)

## Key claims

- **JEPA encodes slow features.** When trained on sequences of `(observation, next observation)` pairs, JEPA encoders preferentially capture the slowly-varying components of the observation — exactly the components useful for downstream control. This is the *representational* justification for using JEPA in WM-style pipelines.
- **Failure mode: fixed-distractor noise.** When the distractor (background) noise is *fixed* across timesteps rather than varying, JEPA fails to learn useful representations. The slow-features bias depends on temporal variability in the input distribution.
- **VICReg and SimCLR both work.** The "JEPA encodes slow features" claim doesn't depend on a specific objective — both contrastive ([SimCLR](../glossary.md#simclr)) and variance-covariance ([VICReg](../glossary.md#vicreg)) flavors of JEPA training exhibit the same representational behavior.
- **Bridge to control.** The slow-features framing is the conceptual link between SSL JEPA work (representation learning for its own sake) and the JEPA-as-WM line (slow features = useful state for planning).

## Why it matters in this wiki

- **The "slow features" framing is foundational** for everything in [Module 11](../syntheses/curriculum-11-jepa-deep.md) and [Module 12](../syntheses/curriculum-12-lewm-deep-dive.md). When a JEPA paper says "the latent encodes the dynamically-relevant features," this is the paper that backs that claim experimentally.
- **The fixed-distractor failure mode is the proximate ancestor of the collapse problem.** Module 11's collapse-prevention zoo addresses a different failure mode (encoder degenerates to a constant); the 2022 paper's fixed-distractor failure is a *third* failure mode — the encoder doesn't collapse but it doesn't pick up the right features either. Worth noticing as a separate axis.
- **Closes the [PLDM](../entities/pldm.md) lineage.** Module 11's collapse-prevention zoo §5 (multi-fix soup) cites PLDM via [the 2025 paper](pldm-paper.md). The 2022 paper is the predecessor that establishes *why* PLDM was worth proposing in the first place.

## Predecessor / successor

- **Successor:** [PLDM (Sobal et al. 2025)](pldm-paper.md) — the planning-and-stress-test followup that builds on this paper's representational claim.

## Entities mentioned

- [PLDM](../entities/pldm.md) — the family entity; this paper is the 2022 predecessor.
- [Yann LeCun](../entities/yann-lecun.md) — senior author.

## Concepts touched

- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — this paper's representational diagnosis.
- [Learned latent space](../concepts/latent-space.md) — what the slow-features framing is *about*.

## Open questions / TBD

- **Full PDF ingest** — the abstract page summary is paraphrased; primary-source quotes would tighten the slow-features claim. Drop the PDF in `raw/` and re-ingest.
- **Vlad Sobal author entity page** — would anchor the lead-author thread of the PLDM lineage.
- **Connection to neuroscience's "slow feature analysis"** (Wiskott & Sejnowski 2002, "Slow Feature Analysis: Unsupervised Learning of Invariances") — the inspiration for the term "slow features" in this paper. Worth flagging if the curriculum picks up the SFA-line connection.
