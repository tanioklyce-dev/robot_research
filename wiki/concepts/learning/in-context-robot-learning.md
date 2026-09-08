---
title: In-context robot learning
type: concept
created: 2026-08-29
updated: 2026-09-07
sources: 8
tags: [in-context-learning, robot-foundation-model, demonstration-conditioning, test-time-adaptation, vla, skild-ai, s1, generalist-ai, gen-1-5, physical-prompting, emergence]
---

# In-context robot learning

**Adapting a robot policy from information supplied at inference time — a demonstration of the task, or the policy's own recent experience of the body — rather than from a language instruction or from post-training.** The weights do not change; the information enters as context and the policy conditions on it, exactly as an LLM conditions on few-shot examples in its prompt. See [Two modes](#two-modes-often-conflated) — the term is routinely used for both, and they are not the same mechanism.

The framing that makes it precise is a two-loop one, from [S1](../../sources/skild-s1-blog.md): *"Pre-training is the outer loop that teaches the policy how to learn from context; at inference time, the demonstration drives the inner loop without changing any weights."* Pre-training must therefore use episodic data in which **the task is identified only by an in-context demonstration** — otherwise the model has no pressure to learn the inner loop at all, and will simply learn the tasks.

> [!warning] The second vendor instance contradicts exactly that sentence
> [GEN-1.5](../../sources/generalist-gen-1-5-blog.md) ([Generalist AI](../../entities/generalist-ai.md), Aug 2026) reports the same capability from the opposite premise: *"**We did not explicitly train for any of them: no architectural changes to promote in-context learning, no inner or outer meta-learning loop**, no auxiliary objectives."* Pretraining used **randomly sampled continuous spans** with *"no bespoke infrastructure for packing examples into context"* — so their physical prompts *"introduce **discontinuous jumps in time that the model never saw in training**."*
>
> | | **S1** ([Skild](../../entities/skild-ai.md)) | **GEN-1.5** ([Generalist](../../entities/generalist-ai.md)) |
> |---|---|---|
> | The inner loop is | **designed** — structure the episodes so the task is only identifiable from the demo | **emergent** — no structure, no meta-learning, no packing |
> | Scale threshold | yes — crossover at 100k h | yes — *"past a certain threshold of pretraining, the cost of adaptation becomes negligible"* |
> | Evidence | vendor blog | vendor blog |
>
> **They agree on the shape and disagree on the mechanism**, and neither ablates. This is now the most interesting unresolved question on this page, and it is a practical one: if S1 is right, episodic structure is a *requirement* and anyone pretraining without it is wasting the run; if Generalist is right, it is an optimization at best.
>
> What would settle it is one figure neither has published: **in-context ability against pretraining scale, with episodic structure ablated.**

## Why it is a different answer to the specification problem

Every generalist policy has to be told what to do. The field's three answers:

| Approach | Specification | Cost of a new task |
|---|---|---|
| **Post-training / fine-tuning** | task-specific data | hundreds to thousands of demonstrations |
| **Language conditioning** ([VLA](vla-models.md)) | a natural-language instruction | zero, *if* the task is in-distribution; post-training if not |
| **In-context learning** | one demonstration at inference | one demonstration |
| **Latent-goal planning** ([Demo-JEPA](../../sources/demo-jepa-paper.md)) | one demonstration, read as a **goal** | one demonstration **+ the target's own interaction experience** |

> [!note] The fourth row is not in-context learning, and the distinction is the point
> [Demo-JEPA](../../sources/demo-jepa-paper.md) shares this page's headline property — **one demonstration, no weight update at deployment** — and gets there by an entirely different route. There is **no context window and no prompt**. A visual demonstration from another robot is translated into **target-compatible future latent states**, which a planner then reaches under the target's own learned forward dynamics (CEM over a V-JEPA 2.1 world model).
>
> So: *"the target agent should infer **what state** the demonstrator is trying to realize, rather than **how** the demonstrator executes it."* Where in-context learning asks a policy to **generalize from an example**, this asks a planner to **reach a goal inferred from one**. Both cost one demonstration; only one of them is learning-from-context.
>
> **It therefore does not settle the built-vs-grown dispute below** — a correction to how the wiki filed it. What it does supply is the first **non-vendor, published** system in this general family, with ablations.

