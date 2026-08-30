---
title: Mechanistic interpretability
type: concept
created: 2026-05-15
updated: 2026-08-30
sources: 8
tags: [mechanistic-interpretability, anthropic, goodfire, neural-geometry, robotics, chris-olah, sparse-autoencoders, feature-extraction, ai-safety]
---

**Mechanistic interpretability** — the research program of *reading and intervening on the internal computations of trained neural networks*, in the hope of understanding what concepts a model represents and how it uses them to produce behavior. The intellectual descendant of neural-network "circuits" work pioneered by **Chris Olah** and collaborators. Distinct from input-output interpretability (e.g., LIME, attention heatmaps) in that it targets the model's *intermediate representations* directly.

## Definition

Given a trained model `f_θ`, mechanistic interpretability asks:

1. **Feature extraction**: what concepts are represented in `f_θ`'s internal activations? Modern best-practice technique is **sparse autoencoders (SAEs)** — a separate learning algorithm that trains a wider, sparser representation `z = SAE(activation)` such that each `z_i` often corresponds to a human-understandable concept.
2. **Feature steering**: once a feature is extracted, can you *increase or decrease* its strength in `f_θ` and observe a corresponding change in behavior? This is the operational test for whether a feature is causally relevant, not just statistically present.
3. **Circuit discovery**: how do features combine through the model's layers to produce the model's outputs? This is the *mechanistic* part — finding the actual circuits.

## Key references in this wiki
- **[Welch Labs Illustrated Guide to AI, Vol I — Ch 7](../../sources/welchlabs-illustrated-guide-to-ai.md)** (Stephen Welch, 2026) — pedagogical hub for the field. Anchors on Anthropic's Templeton et al. 2024 sparse-autoencoder work and Chris Olah's "dark matter of interpretability" framing.
- **Anthropic's [Claude](../../entities/anthropic.md)** is the canonical demonstration system in modern mech-interp work — Welch's Ch 7 walks through the "ask Claude to forget a phrase; then increase the internal-conflict feature and watch it admit it can't" demonstration as the field's archetypal feature-steering result.

## Core findings (per Welch Ch 7)
- **Sparse autoencoders extract human-meaningful features.** Templeton et al. 2024 (Anthropic) — "Scaling Monosemanticity" — demonstrated this at scale on Claude. Features for "cats," "dogs," "WiFi networks," up to abstract concepts like "internal conflict."
- **Features can be steered.** Boosting a feature's value in the live model produces qualitatively predictable behavioral changes. This is the most direct evidence that the extracted features are causally part of how the model produces behavior, not just descriptive correlates.
- **We're still in the early innings.** Olah's "dark matter" framing (quoted in Welch Ch 7): *"the features we haven't been able to extract may be a kind of dark matter of interpretability"* — i.e., **we've extracted <1% of the concepts** large language models must know about. The known features are like the brightest stars; everything dimmer is invisible.

