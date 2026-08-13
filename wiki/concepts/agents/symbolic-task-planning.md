---
title: Symbolic task planning (PDDL and generalized planning)
type: concept
created: 2026-08-04
updated: 2026-08-04
sources: 2
tags: [pddl, symbolic-planning, generalized-planning, classical-ai, action-representation, llm-planning, program-synthesis]
---

# Symbolic task planning (PDDL and generalized planning)

**PDDL** (Planning Domain Definition Language) is the standard formalism for classical AI planning: a **domain** declares typed predicates and operators, each with preconditions and effects; a **problem** declares objects, an initial state, and a goal. A planner searches for an operator sequence transforming the initial state into one satisfying the goal.

It is the fifty-year-old answer to "a human-readable, embodiment-agnostic way to specify actions" — and its presence and its limits are both essential to [action representation languages](../../syntheses/agents/action-representation-languages.md).

## What PDDL does and doesn't give you

**Does:** a specified grammar, a closed and declared vocabulary, formal semantics, decades of solvers (Fast Downward and successors), and genuine embodiment-independence — `(on block-a block-b)` commits to no morphology.

**Doesn't:** any account of *motion*. An operator's effect is a change in a symbolic state, not a trajectory. Grounding `(pick ?obj)` into torques is entirely outside the formalism — which is why the tradition sits above, and never replaced, the control layer. This is the same gap [behavior trees](../robotics/behavior-trees.md) fill from the composition side and [code-as-policy](code-as-policy.md) APIs fill by fiat.

## Generalized planning

Rather than solving one problem, **generalized planning** synthesizes a *program* that solves any problem in a domain. [Silver et al. (AAAI 2024)](../../sources/generalized-planning-pddl-llm-paper.md) have GPT-4 write Python generalized planners from a PDDL domain plus a few training tasks, with **CoT summarization** and **automated debugging** (validate against training tasks, re-prompt on error).

Results across seven domains (10 seeds × 30 evaluation tasks):

- **Automated debugging is essential** — removing it roughly halves performance (0.90 → 0.10 on Delivery).
- **CoT summarization is non-uniform** — helps Ferry (0.20 → 0.80), hurts Heavy (1.00 → 0.60).
- **Two training tasks are often enough.**
- Synthesized programs vastly outrun **Fast Downward** on large instances, because a domain-specific program skips search.

### The classical/LLM split, in a setting with no perception

**PG3**, the specialized symbolic method, scores **1.00 on six of seven domains** — and **0.00 on Heavy**, the one domain new to the paper. GPT-4 scores **0.60** on Heavy.

> [!note] The wiki's recurring shape, with perception removed
> Specialized method: better in-distribution, falls off a cliff outside it. LLM: worse in-distribution, degrades gracefully. Exactly the pattern from [Code as Policies](../../sources/code-as-policies-paper.md) (62–80% vs CLIPort's 0.00% OOD) through [CaP-X](../../sources/cap-x-paper.md) and [ASPIRE](../../sources/aspire-paper.md) — and here it appears in a **purely symbolic** setting, which rules out perception robustness as the explanation. Heavy is the load-bearing domain: the four standard benchmarks were plausibly in GPT-4's pretraining data (the authors say so), and Heavy is the one they can guarantee wasn't.

## The names result

The **No Names** ablation replaces every identifier — domain, problem, predicates, operators, variables, types, objects — with `predicate1`, `operator2`, etc. Structure untouched. Performance **collapses**: 0.90 → 0.10, 1.00 → 0.11, 0.80 → 0.00.

> [!note] PDDL is the sharpest version of a three-way convergence
> This is structurally the same experiment as [RT-H](../../sources/rt-h-paper.md)'s OneHot ablation and [TurboVLA](../../sources/turbovla-paper.md)'s task-ID ablation — hold the structure fixed, strip the human-meaningful names, measure the loss. All three lose.
>
> **PDDL is the extreme case, for two reasons.** The loss isn't degradation, it's *collapse to near zero*. And PDDL is the one representation of the three that is **formally complete without names** — a classical planner solves the renamed domain exactly as well, because it only reads structure. The names exist purely for humans. A language model turns out to need them for the same reason a human does. See [action representation languages](../../syntheses/agents/action-representation-languages.md).

## Current state

Classical planning and learned control remain largely disjoint in this wiki: PDDL appears where an LLM writes plans or planners, and never below the task level. The live question is not whether PDDL is a good action language — it is a good *task* language — but whether the grounding layer beneath it can be learned rather than hand-written. [PA-BT](../robotics/behavior-trees.md) backchains from goal conditions into a reactive executable and is the closest thing here to a bridge.

## Related
- [Action representation languages](../../syntheses/agents/action-representation-languages.md) — PDDL as the formal-task-language row
- [Behavior trees](../robotics/behavior-trees.md) — the composition layer; PA-BT backchains like a planner
- [Code as policy](code-as-policy.md) — the LLM writes a program; here the program is a planner
- [LLM-agent architecture](llm-agent-architecture.md) — where an LLM plans over a tool schema instead of a domain file
- [Chain-of-thought](../learning/chain-of-thought.md) — CoT summarization, with a measured non-uniform effect

## Mentioned in
- [Generalized Planning in PDDL Domains with Pretrained LLMs](../../sources/generalized-planning-pddl-llm-paper.md)
