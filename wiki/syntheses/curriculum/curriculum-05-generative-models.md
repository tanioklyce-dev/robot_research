---
title: Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-5, generative-models, ddpm, diffusion, vae, elbo, kl-divergence, score-matching, classifier-free-guidance, ho-2020]
prereqs: [curriculum-01, curriculum-02, curriculum-03]
status: draft
---

> [!note] Curriculum context
> This is **Module 5** of the [Robot-learning curriculum](robot-learning-curriculum.md). Tier 2 — sole module. Builds on Tier 1 (NN basics, CNNs, attention) and is the prerequisite for [Module 7](curriculum-07-bc-lineage-pusht.md)'s Diffusion Policy section. Per the curriculum's resolved decision (2026-05-10), Module 5 goes **deep on DDPM math** — full ELBO derivation, KL decomposition, the ε-parameterization, the simplified loss, and classifier-free guidance.
>
> This is the longest module in the curriculum. If you already know DDPMs, skim — your time is better spent in Modules 6–12. If you don't, plan **2–4 evenings** to work through the math with pen and paper.
>
> Acronyms used here are also in the [Glossary](../../glossary.md). First-mention links go there.

## What this module is

A self-contained derivation of **denoising diffusion probabilistic models** (DDPM) starting from variational autoencoders, with all the math that was hand-waved in [Module 7](curriculum-07-bc-lineage-pusht.md)'s Diffusion Policy section explicitly worked out. We touch autoencoders → VAEs → energy-based models → score matching → DDPM → DDIM → classifier-free guidance.

By the end you should be able to:

1. Write the DDPM forward and reverse processes from memory, including the closed-form `q(x_t | x_0)` reparameterization.
2. Derive the simplified loss `L_simple = 𝔼[‖ε − ε_θ(x_t, t)‖²]` from the variational lower bound on `log p(x_0)`. Show every step. **Module 12's anchor exercise asks for this.**
3. Explain *why* the constant prefactor in front of the per-step KL is dropped in the simplified loss, and what that costs in terms of the bound.
4. Derive **classifier-free guidance** from Bayes' rule on the score function and translate the result back into the ε-parameterization.
5. Place DDPM, VAE, EBM, score matching, and GAN on a single design-space axis (what they predict, what loss they use, what they're good at).
6. Explain why DDPM matters for [Module 7](curriculum-07-bc-lineage-pusht.md) (Diffusion Policy = conditional DDPM over action chunks) and for [Module 10](curriculum-10-world-models.md) (generative-video world models like [NVIDIA Cosmos](../../entities/nvidia-cosmos.md) are large conditional diffusion models in pixel space).

## §1 — Generative modeling primer

Three sentence-length definitions before we dive into DDPM.

### Autoencoder ([AE](../../glossary.md#ae))

Encoder `g_φ: 𝒳 → 𝒵`, decoder `d_ψ: 𝒵 → 𝒳`. Loss: `L = ‖x − d_ψ(g_φ(x))‖²`. Learns a compressed representation `z = g_φ(x)` such that `x` is roughly recoverable. **Not a generative model on its own** — it has no prior over `𝒵`, so you can't sample new `x`.

### Variational Autoencoder ([VAE](../../glossary.md#vae))

Kingma & Welling 2013. The minimal-modification fix that makes an AE generative:

- Encoder produces a *distribution* `q_φ(z | x) = 𝒩(μ_φ(x), σ²_φ(x))` instead of a point.
- Prior `p(z) = 𝒩(0, I)` over `𝒵`.
- Decoder: `p_ψ(x | z)` (often Gaussian or Bernoulli).
- Loss = **negative ELBO** (evidence lower bound):

```
−log p(x)  ≤  𝔼_{q_φ(z|x)} [−log p_ψ(x | z)]  +  D_KL( q_φ(z | x) ‖ p(z) )
                 ↑ reconstruction term            ↑ regularizer to prior
```

To sample: draw `z ~ p(z)`, decode `x ~ p_ψ(x | z)`. The ELBO is the central tool here, and it's the same tool DDPM uses (we'll re-derive it for diffusion in §4).

**Why VAEs aren't enough.** Sample quality is mediocre — the Gaussian-output decoder produces blurry images. Forcing a single-step `z → x` decoder to be both flexible and well-regularized is hard. Diffusion's move: replace one big decoding step with many small denoising steps.

### Energy-Based Model ([EBM](../../glossary.md#ebm))

Define a scalar **energy** `E_θ: 𝒳 → ℝ`; declare the implied probability `p_θ(x) ∝ exp(−E_θ(x))`. Train so that data has low energy and non-data has high energy.

