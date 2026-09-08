---
title: "Embodied AI: Systems that See, Hear, and Act in the World Alongside Humans — Yann LeCun in conversation with Marc Pollefeys (AI House Davos 2026)"
type: source
url: https://www.youtube.com/watch?v=pJyoqapCRZE
author: "Yann LeCun (Founder and Executive Chairman, Advanced Machine Intelligence); Marc Pollefeys (Professor, ETH Zürich / ETH AI Center; host)"
venue: "AI House Davos 2026 — a side venue during the WEF Annual Meeting, run by the ETH AI Center, Merantix, G42, HPE, EPFL AI Center and the University of Tokyo; not an official WEF session. Fireside conversation, summit stage."
published: 2026-01-22
ingested: 2026-09-07
format: "video, 54:18; YouTube auto-captions (English) as transcript"
local_path: raw/2026-01-22-ai-house-davos-embodied-ai.en.vtt
sha256: 6cdafeb5364263cfb8e30f21c045d23b1d3bb46aeef1a8844e9fbe49600a6ba2
tags: [lecun, ami-labs, davos, ai-house, embodied-ai, world-model, jepa, v-jepa-2, vla, hierarchical-planning, domestic-robots, humanoid, self-supervised, test-time-adaptation, hardware, convnets, primary-source, video, transcript]
---

## Summary

**The January-2026 LeCun primary — the one Fortune quoted, and the most complete statement of his robotics position in this wiki.** Fifty-four minutes with Marc Pollefeys, one day after AMI Labs was announced, on the day he was also interviewed by [MIT Technology Review](mit-tech-review-lecun-ami-labs-interview.md). Where the interview gives two answers about robots, this conversation gives the whole argument: what a robot's world model has to contain, why VLAs are the expert systems of the 2020s, how V-JEPA 2 was made action-conditioned with little data, why hierarchical planning is *"a completely unsolved problem in AI"* that *"people have mostly given up"* on, and why online adaptation is *"not a particularly challenging conceptual problem."* It also carries the *"LLM-pilled"* line, the *"digging the same trench"* line, and the statement that leaving Meta was partly because *"Meta also became LLM-pilled."*

On the question this wiki brought to it — when do household robots arrive — the answer is the same shape as [Davos 2025](wef-davos-2025-debating-technology.md) and the [interview](mit-tech-review-lecun-ami-labs-interview.md): *"we don't have domestic robots, we don't have level-five self-driving cars still"*; *"none of those companies, absolutely none of them, has any idea how to make those robots smart enough to be useful — it's a big secret of the robotics industry"*; and the bar is *"nearly as good common sense as your house cat."* The nearest thing to a timeframe: *"that's the challenge for the next few years — getting a system to really understand the real world,"* and a company that aims to *"solve that problem within a few years."* **Both clocks are on the world model, not the robot.**

> [!note] Which recording, and why this one
> Two recordings exist. An attendee's phone upload (35 min, posted 2026-01-21) starts eleven minutes in and has worse captions; it was downloaded, checked against this one, and discarded as a duplicate. This is AI House's own upload of the full session. Captions garble names — the host says *"Jan"* throughout, *"Jepa"* becomes *"Jeff architecture"* twice — and one numeric claim is unusable (see §Hardware). Pollefeys is identified from the description; the description's framing (*"from navigation to mobile manipulation… how soon we can expect to see these technologies making a tangible impact on our daily lives"*) is AI House's, and the conversation never returns to that question with a date. Timestamps are `[mm]` minutes into the video.

## Key claims

### Robots: what is missing and how long

