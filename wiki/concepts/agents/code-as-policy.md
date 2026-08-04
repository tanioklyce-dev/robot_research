---
title: Code as policy
type: concept
created: 2026-08-03
updated: 2026-08-03
sources: 10
tags: [code-as-policy, llm-agent, agentic-robotics, program-synthesis, skill-library, voyager, saycan, voxposer, inner-monologue, codeact, tool-use, waddle, cap-x, aspire, benchmark]
---

# Code as policy

## Definition

**Code as policy** is the control pattern in which a language model, given a natural-language goal and a perception/actuation API, **writes an executable program** that runs on the robot — rather than emitting low-level actions directly (as a [VLA](../learning/vla-models.md) does) or selecting from a fixed menu of tool calls (the classic [LLM-agent](llm-agent-architecture.md) pattern). The program *is* the policy: it composes perception primitives, control primitives, and library skills into task-specific logic, with loops, conditionals, and verification.

It is best read as a **sub-pattern of [LLM-agent architecture](llm-agent-architecture.md)** where the action vocabulary is *arbitrary code* instead of a discrete tool schema. That distinction matters: a JSON-tool agent can only reach behaviors someone pre-named as tools; a code-writing agent can express new control flow — retries, servoing, parametrized sweeps — the tool designer never enumerated.

## The lineage — fully ingested as of 2026-08-03

Nine papers, four years, two branches. Every one is now a source page in this wiki.

| Year | Paper | What the model emits | Key result |
|---|---|---|---|
| 2022 | [SayCan](../../sources/saycan-paper.md) | **A choice among pretrained skills**, weighted by learned affordances | 84% plan / 74% execute on 101 kitchen instructions; **0%** without language grounding |
| 2022 | [Inner Monologue](../../sources/inner-monologue-paper.md) | Same, but **re-planned against textual feedback** | Under disturbance, SayCan → 0%, IM → 60.4% |
| 2022 | [Code as Policies](../../sources/code-as-policies-paper.md) | **Executable policy code** | Beats a 30k-demo CLIPort 62–80% vs **0.00%** out-of-distribution |
| 2023 | [VoxPoser](../../sources/voxposer-paper.md) | Code composing **3D value maps** for a planner | 88% vs 24% real-world; primitives baseline **0%** under disturbance |
| 2023 | [Language to Rewards](../../sources/language-to-rewards-paper.md) | Code defining **reward functions** for MPC | 90% of 17 tasks vs **50%** for a CaP baseline |
| 2023 | [Voyager](../../sources/voyager-paper.md) | Code, into a **persistent skill library**, self-verified | Only agent to reach Minecraft's diamond tier; library transfers to *other agents* |
| 2024 | [CodeAct](../../sources/codeact-paper.md) | Code as the **general agent action space** | +20.7 pp over next-best format on multi-tool composition |
| 2026 | [CaP-X](../../sources/cap-x-paper.md) | Code, **measured across 8 abstraction tiers** | Prior results were inflated by human-designed macros |
| 2026 | [ASPIRE](../../sources/aspire-paper.md) | Code, **repaired against per-primitive traces** | +41 to +77 points; skill library provably compounds |

**Two branches, one disagreement.** SayCan and Inner Monologue let the model *choose among skills*; everything after lets it *write* them. [Code as Policies](../../sources/code-as-policies-paper.md) states the split with an example: an LLM planner asked to "move the coke can a bit to the right" emits `1. Pick up / 2. Move a bit right / 3. Place` — which **assumes a skill exists** for "move a bit right." Writing the servo loop needs no such skill to have been trained.

> [!note] Two lineages that are literally the same people
> **Voyager → ASPIRE is one lab.** Voyager is an [NVIDIA GEAR](../../entities/nvidia-gear.md) paper, and [Guanzhi Wang](../../entities/guanzhi-wang.md) is Voyager's first author *and* an ASPIRE project co-lead (with [Jim Fan](../../entities/jim-fan.md) and [Yuke Zhu](../../entities/yuke-zhu.md) on both). Automatic curriculum → evolutionary search, code skill library → repair-knowledge library, self-verification → execution traces: the same architecture, ported from a domain where trials are free to one where they are not.
>
> **The Google cohort split toward VLAs.** [Brian Ichter](../../entities/brian-ichter.md) and [Karol Hausman](../../entities/karol-hausman.md) co-authored SayCan, Inner Monologue, and Code as Policies — then co-founded [Physical Intelligence](../../entities/physical-intelligence.md), the [π0](../../entities/pi-zero.md) lab whose models score 0.00 under perturbation in the 2026 tables. **The two "camps" in this wiki's architectural argument are overlapping sets of people**, which is a reason to read the 2026 comparison as a within-community finding rather than a rivalry.

