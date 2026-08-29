---
title: "Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix (Wang, Wei, Ling 2026)"
type: source
url: https://arxiv.org/abs/2607.06925
author: Yufeng Wang, Lu Wei, Haibin Ling (Stony Brook University / Westlake University)
published: 2026-07-08
ingested: 2026-07-26
local_path: raw/2607.06925.pdf
sha256: c0a9daf7fd93bcc465c2b6b13b63b34f2de9dc5299fdab1eb7d58bb04fdaccea
venue: arXiv preprint (cs.AI)
license: arXiv
format: pdf
tags: [world-model, jepa, instruction-leakage, spatial-relations, goal-conditioning, evaluation-confound, reference-anchors, goal-free-dynamics, babyai, language-table]
---

# Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix

## Summary

An **evaluation-methodology critique** of compact goal-conditioned [world models](../concepts/world-models/world-model.md) (not a [LeCun](../entities/yann-lecun.md)/coauthor paper). It targets the popular recipe — a [JEPA](../concepts/world-models/jepa.md) latent + a sparse set of explicit metric **reference anchors** + a language-goal token (à la [LeWorldModel](../entities/leworldmodel.md)/Maes 2026) — that promises to ground relational goals like "put the red block left of the blue block." The paper's finding: such a model *appears* to ground spatial relations superbly (0.90 relation-readout accuracy) but this is **[instruction leakage](../concepts/world-models/instruction-leakage.md)** — the predictor is **transcribing the instruction, not perceiving the scene**. The fix: **keep the goal out of the dynamics** (it belongs to the planner's cost, not the transition model) and supervise the read path — which recovers genuine, instruction-independent grounding.

## Key claims

- **The confound, made falsifiable:** *instruction leakage occurs when the scored quantity is transcribable from the instruction (the instruction names the answer) and is essentially independent of how predictive the non-instruction inputs (action, state) are.*
- **The evidence (detection protocol):**
  - A goal-conditioned model hits **0.90** relation-readout accuracy, deceptively robust to referential ambiguity.
  - **Withholding the goal collapses it to chance: 0.90 → 0.27** (3 seeds).
  - A **counterfactual instruction** makes predicted anchors follow the *false* instruction **94.5%** of the time (true scene 2.3%; N=256).
  - A validated positive control (engineered-leaky model) fires the probes at 0.97.
- **Where it leaks:** the authors' tabletop and the external **BabyAI** benchmark leak (instruction names the relation); a **Language-Table** forward-dynamics world model whose instruction names *referents* (not the answer) does **not** leak — until the instruction is augmented to name the direction. An action-ablation dose-response shows degrading the action **never increases** leakage — the opposite of what predictor-competition would predict (the model transcribes even against a perfect action).
- **The fix — goal-free dynamics:** train the predictor to *never see the goal* (a world model's transition should predict the consequences of **actions**; the goal enters only through the planner's cost) plus a supervised **read path** for the anchors. Result: genuine grounding, **0.88 readout identical with and without the goal**, and control recovers to the no-goal baseline — confirming goal-conditioning was actively *hurting*.
- **Generality:** the detection protocol (goal-withheld + counterfactual probes, run on the training render distribution) and the remedy apply to **any** goal-conditioned world model whose instruction names the scored quantity.

## Entities mentioned

- [LeWorldModel](../entities/leworldmodel.md) — the compact JEPA+anchors+goal recipe (Maes et al. 2026) the paper analyzes.
- Authors: Yufeng Wang, Lu Wei (Stony Brook), Haibin Ling (Westlake University).

## Concepts touched

- [Instruction leakage](../concepts/world-models/instruction-leakage.md) — the named confound this paper introduces.
- [JEPA](../concepts/world-models/jepa.md) / [World model](../concepts/world-models/world-model.md) — the model class critiqued.

## Open questions

- Does instruction leakage also inflate the headline results of goal-conditioned VLAs (which likewise see the instruction), or is it specific to explicit-anchor world models?
- The goal-free-dynamics fix leaves a residual gap to oracle attributed to *dynamics fidelity* — how much of compact-world-model relational control is bottlenecked there rather than at grounding?
