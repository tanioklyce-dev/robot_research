---
title: "The Elements of Differentiable Programming (Blondel & Roulet, Google DeepMind, draft v3, June 2025)"
type: source
local_path: raw/2403.14606v3.pdf
arxiv: https://arxiv.org/abs/2403.14606
url: https://arxiv.org/abs/2403.14606
author: Mathieu Blondel, Vincent Roulet
affiliation: Google DeepMind
published: 2024 (v1); 2025-06-24 (v3 draft)
pages: 485
license: arXiv non-exclusive
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
tags: [pedagogical, textbook, differentiable-programming, automatic-differentiation, jvp, vjp, backpropagation, optimization, gradient-descent, sgd, adam, fenchel-young-loss, sparsemax, reinforce, reparametrization-trick, gumbel-softmax, smoothing, mathieu-blondel, google-deepmind, primary-source]
---

> [!note] Reference textbook, not a research paper
> 485-page **draft textbook** from Google DeepMind that systematically derives the math underlying every neural net, every gradient-based optimization, and every "differentiate through X" trick in modern ML. Free draft on arxiv (v3, June 2025). Companion Python source code on GitHub (link in book). The wiki ingests pedagogical companions at section-summary depth (cf. [Sutton & Barto](sutton-barto-rl-textbook.md), [Welch Labs Vol I](welchlabs-illustrated-guide-to-ai.md)) — this page captures structure + which chapters feed which existing wiki threads.

## Summary

**"The Elements of Differentiable Programming"** by **[Mathieu Blondel](../entities/mathieu-blondel.md)** and **Vincent Roulet** (Google DeepMind). The book's thesis (verbatim from abstract):

> "Differentiable programming is not merely the differentiation of programs, but also the **thoughtful design of programs intended for differentiation**. By making programs differentiable, we inherently introduce probability distributions over their execution, providing a means to quantify the uncertainty associated with program outputs."

Five parts × 18 chapters cover the entire mathematical substrate of modern ML, from univariate calculus through transformer architectures and quasi-Newton optimization. Two cross-cutting framings tie everything together: **the optimization perspective** and **the probabilistic perspective**, with explicit analogies between the two (e.g. softmax = argmax + entropic regularization = Gibbs distribution).

This is the **most comprehensive single reference** for the math underneath every other ML/robotics ingest in this wiki — autodiff, transformers, flow matching, REINFORCE, reparametrization trick, Gumbel-softmax, Fenchel-Young losses, second-order optimization, all in one volume.

## Structure — 5 parts, 18 chapters

### Part I — Fundamentals (chs. 2–3)

- **Ch. 2 Differentiation** — univariate / multivariate derivatives, Jacobians, **linear maps + adjoints**, **JVPs + VJPs**, chain rule using linear maps, second-order + higher-order differentiation, Taylor expansions, **differential geometry** (manifolds, tangent + cotangent spaces, pushforward + pullback), generalized derivatives (Clarke, Rademacher). The grammar of everything downstream.
- **Ch. 3 Probabilistic learning** — MLE, KL divergence consistency, conditional distributions for binary/multiclass/regression, **exponential family + log-partition**, maximum entropy principle. Closes with "probabilistic learning with exponential families" — the foundation the rest of the book points back to when introducing softmax-as-Gibbs-distribution, Fenchel-Young losses, etc.

### Part II — Differentiable programs (chs. 4–6)

- **Ch. 4 Parameterized programs** — programs as DAGs / arithmetic circuits → feedforward networks → MLPs → activation functions (ReLU, softplus, max pooling, log-sum-exp, sigmoids, **argmax + softargmax**) → batch + layer normalization → **residual networks** → **RNNs** (vector↔sequence, aligned + unaligned seq2seq) → **transformers** (attention, self-attention, multi-head, transformer layer + block, token + positional encoding, encoder-only + decoder-only + encoder-decoder architectures). **The wiki's most rigorous single reference for transformer mechanics.**
- **Ch. 5 Control flows** — comparison operators, **soft inequality + soft equality** operators (heuristic + stochastic-process + Gaussian-process perspectives), logical operators + continuous extensions (triangular norms / co-norms), **if-else statements** (differentiating through branches + predicates; continuous relaxations), **for / scan / while loops** (cyclic graphs, unrolled, Markov-chain perspectives). The math behind "differentiable control flow."
- **Ch. 6 Data structures** — lists (basic + variable-length + soft indexing via continuous relaxations), **dictionaries** (basic + kernel-regression relaxation + discrete-distribution perspective + **link to attention in transformers**). Closes Part II by deriving attention as a differentiable dictionary lookup.

### Part III — Differentiating through programs (chs. 7–12)