## The abstraction confound — the finding that reframes the lineage above

> [!warning] Much of the published code-as-policy success belonged to the API designer, not the model
> [CaP-X](../../sources/cap-x-paper.md) is the first work to vary primitive abstraction as a controlled axis, and success rises **monotonically** as human-designed macros are added back: low-level primitives with only docstrings (**S4**) → low-level with examples (**S3**) → human macros with real perception (**S2**) → macros with privileged state (**S1**).
>
> **S2 is "the default setting for most prior work."** Prior CaP systems called things like `stack_objs_in_order()` — macros that "reduce the effective search space and allow models to focus on task sequencing." So the strong zero-shot numbers reported across the lineage above are **not clean measurements of agent capability**; they are measurements of agent-plus-scaffolding, and the split was never reported.
>
> CaP-X's recommendation to the field: evaluate embodied coding agents **primarily at primitive level**, "ensuring that success stems from robust reasoning rather than from the inductive biases of an over-engineered, often task-specific, API set."

> [!warning] Correction (2026-08-03): this finding is not new, and CaP-X is not its discoverer
> Ingesting the pre-2026 lineage changes the story the wiki told two entries ago. **The primitive-scope ceiling was named by the original paper and attacked by its immediate successors, three years before CaP-X measured it.**
>
> - **[Code as Policies](../../sources/code-as-policies-paper.md) (2022) flagged it in its own Discussion:** LMPs are "restricted by the scope of … **which control primitives are available**. Only a handful of named primitive parameters can be adjusted without over-saturating the prompts," and they struggle with commands that "operate at a different abstraction level than the given Examples."
> - **[VoxPoser](../../sources/voxposer-paper.md) (CoRL 2023)** targeted exactly this — reliance on pre-defined primitives, "often considered a major bottleneck" — and beat a CaP-style baseline in all six seen/unseen cells by writing value maps instead.
> - **[Language to Rewards](../../sources/language-to-rewards-paper.md) (CoRL 2023)** reported the same diagnosis in almost the same words: CaP does well on tasks "expressed by the given primitives … but **fails to generalize to novel low-level skills**" — 90% of tasks vs CaP's 50%.
>
> **CaP-X's actual contribution is methodological, not empirical:** the 2023 papers *routed around* the ceiling by changing the output representation; CaP-X was the first to hold the method fixed and **vary abstraction as a controlled axis**, turning a known qualitative limitation into a measured monotonic curve. That is a real contribution — but the wiki's earlier framing ("published results were substantially carried by the API designer" as a *revelation*) overstated its novelty. Three independent groups had said so already.

The compensating result is that **test-time compute buys back what abstraction removal costs**. Multi-turn interaction over *low-level* primitives (tier M4) reaches parity with *high-level* multi-turn (M3) and surpasses high-level single-turn (S2) — so the expressivity of low-level APIs is available without permanently paying their difficulty penalty.

## What is now measured

### Against human experts
CaP-X's reference is **N=7 authors with 2+ years of robotics-programming experience** writing against the identical API, iterating to **88.5% average single-turn success**. Across 12 frontier models at tier S4, **none matches human-written programs zero-shot**. But with the full CaP-Agent0 harness — visual differencing + auto-synthesized skill library + parallel multi-model reasoning — the agent matches or exceeds human code on **4 of 7 tasks** while still operating only on low-level primitives. [ASPIRE](../../sources/aspire-paper.md) surpasses human experts on both BEHAVIOR-1K tasks.

> [!note] Whose humans?
> The human baseline was written by the paper's own authors on their own API. It is a reasonable *ceiling estimate* and a weak *"beats humans"* claim. Treat "exceeds human expert" in this thread as unreplicated.

### Against learned policies, out of distribution — a four-year-old result

This is the paradigm's strongest comparative result, and ingesting the lineage shows it has been stable since 2022.

| Year | Learned policy | In-distribution | Out-of-distribution |
|---|---|---|---|
| 2022 | [CLIPort](../../entities/cliport.md), 30k demos ([CaP](../../sources/code-as-policies-paper.md)) | 78.8–97.3% | **0.00–0.01%** |
| 2022 | CLIPort + oracle termination ([Inner Monologue](../../sources/inner-monologue-paper.md)) | up to 94% | **0.0%** on every unseen task |
| 2023 | CaP-style primitives under disturbance ([VoxPoser](../../sources/voxposer-paper.md)) | 24% | **0.0%** |
| 2026 | [OpenVLA](../../entities/openvla.md) / [π0](../../entities/pi-zero.md) ([LIBERO-PRO](../../sources/libero-pro-paper.md)) | 94–98% | **0.00** |