> [!warning] The linear-representation assumption is now contested
> The account above — features as *directions* in activation space, extracted by SAEs, validated by turning them up and down — is the **linear representation hypothesis**, and as of 2026 it is disputed rather than settled.
>
> [Goodfire](../../entities/goodfire.md)'s *The World Inside Neural Networks* (Geiger et al., May 2026, [catalog record](../../sources/goodfire-research-index.md)): *"Neural networks often do not represent the world as a set of clean, linear directions. Even when a model has learned a scalar concept like position, that concept may live on a **curved manifold** rather than along a straight line in activation space."* They report a concrete failure signature — steering **linearly** along a curved concept produces garbled outputs and teleportation artifacts, while steering **along the fitted manifold** moves smoothly.
>
> If that holds, SAE features are a **linear approximation to a curved object**, which is one candidate account of Olah's "dark matter": not concepts we failed to find, but concepts that are not shaped like directions.
>
> **Independently corroborated.** [Engels, Michaud, Liao, Gurnee & Tegmark](../../sources/engels2024-not-all-features-one-dimensionally-linear.md) (MIT, **ICLR 2025**, arXiv May 2024 — 18 months before Goodfire's post, and product-free) define **irreducible multi-dimensional features**, find **circular** representations of days of the week and months of the year in GPT-2 and Mistral 7B by clustering SAE dictionary elements, and show causally that patching **only the 2-D circular subspace** has "almost the same intervention effect as patching the entire layer."
>
> **What is established**: some concepts are irreducibly multi-dimensional, and where they are the geometry is causally load-bearing. **What is not**: how common that is — Engels et al. explicitly cannot say. So the section above is **not universally true, and may still be usually true.** See [neural geometry](neural-geometry.md).

## The field now has a commercial pole

Until 2026 this page described mech-interp as a frontier-lab safety programme. [Goodfire](../../entities/goodfire.md) — a **$150M Series B at a $1.25B valuation** ([announcement](../../sources/goodfire-series-b.md)), founded by DeepMind and OpenAI interpretability alumni — sells it as **tooling**, through an agent product ([Silico](../../sources/goodfire-silico-robotics-vision.md)) that runs interpretability experiments autonomously.

Two things follow that matter beyond the funding:

- **The pitch is not primarily defensive.** Alongside safety, Goodfire argues interpretability is a **model-design** instrument and a **scientific-discovery** one — extracting from a genomics or echocardiography model what it knows and nobody has written down. That is a different justification from "know when the model is lying," and it is the one attracting customers (Arc Institute, Mayo Clinic, Rakuten, Microsoft).
- **Robotics is a named vertical.** See below.

## Interpretability applied to robot policies

The wiki's robotics material has a standing problem with no method attached: [LIBERO-PRO](../../sources/libero-pro-paper.md) showed policies scoring **>90%** collapsing to **0.0%** under perturbation, which establishes that benchmark success does not distinguish generalization from memorization — and offers no way to tell them apart short of building a perturbed benchmark for every task.

Reading the policy's **internals** is one of the few proposals anywhere for doing that directly. [Goodfire's robotics & vision page](../../sources/goodfire-silico-robotics-vision.md) frames it as: *"Vision and robotics models often fail in the real world because they learned brittle shortcuts instead of generalizable concepts"* — and claims to catch generalization failure pre-deployment by evaluating the latent space, to attribute a failure back to the training episodes that caused it, and to steer between latent modes without retraining.

> [!warning] Framing only — nothing here is evidence
> The robotics case study **names no model, reports no benchmark, and gives no numbers**, and Goodfire's 40-item [research corpus](../../sources/goodfire-research-index.md) contains **no robotics research at all**. The closest published thing is an image-action model on the toy mountain-car environment. Cite this as an approach being attempted, never as one shown to work.

The nearest testable version: **does latent-space inspection predict which policies collapse under [LIBERO-PRO](../../sources/libero-pro-paper.md)-style perturbation, before running the perturbed benchmark?** Nobody has published it. A runnable design — open checkpoints, one GPU, no robot — is now filed at [latent-inspection-policy-collapse](../../syntheses/projects/latent-inspection-policy-collapse.md).

## Why this matters in this wiki

- **Adjacent to [AI safety and alignment](ai-safety-alignment.md)**. The standard safety pitch for mech-interp is "if we understood the model, we could trust it (or distrust it for the right reasons)." Welch frames this as "how would you know if a language model is lying to you?" Anthropic's [Claude](../../entities/anthropic.md) is both the safety-research target and the operational system being interpreted.
- **Adjacent to [Chain of thought](../learning/chain-of-thought.md)**. CoT faithfulness depends on whether the model's verbalized reasoning matches its actual internal computation — a question mech-interp is in principle positioned to answer. As of 2026 it can't yet.
- **Adjacent to [Corrigibility](corrigibility.md)**. The "feature for being corrigible" is the kind of internal concept mech-interp would need to identify and reason about. Currently aspirational.