You don't need EBMs in detail for diffusion — but [Module 7](curriculum-07-bc-lineage-pusht.md) covers EBMs in the [IBC](../../entities/ibc.md) (Implicit Behavior Cloning) section, where the policy `π(a | s)` is defined as `argmin_a E_θ(s, a)`. So: DDPM and EBM are siblings — both side-step the explicit-density issue, but in different ways. DDPM defines a forward noising chain and learns to invert it; EBM defines an energy and samples via MCMC.

### Score matching (Song & Ermon, NeurIPS 2019)

The score function `s(x) = ∇_x log p(x)` is the gradient of log-density w.r.t. the input. If you know the score, you can sample via Langevin dynamics:

```
x ← x + (η/2) · s(x) + √η · ξ,    ξ ~ 𝒩(0, I).
```

Score matching is the parallel theoretical foundation of diffusion: DDPM can be re-derived as **denoising score matching**, with the key identity that the score of the noisy distribution `q(x_t | x_0)` is proportional to the noise `ε`. This is why DDPM's "predict the noise" parameterization works — predicting noise *is* predicting score, up to a sign and a scale. We won't formalize this here; it's a parallel derivation that arrives at the same algorithm.

> [!note] Family map
> **VAE:** explicit density via amortized variational inference; one big decoder.
> **EBM:** unnormalized density via energy function; sample via MCMC.
> **Score matching:** learn `∇ log p(x)`; sample via Langevin.
> **DDPM:** learn to denoise a Markov noising chain; sample by iterated denoising.
> **GAN:** implicit density via adversarial training; one-shot generator.
>
> In 2024–2026, **DDPM is the dominant paradigm** for high-quality generative modeling across modalities. GANs are largely superseded for unconditional image generation; VAEs survive as components inside latent-diffusion stacks (Stable Diffusion is "VAE encoder + DDPM in latent space").

## §2 — DDPM forward process

Setup: `x_0 ~ q(x_0)` is the data distribution. Define a Markov chain that gradually adds Gaussian noise over `T` steps until `x_T ≈ 𝒩(0, I)`.

### The single-step transition

```
q(x_t | x_{t−1})  =  𝒩( x_t ;  √(1 − β_t) · x_{t−1} ,  β_t · I )
```

where `β_1, β_2, …, β_T ∈ (0, 1)` is a fixed **noise schedule**. Each step takes a small step toward zero-mean noise: `x_{t−1}` is multiplied by `√(1 − β_t)` (slight contraction), and Gaussian noise of variance `β_t` is added.

### The full chain

```
q(x_{1:T} | x_0)  =  ∏_{t=1}^T  q(x_t | x_{t−1})
```

### The closed-form marginal `q(x_t | x_0)`

This is the **key technical trick** that makes DDPM trainable. Define:

```
α_t  ≜  1 − β_t            (per-step retention)
ᾱ_t  ≜  ∏_{s=1}^t α_s       (cumulative retention)
```

Then by induction (using the Gaussian convolution identity):

```
q(x_t | x_0)  =  𝒩( x_t ;  √ᾱ_t · x_0 ,  (1 − ᾱ_t) · I )       (Eq. 2.1)
```

Equivalently, by the reparameterization trick:

```
x_t  =  √ᾱ_t · x_0  +  √(1 − ᾱ_t) · ε ,    ε ~ 𝒩(0, I)        (Eq. 2.2)
```

This is huge. To sample `x_t` for any `t`, you don't need to roll out `t` steps — you compute it in **one shot** from `x_0` and a single Gaussian noise sample. Training can sample a random `t` per training example, run forward in one step, and learn to invert it.

### Why this matters

