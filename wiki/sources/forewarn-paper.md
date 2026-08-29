---
title: "FOREWARN — From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment"
type: source
url: https://arxiv.org/abs/2502.01828
local_path: raw/FOREWARN_ForesightToForethought_2502.01828.pdf
sha256: 2a2c3386e99f98c42a0254fd8f16f86aebd1e2221186f3efd6a6937e1283f96f
project_page: https://yilin-wu98.github.io/forewarn/
author: "Yilin Wu, Ran Tian, Gokul Swamy, Andrea Bajcsy (Carnegie Mellon University; Tian at UC Berkeley)"
published: 2025-02-03
ingested: 2026-08-16
venue: arXiv 2502.01828 (v3, 2025-05-02)
format: pdf
tags: [policy-steering, world-model, dreamerv3, vlm, latent-alignment, runtime-intervention, failure-prediction, diffusion-policy, llama, lora, franka, generation-verification-gap, cmu]
---

# FOREWARN — Filtering Options via REpresenting World-model Action Rollouts as Narration

## Summary

**The intervention layer the wiki's runtime thread kept ending without.** [Safety filters](../concepts/robotics/safety-filters.md) prevent physical harm; [runtime monitors](../concepts/robotics/runtime-failure-detection.md) raise a flag and stop. FOREWARN does something: at each decision point it takes **K candidate action plans the base policy already proposed**, predicts each one's outcome with a **latent world model**, has a **VLM narrate those outcomes in natural language**, and then asks the same VLM to pick the best plan given the task description.

The premise is that most runtime failures are **mode-selection failures, not capability failures**: *"the base policy may already contain the 'right' behavior mode within its distribution… but due to putting too much probability mass on an undesired mode, the robot does not reliably choose the correct action plan at runtime."* Diffusion policies are multimodal by design — the fix is often to pick a different sample, not to retrain.

Base-policy success 0.30 / 0.20 / 0.10 across three real Franka tasks → **0.80 / 0.70 / 0.70** with steering, and — the result that separates it from its own ablations — **it holds up under task descriptions never seen in training** (0.80 / 0.70 / 0.60) where a trained classifier over the same latents collapses to **0.00 / 0.10 / 0.20**.

> [!note] Why this belongs next to PACS, not just next to Sentinel
> [PACS](pacs-paper.md) showed that a safety mechanism that **edits** a policy's action pushes it off the demonstration manifold and destroys task success (0.04 vs 0.72). FOREWARN never edits anything — it **selects among samples the policy itself drew**, so the executed action is in-distribution by construction. Two groups, two problems (safety vs alignment-with-intent), the same structural constraint: **intervene by choosing, not by correcting.**
>
> That is a design rule worth carrying, and neither paper states it in the general form.

## The mechanism

**The framing first.** Policy steering is posed as stochastic MPC over the base policy's own samples:

```
a* = argmax_{a ∈ {a¹…aᴷ}}  E_{o ~ P(·|o,a)} [ R(o; ℓ) ]
```

which decomposes into **prediction** (what will this plan do?) and **verification** (is that what the user asked for?). Classical MPC needs a physics model and a hand-written reward; open-world manipulation has neither. So: **world model for prediction, VLM for verification** — and the paper's contribution is the interface between them.

**Foresight — a frozen DreamerV3 world model.** An RSSM ([DreamerV3](../entities/dreamer.md)) is pretrained on 250 real trajectories per task, deliberately including **both successful and failed base-policy rollouts** so it can predict the outcomes of bad plans too. It predicts `T = 64` future **latent** states from the current observation and a candidate action plan. Frozen thereafter.

**Forethought — latent-text alignment, which is the actual novelty.** A VLM cannot read a world model's latent states, and (as the ablations show) it cannot read decoded images well either. So the world model's latent sequence is projected through **a single linear adapter into Llama-3.2-11B-Vision-Instruct's text-token space**, replacing the ViT patch tokenizer — one token per predicted state instead of many per image. LoRA fine-tuning on a hand-annotated VQA dataset teaches the VLM to **narrate** the predicted latents: *"the robot grasps the cup by the handle,"* *"the robot fails to grasp the fork."*

