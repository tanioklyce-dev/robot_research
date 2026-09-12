---
title: An exact mapping between the Variational Renormalization Group and Deep Learning (Mehta & Schwab, 2014)
type: source
url: https://arxiv.org/abs/1410.3831
fetch_url: https://arxiv.org/pdf/1410.3831v1
author: Pankaj Mehta, David J. Schwab
published: 2014-10-14
ingested: 2026-09-11
venue: arXiv preprint (stat.ML; v1; 8 pp.) — no journal reference on arXiv as of 2026-09
local_path: raw/1410.3831v1.pdf
sha256: 23552a44cbe27dee91cca2b6998d92136cb67c5472d04283d39363399b05519b
format: pdf
tags: [renormalization-group, coarse-graining, rbm, deep-learning-theory, ising-model, statistical-physics, variational, kadanoff, jepa, foundational]
---

## Summary

The preprint the wiki's renormalization-group language has been leaning on, read so that the claim can be scoped. Mehta and Schwab show that **Kadanoff's variational real-space RG and a Restricted Boltzmann Machine are the same object under a change of notation**: define the RG coupling operator as T({v},{h}) = −E({v},{h}) + H[{v}], where E is the RBM energy and H the data Hamiltonian, and the RG-transformed Hamiltonian of the coarse spins equals the RBM's marginal Hamiltonian over hidden units, H^RG_λ = H^RBM_λ (their Eq. 21). When the RG is exact (Tr_h e^T = 1), T is exactly the conditional p(h|v) and the RBM reproduces the data distribution (KL = 0). Stacking RBMs is stacking RG steps. Two illustrations: the 1-D Ising decimation tanh J^(n+1) = tanh² J^(n) realized as a hand-built deep architecture, and a 1600-400-100-25 RBM stack trained on 40×40 2-D Ising samples near criticality (J = 0.408, T_c at 0.4352) with L1 regularization, whose learned receptive fields are local blocks that grow with depth — "self-organizing to implement block spin renormalization," at compression 64. The paper's conclusion is deliberately soft: DNNs "**may be** employing a generalized RG-like scheme."

## Key claims, with their scope

| Claim | Status in the paper | Scope |
|---|---|---|
| Variational RG ↔ RBM is an exact, one-to-one mapping | proved by definition (Eqs. 18–22) | **binary** visible/hidden units, energy-based model; "holds for any Boltzmann Machine" |
| The two *learn* the same way | **no** — stated explicitly: RG minimizes a free-energy difference, RBMs minimize KL; "distinct variational approximation schemes for coarse graining" | — |
| Deep = iterated RG | by stacking; the 1-D construction "contains no information about half of the visible spins" | 1-D Ising, hand-built |
| Trained DNNs discover block-spin RG | **qualitative**: receptive fields are local and grow with layer (Fig. 3); reconstructions "qualitatively reproduce" samples | one 2-D Ising model, one architecture, one temperature, L1-regularized, unsupervised |
| Therefore deep learning is RG | **not claimed** — "suggests," "may be," "reminiscent of" | — |

Also noted by the authors: RG is usually applied to systems with many symmetries, deep learning to data "with limited structure" — "a potential obstacle for importing ideas."

## Reading it against the wiki

> [!note] Verdict on the backlog question
> The [backlog](../backlog.md) asked whether the mapping "holds for the RBM-on-Ising construction it defines and the wiki can use it with that scope, or it does not and the RG language stays a metaphor." **Both.** The mapping is correct and exact *as an identification of objects* — an RBM's energy is a variational RG coupling operator, and its hidden-unit Hamiltonian is the renormalized one. It says nothing about what a trained network with a different loss, continuous units, and no Boltzmann structure actually computes. For a [JEPA](../concepts/world-models/jepa.md) encoder — deterministic, continuous, trained by prediction in latent space with an anti-collapse regularizer — the RBM correspondence does not apply, and the RG reading is an **analogy with one formal anchor at the RBM level**. That is how [Fajmanova's essay](jepa-vs-physics-moudrkat.md) should be cited from now on: the RG↔JEPA table is a productive analogy; the "exact mapping" it rests on is exact for something else.

- What survives as a usable idea is the *criterion*: coarse-grain by keeping what determines the large-scale (predictable) behavior and marginalizing the rest. That is close to the joint-embedding argument on the [JEPA page](../concepts/world-models/jepa.md) and the [abstraction tax](../syntheses/world-models/abstraction-tax.md) — but those are supported by their own results, not by this paper.
- **Twelve years without a journal version** is consistent with the paper being a well-known but contested note; later work reframed the RG-network connection information-theoretically (Koch-Janusz & Ringel 2018, not ingested) and questioned how much the 2-D result shows. Those are the papers to read before making the analogy carry weight.

## Entities mentioned

- Pankaj Mehta (Boston University), David Schwab (Northwestern) — no pages; [Yann LeCun](../entities/yann-lecun.md)'s page notes this as "not his."

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) (as learned coarse-graining — now with the anchor scoped), [world model](../concepts/world-models/world-model.md), [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) (the wiki's actual theory of what encoders keep).

## Open questions

- A version of the mapping for continuous, deterministic encoders — none known to the wiki.
- Koch-Janusz & Ringel's mutual-information RG and Lin, Tegmark & Rolnick's "Why does deep and cheap learning work so well?" as the follow-ups that would settle whether the 2-D result generalizes.
