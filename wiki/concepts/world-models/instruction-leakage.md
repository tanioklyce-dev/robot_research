---
title: Instruction leakage
type: concept
created: 2026-07-26
updated: 2026-07-26
sources: 1
tags: [instruction-leakage, evaluation-confound, goal-conditioning, world-model, jepa, spatial-relations, benchmark-pitfall]
---

# Instruction leakage

An **evaluation confound** in goal-conditioned [world models](world-model.md), named and characterized by [Grounding Spatial Relations in a Compact World Model (Wang, Wei, Ling 2026)](../../sources/grounding-spatial-relations-compact-wm-paper.md).

## Definition

> **Instruction leakage occurs when the scored quantity is transcribable from the instruction (the instruction names the answer) and is essentially independent of how predictive the non-instruction inputs (action, state) are.**

When a world model is conditioned on a language goal that *names the very thing being evaluated* (e.g. goal = "red block **left of** blue block", metric = did it get the left/right relation right), a predictor can score near-perfectly by **transcribing the instruction rather than perceiving the scene**. The high number measures instruction-copying, not grounding.

## Detection protocol

Two probes, run on the training render distribution, separate perception from transcription:
1. **Goal-withheld:** remove the goal at test time. Genuine grounding is robust; leakage collapses to chance (the paper's case: **0.90 → 0.27** relation-readout accuracy).
2. **Counterfactual instruction:** feed a *false* goal. A leaking model follows the false instruction (the paper: predicted anchors follow the counterfactual **94.5%** of the time vs 2.3% matching the true scene). A validated positive control (an engineered-leaky model) fires the probes at ~0.97.

A telltale signature: **degrading the action never increases leakage** — the opposite of what genuine predictor-competition would produce — because the model transcribes even against a perfect action.

## The fix — goal-free dynamics

Leakage is an architecture smell: *the goal is in the dynamics model where it doesn't belong.* A world model's transition should predict the consequences of **actions**; the goal should enter only through the **planner's cost**. Training with **goal-free dynamics** (predictor never sees the goal) plus a supervised read path recovers genuine, instruction-independent grounding (readout ~0.88 identical with and without the goal), and control recovers to the no-goal baseline — showing goal-conditioning was actively hurting.

## Why it matters

The confound applies to **any goal-conditioned world model whose instruction names the scored quantity** — including the compact [JEPA](jepa.md)-latent + reference-anchor + language-goal recipe (e.g. [LeWorldModel](../../entities/leworldmodel.md)-style). It's a reusable red-team check for the wiki's world-model and (plausibly) instruction-following VLA evaluations: a headline "grounding" number should survive goal-withheld and counterfactual probes before being believed.

## Related concepts

- [World model](world-model.md) / [JEPA](jepa.md) — the model class where the confound arises.
- [Identifiability](identifiability.md) — a complementary "is the model really recovering the world?" question, from the representation side rather than the evaluation side.

## Mentioned in

- [Grounding Spatial Relations in a Compact World Model (Wang, Wei, Ling 2026)](../../sources/grounding-spatial-relations-compact-wm-paper.md) — introduces and characterizes instruction leakage.
