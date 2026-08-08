---
title: World Labs
type: entity
subtype: company
created: 2026-08-07
updated: 2026-08-07
sources: 1
tags: [company, world-model, spatial-intelligence, renderer, marble, fei-fei-li]
---

**World Labs** — spatial-intelligence startup co-founded and led by **[Fei-Fei Li](fei-fei-li.md)** (on partial leave from Stanford to serve as CEO). Builds [world models](../concepts/world-models/world-model.md) in the **renderer** sense: interactive, explorable 3D environments generated from text or image prompts.

> [!note] Thin entry — no primary World Labs source ingested
> Everything here comes from the [HAI world-model brief](../sources/hai-world-model-spatial-intelligence-brief.md), which names World Labs as an example rather than documenting it. No funding, team size, model architecture, parameter count, or benchmark result is in the wiki. Ingesting the June 2026 Substack post and any Marble technical material is a known gap.

## Marble

World Labs' product, cited by the brief as evidence that **renderers are the most commercially mature** of the three world-model categories — Marble and **Tencent's HY-World 2.0** "already produce explorable scenes from text or image prompts." No technical detail beyond that in the wiki.

The caveat the brief attaches to the whole category applies: renderers are "optimized for plausibility rather than underlying truth," and their output "may look convincing without preserving stable geometry or physical consistency." See [world-model evaluation](../concepts/world-models/world-model-evaluation.md).

## The functional taxonomy

The **renderer / simulator / planner** framework that structures the HAI brief originates in a World Labs Substack post — *"A Functional Taxonomy of World Models,"* by Fei-Fei Li, **June 3, 2026**. Filed here as [world-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md). That a company blog post became the organizing frame of a Stanford policy brief is worth noting on its own.

## Position in the landscape

Per the brief, the world-model push splits between **tech incumbents on both sides of the Pacific** — [Google DeepMind](google-deepmind.md), [NVIDIA](nvidia.md), Alibaba, Tencent — and **newer startups**: World Labs, [AMI Labs](ami-labs.md), and **Odyssey**. That places World Labs in direct company with Yann LeCun's post-Meta lab, which is the wiki's other founder-led world-model startup and comes at the problem from the opposite architectural pole ([JEPA](../concepts/world-models/jepa.md) latent prediction rather than pixel rendering).

> [!warning] Structural disadvantage, and the policy that would relieve it
> The brief's own analysis says the scarce input is **action-labeled interaction data** — robot trajectories, teleoperation logs, fleet streams — which "cannot simply be scraped from the internet" and compounds for whoever already deploys machines at scale. A renderer-first startup with no deployed fleet is precisely the party disadvantaged by that dynamic, and precisely the party helped by the brief's call for public pools of shared action data. See the [funding disclosure](stanford-hai.md#funding-disclosure).

## Related

- [Fei-Fei Li](fei-fei-li.md) — co-founder and CEO.
- [Stanford HAI](stanford-hai.md) — she is also its founding director.
- [Genie 3](genie-3.md) — the DeepMind incumbent's interactive-world model.
- [AMI Labs](ami-labs.md) — the other founder-led world-model startup here.

## Mentioned in

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)
