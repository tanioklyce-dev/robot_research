---
title: "Yann LeCun's new venture is a contrarian bet against large language models (MIT Technology Review interview)"
type: source
url: https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/
author: Caiwei Chen (interviewer); Yann LeCun (interviewee)
venue: MIT Technology Review
published: 2026-01-22
ingested: 2026-09-07
format: Q&A interview, online, "edited for clarity and brevity"
local_path: raw/2026-01-22-technologyreview-lecun-ami-labs.html
sha256: cd1f03d532739a3e48131cf92ffaa73aa67e398b1f8d9670fe100b2082b59ae3
tags: [lecun, ami-labs, jepa, world-model, domestic-robots, humanoid, vla, llm-critique, moravec-paradox, open-source, meta-fair, primary-source, interview]
---

## Summary

**The wiki's first source in which LeCun speaks directly about domestic robots, in his own words.** An exclusive Q&A from his Paris apartment, one day after AMI Labs was announced and six weeks before its $1.03 B seed round became public. Most of the interview is about the company — Paris headquarters, open-source-as-platform, the US–China binary, his departure from Meta — and the robotics content is two answers near the end. But those two answers are the clearest statement on record of **his position on when generally useful home robots arrive: not a date, a precondition.**

The precondition is the one the whole JEPA program rests on: *"If we want a generally useful domestic robot, we need systems to have a kind of good understanding of the physical world. That's not going to happen until we have good world models and planning."* He gives no year. The only timing he offers is negative and general — human-level systems are *"not going to happen next year or two years from now. It's going to take a while"* — and it is about intelligence, not robots.

The interview also settles two things the wiki had held only from secondaries: AMI Labs' leadership (LeCun as **executive chairman**, Alex LeBrun as **CEO**), and a fact no other ingested source carries — that **Meta shut down FAIR's robotics group**, which LeCun calls *"a strategic mistake."*

> [!note] Raw copy is an HTML snapshot
> `local_path` is the page as fetched on 2026-09-07 (452 KB, article inside `<article>`). No `fetch_url` is set: a news page's HTML changes with every template and ad rotation, so a hash-drift check would fire on every sweep without meaning anything. The interview text itself is the thing to compare if a revision is ever suspected; a plain-text extraction sits beside the HTML in `raw/`.

## Key claims

### On domestic and humanoid robots — the reason this was ingested

- **Why we don't have one.** The Moravec paradox framing: LLMs *"can't truly reason or plan, because they lack a model of the world. They can't predict the consequences of their actions. **This is why we don't have a domestic robot that is as agile as a house cat, or a truly autonomous car.**"*
- **Nobody knows how yet.** Asked about Chinese humanoids: *"the secret of all the companies getting robots to do kung fu or dance is they are all planned in advance. But frankly, **nobody — absolutely nobody — knows how to make those robots smart enough to be useful.** Take my word for it."*
- **The diagnosis is the VLA critique.** *"You need an enormous amount of tele-operation training data for every single task, and when the environment changes a little bit, it doesn't generalize very well. What this tells us is we are missing something very big."* The 17-year-old-learns-to-drive-in-20-hours argument follows.
- **The precondition, stated as the answer.** *"If we want a generally useful domestic robot, we need systems to have a kind of good understanding of the physical world. **That's not going to happen until we have good world models and planning.**"*
- **World models are framed as the unlock for both robots and cars.** *"An agentic system that is supposed to take actions in the world cannot work reliably unless it has a world model to predict the consequences of its actions… This is the key to unlocking everything from truly useful domestic robots to Level 5 autonomous driving."*

> [!warning] He does not give a date for household deployment — anywhere
> Read carefully, LeCun commits to a timeline for the *architecture* and refuses one for the *robot*. Here the only timing statement is *"not next year or two years from now… It's going to take a while."* Elsewhere the wiki records **3–5 years** for a new paradigm and *"maybe the coming decade will be the decade of robotics"* (Davos, January 2025 — not ingested; see Open questions), and a **1–2 year** AMI Labs plan that explicitly *excludes* robots ([Welch Labs Part 2](welchlabs-lecun-1b-bet-against-llms-part2.md)). Anyone quoting LeCun as predicting home robots by a given year is inferring, not citing.

### On AMI Labs — new facts

