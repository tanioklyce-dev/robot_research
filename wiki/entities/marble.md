---
title: Marble
type: entity
subtype: product
created: 2026-08-26
updated: 2026-08-26
sources: 3
tags: [product, world-labs, world-model, renderer, simulator, gaussian-splatting, collision-mesh, 3d-generation]
---

**Marble** — [World Labs](world-labs.md)' world-generation model and **first product**; "the **code name for the base model** that World Labs has been training and iterating on" ([a16z conversation](../sources/a16z-worldlabs-scenix-conversation.md)). First public release **~November–December 2025**. Takes **multimodal prompts — text, image, video, or spatial sketch** — and generates explorable 3D environments, outputting **Gaussian splats** for visual exploration **alongside collision meshes a physics engine can operate on** ([functional taxonomy essay](../sources/world-labs-functional-taxonomy.md)).

Its maker's description (~6:04): take a prompt — "an image, a few images, or text" — and "turn that into a **geometrically consistent world** that can be represented in 3D geometry, **whether it's Gaussian splat or mesh**." The [About page](https://www.worldlabs.ai/about) adds *persistent* and *single image, video or text prompt*.

## The robotics market found it, not the reverse

Marble is how [SceniX](scenix.md) entered World Labs — **as a paying customer**, unrecognized by Fei-Fei Li at the time. And it was not alone: *"even before SceniX, our inbound customers for Marble were already seeing this kind of demand. We just cannot serve these customers. But we are already getting a lot of phone calls from early-stage robotics companies."* The [acquisition](../sources/world-labs-scenix-acquisition.md) is the response to demand a renderer product surfaced and could not fill. SceniX now uses Marble as an **internal** customer.

## Why the dual output matters

That pairing is the whole point, and World Labs says so: Marble "already outputs Gaussian splats and collision meshes from a single model, **dissolving the boundary between the renderer and the simulator**."

Under the company's own [functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md), a renderer outputs *observations* (pixels for human eyes) and a simulator outputs *state* (geometry a program can compute on). Splats are the first; collision meshes are the second. Marble is presented as the existence proof that one model can serve both — and as the first move in the direction the essay argues is most consequential: "Marble is our first move into this territory… only the first chapter of a much longer arc."

The [HAI brief](../sources/hai-world-model-spatial-intelligence-brief.md) cites Marble (with Tencent's HY-World 2.0) as evidence that **renderers are the most commercially mature** of the three categories — "already produce explorable scenes from text or image prompts."

> [!warning] The category caveat still applies to the splat half
> Renderers are "optimized for plausibility rather than underlying truth," and their output "may look convincing without preserving stable geometry or physical consistency" ([HAI brief](../sources/hai-world-model-spatial-intelligence-brief.md)). World Labs' own essay names the matching risk on the *mesh* half: **"AI-generated geometry can look correct while containing self-intersections or wrong scale that produce nonsensical physics."** Neither claim has been tested against Marble output in this wiki. See [world-model evaluation](../concepts/world-models/world-model-evaluation.md).

## Open questions

- **No architecture, parameters, training data, or benchmark results** in any ingested source. Everything here is product description from company blog posts.
- **Relationship to the [R2S2R](../concepts/robotics/real-to-sim-to-real.md) engine is still unstated**, though narrowed: Yunzhu Li says SceniX's own reconstruction is "a little bit on the heavier side" and that World Labs' **sparse reconstruction and generation** is what will make it efficient — implying Marble-class generation feeding a SceniX-class dynamics pipeline, not either one alone.
- **The ~Nov–Dec 2025 release date is spoken recollection** ("last winter, around November, December"), not a dated announcement.
- **Collision-mesh quality is unquantified** — the difference between a mesh a physics engine *can* load and one that produces correct contact dynamics is the entire simulator claim.
- **RTFM**, World Labs' real-time interactive renderer, is a separate system named in the taxonomy essay with no detail and no page here.

## Related

- [World Labs](world-labs.md) — maker.
- [SceniX](scenix.md) / [real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md).
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) — the renderer/simulator line Marble is claimed to cross.
- [Genie 3](genie-3.md) — the incumbent renderer it is named against.

## Mentioned in

- [A Functional Taxonomy of World Models](../sources/world-labs-functional-taxonomy.md)
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../sources/a16z-worldlabs-scenix-conversation.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md)