## Current state (2026-08)
- **Sparse autoencoders are state-of-the-art** as of Templeton et al. 2024. Multiple labs (Anthropic, Google DeepMind, OpenAI internal) have replicated.
- **Scaling**: SAEs themselves now have to be trained at scale — extracting features from a frontier-scale LLM means training an SAE that's a substantial model in its own right.
- **Olah's pessimism on coverage**: ~1% of concepts extracted as of mid-2024. Welch quotes this as the chapter's anchor caveat — the field is real, the techniques work, the coverage problem is brutal.
- **No dedicated pedagogy primary-source in the wiki besides Welch Ch 7.** Templeton et al. 2024 (Scaling Monosemanticity) is the canonical Anthropic paper but is not yet in `raw/`.
- **The linear hypothesis is under active, peer-reviewed challenge** ([Engels et al., ICLR 2025](../../sources/engels2024-not-all-features-one-dimensionally-linear.md)) — not universally true, prevalence unknown. See [neural geometry](neural-geometry.md).
- **Commercialized as of 2026.** Interpretability is now sold as tooling, with life sciences the proven vertical and **robotics an announced but unevidenced one**.

## Related
- [Neural geometry](neural-geometry.md) — the challenge to the linear framing above.
- [Goodfire](../../entities/goodfire.md) — the field's commercial pole; [Silico](../../sources/goodfire-silico-robotics-vision.md).
- [Proposed experiment: latent inspection vs policy collapse](../../syntheses/projects/latent-inspection-policy-collapse.md).
- [LIBERO-PRO](../../sources/libero-pro-paper.md) — the robot-evaluation problem interpretability is being proposed against.
- [Inductive bias](../learning/inductive-bias.md) — Goodfire's *Priors in Time* frames interpretability's own missing inductive biases.
- [AI safety and alignment](ai-safety-alignment.md) — mech-interp's primary motivating sponsor.
- [Anthropic](../../entities/anthropic.md) — the lab that drives the modern SAE-based program.
- [Chain of thought](../learning/chain-of-thought.md) — adjacent: CoT faithfulness is a mech-interp-shaped question.

## Mentioned in
- [Welch Labs Illustrated Guide to AI, Vol I](../../sources/welchlabs-illustrated-guide-to-ai.md)
- [Silico for Robotics & Vision (Goodfire)](../../sources/goodfire-silico-robotics-vision.md)
- [Goodfire research index (2024–2026)](../../sources/goodfire-research-index.md)
- [Goodfire Series B announcement](../../sources/goodfire-series-b.md)
- [Engels et al. — Not All Language Model Features Are One-Dimensionally Linear](../../sources/engels2024-not-all-features-one-dimensionally-linear.md)

## Open follow-ups
- **Templeton et al. 2024 — *Scaling Monosemanticity*** (Anthropic). Primary-source candidate. Would let this concept page cite specific feature-extraction numbers, model scales, and demonstrations.
- **Olah's "dark matter of interpretability"** essay/talk (July 2024). Primary-source candidate; would let the page cite the framing directly.
- **Chris Olah** entity stub — would tie together the SAE / circuits lineage at Anthropic + earlier Distill / OpenAI work.
- **Sparse autoencoder** concept page — the technique deserves its own page if the field gets deeper coverage. Currently rolled into this concept, and now also needs to carry the manifold critique.
- **Ingest *The World Inside Neural Networks*** (Geiger et al. 2026) and *Can SAEs Capture Neural Geometry?* (Bhalla et al. 2026) as full sources. Together they decide whether the linear framing above needs rewriting rather than caveating.
- ~~EchoJEPA — surfaced only via Goodfire's case study.~~ **Resolved 2026-08-30** — [ingested](../../sources/echojepa-paper.md); the claimed ECG-leakage finding is **not in the paper**, so it remains unverified.
- **Goodfire's evaluation-awareness thread** (*Verbalized Eval Awareness Inflates Measured Safety*; *Reasoning Theater*) is the closest thing in that corpus to this wiki's robot-evaluation problem, approached from language.