- **Ch. 7 Finite differences** — forward / backward / central / higher-accuracy / higher-order / complex-step. The numerical-gradient baseline that autodiff replaces.
- **Ch. 8 Automatic differentiation** — **forward mode + reverse mode** on computation chains, on feedforward networks (computing adjoints + gradients), on general computation graphs, **Baur-Strassen theorem** (reverse mode = ~3× forward cost). Implementation: primitive functions, closure under composition, JVP + VJP examples, **automatic linear transposition**. **Checkpointing** (recursive halving + dynamic programming + online). **Reversible layers** (general + orthonormal JVPs). **Randomized forward-mode gradient estimator**.
- **Ch. 9 Second-order automatic differentiation** — Hessian-vector products (4 methods + complexity), **Gauss-Newton matrix** (approximation of Hessian, GN chain rule, GN vector product, factorization, stochastic setting), **Fisher information matrix** (definition via score function, link with Hessian, **equivalence with Gauss-Newton**), inverse-Hessian vector product (matrix-free linear solvers), second-order backprop, block-diagonal + diagonal approximations, randomized estimators (Girard-Hutchinson, Bartlett).
- **Ch. 10 Inference in graphical models as differentiation** — Markov chains, **Bayesian networks**, **Markov random fields**, conditional random fields, **inference on chains** (forward-backward, Viterbi), inference on trees, **inference as differentiation of log-partition + semirings**. The bridge from classical probabilistic ML to autodiff.
- **Ch. 11 Differentiating through optimization** — **implicit function theorem** + univariate/multivariate versions, JVP/VJP of implicit functions, **adjoint state method** (4 proofs: Lagrange multipliers + IFT + envelope + reverse-mode-with-backsubstitution), inverse function theorem. The math for bilevel optimization, meta-learning, and "differentiable optimization" layers.
- **Ch. 12 Differentiating through integration** — differentiation under the integral sign, **score function estimators / REINFORCE** (variance reduction + vector-valued + second derivatives), **path gradient estimators / reparametrization trick** (location-scale transforms, differentiable transforms, inverse transforms, pushforward operators, change-of-variables theorem), **stochastic programs** + stochastic computation graphs, **differential equations** (parameterized ODEs, continuous adjoint method, reversible discretization). Foundational for VAE training, RL gradient estimators, flow matching, neural ODEs.

### Part IV — Smoothing programs (chs. 13–14)

