---
title: "The abstraction tax — and the one direction of shift it buys"
type: synthesis
created: 2026-09-07
updated: 2026-09-07
tags: [abstraction, generalization, out-of-distribution, joint-embedding, in-context-learning, jepa, scaling, crossover, augmentations, synthesis]
---

# The abstraction tax — and the one direction of shift it buys

In one week the wiki recorded the same curve from **three unconnected mechanisms**, and noted it three times without ever writing it down as a claim. This page writes it down, then does the thing that makes it useful: finds the case where it fails, and narrows it until the failure fits.

**The pattern:** *a method that discards information loses to one that keeps it when the test looks like training, and beats it as the test moves away.*

**The narrowed version, which is the actual content of this page:** *the abstraction buys robustness only to shift along the axis it was told to discard, and buys nothing anywhere else.* "Out-of-distribution" is not one direction, and treating it as one is how the pattern gets over-claimed.

## The three instances

| | Method that abstracts | Method that keeps detail | In-distribution | Under shift |
|---|---|---|---|---|
| **[S1](../../sources/skild-s1-blog.md)** (Skild, 2026) | in-context learning | language-conditioned VLA | **43% vs 53%** at 1k h — ICL loses by 10 | **66% vs 9%** on unseen tasks at 100k h — ICL wins by 57 |
| **[Joint-Embedding vs Reconstruction](../../sources/joint-embedding-vs-reconstruction-paper.md)** (van Assel, …, Balestriero, NeurIPS 2025) | joint-embedding (DINO) | reconstruction (MAE) | reconstruction preferable when irrelevant features are **low-magnitude** | **MAE degrades 2.4× as much as DINO** under ImageNet-C (25.1% vs 10.5% average drop) |
| **[Demo-JEPA](../../sources/demo-jepa-paper.md)** (He et al., 2026) | latent-goal planning | trajectory learning (VPP; their own Demo-DP) | **0.43 vs 0.65** real-world behavior grounding — Demo-JEPA loses | **0.36 vs 0.04** sim zero-shot; 0.25 vs 0.15 real zero-shot |

Three different fields — robot policy specification, image SSL theory, cross-embodiment imitation. No two of these papers cite each other. Two are vendor-free, one has a proof, and **one of the three publishes its own losing ablation** (Demo-DP beats Demo-JEPA in-domain and the authors report it anyway).

A fourth sits *inside* a single comparison: **[LeVJEPA](../../sources/levjepa-paper.md)** at matched FLOPs beats VideoMAEv2 by **+7.6 on ImageNet** and **loses SSv2 by 3.2** — appearance-centric evaluation favours the joint-embedding encoder, motion-centric favours reconstruction, in one table. Neither paper reads it that way; recorded on that page as an observation.

## Why it is not a coincidence

[Joint-Embedding vs Reconstruction](../../sources/joint-embedding-vs-reconstruction-paper.md) is the only one of the three with a mechanism, and it supplies the whole explanation. Under linear models, the deciding quantity is **the magnitude of the irrelevant features**:

> When irrelevant features have **low magnitude** and there is limited prior information on effective augmentations, **reconstruction is preferable**. In contrast, when these irrelevant features are **non-negligible** (as is common with real-world data) or effective augmentations can be identified, **joint-embedding is preferable**.

Reconstruction is not stupid in the easy regime — it is *correct*: when the important components already carry the most magnitude, a reconstruction objective prioritizes them for free and needs no one to tell it what to ignore. The abstraction's cost is the price of a statement about relevance that the easy regime did not require.

**This immediately explains the in-domain loss.** Any method that throws information away is running a bet that the discarded part will not be needed. In-distribution, some of it is. The in-domain deficit is not a flaw the method should be expected to grow out of with scale — **it is the receipt.**

> [!note] Which inverts how the S1 result should be read
> The wiki filed [S1](../../sources/skild-s1-blog.md)'s 43-vs-53 as the weak spot in a vendor post. On this reading it is the opposite: **a method claiming to abstract, that costs nothing in-distribution, is probably not abstracting.** The in-domain loss is corroborating evidence for the mechanism Skild claims, and its absence would have been the thing to worry about.
>
> This does not rescue the post's other problems — no rollout counts anywhere, and the 66-vs-9 gap is a trend claim across a 100× sweep, not a benchmark placement.

