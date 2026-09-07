---
title: "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (Zhang et al., 2025)"
type: source
url: https://arxiv.org/abs/2503.03480
fetch_url: https://arxiv.org/pdf/2503.03480v4
local_path: raw/2503.03480v4.pdf
sha256: 91d8a7eeadc5841ef2328c242e9eb1197eecd9ab769c94c4bd9e2eaceaa68d13
author: "Borong Zhang, Yuhao Zhang, Jiaming Ji (equal contribution), Yingshan Lei, Yishuai Cai, Josef Dai, Yuanpei Chen, Yaodong Yang (Institute for AI, Peking University; PKU-PsiBot Joint Lab; State Key Lab of General AI; Zhongguancun Academy)"
published: 2025-03-05
venue: "NeurIPS 2025 (Spotlight). arXiv v1 2025-03-05 → v2 2025-05-31 → v3 2025-11-06 → **v4 2026-04-19**, the version read here"
format: paper (PDF/HTML, 32 pp. incl. appendices)
tags: [safevla, safe-rl, cmdp, lagrangian, vla, safety-alignment, safety-chores, ai2thor, procthor, benchmark, mobile-manipulation, pku, constrained-learning]
ingested: 2026-09-07
---

## Summary

**Make the VLA safe by constraining how it is trained, rather than by filtering what it does.** SafeVLA formulates VLA fine-tuning as a **constrained MDP** — maximize task return subject to a cap on cumulative safety cost — and solves it with Lagrangian relaxation, with the multiplier adapted online rather than fixed. Around that it builds the other three pieces it argues are inseparable from the optimizer: a **formal specification** of unsafe behavior as logical predicates, a **risk-elicitation environment** designed to make those behaviors happen, and an **assurance protocol** that tests the aligned policy on long-tail and extreme-failure cases. The four together are the **Integrated Safety Approach (ISA)**.

Headline: **83.58% lower cumulative cost than the strongest task-focused RL baseline, with task success maintained (+3.85%)**, on long-horizon navigation-plus-manipulation tasks in a new benchmark, **Safety-CHORES**.

This was ingested because it is the single most load-bearing external citation in the [contact-rich safe-learning survey](safe-learning-contact-rich-survey.md), which leans on it across roughly ten sections for its foundation-model claims. It is a substantial paper. It also does not support the weight the survey puts on it, for a reason the survey's own definitions make unambiguous.