Against each, the code-writing agent degrades gracefully instead: 62–80% (2022), 26–86% (2022), 70% (2023), and in 2026 training-free CaP-Agent0 at **0.12–0.26 (Pos)** / **0.14–0.18 (Task)** — roughly *symmetric* across axes — with [ASPIRE](../../sources/aspire-paper.md) adding **+41 to +77 points**.

**The mechanism is unglamorous but decisive:** learned policies are trained on a fixed instruction and attribute distribution, so shift destroys them. A code-writing agent reads the instruction with a general language model, so paraphrase is free.

> [!note] What actually changed between 2022 and 2026
> Not the finding — **the stakes**. In 2022 the collapsing baseline was a 30k-demo CLIPort, and "imitation learning doesn't generalize" surprised nobody. In 2026 the collapsing baselines are **foundation models trained on internet-scale robot data**, which were supposed to have fixed exactly this. The result is the same; its implication is much larger.
>
> And the honest caveat has been constant too: **in-distribution, the trained policy wins.** CLIPort beat CaP 97.33 vs 89.30 on seen spatial-geometric tasks in 2022; π0.5 beats CaP-Agent0 on position perturbation in two of three suites in 2026. Code-as-policy has never been the better manipulator — only the more robust one.

### The compounding claim, quantified
[ASPIRE](../../entities/aspire.md) is the wiki's first measured evidence that a skill library **compounds**: a library accumulated on LIBERO-90 lifts held-out long-horizon tasks from **4% → ~31%** zero-shot, and success **increases with library size** across snapshots of N ∈ {0, 25, 50, 90} source tasks. Sim-discovered skills also cut real-robot debugging cost by ~4× and took one task from **0/20 to 11/20** success.

> [!note] Cite ASPIRE for this, not CaP-X
> CaP-X also has a skill library, but its ablation contribution (+4 pp, 55→59) **does not survive its sample size** (p = 0.13 at n=700 — see the [audit](../../syntheses/platforms/vla-success-rate-audit.md)). The skill library is the component this paradigm's architectural argument leans on hardest, and exactly one of the two ingested papers actually demonstrates it.

### What actually drives the gains
The single largest component effect in the thread is not the model and not the library — it is **feedback resolution**. ASPIRE's per-primitive multimodal execution traces alone move macro-average success **14% → 62%**; evolutionary search adds the last 10 points to 72%. CaP-X finds the same thing from the other side: **structured text beats raw pixels**. Piping raw RGB back to the agent each turn (M2) *degrades* performance versus plain `stdout`/`stderr` (M1), attributed to a cross-modal alignment gap; converting observations to structured language via a **Visual Differencing Module** (M3) beats both.

> [!note] The transferable engineering lesson
> Across both papers: **give the agent inspectable, textual, per-call evidence.** Not more pixels, not a bigger model — better-attributed failure information. This is the same lesson the software-engineering agent literature learned, arriving in robotics.

### Sim-to-real: the transfer object is the interface
CaP-RL post-trains a **7B** model (Qwen2.5-Coder) with GRPO in simulation only, and it retains **84% / 76%** on real [Franka](../../entities/franka-panda.md) cube lift/stack (up from 24% / 12%). What crosses the reality gap is the **code-as-action-space** — the agent composes perception and control tools that are *fixed across sim and real* rather than mapping pixels to torques. This is a structurally different sim-to-real story from the [visuomotor one](../learning/sim-to-real-transfer.md), and a much cheaper one.

## The skills hierarchy

Code-as-policy systems converge on a **three-level abstraction stack**, though the three ingested systems fill the middle level differently:

1. **Primitives** — a fixed vocabulary the platform provides (`bounding_box`, `solve_ik`, `sam3_text_prompt`, `approach_until`). Ported per robot; **this is where embodiment-specificity actually lives.**
2. **Skills** — parametrized, reusable routines the agent *authors* and shares.
3. **Programs** — per-task code composed from skills.

