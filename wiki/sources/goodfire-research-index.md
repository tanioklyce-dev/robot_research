---
title: "Goodfire research index (Sept 2024 – Aug 2026)"
type: source
url: https://www.goodfire.com/research
author: Goodfire (various; see per-item authors)
published: rolling; index fetched 2026-08-30
ingested: 2026-08-30
format: research index page
tags: [goodfire, interpretability, mechanistic-interpretability, sparse-autoencoders, neural-geometry, research-landscape, corpus-record]
---

> [!note] What this page is
> A **catalog record** of [Goodfire](../entities/goodfire.md)'s published research output — 40 items over two years — not an ingest of the research itself. Only one item ([The World Inside Neural Networks](#the-world-inside-neural-networks-may-2026)) has been read. This exists so the wiki knows what is available before deciding what to ingest properly.
>
> Extraction via WebFetch (small-model summarization of the index page). Titles, dates and author surnames are as returned; **individual items should be fetched directly before being cited**.

## Shape of the corpus

Goodfire tags its own output in two categories, and the split is the most informative thing about the company:

- **Fundamental Research** — the mechanistic-interpretability research programme proper: neural geometry, SAE limitations, parameter decomposition, memorization, superposition.
- **Applied Research** — interpretability pointed at a customer's problem: genomics, Alzheimer's biomarkers, materials discovery, PII detection, hallucination reduction, evaluation awareness.

Roughly half and half, over ~40 items from September 2024 to August 2026. A meaningful number are marked "Link post" — pointers to work published elsewhere (arXiv, LessWrong) rather than original site content.

**This is a real research output, not a blog.** Whatever one makes of the [product claims](goodfire-silico-robotics-vision.md), the volume and the named collaborations (Arc Institute, Rakuten, Mayo Clinic) are not marketing artifacts.

## The item worth reading first

### The World Inside Neural Networks (May 2026)

Geiger, Lubana, Fel, Merullo, Byun, Lewis & McGrath. **The one item read for this ingest**, and the one that matters most to this wiki — because it is a **challenge to the assumption the wiki's [mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) page currently presents as settled.**

The central claim, verbatim:

> "Neural networks often do not represent the world as a set of clean, linear directions. Even when a model has learned a scalar concept like position, that concept may live on a **curved manifold** rather than along a straight line in activation space."

Method: unsupervised discovery of curved manifolds in activation space, then intervention experiments steering representations *along* those manifolds, compared against linear steering vectors and SAEs.

Models studied span an **image-action model trained on the mountain-car RL environment**, language models (numbers, days, months, character sequences), vision models (spatial arrangement, hue/saturation/lightness), and genomic/epigenomic models.

The reported result on mountain car: steering along a fitted **one-dimensional manifold** produced smooth, coherent position changes, while **linear** paths produced garbled outputs and teleportation artifacts.

> [!warning] This cuts against the wiki's current account of the field
> [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) here describes SAEs as "modern best-practice technique" and feature steering as the operational test of causal relevance — the **linear representation hypothesis**, that concepts live along directions in activation space and can be turned up or down.
>
> This work says that assumption is often wrong, and produces a concrete failure signature when it is: **linear steering along a curved concept teleports rather than moves.** If it holds, SAE-extracted features are a linear approximation to a curved object, which would be one plausible account of Olah's "dark matter" — not features we failed to find, but features that are not shaped like directions.
>
> Flagged rather than adopted: this is **one lab's line of work, self-published, and Goodfire has a commercial interest** in "neural geometry" being a distinct capability, since it is a named Silico feature. It should be checked against the SAE literature before the wiki treats the linear hypothesis as superseded. See also the corpus's own **"Can SAEs Capture Neural Geometry?"** (Bhalla et al., May 2026) and **"Understanding Sparse Autoencoder Scaling in the Presence of Feature Manifolds"** (Michaud et al., Sept 2025).

The **mountain-car image-action model** is the direct robotics hook: a policy mapping observations to actions, with a scalar physical concept (position) shown to live on a manifold. That is the smallest possible version of the question the wiki cares about — *what do robot policies actually represent* — and it is answered here on a toy environment.

## The rest of the corpus, by thread

Grouped for orientation; **all un-ingested**.

**Neural geometry** (the house line) — *Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers* (Fel et al., Jul 2026); *Meandering on Manifolds: The Neural Geometry of Stories Over Time* (Bigelow et al., Jun 2026); *Can SAEs Capture Neural Geometry?* (Bhalla et al., May 2026); *Steering Along Manifolds to Control Neural Networks* (Wurgaft et al., May 2026); *A Geometric Calculator Inside a Neural Network* (Feucht et al., May 2026); *Covariance-based Sequence Pooling* (Dooms et al., Apr 2026).

