---
title: "Joint-Embedding vs Reconstruction: Provable Benefits of Latent Space Prediction for SSL (Van Assel et al., NeurIPS 2025)"
type: source
url: https://arxiv.org/abs/2505.12477
fetch_url: https://arxiv.org/pdf/2505.12477v2
local_path: raw/2505.12477v2.pdf
sha256: a7f22b4ad678e49339335ed5965cc4857e6b3504d442814175ddda3d9bfb679d
author: "Hugues Van Assel (Genentech), Mark Ibrahim (Meta AI, FAIR), Tommaso Biancalani (Genentech), Aviv Regev (Genentech), Randall Balestriero (Brown University)"
published: 2025-05-18
venue: "NeurIPS 2025. arXiv v1 2025-05-18 → **v2 2025-10-14**, the version read here. 33 pp., 9 figures."
format: theory paper with empirical validation (PDF)
tags: [jepa, joint-embedding, reconstruction, mae, dino, byol, ssl, augmentation, theory, closed-form, linear-models, imagenet-c, balestriero, genentech]
ingested: 2026-09-07
---

## Summary

**The wiki's longest-running dispute has a stated answer, and it is a crossover rather than a verdict.** Van Assel, Ibrahim, Biancalani, Regev and Balestriero derive **closed-form solutions for both SSL paradigms under linear models**, and use them to characterize exactly when to predict in input space (reconstruction) versus in latent space (joint-embedding). The answer turns on one quantity: **the magnitude of the irrelevant features in the input signal.**

> **Key takeaway** (their box, quoted in full): *"When irrelevant features have **low magnitude** and there is limited prior information on effective augmentations, **reconstruction is preferable**. In contrast, when these irrelevant features are **non-negligible** (as is common with real-world data) or effective augmentations can be identified, **joint-embedding is preferable**."*

So it is **not** "JEPA wins." There is a named regime where reconstruction is the right choice, and a stated reason: when the important components already have the largest magnitude, a reconstruction objective prioritizes them automatically and therefore **depends less on getting augmentations right**.

