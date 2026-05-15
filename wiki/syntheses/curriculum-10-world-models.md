---
title: Curriculum Module 10 — World models, broad
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-10, world-model, mpc, cem, planning, jepa, dreamer, td-mpc, generative-video, taxonomy]
prereqs: [curriculum-04, curriculum-05, curriculum-06, curriculum-08]
status: draft
---

> [!note] Curriculum context
> This is **Module 10** of the [Robot-learning curriculum](robot-learning-curriculum.md). It assumes Tier 1 ([Modules 1–4](robot-learning-curriculum.md): NN, CNN, attention, SSL), [Module 5](robot-learning-curriculum.md) (generative models / DDPM — used in the generative-video paragraph), [Module 6](curriculum-06-imitation-learning.md) (imitation learning + the BC alternative), and [Module 8](robot-learning-curriculum.md) (RL vocabulary — needed to read the Dreamer / TD-MPC paragraph).
>
> Module 10 is the **bridge into Tier 4**. It establishes the taxonomy. [Module 11](robot-learning-curriculum.md) goes deep on the JEPA family. [Module 12](robot-learning-curriculum.md) is the LeWM deep-dive. Without the four-family taxonomy from this module, "LeWM is a JEPA, end-to-end-trained, with an MPC planner" reads as word-soup.
>
> Acronyms used here are also in the [Glossary](../glossary.md). First-mention links go there.

> [!note] Control-theory background (recommended)
> The "MPC" in "WM + MPC" is the receding-horizon approximation of a classical optimal-control problem. If control theory is unfamiliar: [Sussmann & Willems 1997 — 300 Years of Optimal Control](../sources/sussmann-willems-1997-300-years-optimal-control.md) is the historical retrospective (Bernoulli → Pontryagin); [DS4DS 7.01 — Optimal Control, Introduction (Peitz & Wallscheid)](../sources/ds4ds-7-01-optimal-control-intro.md) is the modern-pedagogy video companion (the full DS4DS module 7 also covers LQR, linear MPC, and data-driven MPC via DMD across lessons 7.02–7.09). Together they form a complete optimal-control orientation pre-read for this module's MPC section.

## What this module is

The curriculum's "what is a world model and what could you do with one" module. We define the term functionally, lay out **four families** of world models with one canonical example each, walk through the **three planning algorithms** (MPC, CEM, gradient-based) that operate against a learned world model, and end with the **compounding-error** budget that constrains how far you can plan.

By the end of the module you should be able to:

1. Write the world-model functional definition (`s_{t+1} = f(s_t, a_t)`) and place any specific paper into one of the four families on first reading of the abstract.
2. Pseudocode an MPC loop in 3 lines and explain why CEM is the dominant sampler for it in modern world-model work.
3. Reason about how horizon and per-step prediction error trade off in compounding-error terms (worst-case bound and intuition).
4. Position [LeWM](../entities/leworldmodel.md) as one specific point — JEPA family, end-to-end encoder, MPC planner, no value function — in this design space.
5. Read the LeWM ablation table column headers (Dreamer, TD-MPC, DINO-WM, PLDM) and know which family each represents.

## Functional definition

A **world model** is any function `f` learned from data such that

```
s_{t+1} = f(s_t, a_t)         (deterministic)
p(s_{t+1} | s_t, a_t)         (stochastic)
```

The state space, action conditioning, and prediction target vary widely — see the full design-axis table in [`concepts/world-model.md`](../concepts/world-model.md). The shared commitment is: **dynamics, learned, conditioned on actions** (in the variants useful for control).

> [!note] World model ≠ World *simulator*
> The narrower term [world-model simulator](../concepts/world-model-simulators.md) refers to learned models being used as drop-in replacements for a physics engine in a training or evaluation pipeline. Many world models (e.g. Dreamer-class MBRL) are *not* simulators by that narrower definition — they're inner loops of a training algorithm, not environments anyone "trains in." This module covers the broader umbrella term.

## The four families

The curriculum's organizing axis. Two of these are well-developed in the wiki ([JEPA](../concepts/jepa.md) family in [generative-video vs JEPA](generative-video-vs-jepa-world-models.md); the [generative-video](../concepts/world-model-simulators.md) family there too). The other two — frozen-foundation-feature and Dreamer-style MBRL — are either glossed over in existing pages or were only just ingested. This module names all four with equal weight.

