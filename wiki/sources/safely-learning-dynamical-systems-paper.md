---
title: "Safely Learning Dynamical Systems"
type: source
url: https://doi.org/10.1007/s10208-025-09689-8
author: "Amir Ali Ahmadi, Abraar Chaudhry, Vikas Sindhwani, Stephen Tu"
affiliation: Princeton University; Robotics at Google, New York
published: 2026-04
ingested: 2026-08-03
venue: "Foundations of Computational Mathematics (FoCM)"
format: journal article (65 pp)
local_path: raw/2305.12284.pdf
sha256: ff456689d8f7f604f20600af984ea91669415ded98f1943d70d29d5a936f2c7a
license: "arXiv preprint 2305.12284 (v2, 2024-06-08) used as the readable copy; version of record is the FoCM article"
tags: [safe-learning, formal-methods, semidefinite-programming, conic-optimization, dynamical-systems, control-theory, robust-optimization, safety, primary-source]
---

## Summary

**The formal-guarantees counterweight to everything else in this safety cluster.** Where [ASIMOV](asimov-benchmark-paper.md), [Predictive Red Teaming](predictive-red-teaming-paper.md), and the [Veo simulator](veo-robotics-policy-evaluation-paper.md) attack safety empirically — benchmarks, anomaly prediction, generative probing — this paper asks whether safe exploration can be **proved**, and answers with convex optimization.

The problem: you must learn an unknown dynamical system by observing trajectories, but every trajectory you run risks leaving a safety region. The paper gives "a mathematical definition of what it means to safely learn a dynamical system by sequentially deciding where to initialize the next trajectory."

**The safety condition is worst-case over a hypothesis class**, which is what makes it a guarantee rather than a heuristic: the state must stay within the safety region for a horizon of *T* steps **under the action of all dynamical systems that (i) belong to a given initial uncertainty set, and (ii) are consistent with the information gathered so far.** Safety must hold for every system still compatible with what you know — so it degrades gracefully as data accumulates and uncertainty shrinks.

> [!note] Why this belongs in a robotics wiki
> It is the rigorous answer to the question the empirical safety papers can only bound statistically: *how do you explore without breaking anything, with a certificate?* The trade is scope — this covers linear and polynomial systems with a known uncertainty set, not VLMs driving humanoids.

## Key claims

### Linear systems (n states)

| Horizon | Result |
|---|---|
| **T = 1** | A **linear-programming** algorithm that either safely recovers the true dynamics from **at most n trajectories**, or **certifies that safe learning is impossible** |
| **T = 2** | A **semidefinite representation** of the set of safe initial conditions; **⌈n/2⌉ trajectories generically suffice** |
| **T = ∞** | **SDP-representable inner approximations** of the safe-initial-condition set; **one trajectory generically suffices** |

The T=1 result is the striking one: the algorithm returns either a solution *or a proof that no safe learning strategy exists*. Infeasibility is a certified answer, not a failure to find one.

Extensions cover uncertainty sets containing **sparse, low-rank, or permutation matrices**, and systems **with a control input**.

### Nonlinear systems
- **T = 1:** a **second-order cone programming (SOCP)** representation of the set of safe initial conditions.
- **T = ∞:** SDP-representable inner approximations.
- A procedure to safely collect trajectories and **fit a polynomial model** of the nonlinear dynamics that is consistent with the initial uncertainty set and best agrees with observations.
- Extensions to **noisy measurements** and **systems with disturbances**.

Keywords as given: *learning dynamical systems, safe learning, uncertainty quantification, robust optimization, conic optimization.*

## Entities mentioned
- [Amir Ali Ahmadi](../entities/amir-ali-ahmadi.md) · [Vikas Sindhwani](../entities/vikas-sindhwani.md) · Princeton University · Robotics at Google
- [Google DeepMind](../entities/google-deepmind.md)

## Concepts touched
- [Formal verification](../concepts/learning/formal-verification.md) — proof-carrying guarantees rather than empirical evaluation.
- [Optimal control](../concepts/robotics/optimal-control.md) — the classical-control tradition; SDP/SOCP as the computational tool.
- [Semantic safety](../concepts/safety/semantic-safety.md) — the explicit contrast class.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — safe exploration is the same problem RL faces on hardware.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md)

## Open questions
- **Scope vs. the rest of this cluster.** Results require a *known* initial uncertainty set and a *parametric* system class (linear, or polynomial for the nonlinear case). None of the wiki's ingested robot policies — diffusion policies, VLAs, code-writing agents — fit that description. **The formal thread and the empirical thread do not currently meet**, and no ingested source attempts to bridge them.
- **Generic sufficiency** (⌈n/2⌉ trajectories at T=2, one at T=∞) is a statement about generic problem instances; the non-generic cases and their frequency in practice are not characterized here.
- **Computational scaling** of the SDPs with state dimension n is the practical question for robotics-scale systems, and is not the paper's focus.
- **No robot experiments.** This is a mathematics paper; the robotics motivation is stated but not demonstrated on hardware.
- The earlier companion **"Safely Learning Dynamical Systems from Short Trajectories"** (arXiv 2011.12257, 2020) is not ingested.

> [!note] Access note
> The Springer version of record is behind a cookie-authenticated viewer that could not be fetched. Content here is from the **arXiv preprint (2305.12284v2, 2024-06-08)**; the FoCM article is the citable version and was published 2026-04. Where the two differ, the journal version governs — this ingest has not diffed them.

## Related sources
- [ASIMOV Benchmark](asimov-benchmark-paper.md) · [Predictive Red Teaming](predictive-red-teaming-paper.md) · [Veo world simulator](veo-robotics-policy-evaluation-paper.md) — the empirical wing of the same lab's safety program; [Vikas Sindhwani](../entities/vikas-sindhwani.md) is on all four.
- [DeepMind — Responsibly advancing AI and robotics](deepmind-gemini-robotics-safety-page.md) — the public framing, which does **not** mention this formal line.
