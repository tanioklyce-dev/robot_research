---
title: "Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)"
type: source
url: https://www.youtube.com/watch?v=-tabaM5l3s0
local_path: https://www.worldlabs.ai/blog/news-july-2026
author: Martin Casado (a16z) with Fei-Fei Li and Yunzhu Li
published: 2026-07-28
ingested: 2026-08-26
venue: a16z (YouTube), embedded on the World Labs blog
format: video interview (~42 min)
tags: [world-labs, scenix, real-to-sim-to-real, simulation, robot-policy-evaluation, humanoids, world-action-model, spatial-intelligence, teleoperation, a16z]
---

# Fei-Fei Li is Solving the Hardest Problem in Robotics

**Martin Casado** (a16z) with **[Fei-Fei Li](../entities/fei-fei-li.md)** (co-founder/CEO, [World Labs](../entities/world-labs.md)) and **[Yunzhu Li](../entities/yunzhu-li.md)** (co-founder, [SceniX](../entities/scenix.md); Assistant Professor of CS, Columbia). ~42 minutes.

> [!note] Transcript is machine-generated and garbles every proper noun
> "SceniX" appears as *Cynics / Synex / Synenix / Phoenix*; "Yunzhu" as *Yunu / Vindra / Vindrew / Renu / Vundra*; "Changxi Zheng" as *Changi Jan*; "Fei-Fei" as *Feay / Fay / Faith / FIP*. Names below are **verified against the [World Labs About page](https://www.worldlabs.ai/about) and Yunzhu Li's own public account of the acquisition**, not taken from the captions. Quotes are lightly cleaned of caption artifacts; timestamps are approximate.

## Summary

The reasoning behind the [SceniX acquisition](world-labs-scenix-acquisition.md), which the announcement post deliberately withheld. Yunzhu Li lays out the [R2S2R](../concepts/robotics/real-to-sim-to-real.md) argument in commercial terms — what customers actually buy, and why — and Fei-Fei Li supplies the conceptual defense of simulation: **counterfactual reasoning is the thing real-world data structurally cannot provide.** The most useful material is the parts that contradict the usual pitch: humanoid timelines are "a little bit aggressive," the target is **semi-structured** environments not homes, human-level power efficiency "will take a very long time," and simulation is explicitly *not* proposed as a replacement for real data. Also contains the acquisition's origin story, which is not what anyone would guess.

## Key claims

### The origin story: SceniX was a Marble customer first

Casado assumes the two had planned this for years. Fei-Fei Li corrects him (~5:03):

> "There is a funny story here, because you would think — because we worked together, he was my amazing postdoc, we've been talking about this and World Labs integration for a long time. **It's actually not true. They came into World Labs as a customer.** … When we released the first version of our generative model called Marble last winter, around November, December, SceniX just signed up. **And I didn't even know what it was.** And then I realized this is Yunzhu's company."

That dates Marble's first public release to **~November–December 2025**, and makes the acquisition inbound-led rather than strategically premeditated. Fei-Fei Li adds that this was not isolated (~26:43): *"even before SceniX, our inbound customers for Marble were already seeing this kind of demand. We just cannot serve these customers. But we are already getting a lot of phone calls from early-stage robotics companies."*

### Who SceniX is

- **[Yunzhu Li](../entities/yunzhu-li.md)** — co-founder; Assistant Professor of CS at **Columbia**. PhD at **MIT**, postdoc at the **Stanford Vision and Learning Lab with Fei-Fei Li** (one year — "he already had his faculty offer"). Described by Li as "a full-stack researcher in robotics, from modeling to hardware."
- **[Changxi Zheng](../entities/changxi-zheng.md)** — co-founder; also a Columbia professor, "a world-class technologist in simulation," with a **VFX background — Weta, Tencent**, and prior entrepreneurship.
- **A third co-founder**, described as "a phenomenal engineering leader" from a startup **acquired by Amazon**, who then worked across computer-vision tech stacks at Amazon. **The captions garble his name beyond recovery** (rendered "Sunonni"/"Sunny"); not recorded here as fact.

**Complementarity, per Fei-Fei Li:** SceniX brings full-stack robotics and simulation; World Labs brings "the generative model side as well as the computer vision 3D reconstruction side — that's a technology SceniX needs." Yunzhu Li's version (~10:15): SceniX's reconstruction of appearance, geometry **and dynamics** is "still a little bit on the heavier side," and World Labs' **sparse reconstruction and generation** capability is what makes it efficient.

### Marble, described by its maker

(~6:04) "Marble is the **code name for the base model** that World Labs has been training and iterating on. The fundamental capability right now of Marble that is publicly released is to take a prompt — it can be an image, a few images, or text — and turn that into a **geometrically consistent world** that can be represented in 3D geometry, **whether it's Gaussian splat or mesh**."

### "Can we expect a foundation model for robotics from World Labs?"

Fei-Fei Li (~10:44): *"World Labs is building a foundation model… some of the most exciting base models are omni-models. They take multimodal input, they have multimodal outputs. And what is a foundation model for robotics? It's very likely going to involve **the output of actions in addition to the state of the world**, and **we're definitely not ruling this out.**"*

Yunzhu Li then states the [world-action model](../concepts/world-models/world-action-model.md) formulation exactly (~11:48):

> "If you think about **actions as inputs**, that is essentially a **forward simulator** that predicts how the environment is going to change when you apply a specific action. When the **action is output**, this is essentially a **policy** model… this kind of omni-model can also act as a **backbone for you to fine-tune into specific robotic applications**."

### Why simulation, against the standard objection

Casado raises **[Sergey Levine](../entities/sergey-levine.md)**'s position by name (~18:04): *"simulation will always eventually deviate from the physical world and real-world data collection is absolutely critical."*

Yunzhu Li's answer is explicitly non-oppositional (~18:35): **"They don't contradict with each other."** Simulation is a model of the world; "it doesn't necessarily have to be pure physics — it can be a combination between both physics and also learning." The proposed trajectory is a **shifting mixture over the data flywheel**: physics-heavy at the start "to make sure we have the right consistency and right structure," moving "towards more learning-based modeling of the environments" as real data accumulates through deployment and customer collaboration.

Fei-Fei Li's conceptual defense (~19:32) is the more quotable half:

> "There isn't a binary choice between simulation or no simulation… Think about human intelligence. **We do a lot of simulation in our head.** Why? There's a very important role simulation plays that real-world data doesn't play, which is **counterfactual reasoning** — you play out events that haven't happened or cannot happen, or you don't have enough data to make it happen in the real world. And while you play it out, you learn how to act in it."

Her empirical anchor: **"Waymo has officially said they use billions of hours of simulation, and Waymo is more simulation-heavy than just real-world-data heavy"** — with the caveat she supplies herself, *"cars are the simplest kind of robots."*

### The fidelity question, answered by analogy

Casado presses for a formal statement of "how close is close enough." Yunzhu Li declines a formal answer and gives the locomotion argument instead (~17:36):

> "Quadruped robots, bipedal robots — they can walk on snow, they can walk on bushes. But you don't need a simulator that can simulate all the bushes and snow very precisely. You need a simulation that **captures the essential structure of the problem** and does a whole different kind of randomizations inside the digital environment."

He states the open problem plainly: *"what is the level of fidelity we need to model the massive worlds… such that we'll be able to transfer the robotic systems trained in the simulated environment back into the real scenarios."*

### Two levels of benefit: reliability and efficiency

The clearest commercial articulation in the interview (~21:24), and the second half is an argument the wiki did not have:

- **Reliability** — "you need data to provide **systematic coverage of all the state space** and the variations that robots might encounter." In simulation you can randomize "lighting, frictions, geometries, object types and all different kinds of physical parameters."
- **Efficiency** — and here the argument is about **speed**, not cost:

> "If you look at many of the teleoperation devices — imagining all the exoskeletons you are using — **you're actually collecting the data at a speed that is slower than a human actually doing the task.** But for many of our clients, human speed to them is not good enough. **They want faster than human speeds.** For the robot to move faster, it's not as simple as just driving the robot faster, **because the gravity doesn't change.** But in simulation, you can do systematic speed-up of the robot's behaviors to train the robot such that it considers all the dynamics changes of the environment."

### Evaluation, defined operationally

Yunzhu Li on what "eval" means to a robotics customer (~23:45):

> "For this specific checkpoint, how well does it perform? Does it perform 95% of the time or 99.9% of the time? And **the key criterion people use in industry is how long in wall-clock time does it take for you to distinguish between a checkpoint that is 90% from a checkpoint that is 92%.** And if you only do that in the real environment, that just takes so long."

Plus the iteration-rate claim, repeated from the [R2S2R post](world-labs-r2s2r.md): real-world robotic evaluation is "**multiple orders of magnitude slower** than iterations of those language models" — and, in Casado's gloss, *"atoms have to move through space."*

### What the product actually is

- **Infrastructure, not a robot.** Casado makes the distinction explicit and Yunzhu Li confirms it: *"that's not building a robot, it's building an environment which another company can place their robot brain in."*
- **Embodiment-agnostic and model-agnostic.** Customers run "single robot arm… bimanual… fixed arm… mobile manipulators… grippers… more elaborate versions of the end effectors." On the model side: train "from scratch or doing post-training of existing foundation models like **vision-language-action models or world-action models**."
- **Two purchasable tiers** (~40:12): *"Some customers need **only the real-to-sim part** — they want to digitalize the task they care about and be able to do the evaluations of their robotic systems. Some customers need this real-to-sim-to-real entire pipeline such that they'll be able to have policies running on their hardware."*
- Customers are **"pretty close to the deployment stage,"** working on tasks where "at least tons or hundreds of these kinds of situations" exist to automate.

### On humanoids — notably unenthusiastic

Yunzhu Li's structural-environment ladder (~29:41): **fully structured** (factories, car manufacturing — "automated for decades") → **semi-structured** (Amazon warehouses, restaurants, hotels — "certain control over the environment") → **unstructured** (homes, "the grand challenge"). His position: *"it's so much easier and more approachable, at least right now, to focus more on the semi-structured environments before we move on to fully unstructured environments."* Casado's framing, which neither guest disputes, is that Yunzhu Li thinks "a lot of the predictions around humanoids were a little bit aggressive."

Fei-Fei Li's evolutionary argument against the humanoid form factor (~30:57) is striking coming from her seat:

> "Humanoids mimic the human body, and evolution has optimized the human body for **unstructured environments**. Our fingers, our legs are not the best apparatus to do one thing. If our only goal as a species is to climb trees, we will not have this body… What humans evolved into is this body shape that can be **very general but not necessarily best at everything.** … But from a business point of view, from a pragmatic technology point of view, this unstructured environment and a generalized body is actually **the hardest problem to solve. It's not necessarily even the right way to solve the problem.**"

### On timelines and power

Casado asks whether robots will reach human power efficiency on menial tasks — "5 years or never?" Yunzhu Li: **"I think it's going to take a very long time."** His reasoning is systems-level: "every working robot in the real environment is a system… the hardware, the software, the brain, even the details of what's the friction coefficient of your fingers."

Fei-Fei Li: **"even an LLM does not have human brain efficiency. The human brain operates on 30 watts."** She concedes performance-per-watt may be close for narrow tasks like image generation or software engineering, and adds: *"I don't think we're anywhere close when it comes to robotics."* Her summary line — **"the hardest thing in today's AI is to have the right measured optimism."**

### The reliability asymmetry against LLMs

Yunzhu Li (~35:44), and this is the sharpest framing in the interview:

> "The current state of the language models — those are models with incredible capabilities, but still **you don't just blindly trust it to book your flight tickets or make your hotel reservations**; hopefully there's still a person reading the output. **But that is very different from how people will be using robotic models, because for robotic models, out of the box, the robot has to work reliably in the real environment.** And we don't even have the data, we don't even have all the necessary infrastructure around those for the robots to just out-of-box work reliably."

### Object permanence as the video-model critique

Asked to contrast R2S2R with the video-model approach most robotics companies take (~13:13), Yunzhu Li names **consistency** — "over space, over time, over different viewpoints, and over different types of interactions" — and gives the concrete failure:

> "Imagine if a robot pushes an object forwards. **The object just magically disappears**, which has been a problem of many of the existing video prediction models. This won't provide good enough signal for the robot to know what is the right thing to do."

### Integration and logistics

Not rushing: *"we're not rushing to integrate everything from codebase to teams… we're not rushing to blend the team as a full salad bowl."* SceniX has a "fairly contained tech stack as well as their customers." Integration is starting "on the simulation side as well as the potential base-model action-conditioned model side," and SceniX now uses Marble as an **internal** customer. World Labs is "officially becoming a **bi-coastal company**" — HQ San Francisco, new **New York** office for East Coast talent, with **robots in both offices** specifically so the team can "work with robots remotely, because we have to do that for our customers." Yunzhu Li is moving to San Francisco.

**Two-year success case**, per Fei-Fei Li: "validated customers in a small number of important vertical use cases where our infrastructure has proven to be truly beneficial to their automation needs… these customers became our **lighthouse examples** to scale our business."

### One incidental datapoint on BEHAVIOR

Yunzhu Li, on the survey behind [BEHAVIOR-1K](../entities/behavior-benchmark.md) (built during his Stanford postdoc): *"We actually sent out surveys asking the general public what they want their robots to do for them. **Among the thousand tasks we collected, one-third of the tasks are about cleaning.** People just don't like to do those dull and dirty tasks."*

## How this lands against the wiki

- **It closes the [R2S2R page](../concepts/robotics/real-to-sim-to-real.md)'s biggest open question in the wrong direction.** The blog post's "zero real-world training data" reads as a claim that simulation replaces real data. Here both principals say it does not: physics-heavy early, learning-heavier as real data accumulates, with real data collected continuously through customer deployments. The blog post oversells relative to what its own authors say in conversation.
- **The counterfactual argument is the strongest available defense of learned simulation**, and it is orthogonal to fidelity. Even a *wrong* simulator lets you play out branches that never occurred; the question is whether the branches are informative. The wiki had this only implicitly, via [FOREWARN](forewarn-paper.md)'s use of a world model to predict outcomes of plans that were never executed.
- **"Distinguish 90% from 92%" is the [Clopper-Pearson bar](../concepts/robotics/robot-policy-evaluation.md#the-sample-size-problem) stated as an industry requirement.** A 2 pp discrimination is exactly the ±2 pp band that needs ≈1,030 rollouts. A practitioner independently named the wiki's own number as the operational criterion — without naming the statistics, and while selling the way around it.
- **The object-permanence failure is the [spatial-intelligence](../concepts/world-models/spatial-intelligence.md) progress probe**, arrived at independently. The wiki records the HAI brief's version — move an object, leave, return, is it still there — and the [Genie 3](../entities/genie-3.md) coherence ceiling behind it. Yunzhu Li's version is the same test at manipulation timescale.
- **The teleop-speed argument is new to the wiki.** Every prior source treats teleoperation's problem as cost and scale. This is the first to say teleop is *slower than a human doing the task by hand*, that customers want **super-human speed**, and that you cannot get there by replaying faster because gravity doesn't rescale. Filed to [real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md).
- **The humanoid skepticism is a datapoint against the wiki's humanoid material.** Two people with strong incentives to be bullish on embodied AI both argue for specialized bodies in semi-structured environments. See [humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md).

## Entities mentioned

- [World Labs](../entities/world-labs.md) — founded by [Fei-Fei Li](../entities/fei-fei-li.md) with **Justin Johnson, Christoph Lassner, Ben Mildenhall** (confirmed from the [About page](https://www.worldlabs.ai/about); the captions render the last two as "Justin Ben"). Called "a two-year-old startup… a frontier model lab."
- [SceniX](../entities/scenix.md) / [Yunzhu Li](../entities/yunzhu-li.md) / [Changxi Zheng](../entities/changxi-zheng.md)
- [Marble](../entities/marble.md) — first public release ~Nov–Dec 2025.
- [Sergey Levine](../entities/sergey-levine.md) — cited by Casado as the counter-position.
- [Waymo](../entities/waymo.md) — "billions of hours of simulation."
- [BEHAVIOR-1K](../entities/behavior-benchmark.md) — the survey, one-third cleaning.
- Martin Casado (a16z) — interviewer. No page.

## Concepts touched

- [Real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md) — the commercial articulation.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the 90-vs-92 criterion.
- [World-action model](../concepts/world-models/world-action-model.md) — stated as the foundation-model-for-robotics shape.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the physics/learning mixture over time.
- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md) — object permanence.
- [VLA models](../concepts/learning/vla-models.md) — what customers post-train.

## Open questions

- **The third SceniX co-founder's name is unrecovered** — the captions destroy it and no ingested source names the founding team.
- **No customer is named**, only categories ("industry labs, warehouses, electronics assembly"). The "validated customers in a small number of vertical use cases" success case is two years out, which implies they are not there yet.
- **"What level of fidelity is needed" is stated as the open research question and left open.** That is the honest answer, and it is also the thing the [R2S2R post](world-labs-r2s2r.md)'s results are implicitly claiming to have settled for their demo tasks.
- **Marble's release date (~Nov–Dec 2025) is from spoken recollection** ("last winter, around November, December"), not a dated announcement. Not decision-grade.
- **No numbers of any kind** — this is a conversation, not a results presentation. The blog post it accompanies remains the only source of protocol detail, and it has no success rates either.