| System | What a "skill" is | How it is acquired |
|---|---|---|
| [Waddle](../../entities/waddle-labs.md) | Motor routines (`fold_grasp`, `servo_align`) | Agent-authored during deployment; shared cross-agent |
| [CaP-Agent0](../../entities/cap-x.md) | 9 task-agnostic utility functions | Mined offline from successful rollouts pooled across 12 models |
| [ASPIRE](../../entities/aspire.md) | **Repair knowledge** — failure signature + when-to-apply + fix | Induced from *diagnosed failures*, audited by a coordinator |

ASPIRE's is the notable variant: it stores **what went wrong and how it was fixed**, not what worked. Its library spans localization heuristics, perception prompts, grasping constraints, navigation recovery, and debugging workflows — a taxonomy that **emerged rather than being designed**.

This is the **motor-skill analogue** of [agent skills (portable SKILL.md)](agent-skills.md): both are shared, discoverable capability packages, but SKILL.md bundles are hand-authored runbooks whereas these are **agent-authored and grow from experience**.

## Where this sits on the abstraction ladder

Code-as-policy is **level 2 (programmatic control)** in the [control abstraction levels](../robotics/control-abstraction-levels.md) taxonomy — the level [Anthropic found](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) "substantially outperforms direct control" for essentially every model. CaP-X's contribution to that taxonomy is to show **level 2 is not one level**: its eight tiers subdivide "the model writes a controller" into rungs that span tens of points of success rate. *"Programmatic control works"* is underspecified until you say which primitives were on offer and how many turns the agent got.

## Open questions

- **Cost is unreported everywhere — and has been flagged since 2023.** CaP-Agent0 fires up to 9 parallel frontier-model queries per turn; ASPIRE burned **334.9M tokens** failing to open a drawer unaided. Against a VLA that trains once and runs at near-zero marginal inference cost, "training-free" is not "cost-free," and **no paper in this thread reports success rate alongside compute**.

  > [!warning] Three years, same two limitations, no progress
  > [Voyager](../../sources/voyager-paper.md) listed these as limitations #1 and #2 in **2023**: "The GPT-4 API incurs significant costs. It is **15× more expensive than GPT-3.5**. Nevertheless, Voyager requires the quantum leap in code generation quality from GPT-4, which GPT-3.5 and open-source LLMs cannot provide."
  >
  > [ASPIRE](../../sources/aspire-paper.md) restates both in **2026**: hundreds of millions of tokens per task, and "we have not verified that smaller or weaker LLMs can sustain the same debugging loop." The wiki's [audit directive to record compute at ingest](../../syntheses/platforms/vla-success-rate-audit.md) therefore has a three-year-old precedent that the field itself never acted on. This is the thread's most durable unsolved problem, not a new one.

- **Frontier-model dependence.** CaP-RL is the only real counter-evidence — a **7B** model reaching 76–84% real-world after simulation-only RL — but only on three tasks it was trained for. Note the original [Code as Policies](../../sources/code-as-policies-paper.md) already found scaling laws hold (GPT-3 6.7B: 3–5% on RoboCodeGen; 175B: 68–84%), and that hierarchical code-gen only helps *above* a capability threshold.
- **Skill-library memory management is unsolved.** ASPIRE reports entries going stale, redundant, or misleading as the library grows, and offers this as the explanation for **non-monotonic zero-shot transfer**. Retrieval, pruning, and re-validation are open.
- **The primitive set still has to be ported per embodiment**, and it bounds what the agent can express at all — see the contradiction below.

