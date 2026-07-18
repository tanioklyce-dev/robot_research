---
title: Curriculum Module 9 — Vision-Language-Action models
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-9, vla, vision-language-action, vlm, llm, generalist-policy, gr00t, pi-zero, helix, openvla, vla-jepa]
prereqs: [curriculum-03, curriculum-07]
status: draft
---

> [!note] Curriculum context
> This is **Module 9** of the [Robot-learning curriculum](robot-learning-curriculum.md). It builds on **[Module 3](robot-learning-curriculum.md)** (transformers + ViT) and **[Module 7](curriculum-07-bc-lineage-pusht.md)** (BC lineage on PushT — VLAs are BC's scaling-up). It sits alongside **[Module 10](curriculum-10-world-models.md)** as the *other* dominant paradigm for 2024–2026 generalist robot policies.
>
> Module 9 **closes the policy-side reading chain** (Modules 6 → 7 → 9). The world-model-side chain (Modules 10 → 11 → 12) is its sibling. They cross over at **VLA-JEPA** — JEPA used as an auxiliary loss inside a VLA — which this module covers in detail at the end.
>
> Acronyms used here are also in the [Glossary](../../glossary.md). First-mention links go there.

> [!note] LLM-side background (recommended)
> VLAs are vision-language models fine-tuned on robot-action demonstrations — structurally, this is **SFT applied to a multi-modal model with robot actions in the output space.** If the LLM/VLM training side is unfamiliar, read [Cameron Wolfe — Understanding and Using SFT for Language Models](../../sources/wolfe-sft-blog.md) (theory + survey of the LLaMA-2 / Alpaca / LIMA recipes) and skim [Hugging Face TRL — SFT Trainer documentation](../../sources/huggingface-trl-sft-trainer.md) (the de-facto trainer; VLM support out of the box) before continuing.

## What this module is

A field guide to **Vision-Language-Action (VLA)** models in 2025–2026: what a VLA is structurally, how it differs from the BC lineage of [Module 7](curriculum-07-bc-lineage-pusht.md), why it isn't a world model (despite often appearing alongside one), and the major instances you'll see referenced everywhere — [NVIDIA GR00T](../../entities/nvidia-groot.md), [π0 / Physical Intelligence](../../entities/physical-intelligence.md), [Helix / Figure](../../entities/figure.md), [Gemini Robotics](../../entities/gemini-robotics.md), OpenVLA. We end with [VLA-JEPA](../../entities/vla-jepa.md) — the cross-over point between this module and Module 11.

By the end of the module you should be able to:

1. Define a VLA structurally (vision encoder + language encoder/decoder + action head) and identify which component each part of a paper's architecture diagram corresponds to.
2. Explain why VLAs aren't world models — they emit actions, not next states; they're policies, not dynamics models.
3. Distinguish the dominant **action-head** choices in 2026 (autoregressive action tokens vs flow matching vs DDPM-over-actions — plus the head-free "action-as-text" alternative) and explain when you'd reach for each.
4. Read a VLA paper's training section and identify the backbone (which VLM), the action head, the data scale (hours of teleop / hours of human video), and any hierarchical structure (system 1 / system 2).
5. Place [VLA-JEPA](../../entities/vla-jepa.md) at the cross-over between Modules 9 and 11 and explain why the JEPA-as-auxiliary framing is interesting.

## What a VLA is — structurally

```
image(s)  ── vision encoder ──▶ image tokens ─┐
                                              ├──▶ transformer trunk (often LLM/VLM-pretrained) ──▶ action head ──▶ a_t
language ── language tokens ──────────────────┘
```

Three pieces:

1. **Vision encoder.** Maps raw image(s) (sometimes multiple cameras, sometimes a video segment) to a sequence of feature tokens. Usually a [ViT](../../glossary.md#vit), often pretrained — DINOv2, [SigLIP](https://github.com/google-research/big_vision), or the vision tower of a VLM.
2. **Language tokens.** A natural-language instruction ("pick up the red mug, put it on the rack") is tokenized like any text input.
3. **Trunk + action head.** A transformer (usually pretrained as a [VLM](../../glossary.md#vlm) or [LLM](../../glossary.md#llm)) ingests image + language tokens and emits *actions* — either as discrete tokens (autoregressive over an action vocabulary) or via a continuous head (flow matching, DDPM, or regression).

What makes a VLA different from a [VLM](../../glossary.md#vlm):

- **VLM:** image + text → text. Inference target is a token sequence representing language.
- **VLA:** image + text → **action**. Inference target is a control signal for a robot.

The simplest way to think about it: **a VLA is a VLM whose output head was retrained to emit actions instead of words.**

## How VLAs differ from BC ([Module 7](curriculum-07-bc-lineage-pusht.md))

VLAs are descended from BC. The differences are scale, language conditioning, and architectural inheritance:

| Axis | BC ([Module 7](curriculum-07-bc-lineage-pusht.md)) | VLA |
| --- | --- | --- |
| Backbone | small per-task ResNet/MLP | pretrained VLM (often billions of parameters) |
| Conditioning | observation only | observation + language instruction |
| Multi-task | one policy per task usually | single policy across many tasks |
| Pretraining | trained from scratch on demos | inherits internet-scale priors from VLM pretraining |
| Action head | regression / EBM / discrete / DDPM | autoregressive tokens / flow matching / DDPM |
| Generalization | within demonstrated task | across tasks via instruction-following |

The **scaling up** is the load-bearing claim. A VLA bets that the right path to a generalist robot policy is to **start with a model that already knows things about the world** (from VLM pretraining), and then **fine-tune it to emit actions on top of that knowledge.** Whether that's empirically the right bet vs. world-model-and-plan ([Module 10](curriculum-10-world-models.md)) is the active question of 2025–2026; both approaches have results, and they're complementary rather than directly competing.

## Why VLAs are *not* world models

A frequent confusion. A VLA emits actions. A world model predicts next states. These are different jobs:

- **VLA:** `(image, instruction) → action.` Don't ask it "what happens if I do this?" — that's not what it's trained for.
- **World model:** `(state, action) → next state.` Don't ask it "what should I do?" — that's a planner's job, downstream of the world model.

A VLA can be **trained alongside** a world model, **fine-tuned with** a world-model auxiliary loss (this is [VLA-JEPA](../../entities/vla-jepa.md), §below), or **planned over** by a world model (open research area). But the architectural commitment is different.

[Module 10](curriculum-10-world-models.md)'s four-family WM taxonomy contains *no* VLAs. [Module 9](robot-learning-curriculum.md) is the policy side; [Module 10](curriculum-10-world-models.md) is the dynamics side. Knowing which is which lets you read 2026 robotics papers without the constant "is this a VLA or a WM?" confusion.

> [!note] Architectural similarity is not architectural identity
> The vision encoder of a VLA may be identical to the encoder of a JEPA — same ViT, possibly same pretrained weights. The difference is what's trained on top. When in doubt, look at the *output*: actions or state predictions?

## Action-head design across VLAs

The biggest 2024–2026 design axis. Four flavors (three classic action heads + one that drops the head entirely):

### 1. Autoregressive action tokens

**Idea.** Discretize the continuous action space into a vocabulary; predict action tokens autoregressively, just like text.

- Used by [OpenVLA](../../glossary.md#openvla) and most early VLAs.
- Inherits the LLM training stack directly.
- Tradeoff: discretization error; multi-modality is handled by the categorical head (one of the [Module 7](curriculum-07-bc-lineage-pusht.md) lessons applied to VLAs).

### 2. Flow matching

**Idea.** Continuous action head trained by **flow matching** (a diffusion-cousin generative-modeling technique that learns a velocity field that pushes a base distribution to the target). Sample by integrating an ODE.

- Used by [π0](../../sources/pi-zero-paper.md) (Physical Intelligence). The headline architectural choice that distinguishes π0 from earlier VLAs.
- Continuous, multi-modal, smooth. Often faster than DDPM at inference because flow matching can be sampled in fewer integration steps.
- Sibling of [Diffusion Policy](../../entities/diffusion-policy.md)'s DDPM head from [Module 7](curriculum-07-bc-lineage-pusht.md).

### 3. Conditional DDPM over actions

**Idea.** Conditional [DDPM](../../glossary.md#ddpm) over action chunks, exactly as in [Diffusion Policy](../../entities/diffusion-policy.md), but with a VLM trunk and language conditioning.

- Used by some VLA variants (and as an action head inside hybrid systems).
- Multi-modal action distributions handled exactly as in BC.
- More inference steps than flow matching; same denoising-network structure.

### 4. Action-as-text (no head at all)

**Idea.** Skip the action head entirely — prompt the VLM to **print the action as a string of integers** (normalize the continuous action to e.g. `[0,1000]`, generate `H×D` space-separated numbers), trained with the base VLM's cross-entropy loss.

- Introduced by **[VLA-0](../../entities/vla-0.md)** ([source](../../sources/vla-0-paper.md)). No new tokens, no vocabulary change, no architecture change — the "zero-modification" design.
- Arbitrary action resolution (unlike discrete-token binning) without touching the vocabulary.
- Needs a **recipe** to work: [ACT](../../entities/act.md)-style prediction ensembling + masked-action augmentation. With it, VLA-0 tops π0 / GR00T-N1 / SmolVLA / OpenVLA-OFT on [LIBERO](../../entities/libero.md) with no action pretraining. Cost: slow autoregressive decode (~4 Hz).

### Comparison (recapping the table from [`concepts/vla-models.md`](../../concepts/learning/vla-models.md))

| VLA | Backbone | Action head | Notes |
| --- | --- | --- | --- |
| **OpenVLA** | Llama-2 | autoregressive action tokens | Open-weights baseline. |
| **[VLA-0](../../entities/vla-0.md)** | [Qwen2.5-VL](../../entities/qwen.md) 3B | action-as-text (no head) | [Source](../../sources/vla-0-paper.md). Zero-modification; tops LIBERO with no action pretraining. |
| **[π0](../../sources/pi-zero-paper.md)** | pretrained VLM | flow matching | Physical Intelligence flagship. |
| **[Diffusion Policy](../../entities/diffusion-policy.md)** (BC, not strictly a VLA) | ResNet-18 / no language | DDPM | Reference for π0's action-head choice. |
| **[Helix S1](../../sources/helix-blog.md)** | small transformer | continuous regression @ 200 Hz | Combined with **Helix S2** = 7B VLM @ 7–9 Hz. |
| **[GR00T N1.6/1.7](../../entities/nvidia-groot.md)** | Cosmos-Reason2-2B | mixed | 3B params; 20,854 hr egocentric video pretrain. |

## Major VLAs in 2026

The instances you'll see referenced everywhere. One paragraph each.

### [NVIDIA GR00T](../../entities/nvidia-groot.md)

NVIDIA's open VLA, bundled with Isaac Lab. **N1.6 GA / N1.7 EA** (early 2026) — 3B-parameter VLA built on a **Cosmos-Reason2-2B** VLM backbone. Pretrained on **~20,854 hours** of egocentric human video (per the [Top 10 Physical AI Models 2026 source](../../sources/top-10-physical-ai-models-2026.md)). Open-weights, open-deployment story. The reference VLA for the NVIDIA stack — if you're using Isaac Lab to train robot policies in 2026, GR00T is what you'd grab. Action-head is mixed (multiple options across N1.6/N1.7 variants).

### [π0 / Physical Intelligence](../../entities/physical-intelligence.md)

Octobre 2024 ([source](../../sources/pi-zero-paper.md)). 24-author paper led by Sergey Levine, Chelsea Finn, Karol Hausman, Brian Ichter, Karl Pertsch (the DROID / Metaworld lineage). **Flow-matching action head** on a pretrained VLM backbone. Cross-platform: single-arm, dual-arm, and mobile-manipulator data trained jointly. Tasks: **laundry folding, table cleaning, box assembly** — long-horizon, dexterous, household-flavored. Successor π0.6 (2025) extends task coverage.

The [Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) cites π0 / π0.6 as the leading Physical-AI VLA demonstration. Notable architecturally for proving that **flow matching as an action head** is competitive (and arguably easier) than DDPM in this regime.

### [Helix / Figure](../../sources/helix-blog.md)

Figure AI, February 2025. **Hierarchical S1/S2 architecture:**

- **S2:** 7B-parameter internet-pretrained VLM @ 7–9 Hz — slow scene + language reasoning.
- **S1:** 80M-parameter transformer visuomotor policy @ 200 Hz — fast continuous control.
- End-to-end gradient propagation between the two.

Trained on **~500 hours of teleop** ("<5%" of typical VLA datasets per Figure). Runs **onboard** on embedded low-power GPUs. Demonstrated firsts (per Figure's blog): full humanoid upper-body continuous control, multi-robot collaboration on shared tasks, generalization to "thousands" of unseen household objects via language prompts. Vendor-blog source only — treat marketing claims with appropriate skepticism until peer-reviewed.

The architectural innovation worth tracking: the **System 1 / System 2 split.** Slow VLM-as-planner + fast policy-as-controller, trained jointly. This pattern is appearing in multiple 2025+ VLAs, and the decoupled rates (~10 Hz reasoning + 200 Hz control) are a real engineering insight that single-network VLAs don't capture.

### [Gemini Robotics](../../entities/gemini-robotics.md)

[Google DeepMind](../../entities/google-deepmind.md)'s parallel generalist-policy effort. **Two variants worth distinguishing:**

- **Full Gemini Robotics VLA** — direct VLA in the conventional sense.
- **Gemini Robotics-ER** ("ER" = embodied reasoning) — a *VLM* that emits **tool calls** rather than low-level actions. Pairs with classical robot SDKs. Architecturally an [LLM-agent system](../../concepts/agents/llm-agent-architecture.md), not strictly a VLA.

Boston Dynamics' [Spot + Gemini Robotics demo](../../sources/bostondynamics-spot-gemini-robotics.md) uses the **-ER** variant — important to notice when reading capability claims, because tool-calling-on-Spot-SDK is a different kind of system than end-to-end-action-emission.

### OpenVLA

Open-weights VLA used as a baseline in many 2024–2026 papers. Llama-2 backbone with autoregressive action tokens. Worth knowing because it's the open-weights default many evaluations compare against.

### Smaller / specialized VLAs

- **SmolVLA** — runs on consumer hardware (single RTX, even MacBooks). The "VLAs you can actually run at home" entry.
- **LingBot-VLA** — Ant Group's foundation model for real-world manipulation.

These exist in the curriculum's peripheral vision; check [`concepts/vla-models.md`](../../concepts/learning/vla-models.md) for the live list.

## Hierarchical S1/S2 — a structural pattern worth watching

Helix made the slow-reasoning + fast-control split explicit, but the pattern is showing up elsewhere:

- [Helix](../../sources/helix-blog.md) S2 (7B VLM @ 7–9 Hz) + S1 (80M transformer @ 200 Hz).
- [GR00T](../../entities/nvidia-groot.md) N1 architecture has analogous slow-VLM / fast-control structure.
- [Gemini Robotics-ER](../../entities/gemini-robotics.md) is essentially "S2 only — the VLM emits tool calls; the SDK is the controller."

The decoupled rates have a clean intuition:

- **Reasoning at ~10 Hz** is plenty for high-level intent: "what should I be doing?" doesn't change frame-by-frame.
- **Control at ~200 Hz** is what robot motors need. Trying to run a 7B VLM at 200 Hz isn't viable on embedded hardware.

Whether this is a *temporary* engineering accommodation that will go away when on-robot inference gets fast enough, or a *permanent* architectural insight that biological brains exhibit too, is an open question. Both readings are defensible. Module 9 just flags the pattern so you'll recognize it.

## VLA-JEPA — the cross-over

[VLA-JEPA](../../entities/vla-jepa.md) (Sun et al., February 2026 — [source](../../sources/vla-jepa-paper.md)). The explicit cross-over point between Module 9 (VLAs) and [Module 11](curriculum-11-jepa-deep.md) (JEPA depth).

**The setup.** Train a VLA the standard way (image + language → action), but **add a JEPA-style auxiliary loss** that predicts *future visual embeddings* of the scene the robot is acting on. The VLA learns to output actions; the JEPA auxiliary learns to predict consequences of those actions in latent space.

**The architecture.** Standard VLA forward pass + a parallel JEPA prediction head:

```
image_t ── encoder ──▶ z_t
language ──────────────▶ language tokens
(z_t, language) ── trunk ──▶ a_t                       // action output (VLA)
(z_t, a_t)      ── jepa_pred ──▶ ẑ_{t+1}                // auxiliary JEPA loss
loss = imitation_loss(a_t, a_t*) + λ · ‖ẑ_{t+1} − z_{t+1}‖²
```

The auxiliary loss doesn't change inference (you still emit `a_t` at deploy); it just **shapes the encoder during training** so that the latent predicts forward.

**Benchmarks.** [LIBERO](../../glossary.md#libero), SimplerEnv, and real robots.

**Why this is interesting.**

- **JEPA may not be a competitor — it may be a component.** The VLA-JEPA result suggests JEPA-style next-embedding prediction is *useful as a regularizer / pretext task* even when you're training a VLA. Like contrastive learning's evolution from "the way you train" to "one term in your loss."
- **It bridges the two paradigms** without committing to either. A VLA-JEPA model is a VLA at deploy, and it had a JEPA loss at train. You don't have to pick.
- **It's a candidate path for closing the data gap.** Action-conditioned BC is data-limited; observation-only video is abundant. A VLA-JEPA can in principle pretrain the JEPA half on action-free video and then train the VLA-action half on a much smaller demo dataset — the same recipe V-JEPA 2-AC uses, applied to a VLA architecture.

[Module 11](curriculum-11-jepa-deep.md) covers the JEPA side in detail. This module is the VLA side. They meet here.

## Anchor exercise

> **Sketch the data flow for π0, [Diffusion Policy](../../entities/diffusion-policy.md), and LeWM-MPC on the same PushT episode.**

Three architectures, same task. The point is to feel the structural differences.

```
                       ┌─ image_t ─┐
                       │ language  │
   π0 (VLA):           ├─→ pretrained VLM trunk ──→ flow matching head ──→ a_t
                       └────────────────────────────────────────────────────┘

                       ┌─ image_t ─┐
                       │  no lang  │
   Diffusion Policy:   ├─→ ResNet-18 ──→ DDPM denoising network ──→ a_t (chunk)
                       └─────────────────────────────────────────────────────┘

                       ┌─ image_t ─┐                  ┌─ image_g (goal) ─┐
                       │           │                  │                  │
   LeWM-MPC:           ├─→ ViT-tiny ──→ z_t          ├─→ ViT-tiny ──→ z_g
                       │              │              │
                       │     candidate actions a_{1:H}│
                       │              ↓               │
                       │     pred(z_t, a_1) → ẑ_2     │
                       │     pred(ẑ_2, a_2) → ẑ_3     │
                       │             ⋮                │
                       │     pred(ẑ_{H-1}, a_H) → ẑ_H │
                       │              ↓               │
                       │     cost = ‖ẑ_H − z_g‖²     │
                       │              ↓               │
                       │     CEM optimizer            │
                       │              ↓               │
                       │     a_1 (executed)           │
```

Three things to notice:

1. **Inputs differ.** π0 takes image + language; Diffusion Policy takes only image; LeWM-MPC takes a current image *and a goal image*. PushT is a fixed-goal task, so all three have something to anchor to — but they anchor differently.
2. **Inference steps differ.** π0 = one forward pass through the VLM trunk + flow integration; Diffusion Policy = ResNet encode + 10 DDIM denoising steps; LeWM-MPC = encode + N×H predictor rollouts + CEM iterations.
3. **What's "trained" vs "free at inference."** In π0 and DP, the *policy* is the trained object — actions are the model's output. In LeWM-MPC, the *dynamics model* is the trained object; actions are *optimized* at inference time against the dynamics + cost.

Now expand the LeWM-MPC pipeline with explicit details from [Module 12](curriculum-12-lewm-deep-dive.md): which CEM hyperparameters? what's the planning horizon? Compare the per-tick latency of all three systems. (π0 ~tens of ms; Diffusion Policy ~10 ms × 10 steps; LeWM full plan ~1 sec.) Predict which would dominate on a real robot at 30 Hz control.

This is the closing exercise of the policy-side reading chain. By the end, the wall-clock latency budgets and the architectural commitments should feel like load-bearing facts, not abstract design space.

## Recommended reading

In order:

1. **[`concepts/vla-models.md`](../../concepts/learning/vla-models.md)** — concept page; re-read the action-head comparison table.
2. **[π0 paper](../../sources/pi-zero-paper.md)** — the cleanest architectural exemplar (flow-matching action head on VLM backbone).
3. **[Helix blog](../../sources/helix-blog.md)** — the S1/S2 hierarchical-VLA pattern. Vendor source; read with appropriate skepticism.
4. **OpenVLA paper** — not yet a wiki source page; the open-weights baseline most papers benchmark against.
5. **[VLA-JEPA paper](../../sources/vla-jepa-paper.md)** — the cross-over with [Module 11](curriculum-11-jepa-deep.md).
6. **[Top 10 Physical AI Models 2026](../../sources/top-10-physical-ai-models-2026.md)** — broad VLA-landscape survey, useful for placing GR00T / π0 / Helix in context.
7. **[Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md)** — the "VLAs are still at the research stage" framing; useful background on the data-bottleneck story.

## What you should now be able to do

- Read a 2026 robotics paper and immediately classify whether it's a VLA, a BC method, or a world model. (Look at: language conditioning? what's being trained? what's emitted at inference?)
- Identify the action-head choice in any VLA paper (autoregressive tokens / flow matching / DDPM / continuous regression) and explain why the authors might have chosen it.
- Spot the System 1 / System 2 hierarchical pattern when it shows up and reason about whether the rate decoupling is engineering or insight.
- Place [VLA-JEPA](../../entities/vla-jepa.md) at the cross-over between Modules 9 and 11 and articulate why JEPA-as-auxiliary is a different architectural commitment than JEPA-as-the-whole-model.
- Predict latency budgets for π0 / Diffusion Policy / LeWM-MPC on the same task and reason about which can run at 30 Hz on consumer hardware.

## Closing the policy-side reading chain

[Module 6](curriculum-06-imitation-learning.md) → [Module 7](curriculum-07-bc-lineage-pusht.md) → **Module 9** is the **policy-side** chain:

- Module 6: BC fundamentals; multi-modal failure mode; distribution shift.
- Module 7: IBC → BeT → Diffusion Policy as architectural responses to multi-modal actions.
- Module 9: VLA = scaling-up of BC with language conditioning + VLM pretraining.

[Module 10](curriculum-10-world-models.md) → [Module 11](curriculum-11-jepa-deep.md) → [Module 12](curriculum-12-lewm-deep-dive.md) is the **world-model-side** chain.

These are siblings. They cross over at [VLA-JEPA](../../entities/vla-jepa.md) (auxiliary JEPA loss inside a VLA — covered above) and at the **frozen-vision-encoder** axis (DINOv2 / SigLIP work in both lineages — see [`concepts/jepa.md`](../../concepts/world-models/jepa.md) and [`concepts/vla-models.md`](../../concepts/learning/vla-models.md)).

[Module 13](robot-learning-curriculum.md) (home robotics deployment) is where both chains are evaluated against actual deployment reality.

## Related curriculum modules

- **[Module 3 — Sequence models and attention](robot-learning-curriculum.md)** — transformer + ViT prerequisites for the VLM trunk and action transformer.
- **[Module 5 — Generative models / DDPM](robot-learning-curriculum.md)** — substrate for the DDPM-and-flow-matching action heads.
- **[Module 7 — BC lineage on PushT](curriculum-07-bc-lineage-pusht.md)** — direct ancestor; VLAs are scaled-up BC with language.
- **[Module 10 — World models, broad](curriculum-10-world-models.md)** — sibling paradigm; VLAs aren't WMs.
- **[Module 11 — JEPA in depth](curriculum-11-jepa-deep.md)** — cross-over via VLA-JEPA.
- **[Module 13 — Home robotics deployment](robot-learning-curriculum.md)** — successor; deployment reality of both paradigms.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../../index.md)

## Open questions / TBD

- **OpenVLA paper** as a source page — the open-weights baseline is referenced repeatedly; primary-source ingest would tighten comparisons.
- **GR00T N1.6 / N1.7 papers** as source pages — currently the entity page leans on secondary cites (Top 10 Physical AI Models, NVIDIA developer blog). NVIDIA's published papers on N1.x would close this gap.
- **π0.6 paper** as a separate source — the 2025 successor to π0; not yet ingested.
- **Helix peer-reviewed paper** — at ingest time, no Helix paper exists. Re-check periodically.
- **Flow matching as a concept page** — would be a useful Module 5 addendum if it shows up in more sources.
- **VLA-JEPA as the prototype for hybrid VLA + WM systems** — a synthesis page surveying every "JEPA-as-auxiliary" or "BC + WM" hybrid would be load-bearing for [Module 13](robot-learning-curriculum.md).
