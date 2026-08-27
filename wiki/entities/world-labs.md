---
title: World Labs
type: entity
subtype: company
created: 2026-08-07
updated: 2026-08-26
sources: 5
tags: [company, world-model, spatial-intelligence, renderer, simulator, marble, scenix, r2s2r, fei-fei-li]
---

**World Labs** — spatial-intelligence company founded by **[Fei-Fei Li](fei-fei-li.md)** (CEO, on partial leave from Stanford) with **Justin Johnson, Christoph Lassner and Ben Mildenhall** ([About page](https://www.worldlabs.ai/about)). Describes itself as "a frontier AI research and product company" building "foundational world models that can perceive, generate, reason, and interact with the 3D world"; Fei-Fei Li calls it "a two-year-old startup… a frontier model lab." Entered this wiki as a **renderer** company — [Marble](marble.md) generates explorable 3D environments from prompts — and over June–July 2026 repositioned around the **simulator**: it published the argument that simulation is the linchpin, then acquired [SceniX](scenix.md) and shipped robot sim-to-real results.

## The three-post arc, June–July 2026

| Date | Post | What it does |
|---|---|---|
| 2026-06-03 | [A Functional Taxonomy of World Models](../sources/world-labs-functional-taxonomy.md) | Proposes renderer / simulator / planner; argues **the simulator is the linchpin** |
| 2026-07-21 | [World Labs Acquires SceniX](../sources/world-labs-scenix-acquisition.md) | Buys a robotics-simulation company; defers all detail |
| 2026-07-28 | [Building Worlds That Train Robots](../sources/world-labs-r2s2r.md) | Ships [R2S2R](../concepts/robotics/real-to-sim-to-real.md) results, explicitly "putting that argument to the test" |

Seven weeks from thesis to acquisition, seven days from acquisition to evidence. The sequence is worth reading as a unit: a company published a framework in which its existing product category is commercially mature but structurally limited ("renderers… cannot be trusted to design a building or train a robot"), then bought its way into the category the framework calls most consequential.

## Products and systems

- **[Marble](marble.md)** — takes text, image, video or spatial-sketch prompts and outputs **Gaussian splats plus collision meshes a physics engine can operate on**, from one model. Presented as "dissolving the boundary between the renderer and the simulator."
- **RTFM** — real-time interactive renderer, generating frames conditioned on user input. Named in the [taxonomy essay](../sources/world-labs-functional-taxonomy.md) as World Labs' answer to [Genie 3](genie-3.md); **no technical detail in any ingested source.**
- **[R2S2R engine](../concepts/robotics/real-to-sim-to-real.md)** (via [SceniX](scenix.md)) — reconstructs a real robot task as an aligned interactive world; trains policies with zero real-world data and screens checkpoints before hardware evaluation. Sold in two tiers — real-to-sim only (digitalize a task, evaluate against it) or the full pipeline — and is **embodiment- and model-agnostic**: "not building a robot, it's building an environment which another company can place their robot brain in."

## A foundation model for robotics? "We're definitely not ruling this out"

Asked directly ([a16z conversation](../sources/a16z-worldlabs-scenix-conversation.md), ~10:44), Fei-Fei Li does not deny it:

> "World Labs is building a foundation model… some of the most exciting base models are **omni-models**. They take multimodal input, they have multimodal outputs. And what is a foundation model for robotics? It's very likely going to involve **the output of actions in addition to the state of the world**, and we're definitely not ruling this out."

[Yunzhu Li](yunzhu-li.md) then states the [world-action model](../concepts/world-models/world-action-model.md) formulation exactly — action as *input* makes it a forward simulator, action as *output* makes it a policy, and the same omni-model serves as "a backbone for you to fine-tune into specific robotic applications." So the company's stated trajectory runs from renderer through simulator to the unified endpoint its own [taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) names.

## The taxonomy it authored

The **renderer / simulator / planner** framework that structures the [HAI world-model brief](../sources/hai-world-model-spatial-intelligence-brief.md) originates here, filed as [world-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md). That a company blog post became the organizing frame of a Stanford policy brief is worth noting on its own — and the brief added interactivity-as-fourth-capability and the entire governance argument, neither of which appears in the original.

> [!note] Provenance corrected 2026-08-26
> The wiki previously described the taxonomy as a *Substack post by Fei-Fei Li*. It is a post on the World Labs company blog, bylined "the World Labs team and I."

## Position in the landscape

Per the HAI brief, the world-model push splits between **tech incumbents on both sides of the Pacific** — [Google DeepMind](google-deepmind.md), [NVIDIA](nvidia.md), Alibaba, Tencent — and **newer startups**: World Labs, [AMI Labs](ami-labs.md), and Odyssey. That places World Labs in direct company with Yann LeCun's post-Meta lab, which comes at the problem from the opposite architectural pole ([JEPA](../concepts/world-models/jepa.md) latent prediction rather than pixel rendering).

Against [NVIDIA](nvidia.md) the position is more directly competitive than the brief's framing suggests: the taxonomy essay cites Omniverse's ">$1T addressable market" as the size of the simulator prize, and [R2S2R](../concepts/robotics/real-to-sim-to-real.md) attacks the same real-to-sim evaluation problem NVIDIA's [RoboLab](../sources/nvidia-robolab-evaluation-blog.md) work names as its first failure mode.

> [!note] The data-disadvantage flag, now partly answered
> The brief's analysis says the scarce input is **action-labeled interaction data** — robot trajectories, teleoperation logs, fleet streams — which "cannot simply be scraped from the internet" and compounds for whoever already deploys machines at scale. A renderer-first startup with no deployed fleet is precisely the party disadvantaged by that dynamic. The [SceniX acquisition](../sources/world-labs-scenix-acquisition.md) is a direct response: rather than collect fleet data, **manufacture interaction data by reconstructing tasks into simulation**. Whether that substitutes for real interaction data is exactly what [R2S2R](../concepts/robotics/real-to-sim-to-real.md)'s unquantified results claim and do not demonstrate.
>
> The [funding disclosure](stanford-hai.md#funding-disclosure) on the brief remains relevant: its call for public pools of shared action data would benefit this company, and its CEO co-authored it.

## Open questions

- **No funding, valuation, or headcount** in any ingested source. Founders are now known; team size is not.
- **No customer is named** — only categories (industry labs, warehouses, electronics assembly). The stated two-year success case is "validated customers in a small number of important vertical use cases" as **lighthouse examples**, which implies they are not there yet.
- **No benchmark result of any kind** — not for Marble, not for RTFM, not for R2S2R. Every claim in this wiki about World Labs technology is company prose.
- **The earlier "spatial intelligence is AI's next frontier" essay** — referenced by the taxonomy post, not ingested.
- **RTFM** — named, never documented.

## Related

- [Fei-Fei Li](fei-fei-li.md) — co-founder and CEO.
- [SceniX](scenix.md) — acquired 2026-07-21.
- [Marble](marble.md) — the product.
- [Stanford HAI](stanford-hai.md) — Li is also its founding director.
- [Genie 3](genie-3.md) — the DeepMind incumbent's interactive-world model.
- [AMI Labs](ami-labs.md) — the other founder-led world-model startup here.

## Mentioned in

- [A Functional Taxonomy of World Models](../sources/world-labs-functional-taxonomy.md)
- [World Labs Acquires SceniX](../sources/world-labs-scenix-acquisition.md)
- [Building Worlds That Train Robots (R2S2R)](../sources/world-labs-r2s2r.md)
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../sources/a16z-worldlabs-scenix-conversation.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)
