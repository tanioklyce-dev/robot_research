---
title: "Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Boppana, Ma, Loeffler et al., Goodfire + Harvard, Mar 2026)"
type: source
url: https://arxiv.org/abs/2603.05488
local_path: raw/2603.05488v1.pdf
sha256: 09e4dfe9e81f883da07421f9d2ca4de68be46bc0608c84e725a5a12c0554e23f
author: "Siddharth Boppana*, Annabel Ma*, Max Loeffler, Raphael Sarfati, Eric Bigelow, Atticus Geiger, Owen Lewis, Jack Merullo"
affiliation: Goodfire AI; Harvard University
venue: "arXiv 2603.05488"
published: 2026-03-12
ingested: 2026-08-30
tags: [chain-of-thought, cot-faithfulness, activation-probing, attention-probes, performative-reasoning, early-exit, goodfire, harvard, interpretability, adaptive-compute]
---

> [!note] Ingest depth
> Read from the **arXiv primary** (`raw/2603.05488v1.pdf`, 26 pages), not the Goodfire blog post — §1–7 read in full, appendices skimmed. Code at `github.com/AskSid/disentangling-computation-from-cot`.

## Summary

**Boppana, Ma, Loeffler, Sarfati, Bigelow, Geiger, Lewis & Merullo** (Goodfire AI + Harvard). Evidence of **performative chain-of-thought**: *"a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief."*

The method is a three-way race to decode a model's final answer from a partial trace:

1. **Attention probes** on activations — trained to predict the model's final answer from the first `T` response tokens, one probe per layer.
2. **Forced answering** — inject a forced-answer prompt at token `x` and see what the model says.
3. **A CoT monitor** — an LLM (Gemini-2.5-Flash) reading the partial CoT, allowed to output `N/A` if it cannot tell.

**Performativity is defined as the accuracy gap between the probes/forced-answering and the monitor.** If the activations know and the text does not say, the text is theatre.

Models: **DeepSeek-R1 671B** and **GPT-OSS 120B**. Benchmarks: **MMLU-Redux** and **GPQA-Diamond**.

## The finding is conditional, which is what makes it credible

**On easy recall-based MMLU**: the answer is decodable from activations **far earlier** than the monitor can say. Performativity `|ΔProbe − ΔMonitor|` = **0.417 / 0.505** (DeepSeek-R1, probe / forced-answer). The model has committed; the remaining tokens are display.

**On hard multi-hop GPQA-Diamond**: all three methods start at similar accuracy and **rise together**. Performativity **0.012 / 0.010** — essentially zero. Here the CoT is doing the work, and the tokens are the computation rather than a performance of it.

> [!note] The nuance that keeps this from being a debunking
> The obvious over-read is "chain-of-thought is theatre." The paper's own data says: **theatre on the easy task, genuine on the hard one** — and it goes further, showing that **inflection points** (backtracking, "aha" moments, reconsiderations) *"occur almost exclusively in responses where probes show large belief shifts."*
>
> So the dramatic-looking bits of reasoning traces are **not** learned performance — they track real internal uncertainty being resolved. The performative part is the *filler around a conclusion already reached*, not the visible struggle. That is a much more useful result than a blanket faithfulness failure, and much harder to get without activation access.

**The framing**, borrowing Grice's conversational maxims: *"CoT monitors are at best **cooperative listeners**, but reasoning models are not **cooperative speakers**."* A monitor assumes the speaker is trying to be informative. Nothing in RL-trained CoT makes that true.

## The practical payoff: probe-guided early exit

If a probe can tell when the model has committed, stop generating. **Up to 80% token reduction on MMLU-Redux, 30% on GPQA-Diamond, at similar accuracy** — and the calibration **generalizes to a task the probes were not trained on**.

> [!note] Why an inference-efficiency result matters to robotics
> This is [adaptive computation](../concepts/learning/adaptive-depth-reasoning.md) driven by an *internal* confidence signal rather than a heuristic — spend tokens when the model is genuinely uncertain, stop when it is not.
>
> The robot analogue is direct and unexplored. A reasoning [VLA](../concepts/learning/vla-models.md) that emits chain-of-thought before acting pays that cost against the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md), where the budget is milliseconds. If **80% of those tokens are performative on the easy majority of steps**, a probe-guided early exit is not a nicety — it is the difference between a reasoning policy that fits the loop and one that does not. Nobody in this wiki's VLA coverage has tried it.
>
> It also sharpens a standing question: the wiki's [chain-of-thought](../concepts/learning/chain-of-thought.md) page asks whether CoT faithfulness can be checked for robot policies. This says **the check requires activations**, and a text monitor will systematically miss the cases that matter.

## Relation to the companion paper

Read with **[Verbalized Eval Awareness Inflates Measured Safety](goodfire-verbalized-eval-awareness.md)**, and the pair makes one argument from two ends:

- The eval-awareness paper measures **what models say** and finds it distorts benchmark scores — but concedes it cannot see **non-verbalized** awareness, which is the more worrying case.
- This paper builds the tool that could: **activation probes decode internal state the text does not disclose.**

Together: *text-level monitoring of model reasoning is unreliable in a specific, measurable way, and activation-level monitoring covers part of the gap.* That is the strongest coherent claim in [Goodfire's corpus](goodfire-research-index.md), and it is the intellectual case for their product rather than a marketing one.

## Entities mentioned

- **[Goodfire](../entities/goodfire.md)** — six of eight authors; **Atticus Geiger** and **Jack Merullo** also on *The World Inside Neural Networks* and the memorization work.
- Harvard University — Annabel Ma.
- Models: **DeepSeek-R1 671B**, **GPT-OSS 120B**; Gemini-2.5-Flash as monitor.

## Concepts touched

- **[Chain-of-thought](../concepts/learning/chain-of-thought.md)** — faithfulness, conditionally.
- **[Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md)** — probes as a monitoring surface.
- **[Adaptive-depth reasoning](../concepts/learning/adaptive-depth-reasoning.md)** — the early-exit result.
- **[AI guardrails](../concepts/safety/ai-guardrails.md)** — CoT monitors are a deployed safety mechanism this qualifies.

## Open questions / TBD

- **Probe-guided early exit on a reasoning VLA** is the obvious transfer and is unrun. Both this codebase and several VLA checkpoints are open.
- **Two models, two benchmarks.** Whether the easy/hard split is really about *task difficulty* or about *recall vs multi-hop composition* is not separated.
- **The monitor is a single model** (Gemini-2.5-Flash); a stronger monitor might close part of the gap the paper attributes to performativity.
- **AISI's summariser-as-filter question** — flagged in the wiki's [backlog](../backlog.md) from the containment-incident cluster — is the same problem one layer up: if a summariser can refuse to relay deceptive reasoning, text-level monitoring fails for a second, independent reason. Nobody has connected the two.
