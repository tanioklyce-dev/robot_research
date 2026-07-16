---
title: "Automated Podcast — MIT's Russ Tedrake Says Robotics Is Finally on a Rocket Ship"
type: source
url: https://www.youtube.com/watch?v=c8mQKkuEmiI
author: Automated Podcast (Brian Heater, Association for Advancing Automation / A3); guest Russ Tedrake
published: 2026-07-01
ingested: 2026-07-08
venue: YouTube (Automated Podcast; recorded at Mass Robotics, Boston)
format: video podcast, 47:12 (ingested via auto-captions + description)
tags: [russ-tedrake, tri, lbm, vla, drake, physical-ai, startup, robot-data, deployment, future-of-work, podcast]
---

# Automated Podcast — MIT's Russ Tedrake Says Robotics Is Finally on a Rocket Ship

## Summary

A 47-minute career-spanning interview with [Russ Tedrake](../entities/russ-tedrake.md) (MIT Toyota Professor; [TRI](../entities/tri.md)'s Large-Behavior-Models lead) by Brian Heater, recorded at Mass Robotics in Boston. Three things stand out: (1) **Tedrake confirms he has founded a still-stealth physical AI startup** ("the company that I'm excited to announce soon... built to maximize the chances of us getting to the next level"); (2) the cleanest published articulation of his **[LBM](../concepts/learning/large-behavior-models.md)-vs-VLA taxonomy** (LBM = any image-sequences→actions model; a VLA is one architectural choice — an uptrained VLM; a video/world-model backbone is another); and (3) a deliberate **reframing of the robot-data-scarcity narrative**: you're not competing with GPT-scale corpora, you're **"building a bridge"** from a pretrained base model's existing common sense to one new output — robot actions. Thesis of the title: talent influx + investment + China's manufacturing capacity + AI breakthroughs + demographic need have aligned; "do we have escape velocity? I think so... I would rather be on the rocket ship."

## Key claims

**The stealth startup** (~36:32–40:00 + intro)
- Tedrake has founded a physical AI startup, unannounced at recording; Heater: "more info on that new project soon." Tedrake: it "is built to basically maximize the chances of us... getting to the next level"; differentiators claimed across "data, deployments, operations, business," plus team.
- Strong hint the name references LBMs — Heater: "at least for now, it's in the company name" (unchallenged). Corroborating web signal (not from this source): a Robotics Summit keynote reveal, "Building Great Behavior Models for Industry" ([GadgetArq](https://gadgetarq.com/russ-tedrake-to-unveil-his-stealth-ai-startup-at-robotics-summit/)).
- His stated non-technical reason for founding rather than joining: shaping **"amplifying, not replacing people"** — he is "spending a lot of time talking to labor economists" and people potentially impacted, "building my empathy muscles"; credits Toyota culture (lifetime employment, aging-in-place) for the frame. "A thoughtful physical AI company could change the way that plays out." (40:07–45:00)

**LBM vs VLA** (28:38)
- "Large behavior models in my mind are **any model that takes sequences of images in and outputs actions**... A VLA in my mind is a particular type of LBM" — the choice of uptraining a VLM. "You could start with a video backbone or a world-model backbone and uptrain that to be an LBM."
- "If you want longer context lengths, you should be starting with a **video model as a backbone**." Architectures are converging but codebase agility to absorb the latest base model "is really important."
- LBM naming: coined at TRI by **Bill (Brad?)** [garbled in auto-captions]; "large behavior models was the **multitask version of [Diffusion Policy](../entities/diffusion-policy.md)**, in my vernacular."
- TRI's role: "the **science of LBMs**... the initial scaling laws... with a lot of experiments" — work that a startup wouldn't be immediately motivated to do and academia couldn't resource. The [TRI LBM paper](https://toyotaresearchinstitute.github.io/lbm1/) (linked in the show notes; **not yet ingested**) showed "robustness in individual tasks change in a substantive way by having done pre-training on other tasks" — the magic of **multitask pre-training** (35:25).

**The data-narrative reframe** (30:54–35:25)
- "That whole narrative [data scarcity] misses the bigger picture... we're starting with a strong model and **uptraining it to be a robot model**. The data you need is to **build a bridge** from that common sense to... one extra output, robot actions."
- Evidence-by-thought-experiment: give a frontier video model a photo of your robot + "make a video of it doing a dexterous task" — "it's going to do a pretty good job" → the understanding is already there; you're remapping outputs, not teaching the world.
- Practical corollary: use *all* the modalities (egocentric video, sim, UMI-style interfaces, teleop) but treat them as bridge-building — e.g. sim data of a KUKA doing a task **plus video of a KUKA** lets the model connect the datasets and transfer capabilities. "Kitchen-sink approach to data, but filtering very thoughtfully" (Heater's summary, accepted).
- On Generalist AI's from-scratch approach: "I would not throw away" the base model's value — start from it and build the bridge (his stated position; "I think Generalist is doing that at a high level" too).

**Field state & history**
- Opening thesis: "Machine learning success empirically has gotten far ahead of our ability to understand it theoretically... we've had to change from being engineers... to becoming more like **behavioral scientists** — building things we don't fully understand and probing them to figure out what the heck just happened." He still wants theory (data curricula, robustness, privacy) but "I don't think we've seen the limits of scaling yet." (00:00, 13:46–18:20)
- Locomotion solved-ish: **domain randomization in sim** ("walk over stairs and bumps... somehow good enough for almost anything in the real world — not expected it would be that easy") + GPU sim + open-source recipes made bipeds "surprisingly turnkey"; hardware cost/capability "more amazing than I might have dreamed." Walking ≠ on the path to AGI, but a general-purpose body + AI is "one of the most exciting things happening in the world." (08:33, 12:18)
- **Deployment is the next major milestone**: "the narrative of many people has shifted towards deployment... the field has to earn that"; then the virtuous cycle (more capable robots → more robots fielded → more data → more capable robots). (36:32)
- Career: Detroit-adjacent childhood (GM father); a Ford Wayne Assembly paint-shop internship where his exception-handler shut off booth fans, tipping temperature past the 82 °F unionized walk-off threshold — "a hard lesson about what it means to stop the line"; U. Michigan (video-game AI with John Laird; Microsoft Research summers); MIT Leg Lab basement (Gil Pratt departing, Jerry Pratt, Dan Paluska, Peter Dilworth's Troody dinosaur robot); thesis (2004): **passive-dynamic-walker + RL "Toddler" robot that learned to walk in ~20 minutes** — "RL before it was cool" (same era as Abbeel's apprenticeship-learning helicopters). Later removed RL from his curriculum for lack of student interest — skeptics said it wouldn't scale — before the field swung back. (02:16–12:18)
- **[Drake](https://drake.mit.edu/)**: "my horcrux — I've put a piece of my soul in that software package. I still contribute production code." (26:39)
- Boston/Mass Robotics = "an incredible place to be building a robotics company." (25:31)

## Entities mentioned

- [Russ Tedrake](../entities/russ-tedrake.md) — subject; [TRI](../entities/tri.md) — LBM program home; Drake (see [Tedrake entity](../entities/russ-tedrake.md)); [Diffusion Policy](../entities/diffusion-policy.md) — LBM lineage
- Generalist AI (discussed; no entity page), Boston Dynamics ecosystem via Mass Robotics, [Physical Intelligence](../entities/physical-intelligence.md)-adjacent VLA landscape (implicit)
- People: Brian Heater (host, ex-TechCrunch), Gil Pratt, Jerry Pratt, Dan Paluska, Peter Dilworth, Marc Raibert (hopping robots), Tad McGeer + Andy Ruina (passive dynamic walking), John Laird, Rich Sutton, Pieter Abbeel, Sebastian Seung (PhD advisor — from web bio, not the episode)

## Concepts touched

- [Large behavior models](../concepts/learning/large-behavior-models.md) — the definitional source.
- [VLA models](../concepts/learning/vla-models.md) — VLA-as-LBM-subtype taxonomy.
- [Imitation learning](../concepts/learning/imitation-learning.md), [Scaling laws — VLAs](../concepts/learning/scaling-laws-vla.md) — TRI "science of LBMs" scaling-law framing.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — domain-randomization locomotion story.

## Open questions

- ~~**The startup**: name (LBM-referencing?), funding, team, product focus~~ — **resolved 2026-07-15**: it's **[Walden Robotics](../entities/walden-robotics.md)** ([launch](walden-robotics-launch.md)) — Cambridge MA, spun out of TRI Jan 2026, **$300M seed / $1.1B**, LBM + Diffusion Policy for **manufacturing/logistics**, TRI robot-learning leadership as co-founders. The "name references LBMs" hint did **not** pan out literally — "Walden" references **Thoreau**. Whether Tedrake fully left TRI vs. dual role remains open, but the Toyota-heavy cap table implies an ongoing partnership.
- ~~**TRI LBM paper** — deserves a primary ingest~~ — **ingested 2026-07-08** ([tri-lbm-paper](tri-lbm-paper.md)); confirms the multitask-robustness and smooth-scaling claims with numbers (3–5× fine-tune data efficiency; 20–30-pt CI width at 50 rollouts).
- Who exactly coined "large behavior model" at TRI (captions garble the name — "Bill Brad…"; plausibly a TRI colleague).
- Whether his "video backbone for longer context" position is borne out publicly (cf. [Cosmos 3](../entities/nvidia-cosmos.md) policy mode as the wiki's closest analog).