### Family 1: Generative-video / "World Foundation Models"

**Predict next-frame pixels.** Train a giant conditional video generator on internet video (often diffusion-based — see [Module 5](robot-learning-curriculum.md)). At deploy, condition on the current frame + an action, generate the next frame.

- **Examples:** [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [Genie Envisioner](../entities/genie-envisioner.md) / GE-Sim2.
- **Substrate:** [DDPM](../sources/ddpm-paper.md) and its descendants. Action conditioning typically via classifier-free guidance ([CFG](../glossary.md#cfg)) or token-level conditioning.
- **Pros:** Human-inspectable rollouts (you can *watch* the imagined future). Single substrate scales to internet video.
- **Cons:** Expensive to train and sample. Hallucination and frame-by-frame drift over long rollouts. Decoding to pixels is overhead the policy never actually needs — the policy just wants information.

### Family 2: JEPA / latent-prediction

**Predict the next-state embedding, not pixels.** An encoder maps observation → latent vector `z`. A predictor maps `(z_t, a_t) → z_{t+1}`. Loss is in latent space (typically [MSE](../glossary.md#mse)), not pixel space. No decoder.

- **Examples:** [V-JEPA 2 / V-JEPA 2-AC](../entities/v-jepa-2.md), [LeWorldModel](../entities/leworldmodel.md), [PLDM](../entities/pldm.md).
- **Substrate:** Yann LeCun's [JEPA program](../concepts/jepa.md). Explicit position taken against pixel-prediction.
- **Pros:** Order-of-magnitude cheaper than generative-video both to train and to plan against. [LeWM reports up to 48× faster planning](../sources/leworldmodel-paper.md) than foundation-model-based world models. Pretraining is action-free and scales to web-video.
- **Cons:** **Representation collapse** is a fundamental failure mode — without anti-collapse mechanisms, encoder + predictor can learn trivial constants. Latent space is opaque; failures aren't visually inspectable. Module 11 covers the collapse-prevention zoo (EMA target encoders, stop-gradient, frozen encoders, [SIGReg](../glossary.md#sigreg), …).

### Family 3: Frozen-foundation-feature

**Use a pretrained encoder (e.g. [DINOv2](../entities/dinov2.md)) frozen, learn only the predictor on top.** Architecturally adjacent to JEPA, but the encoder is not co-trained — it's loaded and frozen, removing the collapse problem entirely (the encoder can't collapse if it's not training).

- **Examples:** [DINO-WM](../entities/dino-wm.md), [DINO-world](../entities/dino-world.md), [JEPA-WMs](../entities/jepa-wms.md).
- **Substrate:** Pretrained vision foundation models. Currently DINOv2 is the dominant choice in this niche.
- **Pros:** Training is dramatically simpler — no collapse, fewer hyperparameters. Strong zero-shot generalization inherited from the encoder. [DINO-WM zero-shot planning on novel tasks](../sources/dino-wm-paper.md) is the canonical demonstration.
- **Cons:** You're stuck with DINOv2's representational choices — it was not trained on robot data, so its features may not be ideal for control. End-to-end variants (LeWM) can be better for tasks where a custom encoder helps.

### Family 4: Reward-conditioned MBRL

**Learn a latent dynamics model whose latent is shaped by rewards and value targets, then train an actor-critic in the imagined dynamics.** The world model isn't separately useful — it's an inner loop of an RL algorithm.

- **Examples:** [Dreamer / DreamerV3](../entities/dreamer.md) (generative — pixel reconstruction), [TD-MPC / TD-MPC2](../entities/td-mpc.md) (decoder-free).
- **Substrate:** Model-based RL ([MBRL](../glossary.md#mbrl)) lineage. Hafner-line for Dreamer; Hansen-line for TD-MPC.
- **Pros:** Dreamer is the canonical generality demo (single config, 150+ tasks). TD-MPC's decoder-free latent is structurally close to JEPA. Sample-efficient compared to model-free RL — "imagination" rollouts are free once the world model is trained.
- **Cons:** Requires a reward signal (a constraint JEPA / frozen-feature WMs don't have). Latent space is shaped by reward, which means transferring the model to a new task is non-trivial.

> [!note] Dreamer vs TD-MPC: pixel decoder is the sharpest axis
> [Dreamer](../entities/dreamer.md) decodes to pixels (and reward); [TD-MPC](../entities/td-mpc.md) is decoder-free. The decoder-free choice puts TD-MPC architecturally adjacent to JEPA — and that's the framing [LeWM](../entities/leworldmodel.md) leans on when it benchmarks against TD-MPC.

### A four-family summary table

| Family | Predicts | Examples | Strength | Weakness |
| --- | --- | --- | --- | --- |
| Generative-video | next-frame pixels | [Cosmos](../entities/nvidia-cosmos.md), [Genie Envisioner](../entities/genie-envisioner.md) | inspectable rollouts, scales to web video | expensive, hallucinates, drifts |
| JEPA | next-state embedding (end-to-end encoder) | [V-JEPA 2](../entities/v-jepa-2.md), [LeWM](../entities/leworldmodel.md) | cheap, fast planning, action-free pretraining | collapse-prone; opaque |
| Frozen-foundation-feature | next-state embedding (frozen encoder) | [DINO-WM](../entities/dino-wm.md), [JEPA-WMs](../entities/jepa-wms.md) | trivially stable; inherits DINOv2 generality | locked into off-the-shelf representation |
| MBRL (reward-conditioned) | reward-shaped latent / pixels | [Dreamer](../entities/dreamer.md), [TD-MPC](../entities/td-mpc.md) | sample-efficient; canonical RL benchmarks | reward-dependent; task-coupled latent |

## Planning against a world model

A world model isn't directly a policy — you still need to choose actions. This module covers **planning** (open-loop or receding-horizon optimization against the model). Module 8 covers the alternative — *training* a policy against the model in the [imagination](../glossary.md#imagination) (the Dreamer recipe).

### Model Predictive Control ([MPC](../glossary.md#mpc))

The receding-horizon control loop. At every control tick:

```
1. Sample (or optimize) candidate action sequences a_t, a_{t+1}, ..., a_{t+H−1}.
2. For each candidate, roll out the world model and score the rollout against a cost function.
3. Pick the best sequence; execute the FIRST action; observe; repeat.
```

That's the entire algorithm. Three knobs:

- **Horizon `H`.** How far ahead you imagine. Longer horizon = more opportunity to find good plans but more compounding error.
- **Sampler.** How candidates are generated.
- **Cost function.** How rollouts are scored. Often a goal-image embedding distance ([JEPA](../concepts/jepa.md)-line) or a sum-of-rewards ([MBRL](../glossary.md#mbrl)-line).

MPC is the dominant planner across the JEPA / frozen-feature / latent-MBRL families. [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [V-JEPA 2-AC](../entities/v-jepa-2.md), and [TD-MPC2](../entities/td-mpc.md) all use MPC variants.

### Sampling-based MPC: [CEM](../glossary.md#cem) and MPPI

The cross-entropy method ([CEM](../glossary.md#cem)) is the canonical sampler for MPC against a learned model:

```
Initialize action distribution N(μ_0, Σ_0).
Repeat for K iterations:
  Sample N action sequences from N(μ_k, Σ_k).
  Score each by rolling out the world model.
  Keep the top-M ("elites").
  Refit N(μ_{k+1}, Σ_{k+1}) to the elites.
Return μ_K (or sample one sequence).
```

CEM is **derivative-free** — you don't need gradients through the world model. That matters because rolling gradients through 16 steps of a learned dynamics network is numerically unpleasant; CEM treats `f` as a black-box scoring function. Used by TD-MPC2, DINO-WM, and many others.

**MPPI** (Model Predictive Path Integral) is a closely-related sampler used in some [Dreamer](../entities/dreamer.md)-line and TD-MPC variants. Same structure, different update rule. Treat them as siblings for curriculum purposes.

### Gradient-based planning

If your world model is fully differentiable (it usually is), you can backpropagate the cost-of-rollout through the dynamics and update the action sequence directly:

```
Initialize action sequence a.
Repeat:
  Roll out f(s_t, a_t) to get z_t for t = 1..H.
  Compute cost C(z_1, ..., z_H, goal).
  Update a ← a − η ∇_a C.
```

In principle this is much faster than CEM (one gradient step vs many rollouts). In practice it's brittle — the gradient through 16 steps of a learned latent dynamics model has all the standard "long-RNN" problems (vanishing / exploding gradients, sensitivity to local minima). Some [LeWM](../entities/leworldmodel.md) experiments use gradient-based MPC; others use CEM. Use whichever empirically works on your task — both are in the toolbox.

### When to use which

| Setting | Planner |
| --- | --- |
| Discrete or hybrid actions, no gradients | CEM / random shooting |
| Continuous actions, smooth rollout cost | gradient-based MPC (when it works) |
| Multi-modal optimal-action distributions | CEM (samples cover multiple modes) |
| Rewards-as-cost, MBRL setting | CEM or learned policy in imagination |

For curriculum purposes: **default to assuming "MPC means CEM-MPC"** unless a paper says otherwise. That's true for most JEPA / frozen-feature work.

## Planning horizon and compounding error

The constraint that shapes everything in this module.

**The basic intuition.** Suppose your world model has a per-step prediction error of `ε` — averaging across rollouts, `‖f(s, a) − s_true‖ ≈ ε`. After `H` rollout steps, the error doesn't stay `ε` — it compounds, often *super-linearly*. The naïve bound is `O(H · ε)` for one-step error propagation, but in practice `O(H² · ε)` or worse is common for non-linear systems where small position errors lead to large dynamics differences (think contact discontinuities).

**The implication.** You cannot plan arbitrarily far ahead. Every world-model paper has an implicit (or explicit) optimal horizon `H*` past which more lookahead hurts because the model's predictions are too unreliable. Typical values:

- **JEPA / frozen-feature on PushT-class tasks:** `H = 5–20` steps.
- **TD-MPC2 / Dreamer-line on continuous control:** `H = 5–15` for MPC; longer for in-imagination policy training because the value function provides a learned tail bound.
- **Generative-video at minute scale:** [Genie Envisioner](../entities/genie-envisioner.md) reports stable rollouts at "minute scale" but doesn't claim those rollouts are precise enough for closed-loop control.

**Why MBRL helps.** [Dreamer](../entities/dreamer.md) and [TD-MPC](../entities/td-mpc.md) use a **learned value function** to terminate rollouts. Plan `H = 5` steps with the model, then add `V(s_{t+H})` as a learned approximation of the value-of-rest-of-trajectory. This is the value-bootstrap trick — extends the *effective* planning horizon without paying compounding-error cost on every step.

JEPA-line work without value functions doesn't have this trick. [LeWM](../entities/leworldmodel.md)'s MPC planner uses a fixed horizon; the model's job is to make `H` long enough to beat baselines without compounding into noise.

> [!note] Module 12 cross-link
> The exact horizons LeWM chooses on its four benchmark environments — and the planning protocol details that make those numbers reproducible — are in [Module 12](robot-learning-curriculum.md). For now: assume "the horizon is small, the per-step error is what kills you, and the value function is the standard trick to extend the effective horizon."

## Generative-video vs JEPA — the two-paradigm framing

The wiki has a [dedicated synthesis](generative-video-vs-jepa-world-models.md) on this comparison. Read it once now; it covers in depth what this module flags briefly.

The headline tradeoff:

- **Generative-video:** human-inspectable, expensive, scales to internet video as a training-data engine. Use it for evaluating high-level agent behavior, generating synthetic training data, or authoring tools.
- **JEPA:** opaque, cheap, fast to plan against. Use it for closed-loop MPC on a real robot.

Three derived facts that are load-bearing for the rest of the curriculum:

1. **The 48× planning-speed gap** ([LeWM paper](../sources/leworldmodel-paper.md)). A model-predictive controller running at 10–30 Hz needs many candidate rollouts per cycle. The order-of-magnitude difference between paradigms is what makes JEPA-style WMs viable for closed-loop control on consumer hardware and generative-video WMs not.
2. **Action-free pretraining.** JEPA's two-stage recipe — internet-video pretraining then small-action-data fine-tuning — is the existence proof that representation pretraining substitutes for interaction data. [V-JEPA 2-AC's zero-shot Franka result](../sources/v-jepa-2-paper.md) (62 hr of DROID, two new labs) is the cleanest version.
3. **The paradigms aren't competing for the same job.** Generative-video serves as data-engine + authoring tool; JEPA serves as on-robot perception + planner. The [generative-video vs JEPA synthesis](generative-video-vs-jepa-world-models.md) §"Cross-paradigm interactions" lays this out in detail.

## Where LeWM lives in the taxonomy

The bridge to Module 11 (JEPA depth) and Module 12 (LeWM specifically):

| Axis | LeWM's choice |
| --- | --- |
| Family | JEPA (latent-prediction, end-to-end encoder) |
| Predicts | Embedding `z_{t+1}` of next state |
| Encoder | Small ViT, **trained end-to-end** (not frozen) |
| Predictor | Causal AR transformer over `(z_t, a_t)` |
| Loss | next-embedding MSE + **[SIGReg](../glossary.md#sigreg)** (single anti-collapse regularizer) |
| Planner | MPC (CEM and gradient-based variants both demonstrated) |
| Value function | None |
| Reward signal | None at training time |

What this configuration is responding to (each choice is a contestable decision):

- **End-to-end encoder.** Departure from [DINO-WM](../entities/dino-wm.md)'s frozen-DINOv2 approach. Bet: a small task-shaped encoder beats a generic large encoder when training data is on-task.
- **Single regularizer (SIGReg).** Departure from [PLDM](../entities/pldm.md)'s ~6 anti-collapse hyperparameters and V-JEPA's EMA + stop-gradient battery. Bet: random-projection + normality-test gives the *same* anti-collapse guarantee with one knob. [Module 12](curriculum-12-lewm-deep-dive.md) does the math.
- **No value function.** Departure from Dreamer / TD-MPC. Bet: pure MPC against a strong dynamics model is enough; the compounding-error problem stays inside `H`.
- **No reward at training.** Departure from MBRL. Bet: action-conditioned dynamics are a *task-agnostic* objective; goals come in only at planning time as cost functions over the latent space.

By Module 12 you'll be able to evaluate each of these bets quantitatively against LeWM's reported numbers. By the end of *this* module, you should be able to read the LeWM abstract and place every claim against the right axis above.

## Anchor exercise

> **Write a 3-line MPC pseudocode that plans against a learned next-state predictor and a cost function.**

```python
def mpc_step(z_t, world_model, cost_fn, horizon=5, samples=64):
    actions = sample_action_sequences(samples, horizon)              # (N, H, A)
    z_rollouts = world_model.rollout(z_t, actions)                   # (N, H, Z)
    return actions[argmin(cost_fn(z_rollouts))][0]                   # first action of best plan
```

That's the whole thing. To make it a *good* anchor exercise, extend it in three steps:

1. **Replace the random sampler with CEM.** Five iterations, top-32 elites out of 256 samples, Gaussian fit. Compare success rate vs random shooting on a toy task.
2. **Make `world_model` a tiny MLP** trained on a 1D toy dynamical system (e.g. a damped pendulum). Vary the per-step prediction error by adding noise; plot success rate vs horizon. You should see a peak — an "optimal horizon" past which compounding error eats the lookahead benefit.
3. **Try gradient-based MPC** on the same setup (backprop through your differentiable MLP world model). Compare to CEM in success rate, latency, and stability.

If you want a real-task version: install [`stable-worldmodel`](../entities/stable-worldmodel.md) per the [LeWM howto](leworldmodel-howto.md), load a pretrained PushT LeWM checkpoint, and inspect the planning code. Most of what you'll find is exactly the loop above with goal-image embedding distance as `cost_fn`. That code is what [Module 12](robot-learning-curriculum.md)'s anchor exercise (reproduce LeWM PushT) builds on.

## Recommended reading

In order:

1. **[`concepts/world-model.md`](../concepts/world-model.md)** — concept page. Re-read for the design-axis table and the four-paradigm bullet list.
2. **[Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md)** — the deep-dive synthesis on the two main families.
3. **[V-JEPA 2 paper](../sources/v-jepa-2-paper.md)** — Module 11 prerequisite; primary source for the JEPA family at scale. Skim §1–3 for the architecture.
4. **[DreamerV3 paper](../sources/dreamer-v3-paper.md)** — read the abstract + introduction. The "single-config across 150+ tasks" generality claim is the core result.
5. **[TD-MPC2 paper](../sources/td-mpc2-paper.md)** — read the abstract. The decoder-free + MPC + TD value-bootstrap recipe.
6. **[LeWM paper](../sources/leworldmodel-paper.md)** — read the abstract + Figure 1 only. The deep dive is Module 12.
7. **MPC primer.** If "CEM" is unfamiliar, the [Wikipedia page on Cross-Entropy Method](https://en.wikipedia.org/wiki/Cross-entropy_method) is enough. The TD-MPC papers also have compact pseudocode.

## What you should now be able to do

- Read a paper's abstract and immediately classify the world model as generative-video / JEPA / frozen-feature / MBRL.
- Read a planning section and identify the planner (MPC + CEM vs gradient-based vs in-imagination policy training) and the cost / reward signal.
- Reason about why a given paper chose a specific horizon, and whether the reported per-step error budget is consistent with that horizon.
- Place LeWM in the four-family taxonomy and articulate each of its design choices as a specific bet against a specific alternative.
- Read the LeWM ablation columns (Dreamer, TD-MPC, DINO-WM, PLDM) and know which family each represents and why.

## Hand-off to Module 11

Module 10 names the four families and walks you through the planning vocabulary. **[Module 11](robot-learning-curriculum.md)** goes deep on family 2 (JEPA) and family 3 (frozen-foundation-feature):

- The V-JEPA 1 → V-JEPA 2 → V-JEPA 2-AC → V-JEPA 2.1 progression.
- The collapse-prevention zoo: [EMA](../glossary.md#ema) target encoders, stop-gradient, [BYOL](../glossary.md#byol)-line, frozen encoders, [VICReg](../glossary.md#vicreg)-line, [SIGReg](../glossary.md#sigreg).
- DINO-WM (frozen-feature) vs end-to-end JEPA (LeWM, PLDM) as a sub-axis.
- [JEPA-WMs](../entities/jepa-wms.md) as the first JEPA-for-real-robotics demonstration on Franka.

[Module 12](robot-learning-curriculum.md) then takes the LeWM paper section by section, with the **[SIGReg](../glossary.md#sigreg)** math derivation as the centerpiece. Module 10's four-family taxonomy is what makes the LeWM contribution legible — without it, "yet another world model" is the right read.

## Related curriculum modules

- **[Module 5 — Generative models / DDPM](robot-learning-curriculum.md)** — substrate for the generative-video family.
- **[Module 6 — Imitation learning](curriculum-06-imitation-learning.md)** — the alternative paradigm; world models are the *other* answer to "how to get a policy."
- **[Module 7 — BC lineage](curriculum-07-bc-lineage-pusht.md)** — the BC-side answer to PushT; world-model-side answer (LeWM, DINO-WM) shows up in Modules 11–12.
- **[Module 8 — RL vocabulary](robot-learning-curriculum.md)** — required to read the Dreamer / TD-MPC sections; values, policy gradient, MBRL.
- **[Module 11 — JEPA depth](robot-learning-curriculum.md)** — direct successor.
- **[Module 12 — LeWM deep-dive](robot-learning-curriculum.md)** — Module 10's destination.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- ~~**PLDM source page.**~~ Filed: [PLDM Paper](../sources/pldm-paper.md) + [PLDM entity](../entities/pldm.md) (2026-05-10). The 4–6 anti-collapse hyperparameter framing now backed by the primary source.
- **Genie Envisioner 2.0** as a deeper ingest. The wiki has the announcement filed; the underlying technical paper would deepen the generative-video paragraph.
- **An end-to-end CEM implementation walkthrough** — currently the anchor exercise points the reader at `stable-worldmodel`'s code; a small standalone reference implementation might be worth filing as a separate page if multiple modules end up needing it.
- **MPPI** as a sibling-of-CEM source page — would close the planner-sampler family.