Language conditioning assumes the instruction is enough to identify the behavior. In-context learning assumes a demonstration is a **richer specification** — it carries the intent, the functional correspondences, and the task progress that language leaves implicit. The cost is that someone must perform the task once, on the spot.

## Two modes, often conflated

The term covers two mechanisms that share an implementation (no weight update, information enters through context) and differ in **what the context contains**:

| | **Demonstration-conditioned** | **Experience-conditioned** |
|---|---|---|
| Context holds | a human demonstration of the *task* | the policy's own trials with this *body* |
| Answers | "what should I do?" | "what am I?" |
| Closest classical analogue | few-shot imitation | online system identification |
| Wiki instance | [S1](../../sources/skild-s1-blog.md) (manipulation) | [LocoFormer](../../sources/locoformer-paper.md) (locomotion) |

Both are [Skild AI](../../entities/skild-ai.md) systems and both are marketed under the same "in-context" banner, but the second does something the first does not: **it improves from its own failures within a deployment.** LocoFormer, given a body so unstable it falls on trial 1, keeps that failure in its Transformer-XL cache and walks by trial 3 — frozen weights throughout. That is in-context *reinforcement* learning; S1 is in-context *imitation*.

Keeping them apart matters when reading claims. "Omni-bodied in-context learning" is evidenced for the experience-conditioned locomotion case and not for the demonstration-conditioned manipulation case.

## Current state

Two sources, of very different evidence grade. The **experience-conditioned** case is peer-reviewed and well-controlled ([LocoFormer](../../sources/locoformer-paper.md), CoRL 2025: 0.96 zero-shot across ten unseen robots against 0.99 per-robot experts, with a GRU ablation collapsing to 0.37). The **demonstration-conditioned** case below is a single vendor blog with no third-party evaluation.

[Skild AI](../../entities/skild-ai.md)'s [S1](../../sources/skild-s1-blog.md) (August 2026) reports a **scaling crossover** rather than a flat advantage:

| Pre-training data | Setting | In-context | Language-conditioned |
|---|---|---|---|
| 1,000 h | seen | **43%** | **53%** |
| 100,000 h | **unseen** | **66%** | **9%** |

**At small scale in-context learning is worse.** It only wins once pre-training is large, and Skild's claim is that the gap then *"widens exponentially."* This is the right shape for the claim to have — an inner loop has to be learned before it can pay, so it should cost something at low data — which is a point in its favor, since it is not the result a vendor would fabricate.

Reported corollaries, all self-reported and none independently evaluated:

- **One in-context demonstration ≈ 380 post-training examples**, which for long-horizon tasks is 50–100 hours of teleoperation compressed into an 11-minute setup.
- **Robustness to prompt-to-deployment mismatch** up to ~30 cm / 45° of object displacement and object substitution; degradation when the demonstration implies a different execution plan (e.g. the other arm).
- **Correction of the demonstration** — the policy reportedly executing a step more cleanly than the demonstrator who showed it, which if real means the demonstration is being read as intent rather than copied as trajectory.

> [!warning] Two vendors now, still no replication, still no named embodiment
> Both demonstration-conditioned sources are blog posts with **no third-party evaluation, no rollout counts, no released weights, and no statement of which robot they run on**. Read the numbers as hypotheses with a plausible shape, not as established results. The [success-rate audit](../../syntheses/platforms/vla-success-rate-audit.md) applies with full force to both.

### The second instance: GEN-1.5

[Generalist AI](../../entities/generalist-ai.md)'s [GEN-1.5](../../sources/generalist-gen-1-5-blog.md) (August 2026) — a 30-second multimodal context window, prompted with **3–12 seconds of a single demonstration**, which they call **physical prompting**:

| Setting | Reported |
|---|---|
| **One-shot in-context**, zero gradient steps | **59% ± 10%** across 10 tasks |
| **10 gradient steps** on 5 min (~50 demos) | **83% ± 9%** |
| **1 gradient step** on 1 min, held-out task | **66.5%** |
| Weight change from 10 steps | **< 0.15%** |

Four capabilities beyond one-shot imitation, none of them in S1:

- **Composition.** Two independently recorded prompts in context chain into one behavior, *"bridging the two with intermediate motions, recoveries, and ambidexterity that appear in neither prompt."* They propose **"physical prompt engineering"** — assemble a compound task from a library of short prompts instead of demonstrating the whole thing.
- **Prompt from simulation.** A demonstration recorded in a simulator prompts the real robot, *"despite zero simulation data in pretraining."* If real, task **specification** can be simulated even when pretraining cannot — which moves the [contact-data problem](../robotics/contact-rich-manipulation.md) one layer down rather than solving it.
- **Human-to-robot**, hedged as *"in some cases."*
- **Improvisation that increases as fine-tuning decreases** — banana as a brush, a dustpan used by lifting-and-dumping, removing an obstacle absent from the task data. Their explanation: *"lightly adapted models stay closer to their pretrained priors."*

> [!note] The clearest number in either source, and it is mechanistic
> **Ten gradient steps change the weights by less than 0.15%** — *"fine-tuning slightly reconfigures knowledge already present rather than building new representations."* It is the quantitative version of what both companies are claiming qualitatively: adaptation *"is closer to reminding the model of something it nearly knows."* Compare [LoRA](low-rank-adaptation.md) and [knowledge insulation](knowledge-insulation.md), where the same intuition is architectural rather than measured.
>
> It also cuts against the emergence framing slightly: if 10 steps and 0.15% get you from 59% to 83%, the in-context route is buying *convenience*, not capability the weights lacked.

> [!note] And a third instance of the same curve
> Demo-JEPA reproduces the shape S1 reports, from a different mechanism: it **loses in-domain** (VPP wins behavior grounding; their own Demo-DP variant beats it 0.65 vs 0.43 real-world) and **wins as distribution shift grows** — zero-shot generalization **0.36 vs VPP's 0.04** in simulation. Together with [the JE-vs-reconstruction crossover](../../sources/joint-embedding-vs-reconstruction-paper.md), that is three unconnected results saying *the abstraction costs you in-distribution and pays out of it.*
>
> Which is a reason to read S1's in-domain loss (43% vs 53%) as evidence **for** the mechanism rather than against it.

> [!warning] What neither source shows
> **That in-context ability emerged at scale.** S1 reports a crossover between two conditions at two data scales; GEN-1.5 reports a validation-loss curve improving over eight months and a model that has ICL at the end of it. Neither publishes **in-context ability against pretraining scale**, which is the actual claim both are making. Until one does, "ICL emerges in robot foundation models past a data threshold" is a hypothesis held by two companies with a commercial interest in it being true.

> [!note] Two places to put a prior, thirty years apart in style
> Both this page's sources and [Oriyama et al. 2025](../../sources/hitl-transfer-learning-collision-avoidance.md) are answers to *how do you make adaptation cheap?* — and they differ in **where the prior is stored**.
>
> | | Prior lives in | Where it came from | New behavior costs |
> |---|---|---|---|
> | **Oriyama et al.** | the **initialization** (transferred weights) | a human writing a **four-branch rule** | ~50 online steps |
> | **[S1](../../sources/skild-s1-blog.md) / [GEN-1.5](../../sources/generalist-gen-1-5-blog.md)** | the **context window** | 100k h / 1.89M scenes of pretraining | one demonstration |
>
> The adaptation budgets land in the same neighbourhood from opposite directions. And the small system measures something the large ones do not: **when the prior stops paying.** Its hand-written prior is significant in the matched environment and **not significant** in a dynamic one (p = 0.441) — *"leaving the robot in a state similar to starting from random actions."* Whether the pretrained equivalent degrades the same way off-distribution is untested by either vendor, and it is the same question in a different coat.

## Relationship to neighboring ideas

- **[Test-time adaptation](test-time-adaptation.md)** — in-context learning is its limiting case: adaptation with *zero* gradient steps.
- **[Sim-to-real transfer](sim-to-real-transfer.md)** — [LocoFormer](../../sources/locoformer-paper.md) is an unusually strong instance: trained only on *procedurally generated robots that do not exist*, transferring zero-shot to ten commercial platforms with no system identification.
- **[VLA models](vla-models.md)** — the language-conditioned alternative, and the baseline S1 measures against.
- **[Scaling laws for VLAs](scaling-laws-vla.md)** — the crossover claim is a scaling-law claim, and belongs to that literature rather than to a leaderboard.
- **[Soft-prompt cross-embodiment](soft-prompt-cross-embodiment.md)** — a different route to conditioning a shared policy without retraining per body.
- **[Imitation learning](imitation-learning.md)** — the parent tradition; ICL is imitation where the demonstration arrives at inference rather than at training.
- **[Crowdsourced robot training data](crowdsourced-robot-training-data.md)** — S1's data table rates egocentric human video highest on diversity and scalability, which is what makes the outer loop trainable at all.

