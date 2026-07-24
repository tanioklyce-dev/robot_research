---
title: Mixture-of-Experts (MoE)
type: concept
created: 2026-07-24
updated: 2026-07-24
sources: 1
tags: [mixture-of-experts, moe, sparse-models, routing, language-model, efficiency]
---

# Mixture-of-Experts (MoE)

A **Mixture-of-Experts** layer replaces one big feed-forward network with **many
smaller "expert" FFNs plus a router** that sends each token to only a **small
subset** of them. The model therefore has a large **total** parameter count but a
small **active** count per token — you pay dense-inference cost for a fraction of
the parameters while keeping the capacity of the whole. It is the dominant lever
for the **cost-performance trade-off** in large LMs.

## The mechanism

- **Experts:** N parallel FFNs in a layer (N can be dozens to hundreds).
- **Router:** a small learned gate scores the experts per token and activates the
  **top-k** (k ≪ N). Only those k experts run.
- **Active vs total params:** e.g. [OLMoE](../../entities/olmoe.md)-1B-7B has **7B
  total but ~1B active/token** — 64 experts, top-8
  ([Muennighoff et al. 2024](../../sources/olmoe-paper.md)).
- **Load balancing:** because the router could collapse onto a few experts,
  training adds an **auxiliary load-balancing loss** (spread tokens across experts)
  and a **router z-loss** (keep gate logits well-scaled).

## Design choices that matter (the OLMoE findings)

The clearest open reference on *how* to build an MoE is
[OLMoE](../../sources/olmoe-paper.md), which ran the ablations most labs keep
private:

- **Fine-grained / granular experts** — many small experts (64 × top-8) beat few
  large ones.
- **Dropless token-based routing** beats expert-based routing (no tokens dropped
  when an expert is "full").
- **Shared experts were ineffective** in OLMoE's regime — a direct challenge to
  the DeepSeekMoE design that keeps always-on shared experts.
- **Sparse upcycling** (converting a pretrained *dense* model into an MoE) gave
  **limited benefit** except at small compute — argues for training MoE from
  scratch.
- Routing analysis shows **high expert specialization** (experts specialize by
  domain/token type).

> [!note] Contested at scale. OLMoE's "shared experts don't help / upcycling is
> weak" findings are first-party to its ~1B-active regime; larger MoEs
> (DeepSeek-V3, Qwen MoE) *do* use shared experts and upcycling, so treat these as
> regime-dependent, not universal laws.

## Where it shows up in this wiki

- [OLMoE](../../entities/olmoe.md) — the fully-open MoE LM; backbone of Molmo's
  **MolmoE-1B**. The concrete, inspectable instance.
- Contrast the **dense** [OLMo](../../entities/olmo.md) family (same lab, no MoE) —
  useful as the apples-to-apples "what does sparsity buy?" comparison.

## Related concepts

- [VLA models](vla-models.md) — an MoE LM can serve as the decoder backbone of a
  VLM/VLA (as OLMoE does under MolmoE).
- [Scaling laws for VLAs](scaling-laws-vla.md) — MoE changes the compute/parameter
  accounting scaling arguments assume.

## Current state

MoE is standard in frontier LMs (Mixtral, DeepSeek-V3, Qwen MoE, Gemini) as the
way to grow capacity without proportional inference cost. What remains
lab-specific and debated: **expert granularity, shared-vs-routed experts,
upcycling, and routing algorithm** — the exact axes [OLMoE](../../sources/olmoe-paper.md)
documents openly and where its conclusions diverge from the closed frontier MoEs.

## Mentioned in

- [OLMoE (Muennighoff et al. 2024)](../../sources/olmoe-paper.md)
