---
title: Inner Monologue
type: entity
subtype: system
created: 2026-08-03
updated: 2026-08-03
sources: 2
tags: [inner-monologue, llm-agent, closed-loop, feedback, replanning, google]
---

**Inner Monologue** — Robotics at Google, CoRL 2022. Closes the loop on [SayCan](saycan.md) by continually injecting **textual environment feedback** (success detection, scene description, object recognition, human answers) back into the LLM prompt, forming a running monologue the planner reasons over. No training; few-shot prompting only ([paper](../sources/inner-monologue-paper.md)).

## The result worth carrying
**Closed-loop feedback is worth little in nominal conditions and decisive under disturbance.** In the real kitchen, adding feedback moves SayCan from 50% → 75% on manipulation without disturbance — but from **0% → 75%** on mobile manipulation *with* disturbance, because SayCan has no high-level retry behavior at all.

On the real tabletop, object feedback alone gives 45% and success detection alone 40%, but **together 90%** — the two are complementary, not redundant.

## Position in the lineage
This is the **2022 origin of the finding both 2026 papers rediscover**: the bottleneck is the feedback channel, not the model. [ASPIRE](aspire.md) re-derives it at finer granularity — per-primitive multimodal traces move macro-average success 14% → 62%. Inner Monologue established *that* feedback matters; ASPIRE established that its *resolution* matters.

> [!warning] Oracle feedback caveat
> Two of the three domains assume "oracle scene descriptors in the form of human observers or scripted systems." Only the real tabletop experiment uses learned perception end-to-end.

## Related
- [SayCan](saycan.md) — baseline, environment, and task definitions.
- [ASPIRE](aspire.md) — the 2026 descendant; feedback made per-primitive and measured.
- [CaP-X](cap-x.md) — independently finds feedback *modality* matters (structured text beats raw pixels).
- [Wenlong Huang](wenlong-huang.md), [Fei Xia](fei-xia.md), [Andy Zeng](andy-zeng.md), [Brian Ichter](brian-ichter.md) — co-first and senior authors.

## Mentioned in
- [Inner Monologue paper](../sources/inner-monologue-paper.md) — primary source.
- [Introducing Waddle](../sources/waddle-labs-introducing-waddle.md) — cited in Waddle's lineage survey.
