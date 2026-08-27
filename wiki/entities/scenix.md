---
title: SceniX
type: entity
subtype: company
created: 2026-08-26
updated: 2026-08-26
sources: 3
tags: [company, robotics, simulation, real-to-sim, world-labs, acquisition]
---

**SceniX** — robotics and simulation company, **acquired by [World Labs](world-labs.md) on 2026-07-21**. Built the **[real-to-sim-to-real (R2S2R)](../concepts/robotics/real-to-sim-to-real.md) engine**: systems that "turn real robots, environments, and interactions into simulations for policy training and evaluation."

## Founders

Three technical co-founders, per the [a16z conversation](../sources/a16z-worldlabs-scenix-conversation.md):

- **[Yunzhu Li](yunzhu-li.md)** — robotics and robot learning; Assistant Professor of CS at Columbia, PhD MIT, postdoc at Stanford with [Fei-Fei Li](fei-fei-li.md).
- **[Changxi Zheng](changxi-zheng.md)** — physical simulation and graphics; also a Columbia professor, with a VFX background (Weta, Tencent).
- **A third co-founder**, an engineering leader from a startup acquired by Amazon who then worked across computer-vision stacks there. **His name is destroyed by the auto-captions and is not recorded anywhere in the wiki.**

The founding pair maps onto the method: R2S2R's distinguishing claim is a reconstructed world faithful in **appearance and dynamics simultaneously**, and the team is one roboticist and one simulation/graphics researcher.

## What it built

Per World Labs' [R2S2R post](../sources/world-labs-r2s2r.md), the engine "turns one physical task into many controllable, reusable worlds, helping robotics teams train policy models and test changes faster, uncover failures earlier, and reduce costly experimentation on hardware." The first published results appeared **seven days after the acquisition** ([2026-07-28](../sources/world-labs-r2s2r.md)) — policies trained with zero real-world data transferring to ALOHA, YAM, RB-Y1, Flexiv and xArm platforms on contact-rich tasks, and simulated evaluation preserving real-hardware policy rankings.

## How the acquisition actually happened

Not a long-planned reunion between Fei-Fei Li and her former postdoc. **SceniX arrived as a paying Marble customer** ([a16z conversation](../sources/a16z-worldlabs-scenix-conversation.md), ~5:03):

> "You would think — because we worked together, he was my amazing postdoc… **It's actually not true. They came into World Labs as a customer.** When we released the first version of our generative model called Marble last winter, around November, December, SceniX just signed up. **And I didn't even know what it was.**"

Fei-Fei Li adds that the inbound demand was general, not specific to SceniX: World Labs was "getting a lot of phone calls from early-stage robotics companies" for Marble and "just cannot serve these customers." So the acquisition is better read as **a renderer company discovering it had a robotics market it could not address, and buying the team that could** — than as a top-down strategic pivot.

## What customers buy

Two tiers, per Yunzhu Li:

- **Real-to-sim only** — "they want to digitalize the task they care about and be able to do the evaluations of their robotic systems."
- **The full R2S2R pipeline** — "such that they'll be able to have policies running on their hardware."

The platform is **embodiment-agnostic** (single arm, bimanual, fixed arm, mobile manipulators, varied end effectors) and **model-agnostic** (train from scratch, or post-train existing [VLAs](../concepts/learning/vla-models.md) / [world-action models](../concepts/world-models/world-action-model.md)). Casado's summary, which Yunzhu Li confirms: *"that's not building a robot, it's building an environment which another company can place their robot brain in."* Customers are described as "pretty close to the deployment stage," each with "tons or hundreds" of instances of the task they want automated.

## Why World Labs bought it

The [acquisition post](../sources/world-labs-scenix-acquisition.md) states the strategy as combining "spatial intelligence, world models, learning-based simulation, and a closed loop with real-world learning," and says the SceniX team "broadens our use cases from virtual to physical environments."

Read against World Labs' own [functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md), the move is legible: World Labs was a **renderer** company by its own classification, and its essay argues renderers "cannot be trusted to design a building or train a robot." SceniX supplies the **simulator** half — the category the essay calls the linchpin. It also addresses the structural disadvantage the wiki had flagged on the [World Labs page](world-labs.md): a startup with no deployed robot fleet cannot collect action-labeled interaction data at scale, so it buys the machinery to *manufacture* it instead.

## Integration

Deliberately slow. Fei-Fei Li: *"we're not rushing to integrate everything from codebase to teams… we're not rushing to blend the team as a full salad bowl,"* because SceniX has "a fairly contained tech stack as well as their customers." Integration starts on **simulation** and the **action-conditioned base model**, and SceniX now uses [Marble](marble.md) as an *internal* customer. The acquisition makes World Labs **bi-coastal** — a New York office alongside San Francisco HQ, with **robots deployed in both** so the team can practice working with hardware remotely, as its customers must.

> [!note] Still no primary SceniX source
> Founding date, funding, headcount, named customers, and publications remain absent. Whether the R2S2R technology is SceniX's pre-existing stack, [Marble](marble.md) extended, or a fusion is still unstated — though Yunzhu Li says SceniX's own reconstruction was "a little bit on the heavier side" and that World Labs' **sparse reconstruction and generation** is what makes it efficient, which implies a real fusion rather than a rebrand.

## Related

- [World Labs](world-labs.md) — acquirer.
- [Real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md) — the technology.
- [Marble](marble.md) — World Labs' existing world-generation product, and the front door SceniX came in through.
- [Yunzhu Li](yunzhu-li.md) / [Changxi Zheng](changxi-zheng.md) — co-founders.

## Mentioned in

- [World Labs Acquires SceniX](../sources/world-labs-scenix-acquisition.md)
- [Building Worlds That Train Robots (R2S2R)](../sources/world-labs-r2s2r.md)
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../sources/a16z-worldlabs-scenix-conversation.md)