- **[03–04]** *"We have systems that can pass the bar exam… write code. But they don't really deal with the real world, which is the reason why we don't have domestic robots, we don't have level-five self-driving cars still."* Pollefeys: level four exists. LeCun: with full maps, geofencing, *"exotic sensors, lidars"* — *"I don't think that's cheating, by the way"* — but expensive, and *"how is it that a 17-year-old can learn to drive in 10 to 20 hours of practice?"* Imitation from millions of hours of human driving *"doesn't work. You don't get reliable driving systems this way."*
- **[04]** *"There's a lot of companies building humanoid robots… they play kung fu… This is all precomputed. **None of those companies, absolutely none of them, has any idea how to make those robots smart enough to be useful. It's a big secret of the robotics industry.** You can train them on very narrow tasks, and you have to collect lots and lots of data the same way people thought they would build self-driving cars… practical for a small number of narrow tasks, and you don't have robots that have nearly as good common sense as your house cat, let alone human intelligence."*
- **[04–05]** *"That's the challenge for the next few years: getting a system to really understand the real world. And the problem is that the approaches that have been successful for language do not work for high-dimensional, continuous, noisy data."*
- **[35]** The zero-shot standard: *"ask a 10-year-old to clear the dinner table and fill up the dishwasher. A 10-year-old can do it the first time. Doesn't need to be trained for it… Why? Because of a world model."*
- **[52–53]** Asked about ten years out: *"I'm starting a new, very ambitious company with the idea that we're going to be able to solve that problem within a few years — systems that understand the physical world or any modality you throw at them, can build world models, use them to plan, build hierarchical world models… This is going to be the next AI revolution."*

> [!warning] Still no date on the robot
> Read the three January-2026-and-earlier primaries together — [Davos 2025](wef-davos-2025-debating-technology.md), the [interview](mit-tech-review-lecun-ami-labs-interview.md), and this — and the structure never changes: robots are what a world-model breakthrough unlocks; the breakthrough gets *"a few years"*; the robots get nothing. AI House's own description promised the conversation would address *"how soon"*; it did not. The [Hassabis](wef-davos-2026-the-day-after-agi.md) session the same week has the identical shape from the other camp.

### VLAs as the expert systems of the 2020s

- **[06–07]** VLMs mix visual tokens into LLM machinery; VLAs make the output a sequence of actions. *"There's a major flaw… they only work in situations where the actions obey a script that you have to basically repeat all the time… **a new way of automating a task, which is data-driven instead of programmatic.** But it's very brittle, very restricted to narrow applications for which there is a script you can follow."*
- **[11–12]** The analogy, new to this wiki: 1980s expert systems — *"the coolest job at the time was going to be knowledge engineer… translate the knowledge of the human expert into rules and facts… That approach essentially failed because of the brittleness of the resulting system and the cost of knowledge transfer into a machine. **It's going to be the same thing for VLA.** A relatively small number of applications where you have scripted scenarios."*
- **Pollefeys pushes back, twice [10–11, 12]:** *"In industry there are many things that are useful and that are scripted… a lot of potential for this current technology to deliver value with today's state… probably a simpler way to program than what we used to do before."* LeCun concedes the point without conceding the frame: *"Those things are useful… LLMs are super useful for coding, no question."*

> [!note] The wiki's counter-evidence, for the record
> The [VLA page](../concepts/learning/vla-models.md) carries the standing counterargument — [π0.7](../entities/pi07.md)'s out-of-distribution emergent tasks, RT-2 generalization — and the [code-as-policy](../concepts/agents/code-as-policy.md) lineage's constant finding that code agents degrade gracefully where trained policies fall off a cliff *and lose to them in-distribution*. LeCun's "data-driven instead of programmatic" is a precise description of the trade the field made, and Pollefeys's reply is the industry's: the scripted regime is where the money is.

### World models, abstraction, hierarchy

- **[08–09] Definition:** *"Given the state of a system you want to control at time T, and an action or intervention you imagine taking, can you predict the state at T+1? … You don't do this at the pixel level. You do this in an abstract representation space."* The dress example: *"absolutely no way in hell I can predict the texture of your beautiful dress."*
- **[14–19] Hierarchical planning:** the New York → Paris decomposition; *"this is called hierarchical planning. **It's a completely unsolved problem in AI. People have mostly given up.**"* Requires a *multi-level world model*: low level short-term, detailed, muscle-level, *"not describable in language"*; high level *"maybe VLA will do something like that"* if scripted. **The abstraction level a JEPA learns depends on the prediction horizon it is trained at** — 10 ms, then a tenth of a second, then longer. Quantum-field-theory-of-this-room as the reductio. Pollefeys: JEPA today learns *"a fixed level"*; LeCun: *"we're working on multi-level hierarchies."* (Three months later: [HWM](../entities/hwm.md).)
- **[20–21, 37–38] What a robot's world model contains:** (1) a **mechanical dynamical model** of the robot — *"you can write down such models with a bunch of equations, this is what classical robotics is about… the kung-fu videos, that's what they do, planned in advance using handwritten models, fine-tuned a little with RL"*; (2) a **model of the environment** — intuitive physics, learned *"as babies by watching the world go by"* (gravity at 9 months: 6-month-olds don't attend to a floating car, 10-month-olds do); (3) a **model of the interaction** — *"if I close my hand here, nothing happens; around the glass, I pick up the glass."*

