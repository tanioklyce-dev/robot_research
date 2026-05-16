---
title: Mechanistic interpretability
type: concept
created: 2026-05-15
updated: 2026-05-15
sources: 1
tags: [mechanistic-interpretability, anthropic, chris-olah, sparse-autoencoders, feature-extraction, ai-safety]
---

**Mechanistic interpretability** — the research program of *reading and intervening on the internal computations of trained neural networks*, in the hope of understanding what concepts a model represents and how it uses them to produce behavior. The intellectual descendant of neural-network "circuits" work pioneered by **Chris Olah** and collaborators. Distinct from input-output interpretability (e.g., LIME, attention heatmaps) in that it targets the model's *intermediate representations* directly.

## Definition

Given a trained model `f_θ`, mechanistic interpretability asks:

1. **Feature extraction**: what concepts are represented in `f_θ`'s internal activations? Modern best-practice technique is **sparse autoencoders (SAEs)** — a separate learning algorithm that trains a wider, sparser representation `z = SAE(activation)` such that each `z_i` often corresponds to a human-understandable concept.
2. **Feature steering**: once a feature is extracted, can you *increase or decrease* its strength in `f_θ` and observe a corresponding change in behavior? This is the operational test for whether a feature is causally relevant, not just statistically present.
3. **Circuit discovery**: how do features combine through the model's layers to produce the model's outputs? This is the *mechanistic* part — finding the actual circuits.

## Key references in this wiki
- **[Welch Labs Illustrated Guide to AI, Vol I — Ch 7](../sources/welchlabs-illustrated-guide-to-ai.md)** (Stephen Welch, 2026) — pedagogical hub for the field. Anchors on Anthropic's Templeton et al. 2024 sparse-autoencoder work and Chris Olah's "dark matter of interpretability" framing.
- **Anthropic's [Claude](../entities/anthropic.md)** is the canonical demonstration system in modern mech-interp work — Welch's Ch 7 walks through the "ask Claude to forget a phrase; then increase the internal-conflict feature and watch it admit it can't" demonstration as the field's archetypal feature-steering result.

## Core findings (per Welch Ch 7)
- **Sparse autoencoders extract human-meaningful features.** Templeton et al. 2024 (Anthropic) — "Scaling Monosemanticity" — demonstrated this at scale on Claude. Features for "cats," "dogs," "WiFi networks," up to abstract concepts like "internal conflict."
- **Features can be steered.** Boosting a feature's value in the live model produces qualitatively predictable behavioral changes. This is the most direct evidence that the extracted features are causally part of how the model produces behavior, not just descriptive correlates.
- **We're still in the early innings.** Olah's "dark matter" framing (quoted in Welch Ch 7): *"the features we haven't been able to extract may be a kind of dark matter of interpretability"* — i.e., **we've extracted <1% of the concepts** large language models must know about. The known features are like the brightest stars; everything dimmer is invisible.

## Why this matters in this wiki

- **Adjacent to [AI safety and alignment](ai-safety-alignment.md)**. The standard safety pitch for mech-interp is "if we understood the model, we could trust it (or distrust it for the right reasons)." Welch frames this as "how would you know if a language model is lying to you?" Anthropic's [Claude](../entities/anthropic.md) is both the safety-research target and the operational system being interpreted.
- **Adjacent to [Chain of thought](chain-of-thought.md)**. CoT faithfulness depends on whether the model's verbalized reasoning matches its actual internal computation — a question mech-interp is in principle positioned to answer. As of 2026 it can't yet.
- **Adjacent to [Corrigibility](corrigibility.md)**. The "feature for being corrigible" is the kind of internal concept mech-interp would need to identify and reason about. Currently aspirational.

## Current state (2026-05)
- **Sparse autoencoders are state-of-the-art** as of Templeton et al. 2024. Multiple labs (Anthropic, Google DeepMind, OpenAI internal) have replicated.
- **Scaling**: SAEs themselves now have to be trained at scale — extracting features from a frontier-scale LLM means training an SAE that's a substantial model in its own right.
- **Olah's pessimism on coverage**: ~1% of concepts extracted as of mid-2024. Welch quotes this as the chapter's anchor caveat — the field is real, the techniques work, the coverage problem is brutal.
- **No dedicated pedagogy primary-source in the wiki besides Welch Ch 7.** Templeton et al. 2024 (Scaling Monosemanticity) is the canonical Anthropic paper but is not yet in `raw/`.

## Related
- [AI safety and alignment](ai-safety-alignment.md) — mech-interp's primary motivating sponsor.
- [Anthropic](../entities/anthropic.md) — the lab that drives the modern SAE-based program.
- [Chain of thought](chain-of-thought.md) — adjacent: CoT faithfulness is a mech-interp-shaped question.

## Mentioned in
- [Welch Labs Illustrated Guide to AI, Vol I](../sources/welchlabs-illustrated-guide-to-ai.md)

## Open follow-ups
- **Templeton et al. 2024 — *Scaling Monosemanticity*** (Anthropic). Primary-source candidate. Would let this concept page cite specific feature-extraction numbers, model scales, and demonstrations.
- **Olah's "dark matter of interpretability"** essay/talk (July 2024). Primary-source candidate; would let the page cite the framing directly.
- **Chris Olah** entity stub — would tie together the SAE / circuits lineage at Anthropic + earlier Distill / OpenAI work.
- **Sparse autoencoder** concept page — the technique deserves its own page if the field gets deeper coverage. Currently rolled into this concept.
