---
title: "World Models: Enabling the Next AI Revolution — Yann LeCun, Brown University Lemley Lecture (2026-04-01, slides)"
type: source
url: https://ami.frenchtechjournal.com/docs
fetch_url: https://ami.frenchtechjournal.com/documents/lecun-20260401-brown-lemley-2.pdf
local_path: raw/2026-04-01-lecun-brown-lemley-lecture.pdf
sha256: fcdd62fdcd69d33f78fcd8e35796aa1dfd7aa8e9e55c6bc080f83658f6364b4a
author: Yann LeCun (Courant Institute NYU; AMI Labs)
published: 2026-04-01
ingested: 2026-10-24
venue: Brown University, Lemley Lecture
format: "slide deck, 47 slides (Google Slides export, PDF title '20260401-brown'); text extracted, figures not inspected. Obtained via a third-party tracker that labels it an 'official AMI Labs public document'. No original host was found, so provenance is the tracker's."
tags: [lecun, ami-labs, world-model, jepa, sigreg, lejepa, leworldmodel, v-jepa-2, dino-wm, hierarchical-planning, objective-driven-ai, mpc, talk, slides]
---

# Yann LeCun — Brown University Lemley Lecture (2026-04-01)

> [!note] Provenance
> Obtained from the [AMI Labs Intelligence Hub](ami-labs-intelligence-hub-research.md), a third-party tracker that hosts it as an *"official AMI Labs public document."* The deck carries LeCun's NYU and AMI Labs affiliations and matches his known talk content. No primary host was located. If one turns up, record it as `fetch_url` and re-seal.

## Summary

This is LeCun's standard 2026 world-model talk, delivered **as AMI Labs' pitch**. AI fails at what animals do easily (Moravec). A 4-year-old has seen about as many bytes (1.1e14) as an LLM is trained on (0.9e14). Intelligence is fast zero-shot adaptation, so *"AGI makes no sense."* The road there is **objective-driven "System 2" agents**: a world model predicts consequences in an abstract representation space; actions come from search under task and **guardrail** objectives; and a **hierarchical** world model plans at multiple time scales.

The technical slides walk the JEPA line the wiki tracks: SIGReg/LeJEPA → LeWorldModel → I-JEPA / DINOv3 → DINO-WM → V-JEPA 2 and V-JEPA 2-AC. The talk closes with his standing recommendations and AMI's market pitch.

## Key claims
- **What world models should and should not be** (slide "Learning a hierarchy of abstractions"):
  - *Not*: *"world simulators, digital twins, generative models, video generation systems."*
  - *Should be*: *"action-conditioned predictors in abstract representation space, preferably differentiable."*
- **Definition:** *"A causal model that, given an observation of a system and an intervention on the system, predicts the outcome of the intervention … in an abstract representation space."*
- **Agent architectures:** *System 1* (state → action, *"how LLM-based agentic systems work (or don't work)"*) vs *System 2* (planning with a world model, *"how AMI Labs' agentic systems work"*).
- **AMI's stated goals:**
  - self-supervised models of *"any data source"* (high-dimensional, continuous, noisy);
  - agents with **persistent memory (factual, working, episodic, procedural)**, long reasoning chains and hierarchical planning;
  - zero-shot task completion, *"controllable and safe"*.
- **Collapse prevention**, as LeCun groups it:
  - distillation (DINO, I-JEPA, V-JEPA) and information maximisation (SIGReg, VCReg, Barlow Twins), both *"from AMI Labs team members"*;
  - plus MMCR, MCR², W-MSE from other labs;
  - *"over 1300 papers"* on Google Scholar for JEPA.
- **Lineage claim:** world models are *"an old idea in optimal control"*: Kelley–Bryson (1962), Pontryagin / adjoint methods, and his own 1988 Lagrangian formulation of backprop.
- **Recommendations:**
  - abandon generative models (→ joint-embedding), probabilistic models (→ energy-based) and contrastive methods (→ regularised);
  - abandon RL in favour of MPC, *"use RL only when planning doesn't yield the predicted outcome"*;
  - *"if you are interested in human-level AI, don't work on LLMs."*
- **Market pitch:** AMI aims to become *"the main provider of intelligent systems"*, citing turbofan engines (1,000+ sensors) and the A380 (25,000 sensors). Hierarchical JEPA should produce causal models of complex systems, possibly *"human cells, organs, and bodies."*
- Papers cited on slides: arXiv 2603.15381 (how animals learn), 2602.23643 (what intelligence is), 2601.05230 (*"Inferring hidden actions from video"*), 2603.19312 (LeWM), 2511.08544 (LeJEPA), 2411.04983 (DINO-WM), 2507.19468 (DINO-World), 2506.09985 (V-JEPA 2), 2502.11831 (intuitive physics from V-JEPA).

## Reading notes (wiki inference)
- **"Guardrail objectives" are a planning-time safety mechanism.** In this architecture, safety constraints are costs the planner optimises against. That is the same shape as the wiki's [safety filters](../concepts/robotics/safety-filters.md) concept, but placed inside the world-model planner. [LeHami](lehami-symplectic-latent-dynamics-paper.md)'s time-reversal pitch (backward reachable sets) and [Toso et al.](preserving-unstable-modes-inverse-dynamics-paper.md)'s stabilisability result are both, in effect, conditions for such guardrails to be enforceable from a latent.
- The deck makes AMI's commercial thesis explicit: **industrial sensor systems and biomedicine first**, not household robots. That is consistent with LeCun's [Davos](ai-house-davos-2026-lecun-embodied-ai.md) "disembodied physical AI" scope note on the [AMI Labs](../entities/ami-labs.md) page.
- Talk claims are uncited assertions (e.g. the bytes comparison, *"best video representation learning system in the world"*). They are recorded as the founder's positions.

## Entities mentioned
- [Yann LeCun](../entities/yann-lecun.md) · [AMI Labs](../entities/ami-labs.md) · [LeWorldModel](../entities/leworldmodel.md) · [DINO-WM](../entities/dino-wm.md) · [V-JEPA 2](../entities/v-jepa-2.md)

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md) · [SIGReg](../concepts/world-models/sigreg.md) · [World model](../concepts/world-models/world-model.md) · [Optimal control](../concepts/robotics/optimal-control.md) · [Safety filters](../concepts/robotics/safety-filters.md)

## Open questions
- arXiv 2601.05230, *"Inferring hidden actions from video"*: is it ingested? It is directly relevant to learning action-conditioned models from action-free video.
- Is there a primary host (Brown, NYU, AMI) for this deck or a recording of the lecture?
