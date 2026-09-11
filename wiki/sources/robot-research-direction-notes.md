---
title: "Robot Research Direction — notes on the wiki's open questions (first-party, with ChatGPT)"
type: source
url: none (local document)
author: Tanio Klyce with ChatGPT (first-party notes)
published: 2026-09-10
ingested: 2026-09-10
local_path: raw/Robot Research Direction.pdf
sha256: c32fb18236ebd077b0ca019d1069bca8a265189f58ea09c75f869af0ddf22fba
format: Google Docs PDF export, 4 pp.
tags: [first-party, research-direction, open-questions, world-model, representation, latent-variable, cross-embodiment, continual-learning, semantic-safety, evaluation, meta, chatgpt]
---

# Robot Research Direction — notes on the wiki's open questions

> [!note] What kind of source this is
> A **reading of this wiki, not a source about the world.** The document was produced by the wiki's author in conversation with ChatGPT, given the wiki as material, and asked what is actually preventing general-purpose physical intelligence. Every factual claim in it is a claim *about what the wiki already says*, so the ingest work here was verification: each of the ten questions was traced back to the pages it paraphrases, and the result is recorded below. No new evidence about robots enters the wiki through this page. What enters is a **ranking** and a **focused question**, both of which are judgments. The document carries no date of its own; `published` is the file date.

## Summary

The notes rank the wiki's open problems by how fundamental they are to a useful general-purpose robot, and find that the ten do not stay separate. They collapse into one loop — *perceive → represent → predict → plan → act → observe consequences → learn → stay safe* — that the field has solved piecewise and not closed. The dividing line that matters, the document argues, is no longer VLA vs JEPA vs generative world model. It is whether a robot can **build a compact internal model of the world that keeps the right information, predict how its actions change that world, notice when the prediction is wrong, and update without destroying what it already knows**. If that is solved, action heads become an implementation detail; if it is not, scaling behaviour cloning yields better demonstrations without robust physical intelligence.