Ingested one turn after being filed as the top backlog item, off [Balestriero's own site](randall-balestriero-personal-site.md) — where the wiki discovered a paper it had never mentioned that addresses precisely what it had been arguing about for months.

## The mechanism, in their terms

Set up: input `x̃ = x + γ`, where the **important features** `X` occupy `k` components (singular values `κᵢ > 0`) and the **irrelevant noise** `γ ∼ N(0, Γ)` is zero on those `k` and strictly positive on the rest. Augmentations are `τ(x) = x + θ + α·γ`, where **α controls how well the augmentation is aligned with the noise** — the augmentation's noise term is drawn from *the same distribution* as the irrelevant features.

Three results, in order of how much they change:

**1. Supervised learning has two escape routes; SSL has one.** (Prop. 4.2 vs 4.3/4.4)

| | Perfect alignment (α → ∞) | Infinite samples (n → ∞) |
|---|---|---|
| **Supervised** | recovers optimum | **recovers optimum, for any fixed α** |
| **Reconstruction SSL** | recovers optimum | **only if α² > α²_RC** |
| **Joint-embedding SSL** | recovers optimum | **only if α² > α²_JE** |

> [!warning] This is a hard limit on scale, stated as a theorem
> *"Unlike SSL, supervised models can overcome misalignment between augmentations and noise with enough samples, as [they learn] robustness by observing different noise realizations across identically labeled data."*
>
> **For SSL, more data does not fix bad augmentations.** The alignment requirement *"persists even as the sample size n becomes arbitrarily large."* Labels supply an independent signal about what is irrelevant; without them, the augmentation *is* the only statement of what should be ignored, and no quantity of samples substitutes for it.
>
> Set that against the week's other reading. [GEN-1.5](generalist-gen-1-5-blog.md): *"more pretraining makes adaptation faster, cheaper, and more general… we do not yet see where that curve asymptotes."* Both can be true — GEN-1.5 is not doing augmentation-based SSL — but this is the sharpest available statement of **a thing scale provably does not buy**, in a field whose default assumption is that it buys everything.

**2. The crossover.** (Corollary 4.5) With `η`, `δ` defined from the important components' singular values:

- **low noise** (`max λᵢ^Γ < η²/δ`) → `α_JE > α_RC` → **reconstruction is preferable** (it needs *less* tailored augmentation)
- **high noise** (`min λᵢ^Γ > η²/δ`) → `α_JE < α_RC` → **joint-embedding is preferable** (strictly weaker alignment condition)

The intuition they give for each direction is worth keeping. Under weak noise, *"the core important components possess the greatest magnitude and are consequently prioritized by the model during reconstruction"* — reconstruction gets the right answer for free. Under strong noise, joint-embedding wins because it *"prioritizes latent space prediction, thereby **bypassing the need to reconstruct irrelevant noise components as model outputs**."*

And the practical asymmetry that decides it in the field: *"the irrelevant components are typically unknown in real-world applications,"* so **the goal is to minimize the alignment requirement** — you want the method that needs you to be least right about what to ignore.

**3. Why language and vision differ, which the wiki had as intuition and now has as an argument.** From §1.1:

> In language, reconstruction-based learning… is highly effective because **textual tokens represent compact, semantically meaningful units that already abstract away most low-level variability**… Predicting a missing token provides a learning signal that operates directly in semantic space.
>
> In contrast, **visual data are essentially sensorial recordings of the physical world, capturing raw information without inherent semantic compression.** As a result, pixel-level reconstruction objectives tend to drive models toward capturing local statistics and textures that account for most of the input's variance.

Named examples of "irrelevant features" with large magnitude: **image backgrounds**, and **experimental batch effects in scRNA-seq data** — the latter explaining the author list, three of whom are at **Genentech**. The theory is motivated by a domain where the noise genuinely dominates.

## The measurement

ImageNet-100, **linear probing** top-1 under [ImageNet-C](https://arxiv.org/abs/1903.12261) corruptions, severity 1 → 5:

| Method | Pixelate drop | Gaussian-noise drop | Zoom-blur drop | **Average** |
|---|---|---|---|---|
| **DINO** (ViT) | 12.4% | 12.7% | 6.5% | **10.5%** |
| **BYOL** (ResNet) | 12.0% | 16.1% | 9.0% | **12.4%** |
| **MAE** (ViT) | **27.9%** | **27.3%** | **20.0%** | **25.1%** |

**MAE degrades roughly 2.4× as much as DINO under the same corruption**, which is the theory's prediction: crank up the irrelevant-feature magnitude and the reconstruction method falls off first. DINO-vs-MAE is the clean comparison (both ViT); BYOL is a ResNet, so that row mixes architecture with objective.

Linear-model experiments on MNIST, Fashion-MNIST, Kuzushiji-MNIST and **single-cell RNA-seq** confirm all three propositions directly, sweeping α and n against weak (`λ_max^Γ = 10³`) and strong (`10⁶`) noise.

> [!warning] The empirical half uses the metric MAE's authors reject
> Table 1 is **linear probing**, and [MAE's central defence](mae-paper.md) is that *"linear probing and fine-tuning results are largely uncorrelated"* — tuning one transformer block takes ViT-L from 73.5 → 81.0 and inverts orderings. **This paper does not run the fine-tuning comparison**, so its deep-network experiment does not engage MAE's counterargument on MAE's chosen ground.
>
> They are aware of it, and they turn it into evidence: the conclusion cites *"a consistent empirical finding: reconstruction methods **typically necessitate fine-tuning** to address the inherent misalignment between the features they learn and those that are perceptually useful."* That is a defensible move — *needing* fine-tuning is a cost — but it is an argument, not a measurement, and the wiki should not record the dispute as closed on the empirical side.
>
> The *theoretical* half is unaffected: it is about recovering the optimal **linear** representation, so a linear probe is the natural instrument rather than a contested one.

## What it does and does not settle

> [!note] The scope caveat that governs everything above
> **The closed-form results are for linear encoders and decoders.** Theorems 3.1 and 3.2 solve linear models; Propositions 4.2–4.4 and Corollary 4.5 are statements about those. The deep-network section is *validation that the ordering survives*, not proof that it does. Every "provable" in the title applies to the linear case.
>
> That is still a great deal more than the field had — an explicit condition, a named crossover quantity, and a mechanism — but "provable benefits" should be read as *provable in a tractable model whose predictions then held on ImageNet-C*.

**What it settles for this wiki:** the reconstruction-vs-latent-prediction question is **not a matter of taste or of one side being wrong**. It is a property of the data. The wiki has been recording the dispute as unresolved across [MAE](mae-paper.md), [the anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md), [Balestriero's Day 3 case](chicago-booth-world-modeling-workshop-2026-day3.md) and the [generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) comparison. The axis is **irrelevant-feature magnitude**, and both sides are right in their own regime — MAE on data that is already semantically compressed, JEPA on raw sensory recordings.

**What it leaves open:** the finite-sample regime, which they name as future work; whether the crossover point is estimable in practice (you would need to know Γ, which is the thing you don't know); and the deep, non-linear case.

> [!note] Two 2026 robot systems independently implemented the fix this theory implies
> By this paper's criterion, **robot camera and proprioceptive streams are squarely in the joint-embedding regime** — "sensorial recordings of the physical world, capturing raw information without inherent semantic compression" is a literal description of a robot's input. Yet the two strongest robot results the wiki ingested this week run on **generative video backbones**: [FLUX-mimic](flux-3-launch.md) on FLUX 3, and [mimic-video](mimic-video-paper.md) on Cosmos-Predict2.
>
> That looks like a contradiction and isn't, because **both modify the pure-reconstruction recipe in exactly the direction this theory says you would have to**:
>
> - **mimic-video never reconstructs.** Best control comes at **τ_v = 1 — pure noise** — reading *intermediate* features, and *"high-fidelity video reconstruction is not required for performant robot policies."* More reconstruction makes control **worse**. It is a generatively-*trained* network used as a representation extractor.
> - **Self-Flow puts representation learning inside the generative objective**, explicitly because generative models *"produce less disentangled representations, which puts a ceiling on their usefulness."*
>
> **The theory predicts the fix; two independent systems shipped it.** And it sharpens the wiki's framing: the axis is not *does the model have a decoder* but *is the training signal dominated by variance that doesn't matter* — a generative model that routes around irrelevant features is not in the regime the corollary penalizes.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) — senior author; this is the theoretical basis under his [Day 3 case against reconstruction](chicago-booth-world-modeling-workshop-2026-day3.md), which the wiki had recorded as argued on probe accuracy with no stated theory.
- **Hugues Van Assel**, **Tommaso Biancalani**, **Aviv Regev** — Genentech; no pages. **Mark Ibrahim** — Meta FAIR, also a [Cookbook](ssl-cookbook.md) co-author.
- [MAE](../entities/mae.md) · [DINO](../entities/dino.md) · [BYOL](../entities/byol.md) — the three methods measured.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the condition under which its central bet pays.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md) — the comparison this reframes as a crossover.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — the family tree; this supplies the axis it was missing.
- [Contrastive learning](../concepts/learning/contrastive-learning.md) — augmentation design as the load-bearing choice, now with a theorem.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — the linear-probe caveat above.
- [Financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) — the same finding in another domain: augmentations are domain structure, and the wrong ones provably cannot recover the signal.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — force and tactile streams are raw sensory recordings nobody has augmentations for.

## Open questions

- **What are the "irrelevant features" of a robot sensor stream, and what augmentation aligns with them?** This is the paper's requirement translated into the wiki's domain, and nobody has an answer. For images the community found colour jitter and cropping by a decade of trial and error; for **force/torque and tactile** there is no such playbook, and the theorem says sample size will not rescue a bad guess.
- **Can the crossover be estimated without knowing Γ?** The corollary compares `max λᵢ^Γ` against `η²/δ` — quantities defined in terms of the noise you are trying to remove. A usable diagnostic that says *"you are in the JE regime"* from data alone would turn the result from an explanation into a tool. Note [RankMe](../concepts/learning/representation-evaluation.md) is the wiki's only label-free instrument of this shape.
- **Does the ordering survive fine-tuning?** The one experiment that would close the dispute on MAE's own terms, and it is not run.
- **Where does [Self-Flow](flux-3-launch.md) sit in this framework?** It claims generation and representation quality improve *together* via heterogeneous per-token noise. In this paper's language that reads as **changing the effective alignment between the corruption process and the irrelevant features** — which, if right, means Self-Flow is a way to *manufacture* the alignment condition rather than a refutation of the trade-off. Neither paper cites the other.
