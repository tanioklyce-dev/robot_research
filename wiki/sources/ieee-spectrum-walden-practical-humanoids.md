---
title: Walden Robotics Partners With Toyota on Practical Humanoids (IEEE Spectrum)
type: source
url: https://spectrum.ieee.org/humanoid-robots-walden-robotics-toyota
author: Evan Ackerman
affiliation: IEEE Spectrum
published: 2026-08-03
ingested: 2026-08-28
venue: IEEE Spectrum
format: article
tags: [walden-robotics, russ-tedrake, wheeled-base, mobile-manipulation, humanoid, amr, safety-case, grippers, diffusion-policy, toyota, manufacturing]
---

> [!note] Independent reporting, not a vendor post
> An interview piece by IEEE Spectrum's robotics editor. Rare in this wiki's humanoid coverage: the reasoning is on the record and attributed, and the reporter pushes back in his own voice. It **resolves the standing "robot hardware" open question** on [Walden Robotics](../entities/walden-robotics.md), which the July launch left blank. Also circulated under the headline *"Why Walden's Humanoid Robots Run on Wheels, Not Hype."*

## Summary

[Walden Robotics](../entities/walden-robotics.md) — the [TRI](../entities/tri.md) spinout led by **[Russ Tedrake](../entities/russ-tedrake.md)** — builds a **humanoid torso with two arms and simple two-finger grippers on a large wheeled base**. No legs. The article is essentially one sustained argument for that choice, made by the person with the least obvious incentive to make it: Tedrake taught legged locomotion at MIT for two decades and led Team MIT's bipedal entry in the DARPA Robotics Challenge.

The reasoning inverts the industry's usual order. Ackerman: *"Rather than developing a robot first and searching for a viable commercial use case second, Walden instead identified applications where robots can provide value now, and designed a robot that could safely and efficiently meet those needs."*

## Key claims

### Why no legs

> **"It's ironic," says Tedrake. "I thought about legs for 20 years; that's the class I teach at MIT. There are many reasons to build a robot with legs. But the question is, what's the addressable market? And what percentage of it is covered by a wheeled base?"**

Three distinct advantages, only one of which is mechanical:

1. **The safety case already exists.** *"Factories already have autonomous mobile [wheeled] robots. They already have safety cases built around AMRs. **You can piggyback on that** with a wheeled base."* — a **regulatory** argument, not an engineering one.
2. **Statically stable robots cannot fall over.** This "bypasses the safety challenges that are currently keeping legged humanoids physically separated from real humans."
3. **The base is a battery compartment.** *"You're incentivized to cram the base full of batteries, since more weight near the floor keeps the robot stable, which also solves the problem of running out of power during the middle of the workday."*

Ackerman states the counter-case fairly: *"stairs exist, for one, and legged robots have a smaller footprint compared with ones that have wheels."*

### Why simple grippers

Two-finger grippers, not five-fingered hands:

> **"There's a question of what you need to do the tasks, but the real question is just durability. We have been deployed in a Toyota factory, and at the end of the week, the hands take a beating, so we built hands that can take that. I have not seen a more dexterous hand that could have done the work our hand has done."**

### The economics

- *"You need to find applications with **high utilization** — where the robot is used 24 hours a day, 7 days a week. Manufacturing is a global imperative right now, and it makes the economics work."*
- The bar Ackerman names: robots "are going up against human workers who are **more flexible while also cheaper to employ**."

### Hardware, such as it is described

- **Humanoid torso, two arms, wheeled base.** No robot name given.
- *"The robot's **chonky** design allows it to meet the **high-payload requirements** of useful manufacturing work."*
- *"Simple, rugged grippers make the robot suitable for commercial deployment."*
- A "slightly asymmetric head" that Walden "isn't sure why people like... but they do."

### The AI, and Ackerman's pushback

