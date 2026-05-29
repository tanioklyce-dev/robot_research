---
title: Three thinking styles (computational, inferential, economic)
type: concept
created: 2026-05-29
updated: 2026-05-29
sources: 1
tags: [economics-of-ml, mechanism-design, inference, computational-thinking, michael-jordan, system-design]
---

**Three thinking styles** — [Michael I. Jordan](../../entities/michael-i-jordan.md)'s organizing framework for designing real-world ML systems ([Jordan 2025](../../sources/jordan-collectivist-economic-ai.md)). The claim: algorithm design draws on three distinct, decades-matured **styles of thinking**, and emerging AI systems require the **tripartite blend** of all three — not any single style and not "just more data and compute."

## The three styles

| Style | Field of origin | Algorithms called | Core source of uncertainty it handles | Solution concept |
|---|---|---|---|---|
| **Computational thinking** | Computer science (Wing 2006) | "algorithms" | data **provenance** (when/where/who of collection) | modularity, abstraction, scaling |
| **Inferential thinking** | Statistics | "procedures" | **sampling** — data is a subset of all useful data | generative models, causal "what-if", uncertainty quantification |
| **Economic thinking** | Economics | "mechanisms" | **information asymmetry** between strategic agents (does *not* shrink with sample size) | **equilibria, not optima** |

Key insight: these are styles of *thinking behind* algorithms, not three disjoint algorithm sets — "focusing solely on 'computation' misses the point." Each can be embodied in a computational device, which is what gives them new power.

## Why the blend is needed
Computational thinking was developed for systems with **limited, carefully-designed interaction with the outside world**. The real world adds two things it was never designed for ([Jordan 2025](../../sources/jordan-collectivist-economic-ai.md)):
1. **Vast complexity and partial observability** → coping with uncertainty becomes central (inferential thinking).
2. **Strategic agents** acting in social environments → incentives and equilibria matter (economic thinking).

Jordan's Figure 1: the **pairwise** blends already exist as academic disciplines — but each uses only two ingredients and so addresses only part of the problem in systems of people + machines + data. The missing piece is the **tripartite** blend.

Worked instances of blends in [Jordan 2025](../../sources/jordan-collectivist-economic-ai.md):
- *Computation + Inference* → inferential database design (population vs sample, post-hoc assumption checks, causal inference).
- *Inference + Economics* → [statistical contract theory](mechanism-design.md): e-values ⟺ incentive-compatible contracts (Bates et al. 2024).
- *All three* → [multi-way / multi-layer markets](collectivist-ai.md) and [prediction-powered inference](prediction-powered-inference.md).

## The "no Maxwell's equations" caveat
Jordan argues AI is not yet a mature engineering discipline: chemical and electrical engineering matured by building modular, transparent design abstractions on top of solid foundations (Schrödinger's / Maxwell's equations). AI faces equally complex phenomena but has **no comparable foundation** — "we are winging it." The tripartite blend is offered as a step toward such design principles, not as the foundation itself.

## Related concepts
- [Collectivist AI / AI-as-market](collectivist-ai.md) — the systems the blend is meant to design.
- [Mechanism design & statistical contract theory](mechanism-design.md) — the economic leg.
- [Prediction-powered inference](prediction-powered-inference.md) — an inferential-economic blend in action.
- [AI safety and alignment](../safety/ai-safety-alignment.md) — Jordan reframes alignment/privacy/fairness as **tradeoffs**, which the blend makes expressible.

## Mentioned in
- [A Collectivist, Economic Perspective on AI (Jordan, 2025)](../../sources/jordan-collectivist-economic-ai.md)
