---
title: "The declared-axis experiment — a design"
type: synthesis
created: 2026-09-07
updated: 2026-09-10
tags: [experiment-design, declared-axis, abstraction, generalization, leworldmodel, stable-worldmodel, pusht, jepa, falsification]
---

# The declared-axis experiment — a design

[The abstraction tax](abstraction-tax.md) claims that **a representation is robust to shift along an axis if and only if its training procedure declared that axis irrelevant**. That currently rests on three papers agreeing by coincidence, one accidental ablation inside [Demo-JEPA](../../sources/demo-jepa-paper.md), and two recipe checks. This is the controlled version, designed to be cheap enough that nobody has an excuse.

**Sharpened for the model it runs on:** [LeWorldModel](../../sources/leworldmodel-paper.md)'s objective is *paid* to encode the agent's colour — colour is the most predictable feature in any trajectory, and `L_pred` rewards predictable features. That is the wiki's mechanistic explanation for [stable-worldmodel](../../sources/stable-worldmodel-paper.md)'s **50.8% → 6–26%** collapse under colour/size/shape shift. Add a declaration that colour is irrelevant, change nothing else, and the collapse should not happen.

## Two design problems, which are most of the content

The version originally filed — *"train one JEPA with colour jitter and one without"* — does not work, for two separate reasons. Both are worth stating because each is a finding in its own right.

**1. Colour is task-relevant in [PushT](../../entities/pusht.md).** The agent is a **blue circle**, the block a **gray T**, the goal a **green T outline**. Colour is the only thing separating the three. Global colour jitter destroys the task rather than declaring a nuisance irrelevant.

> So the declaration must be **targeted at agent colour specifically** — which is exactly the factor [stable-worldmodel](../../sources/stable-worldmodel-paper.md) perturbs (*"agent color/size/shape"*) — and that requires **re-rendering through the simulator**, not image-space jitter.

**2. Data diversity is not a declaration.** This is the part that makes the experiment interesting rather than routine.

