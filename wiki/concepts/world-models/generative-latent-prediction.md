---
title: Generative Latent Prediction (GLP)
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 3
tags: [world-model, glp, generative-latent-prediction, jepa, decoder, generative-loss, latent-loss, stateful, discrete-tokens, position]
---

**Generative Latent Prediction (GLP)** — a world-model architecture class proposed by [Xing, Deng & Hou](../../sources/critique-of-world-model-paper.md) as the explicit alternative to [JEPA](jepa.md): keep JEPA's *next-latent prediction* as the reasoning substrate, but **close the loop with a decoder** so that the predicted latent is supervised by, and can be checked against, the next observation. In their formula, JEPA is `ŝ′ = f(h(o), a)` supervised by `‖ŝ′ − h(o′)‖`; GLP adds `g` and supervises `‖g(ŝ′) − o′‖`. The term dates from mid-2025 and the wiki has one primary for it, so this page is a statement of a *position*, not a survey of a field.

## The three claims

1. **Statefulness.** A representation that can be re-identified and carried forward in memory is a precondition for simulation over long horizons; a fixed-size embedding of a raw sensory stream is not one, because it moves with nuisance factors rather than with the world. GLP therefore favours a **mixed** state: discrete vocabulary tokens as the stable backbone, continuous embeddings for perceptual nuance. (This is the [belief-state](belief-states-and-mixed-states.md) requirement, with a claim about which carrier satisfies it.)
2. **The decoder is a diagnostic, not a renderer.** A lossy, non-invertible encoder can discard what the dynamics need, and nothing inside latent space can tell you. If `g` cannot reconstruct `o′` from the predicted `ŝ′`, the encoder was too lossy. The sharp corollary: a semantic encoder abstracts away whatever was rare in training — and rare events are where predictions carry the highest stakes.
3. **Latent loss is a loose surrogate.** Proposition 1: the bare latent loss has a trivial constant-encoder optimum. Theorem 2: under isotropic-Gaussian assumptions, `L_latent ≤ L_gen + ε`, so minimising the latent loss does not bound the observation error. *"Not that world models must operate in pixel space, but that they should learn from it."*

Plus a usage claim: use the world model to **train a policy by RL on simulated experience** rather than to plan by MPC at every step.

## Where it is right, where it is contested

- **Right, and already in the wiki under other names.** The rare-event argument is the [OOD-collapse measurement](../../syntheses/world-models/generative-video-vs-jepa-world-models.md#a-third-jepa-failure-mode-measured-may-2026-out-of-distribution-collapse) as a mechanism, and the [abstraction tax](../../syntheses/world-models/abstraction-tax.md) as a cost. "JEPA is functionally autoregressive and deterministic" matches what the [WorldDP close read](../../sources/worlddp-paper.md#reading-notes) found in one model.
- **Contested by a theorem pointing the other way.** [Van Assel et al.](../../sources/joint-embedding-vs-reconstruction-paper.md) prove reconstruction is *worse* for the downstream target when nuisance noise is high-dimensional, because it is forced to spend capacity on it. Theorem 2 weights every pixel equally and is silent on which residuals matter. The two results do not contradict; they disagree about what counts as a mistake.
- **Proposition 1 is a strawman.** Every anti-collapse mechanism in the [lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md) exists because of it; the live question is heuristic vs principled, which [SIGReg](sigreg.md) addresses and the essay does not engage.
- **Proposition 2 does not cover posterior collapse.** A generative loss with a decoder that ignores the latent is the standard [VAE](../learning/variational-autoencoder.md) failure. "Reconstruction cannot collapse" is true of the reconstruction, not of the state.
- **Statefulness-via-tokens is an existence result.** Theorem 1 says a quantisation code fine enough to separate any two inputs exists and that longer codes are cheaper than bigger vocabularies. It says nothing about learnability or stability of such a code.

## Instances

- [PAN](../../entities/pan-world-model.md) — the named instantiation, now read from its [technical report](../../sources/pan-world-model-paper.md). **It implements the encoder–backbone–decoder shape and the generative loss, and none of the three claims above**: the state is 256 *continuous* VLM tokens, the encoder is *frozen* (so the decoder diagnoses nothing), and usage is per-step planning with an external VLM rather than RL on simulated experience. Best open-source on its own benchmark; +23–27 pts for an o3 planner.
- In spirit, the generative-video side of the wiki's [paradigm comparison](../../syntheses/world-models/generative-video-vs-jepa-world-models.md): [Cosmos 3](../../sources/cosmos-3-technical-report.md), [Genie 3](../../entities/genie-3.md) — GLP claims to inherit their *validation* while adding JEPA's *abstraction*.
- The hybrid the wiki already tracks under [a third position](../../syntheses/world-models/generative-video-vs-jepa-world-models.md#a-third-position-fix-the-representation-inside-the-generative-objective) — fixing the representation *inside* a generative objective — is the same bet made from the generative side.

## Related concepts

- [JEPA](jepa.md) — the position GLP is written against.
- [World model](world-model.md) — the definition fight ("simulator, not renderer").
- [Belief states and mixed states](belief-states-and-mixed-states.md) — "stateful" formalised.
- [Identifiability](identifiability.md) — the essay's claim that latents of real signals are intrinsically unidentifiable.
- [World-model functional taxonomy](world-model-functional-taxonomy.md) — the same *simulator* cut from [Fei-Fei Li](../../entities/fei-fei-li.md)'s side.

## Key references

- [Critique of World Model](../../sources/critique-of-world-model-paper.md) — the position.
- [PAN technical report](../../sources/pan-world-model-paper.md) — the built instance.
- [LeCun & Xing debate](../../sources/lecun-xing-jepa-glp-debate-2026.md) — the position argued live; the crux narrows to *where prediction is checked*, and Xing concedes GLP with reconstruction weight zero *is* JEPA.

## Current state

One position paper, one results paper that builds less than the position asked for, one debate in which the position softens. The wiki's head-to-head evidence ([mid-2026](../../syntheses/world-models/generative-video-vs-jepa-world-models.md#the-first-head-to-head-measurements-mid-2026)) says latent prediction wins on representation quality *by less than its advocates claim*, which leaves room for GLP's argument without confirming it.

## Mentioned in

- [Critique of World Model](../../sources/critique-of-world-model-paper.md)
- [PAN technical report](../../sources/pan-world-model-paper.md) — the architecture as actually built.
- [LeCun & Xing debate (2026)](../../sources/lecun-xing-jepa-glp-debate-2026.md) — the position argued live against LeCun.
