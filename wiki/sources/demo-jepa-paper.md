---
title: "Demo-JEPA: JEPA for One-shot Cross-Embodiment Imitation (He et al., 2026)"
type: source
url: https://arxiv.org/abs/2605.20811
fetch_url: https://arxiv.org/pdf/2605.20811v1
local_path: raw/2605.20811v1.pdf
sha256: a4b084d8b213a8cd6d6bc1d0e27f3073e97bd88dd2041d53836f9cf97365e287
author: "Jingyang He, Guangrun Li, Jieyu Zhang, Chengkai Hou, Zhengping Che, Shanghang Zhang"
published: 2026-05-20
venue: "arXiv preprint (v1 only), cs.RO. 19 pp."
format: paper (PDF)
tags: [demo-jepa, cross-embodiment, imitation-learning, jepa, v-jepa-2, latent-planning, cem, rlbench, one-shot, world-action-model, dreamer-predictor]
ingested: 2026-09-07
---

## Summary

**Treat a demonstration as a statement of *what state to reach*, not *how to move* — then plan to it in latent space.** Demo-JEPA takes a visual demonstration from one robot (Sawyer in sim, UR5e in the real world), translates it into **target-compatible future latent states** for a different robot (Franka), and reaches them by **CEM planning under the target's own learned forward dynamics**. No shared action space, no retargeting, no action-level correspondence — the source provides **observations only**.

> Rather than asking *how* an action should be reproduced, we ask **what future state the demonstration is trying to realize**.

Tier-1 pick from [the awesome-jepa triage](awesome-jepa-github.md), filed on the expectation that it would put non-vendor evidence into the [in-context learning](../concepts/learning/in-context-robot-learning.md) dispute. **That framing was wrong and is corrected below** — it is a different answer to the same problem, not a data point in that argument, which makes it more useful rather than less.

> [!warning] Correction to how this was filed
> The backlog described this as *"the first non-vendor evidence in the S1-vs-GEN-1.5 dispute"* over whether the in-context inner loop is **built or grown**. **Demo-JEPA is not in-context learning at all.** There is no context window, no prompt, no frozen policy conditioning on examples. The demonstration is consumed as a **goal specification for a planner**.
>
> It shares ICL's headline property — one demonstration, no weight update at deployment — and arrives there by an entirely different mechanism. So it adds a **fourth row** to the specification-problem table on that page rather than settling its argument.

## The four ways to tell a robot what to do

| Approach | Specification | Mechanism | Cost of a new task |
|---|---|---|---|
| Post-training | task-specific data | gradient descent | hundreds–thousands of demos |
| Language conditioning ([VLA](../concepts/learning/vla-models.md)) | an instruction | attention over text | zero if in-distribution |
| [In-context](../concepts/learning/in-context-robot-learning.md) ([S1](skild-s1-blog.md), [GEN-1.5](generalist-gen-1-5-blog.md)) | one demo **in the context window** | learned inner loop over a prompt | one demonstration |
| **Demo-JEPA** | one demo **as a latent goal** | **translate to target latents, then plan** | one demonstration **+ the target's own interaction experience** |

The last column is the honest cost. Demo-JEPA does not need cross-embodiment *action* data, but it does need the target robot to have learned its own forward dynamics — *"the target agent's own interaction experience."* That is cheaper than co-training across embodiments and it is not free.

## How it works

**World model**: **V-JEPA 2.1** as an action-conditioned world model. Encoder `z = E(o)`, dynamics `ẑ_{k+1} = F_wm(z_k, s_k, a_k)`. Planning solves `argmin_a d(F_wm(z_k, s_k, a), z_goal)` by **Cross-Entropy Method**.

**Dreamer Predictor** — the contribution. At each step it sees the current *target* observation plus a **source frame pair** `(o^s_k, o^s_{k+n})`, and emits the latent goal. Two cross-attention modules separate the two things that have to be figured out:

- `f_emb = Attn(Q = z^t_k, K,V = z^s_k)` — **cross-embodiment correspondence** (what does the source's state mean for *my* body?)
- `f_mot = Attn(Q = z^s_{k+n}, K,V = z^s_k)` — **temporal evolution** (where is the demonstration going?)

Fused by a 3D convolution, decoded by a transformer into `ẑ_goal`.

**Three-stage training**: pretrain the action-conditioned world model; train the Dreamer Predictor on **action-free** cross-embodiment demo pairs against a latent reconstruction loss; then freeze it and co-train the dynamics predictor. A nice regularizer in stage 1 — **temporal perturbation**, sampling `(o^s_{k+δ}, o^s_{k+n})` with `δ ~ U(−r, r)`, *"forcing it to maintain robust goal alignments"* against the off-distribution states that imperfect planning will actually produce at inference.

## The result that matters most is a negative one

> [!warning] A shared JEPA latent space does **not** abstract away embodiment for free
> They test the obvious shortcut — a *"naive reference"* that plans directly toward the **source demonstration's own future latent**, skipping the Dreamer Predictor entirely:
>
> > **The naive reference fails across all tasks**, indicating that **V-JEPA 2.1 alone does not provide cross-embodiment goal compatibility.**
>
> Demo-JEPA meanwhile *"closely approaches the oracle"* — a privileged upper bound using the target's ground-truth future trajectory.
>
> This wiki's [JEPA](../concepts/world-models/jepa.md) material tends to treat "latent" as implying "abstract," and the whole appeal of latent prediction is that it discards what does not matter. **This is a measured counterexample: the latent still encodes which robot you are, and an explicit translation module is required.** Worth setting against [LeVJEPA](levjepa-paper.md)'s emergent semantic patch tokens — semantic organization and embodiment-invariance are different properties, and one does not deliver the other.

## The pattern in the numbers

Three evaluation suites at increasing distribution shift. Simulation is 30 rollouts/scenario, real world 20.

| Suite | | Demo-JEPA | VPP | XSkill |
|---|---|---|---|---|
| **Simulation** | behavior grounding | — | **best** | — |
| | cross-embodiment bridging | **0.45** | 0.28 | 0.17 |
| | zero-shot generalization | **0.36** | 0.04 | 0.03 |
| **Real world** | behavior grounding | 0.43 | **best** | — |
| | cross-embodiment bridging | **0.55** | — | — |
| | zero-shot generalization | **0.25** | — | — |

**It loses in-domain and wins out-of-domain, consistently.** The authors state it plainly: *"VPP performs best in behavior grounding, suggesting its advantage in in-domain trajectory learning. However, Demo-JEPA shows stronger performance as the distribution shift increases."*

And their own **Demo-DP** ablation sharpens this rather than hiding it — applying the same demonstration-as-goal idea to a Diffusion Policy beats Demo-JEPA on real-world behavior grounding (**0.65 vs 0.43**) and cross-embodiment bridging (**0.73 vs 0.55**), and loses only where it matters for the thesis: **zero-shot, 0.15 vs 0.25**.

> [!note] The third independent instance of one shape this week
> *The abstraction costs you in-domain and pays off out-of-domain* is now the wiki's most-repeated empirical pattern, from three unconnected places:
>
> - **[S1](skild-s1-blog.md)**: in-context learning **loses** at 1k h (43% vs 53%) and **wins** on unseen tasks at 100k h (66% vs 9%).
> - **[Joint-Embedding vs Reconstruction](joint-embedding-vs-reconstruction-paper.md)**: joint-embedding wins precisely when irrelevant features are large — i.e. when the nuisance variation is big.
> - **Demo-JEPA**: latent-goal planning loses to trajectory learning in-domain and beats it 0.36-to-0.04 zero-shot.
>
> Different mechanisms, same curve. It is also the reason the in-domain losses should not be read as weakness — a method that never costs anything in-distribution probably is not abstracting.

**Setup**: RLBench, **Sawyer → Franka** in sim; **UR5e → Franka** in the real world, six tasks (lift cup, lift cube, remove plate, press button, remove pot lid, remove pepper). Real-world source/target demos are independent and aligned frame-wise using **GTCC** progress-aware features — the wiki has nothing on temporal alignment of unpaired cross-embodiment video, and it is the piece that makes the real-world half possible.

## Where to hold it at arm's length

- **v1 only, no venue.** Single arXiv version.
- **30 sim / 20 real rollouts per scenario.** By the [wiki's standard](../concepts/robotics/robot-policy-evaluation.md) that is roughly ±18–20 pp, so the **0.36 vs 0.04** zero-shot gap survives comfortably and the **0.55 vs 0.43** style comparisons do not.
- **Absolute success rates are low** — 0.25–0.55 outside the in-domain suite. This is a *relative* result about robustness under shift, not a deployable policy.
- **One source→target pair per domain.** "Cross-embodiment" is tested as Sawyer→Franka and UR5e→Franka: three 6-7 DoF arms with parallel grippers. The abstract's *"radically different embodiment configurations"* is doing more work than the experiments support; **no human demonstrator, no hand, no mobile base.**
- **The tasks are not [contact-rich](../concepts/robotics/contact-rich-manipulation.md).** Lift, remove, press — pick-and-place with fixed post-grasp contact. Given that the whole method plans in a *visual* latent, the [force-vs-vision question](tau-touch-augmented-vla-paper.md) is untouched here.

## Entities mentioned

- [V-JEPA 2](../entities/v-jepa-2.md) — V-JEPA 2.1 is the world-model backbone. [Franka Panda](../entities/franka-panda.md) — the target embodiment throughout.
- **VPP**, **XSkill**, **GTCC**, **Sawyer**, **UR5e** — no pages. **Shanghang Zhang** (senior author) — no page.

## Concepts touched

- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the fourth row added to its specification table, and the correction to how this was filed.
- [World-action model](../concepts/world-models/world-action-model.md) — an action-conditioned world model used in the **policy** mode via planning, with goals supplied from another embodiment.
- [JEPA](../concepts/world-models/jepa.md) — and the measured limit on what a JEPA latent abstracts away.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — CEM rather than gradients, in the same latent-planning family; compare [PLDM](pldm-paper.md).
- [Imitation learning](../concepts/learning/imitation-learning.md) — the objective-centric reframing of what a demonstration *is*.

## Open questions

- **Does it work from human video?** The pitch is embodiment-agnostic imitation, and every experiment is arm→arm. A human hand demonstrating is the case that would make this matter, and is exactly where [GEN-1.5's](generalist-gen-1-5-blog.md) hedged *"in some cases"* human-to-robot claim also sits.
- **What is in the latent that identifies the embodiment?** The naive-reference failure proves *something* embodiment-specific survives V-JEPA 2.1 encoding. Nobody has said what. A probe for embodiment identity on those latents is a small experiment with a clean answer.
- **Would a [block-causal encoder](levjepa-paper.md) change the planning cost?** CEM over a bidirectional world model re-encodes per step. LeVJEPA's causal encoder *"extends to incoming frames without re-encoding"* — the same substitution question raised on [mimic-video](mimic-video-paper.md), now in a planning loop rather than a policy.
- **Is the in-domain loss avoidable, or is it the price of abstraction?** Demo-DP beats Demo-JEPA in-domain using the same goal-centric idea with a diffusion policy. If the goal-centric *framing* is what generalizes and the JEPA latent is what costs in-domain accuracy, the two could be separated — and no one has tried.