> [!warning] In a temporal-prediction world model, across-trajectory diversity buys nothing
> Re-render training trajectories with a randomly sampled agent colour, held constant *within* each trajectory. Colour remains **perfectly predictable from frame *t* to frame *t+1***. `L_pred` is unchanged. **The objective is still paid to encode it.**
>
> Which predicts that the only ways to declare a *static* attribute irrelevant in this architecture are (a) an **explicit invariance term**, or (b) **physically implausible per-frame randomization**. Nothing in the standard data-augmentation playbook does the job, because that playbook was written for joint-embedding models whose positive pair is two views of *one* frame — and [LeWM's positive pair is (frame *t*, frame *t+1*)](../../sources/leworldmodel-paper.md).
>
> If this is right it is a general statement about the [world-action model](../../concepts/world-models/world-action-model.md) family, not a quirk of one model.

## Four arms

Identical data volume, architecture, schedule and seed set throughout. Only the declaration changes.

| | Arm | Change to LeWM | Declares colour irrelevant? |
|---|---|---|---|
| **A0** | baseline | none — the published recipe | no |
| **A1** | **diversity only** | agent colour sampled **per trajectory**, constant within | **no** — colour stays predictable |
| **A2** | temporal randomization | agent colour resampled **per frame** | yes, through `L_pred` |
| **A3** | **explicit invariance** | `L = L_pred + λ·SIGReg + β·‖E(o_t) − E(recolour(o_t))‖²` | yes, [LeVJEPA](../../sources/levjepa-paper.md)-style |

- **A1 is the control that carries the design.** It isolates *declaration* from *exposure*, and it is the arm the naive experiment would have silently conflated with A2/A3.
- **A2 corrupts the physics** and is expected to cost dynamics quality. It exists to separate *the mechanism works* from *this particular implementation is usable*.
- **A3 carries the hypothesis.** It is the smallest possible additive change and the closest analogue to what LeVJEPA actually does.

## Readouts, in order of signal quality

1. **Colour decodability.** A linear probe from the frozen latent to agent colour. This is the **mechanistic** measurement, and it is cheap and low-variance — thousands of samples, tight intervals, no rollouts. *Prediction: A0/A1 near-perfect, A2/A3 near chance.*
2. **Planning success under agent-colour shift** — the outcome measure, using swm's own perturbation. **≥100 rollouts per cell** (see power below).
3. **In-distribution planning success** — must be preserved. Report as an **equivalence bound**, never as "no difference."
4. **Off-axis control: shift in agent *shape***, which **no arm declares**. *Prediction: all four arms equally brittle.*

> [!note] Readout 4 is not optional
> Without the shape control the experiment cannot distinguish **"declaring colour buys colour-robustness"** from **"augmentation makes models generically more robust."** The second is the boring hypothesis and it explains the same colour result. Any version of this experiment that omits the off-axis arm proves nothing.

## What each outcome means, committed in advance

| Result | Reading |
|---|---|
| A1 ≈ A0 brittle; A2/A3 robust | **The mechanism holds.** Declaration, not diversity, is the operative variable. |
| **A1 ≈ A3 robust** | **Mechanism wrong**, or not operative — coverage is doing the work. [The abstraction tax](abstraction-tax.md) needs rewriting, not annotating. |
| A3 robust on colour **and** on shape | Generic regularization effect; axis-specificity is false. |
| A3's colour probe at chance but planning still collapses | Encoder invariance **does not reach the planner** — the predictor or CEM re-introduces the dependence. Kills the simple story, and is the most interesting failure available. |
| A3 loses in-distribution success | **The abstraction tax, quantified** — the wiki's first direct measurement of it rather than an inference across three unrelated papers. |

## Power, cost, staging

**Power.** The collapse effect is large (~25 pp against a base rate near 0.3), so **n = 100 rollouts per cell gives roughly 4σ** — comfortably enough to separate collapse from no-collapse. The **in-distribution equivalence claim is the hard one**: at n = 200 per cell a difference can only be bounded at roughly **±9 pp** at 95%, and no realistic budget tightens that much. State the bound; do not report a null. See [robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md).

**Cost.** LeWM is **~15M parameters**, *"trainable on a single GPU in a few hours"* (the paper used a single **NVIDIA L40S**). Four arms × 3 seeds ≈ **1–2 GPU-days** plus rollouts. The smallness is the main argument for running it.

**Staging.**

- **Stage 0 — hours, no training at all.** Pull the **released checkpoint** ([`quentinll/lewm-pusht`](https://huggingface.co/quentinll/lewm-pusht), with datasets in the same collection) and run readout 1 on it. If agent colour is linearly decodable at high accuracy from LeWM's latent, that confirms the *"the objective encodes it"* half of the mechanism **on the exact model stable-worldmodel measured**. Highest value per hour in the plan, and it can falsify the premise before anything is trained.
- **Stage 0.5 — reproduce the baseline, and settle the 50.8%-vs-94% ambiguity** the wiki [flagged on the stable-worldmodel page](../../sources/stable-worldmodel-paper.md) and never resolved. Every downstream number is measured against this one, so it has to be pinned first.
- **Stage 1 — A0 vs A3, 3 seeds.** This is the hypothesis.
- **Stage 2 — A1, A2, and the shape control.** This is what makes it publishable rather than suggestive.

## Where it could go wrong

- **Re-rendering fidelity.** Perturbed *training* data must come from swm's factor machinery, not a post-hoc image filter, or A1/A2 differ from the evaluation distribution along axes other than colour and the comparison is dead.
- **β needs tuning in A3**, and LeWM's entire pitch is *one untuned hyperparameter*. Adding a second is a real cost to the comparison and should be reported with a sweep rather than a lucky value.
- **A2 may simply be worse at everything.** Per-frame colour flicker is not physics. Bad A2 results are evidence about implementation, not mechanism — which is precisely why A3 and not A2 carries the hypothesis.
- **Seed variance.** stable-worldmodel's own LeWM numbers are ambiguous enough that the wiki could not tell which baseline was which. **3 seeds minimum, 5 if Stage 0.5 shows spread.**
- **Generalizing past PushT.** One 2D environment with a point-mass agent. The OGBench-Cube and TwoRoom configs ship with the same repo and would cost little more, and *"colour" in a 3D scene is not the same nuisance it is in a 2D one.*

## Related

- [The abstraction tax](abstraction-tax.md) — the claim this is designed to break.
- [LeWorldModel](../../sources/leworldmodel-paper.md) — the model, and the verified fact that it trains with no augmentation at all.
- [LeVJEPA](../../sources/levjepa-paper.md) — where the A3 declaration comes from, and the evidence that an undeclared axis is *taxed* rather than lost.
- [stable-worldmodel](../../sources/stable-worldmodel-paper.md) — the harness, the perturbation factors, and the collapse being explained.
- [Robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) — the rollout-count discipline this design is bound by.
- [World-action model](../../concepts/world-models/world-action-model.md) — the family the "diversity is not a declaration" argument would generalize to.
- [Ten open questions, and the one the wiki is pointed at](open-questions-and-research-direction.md) — Stage 0 and the Demo-JEPA embodiment probe are the same measurement on two checkpoints; run them in one session.
