---
title: The Birth of Self Supervised Learning — A Supervised Theory (Balestriero & LeCun; NeurIPS 2024 SSL Workshop)
type: source
url: https://openreview.net/forum?id=NhYAjAAdQT
author: Randall Balestriero, Yann LeCun
published: 2024-12
ingested: 2026-09-11
venue: Self-Supervised Learning Workshop, NeurIPS 2024 (spotlight poster); 4 pp. + appendix
local_path: raw/birth_of_SSL.pdf
sha256: fdf655c2e36b91df1073604c9fe7bd23b11bbabace15eab53d64cd012d42187b
format: pdf (user-supplied; OpenReview's PDF endpoint was not reachable from the ingest environment)
tags: [self-supervised-learning, ssl-theory, supervised-learning, vicreg, whitening, spectral-embedding, instance-discrimination, mutual-information, balestriero, lecun, representation-learning, data-curation]
---

## Summary

A short theory note that reframes the supervised / self-supervised split as a difference in **labels, not losses**. Theorem 1: minimizing the ordinary supervised MSE through a ridge-regularized linear head, once the head is solved in closed form, *is* a "relative" objective that aligns the pairwise-prediction matrix of the backbone with the pairwise-label matrix **G = YᵀY** — the same form as SSL losses. Corollary 1: when G has a single nonzero eigenvalue (balanced classes, or the SSL positive-view graph), the relative objective recovers **VICReg and Whitening-MSE** up to a rescaling of dimensions. Proposition 1: the SSL graph "views of the same sample are positives" is the supervised objective under the labeling that gives **every sample its own class** — the labeling that forces the representation to keep enough to separate all training samples, hence maximizes mutual information between X and f_θ(X), which the authors identify with "best worst-case downstream performance." Theorem 2 shows the singular-value gradient vanishes, so the objective does not blow representations up. The conclusion: SSL's downstream advantage "may not be the actual training objective… but instead may be due to that optimal labeling," and Appendix B sketches how a different head constraint (orthogonal W) yields a different SSL method.

## Key claims

- **Lemma 1 / Theorem 1.** With f_θ(X) = UΣVᵀ, min over W, b of the ridge-regularized MSE equals −(1/N) Tr(VᵀYᵀY V D) + const, with D_kk = s_k² / (s_k² + λN). The left singular vectors drop out ("the optimal W automatically maps them"); only the right singular vectors and singular values of the representation matter, compared against YᵀY. **No assumptions on X, f_θ, or Y.**
- **Theorem 2.** ∂/∂σ_k = (VᵀGV)_kk · 2σ_kλ / (σ_k² + λN)²: always pushes σ_k up when λ > 0, vanishes as σ_k grows, and vanishes as λ → 0 — "the only role of σ_k is to allow a more regularized classifier head to solve the task by expanding the features."
- **Corollary 1.** Constraining σ_k = 1 recovers Whitening-MSE, σ_k ≥ 1 recovers VICReg (via Balestriero & LeCun 2022); the practical parametrization is −(1/N) Tr(HGH f_θ(X)ᵀf_θ(X)) + α‖Cov(f_θ(X)) − I‖²_F, which "reorganiz[es]… directly [to] the exact VICReg objective."
- **Proposition 1.** G_ij = 1{⌊i/V⌋ = ⌊j/V⌋} over NV augmented views is recovered from labels Y ∈ ℝ^{NV×N} assigning each original sample a unique class.
- **Practical corollary the authors draw:** the theory predicts that **duplicates and very noisy data break the assumption** behind SSL's labeling, "corroborat[ing]" the empirical importance of data curation (Assran et al. 2022; Vo et al. 2024).
- **Appendix B:** with an orthogonality constraint on the head, the objective becomes (1/P)‖f_θ(X)‖²_F − (2/P) Tr((f_θ(X)ᵀ G f_θ(X))^{1/2}) + const — a different SSL-shaped loss from the same supervised starting point.

> [!warning] Workshop-grade, and visibly unfinished
> The appendix proof of Lemma 1 contains the line **"Positivity of D — ToDo"**, and Appendix B.1 is a set of pasted paragraph fragments about explicit affinity graphs and augmentation strength that belong to another manuscript. Figure 2 is an empirical check of Lemma 1 at λ = 0. The main results are algebra and are almost certainly right, but this is a four-page note plus an unpolished appendix, not a reviewed paper. Cite the *statements* (Theorem 1, Proposition 1), not the document's authority.

## Reading it against the wiki

- **It is the second half of the [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md).** The 2022 paper showed SSL objectives are spectral embeddings on a positive-pair graph G; this note shows the *supervised* objective is the same embedding on G = YᵀY. The two together make "supervised vs self-supervised" a choice of graph — which is exactly how the [LeJEPA](lejepa-paper.md) program talks about it and why that program treats the objective as interchangeable and the target as what matters.
- **A tension with the same day's [Mehta & Schwab](mehta-schwab-2014-variational-rg-deep-learning.md) ingest, worth keeping.** The coarse-graining reading of representation learning says *discard* the irrelevant. Proposition 1 says SSL's implicit labeling is instance discrimination, which **maximizes retained information** — keep everything that separates samples. Both are true of different objectives: instance-discrimination SSL keeps; latent-space *prediction* (a JEPA's actual loss) is what discards. For the wiki's [focused question](../syntheses/world-models/open-questions-and-research-direction.md) — what must a world model preserve — this note is the clearest statement that the anti-collapse term and the prediction term pull in opposite directions, and that "SSL" alone does not say which wins.
- **"Maximizes worst-case downstream performance" is argued through mutual information, not proved as a bound.** The step from "keeps every sample separable" to "best worst case over downstream tasks given the function class" is a sentence, not a theorem; the [representation-evaluation](../concepts/learning/representation-evaluation.md) page's probes are how one would check it.
- **Data curation as a theoretical prediction** is a useful reframing of a practical finding: duplicates make the implicit labels wrong, not just the dataset inefficient.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md), [Yann LeCun](../entities/yann-lecun.md).
- VICReg (Bardes, Ponce, LeCun), Whitening-MSE (Ermolov et al.), spectral contrastive loss (HaoChen et al.) — no pages.

## Concepts touched

- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md), [JEPA](../concepts/world-models/jepa.md), [representation evaluation](../concepts/learning/representation-evaluation.md), [distributed representations](../concepts/learning/distributed-representations.md).

## Open questions

- Whether the "Positivity of D" gap was closed in a later version — no arXiv or journal version was found.
- The orthogonal-head objective (Appendix B) is derived and never tested.
- Which SSL method corresponds to *label-imbalanced* G — the abstract promises it, the body does not deliver it.