From the ten it picks three as experimentally reachable without a large lab — **representation** (#1), **uncertainty and the missing latent variable** (#5), and **embodiment invariance** (#10) — notes that the wiki's [backlog](../backlog.md) already holds an experiment for each, and proposes the sharpened direction:

> *What information does a robot world model need to preserve, and how can we tell whether it learned the right representation before putting it on a robot?*

The wiki's own verified, cross-linked version of the ten, with each routed to its primaries and filed experiments, is [Ten open questions, and the one the wiki is pointed at](../syntheses/world-models/open-questions-and-research-direction.md).

## Key claims — the ten questions, verified against the wiki

Each row gives the document's question, what it says the wiki holds, and whether that survived a check against the actual pages. The document paraphrases the wiki accurately throughout; the nuances column is where the paraphrase is looser than the page.

| # | Question | What the document attributes to the wiki | Verified against | Nuance |
|---|---|---|---|---|
| 1 | What representation should a world model learn? | JEPA discards, reconstruction keeps; the "abstraction tax" says the discard decision can silently destroy what is needed under shift; the GLP-vs-JEPA experiment is a laboratory version | [The abstraction tax](../syntheses/world-models/abstraction-tax.md), [Critique of World Model](critique-of-world-model-paper.md), [backlog](../backlog.md) §2026-09-07b | ✔ — the abstraction-tax page's own narrowed claim is stricter than "may destroy information": the abstraction buys robustness **only along the declared axis** |
| 2 | Long-horizon hierarchical planning | LeCun calls it "completely unsolved"; HWM reports 0→70% on a real Franka | [AI House Davos 2026](ai-house-davos-2026-lecun-embodied-ai.md), [HWM paper](hwm-paper.md) | ✔ — the 0→70% is pick-and-place from a **single final-goal image with no oracle subgoals**; with oracle subgoals flat and hierarchical both reach 80%, so the gain is subgoal *discovery* |
| 3 | Continual learning without forgetting | The wiki connects this to continual learning, skill libraries, ASPIRE, adaptation; Hassabis names it independently | [ASPIRE](aspire-paper.md), [Davos 2026 — the day after AGI](wef-davos-2026-the-day-after-agi.md) | ⚠ **Thinnest of the ten in the wiki.** "Continual learning" appears on eight pages and "catastrophic forgetting" on three, and there is **no concept page** for either. The document's "already connects" overstates how organized the coverage is |
| 4 | Generalize, not memorize | >90% on LIBERO collapses to 0% under LIBERO-PRO; π0.5 got scene but not instruction generalization; declared axes | [LIBERO-PRO](libero-pro-paper.md), [π0.5 entity](../entities/pi-zero-5.md), [declared-axis experiment](../syntheses/world-models/declared-axis-experiment.md) | ✔ verbatim |
| 5 | Uncertainty and multiple futures | "Actions are doing the latent variable's job"; the JEPA/EBM blueprint has a latent `z` that no studied JEPA implements | [World-action model](../concepts/world-models/world-action-model.md), [JEPA](../concepts/world-models/jepa.md), [Dawid & LeCun notes](dawid-lecun-lvebm-lecture-notes.md), [Balestriero EP11](information-bottleneck-ep11-jepa-balestriero.md) | ✔ — and the document is right that this is the wiki's **own reading**, stated by no source; the backlog flags it as one of two originated claims |
| 6 | The sensing mixture | τ: tactile on the same π0.5 backbone, plug insertion 20%→60%, four-task average 28.75%→71.25%; ablating touch returns to baseline; wrist F/T as the cheap substitute is a proposed experiment | [τ paper](tau-touch-augmented-vla-paper.md), [tactile sensing](../concepts/robotics/tactile-sensing.md), [backlog](../backlog.md) (F/T item) | ✔ numbers exact. The backlog separately marks the τ→[FLUX-mimic](flux-3-launch.md) *force-vs-vision* thread **blocked** pending new evidence; the F/T experiment is a different, runnable item, and the document conflates neither |
| 7 | Evaluation without millions of trials | ±2 pp needs ~1,030–2,450 rollouts, papers run ~70; a learned evaluator that shares the policy's simulator can flatter it | [RoboLab methodology](nvidia-robolab-evaluation-blog.md) via the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md); [WorldArena](worldarena-paper.md) via [world-model evaluation](../concepts/world-models/world-model-evaluation.md) | ✔ — the flattery is **measured**, not hypothetical: both world-model evaluators scored policies consistently higher than the simulator's own verdict |
| 8 | Physical commonsense from non-robot data | Robot corpora hundreds to low thousands of hours; egocentric human video tens of thousands; curves not saturated | [Crowdsourced robot data](../concepts/learning/crowdsourced-robot-training-data.md), [EgoScale](egoscale-paper.md) via [EgoDex](../entities/egodex.md) and [scaling laws](../concepts/learning/scaling-laws-vla.md) | ✔ — the un-saturated curve is EgoScale's **1k–20k hours of human video**, and the authors decline to extrapolate |
| 9 | Semantic safety | The wiki's conclusion: "measured, sometimes predicted, not enforced" | [Semantic safety](../concepts/safety/semantic-safety.md), [GR 2 safety report](gemini-robotics-2-safety-report.md) | ✔ — and now **stronger than the document says**: since 2026-09-07 the page records that the vendor's own safety report states the enforcement layer is out of scope, so the conclusion is documented, not inferred |
| 10 | Transfer across radically different bodies | V-JEPA 2.1 latents stay embodiment-specific; "cross-embodiment" in Demo-JEPA is similar 6–7 DoF parallel-gripper arms; the "which robot is this?" probe | [Demo-JEPA](demo-jepa-paper.md) | ✔ verbatim — the probe is the Demo-JEPA page's own open question |

## The convergence claim

The document's contribution beyond the ranking is the argument that the ten reduce to one closed loop, and that the loop rather than any architecture is the dividing line. Read against the wiki, the stages map as follows, which is also where the wiki is thick and thin:

| Stage | Where the wiki carries it | Density |
|---|---|---|
| Perceive / Represent | [JEPA](../concepts/world-models/jepa.md), [world model](../concepts/world-models/world-model.md), [representation evaluation](../concepts/learning/representation-evaluation.md), [identifiability](../concepts/world-models/identifiability.md) | thick |
| Predict | [world-action model](../concepts/world-models/world-action-model.md), [generative latent prediction](../concepts/world-models/generative-latent-prediction.md) | thick |
| Plan | [HWM](../entities/hwm.md), [gradient-based planning](../concepts/world-models/gradient-based-planning.md), [task and motion planning](../concepts/robotics/task-and-motion-planning.md) | medium |
| Act | [VLA models](../concepts/learning/vla-models.md) — the wiki's most-cited page | thick |
| Observe consequences | [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md), [world-model evaluation](../concepts/world-models/world-model-evaluation.md), [runtime failure detection](../concepts/robotics/runtime-failure-detection.md) | medium |
| Learn | [real-world robot RL](../concepts/learning/real-world-robot-rl.md), [in-context robot learning](../concepts/learning/in-context-robot-learning.md), [test-time adaptation](../concepts/learning/test-time-adaptation.md); **no continual-learning page** | thin |
| "Stay safe" — the wiki reads this as two veto points, on plans and on actions (see below) | [semantic safety](../concepts/safety/semantic-safety.md) (constraint on plans), [safety filters](../concepts/robotics/safety-filters.md) and [safety certificates](../concepts/robotics/safety-certificates.md) (constraint on actions) | medium; enforcement exists only for the action-side filter |

## Where the document and the wiki differ

- **Ownership of claims.** The document says "your wiki notes" for findings that belong to specific papers (LIBERO-PRO's collapse, τ's ablation, RoboLab's rollout arithmetic, WorldArena's evaluator bias). The wiki's convention is to cite the primary; the synthesis page does that routing. Two claims *are* the wiki's own and are labelled as such where they appear: the declared-axis mechanism and "actions are doing `z`'s job".
- **Question 3 is under-built.** The document treats continual learning as covered. It is mentioned, not organized. Filed to the backlog.
- **Question 10's vocabulary has no home.** "Cross-embodiment" appears on over a hundred wiki pages and has no concept page; the only page with it in the title is the narrow [soft-prompt method](../concepts/learning/soft-prompt-cross-embodiment.md). Filed to the backlog.
- **The ranking is unargued.** Ten questions are ordered "by how fundamental they seem"; the document gives no criterion beyond that phrase. The three chosen for independent work are chosen by *accessibility*, which is a different axis, and the document is explicit about that.

## Entities mentioned

- [HWM](../entities/hwm.md) — the 0→70% hierarchical-planning result
- [Yann LeCun](../entities/yann-lecun.md) — "completely unsolved"
- [Demis Hassabis](../entities/demis-hassabis.md) — world models and continual learning as the missing ingredients
- [π0.5](../entities/pi-zero-5.md) — scene vs instruction generalization; τ's backbone
- [V-JEPA 2](../entities/v-jepa-2.md) — the 2.1 latents Demo-JEPA finds embodiment-specific
- [LeWorldModel](../entities/leworldmodel.md) — the checkpoint Stage 0 probes
- [LIBERO](../entities/libero.md) — the benchmark LIBERO-PRO perturbs
- [WorldArena](../entities/worldarena.md) — the evaluator-bias measurement
- [EgoDex](../entities/egodex.md) — the egocentric-hours comparison
- [OpenAI](../entities/openai.md) — ChatGPT, the co-author of the document

## Concepts touched

[World model](../concepts/world-models/world-model.md) · [JEPA](../concepts/world-models/jepa.md) · [World-action model](../concepts/world-models/world-action-model.md) · [Generative latent prediction](../concepts/world-models/generative-latent-prediction.md) · [Identifiability](../concepts/world-models/identifiability.md) · [Belief states](../concepts/world-models/belief-states-and-mixed-states.md) · [Representation evaluation](../concepts/learning/representation-evaluation.md) · [World-model evaluation](../concepts/world-models/world-model-evaluation.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) · [Tactile sensing](../concepts/robotics/tactile-sensing.md) · [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) · [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) · [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) · [Semantic safety](../concepts/safety/semantic-safety.md) · [Safety filters](../concepts/robotics/safety-filters.md) · [In-context robot learning](../concepts/learning/in-context-robot-learning.md) · [VLA models](../concepts/learning/vla-models.md)

## Open questions

- **Is the ranking right?** The document orders by "fundamental" without a criterion. A defensible criterion — *which question, if answered, changes the answer to the most others* — would put #1 and #7 at the top (representation determines everything downstream; evaluation gates whether any answer can be trusted) and would demote #6 (a mixture question with a measured partial answer). Worth arguing on the synthesis page rather than here.
- **Does the closed-loop framing survive contact with the wiki's safety material?** "Stay safe" is listed as a stage of the loop, but the [safety-filter](../concepts/robotics/safety-filters.md) literature treats safety as a *wrapper* around the loop with veto authority, not a stage in it. The two framings imply different architectures. *Resolved 2026-09-11:* the wiki's own statement of the loop drops the stage and names the two veto points instead — *plan, under semantic constraints → act, through a physical safety filter* — see the [synthesis](../syntheses/world-models/open-questions-and-research-direction.md) and the [overview](../overview.md). The document's wording is preserved above because this page records what the document says.
- **What would the focused question's answer look like?** "How can we tell whether it learned the right representation" already has a partial method on file — [representation evaluation](../concepts/learning/representation-evaluation.md) and the [declared-axis readouts](../syntheses/world-models/declared-axis-experiment.md) — but no page yet says what *right* means for a robot world model beyond "planning success under a declared shift". That definition is the missing piece.