The closed-form marginal is what differentiates diffusion from VAE: rather than committing to a single `z` per `x_0` (VAE's `q_φ(z | x)`), the diffusion forward process gives you `T` different noised versions of the same `x_0`, each at a known noise level. The model learns to denoise *all* of them — a much richer training signal than VAE's one-shot encode-decode.

## §3 — DDPM reverse process

The reverse process inverts the forward chain:

```
p_θ(x_{t−1} | x_t)  =  𝒩( x_{t−1} ;  μ_θ(x_t, t) ,  Σ_θ(x_t, t) )
```

where `μ_θ` and `Σ_θ` are neural networks (typically a single U-Net taking `(x_t, t)` as input and producing both, though Ho et al. fix `Σ_θ = σ_t² I` with `σ_t² = β_t` or `σ_t² = β̃_t` — see Eq. 4.4 below).

The **terminal prior** `p(x_T) = 𝒩(0, I)` matches the limit `q(x_T) ≈ 𝒩(0, I)` (assuming the schedule is long enough that ᾱ_T ≈ 0).

### The full generative model

```
p_θ(x_{0:T})  =  p(x_T)  ·  ∏_{t=1}^T  p_θ(x_{t−1} | x_t)
```

To sample: start with `x_T ~ 𝒩(0, I)`, iteratively sample `x_{t−1} ~ p_θ(x_{t−1} | x_t)` for `t = T, T−1, …, 1`. Final `x_0` is the generated sample.

The whole game is now: **learn `μ_θ(x_t, t)`** so that the implied `p_θ(x_{0:T})` is close to `q`, hence close to the data distribution.

## §4 — The variational lower bound (full ELBO derivation)

We can't compute `log p_θ(x_0)` directly (it requires marginalizing over all `T` noise paths). Standard variational trick: pick a tractable distribution over the noise path and bound the log-likelihood from below. The natural choice is `q(x_{1:T} | x_0)` from §2.

### The bound

By Jensen's inequality:

```
log p_θ(x_0)
   = log ∫ p_θ(x_{0:T}) dx_{1:T}
   = log 𝔼_{q(x_{1:T} | x_0)} [ p_θ(x_{0:T}) / q(x_{1:T} | x_0) ]
   ≥ 𝔼_q [ log p_θ(x_{0:T}) − log q(x_{1:T} | x_0) ]            (4.1)
```

Define `L_VLB ≜ −𝔼_q [ log p_θ(x_{0:T}) − log q(x_{1:T} | x_0) ]`. So `L_VLB` is an *upper* bound on `−log p_θ(x_0)`, i.e. a *negative* ELBO. We minimize `L_VLB`.

### Per-step decomposition

Substitute the factorizations:

```
log p_θ(x_{0:T})        = log p(x_T) + Σ_{t=1}^T log p_θ(x_{t−1} | x_t)
log q(x_{1:T} | x_0)    =              Σ_{t=1}^T log q(x_t | x_{t−1})
```

Then apply Bayes' rule to swap `q(x_t | x_{t−1})` for `q(x_{t−1} | x_t, x_0)`:

```
q(x_t | x_{t−1})  =  q(x_{t−1} | x_t, x_0) · q(x_t | x_0) / q(x_{t−1} | x_0)    (4.2)
```

After substituting (4.2) into the sum, telescoping the `q(x_t | x_0) / q(x_{t−1} | x_0)` ratios, and rearranging — this is the algebraic core of the derivation; do it once with pen and paper — we get:

```
L_VLB  =  𝔼_q [
            D_KL( q(x_T | x_0) ‖ p(x_T) )                               // L_T
          + Σ_{t=2}^T  D_KL( q(x_{t−1} | x_t, x_0) ‖ p_θ(x_{t−1} | x_t) )   // L_{t−1}
          − log p_θ(x_0 | x_1)                                          // L_0
          ]
                                                                          (4.3)
```

Three pieces:

- **`L_T`** — the KL between `q(x_T | x_0)` and the prior `p(x_T) = 𝒩(0, I)`. **No trainable parameters** (the forward process is fixed). For long enough `T` this is approximately zero. Drop it.
- **`L_{t−1}`** for `t = 2, …, T` — the per-step KL between the **forward posterior** `q(x_{t−1} | x_t, x_0)` and the model's reverse step `p_θ(x_{t−1} | x_t)`. **This is where all the training signal lives.**
- **`L_0`** — the reconstruction-like term at the final step. Often handled with a discrete decoder (Bernoulli for binary images, scaled-Gaussian for continuous). Small but non-zero.

The work is now to compute the per-step KL term `L_{t−1}`.

### The forward posterior `q(x_{t−1} | x_t, x_0)`

Bayes' rule gives:

```
q(x_{t−1} | x_t, x_0)  =  q(x_t | x_{t−1}) · q(x_{t−1} | x_0) / q(x_t | x_0)
```

All three densities on the right are Gaussian — so the posterior is Gaussian too. After completing the square (this is Appendix A of Ho et al. 2020; do it once on paper):

```
q(x_{t−1} | x_t, x_0)  =  𝒩( x_{t−1} ;  μ̃_t(x_t, x_0) ,  β̃_t · I )       (4.4)

μ̃_t(x_t, x_0)  =  ( √ᾱ_{t−1} · β_t / (1 − ᾱ_t) ) · x_0
                 +  ( √α_t · (1 − ᾱ_{t−1}) / (1 − ᾱ_t) ) · x_t

β̃_t  =  (1 − ᾱ_{t−1}) / (1 − ᾱ_t)  ·  β_t
```

The posterior mean `μ̃_t` is a **convex combination of `x_0` and `x_t`**, with weights determined by the schedule.

### KL between two Gaussians

The forward posterior `q(x_{t−1} | x_t, x_0)` and the reverse step `p_θ(x_{t−1} | x_t)` are both Gaussian. The KL between two `d`-dimensional Gaussians has closed form:

```
D_KL( 𝒩(μ_1, Σ_1) ‖ 𝒩(μ_2, Σ_2) )
   =  ½ [ tr(Σ_2^{−1} Σ_1)
         + (μ_2 − μ_1)^⊤ Σ_2^{−1} (μ_2 − μ_1)
         − d
         + log( det Σ_2 / det Σ_1 ) ]
```

If we fix `Σ_θ = σ_t² · I` (Ho et al.'s choice; `σ_t² = β_t` or `β̃_t`), then `Σ_2^{−1} Σ_1` is diagonal, the log-determinants cancel, and the cross-term is a scaled squared difference of means:

```
L_{t−1}  =  𝔼_q [ (1 / (2 σ_t²)) · ‖μ̃_t(x_t, x_0) − μ_θ(x_t, t)‖² ]  +  C    (4.5)
```

where `C` collects schedule-dependent constants that don't depend on `θ`.

This is a **Gaussian regression problem** at each step `t`: predict the posterior mean `μ̃_t(x_t, x_0)` from `(x_t, t)`. We're done in principle. But Ho et al.'s parameterization makes this much cleaner.

## §5 — From ELBO to the simplified ε-prediction loss

The conceptual breakthrough of the Ho et al. 2020 paper.

### Reparameterize `μ_θ` in terms of `ε_θ`

From Eq. 2.2: `x_t = √ᾱ_t · x_0 + √(1 − ᾱ_t) · ε`, equivalently `x_0 = (x_t − √(1 − ᾱ_t) · ε) / √ᾱ_t`.

Substitute this into `μ̃_t(x_t, x_0)` (Eq. 4.4) and simplify. After algebra:

```
μ̃_t(x_t, x_0)  =  (1 / √α_t) · [ x_t  −  (β_t / √(1 − ᾱ_t)) · ε ]      (5.1)
```

So the posterior mean is a **fixed function of `x_t` and `ε`**. Define the model's reverse mean to mirror this structure:

```
μ_θ(x_t, t)  =  (1 / √α_t) · [ x_t  −  (β_t / √(1 − ᾱ_t)) · ε_θ(x_t, t) ]   (5.2)
```

where `ε_θ(x_t, t)` is a neural network predicting the noise that was added.

### Substitute back into `L_{t−1}`

Plug (5.1) and (5.2) into (4.5). The `x_t` terms cancel, leaving only the `ε` vs `ε_θ` difference:

```
L_{t−1}
   =  𝔼_q [ (1 / (2 σ_t²)) · (1 / α_t) · (β_t² / (1 − ᾱ_t)) · ‖ε − ε_θ(x_t, t)‖² ]
   =  𝔼_q [ λ_t · ‖ε − ε_θ(x_t, t)‖² ]                                   (5.3)
```

where `λ_t = β_t² / (2 σ_t² α_t (1 − ᾱ_t))` is a per-step weight.

### The "simple" loss

Ho et al. observe empirically that **dropping the `λ_t` weight produces better samples** (despite making the bound looser):

```
L_simple  =  𝔼_{t, x_0, ε} [ ‖ε − ε_θ( √ᾱ_t · x_0 + √(1 − ᾱ_t) · ε ,  t )‖² ]   (5.4)
```

This is the **headline DDPM training objective**. It says: pick a random `x_0` from the data, pick a random `t ~ Uniform(1, T)`, sample fresh noise `ε ~ 𝒩(0, I)`, compute `x_t = √ᾱ_t · x_0 + √(1 − ᾱ_t) · ε`, run `ε_θ(x_t, t)` through the network, compute MSE against `ε`. Average over training.

### Why dropping `λ_t` works

The `λ_t` weights down-weight large-`t` (very noisy) steps and up-weight small-`t` (mostly-clean) steps, *because* the per-step posterior variance there is small and the bound is dominated by precise predictions. Dropping `λ_t` effectively **reweights training toward harder noise levels**, which empirically gives sharper samples. The cost: `L_simple` is no longer a tight ELBO; the model's likelihood is worse than a `λ_t`-weighted version would be. But likelihood and sample quality are not the same thing — Ho et al.'s key empirical insight.

> [!note] This is **exactly** Module 12's anchor exercise Part B
> Module 12 asks you to "derive the simplified loss `L_simple = 𝔼[‖ε − ε_θ(x_t, t)‖²]` from the ELBO on paper." That's §4 + §5 above, end to end. By Module 12 you should be able to do this without notes.

## §6 — Noise schedule

`β_t` controls how much noise is added at each step. The cumulative `ᾱ_t` controls the signal-to-noise ratio at step `t`. Two common schedules:

### Linear schedule (Ho et al. 2020)

```
β_1, β_2, …, β_T  linearly interpolated from β_1 = 10^{−4} to β_T = 0.02,  T = 1000
```

Simple and effective for image generation. But the linear schedule destroys signal too quickly near `t = T` — `ᾱ_T` is essentially zero by step ~700, and the last 300 steps add noise to already-noisy data.

### Cosine schedule (Nichol & Dhariwal 2021, [iDDPM](../../glossary.md#iddpm))

```
ᾱ_t  =  cos²( ((t/T + s) / (1 + s)) · π/2 )       (6.1)

with s = 0.008 a small offset to keep β_t bounded.
```

The cosine schedule destroys signal **gradually** — `ᾱ_t` decreases smoothly from 1 to 0 across the full schedule. Better samples at the same `T`, *and* allows reducing `T` (e.g., to 1000 → 100) without quality loss.

> [!note] What [Diffusion Policy](../../entities/diffusion-policy.md) uses
> Diffusion Policy adopts the cosine schedule from iDDPM. The original DDPM uses linear. Most modern diffusion models use cosine or a learned variant. See the [Diffusion Policy paper](../../sources/diffusion-policy-paper.md) §II for the explicit choice.

### Learned variances (iDDPM)

iDDPM also makes `Σ_θ` learnable (interpolated between `β_t · I` and `β̃_t · I`), which improves likelihood at small additional cost. We won't unpack this — the simple-fixed-variance version is the curriculum default.

## §7 — Sampling

Given a trained `ε_θ`, how do we generate?

### Ancestral sampling (DDPM, Ho et al. 2020)

Iterate `t = T, T−1, …, 1`:

```
ε ~ 𝒩(0, I)  if  t > 1  else  ε = 0
x_{t−1}  =  (1 / √α_t) · ( x_t  −  (β_t / √(1 − ᾱ_t)) · ε_θ(x_t, t) )  +  σ_t · ε
```

Start from `x_T ~ 𝒩(0, I)`. After `T` iterations you get `x_0`.

**Cost.** `T` forward passes through `ε_θ`. With `T = 1000`, this is slow.

### DDIM — deterministic faster sampling (Song, Meng, Ermon, ICLR 2021)

The key DDIM insight: the forward process `q(x_{1:T} | x_0)` doesn't have to be Markov. As long as the *marginals* `q(x_t | x_0)` match Eq. 2.1, the model trained with `L_simple` can be sampled with a **non-Markov reverse process** that has different (or zero) noise levels per step.

DDIM defines:

```
x_{t−1}  =  √ᾱ_{t−1} · x̂_0  +  √(1 − ᾱ_{t−1} − σ_t²) · ε_θ(x_t, t)  +  σ_t · ε

where  x̂_0  =  ( x_t  −  √(1 − ᾱ_t) · ε_θ(x_t, t) )  /  √ᾱ_t
```

Set `σ_t = 0` for fully deterministic sampling. The result: **samples in 10–50 steps instead of 1000**, with quality comparable to DDPM at full `T`. Diffusion Policy uses DDIM at inference (10 steps) for real-time control.

> [!note] DDIM is a separate paper but uses the same trained model
> A model trained with DDPM's `L_simple` can be sampled with DDIM at inference time. You don't retrain. This is the practical recipe everywhere in 2024–2026: train DDPM-style, sample DDIM-style.

## §8 — Classifier-free guidance (CFG, full derivation)

Ho & Salimans 2022. The dominant conditioning method for diffusion in 2024–2026.

### The setup

Given conditional information `c` (a class label, a text caption, an image, an action context), we want to sample from `p(x | c)` — a *conditional* distribution.

The naive approach: train `ε_θ(x_t, t, c)` directly on `(x_0, c)` pairs. This works but produces **weak conditioning** — the model treats `c` as a soft hint rather than a strong constraint.

CFG strengthens conditioning by extrapolating between conditional and unconditional models. It costs almost nothing at training and adds a single hyperparameter `s` (the guidance scale) at inference.

### Derivation via Bayes' rule on the score

Diffusion's `ε_θ(x_t, t)` is proportional to the negative score of `q(x_t)`:

```
ε_θ(x_t, t)  ≈  −√(1 − ᾱ_t) · ∇_{x_t} log q(x_t)        (8.1)
```

For the *conditional* score, by Bayes' rule:

```
∇_{x_t} log p(x_t | c)  =  ∇_{x_t} log p(x_t)  +  ∇_{x_t} log p(c | x_t)     (8.2)
```

We don't have `p(c | x_t)` — that would be a classifier. But we can solve for it:

```
∇_{x_t} log p(c | x_t)  =  ∇_{x_t} log p(x_t | c)  −  ∇_{x_t} log p(x_t)     (8.3)
```

Now define a **guided distribution** that amplifies the conditioning by a factor `s`:

```
log p̃_s(x_t | c)  ≜  log p(x_t)  +  s · log p(c | x_t)  +  const           (8.4)
```

Take the gradient and apply (8.3):

```
∇ log p̃_s(x_t | c)  =  ∇ log p(x_t)  +  s · [ ∇ log p(x_t | c)  −  ∇ log p(x_t) ]
                    =  (1 − s) · ∇ log p(x_t)  +  s · ∇ log p(x_t | c)        (8.5)
```

### Translate back to ε-parameterization

Using (8.1) and the conditional analogue `ε_θ(x_t, t, c) ≈ −√(1 − ᾱ_t) · ∇ log p(x_t | c)`:

```
ε̂_θ(x_t, t, c)  =  (1 − s) · ε_θ(x_t, t, ∅)  +  s · ε_θ(x_t, t, c)             (8.6)
                =  ε_θ(x_t, t, ∅)  +  s · [ ε_θ(x_t, t, c)  −  ε_θ(x_t, t, ∅) ]
```

where `∅` denotes the unconditional model (the conditioning is masked or replaced with a null token).

Setting `s = 1` recovers the standard conditional model. `s > 1` **extrapolates beyond** the conditional model in the direction of stronger adherence to `c`. Typical values: `s = 2` to `s = 7.5` for image generation. Diffusion Policy uses `s = 0` (no CFG) — the action distribution is conditioned directly on observations without amplification.

### Training: just one network, with random unconditioning

The clever practical trick: at training time, randomly replace `c` with `∅` (drop conditioning) with some probability `p_uncond ≈ 0.1`. The single model `ε_θ(x_t, t, c)` then learns *both* the conditional and unconditional distributions. At inference, run it twice (once with `c`, once with `∅`) and combine via (8.6).

> [!note] Why this is dominant
> CFG removes the need to train a separate classifier for guidance (the original "classifier guidance" approach by Dhariwal & Nichol 2021). Single network, single training run, controllable conditioning at inference. The `s` knob is intuitive: `s = 1` is "normal," `s > 1` is "more conditional," `s < 1` is "less conditional." Trade-off: high `s` produces sharper but less diverse samples.

## §9 — Conditional diffusion in general

CFG is one specific way to condition; the broader question is how to inject `c` into `ε_θ(x_t, t, c)`. Standard choices:

- **Concatenation** — append `c` to `x_t` along the channel dimension (works for image-to-image conditioning).
- **Cross-attention** — `c` is a sequence (e.g., text tokens); `x_t`'s feature maps attend to it. The Stable Diffusion / DALL-E recipe.
- **Adaptive normalization (AdaLN, AdaGN)** — normalize `x_t` then scale-and-shift with parameters predicted from `c`. The [LeWM](../../entities/leworldmodel.md) action-conditioning recipe (per [Module 12 §3.2](curriculum-12-lewm-deep-dive.md)).
- **Time-step + condition embedding addition** — embed `t` and `c` separately, sum, project, inject as a bias term throughout the U-Net.

Diffusion Policy uses **observation-feature concatenation** at the U-Net's hidden layers. See [Diffusion Policy paper](../../sources/diffusion-policy-paper.md) §III for the exact mechanism.

## §10 — Bridges

### To Module 6 (BC) and Module 7 (BC lineage on PushT)

[Module 7](curriculum-07-bc-lineage-pusht.md) covers [Diffusion Policy](../../entities/diffusion-policy.md) (Chi et al., RSS 2023) — a direct application of conditional DDPM to robot policy learning. The mapping:

| DDPM concept | Diffusion Policy instantiation |
| --- | --- |
| `x` (the variable being denoised) | **action chunk** `A_t = (a_t, a_{t+1}, …, a_{t+T_a−1})` |
| `c` (conditioning) | **observation history** `O_t` |
| `ε_θ(x_t, t, c)` (noise predictor) | observation-conditioned U-Net or transformer |
| Forward process | adds Gaussian noise to action chunks |
| Sampling | DDIM, 10 inference steps |
| Loss | exactly `L_simple` from §5 |

Diffusion Policy's contribution is *not* a new generative-modeling technique — it's the recognition that DDPM's multi-modal-distribution-modeling capability is exactly what BC needs to escape mode-averaging (the failure mode set up in [Module 6](curriculum-06-imitation-learning.md)).

### To Module 9 (VLA) — flow matching

[Module 9](curriculum-09-vla.md) covers [π0](../../entities/physical-intelligence.md), which uses **flow matching** instead of DDPM as its action head. Flow matching is a sibling of diffusion that learns a velocity field `v_θ(x_t, t)` such that integrating an ODE pushes a base distribution to the target. Same multi-modal-modeling capability, often faster sampling. The shared frame: both DDPM and flow matching are *generative models over actions*; the difference is the parameterization of the underlying transport map.

### To Module 10 (world models) — generative-video WMs

[NVIDIA Cosmos](../../entities/nvidia-cosmos.md) and [Genie Envisioner](../../entities/genie-envisioner.md) — the generative-video family from [Module 10](curriculum-10-world-models.md) §"Family 1" — are **giant conditional diffusion models in pixel space**. The conditioning `c` is an image + action history; the variable `x` is the next frame's pixels. Same DDPM math at scale.

This is the contrast point with [JEPA](../../entities/leworldmodel.md): JEPA-style WMs predict in **embedding space** and avoid ever generating pixels. Module 10 §"Generative-video vs JEPA" lays this out — and Module 12's "48× faster planning" claim for LeWM is essentially the cost of *not* running the giant diffusion U-Net at every MPC rollout step.

### To EBM (and IBC)

[Module 7](curriculum-07-bc-lineage-pusht.md)'s [IBC](../../entities/ibc.md) uses an **energy-based model** as the policy: `π(s) = argmin_a E_θ(s, a)`. EBM and DDPM are siblings — both finesse the explicit-density issue. EBM defines an unnormalized density and samples via MCMC (DFO, Langevin); DDPM defines a noising chain and learns to denoise.

Empirically, on PushT-class tasks, DDPM (Diffusion Policy) outperforms EBM (IBC) — see [Module 7 §"Diffusion Policy"](curriculum-07-bc-lineage-pusht.md). The DDPM advantage: stable training (no MCMC), direct gradient-based optimization, and a smooth multi-modal action distribution by construction.

## Anchor exercise

Two parts.

### Part A — Train a tiny DDPM on MNIST

1. Implement the forward process from Eq. 2.2 (closed-form `q(x_t | x_0)`).
2. A small CNN U-Net for `ε_θ(x_t, t)`. ~100k parameters is fine.
3. Train with `L_simple` (Eq. 5.4): random `t ~ Uniform(1, 1000)`, noise `ε ~ 𝒩(0, I)`, MSE loss. Linear schedule, `T = 1000`. ~30 minutes on a single GPU.
4. Sample with ancestral sampling (§7). You should get recognizable MNIST digits. Then sample with **DDIM**, `T_inference = 10` — confirm samples are still recognizable.

If you've never trained a generative model, this is the cleanest entry point. The Hugging Face [`diffusers`](https://github.com/huggingface/diffusers) library has reference implementations; a from-scratch implementation in ~200 lines is worth doing once.

### Part B — Derive `L_simple` from ELBO on paper

Re-derive (4.1) → (4.3) → (5.4). Show every step. This is **Module 12's anchor exercise Part B** and the prerequisite for fully understanding why "predict noise" is the right parameterization.

Specific things to make sure you can do:

1. Write the per-step decomposition (4.3) by hand, including the Bayes' rule swap (4.2) and the telescoping.
2. Compute the closed-form `q(x_{t−1} | x_t, x_0)` (Eq. 4.4) by completing the square on the product of three Gaussians.
3. Reparameterize `μ̃_t` in terms of `ε` (Eq. 5.1) using the closed-form `x_0 = (x_t − √(1 − ᾱ_t) ε) / √ᾱ_t`.
4. Substitute into the KL between two equal-variance Gaussians and recover Eq. 5.3.
5. Identify which term is dropped to go from Eq. 5.3 to `L_simple` (Eq. 5.4) and explain *why* dropping it improves sample quality despite making the bound loose.

If you can't do 1–5 fluently, your understanding of Module 12's SIGReg derivation will also be shaky — both rest on the same comfort with Gaussian KL closed forms and on completing the square. Spend the time here; it pays off in [Module 11](curriculum-11-jepa-deep.md) and [Module 12](curriculum-12-lewm-deep-dive.md).

## Recommended reading

In order:

1. **[DDPM Paper](../../sources/ddpm-paper.md)** — Ho, Jain, Abbeel (NeurIPS 2020). The primary source. Read §1 (intro), §2 (background — covers the diffusion / score-matching connection), §3 (the `L_simple` derivation), §4 (architecture). Skip §5 (experiments) on first pass.
2. **[Diffusion Policy paper](../../sources/diffusion-policy-paper.md)** §II — a compact, clean DDPM tutorial with the action-modeling adaptation. If Ho et al. is too dense, this is a friendlier entry point.
3. **iDDPM** (Nichol & Dhariwal, ICML 2021) — for the cosine schedule and learned variance; not yet a wiki source page.
4. **DDIM** (Song, Meng, Ermon, ICLR 2021, arxiv 2010.02502) — for the deterministic / faster sampling; not yet a wiki source page.
5. **CFG** (Ho & Salimans 2022, arxiv 2207.12598) — for the classifier-free-guidance derivation. Quick read; the math is one page.
6. **Score matching foundations** (Song & Ermon, NeurIPS 2019) — for the parallel derivation. Optional unless you want to understand *why* `ε_θ` predicts the score.

For a textbook treatment: Lilian Weng's blog post [What are diffusion models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) is the canonical online reference and walks through (4.1) → (5.4) carefully.

## What you should now be able to do

- Read any DDPM-line paper's "method" section and parse the math at speed.
- Implement DDPM training in ~200 lines of PyTorch from scratch.
- Read Diffusion Policy's §II in 5 minutes and recognize it as a 1-to-1 mapping of DDPM's framework onto action chunks.
- Derive `L_simple` on paper from `−log p(x_0) ≤ L_VLB` without notes.
- Read NVIDIA Cosmos / Genie Envisioner papers and recognize them as conditional DDPMs at scale.
- Argue *for* and *against* the JEPA-vs-generative-video framing from [Module 10](curriculum-10-world-models.md) using the costs you've now seen up close (one full DDPM rollout per MPC sample is expensive; latent-space prediction sidesteps this entirely).

## Hand-off

Module 5 is referenced from:

- **[Module 7 — BC lineage on PushT](curriculum-07-bc-lineage-pusht.md)** §"Diffusion Policy" — direct consumer; the DDPM math you just derived is exactly what Diffusion Policy uses as its action head.
- **[Module 9 — VLA](curriculum-09-vla.md)** §"Action-head design across VLAs" — π0's flow-matching head is a sibling of DDPM; understanding DDPM here makes flow matching a 5-minute extension.
- **[Module 10 — World models, broad](curriculum-10-world-models.md)** §"Family 1: generative-video" — generative-video WMs are large conditional DDPMs; this module is what backs that paragraph.
- **[Module 12 — LeWM deep-dive](curriculum-12-lewm-deep-dive.md)** §2 (SIGReg derivation) — the *style* of math is similar (Gaussian KL closed forms, completing the square). If you can do Module 5's Part B exercise fluently, Module 12's SIGReg gradient derivation is straightforward.

## Related curriculum modules

- **[Modules 1–4](robot-learning-curriculum.md)** — prerequisites (NN basics, CNN U-Nets, attention for transformer-based diffusion, SSL representation learning).
- **[Module 6 — Imitation learning](curriculum-06-imitation-learning.md)** — sets up multi-modal action distributions; Module 5 enables Module 7's solution.
- **[Module 7 — BC lineage on PushT](curriculum-07-bc-lineage-pusht.md)** — direct successor; consumes Module 5's DDPM machinery.
- **[Module 9 — VLA](curriculum-09-vla.md)** — flow-matching action heads (π0) build on the same generative-modeling-over-actions frame.
- **[Module 10 — World models, broad](curriculum-10-world-models.md)** — generative-video WMs build on DDPM at scale.
- **[Module 12 — LeWM deep-dive](curriculum-12-lewm-deep-dive.md)** — the contrast point; LeWM's JEPA *avoids* ever doing diffusion on pixels.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../../index.md)

## Open questions / TBD

- **iDDPM source page** ([Nichol & Dhariwal, ICML 2021](https://arxiv.org/abs/2102.09672)) — referenced for the cosine schedule and learned variances; not yet ingested.
- **DDIM source page** ([Song, Meng, Ermon, ICLR 2021, arxiv 2010.02502](https://arxiv.org/abs/2010.02502)) — referenced for fast sampling; not yet ingested. Diffusion Policy uses it at inference.
- **CFG source page** ([Ho & Salimans 2022, arxiv 2207.12598](https://arxiv.org/abs/2207.12598)) — referenced for the classifier-free-guidance derivation; not yet ingested.
- **Score matching source pages** — Song & Ermon NeurIPS 2019, arxiv 1907.05600; Song et al. ICLR 2021 — referenced for the score-matching connection; not yet ingested.
- **Flow matching as a separate concept page** — π0 uses it; the Module 9 VLA module references it; could be a useful own-page if more sources surface.
- **A worked DDPM-on-MNIST notebook** — the anchor exercise's Part A would benefit from a sample notebook for the curriculum.