## Prehistory: adaptation before long context

The experience-conditioned mode did not begin with long context. **[RMA](../../sources/rma-paper.md)** (Kumar, Fu, [Pathak](../../entities/deepak-pathak.md) & Malik, RSS 2021) solved the same problem — a robot inferring its own situation online, with no weight update — using **0.5 s of proprioception** and an explicitly engineered two-module design: a privileged teacher produces a latent "extrinsics" vector in simulation, and a small CNN learns to regress it from state–action history at deployment.

Crucially, RMA also **declines to identify the system**: it predicts *how behavior should change*, not the physical parameters, and its ablation shows that predicting the physics directly is **worse** (56.5% vs 73.5%). That is the same instinct long-context in-context learning acts on — the useful latent is behavioral, not physical — reached four years earlier with a hand-built bottleneck instead of attention.

What separates them is horizon and structure, not aim. RMA adapts to **terrain, payload and friction within a trial**; [LocoFormer](../../sources/locoformer-paper.md) adapts to **morphology across trials**, which requires remembering a failure. LocoFormer calls the RMA class *"myopic"* — accurate, and a deliberate choice on RMA's part, made to fit a cheap robot's onboard compute.

## Key references

- [Introducing S1: In-Context Learning for Robotics](../../sources/skild-s1-blog.md) — [Skild AI](../../entities/skild-ai.md), August 2026. Vendor blog; the *designed* outer loop.
- [**Demo-JEPA**](../../sources/demo-jepa-paper.md) — He et al., 2026. The published, non-vendor neighbour: demonstration-as-latent-goal plus planning, with the finding that **V-JEPA 2.1 latents are not embodiment-invariant on their own**.
- [**GEN-1.5: Embodied Foundation Models are One-Shot Learners**](../../sources/generalist-gen-1-5-blog.md) — [Generalist AI](../../entities/generalist-ai.md), August 2026. Vendor blog; the *emergent* outer loop, plus composition, sim-prompting and the 0.15% weight-change number.
- [**RMA: Rapid Motor Adaptation for Legged Robots**](../../sources/rma-paper.md) — Kumar, Fu, Pathak & Malik, RSS 2021. The prehistory: fixed 0.5 s window, explicit adaptation module, privileged teacher.
- [**LocoFormer: Generalist Locomotion via Long-context Adaptation**](../../sources/locoformer-paper.md) — Liu, [Pathak](../../entities/deepak-pathak.md) & Agarwal, CoRL 2025. The experience-conditioned instance, and the better-evidenced of the two: peer-reviewed, with baselines (GRU 0.37 vs 0.96) and per-robot expert upper bounds (0.99).

## Mentioned in

- [Introducing S1](../../sources/skild-s1-blog.md) — the demonstration-conditioned mode.
- [GEN-1.5](../../sources/generalist-gen-1-5-blog.md) — the second demonstration-conditioned instance, and the contradiction about mechanism.
- [Demo-JEPA](../../sources/demo-jepa-paper.md) — the fourth specification route: one demonstration read as a latent goal for a planner.
- [LocoFormer](../../sources/locoformer-paper.md) — the experience-conditioned mode.
- [Skild AI](../../entities/skild-ai.md) — the company behind both.
- [RMA](../../sources/rma-paper.md) — the pre-long-context ancestor.
- [Locomotion adaptation lineage](../../syntheses/rl/locomotion-adaptation-lineage.md) — the full 2021→2025 arc these two sit at either end of.
- [Deepak Pathak](../../entities/deepak-pathak.md) — co-author of both LocoFormer and RMA.

> [!note] How to read S1's in-domain loss (2026-09-07)
> [The abstraction tax](../../syntheses/world-models/abstraction-tax.md) collects three unconnected instances of *loses in-distribution, wins under shift* and argues the in-domain deficit is **corroborating evidence for the mechanism, not a defect** — a method that claims to abstract and costs nothing in-distribution is probably not abstracting. On that reading S1's **43% vs 53%** at 1k h is the expected shape rather than the weak spot.
>
> The page also narrows what ICL should be expected to generalize *over*: pre-training episodes specify the task **only** by an in-context demonstration, so the declared axis is *which task this is* — and nothing in that procedure declares a new kitchen, a new object, or a new robot irrelevant.
