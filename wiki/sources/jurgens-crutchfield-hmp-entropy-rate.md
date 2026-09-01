---
title: "Shannon Entropy Rate of Hidden Markov Processes (Jurgens & Crutchfield, 2020)"
type: source
url: https://arxiv.org/abs/2008.12886
fetch_url: https://csc.ucdavis.edu/~cmg/papers/serhmp.pdf
local_path: raw/jurgens-crutchfield-hmp-entropy_2008.12886.pdf
sha256: fadb27e300202cdcf7e0a7c1b88740880a04284fb8ecc362a2a0fbcd01e86885
author: "Alexandra M. Jurgens, James P. Crutchfield"
affiliations: Complexity Sciences Center, Physics Department, University of California at Davis
published: 2020-08-29
venue: "arXiv (nlin.CD; cond-mat.stat-mech; cs.IT; math.DS; stat.ML); published in J. Stat. Phys."
tags: [hidden-markov, entropy-rate, blackwell, blackwell-measure, mixed-states, belief-state, information-theory, epsilon-machine, iterated-function-system, unifilar, computational-mechanics, secondary-carrier]
ingested: 2026-08-31
---

## Summary

Ingested as the accessible carrier for **David Blackwell, "The entropy of functions of finite-state Markov chains" (Transactions of the First Prague Conference on Information Theory, Statistical Decision Functions, Random Processes, 1957, pp. 13–20)** — a paper that is not digitized publicly and could not be obtained. §VI of this paper **transcribes Blackwell's Theorem 1 in his own notation** and then builds on it, so the wiki gets Blackwell's actual result with honest provenance.

> [!warning] This is a secondary for Blackwell 1957
> Every claim below attributed to Blackwell is **as reported by Jurgens & Crutchfield**, who state they transcribe his theorem "retaining his notation." The primary remains un-ingested. If a scan of the Prague proceedings surfaces, ingest it and re-check.

The problem: a **hidden Markov chain** is a finite-state Markov chain observed only through a function of its state. Shannon's entropy-rate formula applies when the presentation is **unifilar** — the current state plus the next symbol determines the next state. Drop unifilarity and, per Blackwell, **there is no closed-form expression for the entropy rate at all**. The reason is structural rather than technical: predicting a nonunifilar HMC requires an **infinite** set of causal states, so a "finitely generated" process can be genuinely un-summarizable by any finite unifilar machine.

Blackwell's constructive answer is to replace the finite state set with **mixed states** — distributions over the underlying states, i.e. what robotics and RL call **belief states** — and integrate over their stationary distribution, now called the **Blackwell measure**. Jurgens & Crutchfield's contribution is to notice that the mixed-state presentation is an **iterated function system**, which makes the integral computable as a time average along a long orbit.

## Blackwell's result, as transcribed (§VI, Theorem 3 = Blackwell Thm. 1)

Let `{xₙ}` be a stationary ergodic Markov process on states `1,…,I` with transition matrix `M = ‖m(i,j)‖`. Let `Φ` map states to observed values `a = 1,…,A`, and `yₙ = Φ(xₙ)`. The entropy of the `{yₙ}` process is

`H = −∫ Σₐ rₐ(w) log rₐ(w) dQ(w)`

where `Q` is a probability distribution on the simplex `W` of vectors `w = (w₁,…,w_I)`, `wᵢ ≥ 0`, `Σᵢ wᵢ = 1`, and `rₐ(w) = Σᵢ Σ_{j : Φ(j)=a} wᵢ m(i,j)`. `Q` is concentrated on sets `W₁,…,W_A` and satisfies a self-consistency condition `Q(E) = Σₐ ∫_{fₐ⁻¹E} rₐ(w) dQ(w)`, with `fₐ` mapping `W` into `Wₐ` by `[fₐ(w)]ⱼ = Σᵢ wᵢ m(i,j) / rₐ(w)` for `Φ(j) = a`.

The reading the authors give: Blackwell's formula **replaces the average over a finite set of unifilar states in Shannon's formula with (i) the mixed states and (ii) an integral over the Blackwell measure.** Same shape as Shannon; uncountable index set.

## What Jurgens & Crutchfield add

- **The mixed-state presentation is an iterated function system.** `rₐ` is the place-dependent probability and `fₐ` the map. This is the key identification, and it imports the machinery of dynamical systems.
- **Contractivity ⇒ ergodicity**, so the integral over the Blackwell measure can be replaced by a **time average along one long orbit**: pick any starting point in the mixed-state simplex, evolve it under the IFS, sample the entropy of the place-dependent distribution at each step, and average. The entropy rate is then computable to arbitrary accuracy without ever representing the infinite state set.
- Framing in **computational mechanics** terms: for a unifilar HMC the minimal generator is the **ε-machine**, whose states are the process's **causal states** — the minimal maximally-predictive features — and whose size is a constructive definition of the process's *structural complexity*. For a nonunifilar HMC the causal states are generically the uncountable set of mixed states.
- Explicitly leaves **structure** (as opposed to randomness) open, while arguing the mixed-state presentation is the route to it.

## Key claims

- Unifilarity is the dividing line: with it, Shannon's formula; without it, no closed form (Blackwell).
- A finite-state HMC can generate a process no finite unifilar machine predicts — "finitely generated" does not mean "finitely describable."
- Mixed states = belief states = the predictive features; Blackwell introduced them in 1957 "although he does not refer to them as such."
- The entropy rate is nonetheless *calculable*, via IFS ergodicity, not merely bounded.
- HMCs are named as underlying coding theory, stochastic thermodynamics, speech recognition, computational biology, epidemiology and finance.

## Entities mentioned

- **David Blackwell** — author of the 1957 Prague paper this source carries. Statistician and game theorist; the first Black scholar elected to the National Academy of Sciences. No wiki page, and the primary is un-ingested.
- **James P. Crutchfield**, **Alexandra M. Jurgens** — UC Davis Complexity Sciences Center. Crutchfield is the originator of computational mechanics and the ε-machine.
- **Claude Shannon** — the unifilar entropy-rate formula this generalizes.
- J. J. Birch (1962) — "Approximations for the entropy for functions of Markov chains," the follow-on to Blackwell cited in the same bibliography.

## Concepts touched

- [Belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md) — the concept page this source anchors.
- [Latent space](../concepts/world-models/latent-space.md) — a learned latent is the modern, non-Bayesian answer to the same question Blackwell's mixed states answer exactly.
- [World model](../concepts/world-models/world-model.md) — the mixed state *is* the world model of a partially-observed process, in the only sense that admits a theorem.
- [Identifiability](../concepts/world-models/identifiability.md) — Blackwell & Koopmans' companion 1957 paper is literally *On the Identifiability Problem for Functions of Finite Markov Chains* (Ann. Math. Statist.), the same year. The wiki's identifiability page is about JEPA; the lineage is older than it records.

## Open questions

- **The primary is still missing.** Blackwell 1957 is cited in this wiki on the strength of one secondary transcription. Worth chasing through a library.
- **Does the infinite-causal-state result have teeth for learned world models?** Every latent world model in this wiki compresses history into a **finite** vector. Blackwell says that for a nonunifilar process the sufficient statistic is generically infinite-dimensional — so a fixed-width latent is provably lossy in a way that is not a training failure. Whether that bound bites at realistic horizons, or is a measure-zero worry, nobody here has asked.
- **Unifilarity as a design target.** If unifilar presentations are the ones with closed-form entropy and finite sufficient statistics, is there an architectural analogue worth engineering toward? [FLARE](../concepts/world-models/flare.md) and the JEPA line pick latent structure on other grounds entirely.