> [!warning] The paper the contact-rich survey rests on is not about contact-rich tasks
> Safety-CHORES has three tasks: **Safety-ObjNav** (navigate rooms to find an object), **Safety-PickUp** (pick an object off a surface), **Safety-Fetch** (both). By [the survey's own §2.1 definition](safe-learning-contact-rich-survey.md), navigation is not contact-rich and **simple pick-and-place is explicitly excluded** — the contacts are fixed after the grasp.
>
> The cost function makes it sharper. The five safety predicates are **corners** (stuck / repeated collisions), **blind spots** (collision with a previously-seen but currently-unobserved obstacle), **fragile collections** (collateral displacement during manipulation), **critical points** (destabilizing a precariously placed object), **dangerous equipment** (prohibited interaction with a hot stovetop or exposed wiring). Every one is a **discrete collision-or-interaction event with simulator ground truth**. **There is no force anywhere in this paper** — no wrench, no impedance, no compliance, no contact-mode reasoning.
>
> So the survey's chapter on foundation-model safety in contact-rich manipulation is anchored on a paper working in a different regime with a different hazard model. That does not make SafeVLA wrong; it makes the survey's citation of it wrong. And it independently confirms the survey's own complaint that **no standardized contact-force evaluation protocol exists** — SafeVLA is the field's flagship VLA-safety result and it does not supply one.

## The four parts, and which one the ablations say matters

**1. Modeling — safety as compositional predicates.** Two forms. State-action: `φ(s,a) = 1 ⟺ Pₛ(s) ∧ Pₐ(a) ∧ R(s,a)` — a condition on the state, a condition on the action, and a **risk-inducing relation** between them. Trajectory-level: `ψ(τ) = 1` if there exist timesteps satisfying a conjunction of event predicates plus a **temporal** relation. Corners and dangerous equipment are state-action; blind spots, fragile collections and critical points are trajectory-level.

This is worth keeping independent of the rest of the paper. It is a **compact, checkable specification language for "what counts as unsafe"** that separates the physical condition from the temporal pattern — and the trajectory form is what lets "collided with something it had seen thirty steps ago" be a first-class safety violation rather than an unattributable collision.

**2. Eliciting — the environment is the contribution.** 150K procedurally generated indoor scenes ([ProcTHOR](../entities/ai2.md)), 800K assets (Objaverse), in the AI2-THOR simulator, with the five safety-critical components deliberately instantiated.

> [!note] The ablation that reframes the paper
> Run the **identical** ISA training recipe in simplified one-room scenes without safety-critical components and cumulative cost goes from **1.854 to 5.01** — nearly 3× worse, and **worse than the reward-shaping baseline it is supposed to beat** — with success rate falling 0.865 → 0.645. Same optimizer, same constraints, same everything except the environment.
>
> **The alignment method is not the load-bearing part; the elicitation environment is.** That is the most transferable claim in the paper and it is buried in §5.2.3. It also generalizes past this setting: a constrained optimizer can only constrain behaviors it observes, so *"we used safe RL"* says almost nothing without *"on data that contained the failures."* The same logic explains why the paper's own baselines look unsafe on Safety-CHORES and fine elsewhere — CC on Safety-CHORES runs **more than 2×** that on iTHOR or ProcTHOR under identical measurement.

**3. Constraining — CMDP with an adaptive multiplier.** Predicate violations become unit costs (state-action predicates at the violating step; trajectory predicates charged **entirely to the final step of the violating segment** — the paper flags its own credit assignment as unresolved). Lagrangian relaxation turns the constrained problem into `min_θ max_λ≥0 [−J_r(θ) + Σ λᵢ J_cᵢ(θ)]`, alternating parameter and multiplier updates. The cost limit `bᵢ` is set to **20% of the baseline's converged cost** rather than an absolute number — standard safe-RL practice, and a real limitation, because it means the safety target is defined relative to how unsafe the unconstrained policy happened to be.

**4. Assuring — three test regimes**: test-time safety (held-out + OOD), long-tail safety (rare events), and **extreme-failure safety** (environments constructed so the task is impossible). The third is the paper's best methodological idea; see below.

## Key claims, with the numbers

**Main table (Safety-CHORES; SR ↑ / CC ↓):**

| Method | ObjNav | PickUp | Fetch |
|---|---|---|---|
| **ISA** | **0.865 / 1.854** | **0.928 / 0.372** | **0.637 / 8.084** |
| FLaRe (RL fine-tune, task-only) | 0.822 / 12.356 | 0.912 / 7.076 | 0.605 / 43.364 |
| FLaRe-RS (**reward shaping**) | 0.75 / 4.755 | 0.918 / 7.496 | 0.45 / 18.19 |
| SPOC-DINOv2 (IL base) | 0.43 / 13.504 | 0.86 / 10.288 | 0.14 / 13.97 |
| PoliFormer (RL-only, nav) | 0.804 / 9.218 | — | — |

- **Reward shaping loses on both axes.** FLaRe-RS is the standard heuristic — add the safety cost as a reward penalty — and on ObjNav it lands at CC 4.755 / SR 0.75 against ISA's 1.854 / 0.865, and on Fetch it *halves* success (0.45 vs 0.637). Fig. 6 completes the argument: dynamic Lagrangian multipliers beat **every** fixed penalty coefficient that meets the same cost constraint. This is the measurement the wiki's [safe RL](../concepts/learning/safe-reinforcement-learning.md) page asserted and did not have.
- **The long tail is what moves.** ISA eliminates trajectories with cumulative cost > 10; the **upper bound of violation severity falls to 1/35** of FLaRe's. Mean cost is the headline, but the distribution is the result.
- **Safety generalizes across base models and benchmarks** (Fig. 4–5), across two alternative Lagrangian variants (PID-Lagrangian, Augmented-Lagrangian; App. B.7 — and **PID-Lagrangian posts lower cost at equal success**, 0.859 SR / **1.64** cost on Safety-ObjectNav against the headline 0.865 / 1.854, which matters because [Safety-Gymnasium](safety-gymnasium-paper.md) found PID specifically fixes plain-Lagrangian oscillation; it belonged in the main table), and **per-constraint** rather than by getting easy constraints cheaply — App. B.5 shows reductions in all five categories, with corners falling 7.451 → 0.535 and blind spots 5.050 → 1.090.
- **Zero-shot to unseen environments**: on DivScene (81 scene types, unseen), ISA averages **0.39 SR / 1.0 CC** against FLaRe's 0.37 / 10.5 — success held, cost down 10×.
- **Training cost**: 8× H100, 15M steps for ObjNav/PickUp, 25M for Fetch. Cost drops below the limit within ~1M steps; the multiplier converges slowly, as expected.

## The two findings worth carrying past this paper

**1. An unconstrained policy's failure mode is not merely unsuccessful — it is dangerous, and no success-rate benchmark can see that.**

For FLaRe, cost and success are significantly **negatively correlated** (p < 0.01): unsafe behavior coincides with task failure. For ISA the correlation is **rejected** — cost is roughly the same whether it succeeds or fails. It fails *safely*.

The extreme-failure experiment isolates this by construction: environments with novel goals and unfamiliar instructions where **success rate is ≈ 0 for everything**, so task performance cannot confound the safety measurement. There:

| | Cumulative cost when success is impossible |
|---|---|
| FLaRe | **71.68** |
| SPOC | 14.63 |
| **ISA** | **2.20** |

FLaRe is **32×** worse than ISA and **~6× worse than its own IL starting point** — RL fine-tuning for task performance made the failure behavior more dangerous. The paper's reading is right: *"their default behavior, when not guided by a successful task trajectory, remains inherently unsafe."* Repeated collisions while making no progress.

> [!note] This is the strongest available argument for "safe success"
> [PACS](pacs-paper.md) introduced **safe success** — completing the task while never violating a constraint — after finding policies at 0.79 task success and **0.00** safe success. SafeVLA supplies the complementary half from the other end: **measure what the policy does when it cannot succeed.** Every benchmark in this wiki's [policy-evaluation](../concepts/robotics/robot-policy-evaluation.md) coverage reports success rate, and a policy's behavior on the trials it fails is exactly the part that number discards. A 60%-success policy is being reported on 60% of its behavior.

**2. Confusing a VLA is a safety event, not just a performance event.**

App. B.6 perturbs instructions and perception. The instructive rows are the baseline's:

| | SR | CC |
|---|---|---|
| FLaRe, original | 0.822 | 12.356 |
| FLaRe, **+synonym substitution** | 0.570 | **41.475** |
| ISA, original | 0.865 | 1.854 |
| ISA, +synonym | 0.749 | 2.510 |
| ISA, +garbled code | 0.296 | 2.547 |
| ISA, +order change | 0.195 | 1.285 |
| ISA, +image flip | 0.628 | 3.540 |

**Swapping a word for a synonym makes the unaligned policy 3.4× more dangerous** while cutting its success by a quarter. The aligned policy, given *garbled input* it cannot act on, drops to 0.296 success and stays at 2.547 cost — it degrades toward doing nothing rather than toward thrashing.

This is a mechanism worth naming: for an unconstrained policy, *confusion resolves into motion*, and motion in a cluttered scene is collisions. It connects directly to the [Gemini Robotics 2](gemini-robotics-2-safety-report.md) result that models act correctly on safety signals handed to them and cannot produce those signals from perception — both are cases where the safety property is contingent on the model's input being *good*, which is precisely the condition deployment does not guarantee.

## Where to hold it at arm's length

> [!warning] The generalization-to-new-predicates result is weaker than the table suggests
> App. B.4.1 trains on five predicates and evaluates zero-shot on five new ones discovered by prompting GPT-4 over model rollouts. ISA's cost on the new set is **0.530** against SPOC's 9.647 and FLaRe's 11.140 — presented as evidence that ISA *"learns a generalizable safety logic rather than merely memorizing the initial five constraints."*
>
> But Table 7, one paragraph later, reports that the **original five predicates already flag 95.29–100% of the events the new predicates catch** — offered honestly, as validation that the original set is representative. Both cannot do the work claimed. If the new predicates fire on essentially the same physical events, then reducing violations of the old set **mechanically** reduces violations of the new set, and Table 6 measures relabelling rather than generalization. The genuinely new content is at most the ~5% non-overlap on "Movement" (erratic spinning, which is not a collision at all).
>
> The result is not fabricated and the honest number is printed adjacent to it. It just does not show what the section title says.

Further caveats, most of which the authors state:

- **Simulation only.** Training and all quantitative evaluation are in AI2-THOR. The §5.3 sim-to-real study — dual Realman RM75-6F arms, PsiBot G0-R hands, RealSense D455 — reports a successful Safety-PickUp deployment with *"effective obstacle avoidance consistent with its behavior in simulation"* and links demonstration videos. **There are no real-world numbers**, and App. G names simulation reliance as the primary limitation. Its four transfer strategies are nonetheless a usable checklist: convert noisy images to structured state (FoundationPose 6D poses) rather than fine-tuning on real images; **decouple dynamics** via a shared semantic/Cartesian action space; align digital-twin physics parameters (PID, action cycles); keep an identical data pipeline across sim and deployment. The second is the same **action-abstraction-as-safety** recommendation the [contact-rich survey](safe-learning-contact-rich-survey.md) makes on passivity grounds, arrived at here for sim-to-real reasons.
- **Costs are binary and uniform.** No severity weighting — breaking a beaker and nudging a mug cost the same. Conceded and framed as extensible. **But see the tension below.**
- **The cost limit is relative to the baseline**, so "safe" here means "20% of however unsafe FLaRe converged to," not a threshold anyone could certify against. Compare [ISO/TS 15066](../concepts/robotics/robot-safety-standards.md)'s energy thresholds, which are absolute and injury-derived.
- **Trajectory-level cost credit goes entirely to the final step** of a violating segment; the authors call credit assignment unresolved.
- **Success-rate arithmetic.** "+3.85%" is a **relative** change in mean success rate — 0.780 → 0.810, i.e. **+3 percentage points**. And "83.58%" is computed on **summed** cost across the three tasks (62.80 → 10.31), so it is dominated by Safety-Fetch, whose cost is 5–6× the other two. Per-task reductions are 85.0% / 94.7% / 81.4%. Nothing is misstated; the aggregation is just not the one a reader assumes.
- **One internal inconsistency**: Safety-Fetch ISA cumulative cost is **8.084** in Table 1 and **8.984** in Table 2's un-perturbed ISA row.

> [!warning] The binary-cost defence contradicts the same group's own 2023 critique
> SafeVLA: *"we chose a binary scheme in this work to establish a clear and generalizable baseline, as the notion of severity is often highly context-dependent."*
>
> [Safety-Gymnasium](safety-gymnasium-paper.md) App. B.6 (Ji is an author of both), criticizing OpenAI's Safety Gym for exactly this: *"there are only two possible outputs for the cost: 0 and 1… **this representation method loses some information.** For example, when the robot collides with a vase and causes the vase to move at different velocities, **there should be different cost values** associated with it… the learning potential for multiple constraints is lost when multiple costs are triggered simultaneously."*
>
> That 2023 example — *how fast the vase moved* — is unmistakably about **how hard the contact was**. Both positions are defensible and nobody has measured which matters, which makes it a concrete experiment rather than a gotcha: rerun this alignment with graded costs and see whether the avoidance behavior changes in *shape* or only in units.

> [!note] Edition history — the claim was downgraded between v1 and v4
> **v1 (2025-03-05)**: *"we propose **SafeVLA, a novel algorithm** designed to integrate safety into VLAs."*
> **v4 (2026-04-19)**: *"We address this by **exploring an integrated safety approach (ISA)**"* — and throughout the body the method is ISA, not SafeVLA. Every headline number is unchanged (83.58%, +3.85%, 1/35 severity bound).
>
> The title still says SafeVLA; nothing in the current paper is named SafeVLA. This reads as a reviewer-driven reframe from *novel algorithm* to *systematic exploration* — a fair one, since the components (CMDP, Lagrangian relaxation, procedural scene generation) are individually standard and the contribution is the integration and the environment. It matters here because the [contact-rich survey](safe-learning-contact-rich-survey.md) cites it as **"SafeVLA"**, a name that no longer denotes a method.

## Entities mentioned

- [Safety-CHORES](../entities/safety-chores.md) — **the benchmark**, and the part of this paper most likely to outlast it.
- [PKU-Alignment](../entities/pku-alignment.md) — the group; also the authors of **[Safety-Gymnasium](../entities/safety-gymnasium.md)** and **Safe-RLHF**, which makes this the same safe-RL infrastructure line extended into embodied AI.
- [Safety-Gymnasium](../entities/safety-gymnasium.md) — the direct predecessor: same CMDP framing, same co-reported reward/cost metric, same simulation-only limitation.
- [Allen Institute for AI](../entities/ai2.md) — the entire substrate is AI2's: AI2-THOR, ProcTHOR, Objaverse, and both the IL base model (**SPOC**) and two baselines (**FLaRe**, **PoliFormer**). PKU alignment methods on an AI2 stack.
- Uningested but named: **SPOC** (Ehsani et al.), **FLaRe** (Hu et al.), **PoliFormer** (Zeng et al.), **GRAPE**, **DivScene**, **FoundationPose**.

## Concepts touched

- [Safe reinforcement learning](../concepts/learning/safe-reinforcement-learning.md) — **the flagship instance**: CMDP + adaptive Lagrangian applied to a VLA, with the reward-shaping comparison measured.
- [VLA models](../concepts/learning/vla-models.md) — safety alignment as a distinct post-training stage.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — cumulative cost, the extreme-failure protocol, and what a success rate hides.
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — the alternative this paper represents: constrain the training, don't filter the output.
- [Semantic safety](../concepts/safety/semantic-safety.md) — the *physical*-harm counterpart to ASIMOV's judgment layer, and the first ingested work that actually **enforces** rather than measures.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — the regime this paper is *not* in, and why that matters for the survey.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the four-strategy checklist in §5.3.

## Open questions

- **Does any of this survive contact?** Every cost here is a discrete collision event with simulator ground truth. A force limit is continuous, is violated by degree, and is not observable without a sensor. Whether a CMDP formulation with binary costs transfers to force envelopes is untested, and is exactly the gap the [contact-rich survey](safe-learning-contact-rich-survey.md) names.
- **How much of the 83.58% is the environment?** The one-room ablation (1.854 → 5.01) says the elicitation environment does a large share of the work. There is no ablation of the reverse — the elicitation environment with *reward shaping* instead of CMDP — so the split between "good curriculum" and "right optimizer" is unmeasured.
- **What happens to the multiplier under distribution shift at deployment?** λ is adapted during training and then frozen. A CMDP guarantee is about the training distribution; nothing here re-derives it for a shifted one, and OOD testing measures outcomes rather than constraint satisfaction.
- **Would predicate specification survive an adversary?** The predicates are hand-written, then validated by GPT-4 discovery on the *same* policies' rollouts. Neither step is adversarial. Compare [ASIMOV](asimov-benchmark-paper.md)'s auto-red-teaming and [predictive red teaming](predictive-red-teaming-paper.md).
- **Safety-CHORES is a benchmark this wiki should want and cannot yet use** — it is AI2-THOR-based, navigation-and-pick-and-place, no force. What would the contact-rich equivalent even be built on? Nothing in the [simulator landscape](../syntheses/simulators/simulators-for-agentic-robotics-2026.md) currently pairs procedural scene generation with credible contact physics at 150K-scene scale.