## The counterexample, which is the useful part

If abstraction bought out-of-distribution robustness in general, then the most abstract world model in the wiki should be the most robust one. It is not.

**[stable-worldmodel](../../sources/stable-worldmodel-paper.md)** (Balestriero's own group) measures [LeWorldModel](../../entities/leworldmodel.md) — a [SIGReg](../../concepts/world-models/sigreg.md) JEPA, single distributional regularizer, [identifiability theorem](../../concepts/world-models/identifiability.md) attached, about as committed to latent abstraction as anything built:

| Push-T | LeWorldModel |
|---|---|
| base task | **50.8%** |
| under targeted **color / size / shape** change | **6–26%** |
| with distractor objects | **quadratic collapse**, across all baselines |

Nothing here contradicts the three instances. But it does kill the general form of the claim, and the wiki should stop reaching for "latent implies robust" — a habit two of this week's sources caught it in.

## The narrowed claim: shift is not one direction

Read the counterexample through the theorem and it stops being a counterexample.

In that framework the augmentation **is** the statement of what is irrelevant, and the theorem's sharpest line is that **no amount of data substitutes for it**: the alignment requirement *"persists even as the sample size n becomes arbitrarily large."* Supervised learning has a second escape route — labels supply an independent signal about what to ignore — and SSL does not.

So the mechanism is not *abstraction → robustness*. It is:

> **The training procedure declares some axis irrelevant. The method becomes robust along that axis and no other. Shift along an undeclared axis is exactly as damaging as it would be to a model that abstracted nothing.**

Every row lines up once you ask *what was declared*:

| | Declared irrelevant by the training | Shift measured | Result |
|---|---|---|---|
| **S1** | *which task this is* — pre-training episodes specify the task **only** by an in-context demonstration | unseen tasks | pays, hugely |
| **DINO vs MAE** | whatever the augmentation set covers | ImageNet-C corruptions | pays, ~2.4× |
| **Demo-JEPA** | *which robot this is* — the Dreamer Predictor is trained on cross-embodiment demo pairs | new embodiment | pays |
| **LeWorldModel** | **nothing** — verified 2026-09-07: no augmentation of any kind, and SIGReg constrains the *shape of the representation*, not which input variations to discard | agent color, size, shape | **does not pay** |
| **LeVJEPA** | **where you crop spatially, photometric appearance, and which tokens you see** — verified 2026-09-07. All views *“share the identical temporal window and differ only spatially and photometrically.”* **Nothing is declared about time.** | appearance (IN1K) vs motion (SSv2) | **pays +7.6 on the declared axis, loses 3.2 on the undeclared one** |

SIGReg is the clean case because it is the honest one. It is derived from [identifiability](../../concepts/world-models/identifiability.md) — *the isotropic Gaussian is minimax-optimal under task uncertainty* — and that is a claim about latent geometry. **It never says color does not matter.** Nothing in the objective could make it robust to a color shift, and the measurement agrees.

### Checked, 2026-09-07: LeWorldModel declares nothing, and its objective actively preserves the thing that breaks it

This page originally hedged here — LeJEPA carries a multi-view invariance loss on top of SIGReg, so perhaps LeWM inherited an augmentation-based declaration after all. **It did not.** Verified against the [paper](../../sources/leworldmodel-paper.md), its Appendix D implementation details, and the [`le-wm` source and configs](https://github.com/lucas-maes/le-wm):

- The word **"augment" appears zero times** in the paper. So do *crop*, *jitter*, *flip*, and *blur*. Every occurrence of *color* is the violation-of-expectation **perturbation** they test, never a transform they train with.
- The entire image pipeline is `get_img_preprocessor` → **`ToImage(imagenet_stats)` + `Resize(224)`**, plus z-score normalization of the action/proprio/state columns. **Deterministic. No stochastic augmentation anywhere.**
- **LeWM is not LeJEPA.** It borrows SIGReg and *not* the multi-view invariance loss. Its two terms are `L_pred = ‖ẑ_{t+1} − z_{t+1}‖²` — action-conditioned next-frame latent prediction, teacher-forced, causally masked — and `λ·SIGReg(Z)`. **The positive pair is (frame *t*, frame *t+1*), not (aug₁(x), aug₂(x)).** Temporal adjacency is the invariance signal.

So the narrowed claim survives the check. But the finding is better than "no declaration was made", because it supplies a **mechanism** rather than an absence:

> [!warning] A next-frame prediction objective does not merely ignore static nuisance attributes — it is paid to keep them
> Temporal prediction declares the **unpredictable** irrelevant. The agent's colour, size and shape are the **most predictable features in the scene**: constant across every frame of every trajectory. Encoding them is free accuracy on `L_pred`, and discarding them costs.
>
> So LeWM does not have "no incentive to discard colour." **It has a positive incentive to encode it** — and stable-worldmodel then perturbs exactly the attributes the objective was rewarded for preserving. The 50.8% → 6–26% collapse is not a surprise about abstraction; it is the objective working as specified.
>
> **This generalizes past LeWM.** Any latent world model whose only invariance signal is temporal prediction — [DINO-WM](../../entities/dino-wm.md), [PLDM](../../entities/pldm.md), LeWM — should preserve static scene attributes and be brittle to shift in exactly those. Which is what [stable-worldmodel](../../sources/stable-worldmodel-paper.md) reports: the distractor collapse is *"quadratic across all baselines."* **The [world-action model](../../concepts/world-models/world-action-model.md) family has no mechanism for declaring a static attribute irrelevant, and none of these papers claims one.**

> [!warning] Demo-JEPA ran the controlled version of this by accident
> The best evidence for the narrowed claim is a single ablation inside one paper, because it holds the abstraction fixed and varies only whether the axis was declared.
>
> - **Naive reference** — plan directly toward the source demonstration's own V-JEPA 2.1 future latent. Same encoder, same latent space, *never told that embodiment is a nuisance variable*. Result: *"**fails across all tasks**."*
> - **Demo-JEPA** — the identical latent space, plus a module trained on cross-embodiment demonstration pairs, i.e. explicitly told what to abstract over. Result: *"closely approaches the oracle."*
>
> **One latent space, two outcomes, and the difference is whether anything declared the axis.** That is as close to a controlled experiment on this page's claim as the wiki holds, and its authors were testing something else.

### Checked, 2026-09-07: LeVJEPA is LeWM's exact complement

The follow-up question — does [LeVJEPA](../../sources/levjepa-paper.md)'s global/local view construction carry photometric augmentation — has a clean answer: **yes, explicitly.**

> …V local views obtained by **aggressive spatial cropping and photometric augmentation**. All views **share the identical temporal window and differ only spatially and photometrically.**

So the two models built on the same regularizer declare **disjoint** axes, and each is brittle exactly where it declared nothing:

| | Invariance signal | Declares irrelevant | Wins | Loses |
|---|---|---|---|---|
| **[LeWorldModel](../../sources/leworldmodel-paper.md)** | temporal adjacency: predict frame *t+1* from *t* | the **unpredictable** | — | **static appearance**: 50.8% → 6–26% under colour/size/shape |
| **[LeVJEPA](../../sources/levjepa-paper.md)** | spatial + photometric views, **identical temporal window** | **spatial position, appearance, which tokens you see** | **appearance: +7.6 IN1K** over the strongest baseline | **motion: −3.2 SSv2** |

Same family, same [SIGReg](../../concepts/world-models/sigreg.md), opposite declarations, opposite failure modes. Neither paper frames it this way and neither cites the other's weakness.

**And the split is visible inside a single ablation.** Sweeping the token-drop ratio ρ, ImageNet accuracy *"increases monotonically"* — 33.9 → 47.6 from ρ=0 to 0.95 — while on Something-Something-v2, *"which primarily probes motion understanding, **accuracy declines for dropping ratios beyond 0.3**, in contrast to the monotonic improvement observed on ImageNet."* Their own reading of why is this page's mechanism in the authors' words: sparse random observations render *"motion cues, which depend on correspondences across frames, less frequently recoverable within a single view."* One knob, two directions, split by whether the axis was declared.

> [!warning] The honest complication, and it changes how strongly this page can be stated
> LeVJEPA reports the motion loss is **partly recoverable with compute**: *"with longer training, higher dropping ratios **recover** the accuracy of lower ones on Something-Something-v2 while retaining their lower per-iteration cost."*
>
> That weakens the claim from *the abstraction destroys the undeclared axis* to **the abstraction taxes it** — a per-sample-signal effect that more iterations partly buy back, not a hard representational limit. Their framing: *"additional iterations compensate for the reduced per-sample signal."*
>
> It does not dissolve the finding — the FLOP-matched headline still **loses SSv2 by 3.2 on a 1,085-epoch schedule**, which is not a short one, and they name *"dropping schemes that preserve motion information at high sparsity"* as unsolved future work. But wherever this page says an undeclared axis is *lost*, the defensible word is **taxed**, at an exchange rate nobody has measured.

> [!note] A second thing worth taking from the recipe: the asymmetry comes from the views
> *"As the global view is the only view that remains **photometrically unaltered** and covers the largest spatial extent, it constitutes the prediction target **by construction of the views alone**."*
>
> [The anti-collapse lineage](ssl-anti-collapse-lineage.md) established that branch **asymmetry** is the load-bearing ingredient and that the EMA is one substitutable source of it. LeVJEPA supplies another: **augmentation asymmetry**. The teacher is not a slower copy of the student — it is the same encoder shown the least-corrupted view.

## What this is worth in practice

A decision rule that is actually usable, and narrower than "use a JEPA":

1. **Name the shift you expect at deployment before choosing the method.** Not "generalization" — the axis. New objects? New lighting? New task? New robot? The abstraction only helps if you can name it.
2. **Then check that the training procedure says something about that axis.** An augmentation, an episode structure, a paired-data module, an inverse-dynamics term. A regularizer that shapes the *latent distribution* — SIGReg, VICReg, a Gaussian prior — is not such a statement, however principled.
3. **If it does, budget for the in-domain loss and do not read it as a defect.** Ten points on S1, 22 on Demo-JEPA real-world. If a method claims abstraction and costs nothing in-distribution, be suspicious rather than pleased.
4. **If it does not, you are paying the tax and buying nothing.** This is the LeWorldModel case, and it is the common one.

For [in-home deployment](../assistive/long-term-in-home-robot-deployments.md) specifically, the axes that matter are *this house, not that house* and *this mug, not that mug* — object identity, layout, lighting, clutter. Nothing in the JEPA line's standard objectives declares any of those irrelevant. **The relevant question for that setting is not "JEPA or diffusion policy" but "what in this recipe tells the model that the kitchen is different from the one in the data."**

## Where this could be wrong

- **One of the three instances is a vendor blog with no rollout counts**, one is a v1 preprint with 20–30 rollouts per cell, and one is a theorem about **linear** models validated on ImageNet-C. Any single instance is weak. The argument rests on their independence, which is a weaker form of evidence than it feels like.
- **"Declared irrelevant" is doing a lot of work and is not always crisp.** ~~The clean SIGReg story needs checking against which augmentation set LeWorldModel actually used.~~ **Checked 2026-09-07 and it held — LeWM uses no augmentation at all** (above). ~~The residual imprecision is elsewhere: whether LeVJEPA's views carry photometric augmentation is unverified.~~ **Also checked 2026-09-07 — they do, and the two models turn out to be exact complements** (above). What remains imprecise is the *strength* of the effect: LeVJEPA shows the undeclared axis is partly recoverable with a longer schedule, so **"taxed" is defensible and "lost" is not.**
- **The counterexample may just be a weak model.** [stable-worldmodel](../../sources/stable-worldmodel-paper.md) reports a quadratic distractor collapse *across all baselines*, which is consistent with "current world models are brittle" rather than with anything specific about declared axes.
- **Selection.** Three instances arrived in one week of ingesting, chosen partly because they were interesting. The wiki has not gone looking for methods that abstract, cost nothing in-domain, and generalize anyway — which is the shape that would falsify the first claim.

## The experiment that would settle it

**Designed in full: [The declared-axis experiment](declared-axis-experiment.md)** — four arms on [LeWorldModel](../../sources/leworldmodel-paper.md), ~1–2 GPU-days, with a **stage-0 probe on the released checkpoint** that tests half the mechanism before anything is trained.

Writing the design surfaced two things the one-line version got wrong, and both are findings rather than details:

- **Color is task-relevant in [PushT](../../entities/pusht.md)** — blue agent, gray block, green goal outline. Global jitter destroys the task instead of declaring a nuisance irrelevant, so the declaration has to target *agent* color and be re-rendered through the simulator.
- **Data diversity is not a declaration.** Sampling agent color per trajectory leaves it **perfectly predictable frame-to-frame**, so `L_pred` is unchanged and the objective is *still paid to encode it*. In a temporal-prediction world model the standard augmentation playbook does not apply, because that playbook assumes a positive pair of two views of **one frame**. Isolating this is what the design's A1 arm is for.

The naive version, kept for the record: **train one JEPA twice on identical data — once with color jitter, once without — and measure Push-T success under color shift.** The narrowed claim predicts the declared-color model holds and the other collapses to stable-worldmodel's 6–26%, while both score the same in-distribution. If the color-jitter model *also* collapses, the "declared axis" mechanism is wrong and this page is a pattern-match.

Two more, in rough order of cost:

- **A linear probe for embodiment identity** on V-JEPA 2.1 latents ([already filed](../../backlog.md) from the Demo-JEPA ingest). The naive-reference failure proves something embodiment-specific survives encoding; this measures how much, and whether the Dreamer Predictor removes it or routes around it.
- **Separate the framing from the latent.** Demo-DP applies demonstration-as-goal to a diffusion policy and beats Demo-JEPA in-domain while losing zero-shot. If the *goal-centric framing* is what generalizes and the *JEPA latent* is what costs in-domain accuracy, they are separable — and this page predicts a specific split.

## Related

- [JEPA for a household mobile manipulator](jepa-for-household-mobile-manipulator.md) — where this page's "what declares the kitchen different" question becomes the deciding limit in a platform decision.
- [SSL anti-collapse lineage](ssl-anti-collapse-lineage.md) — the devices that make abstraction possible at all, and the reason it costs something.
- [Generative video vs JEPA world models](generative-video-vs-jepa-world-models.md) — the same crossover, scoped to that one comparison.
- [What world models are measurably good for](what-world-models-are-measurably-good-for.md) — the measurement side, including where the claims outrun the evidence.
- [JEPA](../../concepts/world-models/jepa.md) — including the measured limit on what a JEPA latent abstracts away.
- [In-context robot learning](../../concepts/learning/in-context-robot-learning.md) — where the S1 row is argued in full.
- [Identifiability](../../concepts/world-models/identifiability.md) — why SIGReg's target is a claim about latent geometry and not about relevance.
- [Robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) — the rollout counts that decide which gaps above survive.

## Sources used in this synthesis

- [S1 — Skild AI](../../sources/skild-s1-blog.md) · [Joint-Embedding vs Reconstruction](../../sources/joint-embedding-vs-reconstruction-paper.md) · [Demo-JEPA](../../sources/demo-jepa-paper.md) — the three instances.
- [stable-worldmodel](../../sources/stable-worldmodel-paper.md) — the counterexample that narrowed the claim.
- [LeVJEPA](../../sources/levjepa-paper.md) — the within-one-table version, and the token-dropping caveat.
- [Dawid & LeCun lecture notes](../../sources/dawid-lecun-lvebm-lecture-notes.md) — *"every model that can be multimodal is susceptible to collapse"*; the general form of "abstraction has a price."
- [GEN-1.5](../../sources/generalist-gen-1-5-blog.md) — the other side of the scale argument, and the one the theorem contradicts on augmentation alignment.