### V-JEPA 2 and the embodiment question

- **[22–24]** Recipe: 64-frame windows, mask, encode both, predict the full representation from the corrupted one, train end to end. Trained on *"the equivalent of 100 years of video"* — *"about a day of YouTube uploads"* — **10¹⁵–10¹⁶ bytes at 2 MB/s, "100 times more than the biggest LLMs"** against text's ~10¹⁴. Hence, again, *"never going to get to human-level intelligence by training LLMs or on text only."*
- **[24–25] Violation of expectation:** show a ball that stops mid-air, turns into a cube, or vanishes — *"the prediction error goes to the roof… the first time I've seen any kind of model that has some level of common sense."* (The [LeWM](../entities/leworldmodel.md) surprise-score result is the small-scale version.)
- **[36–38] Transfer to an embodiment**, answering Pollefeys directly: freeze the encoder, fine-tune the predictor with an action input over (robot state, world state, action) → next state. *"That fine-tuning phase does not require that much data. And the data you can obtain through simulation — **not a simulation of a task, a simulation of just the dynamics**… the model you get is generic, you can use it for any task."* Announces **V-JEPA 2.1** as *"coming out soon."*

### The disagreement: can pixels do it?

- **[25–29]** Pollefeys: given a start frame, a pixel-level video model would also flag the impossible event. LeCun: *"I hope you'll pardon my French, but absolutely no way in hell… It simply does not work. I've tried to do self-supervised learning from video for 15 years. The first 10 years I tried generative models with latent variables… it never worked for natural video."* Mechanism: infinite plausible futures → the predictor averages them; diffusion avoids the blur but *"can be completely mode-collapsed… it will produce a nice video but not understand the underlying dynamics."* Evidence offered: MAE vs [DINO](../entities/dino.md) — reconstruction *"very expensive to train and the representation you get out of it sucks"*; joint-embedding SSL *"beats all approaches to supervised learning, even those for which we have tons of data — this is new, only happened in the last year."*

> [!note] The wiki's own reading is narrower than either side here
> [Joint-Embedding vs Reconstruction](joint-embedding-vs-reconstruction-paper.md) gives the condition under which LeCun is right — high-magnitude irrelevant features — and the regime where reconstruction is *correct*, not merely adequate. And [the anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) records that MAE fine-tuned reaches 84.0 with no augmentation at all. "Sucks" is a linear-probe verdict; the crossover is the finding.

### The cake, RL, and simulation

- **[30–33]** The 10-year-old slide: SSL is *"the genoise"*; a thin layer of supervised / imitation / behavior cloning / inverse RL (*"most animals never go to that phase because they never meet their parents… octopus"*); RL *"the cherry… minor fine-tuning because it's so inefficient."* Pollefeys interjects that the SSL layer *"would also be embodiment agnostic"* — LeCun agrees. The cliff: a car would run off *"a few dozen times"* per cliff, *"and then you're next to another cliff."*
- **[33–34]** Pollefeys: simulation decouples the cost — gaits, crawling, *"thousands you might do on one GPU."* LeCun: *"possibly… not if you have perception"*; and *"it will only be trained for this particular task, this particular environment, and it'll be brittle… we can cheat our way out or engineer the hell out of it… 30-year-old gadgets that can beat us at chess."*

### Inductive bias, ConvNets, and real time