**Steering.** Sample 100 plans from the [diffusion policy](../entities/diffusion-policy.md), cluster to **K = 6 modes** by non-maximum suppression, narrate each, then query the same VLM as a multiple-choice verifier against the task description. Execute the winner.

## Key claims

**Narration accuracy — the world model is doing real work (50 rollouts, 3 seeds):**

| Method | GT accuracy (avg) | LLM score (avg) |
|---|---|---|
| FOREWARN-Oracle (privileged true future latents) | 0.85 | 0.81 |
| **FOREWARN** | **0.82** | **0.76** |
| VLM-Img-Oracle (GPT-4o on *ground-truth* future images) | 0.52 | 0.64 |
| VLM-Act (fine-tuned Llama, actions as text, no world model) | 0.37 | 0.51 |
| VLM-Img (GPT-4o on world-model-decoded images) | 0.35 | 0.58 |

- **Predicted latents beat ground-truth images.** FOREWARN at 0.82 versus VLM-Img-**Oracle** at 0.52 — a frontier VLM shown the *actual* future frames describes the robot's behavior worse than a small fine-tuned model reading a world model's imagination. Fine-grained contact detail (handle vs rim vs interior) is apparently not what a general VLM extracts from video.
- **Actions-as-text does not work.** VLM-Act (0.37) is barely above chance on this metric despite identical fine-tuning data. *"Low-level action data is beyond the training distribution of current VLMs."* The decoupling is what buys the accuracy, and the paper's own headline framing — separate **foresight** from **forethought** — is exactly this result.

**Closed-loop steering on real hardware (Franka, 20 trials per cell):**

| Method | Cup | Bag | Fork | Cup* | Bag* | Fork* |
|---|---|---|---|---|---|---|
| Base policy (no steering) | 0.30 | 0.20 | 0.10 | 0.50 | 0.40 | 0.30 |
| **FOREWARN** | **0.80** | **0.70** | **0.70** | **0.80** | **0.70** | **0.60** |
| VLM-DynLat-Category (VLM predicts success indices, no narration) | 0.80 | 0.40 | 0.50 | 0.30 | 0.40 | 0.30 |
| Classifier-Dyn-Latent (transformer classifier on latents) | 0.80 | 0.70 | 0.70 | **0.00** | 0.10 | 0.20 |
| VLM-Act | 0.40 | 0.20 | 0.20 | 0.30 | 0.50 | 0.20 |

`*` = **novel task description** at test time — e.g. Cup goes from *"serve the cup of water to the guest"* to *"the handle is covered with oil"*, which inverts which grasp mode is correct.

- **The novel-description column is the whole argument.** A trained classifier over the same predicted latents *matches FOREWARN exactly* on trained descriptions (0.80 / 0.70 / 0.70) and then **collapses to 0.00 / 0.10 / 0.20** when the instruction changes. Routing the decision through **natural language** is what preserves the VLM's open-world reasoning; feeding it latents and asking for a category *"essentially degrades to a traditional end-to-end model."*
- **The intermediate representation is load-bearing, not decorative.** That is a claim with consequences well beyond this paper: text is not just an interface for humans here, it is the representation in which generalization survives.
- **Fast enough to be interesting, slow enough to matter**: 3.7 s total per steering decision (0.1 s world model, 1.3 s narrating 6 plans, 2.3 s selecting) against **22.0 s** for VLM-Act — the speedup coming largely from one token per predicted state instead of per image patch, and from world model and VLM communicating in latent space with no decode/re-encode round trip.
- **Generalizes to environment variation too** — object colors/sizes and background changes across all three tasks, with *"small performance drop"* (qualitative; no table).

## Where the authors place themselves

