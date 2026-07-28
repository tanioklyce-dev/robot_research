---
title: "Project Fetch: Can Claude train a robot dog?"
type: source
url: https://www.anthropic.com/research/project-fetch-robot-dog
author: Anthropic Frontier Red Team (no individual byline)
affiliations: Anthropic
published: 2025-11-12
ingested: 2026-07-27
venue: anthropic.com — Policy > Frontier Red Team
format: web article (blog / research note)
tags: [anthropic, claude, uplift-study, quadruped, robot-dog, frontier-red-team, ai-safety, responsible-scaling, embodiment, human-ai-collaboration]
---

## Summary

Anthropic's Frontier Red Team ran a one-day **randomized uplift study**: eight Anthropic staff with no robotics background were split into two teams of four and asked to program a quadruped "robodog" to fetch a beach ball. **Team Claude** had Claude; **Team Claude-less** did not. Team Claude finished **7 of 8 tasks** to Team Claude-less's **6**, completed the tasks *both* teams finished in roughly **half the time**, wrote about **9× more code**, and was the only team to get the robot autonomously finding and approaching the ball. Beyond the performance gap, the post reports a **behavioral** result: transcript analysis found Team Claude-less expressed significantly more negative emotion (p = 0.0017, Cohen's d = 2.16) and twice the confusion, and asked 44% more questions — while Team Claude fragmented into four humans each pairing with their own Claude rather than working as a team. The framing is a safety argument, not a robotics one: the dek asks "How could frontier AI models like Claude reach beyond computers and affect the physical world?", and the reflection section argues that in AI, **uplift historically precedes autonomy**, so measurable uplift on unfamiliar hardware is an early indicator worth tracking under Anthropic's Responsible Scaling Policy.

> [!note] Not a robotics-capability paper
> This is a **policy/evaluation** artifact filed under Anthropic's Frontier Red Team, not a robot-learning result. Nothing here advances quadruped control. What it measures is *how much faster non-experts touch unfamiliar physical hardware when an LLM is in the loop* — the wiki's first ingested source that treats "can a model help you reach into the physical world" as a **threshold to monitor** rather than a capability to build.

## Experimental design

**Uplift study** — the method: randomize participants into a treatment arm (has AI) and a control arm (does not), and measure the performance differential. The post notes Anthropic has previously used this design in its **biological-risk** work; Project Fetch ports it to robotics. See [AI uplift studies](../concepts/safety/ai-uplift.md).

- **Participants** — 8 Anthropic employees, none roboticists. (Footnote: a couple had done high-school-level Lego robotics; acknowledged as a minor confound.) All are daily Claude users in their normal jobs.
- **Arms** — Team Claude (n=4, Claude access) vs Team Claude-less (n=4, no AI).
- **Duration** — a single workday.
- **Environment** — a warehouse space with a fake-grass play area and a beach ball.
- **Task ladder (three phases):**
  1. **Phase 1** — drive the robot to the ball using the **manufacturer's own controller**. Baseline familiarization; no AI advantage expected.
  2. **Phase 2** — connect their *own* laptops to the robot, read its **onboard sensors (video camera + lidar)**, write custom movement software, and fetch the ball programmatically.
  3. **Phase 3** — **autonomy**: the robot must locate and retrieve the ball with no human directional input.
- **Task calibration** — chosen to fill one day without being so hard that neither team showed measurable progress. The post concedes beach-ball retrieval has no economic value; it is framed as the physical-world successor to **Project Vend** (Claude running a small retail operation through *human* intermediaries), with robots substituted for the human hands.

## Key claims

### Performance

- **Task count** — Team Claude **7/8**, Team Claude-less **6/8** (Table 1 in the post breaks tasks down by connectivity / control / detection / localization).
- **Speed** — on the tasks *both* teams completed, Team Claude took **≈50% of the time** (Figure 1).
- **Autonomy** — by end of day Team Claude's robot could autonomously **locate the ball, navigate to it, and manipulate it**, but lacked the dexterity to complete the retrieval. Team Claude-less reached no autonomous capability.

### Where Claude's advantage was largest

- **Connecting to unknown hardware.** The single biggest gap. Multiple connection methods to the robot existed, with **online documentation of varying accuracy**. Team Claude navigated the options efficiently; Team Claude-less was **misled by inaccurate online information** and prematurely discarded the *simplest* connection method, only recovering after hints from the organizers.
- **Sensor access, especially lidar.** Team Claude-less had to dedicate **one team member for the whole day** to extracting lidar data, succeeding only near the end; they fell back on the video camera for Phase 3. This is the concrete shape of the "unfamiliar SDK / undocumented sensor stack" tax.

### Where Team Claude-less was faster

- Once the video connection was up, Team Claude-less **wrote its control program faster** and finished **localization** (recovering position relative to previous locations) sooner.
- **Interface trade-off** — Team Claude built a controller with *streaming* video from the robot's viewpoint (slower to build); Team Claude-less shipped one on intermittent *still images* (less intuitive, faster to build).
- **Localization detail** — Team Claude-less ran one approach straight through in about the time Team Claude spent on parallel exploratory attempts: Team Claude's first solution came out with inverted coordinates, they switched to alternative approaches, then reverted to just fixing the coordinates.
- **Volume ≠ progress** — Team Claude produced **~9× more code** (Figure 2), which the post describes as including "arguably distracting" **side quests** running parallel to the actual objective.
- **Comprehension** — team members speculated Team Claude-less would score **higher on a post-hoc quiz** about the software libraries involved, despite being slower. Speed-vs-understanding trade-off, offered as speculation, not measured.

### Team dynamics and affect (the transcript analysis)

Claude analyzed recorded team dialogue using **dictionary-based text analysis** in the LIWC tradition (Pennebaker & Francis 1996; Tausczik & Pennebaker 2010). Statistics via **two-sided Mann-Whitney U** (asymptotic normal approximation); effect size via Cohen's d.

| Measure | Result |
|---|---|
| Negative-emotion word frequency | Team Claude-less significantly higher — **p = 0.0017, d = 2.16** (large effect) |
| Net emotion (positive − negative) | **Not** significant — **p = 0.2703** |
| Expressions of confusion | Team Claude-less **≈2×** |
| Questions asked | Team Claude-less **+44%** |

- The negative-emotion gap **persisted across the whole day**, even after Team Claude-less started succeeding and Team Claude hit frustration when time ran out mid-Phase-3. The *net* emotion measure washes out because end-of-day mood shifts partly offset the mid-day gap.
- **Work-style divergence.** After initial group consultation, Team Claude members mostly **split off to pair individually with their own Claude instances** on parallel objectives. Team Claude-less strategized together and consulted each other frequently — more interpersonal engagement. The post offers the counter-reading that Team Claude was effectively **"eight agents, not four people."**
- **A design observation, flagged as changeable.** Claude is currently built to partner with *an individual*, not to coordinate a team or divide labor across one — described as a **"malleable design choice."**
- **Withdrawal.** Team Claude-less members found going without Claude "strange"; some reported feeling their coding skills had degraded. The post notes **Claude Code had shipped only six months before the experiment** — the dependency formed that fast.

### Outtakes

- The robots shipped **pre-programmed party tricks** (dancing, standing bipedally, backflips) that participants unlocked; Team Claude-less leaned into the acrobatics after finally getting connected.
- **Side quest** — a Team Claude member built a controller taking **natural-language commands** ("walk forward", "walk backward", "do push-ups") instead of mapped keyboard buttons.
- **The green-on-green failure.** Team Claude's detector was built to find a **green** ball. Placed on the **fake green grass**, it could not separate ball from background. The post reads this as humans making a "potentially sub-optimal choice about specification level" — an instance of the general problem that physical environments supply adversarial context that a spec written indoors doesn't anticipate.
- **Safety anecdote (opening).** Team Claude's robot was commanded to move 1 m/s for 5 s toward a table less than 5 m away — an arithmetic error. It nearly hit the other team. A one-line reminder that in embodiment, an off-by-one is kinetic.

## The safety argument (Reflection)

- **Uplift precedes autonomy.** The post's central inference: in AI, the capability to *help a human* do X reliably shows up before the capability to *do X alone* — the cited precedent is code **debugging assistance → code generation**. Given Project Fetch's uplift result, they expect "frontier AI models capable of successfully interacting with previously unknown hardware" **soon**.
- **Why the Frontier Red Team cares.** Robotics capability is tracked because it bears on whether AI can **automate or accelerate the development of future AI** — a capability threshold named in Anthropic's **Responsible Scaling Policy**, on the reasoning that autonomous AI R&D could produce "rapid, unpredictable advances" faster than risk evaluation can keep up.
- **Current status** — models remain **below** the fully-autonomous-AI-R&D threshold.
- **The bottleneck is unclear.** They flag genuine uncertainty about both model improvement rates and **physical-world iteration speed**, and draw a line between *controlling existing hardware* (nearer) and *designing and building new hardware* (further).
- **Prior baseline** — the **Claude 4 System Card (p. 114)** documented an earlier evaluation of Claude training an ML model to control a quadruped **in simulation**; Claude was not yet capable of doing it autonomously.
- Intent to **re-run** the experiment with better models ("the robots are in kennels at the moment").

## Limitations (as stated in the post)

- One experiment, two teams, one day — very small sample.
- Tasks are academically interesting but practically trivial; **no economic significance**.
- **Convenience sample** of Anthropic volunteers, all daily Claude users. The Claude-less arm therefore measures *withdrawal* from a habituated tool, not the baseline of a general population. AI novices in the treatment arm would need acclimation time; AI novices in the control arm would show far less disorientation.
- **Claude's end-to-end autonomy was not evaluated at all.** This measures uplift only; the post calls itself an "important initial step towards evaluations" of autonomous robotics capability.

## Open questions

- **Which robot?** The post says only "quadruped robodog" and never names a manufacturer or model. Secondary coverage of the experiment consistently identifies it as a **[Unitree Go2](../entities/unitree-go2.md)**; the wiki treats that as *reported, not confirmed by the primary source*. The identification matters because "connecting to unknown hardware" is the headline uplift result and the Go2's SDK/DDS/WebRTC surface is exactly the kind of stack the post describes as badly documented.
- **Which Claude model?** Never stated. Claude Code is mentioned only for its release timing, not as a confirmed tool in the experiment. Given the November 2025 date, a Claude 4.x-generation model is likely but unverified.
- **What were the 8 tasks, exactly?** Table 1 is summarized by category (connectivity / control / detection / localization); the post's prose does not enumerate all eight with per-team outcomes.
- **What software stack?** No SDK, library, middleware, or language is named. For a study whose central finding is *hardware-connection uplift*, the absence of the connection method's name limits reproducibility.
- **Does the affect result survive a non-habituated sample?** The negative-emotion effect (d = 2.16) is large, but the control arm is composed of people abruptly deprived of a daily tool. How much of the measured frustration is "robotics is hard" vs "my tool was taken away" is not separable in this design.
- **The companion evaluation.** Anthropic also publishes [*How Claude Performs on Robotics Tasks*](https://www.anthropic.com/research/claude-plays-robotics) — an adjacent Frontier Red Team page not yet ingested; likely the autonomy-side complement to this uplift-side result.

## Entities mentioned

- [Anthropic](../entities/anthropic.md) — publisher and experimental subject.
- [Anthropic Frontier Red Team](../entities/frontier-red-team.md) — the authoring team.
- [Unitree Go2](../entities/unitree-go2.md) — the robot, per secondary coverage (not named in the post).

## Concepts touched

- [AI uplift studies](../concepts/safety/ai-uplift.md) — the methodology and the uplift→autonomy argument.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — Responsible Scaling Policy, capability thresholds.
- [AI red-teaming](../concepts/safety/ai-red-teaming.md) — sibling evaluation genre; this is the wiki's first *embodied* frontier-safety evaluation.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the contrast case: here Claude writes the code, it does not *sit in* the control loop.