- **Leadership:** LeCun is **executive chairman**; **Alex LeBrun** is CEO — serial founder (first company sold to Microsoft; second to Facebook, where he ran FAIR Paris engineering; then Nabla in healthcare). *"It's going to be LeCun and LeBrun."*
- **Saining Xie** as chief scientist — asked directly, LeCun does not confirm: *"I hired him twice already… Let's just say I have a lot of respect for him."*
- **Structure:** global company, HQ Paris, a North American office (New York implied), probably Asia. LeCun keeps his NYU position.
- **Recruiting:** *"We've already recruited people from places like OpenAI, Google DeepMind, and xAI."* Motivation framed as belief in world models over pay.
- **Training data:** *"video, audio, and sensor data of all kinds — not just text… from the position of a robot arm to lidar data to audio."* Plus a project *"using JEPA to model complex physical and clinical phenomena."*
- **Target applications:** industrial processes with thousands of sensors (jet engine, steel mill, chemical factory); **smart glasses** that predict what you will do next; reliable agentic systems generally. Consistent with the industrial-first plan on the [AMI Labs](../entities/ami-labs.md) page — robots are the *eventual* beneficiary, not the target.
- **Meta relationship:** *"Meta might be our first client!"* — framed as non-competing: AMI on physical-world world models, Meta on generative AI and LLMs.
- **Funding details deferred:** *"Soon — in February, maybe."* (The $1.03 B round was reported 2026-03-09.)

### On Meta and FAIR

- **FAIR's robotics group was shut down.** *"Mark made some choices that he thought were the best for the company. I may not have agreed with all of them. For example, **the robotics group at FAIR was let go, which I think was a strategic mistake.**"* The wiki's [Meta FAIR](../entities/meta-fair.md) page had no record of this.
- FAIR *"was extremely successful in the research part. Where Meta was less successful is in picking up on that research and pushing it into practical technology and products."*
- On leaving: *"there's no reason to be upset."*

### On LLMs, open source, and academia

- **LLMs:** *"There is a sense in which they have not been overhyped"* — useful for text, research, code — but *"people have had this illusion, or delusion, that it is a matter of time until we can scale them up to having human-level intelligence, and that is simply false."* Current chatbots are *"LLM plus a lot of things"*; LLMs will be *"the orchestrator in systems, a little bit."*
- **JEPA in one paragraph:** *"The world is unpredictable. If you try to build a generative model that predicts every detail of the future, it will fail… learn an abstract representation of the world and make predictions in that abstract space, ignoring the details you can't predict."* And: *"The most exciting work so far on this is coming from academia, not the big industrial labs stuck in the LLM world."*
- **Open source as sovereignty:** all leading open platforms are Chinese; the alternative future is either proprietary US models or Chinese models needing fine-tuning to answer about Tiananmen. *"You need high diversity of assistance for the same reason that you need high diversity of press."* Positions AMI as *"a credible frontier AI company that is neither Chinese nor American."*
- **Advice to academia:** *"Don't work on LLMs. There is no point… LLMs are now technology development, not research"* — compared to speech recognition in the early 2010s.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — interviewee; this is the primary source for his domestic-robot stance.
- [AMI Labs](../entities/ami-labs.md) — leadership, structure, data modalities, target applications.
- [Meta FAIR](../entities/meta-fair.md) — robotics group shut down; research-to-product gap.
- [V-JEPA 2](../entities/v-jepa-2.md) — the "learns to represent videos really well" system he describes without naming.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the elevator pitch, in his words.
- [World model](../concepts/world-models/world-model.md) — as the precondition for reliable agents, robots, and Level 5 driving.
- [VLA models](../concepts/learning/vla-models.md) — the tele-operation-data-per-task critique, restated.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the domestic-robot bar he sets ("as agile as a house cat").
- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md) — the Moravec framing.

## Open questions

- **The Davos statement is not ingested.** *"Maybe the coming decade will be the decade of robotics"* (World Economic Forum, 2025-01-23) and the 3–5-year paradigm claim are cited from secondary coverage on the [LeCun](../entities/yann-lecun.md) page; the primary is a WEF session recording. Worth ingesting if his robotics timeline is ever quoted in a decision.
- **The October 2025 MIT keynote** where he called it *"the big secret of the industry"* that humanoid companies cannot make their robots generally useful — same claim as here, five months earlier, also un-ingested.
- **Was FAIR's robotics group actually dissolved, and when?** LeCun's is the only voice for this; no Meta statement or reporting is filed.
- **Did Saining Xie join?** Unconfirmed here.
- **Which "complex physical and clinical phenomena" project?** Possibly related to the clinical JEPA line ([EchoJEPA](../entities/echojepa.md)), which is not his; unverified.
