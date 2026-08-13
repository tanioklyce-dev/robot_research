---
title: Flow matching
type: concept
created: 2026-05-25
updated: 2026-08-13
sources: 17
tags: [flow-matching, generative-model, ode, continuous-actions, vla, action-head, pi-zero, smolvla, molmoact2, dit, lipman, esser, xvla]
---

**Flow matching** — a continuous-time generative-modeling technique that learns a **vector field** `v_θ(x_τ, τ)` whose flow transports samples from a noise distribution to a data distribution. Trained by regressing on a closed-form target vector field along straight-line (or other) interpolants between noise and data, without the score-matching detour DDPM-class diffusion models take. **The dominant continuous-action-head technique in 2025+ VLAs** — used by [π0](../../entities/pi-zero.md), [π0.7](../../entities/pi07.md), [π*0.6](../../entities/pistar06.md), [SmolVLA](../../entities/smolvla.md), [GR00T N1](../../sources/groot-n1-paper.md) (DiT action head, Beta(1.5,1) timestep prior following π0, only **K=4 Euler steps** at inference), and [EgoScale](../../sources/egoscale-paper.md). Sibling-not-subclass of [DDPM](../../entities/ddpm.md): both are continuous-action approaches that avoid action-tokenization quantization, but flow matching trains a deterministic vector field rather than a noise-prediction network.

## Mechanics (per π0 / SmolVLA conventions)

Given target distribution over actions `A_t` and noise `ε ~ N(0, I)`:

- Sample `τ ~ Beta(α, β)` (both π0 and SmolVLA use a Beta distribution for the flow-matching time variable, rather than uniform).
- Interpolate: `A^τ_t = τ · A_t + (1 − τ) · ε` (linear interpolant; "rectified flow" / straight-line).
- Target vector field: `u(A^τ_t | A_t) = ε − A_t` (closed form for the straight-line case).
- Train `v_θ` (the **action expert**) to regress on `u` via conditional flow-matching loss:
  ```
  L_τ(θ) = E[ || v_θ(A^τ_t, o_t) − u(A^τ_t | A_t) ||² ]
  ```
  where `o_t` are the VLM features extracted from the observation.

At inference, integrate the learned vector field from noise to data over `τ ∈ [0, 1]` — typically with **10 ODE steps** for the wiki's reference implementations.

## Action-head taxonomy in VLAs

| Family | Reference | Continuous? | How actions are produced |
|---|---|---|---|
| **Autoregressive tokens** | OpenVLA | No (discretized to bins) | LLM-style next-token prediction |
| **DDPM** | [Diffusion Policy](../../entities/diffusion-policy.md) | Yes | Iterative noise prediction + denoising |
| **Flow matching** | [π0](../../entities/pi-zero.md), [π0.7](../../entities/pi07.md), [π*0.6](../../entities/pistar06.md), [SmolVLA](../../entities/smolvla.md), [X-VLA](../../entities/x-vla.md), [EgoScale](../../sources/egoscale-paper.md) | Yes | Learned vector field + ODE integration |

The flow-matching family is winning the 2025 action-head contest — every major late-2025 VLA primary source ingested in this wiki uses flow matching. **All three families are instances of a [Fenchel-Young loss](../../entities/mathieu-blondel.md)** with different convex-conjugate regularizers — [Blondel & Roulet 2025](../../sources/blondel-roulet-differentiable-programming.md) (chs. 13 + 18) gives the unifying math.

## Architectural variation across flow-matching VLAs

The flow-matching head is a small transformer ("action expert") that attends to VLM-backbone features. Three distinct attention patterns have been published:

| Model | Action-expert attention |
|---|---|
| [π0](../../entities/pi-zero.md) | **Full bidirectional self-attention** — all action tokens attend to each other |
| [π0.7](../../entities/pi07.md) / [π*0.6](../../entities/pistar06.md) | Full bidirectional SA + **[Knowledge Insulation (KI)](knowledge-insulation.md) training** — VLM trained via next-token prediction with [FAST](../../entities/fast-action-tokenization.md) tokens; action expert gets **stop-gradient** to VLM |
| [SmolVLA](../../entities/smolvla.md) | **Interleaved cross-attention + causal self-attention** — each block is either CA (action tokens cross-attend to VLM keys/values) or SA (causal masked, action tokens attend only to past tokens) |
| [X-VLA](../../entities/x-vla.md) | **No separate action expert at all** — action tokens are ordinary tokens in one 24-layer bidirectional self-attention stack shared with the multimodal tokens and the [soft prompts](soft-prompt-cross-embodiment.md). Proprioception, noisy action chunk, and flow time `t` are concatenated and projected by a single linear layer, fusing *early*. Uses `t ~ U(0,1)` and the OT/rectified-flow path — **not** the Beta prior π0 and SmolVLA adopt. |
| [MolmoAct2](../../entities/molmoact2.md) | **DiT-style expert (36 layers, matching VLM depth) with [per-layer KV conditioning](per-layer-kv-conditioning.md)** — each expert block does SA → CA to the *corresponding VLM layer's* keys/values → MLP, with DiT shift/scale/gate from the flow-time embedding. KI-style stop-gradient in post-training, dropped in fine-tuning. |

