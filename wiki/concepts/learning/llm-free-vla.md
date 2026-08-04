---
title: LLM-free VLA (the V+L→A paradigm)
type: concept
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [vla, llm-free-vla, efficient-inference, cross-attention, grounding, control-abstraction-levels, turbovla, inference-latency]
---

# LLM-free VLA (the V+L→A paradigm)

**An LLM-free VLA is a language-conditioned robot policy that keeps language conditioning but removes the language model from the control loop.** Vision and text are encoded independently by compact encoders and fused directly — typically by cross-attention — into a control representation, with no shared language-model latent space acting as the bridge.

## The distinction being drawn

The [TurboVLA paper](../../sources/turbovla-paper.md) (Xie, Yao et al., 2026) names the two pathways, and the naming is the useful contribution:

**V→L→A (LLM-centric)** — the dominant design. Visual features are projected into a language model's token space, concatenated with the tokenized instruction, and processed by the LLM; actions are decoded from the resulting hidden state:

```
Z̃ᵛ = P_v(E_v(O))          # project vision into LLM token space
Hᴸ  = F_L[ Z̃ᵛ ; Tok(x) ]   # the LLM is the bridge
Â   = D_act(Hᴸ, s)         # actions decoded from LLM features
```

Everything in this wiki does this — [OpenVLA](../../entities/openvla.md), [π0](../../entities/pi-zero.md)/[π0.5](../../entities/pi-zero-5.md)/[π0.7](../../entities/pi07.md), [GR00T](../../entities/nvidia-groot.md), [SmolVLA](../../entities/smolvla.md), [MolmoAct2](../../entities/molmoact2.md), [VLA-0](../../entities/vla-0.md). The **action-head families** the wiki tracks (discrete tokens / flow matching / custom heads / action-as-text) are all choices about `D_act`. They differ in how actions leave the LLM, not in whether they pass through one.

**V+L→A (LLM-free)** — `Hᴸ` is never formed:

```
Zᵛ = E_v(O)                # vision encoder (e.g. DINOv3)
Zˡ = E_l(x)                # small text encoder (e.g. BERT), token sequence retained
(Zᵛ, Zˡ) → N× bidirectional cross-attention → Z^{vl}
Â  = D_act(Z^{vl}, s)
```

> [!note] This is an orthogonal axis, not a fifth action-head family
> The wiki's [VLA taxonomy](vla-models.md) enumerates four action-head families. LLM-free is a cut across a **different** dimension — *what produces the representation the head consumes*. A V+L→A model can in principle use any of the four heads; [TurboVLA](../../entities/turbovla.md) happens to use an [ACT](../../entities/act.md)-style parallel-query decoder.

## The argument

From [TurboVLA §1](../../sources/turbovla-paper.md): *"language is necessary for instruction-conditioned manipulation, but execution-level control need not be centered on a large language model."* Once an instruction has specified the skill, the executor does not perform open-ended generation or task decomposition — it needs to use the instruction to decide **how current visual evidence should guide action**. A general-purpose LLM's reasoning and generative capacity exceeds that requirement, and is paid for at every policy invocation.

This is a claim about [control abstraction level](../robotics/control-abstraction-levels.md), and it is compatible with LLMs mattering enormously one level up. TurboVLA's own conclusion proposes exactly that hierarchy — LLM planner over LLM-free executor — which is the [System 1 / System 2](vla-models.md) pattern of [Helix](../../sources/helix-blog.md) and GR00T with a much cheaper System 1.

## Evidence so far

One data point, but a well-powered one. [TurboVLA](../../entities/turbovla.md): **97.7% [LIBERO](../../entities/libero.md)** (n = 2,000) at **0.2 B params / 0.9 GB VRAM / 31.2 ms**, statistically tied with π0.5 (3.4 B / 12.8 GB / 93.6 ms) and OpenVLA-OFT; **60.2% on [RoboTwin 2.0](../../entities/robotwin.md)** bimanual (n = 5,000), which *does* separate from π0.5's 57.0 (p = 0.0012).

The ablations are what make this more than an efficiency result:

