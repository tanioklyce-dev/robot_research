---
title: Kona
type: entity
subtype: model
created: 2026-05-17
updated: 2026-05-17
sources: 2
tags: [kona, logical-intelligence, ebm, energy-based-reasoning-model, ebrm, non-autoregressive, latent-variable, reasoning, post-llm, lecun]
---

**Kona** — [Logical Intelligence](logical-intelligence.md)'s proprietary **non-autoregressive energy-based reasoning model (EBRM)**. Positioned as a **reasoning substrate underneath modern AI stacks** — specifically as the verification / constraint-satisfaction layer where statistical plausibility is not an acceptable failure mode ([Kona EBMs page](../sources/2026-05-14-logical-intelligence-kona-ebms-page.md); [Aleph EBM video](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)).

## Logical Intelligence's own positioning

From the [Kona product page (2026-05-14)](../sources/2026-05-14-logical-intelligence-kona-ebms-page.md), verbatim:

- Subtitle: **"Certainty, Not Probability."**
- "Kona is Logical Intelligence's core Energy-Based Model and the foundation of everything we build."
- "It is not a chatbot, assistant, or generator."
- "Kona is a reasoning system designed to sit beneath modern AI stacks, evaluating what is valid, safe, and permissible across all possible states of a system."
- "It does not predict likely outcomes. It enforces constraints."
- "It replaces trust with proof and makes certification, audit, and deployment possible where failure is not an option."

The "evaluates ... across all possible states" framing — paired with the [Sudoku demo](https://sudoku.logicalintelligence.com)'s "Kona evaluates the entire puzzle at once" claim — is consistent with **whole-state evaluation** rather than the cell-by-cell / token-by-token mode of autoregressive models.

**Kona 1.0** entered pilots in Q1 2026 with partners in energy, advanced manufacturing, and semiconductor verification.

## Architecture (paraphrased from Bodnia interview summary)

- **Non-autoregressive.** Reasoning is not sequential next-token prediction in language space.
- **Latent-variable + energy-minimization.** The model operates in an **abstract vector space**; natural language is treated as **optional output / user interface**, not the substrate of thought.
- **Energy function over (input, candidate-solution) pairs.** Inference is finding low-energy configurations consistent with the input constraints ([energy-based models](../concepts/learning/energy-based-models.md)).
- **Parameter scale**: 16M–200M parameters, versus hundreds-of-billions for frontier LLMs.

The non-autoregressive + latent-prediction commitment is structurally similar to LeCun's [JEPA](../concepts/world-models/jepa.md) program — same architect on the research board, same architectural commitment to **predicting in representation space** rather than in raw output space. Kona is the **reasoning** branch of that commitment; JEPA is the **predictive representation learning** branch.

## Reported claims

These claims come from the Bodnia interview summary cited via [the Aleph EBM video source page](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md), and are reproduced here with attribution rather than endorsement:

- **Sudoku demo** at **~$4 in compute** vs ~**$15,000** estimated for a frontier LLM on equivalent tasks.
- **"Spontaneous knowledge extrapolation emerged at just 16 million parameters."** Bodnia frames this as **extrapolation** (deriving novel knowledge from rules) vs LLM **interpolation** (recombining training patterns).
- **Bodnia (verbatim, BusinessWire press release)**: "Kona learns by recognizing and correcting its own mistakes, rather than guessing the most likely answer."

> [!warning] Vendor-source caveat
> The cost-comparison and extrapolation claims come from a single founder interview summary. They are reported here, not independently corroborated.

## Relationship to Aleph and to GPT-5.2

In the May 2026 [PutnamBench result](aleph.md), Aleph used **GPT-5.2** as its reasoning engine. Kona is the long-term substitute for that engine in the Aleph pipeline — once Kona is mature enough to take that role. The architecture is **engine-agnostic by design**: Aleph orchestrates and Lean verifies regardless of which reasoning model is underneath.

## Target domains

From the BusinessWire press release and Bodnia interview summary: chip design / semiconductor verification, surgical robotics, smart grids, pharmacology, verified code generation, financial automation, hardware design. The thread is **zero hallucination tolerance**.

## Related

- [Logical Intelligence](logical-intelligence.md) — vendor.
- [Aleph](aleph.md) — the orchestrator Kona slots into.
- [Energy-based models](../concepts/learning/energy-based-models.md) — the substrate.
- [JEPA](../concepts/world-models/jepa.md) — sibling EBM-flavored architecture from the LeCun-aligned research line; predictive-representation branch.
- [IBC](ibc.md) — older EBM application (imitation learning).
- Autoregressive next-token prediction (the standard LLM training objective) — what Kona is positioned against.

## Public demo

**[sudoku.logicalintelligence.com](https://sudoku.logicalintelligence.com)** — live interactive demo comparing Kona to frontier LLMs on Sudoku. Methodologically: **code execution is disabled for both sides** to prevent LLMs from brute-forcing the puzzle through a code interpreter. Detail and verbatim framing on the [Kona EBMs page source](../sources/2026-05-14-logical-intelligence-kona-ebms-page.md).

## Mentioned in

- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)
- [Kona: Energy-Based Models (EBMs) for AI Reasoning — Logical Intelligence page](../sources/2026-05-14-logical-intelligence-kona-ebms-page.md)
