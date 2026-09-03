---
title: "Third World Modeling Workshop — Day 1 (Chicago Booth, 2026-08-31)"
type: source
url: https://www.youtube.com/watch?v=M8iBx7rTsdY
local_path: raw/2026-08-31-chicago-booth-world-modeling-workshop-transcript.txt
sha256: 3460545f885cc2ae92297a9f9c563f4f73aa85e528e0c8089728057cd57ddfcb
author: "Center for Applied Artificial Intelligence (CAAI), Chicago Booth; organized by Randall Balestriero"
published: 2026-08-31
venue: "Chicago Booth School of Business — livestream recording, 9h37m"
format: video (livestream) — machine transcript
tags: [world-models, workshop, jepa, lecun, balestriero, bohg, hafner, donoho, blackwell, belief-state, panel, transcript, secondary-source]
ingested: 2026-08-31
---

## Summary

Day 1 of the **third World Modeling Workshop**, hosted by Chicago Booth's Center for Applied AI. Nine and a half hours: five long talks, four lightning talks, and a one-hour panel. Previous editions were at the Flatiron Institute and in Montréal; this one was deliberately pointed at **"non-stationary signals, time series, economy, finance, business"** because the host is a business school — the organizer's framing is that world-modeling researchers "need to understand what type of properties those guys need."

> [!warning] Machine transcript — treat names and numbers as approximate
> No captions existed for this video, so the transcript in `raw/` was produced locally with Whisper (`distil-large-v3`). It is accurate on argument and unreliable on proper nouns: it renders Danijar Hafner as "Danny Jar," Yann LeCun as "Jan Lequin," and — a mistake this wiki made in consequence — [SimToolReal](simtoolreal-paper.md) as "sim tool real." **Speaker attributions below are inferred from context; quotes are lightly cleaned.** Timestamps are reliable.

**Why this source matters:** it is the connective tissue for a cluster of papers ingested here on the same day. [Vafa et al.](vafa-world-model-implicit.md) is the subject of a keynote's second half; [SimToolReal](simtoolreal-paper.md) and [Causal-PIK](causal-pik-paper.md) are both presented in Bohg's talk; [LPWM](lpwm-paper.md) is a lightning talk. And the opening keynote is about **David Blackwell** — whose 1957 paper the wiki chased the same day and could not obtain.

## Programme

| Time | Speaker | Topic |
|---|---|---|
| 00:31 | **Randall Balestriero** (organizer) | Framing: third edition, business/time-series focus |
| 00:41 | Booth deputy dean for faculty | Booth's **Applied AI faculty area** — its first new faculty area in decades, currently two untenured assistant professors |
| 00:45–01:40 | **Dave Donoho** (Stanford Statistics) | *"David Blackwell the mathematician, Blackwell the GPU, and Blackwell's World Models theorem"* |
| 01:55–02:42 | **Aditya Grover** (UCLA / Inception) | Multimodal world modeling; **diffusion language models**; complementary unmasking; a novel caching scheme |
| 02:46–03:39 | **Jeannette Bohg** (Stanford) | World models from robotics: **latency**; [SimToolReal](simtoolreal-paper.md); [Causal-PIK](causal-pik-paper.md) at 03:16 |
| 04:45–05:36 | **Yilun Du** (Harvard) | Embodied reasoning with world models |
| 05:36–06:36 | **Danijar Hafner** (independent) | *"Predict Everything"* — Dreamer 4 and where the field is |
| 06:52–07:09 | Lightning talks ×4 | incl. **[LPWM](lpwm-paper.md)** (NYU, LeCun's group); one on *selection-induced optimism* |
| 07:16–08:11 | **Yann LeCun** (NYU / AMI Labs) | Keynote + Q&A |
| 08:19–09:37 | **Panel** | Balestriero moderating LeCun, Bohg, Hafner and others |

## The Blackwell keynote (Donoho, 00:45)

Donoho's premise is a pun with substance: *"everyone knows the current generation of dominant GPU hardware is called Blackwell, but very few people know anything about the man's life."* The work is joint with his brother Andrew, run on a **dual DGX Spark system** — GB10 Blackwell chips, i.e. deliberately using Blackwell silicon to study Blackwell's theorem — and he notes Claude was used extensively for the experiments.

The biography he gives: Howard University (an HBCU) in the 1940s → sabbatical at Stanford in the early 1950s → **Berkeley's first Black tenured professor**, and the first Black mathematician elected to the US National Academy of Sciences. Donoho credits him with founding *"essentially modern dynamic programming associated with understanding and controlling Markov processes, which is now called reinforcement learning,"* done in the late 40s and early 50s, and a book with **Abe Girshick**, founder of Stanford's statistics department. Blackwell died in 2010; the National Medal of Science followed posthumously in 2014.

The talk's second half is a walkthrough of **[Vafa et al.'s](vafa-world-model-implicit.md) Manhattan taxi experiment** — sequences of compass directions between shuffled intersection IDs, and the question of what implicit world model sits behind them. Donoho notes an AI-generated podcast about the paper had reached his feed, which he plays.

