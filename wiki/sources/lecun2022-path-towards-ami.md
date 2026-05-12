---
title: "A Path Towards Autonomous Machine Intelligence (LeCun, 2022)"
type: source
url: https://openreview.net/forum?id=BZ5a1r-kVsf
local_path: raw/10356_a_path_towards_autonomous_mach.pdf
author: Yann LeCun
affiliation: Courant Institute (NYU) + Meta-FAIR
published: 2022-06-27 (Version 0.9.2)
ingested: 2026-05-11
created: 2026-05-11
updated: 2026-05-11
tags: [lecun, jepa, h-jepa, world-model, ami, energy-based-model, self-supervised, configurator, intrinsic-motivation, position-paper, foundational]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/10356_a_path_towards_autonomous_mach.pdf`, 62 pages, Version 0.9.2 dated 2022-06-27). Sections 2 (introduction), 3 (architecture), 4 (world model / SSL / EBM / JEPA / H-JEPA), 5 (actor), 6 (configurator), 7 (intrinsic cost), and 8 (discussion) read in full; appendices on amortized inference and notation skimmed. This source page is **long because the paper is foundational** — multiple existing wiki pages (JEPA, World model, Yann LeCun) carry "open question" annotations that flag this paper as a gap. The page is structured to be the canonical reference for what's actually in the document.

## Summary

**"A Path Towards Autonomous Machine Intelligence"** — LeCun's 2022 position paper, the **architectural blueprint for the entire [JEPA](../concepts/jepa.md) research program** that has since produced [V-JEPA 2](v-jepa-2-paper.md), [V-JEPA 2.1](v-jepa-2-1-paper.md), [LeWorldModel](leworldmodel-paper.md), [DINO-WM](dino-wm-paper.md), [DINO-world](dino-world-paper.md), [JEPA-WMs](jepa-wms-paper.md), [PLDM](pldm-paper.md), [LeJEPA](lejepa-paper.md), and [VLA-JEPA](vla-jepa-paper.md).

The paper is **explicitly not a technical paper** — it is a vision document. LeCun proposes an overall cognitive architecture for autonomous agents that combines: (1) a configurable, predictive **world model** trained by self-supervised learning, (2) **hierarchical Joint-Embedding Predictive Architectures (JEPA / H-JEPA)** as the technical mechanism for that world model, (3) **non-contrastive, regularized energy-based learning** as the training paradigm (precursor to VICReg / SIGReg / DINO-style training), and (4) behavior driven by **intrinsic costs + a learned critic**, not external reward.

Three central claims:

1. **Animals learn world models from observation** — the central capacity AI lacks. Children acquire object permanence, intuitive physics, etc. by ~6 months, mostly without intervention. The paper argues this is the path AI must take (Sections 2.1–2.2, Figure 1's "Dupoux chart" of infant concept acquisition).
2. **One configurable world model, not many task-specific models.** The paper hypothesizes a single world-model "engine" (likely prefrontal-cortex-analogue) dynamically configured by a **configurator module** for the current task. This enables reasoning by analogy and shared knowledge across tasks (Sections 2.2, 3, 6).
3. **Latent-space prediction (JEPA), not generative prediction.** Predicting at pixel level forces the model to "fill in" details that are intrinsically unpredictable. JEPA encodes both `x` and `y` into a representation space and predicts in that space — invariant to predictable-but-irrelevant details. Hierarchical JEPA (H-JEPA) stacks this across time scales (Sections 4.4–4.7).

The paper carries the JEPA *thesis* — every later JEPA paper instantiates a piece of this blueprint, often citing this document as the rationale.

## Abstract (verbatim)

> "How could machines learn as efficiently as humans and animals? How could machines learn to reason and plan? How could machines learn representations of percepts and action plans at multiple levels of abstraction, enabling them to reason, predict, and plan at multiple time horizons? This position paper proposes an architecture and training paradigms with which to construct autonomous intelligent agents. It combines concepts such as configurable predictive world model, behavior driven through intrinsic motivation, and hierarchical joint embedding architectures trained with self-supervised learning."

## The cognitive architecture (Section 3, Figure 2)

LeCun proposes a **six-module differentiable agent**. All modules are differentiable so gradients can flow end-to-end:

| Module | Role |
|---|---|
| **Perception** | Estimates current state of the world from sensors. |
| **World Model** | Predicts future world states given imagined action sequences. The configurable engine. |
| **Actor** | Proposes action sequences; optimizes them against the cost using the world model. |
| **Cost** | Scalar "energy"/discomfort. Two sub-modules: **intrinsic cost** (immutable, hard-wired — pain, pleasure, hunger) + **critic** (trainable, predicts future intrinsic cost — i.e. learned reward). |
| **Short-term memory** | Tracks current + predicted world states and costs. |
| **Configurator** | Top-level executive: configures all other modules for the task at hand. Inputs from every module. |

The architecture is biologically motivated but framed as an engineering proposal. LeCun explicitly notes that **emotions emerge naturally** as the anticipation-of-cost signal from the critic (Section 8.2.1).

### Two modes of operation (Section 3.1)

- **Mode-1 (reactive)**: a learned policy module `A(s)` outputs an action in one forward pass. Cheap, fast, no planning.
- **Mode-2 (deliberative)**: the actor unrolls the world model `T` steps into the future, optimizes the action sequence against accumulated cost using gradient-based search, and outputs the first action. Expensive, slow, but capable of planning under uncertainty.

The agent can **distill Mode-2 into Mode-1**: after solving a task by deliberation, train the policy `A(s)` to imitate the Mode-2 action sequence (amortized inference). This is how new skills become reactive (Figure 5, Section 3.1.3).

> [!note] This split is the LeCun-restatement of System-1/System-2 thinking (Kahneman), made architectural and gradient-compatible. It's directly inherited by V-JEPA 2's "model-predictive control with V-JEPA 2-AC" workflow.

## Self-supervised learning as energy-based modeling (Section 4)

LeCun reframes SSL through the lens of **Energy-Based Models (EBMs)**. A scalar function `F_w(x, y)` outputs low energy when `x` and `y` are compatible, high energy otherwise. This is the framework for *all* the architectures discussed in the paper.

Why EBMs over probability distributions? **Because many `y` may be compatible with a given `x`** (e.g. infinitely many video futures), and explicitly representing that distribution is intractable. EBMs sidestep the normalization problem entirely — the energy function is the fundamental object, not the log-density.

### Latent variables for multi-modality (Section 4.2, Figure 9)

To handle multiple compatible `y`, EBMs may use a **latent variable** `z`:
- `z` parameterizes the set of possible relationships between `x` and `y`.
- Inference: `z* = argmin_z E_w(x, y, z)`.
- Examples LeCun uses: camera displacement between two views; car turning left vs right at a fork; what a driver will do next.

In a temporal-prediction setting, `z` represents what cannot be predicted about the future from the past — captures the irreducible uncertainty.

### The collapse problem (Section 4.3, Figures 10–11)

The central technical challenge: without provisions, EBM training can produce a **collapsed energy landscape** — flat energy, the same low value everywhere. LeCun enumerates which architectures collapse and how:

| Architecture | Collapses? | Why |
|---|---|---|
| Deterministic prediction | No | Forced to produce single output. |
| Generative latent-variable | Yes (if `z` too rich) | Excess capacity in `z` lets it parameterize all `y`. |
| Auto-encoder | Yes | Can learn the identity function. |
| Joint-embedding (JEA) | Yes | Encoders can ignore inputs, output constants. |

Two families of fixes (Figure 11):
- **Contrastive methods** — push down on training-sample energy, push up on contrastive-sample energy. Disadvantage: number of contrastive samples scales exponentially with the dimension of `y`.
- **Regularized methods** — push down on training samples + a regularizer that minimizes the *volume* of low-energy regions. LeCun argues regularized methods scale better with dimension and will "in the long run" be preferred. **This is the bet underlying VICReg, BYOL, DINO, and SIGReg.**

## JEPA (Section 4.4, Figure 12)

The Joint-Embedding Predictive Architecture, as defined in this paper:

- Two encoders compute representations: `s_x = Enc(x)`, `s_y = Enc(y)` (often identical encoders).
- A **predictor** module predicts `s_y` from `s_x`, optionally with help of a latent `z`.
- The energy is the prediction error: `F(x, y) = D(s_y, Pred(s_x, z))`.

LeCun's stated advantages over generative architectures:

1. **Encoders can be invariant** to predictable-but-irrelevant details (the `s_y = Enc(y)` can collapse irrelevant variation, making energy constant over an equivalence class).
2. **Predictions in representation space** — no need to render every detail of `y`. Cheap, well-defined loss.
3. **Multi-modality via latent `z`** — varying `z` over a set `Z` produces a set of plausible predictions `Pred(s_x, Z)`.

The paper argues this is the architecture that fits the EBM framework *without* the collapse pathologies of generative latent-variable or auto-encoder approaches — *provided* the encoder doesn't itself collapse, which is handled by the non-contrastive regularizers.

### Why latent prediction over pixel prediction (Sections 4.4–4.5)

The key intuition (Section 4.5): a representation should capture **all and only the information predictable from the past**. Things like the position of leaves on a tree blowing in the wind are predictable in distribution but not in detail — a generative model is forced to predict them anyway, with blurry-mean failure modes. JEPA encoders can mark these as not represented, the predictor doesn't need to predict them, and the prediction can be sharp where the world is sharp.

> [!note] This is the technical heart of the "LeCun bet against generative video" frame popularized in the [Welch Labs explainer (2026-05-01)](welchlabs-lecun-1b-bet-against-llms.md) — which uses this exact pixel-blur argument as its visual centerpiece.

### Anti-collapse for JEPA (Sections 4.4–4.5)

LeCun proposes **VICReg** ([Bardes, Ponce, LeCun 2022](https://arxiv.org/abs/2105.04906)) as a JEPA-compatible non-contrastive regularizer with four criteria:

1. **Variance** — hinge loss enforcing per-component standard deviation above a threshold (anti-collapse).
2. **Covariance** — push pairwise covariances toward zero (decorrelate).
3. **Invariance** (representation prediction error) `D(s_y, ŝ_y)`.
4. (Optional) **Latent-information limiter** — regularize `z` to prevent the predictor from copying `z` straight onto its output.

This is the methodological lineage that runs **VICReg (2021) → DINO/DINOv2 → SIGReg (LeJEPA 2025)** — and every JEPA paper in this wiki sits somewhere along it.

## Hierarchical JEPA (Sections 4.6–4.7, Figures 15 and 17)

H-JEPA stacks JEPAs to achieve **multi-scale, multi-level prediction**:

- JEPA-1 predicts short-horizon, low-level representations.
- JEPA-2 predicts long-horizon, higher-level representations (built on JEPA-1's encoded states, possibly with temporal pooling).
- Higher levels coarse-grain — they ignore details that lower levels handle.

LeCun argues this is essential for **hierarchical planning**: a complex task decomposes into a high-level plan over abstract states, which becomes a lower-level plan over concrete states. The car-driving example: a route on a map (high-level, discrete) vs. steering-pedal trajectories (low-level, continuous).

Figure 17 shows H-JEPA used for **Mode-2 hierarchical planning under uncertainty**: latent variables at each level capture irreducible uncertainty, regularizers prevent collapse, and at planning time latents are sampled to produce diverse trajectories that the actor optimizes over.

> [!note] No JEPA paper in this wiki has yet *built* a working H-JEPA at the scale envisioned in this document. V-JEPA 2.1's "dense features" and JEPA-WMs' richer action-conditioned setup move in this direction, but a multi-time-scale H-JEPA system remains an open goal.

## The configurator (Section 6)

The least-developed module in the paper (LeCun explicitly says so). Its function: configure the other modules for the task at hand. Sub-functions:

- **Task identification** (what should the agent be doing right now?)
- **Goal setting** — feed the cost module a sub-objective relevant to the current task.
- **Mode-1 policy selection** — switch which reactive policy is active.
- **Predictor configuration** — set what the world model should focus on predicting.
- **Latent prior configuration** — set the regularizer hyperparameters for the prediction-time latents.

LeCun frames the configurator as the **central open problem** — the part of the architecture for which the paper does not propose a concrete instantiation.

## Intrinsic cost + trainable critic (Section 7)

The cost module that drives behavior is split:

- **Intrinsic cost** — immutable, hard-wired (the analogue of biological pain/pleasure/hunger/curiosity). Not learned, not modifiable by the agent. The agent's "values."
- **Critic** — trainable, predicts future intrinsic cost from the current state. This is the agent's learned reward function — playing the role of `V(s)` in classic RL but **derived from the intrinsic cost** rather than externally specified.

LeCun proposes **curiosity / exploration** as part of the intrinsic cost: reward states in which the world model's predictions are inexact. This is the standard intrinsic-motivation move (Schmidhuber et al.), built into the architecture from the start rather than retrofitted.

> [!note] LeCun calls out (Section 8.2.1) that machine emotions emerge inevitably from this architecture — they are the agent's anticipatory cost-prediction signal. He treats this as a feature, not a bug.

## Related-work positioning (Section 9, condensed)

The paper situates JEPA against:

- **Generative video prediction** (Babaeizadeh, Mathieu, Luc, etc.) — what JEPA is designed to replace. LeCun argues blurry-mean failure modes are intrinsic to pixel-MSE losses on multi-modal futures.
- **Contrastive SSL** (CPC, SimCLR, MoCo) — what regularized JEPA aims to obsolete via VICReg-style methods.
- **Model-based RL with world models** (Dreamer, PlaNet, Ha & Schmidhuber 2018) — closest existing relatives. LeCun cites Hafner et al.'s Director (2022) as the most architecturally similar published system to H-JEPA at the time.
- **Trajectory transformers** (Janner et al. 2021) — endorsed as a possible architecture for state-trajectory prediction inside the world model.
- **Common-sense AI critiques** (Marcus & Davis, Lake et al.) — LeCun positions JEPA as an answer to the long-standing critique that current AI lacks common sense (Section 8.2.2). LLMs are called out by name: "much of human common-sense knowledge is not represented in any text and results from our interaction with the physical world."

## Discussion / philosophical claims (Section 8)

A few stances LeCun stakes out that have aged into recurring talking points in his public-facing communication:

1. **LLMs are insufficient for common sense.** "Because LLMs have no direct experience with an underlying reality, the type of common-sense knowledge they exhibit is very shallow and can be disconnected from reality." (Section 8.2.2)
2. **No need for reinforcement learning at the foundation.** Self-supervised learning + intrinsic cost can in principle replace external reward signals for most of the agent's learning. RL is the icing, not the cake. (Echoes his "intelligence is a cake" slide; the present paper is its formalization.)
3. **No need for probabilistic modeling.** EBMs do not assume their energy is a log-density. This is LeCun's explicit rejection of the "everything is a probabilistic generative model" framing dominant in early-2020s ML.
4. **Architecture, not algorithm.** The paper repeatedly emphasizes that intelligence is a property of an *architecture* with the right modules wired together — not a single learning algorithm. This is what justifies the modular diagram in Figure 2.

## What's *not* in this paper

- **No experiments.** Position paper — zero benchmarks, no empirical claims. Every empirical claim about JEPA in the wiki traces to a *later* paper (V-JEPA 2, LeJEPA, etc.) that instantiated a piece of this vision.
- **No working configurator.** Section 6 is largely a sketch; no concrete proposal.
- **No working H-JEPA at multi-time-scale.** Section 4.7 describes the architecture; no implementation reported.
- **No proposal for the actor's exploration policy.** Section 5 leaves the search/exploration strategy open.
- **No proposal for robotic embodiment.** The paper is platform-agnostic; robotics is mentioned only as a downstream application.

These gaps define what the JEPA program has been *filling in* since 2022. The honest summary of the JEPA literature 2022–2026 is: "Yann said it should look like this; here is one piece of that working at one scale on one benchmark." [V-JEPA 2](v-jepa-2-paper.md) instantiates internet-scale video pretraining + action conditioning; [LeJEPA](lejepa-paper.md) instantiates a single-hyperparameter anti-collapse regularizer with proofs; [LeWorldModel](leworldmodel-paper.md) instantiates a stable end-to-end JEPA at robotics scale; etc.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — sole author.
- [Meta FAIR](../entities/meta-fair.md) — institutional affiliation at time of writing.
- Emmanuel Dupoux (developmental psycholinguist, cited for Figure 1 infant-concept chart).
- Frequent technical citations: Hafner et al. (Dreamer / Director), Schmidhuber (intrinsic motivation), Bardes / Ponce (VICReg), Hadsell & Chopra (contrastive learning), Janner (trajectory transformers).

## Concepts touched

- [Joint-Embedding Predictive Architecture (JEPA)](../concepts/jepa.md) — defined here, named here.
- [World model](../concepts/world-model.md) — the central object; the configurable engine.
- [Self-supervised learning](../concepts/jepa.md) (closely entwined with JEPA on this wiki).
- **Energy-based models (EBM)** — *concept page worth creating*; this paper is the canonical reference.
- **Hierarchical JEPA (H-JEPA)** — extension to multi-scale prediction; *concept page worth creating*.
- **Configurator** — proposed top-level executive module; no concept page yet.
- **Intrinsic motivation / intrinsic cost** — concept worth filing; central to LeCun's proposal.
- **Mode-1 vs Mode-2** — fast/slow / reactive/deliberative split (LeCun's restatement of Kahneman). No concept page yet.

## Open questions / TBD

1. **Has H-JEPA been built since 2022?** The wiki has many JEPA papers but no clearly identified *hierarchical* JEPA implementation at multi-time-scale. The closest may be V-JEPA 2.1's dense features. Worth checking literature.
2. **What is the current state of the configurator proposal?** LeCun has continued public talks since 2022; the "configurator" idea may have evolved. Open question whether any FAIR/AMI Labs paper has formalized it.
3. **AMI Labs as institutional successor.** Per the [Towards AI report on AMI Labs](towardsai-lecun-ami-labs.md), LeCun reportedly founded AMI Labs in late 2025 with a $1.03B seed round, after departing Meta. The mission statement aligns precisely with this paper's vision: build autonomous machine intelligence based on world models and self-supervised learning. **AMI Labs is, in effect, the institutional vehicle for executing on this paper.**
4. **How does LeCun's stance evolve with the [Welch Labs explainer (2026-05-01)](welchlabs-lecun-1b-bet-against-llms.md)?** The Welch Labs video covers blurry-pixel intuitions and Siamese networks — i.e. the pre-JEPA visual story. Open question whether LeCun's stated public position has materially changed from this 2022 document, or whether it's the same vision restated with four more years of evidence behind it.
