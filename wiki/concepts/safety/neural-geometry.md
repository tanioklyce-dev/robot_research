---
title: Neural geometry
type: concept
created: 2026-08-30
updated: 2026-08-30
sources: 2
tags: [neural-geometry, linear-representation-hypothesis, manifolds, multi-dimensional-features, sparse-autoencoders, mechanistic-interpretability, representation-structure]
---

**Neural geometry** is the study of the **shape** of a concept's representation inside a network — as opposed to the default assumption that concepts are *directions* in activation space.

The default is the **linear representation hypothesis (LRH)**, stated in two parts by [Engels et al.](../../sources/engels2024-not-all-features-one-dimensionally-linear.md): (1) representations lie along one-dimensional lines, and (2) model states are a sparse sum of those lines. Nearly all of modern [mechanistic interpretability](mechanistic-interpretability.md) practice assumes it — [SAEs](../../glossary.md#sae) decompose activations into directions, and feature steering adds or subtracts along one.

Neural geometry is the finding that **part (1) is not universally true**, and the research programme of characterizing what shapes concepts actually take.

## The evidence, in order of independence

**[Engels, Michaud, Liao, Gurnee & Tegmark (ICLR 2025)](../../sources/engels2024-not-all-features-one-dimensionally-linear.md)** — MIT, peer-reviewed, May 2024. Defines an **irreducible multi-dimensional feature** (one that cannot be split into independent or non-co-occurring lower-dimensional parts), searches for them automatically by clustering SAE dictionary elements, and finds **circular representations of days of the week, months, and years** in GPT-2 and Mistral 7B.

The causal result is the load-bearing one: patching **only the 2-D circular subspace** has "almost the same intervention effect as patching the entire layer" in early layers, and off-distribution `(r, θ)` sweeps *inside* the circle change the model's output coherently. The circle is a coordinate system the model reads, not a projection artifact.

**[Goodfire's *The World Inside Neural Networks*](../../sources/goodfire-research-index.md)** (Geiger et al., May 2026) — the broader and more aggressive claim: *"even when a model has learned a scalar concept like position, that concept may live on a **curved manifold** rather than along a straight line in activation space."* Demonstrated across language, vision, genomics, and — the part this wiki cares about — an **image-action model trained on mountain car**. Reported diagnostic: **linear steering along a curved concept produces garbled output and teleportation artifacts**; steering along the fitted manifold moves smoothly.

> [!note] On weighting these two
> Goodfire sells "neural geometry" as a named [Silico](../../sources/goodfire-silico-robotics-vision.md) capability, which is a reason to check rather than dismiss. The check exists and passes: the core claim is **independently established, at ICLR, 18 months earlier, by an academic group with no product**. Goodfire generalized it and built tooling around it.
>
> The two lines are **connected, not independent** — Eric Michaud co-authored the MIT paper and his later feature-manifold work appears in Goodfire's corpus. Treat Goodfire's version as an extension of a real academic finding, not as corroboration of it.

## What is actually claimed, and what is not

**Claimed and supported**: some concepts are irreducibly multi-dimensional; where they are, the multi-dimensional structure is causally load-bearing; linear interventions on those concepts behave badly in a specific, diagnosable way.

**Not established**: that most features are non-linear. Engels et al. are explicit — *"we are unsure if we are failing to interpret some of the high-scoring multi-dimensional features, if most multi-dimensional features lie in dimensions higher than two, if our clustering technique is not powerful enough, or if there are truly not that many."* Their irreducibility measures are **statistical, not intervention-based**, and were relaxed to work in practice.

So: **the LRH is not universally true. It may still be usually true.** That distinction is the whole current state of the question.

## Why it matters for interpretability tooling

If a concept is curved and you model it as a direction, three things go wrong:

1. **Steering breaks in a characteristic way** — you leave the manifold and land somewhere the model does not represent, producing incoherent output rather than a graded change. This is a *testable signature*, which is what makes the claim useful rather than merely deflationary.
2. **SAE features become a linear approximation to a curved object** — locally fine, globally wrong, and the residual is invisible in reconstruction loss.
3. **It supplies a candidate account of Olah's "dark matter."** The wiki's [mech-interp page](mechanistic-interpretability.md) records his estimate that ~1% of concepts have been extracted. One reading is that the missing ones are *not shaped like directions* — a coverage problem caused by the wrong hypothesis class rather than by insufficient scale.

## The robotics version, which nobody has run

Every result above is language, vision, or genomics. The robotics question is sharper and is untested:

**Does a robot policy's latent encode a continuous physical quantity — object x-position, gripper aperture, distance-to-contact — as a smooth manifold, or as a set of discrete per-demonstration clusters?**

That is arguably the cleanest available operationalization of "did the policy generalize or memorize," and it bears directly on the wiki's largest open evaluation problem: [LIBERO-PRO](../../sources/libero-pro-paper.md) showed policies scoring **>90%** collapsing to **0.0%** under perturbation, with no way to tell in advance which would. A policy whose latent fragments a continuous variable into demonstration-shaped clusters has, by construction, no interpolation capacity between them.

The nearest existing datum is Goodfire's **mountain-car image-action model**, where position was found on a 1-D manifold — a toy environment, a 2-state system, one lab. See [the proposed experiment](../../syntheses/projects/latent-inspection-policy-collapse.md).

## Related concepts

- [Mechanistic interpretability](mechanistic-interpretability.md) — the field whose default assumption this qualifies.
- [Distributed representations](../learning/distributed-representations.md) — the same question one level up: the geometry of an embedding space is learned, not specified, and this is what that geometry turns out to look like.
- [Latent space](../world-models/latent-space.md) — the object being characterized.
- [Inductive bias](../learning/inductive-bias.md) — "features are directions" is itself an inductive bias, imposed by the analyst rather than the model.

## Key references

- **[Engels et al. 2024/2025](../../sources/engels2024-not-all-features-one-dimensionally-linear.md)** — the independent, peer-reviewed foundation.
- **[Goodfire research index](../../sources/goodfire-research-index.md)** — *The World Inside Neural Networks* and the associated corpus (*Can SAEs Capture Neural Geometry?*, *Steering Along Manifolds*, *Meandering on Manifolds*, *Uncovering Neural Geometry in Vision Models*).
- **Un-ingested and wanted**: Michaud et al. 2025, *Understanding Sparse Autoencoder Scaling in the Presence of Feature Manifolds*; Park et al. on the LRH itself; *The Origins of Representation Manifolds in Large Language Models* (arXiv 2505.18235).

## Current state (2026-08)

An active and unsettled question with one solid peer-reviewed result, one well-funded commercial research programme extending it, and no consensus on prevalence. Tooling has moved faster than the evidence: "neural geometry" is already a shipped product feature while the field cannot yet say what fraction of concepts are non-linear.

**Nothing in robotics.** The concept is imported here on the strength of one toy RL example.

## Mentioned in

- [Engels et al. — Not All Language Model Features Are One-Dimensionally Linear](../../sources/engels2024-not-all-features-one-dimensionally-linear.md)
- [Goodfire research index](../../sources/goodfire-research-index.md)
- [Silico for Robotics & Vision](../../sources/goodfire-silico-robotics-vision.md)
- [Goodfire Series B](../../sources/goodfire-series-b.md)

## Open questions / TBD

- **Prevalence.** What fraction of features are irreducibly multi-dimensional? Unanswered by everyone.
- **Does it hold for action representations?** See [the proposed experiment](../../syntheses/projects/latent-inspection-policy-collapse.md).
- **Is there a cheap detector?** Both papers find geometry by expensive search. A metric computable in one pass over a validation set would make this deployable rather than a research activity.
- **Higher dimensions.** Both lines find 1-D and 2-D structure and speculate about more; nothing systematic exists above 2-D.