> [!note] The wiki chased Blackwell 1957 the same day and failed
> *The entropy of functions of finite-state Markov chains* (Prague 1957) is not digitized; the wiki ingested [Jurgens & Crutchfield](jurgens-crutchfield-hmp-entropy-rate.md) as a carrier instead. This talk is a second, independent secondary — and the only one in the wiki that treats Blackwell as a *person* rather than a citation.

## The panel is the most valuable hour

**On what everyone agrees a world model needs:** solving tasks post-training zero-shot or with very fast adaptation, and training on **real, uncurated video** — one panelist: *"world models out there trained mostly on simulation data, I think they're not that useful."*

**Bohg's nuance is the sharpest thing in the session**, and it reframes a claim this wiki has been circling:

> Most of the data VLAs are trained on is *"very carefully curated successful demonstrations only… What's interesting about the world model is that you can actually also train on failures. In VLA land you think of that as low quality, but in the world-model end this is actually providing you with the **counterfactuals** that you need to then plan and reason or learn in imagination."*

She adds that even egocentric human data is task-labelled toward eventual success, so the recovery behaviour is thin there too.

**LeCun on imitation learning**, stated more bluntly than in his written work:

> *"We can learn to drive in about 20 hours of practice and we have millions of hours of training data of experts driving cars, and we still don't have level-five self-driving cars. This is why I'm saying imitation learning has been a failure for [autonomous] driving. And believe me — I believed in this 15 years ago, not anymore."*

His cliff argument: a world model tells you that turning the wheel right runs the car off, *for any cliff*, whereas a reactive policy must be trained by RL "by running off the cliff a few thousand times… Or is another cliff. It doesn't look like the previous one. I'm going to have to run off this one. This is why reinforcement learning is a complete no-no in the real world."

### Disagreement 1 — do you need planning all the way down?

Balestriero puts Bohg's hierarchy (fast reactive policies at the bottom) against LeCun's (JEPA and planning at every level). Bohg's reply is worth quoting:

> *"I don't know where this weird bias against policies comes from. I'm very confused about this. First of all, I identify as a roboticist… I want to have the robot have certain manipulation but also cognitive capabilities, and I'm fine to try whatever is out there that actually works."*

She concedes the world model's distinctive value is *"generalizing to new actions through exploration and planning in imagination"* — but insists policies are needed for speed, citing her own 1 kHz control results, and points at [world action models](../concepts/world-models/world-action-model.md) as a hybrid.

### Disagreement 2 — represent the belief, or discard what you can't predict?

Hafner reports a **negative empirical result** rarely stated this plainly:

> *"I tried this maybe five years ago, really hard, to have a representation that contains the entire belief of states you could be in. It just worked so much better empirically to have a probabilistic model you can sample from… you're better off just sampling your way through it."*

LeCun disagrees directly: *"the best way to handle uncertainty is to just eliminate the information you can't predict — that's the main argument of JEPA."* He allows that options must sometimes be kept open (the fork-in-the-road / car-ahead example), then argues humans are the wrong model for this: *"representing distributions is something humans are absolutely terrible at… The second thing we are absolutely terrible at is tree search. The best proof is that you can go to a toy store and buy a $30 gadget that will beat you at chess."*

> [!note] The workshop argues about Blackwell's object without invoking Blackwell's result
> The opening keynote is about **Blackwell's world-models theorem**. The closing panel argues over whether to represent the full belief state or discard unpredictable information — and the belief state **is** Blackwell's mixed state. [Blackwell 1957](jurgens-crutchfield-hmp-entropy-rate.md) says the sufficient statistic for a nonunifilar hidden Markov process is **generically infinite-dimensional**, which is a theoretical explanation for exactly the failure Hafner reports empirically, and a principled argument for LeCun's discard-what-you-can't-predict position. Nobody in the transcript connects the two. See [belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md).

## Programme correction (added 2026-09-02)

While ingesting [Day 2](chicago-booth-world-modeling-workshop-2026-day2.md), the workshop's own schedule page was captured to `raw/2026-09-02-wm-booth-org-programme.html` (from `wm-booth.org`, while the site was still live). It is the **primary for the programme**, and it fixes several things this page inferred from a machine transcript:

- **Opening remarks** were by **Mike Minnis**, Deputy Dean for Faculty at Booth (this page had "Booth deputy dean for faculty"), with Balestriero.
- **Donoho's keynote** is titled *"Blackwell's World Models"*, and **XY Han (Booth) and Vardan Papyan (U Toronto) are co-authors with Andrew Donoho**, not merely thanked. The abstract also credits **James Crutchfield's "computational mechanics"** and the **Astera Institute** belief-state-hunting program (Shai, Marzen, Riechers) as the bridge from Blackwell to transformers — the connection this page's closing callout says nobody made *is* made, in the keynote abstract, just not on the panel.
- **The lightning talks** were: *LpWM* (Yilun Kuang, NYU), *Selection-Induced Optimism in LLM Social World Models* (Ryan Wu, Duke), *CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization* (Tewodros W. Ayalew, University of Chicago), and *Latent Flow Waypoints for Latent Planning* (Ryan Teehan, NYU). This page had recorded only two of the four.
- **The panel** was Bohg, Du, Hafner and LeCun — four, not "LeCun, Bohg, Hafner and others."
- **Grover's keynote** names the work this page could not trace: **LaViDa**, a line on diffusion language models extended across modalities.
- **Bohg's abstract** names her three works explicitly — SimToolReal, **Play2Perfect**, and **MessyNav** ("decides which obstacles in a cluttered scene can be moved and where they will end up"), plus Causal-PIK. MessyNav is on the wiki's [backlog](../backlog.md) as announced-but-unpublished; this is independent confirmation of its content.

> [!warning] Blackwell 1956 or 1957?
> The keynote abstract says *"Blackwell's little-known **1956** result about hidden Markov models."* This wiki cites **Blackwell 1957** (*Transactions of the First Prague Conference*), including on [belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md). Almost certainly the same paper under conference year vs. proceedings year — the Prague conference was held in 1956 and the proceedings published in 1957 — but the wiki asserts a date it has never been able to verify against the document itself, which is not digitized.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) — organizer and moderator. [Yann LeCun](../entities/yann-lecun.md), [Jeannette Bohg](../entities/jeannette-bohg.md), [Danijar Hafner](../entities/danijar-hafner.md) ([Dreamer](../entities/dreamer.md)).
- **Dave Donoho** (Stanford Statistics), **Aditya Grover** (UCLA; co-founder of **Inception**, a diffusion-LLM company), **Yilun Du** (Harvard) — no wiki pages.
- **David Blackwell** — subject of the opening keynote. **Abe Girshick**, **XY Han** (Booth junior faculty), **Vardan Papyan** — thanked.
- **Chicago Booth CAAI** — host; no wiki page. [DGX Spark](../entities/dgx-spark.md) — Donoho's experimental platform.

## Concepts touched

- [Belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md) — the panel's central disagreement.
- [World model](../concepts/world-models/world-model.md), [JEPA](../concepts/world-models/jepa.md), [world action model](../concepts/world-models/world-action-model.md), [imitation learning](../concepts/learning/imitation-learning.md), [VLA models](../concepts/learning/vla-models.md).

## Open questions

- **Is "train on failures" actually being done anywhere?** Bohg's counterfactual argument is the strongest case in this wiki for collecting unsuccessful robot data, and it converges with [SimToolReal](simtoolreal-paper.md)'s and [Vafa et al.'s](vafa-world-model-implicit.md) coverage-beats-realism findings from two other directions. No ingested source builds a dataset this way.
- **Hafner's negative result deserves a citation.** "I tried representing the full belief and sampling worked better" is, as far as this wiki knows, unpublished. If it is in a Dreamer paper, the wiki should find it; if not, it is folklore doing load-bearing work.
- ~~**Day 2 exists and is not ingested.**~~ **Resolved 2026-09-02** — auto-captions appeared on the VOD as predicted, and Day 2 is [ingested](chicago-booth-world-modeling-workshop-2026-day2.md) (8h05m; the finance/economics day). **Day 3** (`PkaYC3fwEsc`, the hands-on coding day) is [ingested 2026-09-03](chicago-booth-world-modeling-workshop-2026-day3.md). **All three days are now in the wiki.**
- **Day 1 now has YouTube auto-captions**, which did not exist when this page was made (hence the local Whisper pass). Worth a comparison if the proper-noun garbling this page warns about ever becomes load-bearing — though machine ASR garbles names either way, so this is a cheap re-check, not a fix. **The cheaper fix has now been applied to Day 2 instead**: reconcile the speaker list against the event's own programme rather than against a better transcript. See the Programme correction below.
- Aditya Grover's **complementary unmasking** (02:14) and caching scheme (02:22) are named but not traced to a paper here.