- Built on TRI's [diffusion policy](../entities/diffusion-policy.md) line, *"which helps robots learn new skills more quickly by leveraging previously learned skills as a foundation."*
- Tedrake: *"Fundamentally, **multitasking is a way to get to a general-purpose robot**. I believe there is a single platform that can do a lot of tasks that are of high value for real customers."*
- Ackerman, in his own voice: *"nobody is quite sure what 'general purpose' means… I think the closest we can get are robots that can be taught to do a useful number of different skills, which is why I prefer the term **'multipurpose.'** … the distinction is important because it moderates expectations."*

### Toyota

- Tedrake: *"I was never asked how much money this is going to make, but I was asked **how it will improve the quality of life for all people**."*
- Ackerman's caveat: Walden's people-first framing depends on customers sharing it, and *"not all customers will share Toyota's priorities."*

## Assessment

> [!note] The safety-case argument is the sharpest thing in this article
> The other two wheel arguments are mechanical and familiar. "Piggyback on the AMR safety case" is **regulatory arbitrage**, and it is the one a robotics researcher would be least likely to reach for. Factories already run autonomous mobile robots under established safety cases; a statically stable wheeled machine slots into that paperwork, while a legged humanoid needs a case nobody has written. That is a **years-of-calendar-time** advantage that no amount of locomotion research buys.
>
> Set this next to [Figure](../entities/figure.md), which is on the opposite strategy: it went to an OSHA NRTL to **create** a UL 2271 humanoid-battery standard because none existed ([F.03 battery](figure-f03-battery.md)). Two coherent answers to the same problem — **inherit an existing regulatory regime, or write a new one**. Walden's is faster; Figure's, if it works, is a moat. See [robot safety standards](../concepts/robotics/robot-safety-standards.md).

> [!note] A natural experiment in car factories
> Both companies are deployed in automotive plants doing parts handling. [Figure 03](../entities/figure-03.md) argues at BMW that its task is *"structurally infeasible to solve with traditional, fixed automation or six-axis robotic arm"* ([F.03 at BMW](figure-03-at-bmw.md)). Walden argues the wheeled base covers the addressable market. **Neither publishes throughput, cycle time, or success rate**, so the experiment is running with no readout. The wiki should treat "do factory tasks need legs?" as genuinely open, with a well-argued case on each side and no data on either.

> [!warning] The thesis is documented; the machine is not
> Walden publishes **no height, weight, payload, reach, DOF, sensor suite, battery capacity, runtime, compute, price, or robot name** — and no success rate, robot count, or task detail (Tedrake cites partner confidentiality). "Chonky" and "high-payload requirements" are the entire payload specification. This is the mirror image of Figure, which publishes manufacturing numbers and no AI numbers; Walden publishes **reasoning** and no numbers of any kind.

> [!note] Whose word this is
> Tedrake is not a neutral party — he is arguing for the product he sells. What makes the argument unusually credible is that it **costs him something**: he spent twenty years on legged locomotion, teaches it, and competed in the DARPA Robotics Challenge with a biped. When the person with the deepest sunk investment in legs publicly concludes the addressable market does not need them, that is worth more than a competitor saying it.

## Entities mentioned

- [Walden Robotics](../entities/walden-robotics.md) · [Russ Tedrake](../entities/russ-tedrake.md) · [Toyota Research Institute](../entities/tri.md) · [Diffusion Policy](../entities/diffusion-policy.md)

## Concepts touched

- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — the AMR safety-case inheritance argument.
- [Large Behavior Models](../concepts/learning/large-behavior-models.md) — the multitask → general-purpose thesis.
- [Collaborative robots](../concepts/robotics/collaborative-robots.md) — statically stable machines sharing floor space with people.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — what a wheeled base makes unnecessary.

## Open questions

- **Any specification at all.** Payload is the one that matters for the "chonky" claim and it is never given.
- **Is the base holonomic or differential-drive?** Determines whether the arms can be positioned without repositioning the whole robot.
- **Does the torso have a lift/prismatic axis?** The difference between reaching a floor bin and a high shelf, and the axis [Stretch](../entities/stretch.md) is built around.
- **How much remote human assistance is actually in the loop?** The launch described "powerful autonomy combined with a human available for remote assistance"; the ratio is the whole story on autonomy claims.
- **How many robots, doing what, at which Toyota plant?** Confidential.