> [!warning] Contradiction — "works with any embodiment" vs. the API ceiling
> [Waddle](../../sources/waddle-labs-introducing-waddle.md) claims its agents "work with any arms, grippers, and camera setups without new data collection." [ASPIRE's limitations](../../sources/aspire-paper.md) state the opposite constraint plainly: the predefined API "bounds the behaviors the agent can express: if a task requires sensing, control, or interaction capabilities outside the exposed primitives, the agent must either approximate them inefficiently or rely on humans to extend the API."
>
> These are reconcilable — cross-embodiment generality is real *within* the primitive set, and the primitive set is what gets ported — but the vendor framing hides the porting cost, and the wiki's [standing suspicion](../../sources/waddle-labs-introducing-waddle.md) that embodiment-specificity **relocates rather than disappears** is now confirmed by a research group with no product to sell. Both CaP-X and ASPIRE needed per-embodiment primitive work (CaP-X notes "single arm to bimanual control primitive modifications" for its real-robot demos).

## Related concepts
- [LLM-agent architecture](llm-agent-architecture.md) — the parent pattern; code-as-policy is the "action vocabulary = code" special case.
- [Action representation languages](../../syntheses/agents/action-representation-languages.md) — code placed on the full spectrum of action representations, from free-form English to latent codebook tokens. CaP-X's monotonic-abstraction finding is the central evidence there: **the API designer, not the model, supplies much of the performance.**
- [Control abstraction levels](../robotics/control-abstraction-levels.md) — where this sits, and the level CaP-X subdivides.
- [Agent skills (portable SKILL.md)](agent-skills.md) — the hand-authored-runbook cousin of the learned skill library.
- [VLA models](../learning/vla-models.md) — the end-to-end alternative; here a VLA is a *callable tool*, not the whole policy.
- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — CaP-X's 100-trials/task and ASPIRE's disjoint debug/eval seeds are among the better-disclosed protocols in the wiki.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — the code-as-action-space mechanism.
- [World-action models](../world-models/world-action-model.md) — grouped with VLAs as "action models" a code-writing agent can call.
- [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) — an agent writing *arbitrary code* widens the execution-rail problem beyond name-level tool allowlisting. Note ASPIRE's **coordinator audits actor findings for API-policy compliance** — the first mechanism in this wiki's agentic-robotics pages that actually resembles an execution rail.

## Current state

As of mid-2026 the pattern has **crossed from demo to measurement**. [CaP-X](../../entities/cap-x.md) supplies a 187-task environment, a 12-model benchmark, and a training-free harness competitive with post-trained VLAs; [ASPIRE](../../entities/aspire.md) shows the skill library compounds and transfers zero-shot and cross-embodiment; one deployed commercial API ([Waddle](../../entities/waddle-labs.md)) makes the same architectural bet without publishing numbers.

The honest summary of the head-to-head with end-to-end VLAs: **on standard LIBERO, VLAs win overwhelmingly (94–98% vs. code-as-policy's far lower absolute rates). Under perturbation, that inverts, because the VLA numbers go to zero and the code agent's do not.** Which comparison matters depends entirely on whether you believe standard LIBERO measures generalization — and [LIBERO-PRO](../../sources/libero-pro-paper.md) argues it does not. Code-as-policy's real claim is not that it is better at manipulation; it is that it **degrades gracefully** where trained policies fall off a cliff, and that it needs no task-specific data to do so.

What remains unmeasured is what it costs.

> [!note] What four years of lineage actually shows
> Reading 2022 → 2026 end to end, the paradigm's **core empirical claim has not changed once**: a code-writing agent degrades gracefully where a trained policy falls off a cliff, and loses to that policy in-distribution. Every generation re-demonstrated it against a stronger baseline — CLIPort in 2022, primitive-parameterizing CaP in 2023, internet-scale VLAs in 2026.
>
> What *has* changed is the engineering around it, and the direction is consistent: **more and better-attributed feedback**, from open-loop plans (SayCan) → task-level textual feedback (Inner Monologue) → self-verification (Voyager) → structured visual differencing (CaP-X) → per-primitive multimodal traces (ASPIRE). Each step bought more than the model upgrades that accompanied it.
>
> And two things have **not** moved in four years: the primitive set still has to be ported per embodiment, and nobody reports cost.

## Mentioned in
- [Code as Policies](../../sources/code-as-policies-paper.md) (ICRA 2023) — the origin paper; LMPs, hierarchical code-gen, RoboCodeGen.
- [SayCan](../../sources/saycan-paper.md) (CoRL 2022) — the skill-selection branch this pattern defines itself against.
- [Inner Monologue](../../sources/inner-monologue-paper.md) (CoRL 2022) — closed-loop textual feedback; the 2022 origin of "feedback is the bottleneck."
- [VoxPoser](../../sources/voxposer-paper.md) (CoRL 2023) — code that composes 3D value maps for a planner.
- [Language to Rewards](../../sources/language-to-rewards-paper.md) (CoRL 2023) — code that defines reward functions for MPC.
- [Voyager](../../sources/voyager-paper.md) (TMLR 2024) — the persistent, self-verifying skill library; ASPIRE's direct ancestor.
- [CodeAct](../../sources/codeact-paper.md) (ICML 2024) — the general-agent grounding for "code beats a fixed tool schema."
- [CaP-X](../../sources/cap-x-paper.md) (ICML 2026) — the measurement apparatus; abstraction as a controlled axis.
- [ASPIRE](../../sources/aspire-paper.md) (Jun 2026) — continual skill discovery; the compounding evidence.
- [Introducing Waddle](../../sources/waddle-labs-introducing-waddle.md) — deployed commercial system + the lineage survey this page was first built from.
