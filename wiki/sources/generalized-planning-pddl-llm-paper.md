---
title: "Generalized Planning in PDDL Domains with Pretrained Large Language Models"
type: source
url: https://arxiv.org/abs/2305.11014
local_path: raw/2305.11014.pdf
sha256: 4c969df5dc4025611ff41c0a1089333c956b26184c139fca12a5ee7e6d5b1be2
author: Tom Silver, Soham Dan, Kavitha Srinivas, Joshua B. Tenenbaum, Leslie Pack Kaelbling, Michael Katz
venue: AAAI 2024 (arXiv 2305.11014v2), 17 pp.
published: 2023-12-18
ingested: 2026-08-04
format: pdf
tags: [pddl, symbolic-planning, generalized-planning, code-as-policy, llm, gpt-4, program-synthesis, action-representation, controlled-natural-language]
---

# Generalized Planning in PDDL Domains with Pretrained Large Language Models

**Silver, Dan, Srinivas, [Tenenbaum](../entities/josh-tenenbaum.md), [Kaelbling](../entities/leslie-kaelbling.md), Katz** — MIT + IBM Research. AAAI 2024.

## Summary

Not "can an LLM make a plan?" but "can an LLM write a **program that makes plans**?" Given a [PDDL](../concepts/agents/symbolic-task-planning.md) domain and a handful of training tasks, GPT-4 synthesizes a **Python generalized planner** — a program that solves arbitrary future tasks in that domain, at scale far beyond the training instances. Two additions carry the method: **CoT summarization** (describe the domain and propose a strategy in words before writing code) and **automated debugging** (validate against training tasks, re-prompt with one of four error types on failure).

This is the wiki's first primary source on **PDDL** and on classical symbolic planning generally — a 50-year-old tradition that the [action-representation-languages](../syntheses/agents/action-representation-languages.md) synthesis had to reference without coverage.

## Key claims

### The result that matters most here: **names are load-bearing**

The **No Names** ablation replaces every identifier in the PDDL — domain, problem, predicates, operators, variables, types, objects — with `predicate1`, `operator2`, and so on. **The structure is untouched; only the words are gone.** Performance collapses:

| Domain | GPT-4 | No Names | No Debug | No CoT | GPT-3.5 |
|---|---:|---:|---:|---:|---:|
| Delivery | **0.90** | 0.10 | 0.10 | 0.70 | 0.00 |
| Forest | **1.00** | 0.11 | 0.62 | 1.00 | 0.32 |
| Gripper | **0.90** | 0.10 | 0.50 | 0.80 | 0.00 |
| Miconic | 0.01 | 0.00 | 0.00 | 0.13 | 0.00 |
| Ferry | **0.80** | 0.00 | 0.26 | 0.20 | 0.00 |
| Spanner | 0.10 | 0.00 | 0.00 | 0.00 | 0.00 |
| Heavy | **0.60** | 0.00 | 0.20 | 1.00 | 0.00 |

*(Fraction of evaluation tasks solved; 10 seeds × 30 evaluation tasks per domain.)*

> [!note] The third independent instance of the same finding
> This is **structurally identical** to [RT-H](rt-h-paper.md)'s OneHot ablation and [TurboVLA](turbovla-paper.md)'s task-ID ablation: *hold the formal structure fixed, strip the human-meaningful names, measure the loss.* Three papers, three unrelated paradigms — symbolic planning + program synthesis, a 55B VLA action hierarchy, and a 0.2 B LLM-free policy — and all three find that **semantic names beat opaque labels over identical structure.**
>
> PDDL is the most extreme of the three: performance doesn't degrade, it **collapses to near zero**. And PDDL is the one representation here that is *formally complete without names* — a planner doesn't need them at all. The names exist purely for humans, and a language model turns out to need them for exactly the same reason. See [action representation languages](../syntheses/agents/action-representation-languages.md).

### Automated debugging is the other essential ingredient

