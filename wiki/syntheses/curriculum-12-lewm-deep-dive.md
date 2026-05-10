---
title: Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-12, leworldmodel, lewm, sigreg, jepa, latent-prediction, mpc, normality-test, epps-pulley, cramer-wold]
prereqs: [curriculum-04, curriculum-10, curriculum-11]
status: draft
---

> [!note] Curriculum context
> This is **Module 12** of the [Robot-learning curriculum](robot-learning-curriculum.md) — the **destination**. It assumes [Module 4](robot-learning-curriculum.md) (SSL + collapse), [Module 10](curriculum-10-world-models.md) (the four-family WM taxonomy + planning vocabulary), and [Module 11](curriculum-11-jepa-deep.md) (JEPA depth + the collapse-prevention zoo).
>
> Module 12 takes the [LeWM paper](../sources/leworldmodel-paper.md) section by section, with the **full SIGReg derivation** as the mathematical centerpiece. The point is to be able to read the LeWM paper end to end, evaluate every design choice quantitatively, and reproduce the PushT result yourself ([howto](leworldmodel-howto.md), [hello-world scope](lewm-hello-world-project-scope.md)).
>
> Acronyms used here are also in the [Glossary](../glossary.md). First-mention links go there.
>
> > [!warning] Correction from the curriculum outline
> > The curriculum hub and glossary previously described SIGReg's normality test as "Anderson-Darling-style." The paper actually uses the **Epps–Pulley** test statistic. This module uses the correct name throughout; the hub and glossary have been updated accordingly.

## What this module is

The end-to-end deep-dive on [LeWorldModel](../entities/leworldmodel.md) (Maes, Le Lidec, Scieur, LeCun, Balestriero — Mila / NYU / Samsung SAIL / Brown — March 2026). Six sections:

1. The two-loss architecture (encoder + AR predictor + `L = L_pred + λ · SIGReg`).
2. **The full SIGReg derivation** — random projections, the Epps–Pulley test, the Cramér–Wold justification, backprop through the test statistic.
3. Architecture details — including the **BN-after-CLS-token trick** that's load-bearing for SIGReg's optimizability.
4. Latent planning — CEM-MPC with goal-matching cost.
5. Empirical results across four environments — PushT, Reacher, OGBench-Cube, Two-Room — including the **Two-Room failure case** that exposes a SIGReg limitation.
6. Latent-space analysis — physical-quantity probing, latent decoding (despite no reconstruction in training), temporal path straightening, and the violation-of-expectation framework.

By the end of the module you should be able to:

1. Write the LeWM total loss from memory: `L = L_pred + λ · SIGReg(Z)`, including what `Z` is, what `L_pred` regresses against, and what SIGReg does.
2. Derive the SIGReg formulation given just the goals: "match an isotropic Gaussian; make it cheap; make it differentiable."
3. State the Cramér–Wold theorem in one sentence and explain why it makes random-projection-based normality testing rigorous rather than a hack.
4. Evaluate each LeWM design choice (no EMA, no stop-gradient, no frozen encoder, no reward, end-to-end ViT-tiny, AdaLN-zero-init, BN-after-CLS) as a *contestable bet* against a specific alternative from Module 11.
5. Reproduce the PushT result by following the [howto](leworldmodel-howto.md) and [hello-world scope](lewm-hello-world-project-scope.md), and predict the result on a held-out task using the four-environment patterns in §5.
6. Read the LeWM ablation tables and articulate which design choice each row tests.

## 1. The two-loss architecture

LeWM's training pipeline ([source](../sources/leworldmodel-paper.md), Fig. 1):

```
o_t  ─── encoder θ ───▶  z_t                                  // current observation embedding
o_{t+1} ─ encoder θ ───▶ z_{t+1}                              // SAME encoder applied to next frame
(z_t, a_t) ── predictor φ ──▶ ẑ_{t+1}                         // predict next embedding from current + action
L_pred  =  ‖ẑ_{t+1} − z_{t+1}‖²                               // (1) prediction loss
SIGReg(Z) = (1/M) Σ_m T(h^(m)),  h^(m) = Z u^(m)              // (2) anti-collapse regularizer
L_LeWM   =  L_pred  +  λ · SIGReg(Z)                          // total
```

Three things to notice:

- **One encoder, both sides.** Same `enc_θ` produces both `z_t` (input) and `z_{t+1}` (target). This is the joint-embedding commitment from [Module 11](curriculum-11-jepa-deep.md).
- **No EMA, no stop-gradient, no frozen encoder.** Gradients flow through *everything*, all parameters are optimized jointly. This is what makes the LeWM contribution methodologically interesting — every prior end-to-end JEPA needed at least one of these tricks.
- **Two terms, one regularization weight.** `λ` is the only effective hyperparameter. Default value: `λ = 0.1`. (The number of random projections `M = 1024` is a SIGReg-internal hyperparameter that empirically doesn't matter — see §2.5.)

This formulation is clean enough to fit in a 10-line PyTorch function (Algorithm 1 in the paper):

```python
def lewm_loss(obs, actions, lambd=0.1):
    """
    obs:     (B, T, C, H, W)  raw pixels
    actions: (B, T, A)        action sequence
    lambd:   SIGReg loss weight
    """
    emb       = encoder(obs)                   # (B, T, D)
    next_emb  = predictor(emb, actions)        # (B, T, D) — predicted next embedding
    pred_loss = F.mse_loss(emb[:, 1:], next_emb[:, :-1])
    sigreg    = SIGReg(emb.transpose(0, 1))    # treat history axis as data
    return pred_loss + lambd * sigreg
```

Everything Module 11 set up — the joint-embedding commitment, the collapse failure mode, the lineage of anti-collapse mechanisms — comes down to whether the `SIGReg` function on line 9 is a sufficient single anti-collapse mechanism. The next section walks through what `SIGReg` actually does.

## 2. SIGReg in detail

The mathematical heart of the paper. SIGReg = **Sketched Isotropic Gaussian Regularizer**, introduced by **[LeJEPA](../sources/lejepa-paper.md)** (Balestriero & LeCun 2025, arxiv 2511.08544; cited from the LeWM paper as ref [25]).

### 2.1 The goal

SIGReg's job: given a tensor of latent embeddings `Z ∈ ℝ^{N×B×d}` (history `N` × batch `B` × embedding dim `d`), enforce that the empirical distribution of `Z` matches an **isotropic Gaussian** `𝒩(0, I_d)`. If that constraint holds:

- The encoder *cannot* collapse to a constant — a constant has zero variance, far from a unit-variance Gaussian.
- The latent dimensions are decorrelated — covariance is the identity.
- The latent has a calibrated, predictable shape that the predictor can target reliably.

So far this is the same goal [VICReg](../glossary.md#vicreg) had with three loss terms or [Barlow Twins](../glossary.md#barlow-twins) had with one cross-correlation matrix term. The SIGReg innovation is **how** to enforce Gaussianity efficiently in high dimensions.

### 2.2 The high-dimensional normality problem

Direct multivariate normality testing in high dimensions is *hard*. Classical normality tests (Shapiro–Wilk, Anderson–Darling, Kolmogorov–Smirnov) are designed for **univariate** data. Their multivariate generalizations either don't exist, scale poorly, or have low power. So a multivariate normality test isn't a viable training-time loss.

SIGReg's move: **don't test multivariate normality directly. Test all 1-dimensional projections instead.**

### 2.3 The random-projection sketch

For `M` random unit-norm directions `u^(m) ∈ S^{d−1}` (uniform on the sphere), compute scalar projections:

```
h^(m) = Z u^(m)        ∈ ℝ^{N·B}
```

Each `h^(m)` is a 1D distribution that we can run a univariate normality test on. SIGReg averages the test statistics across the `M` projections:

```
SIGReg(Z) = (1/M) Σ_{m=1..M} T(h^(m))           (Eq. 2)
```

where `T(·)` is a univariate normality test statistic (more on which one in §2.4).

> [!note] Average vs max — practical vs formal
> The [LeJEPA paper](../sources/lejepa-paper.md) Theorem 2 actually defines the formally consistent statistic as the **max** over directions: `T_A = max_{a ∈ A} T({a^⊤ f_θ(x_n)})`. The paper's practical SIGReg (Definition 2) uses **average** instead — explicitly: "We replace the maximum over `a ∈ A` [...] by an average [...] to avoid sparse gradient over the directions in `A`." Max is the consistent statistic; average is the gradient-friendly approximation. Same kind of trade-off as VICReg's variance penalty.

**Why is this a sound anti-collapse signal, not just a heuristic?** This is where the Cramér–Wold theorem earns its keep.

### 2.4 The Cramér–Wold theorem (the legitimacy argument)

> **Cramér–Wold theorem.** Two `d`-dimensional probability distributions are equal *if and only if* every 1-dimensional projection of one matches the corresponding 1-dimensional projection of the other.

Equivalently: a multivariate distribution is **uniquely determined** by the set of all its 1D marginals along arbitrary directions.

This is the formal justification for SIGReg. To check whether `Z`'s distribution equals `𝒩(0, I_d)`, you don't need a multivariate test — you can check 1D marginals along a sufficiently rich set of directions. With *random* projections, you sample that set; with enough projections, you cover the sphere arbitrarily well.

What SIGReg loses by sketching: a finite-`M` random sample doesn't span the whole sphere, so SIGReg with `M` projections is an **unbiased estimator** of the (infinitely many) Cramér–Wold marginals. As `M → ∞` it converges to the full multivariate test. In practice `M = 1024` works (and is empirically insensitive — see §2.5).

> [!note] Why not just enforce zero mean and identity covariance?
> First-and-second-moment matching is what [VICReg](../glossary.md#vicreg) does (variance + covariance penalties). It prevents collapse to a constant and decorrelates dimensions, but it does **not** rule out non-Gaussian shapes (heavy tails, clusters, bimodality) that satisfy `𝔼[Z] = 0, Cov(Z) = I` while still being pathological. SIGReg targets the **full distributional shape**, not just first two moments. That's the theoretical upgrade.

### 2.5 The Epps–Pulley univariate normality test

LeWM uses the **Epps–Pulley** [38] test statistic for `T(·)`. (Note: the curriculum outline said "Anderson-Darling-style" — that was incorrect; Epps–Pulley is the actual test.)

The Epps–Pulley test compares the *empirical characteristic function* of the data to the characteristic function of `𝒩(0, 1)`:

```
T(h) = ∫_{−∞}^{∞} | φ̂_h(t) − e^(−t²/2) |² · w(t) dt
```

where:
- `φ̂_h(t) = (1/n) Σ_k exp(i · t · h_k)` is the empirical characteristic function of the 1D sample `h`.
- `e^(−t²/2)` is the characteristic function of `𝒩(0, 1)`.
- `w(t)` is a weighting function (typically Gaussian) that ensures the integral converges and emphasizes small `t` (where deviations are most informative).

The integral is computed numerically over a finite set of "integration knots" — a hyperparameter SIGReg also exposes but which is empirically insensitive (the paper notes both `M` and the number of knots can vary widely without affecting downstream performance).

**Why Epps–Pulley specifically?** [LeJEPA §4.2](../sources/lejepa-paper.md) walks through the alternatives explicitly and rules each out:

- **Smooth, differentiable.** The ECF is a sum of complex exponentials; its gradient is `(i · t / n) · exp(i · t · h_k)` — available via standard autodiff.
- **Bounded loss, gradient, *and curvature*.** Important practical property — second-order optimization tricks remain stable. Established in §4.2.3 of the paper.
- **Distributable via `all_reduce`.** The ECF is a simple average of complex exponentials, so it parallelizes across GPUs without synchronization barriers.
- **Tests the full distribution** — heavy tails, multi-modality, skewness all show up in the characteristic-function comparison.
- **Scales linearly** in sample size — `O(M · N)` total for `M` projections and `N` samples per batch.

The alternatives, ruled out one by one:

- **Moment-based tests (Jarque-Bera, extended JB)** — Theorem 3 of LeJEPA proves finite-`K` moment matching is non-identifying, but going to large `K` is unstable: gradient magnitude grows as `O(k)` and Monte-Carlo gradient variance grows as `O(k² · m_{2(k-1)})`. Stability and identifiability can't be achieved simultaneously.
- **CDF-based tests (Cramér–von Mises, Anderson-Darling, Watson)** — require sorting (rank statistics). Sorting *can* be `O(N log N)` (quicksort) but breaks the embarrassing parallelism of SGD on multi-GPU due to synchronization. Order statistics are also non-differentiable; smooth relaxations introduce more hyperparameters.
- **Kolmogorov-Smirnov** — uses `ℓ_∞` instead of `ℓ_2`, producing **sparse gradients** (the supremum is reached at a single point).
- **Shapiro-Wilk** — found unstable in practice (per LeJEPA §E).

Epps-Pulley is the rigorous answer: it's the only family that's smooth, parallelizable, and consistent.

### 2.6 Backprop through the test statistic

What "backprop through the test statistic" actually means:

```
gradient of T(h) w.r.t. h_k  =  ∂/∂h_k [ ∫ | φ̂_h(t) − e^(−t²/2) |² w(t) dt ]
```

Since `φ̂_h` is a sum of complex exponentials, its derivative w.r.t. each sample is straightforward:

```
∂φ̂_h(t) / ∂h_k  =  (i · t / n) · exp(i · t · h_k)
```

Plug this into the chain rule: `T(h)` becomes differentiable w.r.t. each sample `h_k`, and via `h_k = (Z u^(m))_k = Σ_d Z_{k,d} u^(m)_d`, gradients flow back through `Z` (and through the encoder that produced `Z`).

There's no special trick; it's just calculus. The reason this matters is that *most* statistical tests are not designed to be loss functions — they're designed to give you a p-value, which doesn't need to be differentiable. Epps–Pulley happens to be smooth enough that it can play the role of both.

### 2.7 SIGReg hyperparameters: only one matters

Two internal hyperparameters: `M` (number of random projections) and `K` (number of integration knots). The paper's ablations (Appendix G) report that **both are empirically insensitive** to performance over orders-of-magnitude variations. Default `M = 1024`, `K` ≈ 100 (paper-specific).

Plus the **regularization weight `λ`** — the only effective hyperparameter. Default `λ = 0.1`. Tuning `λ`:

- **Bisection search**, `O(log n)` complexity.
- Compare against **[PLDM](../entities/pldm.md)** ([source](../sources/pldm-paper.md)): ~6 hyperparameters → grid search complexity `O(n^6)`.

This complexity gap — `O(log n)` vs `O(n^6)` — is the LeWM contribution distilled to one number. In practice it means: tune SIGReg in 5 minutes; tune PLDM for a week.

### 2.8 The SIGReg in one sentence

**SIGReg = "match an isotropic Gaussian by projecting onto random directions and running the Epps–Pulley univariate normality test, justified by Cramér–Wold."**

Every word in that sentence corresponds to a specific design decision:
- *Isotropic Gaussian* — the target distribution; chosen for tractability and predictability.
- *Random directions* — the sketching strategy; arbitrarily good as `M → ∞`.
- *Epps–Pulley* — the test statistic; chosen for smoothness + full-distribution sensitivity.
- *Justified by Cramér–Wold* — the theoretical guarantee that a sufficient set of 1D marginals uniquely determines a `d`-D distribution.

If you can articulate why each of those four words is the right choice (or at least *a* defensible choice), you understand SIGReg.

## 3. Architecture details

The encoder + predictor pair, with one detail that's load-bearing.

### 3.1 The encoder — ViT-tiny + (BN after CLS, not LayerNorm)

- **Backbone.** Vision Transformer (ViT) tiny, ~5M parameters. 12 layers, 3 attention heads, hidden dim 192, patch size 14.
- **Pooling.** [CLS] token of the last transformer layer.
- **Projection.** 1-layer MLP **with Batch Normalization**.

The Batch Norm is not cosmetic. ViT's last layer typically applies **Layer Normalization** to its output. LayerNorm normalizes per-sample, which means the *distribution across the batch* is left invariant — but SIGReg operates on exactly that batch distribution. If the encoder ends in LayerNorm, SIGReg can't move the distribution; it's been pre-normalized away.

The fix: **strip LayerNorm at the end and add Batch Norm in the projection MLP instead.** BN normalizes per-feature *across the batch*, which leaves the per-sample structure SIGReg cares about while keeping the activations well-scaled. The paper explicitly notes that without this swap, SIGReg cannot be optimized.

This is the kind of detail that makes a difference between "the math says it should work" and "it actually works in code." It's the engineering complement to the SIGReg derivation.

### 3.2 The predictor — causal AR transformer with AdaLN action conditioning

- **Architecture.** 6-layer transformer, 16 attention heads, 10% dropout, ~10M parameters.
- **Action conditioning.** **Adaptive Layer Normalization (AdaLN)** at each layer, where the LayerNorm scale and shift parameters are themselves *predicted from the action `a_t`* by a small network. So action information modulates each transformer layer rather than being concatenated as input tokens.
- **Initialization.** **AdaLN parameters initialized to zero.** This means at the start of training, action conditioning has no effect; it phases in as the AdaLN MLP learns. Stabilizes early training.
- **Causality.** Temporal causal masking — the predictor can only attend to past frames. Multi-step rollouts are autoregressive.
- **Output projection.** Same BN-MLP projection as the encoder.

Total: encoder ~5M + predictor ~10M = **~15M parameters**. Trainable on a single GPU in a few hours. (Compare V-JEPA 2's 1B-parameter encoder + 300M-parameter predictor from [Module 11](curriculum-11-jepa-deep.md).)

### 3.3 Why the encoder is *small* — and where this helps and hurts

LeWM's encoder is two orders of magnitude smaller than V-JEPA 2's. The bet is that *for tasks where the training data is on-task* (PushT-class benchmarks), a small task-shaped encoder beats a large generic one. The Two-Room failure case in §5 will reveal a flip side: when the task is *too simple*, a Gaussian-prior in a 192-D space over-regularizes and the encoder under-fits the task structure.

## 4. Latent planning (CEM-MPC)

Module 10 set up MPC + CEM in general. LeWM's instantiation:

### 4.1 The cost function

Given current observation `o_1` and goal observation `o_g`, encode both:

```
ẑ_1 = enc_θ(o_1)
z_g = enc_θ(o_g)
```

Roll out the predictor for horizon `H` against a candidate action sequence `a_{1:H}`:

```
ẑ_{t+1} = pred_φ(ẑ_t, a_t)        for t = 1..H−1
```

Score the rollout by the **terminal latent goal-matching distance**:

```
C(ẑ_H) = ‖ẑ_H − z_g‖²            (Eq. 4)
```

Solve:

```
a*_{1:H} = argmin_{a_{1:H}} C(ẑ_H)    (Eq. 5)
```

### 4.2 The solver: CEM

[CEM](../glossary.md#cem) sampling-based optimization:

```
Initialize action distribution 𝒩(μ_0, Σ_0).
Repeat for K iterations:
  Sample n_samples action sequences from 𝒩(μ_k, Σ_k).
  Roll out the world model on each; compute C(ẑ_H).
  Keep the top-m elites (lowest cost).
  Refit 𝒩(μ_{k+1}, Σ_{k+1}) to the elite samples.
Return μ_K.
```

Then **execute the first `K_exec` actions** before re-encoding the new observation and replanning. This is standard MPC — the world model stays in the loop at runtime; planning is closed-loop.

### 4.3 The horizon tradeoff

[Module 10](curriculum-10-world-models.md) covered this in general; LeWM specifics:

- Auto-regressive rollouts accumulate prediction error as `H` grows — past the model's reliability horizon, more lookahead *hurts* because the rollouts diverge from reality.
- LeWM doesn't have a value function (no MBRL-style bootstrap), so the horizon is bounded entirely by the predictor's compounding-error budget.
- Empirically, the paper uses small `H` (~5–10 on the four environments tested). Details in Appendix D of the paper.

### 4.4 Why this is fast

The 48× speedup over DINO-WM ([generative-video vs JEPA synthesis](generative-video-vs-jepa-world-models.md), [LeWM paper](../sources/leworldmodel-paper.md) Fig. 3) decomposes into:

- **~200× fewer tokens per encoded observation** vs DINO-WM (LeWM uses [CLS]; DINO-WM uses dense per-patch features).
- Therefore each rollout step is much cheaper.
- CEM samples many candidate trajectories per cycle, so the per-step speedup multiplies through.

Concrete number: LeWM full planning ≈ **0.98s**; DINO-WM ≈ **47s** on the same task with the same compute budget. That gap is what makes LeWM-class JEPAs viable for closed-loop control on real robots without datacenter-scale GPUs.

## 5. Empirical results

Four environments, comparison against PLDM (end-to-end JEPA), DINO-WM (frozen-feature), GCBC (goal-conditioned BC), GCIVL/GCIQL (goal-conditioned offline RL), Random (lower bound).

### 5.1 The four environments

- **PushT** — 2D T-block pushing. Fully covered in [Module 6](curriculum-06-imitation-learning.md), [Module 7](curriculum-07-bc-lineage-pusht.md), and the [PushT entity](../entities/pusht.md).
- **OGBench-Cube** — 3D manipulation: a robotic arm interacts with a cube to reach a target position. Visually richer than PushT.
- **Two-Room** — 2D navigation between two rooms. Simple. (This is the failure case — see below.)
- **Reacher** — 2-joint arm reaches a target in 2D plane.

### 5.2 The headline results table

(Success rate %, from Fig. 6 of the paper; Random as baseline.)

| Environment | LeWM | DINO-WM (with prop) | DINO-WM | PLDM | GCBC | GCIQL | GCIVL | Random |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **PushT** | **96** | 92 | 74 | 78 | 75 | 20 | 33 | 2 |
| **Reacher** | **86** | — | 79 | 78 | — | — | — | 10 |
| **OGBench-Cube** | 74 | — | **86** | 84 | 64 | 56 | 48 | 2 |
| **Two-Room** | 87 | **100** | 100 | 97 | 100 | 100 | 100 | 0 |

**The pattern.**

- **LeWM wins outright on PushT and Reacher** — the canonical 2D continuous-control benchmarks. On PushT, LeWM with pixels-only beats DINO-WM *with privileged proprioceptive input*.
- **DINO-WM beats LeWM on OGBench-Cube** by 12 points. The paper attributes this to "higher visual complexity and the 3D nature of the environment, which makes encoder training more challenging." DINO-WM's pretrained encoder has the headroom to handle 3D scenes that a tiny end-to-end ViT doesn't.
- **DINO-WM, PLDM, and even goal-conditioned BC all beat LeWM on Two-Room** by 10–13 points. This is the SIGReg failure case.

### 5.3 The Two-Room failure case (a SIGReg limitation)

Two-Room is the simplest of the four environments — low intrinsic dimensionality, low task complexity. The paper's hypothesis (page 8):

> "The low diversity and low intrinsic dimensionality of this dataset make it difficult for the encoder to match the isotropic Gaussian prior enforced by SIGReg in a high-dimensional latent space, which may lead to a less structured latent representation."

In other words: **when the world is simpler than the latent**, Gaussianizing the latent over-regularizes. The encoder is forced to spread information across a 192-D Gaussian when 5–10 dimensions would suffice; the predictor has to model dynamics through a representation that's been smoothed out for collapse-prevention reasons that don't apply at this scale of complexity.

This is a real limitation of SIGReg and worth knowing. LeWM is not a uniformly-best world model — it's a **best-on-tasks-rich-enough-to-justify-the-isotropic-Gaussian-prior** world model.

### 5.4 The 48× planning speedup

(From Fig. 3 of the paper.) On PushT under fixed compute:

- LeWM full planning: **0.98s**
- DINO-WM full planning: **47s**

Planning success rates (under fixed FLOPs, not just fixed wall-clock):

- **PushT:** LeWM 90%, DINO-WM 13%.
- **OGBench-Cube:** LeWM 74%, DINO-WM 48%.

This is a strong "compute-matched" comparison. Even when DINO-WM is given the same FLOP budget as LeWM, LeWM wins on the tasks it wins on. The 48× factor isn't free — it represents a real algorithmic difference (LeWM uses ~200× fewer tokens per observation), not just better implementation.

### 5.5 Ablations (key takeaways from §4.3)

- **`M` (number of SIGReg projections) and `K` (integration knots): largely insensitive.** Performance is stable across orders of magnitude. Confirms the claim that `λ` is the only hyperparameter that requires tuning.
- **Embedding dimension `d`: a threshold effect.** Performance is weak when `d` is too small; saturates above a threshold. The default 192 is comfortably in the saturation regime for the four environments tested.
- **Encoder architecture: agnostic.** Replacing the ViT with a ResNet-18 produces competitive results. The recipe is not architecture-specific.
- **Training-curve smoothness.** LeWM's two-term loss exhibits smooth, monotonic convergence — pred-loss decreases steadily while SIGReg drops sharply early then plateaus. PLDM's seven-term loss is much noisier (Fig. 19).

## 6. Latent-space analysis

The paper's most pedagogically interesting set of experiments — they look beyond "does it succeed at planning?" to "what does the latent space *contain*?"

### 6.1 Physical-quantity probing

Train a probe (linear or MLP) to predict ground-truth physical quantities from a single LeWM embedding. (No fine-tuning of the encoder; just a probe.) Results on PushT (Table 1):

| Quantity | LeWM (linear MSE / `r`) | PLDM | DINO-WM |
| --- | --- | --- | --- |
| Agent Location | **0.052 / 0.974** | 0.090 / 0.955 | 1.888 / 0.977 |
| Block Location | 0.029 / 0.986 | 0.122 / 0.938 | **0.006 / 0.997** |
| Block Angle | 0.187 / 0.902 | 0.446 / 0.745 | **0.050 / 0.979** |

**Reading.** LeWM consistently beats PLDM (the other end-to-end JEPA) by a large margin. LeWM is competitive with DINO-WM on agent location, but DINO-WM wins on block location and block angle. The paper's gloss: DINOv2's pretraining (~124M images) gives it physical-property primitives "for free" that a 15M-parameter task-specific model can't match. The end-to-end vs frozen-feature tradeoff again.

### 6.2 Latent decoding (despite no reconstruction in training)

Train a decoder *after the fact* to reconstruct pixels from a single 192-D LeWM embedding. **Reconstruction is never used during training** — the decoder is a probe. The result (Fig. 8 of the paper): the decoder produces recognizable scene reconstructions.

This is non-trivial. It implies the 192-D LeWM latent retains enough information to reconstruct the visual scene, even though the training objective was *not* "encode enough to reconstruct." It's encoded enough to *predict* the future — and that turns out to be roughly the same information.

### 6.3 t-SNE visualization

A t-SNE of the latent space on PushT (Fig. 9) shows neighborhood relationships and relative positions are preserved. The latent is spatially structured.

### 6.4 Temporal latent path straightening (an emergent property)

Inspired by the *temporal straightening hypothesis* from neuroscience (visual cortex is hypothesized to "straighten" temporal trajectories — make consecutive percepts more linearly related). The paper measures cosine similarity between consecutive latent velocity vectors during training.

**Finding:** LeWM's latent trajectories become **increasingly straight on PushT over training**, as a *purely emergent phenomenon* — no explicit regularization encourages this. Notably, LeWM achieves *higher* temporal straightness than PLDM, despite PLDM having a dedicated temporal smoothness term in its loss.

This is an intriguing data point: the LeWM latent picks up properties that other latent-prediction models *try to enforce* without enforcing them. The paper hedges on whether this is a feature or a bug, but it's at least suggestive that the SIGReg-induced isotropic-Gaussian latent is "well-shaped" in ways that go beyond just preventing collapse.

### 6.5 The violation-of-expectation framework

Inspired by developmental psychology's VoE paradigm — show an agent a physically plausible event and an implausible event, measure whether it "expected" the plausible one more.

LeWM's surprise = discrepancy between the predictor's `ẑ_{t+1}` and the encoder's `z_{t+1}` (i.e., how far off the prediction is). The paper reports that LeWM assigns **higher surprise to physically implausible events** (e.g., objects that pass through walls in the bench environments) than to plausible ones. This is the model "having physics" in a measurable sense beyond just task success.

(I'm summarizing here; the VoE evaluation is on later pages of the paper. Read those if you want the exact protocol — the takeaway for this module is "the latent encodes enough physics to detect when physics is violated.")

## 7. Putting it together — what this means for the JEPA program

LeWM is a **proof of concept for the simplest possible end-to-end JEPA**:

- One encoder, no EMA, no stop-gradient, no frozen features, no auxiliary supervision.
- Two loss terms — prediction + SIGReg.
- One regularization weight to tune.
- A formal anti-collapse guarantee (Cramér–Wold + Epps–Pulley).
- 15M parameters, single-GPU training in hours.
- Wins on 2D continuous-control benchmarks; loses on 3D-rich environments (where DINO-WM's pretrained encoder helps) and on too-simple environments (where the Gaussian prior over-regularizes).

**The contribution is methodological, not scaling.** LeWM doesn't beat V-JEPA 2 at scale — it doesn't even try. It says "if you want a small task-specific JEPA that you can train on a single GPU and reason about formally, here's a recipe with one knob."

**The bridge to the rest of the JEPA program.** The Module 11 collapse-prevention zoo had six families of fixes. SIGReg replaces all of them. If SIGReg holds up under scaling — if a V-JEPA-2-scale model can train with just SIGReg and get the same results — then a future generation of JEPAs may be much simpler. That's a research bet, not a settled fact, but it's what makes the LeWM contribution interesting beyond the four-environment benchmark.

**The bridge to home robotics ([Module 13](robot-learning-curriculum.md)).** A 15M-param JEPA trainable on a single GPU is *the* size class plausibly deployable on consumer robotics hardware. V-JEPA 2 at 1B params is a research demonstration; LeWM is a candidate for actual on-robot inference. Module 13 returns to this; the [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md) and [LeWM-on-ROSOrin-Pro feasibility](lewm-on-rosorin-pro-feasibility.md) syntheses are the concrete artifacts.

## Anchor exercise

Two parts.

### Part A — Reproduce the LeWM PushT result

Follow the [LeWM howto](leworldmodel-howto.md) and the [hello-world scope](lewm-hello-world-project-scope.md). Concretely:

1. Clone [`lucas-maes/le-wm`](https://github.com/lucas-maes/le-wm).
2. Install `stable-worldmodel`, download the PushT dataset, train LeWM on a single GPU for a few hours.
3. Evaluate planning success rate on the held-out test set. Expect ≈90% if training converges; 96% per the paper if you replicate well.
4. Also pull the `quentinll/lewm-pusht` HuggingFace pretrained checkpoint and verify your reproduction matches.

If you only have time for one experiment in the entire curriculum, this is the experiment.

### Part B — Derive the SIGReg gradient on paper

1. Write the Epps–Pulley test statistic `T(h)` as an explicit integral (§2.5 above).
2. Compute `∂T/∂h_k` by hand. Use the chain rule through `φ̂_h(t)`.
3. Continue the chain rule back through `h^(m) = Z u^(m)` to get `∂T/∂Z_{k,d}`.
4. Verify your derivation produces a smooth gradient (no discontinuities, no quantile-based weights). This is what makes Epps–Pulley usable as a loss; AD or KS would not be.

If your derivation comes out clean, you understand SIGReg. If it doesn't, you've found either a real subtlety in the paper or a bug in your derivation — both are educational.

## Recommended reading

1. **[LeWM paper](../sources/leworldmodel-paper.md)** — the primary source. By the time you reach Module 12, this should be readable end-to-end. Take notes on each section against the corresponding Module 12 section above; flag anywhere the paper says something Module 12 didn't.
2. **[LeWM GitHub](../sources/lewm-github.md)** — the code. Walk through the SIGReg implementation; it's one of the cleanest references for the math you derived in Anchor Part B.
3. **[V-JEPA 2 GitHub](../sources/vjepa2-github.md)** — counterpoint. Read alongside the LeWM code to feel the difference in architectural commitment and engineering complexity (V-JEPA 2 has the EMA target, the masking, the dense-feature loss, etc.).
4. **Balestriero 2025 (the SIGReg paper itself)** — referenced as [25] in the LeWM paper. Not yet in the wiki as a separate source page but worth chasing if the math here didn't quite click.
5. **[Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md)** — re-read for the cross-paradigm framing that LeWM lives inside.
6. **[LeWM hello world — Project 1 detailed scope](lewm-hello-world-project-scope.md)** — the experiment plan to actually run.

## What you should now be able to do

- Read the LeWM paper end-to-end and explain every design choice as a contestable bet against the alternatives covered in Modules 10 and 11.
- Derive SIGReg's gradient on paper and identify the role of Cramér–Wold (justification) vs Epps–Pulley (smoothness + full-distribution sensitivity) vs random projections (sketching strategy).
- Predict LeWM's behavior on a new task by checking whether the task is rich enough to need a 192-D Gaussian latent (or simpler than that, in which case expect a Two-Room-style under-performance).
- Reproduce the PushT result yourself, and explain to a colleague why the result requires the BN-after-CLS engineering trick alongside the SIGReg math.
- Read a future paper that cites LeWM and immediately classify whether it's *building on* SIGReg (extending the regularizer, using it on new architectures) or *responding to* SIGReg (proposing a different anti-collapse mechanism).

## Hand-off to Modules 13 + 14

Module 12 is the algorithmic destination. Modules 13 and 14 are the **deployment** destination.

- **[Module 13](robot-learning-curriculum.md) — Home robotics deployment.** Where do all these techniques actually land in real homes? The [assistive-robotics R&D landscape](assistive-robotics-research-landscape.md) synthesis is the curriculum-shaped answer; Module 13 turns it into pedagogy. The 89.4% RLBench vs 12.4% BEHAVIOR-1K gap is the headline; LeWM-class techniques are one (partial) tool to close it.
- **[Module 14](robot-learning-curriculum.md) — Capstone.** Phase A: paper / sim-only — reproduce LeWM PushT (this module's anchor exercise) plus an experiment-design memo for the smallest credible LeWM-on-Stretch or DINO-WM-on-Stretch experiment. Phase B (gated on hardware): execute the memo on a real Stretch.

## Related curriculum modules

- **[Module 4](robot-learning-curriculum.md) — SSL + collapse** — collapse as a general failure mode; this module's SIGReg is the LeWM-specific solution.
- **[Module 5](robot-learning-curriculum.md) — Generative models / DDPM** — the *opposite* paradigm in the four-family taxonomy.
- **[Module 7](curriculum-07-bc-lineage-pusht.md) — BC lineage on PushT** — the policy-learning side; LeWM's MPC-against-the-WM is the alternative.
- **[Module 10](curriculum-10-world-models.md) — World models, broad** — the four-family taxonomy LeWM lives inside.
- **[Module 11](curriculum-11-jepa-deep.md) — JEPA in depth** — direct prerequisite; the collapse-prevention zoo SIGReg replaces.
- **[Module 13](robot-learning-curriculum.md) — Home robotics** — successor; deployment reality.
- **[Module 14](robot-learning-curriculum.md) — Capstone** — successor; reproduce LeWM PushT + write the experiment memo.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- ~~**LeJEPA paper** as a separate source page~~ — Filed: [LeJEPA Paper](../sources/lejepa-paper.md) (2026-05-10). The SIGReg derivation in this module references the LeWM paper's exposition; the LeJEPA paper itself is now linked for direct math reference.
- ~~**PLDM source page.**~~ Filed: [PLDM Paper](../sources/pldm-paper.md) + [PLDM entity](../entities/pldm.md) (2026-05-10). The "6 hyperparameters → 1" comparison is now backed by primary source.
- **Epps–Pulley original paper (1983)** — for completeness on the test statistic; low priority since the curriculum's needs are well-served by the LeWM paper's cite.
- **Cramér–Wold (1936)** — historical citation; unlikely to be useful as a wiki source page.
- **A worked SIGReg PyTorch reference** — could be a separate page if the GitHub implementation diverges from the paper's pseudocode in ways that matter pedagogically.
- **Two-Room failure-case quantification.** The paper hedges that "this may be a SIGReg limitation in low-complexity environments." It would be interesting to know at what intrinsic-dimensionality threshold the failure starts. No published number; could be a curriculum project.
- **Scaling SIGReg.** If SIGReg holds at V-JEPA-2 scale (1B-param encoder), is the result a strictly simpler V-JEPA? The paper doesn't claim this; it's the obvious follow-on.
