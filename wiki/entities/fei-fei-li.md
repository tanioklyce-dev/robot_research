---
title: Fei-Fei Li
type: entity
subtype: person
created: 2026-08-03
updated: 2026-08-26
sources: 6
tags: [person, stanford, computer-vision, embodied-ai, behavior, code-as-policy, world-model, spatial-intelligence, policy]
---

**Fei-Fei Li** — Sequoia Professor of Computer Science at Stanford; **founding director and senior fellow of [Stanford HAI](stanford-hai.md)**; ImageNet. On partial leave from Stanford to serve as **co-founder and CEO of [World Labs](world-labs.md)**. In this wiki she appears as **senior author on [VoxPoser](voxposer.md)**, co-author on **[CaP-X](cap-x.md)**, and co-author of the **[HAI world-model policy brief](../sources/hai-world-model-spatial-intelligence-brief.md)** — bracketing the code-as-policy thread at both ends and now opening the wiki's world-model governance thread.

## Papers in this wiki
- **[VoxPoser](../sources/voxposer-paper.md)** (CoRL 2023) — senior author; 3D value maps composed by LLM-written code.
- **[CaP-X](../sources/cap-x-paper.md)** (ICML 2026) — co-author on the benchmark framework.
- **[The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)** (HAI Issue Brief, July 2026) — co-author; the brief's organizing **renderer / simulator / planner** framework is borrowed from [**A Functional Taxonomy of World Models**](../sources/world-labs-functional-taxonomy.md) (World Labs blog, 2026-06-03), bylined "the World Labs team and I" and filed here as [world-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md).
- **[A Functional Taxonomy of World Models](../sources/world-labs-functional-taxonomy.md)** (2026-06-03) — co-author as CEO; the POMDP derivation and the **simulator-is-the-linchpin** argument.
- **[Building Worlds That Train Robots](../sources/world-labs-r2s2r.md)** (2026-07-28) — [World Labs](world-labs.md)' [R2S2R](../concepts/robotics/real-to-sim-to-real.md) results, published as the evidence for that argument.
- **[a16z conversation on the SceniX acquisition](../sources/a16z-worldlabs-scenix-conversation.md)** (2026-07-28) — with Martin Casado and her former postdoc [Yunzhu Li](yunzhu-li.md).

## The spatial-intelligence turn

The wiki now holds three snapshots of the same person moving down the stack. VoxPoser (2023) puts an LLM on top of a motion planner and lets it write value maps. CaP-X (2026) benchmarks that whole class of agent. The HAI brief (2026) argues that the *environment model* underneath both is the thing nobody knows how to certify — and names [spatial intelligence](../concepts/world-models/spatial-intelligence.md), not language, as the capability that matters next.

> [!note] Dual role
> She is simultaneously co-author of a policy brief recommending public investment in shared simulation infrastructure and CEO of a company that would benefit from it. The brief discloses this ([details](stanford-hai.md#funding-disclosure)).
>
> The wiki can now say more precisely what the company does. In the four weeks after the brief, World Labs [acquired SceniX](../sources/world-labs-scenix-acquisition.md) and published [robot sim-to-real results](../sources/world-labs-r2s2r.md) — moving from the *renderer* category the brief calls commercially mature into the *simulator* category the taxonomy essay calls most consequential and the brief recommends public investment in. The overlap between the recommendation and the business is now direct rather than notional.

## Two positions from the a16z conversation

**Counterfactual reasoning is what simulation gives that data cannot.** Her defense of learned simulation does not rest on fidelity at all:

> "There isn't a binary choice between simulation or no simulation… Think about human intelligence. **We do a lot of simulation in our head.** Why? There's a very important role simulation plays that real-world data doesn't play, which is **counterfactual reasoning** — you play out events that haven't happened or cannot happen, or you don't have enough data to make it happen in the real world. And while you play it out, you learn how to act in it."

Her anchor: "Waymo has officially said they use **billions of hours of simulation**, and Waymo is more simulation-heavy than just real-world-data heavy" — with her own caveat, "cars are the simplest kind of robots."

> [!note] Notably cool on humanoids, from a seat where that is unexpected
> "Humanoids mimic the human body, and evolution has optimized the human body for **unstructured environments**… What humans evolved into is this body shape that can be very general **but not necessarily best at everything.** … From a business point of view, from a pragmatic technology point of view, this unstructured environment and a generalized body is actually **the hardest problem to solve. It's not necessarily even the right way to solve the problem.**"
>
> Paired with "even an LLM does not have human brain efficiency — **the human brain operates on 30 watts**," and her summary line: **"the hardest thing in today's AI is to have the right measured optimism."** Both she and [Yunzhu Li](yunzhu-li.md) argue for specialized bodies in *semi-structured* environments, which is a datapoint against the wiki's [humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) from two people with every incentive to be bullish.

## Why it matters in this wiki
Her group is also behind **[BEHAVIOR](behavior-benchmark.md)** — one of CaP-Gym's three simulator backends and the long-horizon household suite where [ASPIRE](aspire.md) posts its human-exceeding results. So the Stanford contribution to this thread is both a method (VoxPoser) and the hardest evaluation environment it is measured in.

## Related
- [Wenlong Huang](wenlong-huang.md) — VoxPoser first author, her student; also reviewed an early version of the HAI brief.
- [VoxPoser](voxposer.md) / [CaP-X](cap-x.md) / [BEHAVIOR](behavior-benchmark.md).
- [Stanford HAI](stanford-hai.md) / [World Labs](world-labs.md).
- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md) / [world-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md).

## Mentioned in
- [VoxPoser paper](../sources/voxposer-paper.md)
- [CaP-X paper](../sources/cap-x-paper.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)
- [A Functional Taxonomy of World Models](../sources/world-labs-functional-taxonomy.md)
- [Building Worlds That Train Robots (R2S2R)](../sources/world-labs-r2s2r.md)
- [World Labs Acquires SceniX](../sources/world-labs-scenix-acquisition.md)
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../sources/a16z-worldlabs-scenix-conversation.md)
