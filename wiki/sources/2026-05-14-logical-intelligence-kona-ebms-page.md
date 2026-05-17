---
title: "Kona: Energy-Based Models (EBMs) for AI Reasoning (Logical Intelligence)"
type: source
url: https://logicalintelligence.com/kona-ebms-energy-based-models
demo_url: https://sudoku.logicalintelligence.com
author: Logical Intelligence (corporate page; no individual byline)
published: 2026-05-14
ingested: 2026-05-17
created: 2026-05-17
updated: 2026-05-17
tags: [logical-intelligence, kona, ebm, energy-based-model, primary-source, positioning, sudoku-demo, certification, post-llm]
---

> [!note] Ingest depth and provenance
> **Primary source** — but a short marketing / positioning page, not a technical document. No architecture, training procedure, parameter counts, benchmarks, or quantitative comparisons. The value of this source is **verbatim positioning quotes from Logical Intelligence itself** (rather than secondary reporting) and the **live Sudoku demo** at `sudoku.logicalintelligence.com`. Pair with the secondary materials cited via the [Aleph EBM video source](2026-05-aleph-ebm-refuses-bullshit-video.md) for substance.

## Summary

The product page for **Kona 1.0** on `logicalintelligence.com`, dated **2026-05-14**. Establishes Logical Intelligence's own framing of Kona: **"Certainty, Not Probability"** — a reasoning substrate that **enforces constraints** rather than **predicting outcomes**, designed to **sit beneath modern AI stacks** as a verification layer for systems where failure is not an option. Links to a live interactive Sudoku demo comparing Kona to LLMs.

## Verbatim positioning (10 sentences, in page order)

These are the load-bearing quotes — reproduced exactly so they can be cited from downstream pages:

1. "Kona is Logical Intelligence's core Energy-Based Model and the foundation of everything we build."
2. "It is not a chatbot, assistant, or generator."
3. "Language models are good at interaction and expression."
4. "They help people ask questions and explore ideas."
5. "But when software controls physical assets or financial risk, something else has to decide what actions are allowed before they happen."
6. "Logical Intelligence builds that layer."
7. "Kona is a reasoning system designed to sit beneath modern AI stacks, evaluating what is valid, safe, and permissible across all possible states of a system."
8. "It does not predict likely outcomes."
9. "It enforces constraints."
10. "It replaces trust with proof and makes certification, audit, and deployment possible where failure is not an option."

Page subtitle (verbatim): **"Certainty, Not Probability."**

Page description (verbatim): "Kona delivers AI reasoning via Energy-Based Models (EBMs). It provides deterministic, verifiable intelligence for critical systems—a fundamental shift from probabilistic LLMs."

## Sudoku demo

Live interactive demo at **`sudoku.logicalintelligence.com`** comparing Kona to frontier LLMs.

Methodologically interesting detail (verbatim from the demo page): **"the demo disabled code execution for both Kona and LLMs to prevent 'cheating' via brute-force algorithms — Kona actually reasons through the Sudoku without access to code execution."** This is a meaningful fairness control: LLMs with code interpreter access can brute-force Sudoku with backtracking; the comparison is only meaningful if both sides reason in their natural mode.

Demo framing (verbatim): **"Kona evaluates the entire puzzle at once. Solved in seconds, Kona reveals the first glimpse of a self-aligning system and the road to AGI."** Note the "evaluates the entire puzzle at once" language — consistent with Kona being **non-autoregressive** (whole-state evaluation rather than cell-by-cell prediction). Contrast: **"Most AI models guess, backtrack, and get stuck."**

User interaction: paste a 9×9 Sudoku puzzle (9 lines of 9 digits, `0` or `_` for blanks) or click "load a random hard puzzle," then compare model outputs side by side.

> [!note] Not benchmarked here
> The demo doesn't publish accuracy rates, solve times, or compute costs. The Bodnia interview summary cited via [the Aleph EBM video source](2026-05-aleph-ebm-refuses-bullshit-video.md) is the source for the **~$4 Kona vs ~$15,000 frontier-LLM** cost claim on Sudoku — not this page.

## Key claims

- **Kona is positioned as a verification / certification layer**, not a user-facing model. The "below modern AI stacks" framing is explicit.
- **Constraint enforcement vs outcome prediction** is the framing axis. The page distinguishes Kona from LLMs not on capability but on **mode**: LLMs predict; Kona constrains.
- **"Replaces trust with proof"** is the operative verifiability claim — the same thread as [Aleph](../entities/aleph.md)'s [formal-verification](../concepts/learning/formal-verification.md) pipeline, applied here to Kona's reasoning layer.
- **"Across all possible states"** language suggests an EBM that operates over global configurations (consistent with the "evaluates the entire puzzle at once" Sudoku framing) rather than locally / autoregressively.

## Entities mentioned

- [Logical Intelligence](../entities/logical-intelligence.md) — page author.
- [Kona](../entities/kona.md) — the model.
- [Aleph](../entities/aleph.md) — sibling product, name-checked as "delivering verified reasoning today."

## Concepts touched

- [Energy-based models](../concepts/learning/energy-based-models.md) — Kona's substrate.
- [Formal verification](../concepts/learning/formal-verification.md) — the "replaces trust with proof" framing is in the same conceptual family.

## Why it matters in this wiki

- **First primary-source coverage of Kona positioning.** All prior Kona content in the wiki came via secondary reporting ([BusinessWire press release](2026-05-aleph-ebm-refuses-bullshit-video.md), Bodnia interview summary). This page is Logical Intelligence's own framing — useful for downstream pages that want to cite the company's stated position rather than journalists' paraphrases.
- **Concrete public artifact** (Sudoku demo) — the **first publicly testable Kona-vs-LLM comparison** anyone can run.
- **Disambiguates Kona from Aleph in Logical Intelligence's own words**: Kona is the **reasoning substrate**; Aleph is the **delivery / orchestration layer**. The same split surfaced via the [video source page](2026-05-aleph-ebm-refuses-bullshit-video.md), now confirmed by the vendor's own positioning copy.

## Open questions / TBD

- **All the architecture questions remain open** — the page is silent on training loss, data, parameter count, inference procedure, and benchmark numbers. The page is marketing copy, not a tech report. Need a real Kona paper / tech report to advance any of these.
- **Sudoku demo results, quantified**: the demo lets users compare side-by-side but doesn't publish aggregate accuracy or timing. Worth a future ingest if someone (Logical Intelligence or a third party) publishes systematic comparison numbers.
- **What does "self-aligning system" mean in Kona's context?** The phrase appears on the Sudoku demo page paired with "the road to AGI." Could be substantive (a property of the EBM training objective) or marketing — unclear without a tech report.
- **Demo robustness**: which Sudoku puzzles does Kona actually solve? Hard puzzles only? Standard 9×9 or also variants? Not addressed.