Their own three-way taxonomy of handling generative-policy failures is the cleanest in this wiki's corpus, and it locates the other ingested sources precisely:

| Category | What it does | Wiki instances |
|---|---|---|
| **Post-hoc detection** | Find and explain failures in offline datasets | none ingested |
| **Runtime monitoring** | Detect failures *as they happen* — often "fast detector + slow VLM reasoner" | [Sentinel](sentinel-paper.md), [FAIL-Detect](fail-detect-paper.md) |
| **Failure prediction** | Anticipate failures *before* they occur, enabling preemptive correction | **FOREWARN** |

And the criticism they make of the middle row is the one this wiki independently arrived at: monitors *"fundamentally require the robot to start failing for the runtime monitor to activate."*

The paper also frames itself as **learning to search** — local search against a learned verifier inside a learned world model — leaning on the **generation-verification gap**: verifying a plan is easier to learn than generating one, which is why a small VQA dataset suffices where end-to-end steering would need far more.

## Limitations, as stated

- **It assumes the base policy is already competent** — that the right mode is somewhere in the K samples. Detecting *"if none of the policy's generated action plans are suitable"* is named as future work, which is precisely where a [runtime monitor](../concepts/robotics/runtime-failure-detection.md) would have to take over.
- **Most system failures trace to the world model's imprecise imagination**, worsened by limited training data. The authors suggest DINO-style features or large pretrained world models.
- **Inference overhead**, with the standard proposals: hierarchical decomposition (slow reasoning over fast control, as VLAs already do), quantization/caching, distillation.
- **250 trajectories per task of world-model data, hand-annotated narrations, and 20 trials per evaluation cell.** Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), 20 trials puts ±0.10 differences inside the noise — the 0.30→0.80 and the 0.70-vs-0.00 gaps survive that, the ordering among close cells does not.
- Only the **most likely** latent prediction is used per plan, so the stochastic world model is used deterministically.

## Entities mentioned

- [DreamerV3](../entities/dreamer.md) — the RSSM world model, pretrained then frozen; used here as a **runtime verifier substrate** rather than for policy learning.
- [Diffusion Policy](../entities/diffusion-policy.md) — the base policy being steered (100 demos/task, T = 64 action plans).
- **Llama-3.2-11B-Vision-Instruct** — VLM backbone, LoRA-tuned with a linear latent adapter; **GPT-4o** as the zero-shot image baseline and as an evaluation judge.
- [Franka Panda](../entities/franka-panda.md) — hardware, 15 Hz end-effector control.
- Without pages: Yilin Wu, Ran Tian, **Gokul Swamy**, **Andrea Bajcsy** (CMU).

## Concepts touched

- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — **this is the intervention layer** that page's three ingested methods stop short of.
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — same in-distribution constraint, reached from the alignment side.
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) — a **new function**: world model as runtime verifier, not planner or data generator.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — steering changes what a "policy success rate" even measures.
- [VLA models](../concepts/learning/vla-models.md) · [Imitation learning](../concepts/learning/imitation-learning.md) — the multimodality that makes mode selection both possible and necessary.

## Open questions

- **Who decides when steering is not enough?** FOREWARN assumes a good plan is among the six. Sentinel and FAIL-Detect assume something has already gone wrong. **The composition — monitor detects that no candidate is acceptable, system escalates — is unbuilt**, and both sides name it as future work.
- **Does the narration bottleneck survive scale?** Text preserved generalization here at 11B with LoRA and hand-annotated narrations. Whether that holds when the behaviors are less enumerable than "handle vs rim vs interior" is untested.
- **A world model trained on the base policy's own failures** is a quiet data requirement: 250 trajectories per task including failures. That is cheap next to demonstration collection but it is not free, and it is task-specific.
- **3.7 s per decision on a 15 Hz robot** means steering happens at plan boundaries, not continuously. The hierarchical fix is exactly the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md)'s recurring pattern — slow reasoner over fast controller — and nobody has built it for steering.