- **Ch. 13 Smoothing by optimization** — primal approach (infimal convolution, Moreau envelope), **Legendre–Fenchel transforms / convex conjugates** (closed-form examples, properties, conjugate calculus, fast Legendre transform), dual approach (duality between strong convexity + smoothness, smoothing by dual regularization, **generalized entropies**), **smoothed ReLU**, **smoothed max operators** (definition, root finding, **softmax**, **sparsemax**), relaxed step functions + argmax operators. **The book's most distinctive content** — Blondel-line research on Fenchel-Young losses + sparsemax + structured prediction.
- **Ch. 14 Smoothing by integration** — convolution (operators, kernel, discrete, multidimensional, link to infimal convolution, soft infimal convolution, soft Moreau envelope), **Fourier + Laplace transforms** (convolution theorem, link between Fourier + Legendre transforms, soft Legendre-Fenchel transform), perturbation of black-box functions (expectation in location-scale family, gradient estimation by reparametrization or **Stein's lemma**, link to evolution strategies, **zero-temperature limit**), **Gumbel tricks** (Gumbel distribution, perturbed comparison + argmax + max, Gumbel-softargmax, **perturb-and-MAP**).

### Part V — Optimizing differentiable programs (chs. 15–18)

- **Ch. 15 Optimization basics** — objective functions, **oracles**, **variational perspective of optimization algorithms** (each algorithm = a sequence of subproblems), function classes (Lipschitz, smooth, convex, strongly convex, nonconvex), performance guarantees.
- **Ch. 16 First-order optimization** — **gradient descent** (variational + convergence for smooth + momentum + accelerated), **stochastic gradient descent** (vanilla, momentum, adaptive = **Adam-class**), projected gradient + proximal gradient (variational + commonly-used projections + proximal operators).
- **Ch. 17 Second-order optimization** — **Newton's method** (variational + regularized + approximate direction + convergence + linesearch + geometric interpretation + stochastic), **Gauss-Newton** (exact + approximate + linesearch + stochastic), **natural gradient descent** (variational + stochastic NGD), **quasi-Newton** (**BFGS** + **L-BFGS**), approximate Hessian diagonal inverse preconditioners.
- **Ch. 18 Duality** — dual norms, **Fenchel duality**, **Bregman divergences**, **Fenchel-Young loss functions**. The capstone — ties the optimization perspective back to the probabilistic perspective via Fenchel-Young losses (Blondel's signature contribution).

## What this gives the wiki

This book covers the **mathematical foundations** of basically every learned model in this wiki. Specific chapter → wiki-content mappings:

| Chapter | Wiki content it grounds |
|---|---|
| **4.8 Transformers** | [VLA models](../concepts/learning/vla-models.md) → every VLA (OpenVLA, [π0](../entities/pi-zero.md), [π0.7](../entities/pi07.md), [SmolVLA](../entities/smolvla.md), [Helix](helix-blog.md)) is a transformer; [JEPA](../concepts/world-models/jepa.md) predictors are transformers; [DINOv2](../entities/dinov2.md) is a ViT. |
| **8 Automatic differentiation** | Every gradient-based ML technique. The Baur-Strassen result (reverse mode ≈ 3× forward) is the load-bearing complexity bound. |
| **9 Second-order autodiff** | [Optimal control](../concepts/robotics/optimal-control.md) (Gauss-Newton, BFGS for MPC); natural gradient (used in PPO variants). |
| **10 Inference as differentiation** | [Lean theorem prover](../concepts/learning/lean-theorem-prover.md) lineage (forward-backward, Viterbi on chains); CRF / MRF formulations under [VLA models](../concepts/learning/vla-models.md) action heads. |
| **11 Differentiating through optimization** | The mathematical substrate of **MPC + CEM** in [JEPA-WMs](../entities/jepa-wms.md) and [LeWM](../entities/leworldmodel.md); meta-learning (Chelsea Finn's MAML lineage referenced on [chelsea-finn.md](../entities/chelsea-finn.md)). |
| **12.3 REINFORCE / score function estimator** | [RECAP](../entities/pistar06.md) RL fine-tuning of [π*0.6](../entities/pistar06.md); also the gradient estimator most VLA-RL papers reference. |
| **12.4 Reparametrization trick** | VAE training (referenced across [DDPM](../entities/ddpm.md) lineage); the foundation under flow matching. |
| **12.6 Differential equations + continuous adjoint** | The math under **flow matching** in [π0](../entities/pi-zero.md), [π0.7](../entities/pi07.md), [SmolVLA](../entities/smolvla.md), [EgoScale](egoscale-paper.md); neural ODEs. |
| **13.5 Softmax + sparsemax** | Attention mechanisms in every transformer; action-distribution heads in VLAs that don't use flow matching. |
| **14.5 Gumbel tricks** | Action tokenization in OpenVLA-style discrete-action VLAs; differentiable sampling for stochastic policies. |
| **16 First-order optimization** | Every model in the wiki trained via SGD / Adam (variational perspective ties them together). |
| **17 Second-order optimization** | L-BFGS for inverse-problem fitting; Newton-method MPC; Gauss-Newton in least-squares VLA fits. |
| **18 Fenchel-Young losses** | Blondel's research line; the unifying framework that turns "cross-entropy ↔ softmax", "hinge loss ↔ argmax", "sparsemax loss ↔ sparsemax" into instances of one construction. |

## Entities mentioned

- [Mathieu Blondel](../entities/mathieu-blondel.md) — co-author; Google DeepMind; new entity filed by this ingest.
- [Google DeepMind](../entities/google-deepmind.md) — affiliation of both authors.

## Concepts touched

The book is a foundational reference for essentially every ML concept the wiki tracks. The most direct anchors:

- [Imitation learning](../concepts/learning/imitation-learning.md) — ch. 12 (REINFORCE + reparametrization) is the gradient-estimator math behind on-policy IL + RL.
- [VLA models](../concepts/learning/vla-models.md) — ch. 4.8 (transformers) + ch. 12.4 (reparametrization, foundation for flow matching) + ch. 13.5 (softmax / sparsemax).
- [Curriculum Module 1 (neural networks)](../syntheses/curriculum/curriculum-01-neural-networks.md) — chs. 2 (differentiation) + 8 (autodiff) are the rigorous version of Module 1's backprop content.
- [Curriculum Module 3 (attention + transformers)](../syntheses/curriculum/curriculum-03-attention-and-transformers.md) — ch. 4.8 is the rigorous version.
- [Curriculum Module 5 (generative models)](../syntheses/curriculum/curriculum-05-generative-models.md) — chs. 12.4 + 13 are the rigorous version of the DDPM/flow-matching/reparametrization material.

## Why this matters

- **The wiki's most comprehensive mathematical-foundation reference.** Welch Labs Vol I and Sutton & Barto are pedagogical; this is closer to an SICP-of-differentiable-programming reference work.
- **Single coherent narrative across autodiff + optimization + probabilistic-ML + transformers + flow matching + REINFORCE + Fenchel-Young losses.** The wiki has had each of these as separate threads; this is the one source that ties them together with proofs.
- **The Blondel research line on Fenchel-Young losses / sparsemax / smoothed max operators** is the unifying framing for action-distribution design across VLAs — relevant to the wiki's [VLA action-head taxonomy](../concepts/learning/vla-models.md) (autoregressive tokens vs DDPM vs flow matching), since all three are different choices on the same Fenchel-Young loss family.
- **Self-described draft** — book is open for typo + suggestion contributions; expect a v4+ in 2026. Re-check before deep citation.

## Open questions

- **Companion GitHub repo** — book says "Python source code on github" but the URL wasn't extracted from page 17 in this ingest pass. If user wants to use the code, fetch the link from the published PDF directly.
- **Coverage gaps** — book does not appear to cover **JEPA**-style joint-embedding losses, world-model architectures, or reinforcement learning end-to-end (RL covered only at the gradient-estimator level via ch. 12.3). For RL coverage, [Sutton & Barto](sutton-barto-rl-textbook.md) remains the canonical reference.
- **Worked exercises / problems** — TOC doesn't surface an exercise section; structure looks more reference than course. (Welch Labs Vol I is the closer course-style companion.)