- **[39–43]** Pollefeys's frustration: robot policies trained to *"this exact camera, this exact arm, a fixed background."* LeCun: with self-supervised video you have *"more data than you can manage,"* so architectural priors may be unnecessary — but **ConvNeXt** (Saining Xie) shows *"nothing intrinsic about the architecture"* for images; transformers become impractical for high-resolution, high-frame-rate video; and *"**every single real-time vision system uses convolutional nets.** Every car sold in Europe has to have automatic emergency braking… every single one of them uses a convolutional net. Because you need real time, and you're not going to get that from transformers, at least not today."*

### Hardware, rates, and adaptation

- **[44–48]** Power goes to memory traffic, because CMOS forces hardware multiplexing; the brain has *"one physical synapse and one physical neuron per virtual neuron… the weights are in place."* Fix requires exotic analog / 3D / non-volatile technology that *"does not exist."* Human numbers: retina ~15 Hz, brain ~10 Hz, ~100 ms perception + ~100 ms decision → **~300 ms** brake reaction; *"cats are faster… they can stand in front of a cobra."* (Compare the wiki's [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).) One caption-garbled numeric — cerebellum vs cortex neuron counts — is not recoverable and is omitted.
- **[48–51] Online adaptation:** analog chips of the 1980s–90s had to be trained in the loop because device characteristics vary, making each system *"unique… mortal, like a human brain."* Asked whether learning-in-the-loop is coming for embodied systems: *"clearly yes, and I actually don't think it's a particularly challenging conceptual problem. I don't think we need to invent anything new."* The heavy-glass example: the world model *"adapts in milliseconds… probably in the cerebellum."* Pollefeys: that's the cherry, that's RL. LeCun: *"**Absolutely not.** It's self-supervised… my prediction was wrong, I observe what occurred, I adjust my predictor. No task, no reinforcement, no value function. Just prediction error."* (Five months later, his own group publishes exactly this: [AdaJEPA](../entities/adajepa.md).)

### Closing exchange

- **[53–54]** Pollefeys: *"they're generative, but at different levels of abstraction."* LeCun: *"My definition of generative is that you reproduce the input signals. Here you make predictions at representation level. That's not generative in my world."* — a definitional dispute, and the wiki's [generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) page is on the same fault line.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — the primary for his January-2026 robotics position.
- [AMI Labs](../entities/ami-labs.md) — *"Founder and Executive Chairman"*; *"solve that problem within a few years."*
- [Meta FAIR](../entities/meta-fair.md) — *"Meta also became LLM-pilled… one big reason I left."*
- [V-JEPA 2](../entities/v-jepa-2.md) — the recipe, the data arithmetic, the action-conditioned transfer; V-JEPA 2.1 pre-announced.
- [HWM](../entities/hwm.md) — *"we're working on multi-level hierarchies,"* realized in April.
- [AdaJEPA](../entities/adajepa.md) — the online adaptation he says needs nothing new, published in June.
- [DINO](../entities/dino.md) · [MAE](../entities/mae.md) — the comparison he rests the anti-generative case on.
- Marc Pollefeys (ETH Zürich / ETH AI Center; host) — no entity page.

## Concepts touched

- [World model](../concepts/world-models/world-model.md) · [JEPA](../concepts/world-models/jepa.md) — definition, abstraction-by-horizon, hierarchy.
- [VLA models](../concepts/learning/vla-models.md) — the expert-systems analogy; "data-driven instead of programmatic."
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — the cerebellum argument.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the three components of a robot's world model map onto the ladder.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the dishwasher standard.

## Open questions

- **"Meta also became LLM-pilled… with sort of recent research thing"** — the caption is incomplete at the key clause; whether he named a specific reorganization is unrecoverable from this recording.
- **"Only happened in the last year"** — that joint-embedding SSL beats supervised learning even with abundant labels. Which result he means is not stated; [DINOv3](dinov3-paper.md) is the likely referent and the wiki has not checked the claim.
- **The interaction sub-model** — he names three components of a robot world model; whether V-JEPA 2-AC learns the third separately or entangled is not addressed, and the [JEPA-WMs](jepa-wms-paper.md) ablations do not split it either.
- The October-2025 MIT keynote with the same *"big secret"* line remains un-ingested; it is now the older duplicate rather than the missing primary.