SmolVLA's interleaved CA+SA pattern empirically wins on real-world SO-100 multi-task at smaller scale; whether it scales to π0.7's regime is open. MolmoAct2's per-layer-KV design ablates **+1.9 over final-hidden-state conditioning** on LIBERO — evidence that *where* in the backbone the expert reads from matters, not just the attention pattern.

## Why VLA designers picked flow matching over DDPM

- **Fewer inference steps** (10 vs DDPM's 100+ unless DDIM-distilled).
- **Straight-line interpolant** is simpler than DDPM's variance schedule + iteratively-derived posterior.
- **Deterministic vector-field target** is easier to regress on than DDPM's noise-prediction target with the variance-weighting schedule.
- Empirically competitive or better on action-prediction benchmarks ([Lipman et al. 2022](https://arxiv.org/abs/2210.02747); [Esser et al. SD3 2024](https://arxiv.org/abs/2403.03206)).
- Lets the same `v_θ` be **conditioned on VLM features** straightforwardly — the action expert is just a transformer that consumes both `A^τ_t` and the VLM-feature `o_t`.

## Related lineage (not yet ingested as primary sources)

- **Lipman et al. 2022** — "Flow Matching for Generative Modeling" (arXiv 2210.02747). The foundational flow-matching paper. Referenced as `[102]` in π0.7.
- **Liu et al. 2022** — "Rectified Flow" (arXiv 2209.03003). The straight-line interpolant special case.
- **Esser et al. 2024** — SD3 ("Scaling Rectified Flow Transformers for High-Resolution Image Synthesis"). The image-gen scaling result that made flow matching's empirical case.

## What flow matching is NOT

- **Not a strict subset of diffusion** — DDPM and flow matching are siblings, both descending from continuous-time stochastic / ODE generative modeling. DDPM learns a noise predictor whose inferred score gradient defines a reverse-SDE; flow matching learns a vector field directly. Both can be derived from the same underlying continuity equation under different parameterization choices.
- **Not a separate concept from "diffusion-style" generative modeling** in casual usage — papers often conflate; the wiki uses [DDPM](../../entities/ddpm.md) for the discrete-time-noise-prediction variant and **flow matching** for the continuous-time-vector-field variant.
- **Not specific to VLAs** — also used in image gen (SD3, BAGEL), molecular dynamics, and elsewhere.

## Related

- [DDPM](../../entities/ddpm.md) — sibling continuous-action generative model.
- [Diffusion Policy](../../entities/diffusion-policy.md) — DDPM applied to actions; the policy-class contrast for flow matching.
- [π0](../../entities/pi-zero.md), [π0.7](../../entities/pi07.md), [π*0.6](../../entities/pistar06.md) — π-series flow-matching VLAs.
- [SmolVLA](../../entities/smolvla.md) — Hugging Face flow-matching VLA with interleaved CA+SA action expert.
- [MolmoAct2](../../entities/molmoact2.md) — DiT-style flow-matching expert with [per-layer KV conditioning](per-layer-kv-conditioning.md).
- [EgoScale](../../sources/egoscale-paper.md) — flow-matching DiT action expert.
- [VLA models](vla-models.md) — broader concept.
- [The Elements of Differentiable Programming](../../sources/blondel-roulet-differentiable-programming.md) — ch. 12.6 (continuous adjoint for ODEs), ch. 13 (smoothing), ch. 18 (Fenchel-Young losses) all bear on flow matching.
- [Mathieu Blondel](../../entities/mathieu-blondel.md) — Fenchel-Young framework unifying action-head families.

## Mentioned in

- [GR00T N1 paper](../../sources/groot-n1-paper.md) — flow-matching DiT System 1; K=4 Euler steps.
- [π0 paper](../../sources/pi-zero-paper.md)
- [π0.7 paper](../../sources/pi07-paper.md)
- [π*0.6 paper](../../sources/pistar06-paper.md)
- [SmolVLA paper](../../sources/smolvla-paper.md)
- [EgoScale paper](../../sources/egoscale-paper.md)
- [MolmoAct2 paper](../../sources/molmoact2-paper.md) — DiT expert, per-layer KV conditioning, K=4/8 flow samples.
- [Robot Learning: A Tutorial (LeRobot)](../../sources/lerobot-robot-learning-tutorial.md) — covers flow matching in the generative-models chapter.
- [The Elements of Differentiable Programming](../../sources/blondel-roulet-differentiable-programming.md) — rigorous mathematical reference.

## Open questions

- **Lipman / Liu / Esser primary sources** — none ingested directly. If the wiki ever needs a primary source on flow matching itself, those are the obvious targets.
- **Flow matching vs DDPM trade-off in BC** — no head-to-head ablation in the wiki yet. The π0 and SmolVLA papers default to flow matching but don't run a clean DDPM vs flow-matching ablation on the same VLA backbone.
- **Stochastic flow matching for multi-modal action distributions** — π0/SmolVLA flow-matching heads emit deterministic vector fields, so the multi-modality coverage comes from sampling different `ε`s. Whether this is sufficient for genuinely multi-modal action distributions is an open empirical question; the [JEPA-WMs paper §6](../../sources/jepa-wms-paper.md) flags the same limitation for deterministic JEPA predictors.