**SAEs, parameters and mechanisms** — *Interpreting Language Model Parameters* + summary (Bushnaq et al., May 2026); *Towards Scalable Parameter Decomposition* (Bushnaq et al., Jun 2025); *Understanding Memorization via Loss Curvature* (Merullo et al., Nov 2025); *Adversarial Examples Are Not Bugs, They Are Superposition* (Gorton & Lewis, Aug 2025); *Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context* (Gur-Arieh et al., Oct 2025); *Replicating Circuit Tracing for a Simple Known Mechanism* (Loeffler et al., Jun 2025); *The Circuits Research Landscape* (Lindsey et al., Aug 2025); *Open Problems in Mechanistic Interpretability* (Sharkey et al., Jan 2025).

**Evaluation awareness and safety** — *Logits as a new monitor for evaluation awareness* (Aranguri, Jun 2026); *Verbalized Eval Awareness Inflates Measured Safety* (Aranguri & Bloom, May 2026); *Reasoning Theater: Probing for Performative Chain-of-Thought* (Boppana et al., Mar 2026); *Discovering Undesired Rare Behaviors via Model Diff Amplification* (Aranguri & McGrath, Aug 2025); *Predicting Rare LLM Failures with 30× Fewer Rollouts* (Aranguri & Pernice, May 2026); *Probe-Based Data Attribution* (Xiao & Aranguri, Apr 2026); *Features as Rewards: Using Interpretability to Reduce Hallucinations* (Prasad et al., Feb 2026).

> [!note] The evaluation-awareness thread is the one most transferable to robotics
> *Verbalized Eval Awareness Inflates Measured Safety* and *Reasoning Theater* are about models behaving differently when they can tell they are being tested, and about verbalized reasoning that does not match internal computation. Both are direct analogues of problems the wiki has in the robot-evaluation thread — [LIBERO-PRO](libero-pro-paper.md)'s memorization finding, the [VLA success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), and [chain-of-thought](../concepts/learning/chain-of-thought.md) faithfulness in reasoning VLAs. **A robot policy cannot verbalize, but it can absolutely have learned the benchmark.**

**Life sciences / applied** — *Explaining 4.2 million genetic variants* (Pearce et al., Apr 2026); *Using Interpretability to Identify a Novel Class of Alzheimer's Biomarkers* (Wang et al., Jan 2026); *Finding the Tree of Life in Evo 2* (Pearce et al., Aug 2025); *Interpreting Evo 2* (Gorton et al., Feb 2025); *Using Self-Correcting Search to Accelerate Materials Discovery* (Hazra et al., Apr 2026); *Deploying Interpretability to Production with Rakuten: SAE Probes for PII Detection* (Nguyen et al., Oct 2025).

**Data and training** — *Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train* (Bergen et al., Jun 2026); *Why Larger Models Learn More* (Huang et al., Jun 2026); *Priors in Time: Missing Inductive Biases for Language Model Interpretability* (Lubana et al., Nov 2025); *Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering* (Bigelow et al., Nov 2025).

**Earlier / foundational to the company** — *Mapping the Latent Space of Llama 3.3 70B* (McGrath et al., Dec 2024); *Understanding and Steering Llama 3 with Sparse Autoencoders* (McGrath et al., Sept 2024); *Painting With Concepts Using Diffusion Model Latents* (Cammarata et al., May 2025); *Under the Hood of a Reasoning Model* (Hazra et al., Apr 2025); *Forking Fast* (Bigelow et al., Aug 2026).

## Entities mentioned

- **[Goodfire](../entities/goodfire.md)** — publisher.
- Arc Institute, Rakuten, Mayo Clinic — named research collaborators.
- Recurring authors: Tom McGrath, Thomas Fel, Santiago Aranguri, Eric Bigelow, Lucius Bushnaq, Jack Merullo, Nick Cammarata, Leon Bergen, Ekdeep Singh Lubana, Atticus Geiger.

## Concepts touched

- **[Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md)** — the whole corpus.
- **[Inductive bias](../concepts/learning/inductive-bias.md)** — *Priors in Time* is explicitly about missing inductive biases for interpretability.
- **[Chain-of-thought](../concepts/learning/chain-of-thought.md)** — *Reasoning Theater* probes CoT faithfulness.
- **[World models](../concepts/world-models/world-model.md)** — *The World Inside Neural Networks* uses "world model" narrowly, as next-frame prediction given state and action.

## Open questions / TBD

- **Priority ingest: *The World Inside Neural Networks*** as a full source page, and *Can SAEs Capture Neural Geometry?* alongside it. Together they would settle whether the wiki's mech-interp page needs its linear-features framing revised.
- **Second priority: the evaluation-awareness pair** — the closest thing in this corpus to the wiki's robot-evaluation problem, from a completely different direction.
- **Is "neural geometry" a real finding or a product category?** Goodfire sells it as a named Silico capability, which is a reason for care, not dismissal — but the wiki should read the independent SAE-manifold literature (Michaud et al. is a "Link post," so likely published elsewhere) rather than only Goodfire's account of it.
- **No robotics research in the corpus.** Robotics is a named Silico *vertical* with a marketing [case study](goodfire-silico-robotics-vision.md), and there is **no published robotics research** in 40 items. The mountain-car image-action model in *The World Inside Neural Networks* is the closest thing, and it is a toy.