**No Debug** roughly halves performance across domains (0.90 → 0.10 on Delivery, 0.80 → 0.26 on Ferry). Error types encountered during training, and their distribution:

| Error type | All trials | Successful trials | Failed trials |
|---|---:|---:|---:|
| Python exception | 40.0% | 28.9% | 42.5% |
| Plan semantics | 34.0% | 44.7% | 31.4% |
| Plan syntax | 13.0% | 18.4% | 11.7% |
| Timeout | 13.0% | 8.0% | 14.4% |

Successful runs skew toward *semantic* errors and away from *exceptions* — the model that gets there is failing on strategy, not on syntax. The same feedback-loop finding as [CaP-X](cap-x-paper.md)'s multi-turn tiers and [ASPIRE](aspire-paper.md)'s execution traces.

**CoT summarization has non-uniform impact** — it helps Ferry (0.20 → 0.80) and Delivery, and *hurts* Heavy (1.00 → 0.60) and Miconic. The authors report this honestly rather than claiming a uniform win.

### GPT-4 vs. classical generalized planning — the interesting split

**PG3** (Yang et al. 2022; heuristic search over lifted decision lists) scores **1.00 on six of seven domains** — and **0.00 on Heavy**, the one domain new to this paper. GPT-4 scores 0.60 on Heavy.

> [!note] The same shape as this wiki's code-as-policy lineage
> The specialized symbolic method is *better* in-distribution and *fails completely* off it; the LLM is worse in-distribution and degrades gracefully. That is precisely the pattern running from [Code as Policies](code-as-policies-paper.md) (62–80% vs CLIPort's 0.00% OOD) through [CaP-X](cap-x-paper.md) and [ASPIRE](aspire-paper.md), now visible in the purely symbolic setting with no perception involved at all. It also makes the Heavy result the load-bearing one — the four standard domains were plausibly in GPT-4's pretraining data, and the authors say so; **Heavy is the one they can guarantee was not.**

### Efficiency

Synthesized programs are compared against **Fast Downward**, a state-of-the-art planner, on log-log axes: the generalized planners run dramatically faster on large instances, because a domain-specific program sidesteps search entirely. Evaluation tasks are far larger than training tasks by design — e.g. Heavy trains on 3–10 objects and evaluates on **100–250**.

**Two training tasks are often sufficient** for strong generalization.

## Open questions

- **No robot, no perception.** The domains are symbolic benchmarks (Gripper, Miconic, Ferry, Spanner, Delivery, Forest, Heavy). The bridge from a PDDL operator to an actuated robot — the grounding problem this wiki keeps returning to — is entirely out of scope. That gap is exactly what [behavior trees](../concepts/robotics/behavior-trees.md) and [code-as-policy](../concepts/agents/code-as-policy.md) APIs try to fill.
- **Pretraining contamination is acknowledged but only partly controlled.** Four of seven domains are standard benchmarks likely in GPT-4's training data; only Heavy is guaranteed clean.
- **Miconic (0.01) and Spanner (0.10) are near-total failures** and are not deeply diagnosed. Spanner requires irreversible-resource reasoning (each wrench used once) — plausibly the domain type where greedy program strategies break.
- **GPT-4-era result.** Whether a 2026 frontier model changes the picture — particularly on Miconic/Spanner and on the No-Names ablation — is untested here.

## Entities mentioned
- [Tom Silver](../entities/tom-silver.md) · [Josh Tenenbaum](../entities/josh-tenenbaum.md) · [Leslie Kaelbling](../entities/leslie-kaelbling.md)

## Concepts touched
- [Symbolic task planning / PDDL](../concepts/agents/symbolic-task-planning.md) — the concept this source founds in the wiki
- [Code as policy](../concepts/agents/code-as-policy.md) — the LLM writes a program, not a plan; the same architecture one abstraction level up
- [Action representation languages](../syntheses/agents/action-representation-languages.md) — the No-Names result
- [Chain-of-thought](../concepts/learning/chain-of-thought.md) — CoT summarization, with a non-uniform effect