| Question | Finding |
|---|---|
| Is language load-bearing? | **Yes** — removing it costs 26.9 pp (97.7 → 70.8), with LIBERO-Goal collapsing 97.4 → 11.6 |
| Is *semantic* language load-bearing, or just task identity? | **Semantic** — a learned task-ID embedding recovers only to 95.4, a statistically real 2.3 pp short (p = 0.0001) |
| How big must the text encoder be? | **Small** — BERT (216 M) 97.7 and T5-small (142 M) 97.1 are indistinguishable (p = 0.23) |
| Does the fusion design matter? | **Yes** — plain concatenation 95.2, one-way cross-attention 96.1/96.5, bidirectional 97.7 |

Read together: **language semantics matter and language *models* apparently don't** — at least at execution level, on these benchmarks. That is the whole claim, and it is falsifiable.

## Where the semantics come from instead

TurboVLA initializes its fusion layers from **[Grounding DINO](../../entities/grounding-dino.md)** feature-enhancement weights. So the model does inherit large-scale vision-language pretraining — it is just **open-vocabulary grounding** pretraining (object-to-word correspondence) rather than **generative language** pretraining. This reframes the question the paradigm poses: not "is pretraining needed?" but **"which kind of vision-language pretraining does manipulation actually need?"**

## The open question that decides this

> [!warning] Untested against LIBERO-PRO — and this is the paradigm's most exposed flank
> [LIBERO-PRO](../../sources/libero-pro-paper.md) shows models above 90% on standard LIBERO **collapsing to 0.0%** under object/instruction/scene perturbation. An LLM-free VLA with 0.2 B parameters, no embodied pretraining, and no web-scale language priors has, by construction, the least semantic fallback of anything in the wiki's table. If the LLM's contribution is *robustness* rather than *in-distribution accuracy*, deleting it would be invisible on LIBERO and catastrophic on LIBERO-PRO — and every number above would be measuring recall.
>
> The counter-hypothesis is real too: grounding pretraining may transfer under object swaps *better* than an LLM latent, since it was trained for exactly open-vocabulary object-to-word correspondence. π0.5 — the most co-trained model tested — was still the most robust in LIBERO-PRO at 0.38, which suggests broad pretraining does buy something.
>
> **The test is cheap now.** The [VLA evaluation harness](../../sources/vla-evaluation-harness-github.md) runs LIBERO-Pro at ~18 min/H100 for 2,000 episodes. This is the single highest-value experiment the wiki can name against this paradigm.

## Consequences if it holds

- **Edge deployment changes character.** 0.9 GB is the first VLA inference footprint here that fits an [Orin Nano](../../entities/jetson-orin-nano.md) 8 GB with headroom, where [GR00T](../../entities/nvidia-groot.md)'s 16 GB floor rules the board out. See the [control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) and [Jetson module ladder](../../syntheses/platforms/jetson-module-ladder-power-performance.md) — though no edge measurement of an LLM-free VLA exists yet.
- **The efficiency literature gets reframed.** Quantization, token pruning, dynamic depth, layer skipping, distillation, and speculative decoding are all optimizations of a backbone this paradigm argues shouldn't be in the loop.
- **It supports the hierarchical stance the wiki keeps meeting.** [Waddle](../../entities/waddle-labs.md)'s "VLA-as-tool," [code-as-policy](../agents/code-as-policy.md) agents, Helix S1/S2, and Anthropic's [access-level thesis](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) all separate deliberation from execution. TurboVLA measures how cheap the execution tier can get.

## Related
- [Action representation languages](../../syntheses/agents/action-representation-languages.md) — where TurboVLA's task-ID-vs-semantic-English result (95.4 vs 97.7) becomes a measurement of what a *constrained* action vocabulary would cost.
- [VLA models](vla-models.md) — the taxonomy this branches
- [TurboVLA](../../entities/turbovla.md) — the only instance so far
- [Grounding DINO](../../entities/grounding-dino.md) — where the cross-modal fusion comes from
- [Control abstraction levels](../robotics/control-abstraction-levels.md) — the argument is level-specific
- [Control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) · [VLA deployability landscape](../../syntheses/platforms/vla-deployability-landscape.md)

## Mentioned in
- [TurboVLA paper](../../sources/turbovla-paper.md)
