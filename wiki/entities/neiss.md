---
title: NEISS
type: entity
subtype: dataset
created: 2026-08-03
updated: 2026-08-03
sources: 1
tags: [neiss, injury-data, dataset, safety, public-health]
---

**NEISS** — the US **National Electronic Injury Surveillance System**, a stratified sample of approximately **100 US hospitals** with 24-hour emergency departments. Roughly **500,000 injuries reported annually**, with data back to **2001**, carrying narrative descriptions, diagnosis codes, and demographics.

## Why it appears in this wiki
It is the empirical backbone of **[ASIMOV-Injury](asimov-benchmark.md)** ([paper](../sources/asimov-benchmark-paper.md)). From the **338,265 cases in the 2023 subset**, Gemini 1.5 Pro generates first-person and third-party safety scenarios, re-weighted to match the real injury-type distribution.

Sample narratives, verbatim from the data: *"10YOF MOM WENT TO GIVE HER LIQUID AND INSTEAD GAVE HER A TEASPOON OF SYNTHETIC DYE"*, *"19YOM GRABBED FLAT IRON THAT WAS HOT"*, *"32YOM STEPEPD ON A NAIL"*.

This is the wiki's clearest instance of **grounding an AI safety benchmark in real-world harm statistics** rather than researcher intuition — the long tail is sampled from what actually sends people to hospital.

> [!note] Coverage boundaries
> US-only, and only injuries that **present at an emergency department**. Harms that don't reach a hospital, and all non-US legal/cultural contexts, are structurally absent — which interacts with ASIMOV's own argument that constitutions need regional customization.

## Related
- [ASIMOV Benchmark](asimov-benchmark.md) — the consumer.
- [Semantic safety](../concepts/safety/semantic-safety.md).

## Mentioned in
- [ASIMOV Benchmark paper](../sources/asimov-benchmark-paper.md) — the ASIMOV-Injury data source.
