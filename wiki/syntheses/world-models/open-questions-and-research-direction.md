---
title: "Ten open questions, and the one the wiki is pointed at"
type: synthesis
created: 2026-09-10
updated: 2026-09-11
tags: [research-direction, open-questions, world-model, representation, latent-variable, cross-embodiment, continual-learning, evaluation, semantic-safety, synthesis, meta]
---

# Ten open questions, and the one the wiki is pointed at

This page is the wiki's own version of a document its author produced with ChatGPT, [Robot Research Direction](../../sources/robot-research-direction-notes.md), which ranked the wiki's open problems and proposed a single focused question. The document paraphrased the wiki accurately; what it could not do, being a paraphrase, is **cite the primaries or say which experiments are already designed**. This page does both, and then argues with the ranking.

## The question

> **What information does a robot world model need to preserve, and how can we tell whether it learned the right representation before putting it on a robot?**

Two halves. The first is a *design* question about what a latent should keep — the subject of [the abstraction tax](abstraction-tax.md) and the [GLP-vs-JEPA dispute](../../sources/critique-of-world-model-paper.md). The second is a *measurement* question, and it is the one the wiki is better equipped for than it was a month ago: [representation evaluation](../../concepts/learning/representation-evaluation.md) supplies the label-free and probing protocols, [identifiability](../../concepts/world-models/identifiability.md) supplies the theory of when a latent recovers the true factors, and the [declared-axis experiment](declared-axis-experiment.md) supplies four readouts ranked by signal quality.

The document's argument for why this question and not another: it is narrow enough to run experiments against, deep enough that an answer changes how every downstream component is built, and — unlike "solve general-purpose robotics" — reachable with an independent researcher's hardware and compute.

> [!note] A vendor's implicit answer (added 2026-09-11)
> [Unitree](../../entities/unitree.md)'s [UnifoLM-WLA-1.0](../../entities/unifolm.md) replaced its previous generation's video-generating world model with a **VQ-tokenized optical-flow mask of the future dynamic region**, predicted inside the VLM next to the action tokens ([source](../../sources/unifolm-wla-1-project-page.md)). That is one concrete answer to *what must be preserved* — the moving region — chosen by target design rather than by probing a latent. No ablation on the page tests it, which is exactly the gap the focused question names; see the [world-action model](../../concepts/world-models/world-action-model.md) note.

## The ten, routed to their evidence

| # | Question | Strongest evidence in the wiki | Experiment on file | Reachable here? |
|---|---|---|---|---|
| 1 | **What should the representation preserve?** | [Joint-Embedding vs Reconstruction](../../sources/joint-embedding-vs-reconstruction-paper.md): reconstruction degrades 2.4× as much under high-magnitude nuisance; [stable-worldmodel](../../sources/stable-worldmodel-paper.md): LeWM 50.8% → 6–26% under colour shift; [LeVJEPA](../../sources/levjepa-paper.md): the complementary axis | [Declared-axis experiment](declared-axis-experiment.md), Stage 0 = linear-probe a released checkpoint for agent colour, **hours, no GPU**; the λ-sweep GLP-vs-JEPA experiment in the [backlog](../../backlog.md) | **Yes** |
| 2 | **Long-horizon hierarchical planning** | [HWM](../../sources/hwm-paper.md): real Franka pick-and-place **0% → 70%** from a single goal image, no oracle subgoals; [LeCun](../../sources/ai-house-davos-2026-lecun-embodied-ai.md): "completely unsolved… people have mostly given up" | None filed. HWM's own gap: language-conditioned rather than goal-image-conditioned subgoals | Partly — HWM's Push-T and maze variants run on one GPU |
| 3 | **Continual learning without forgetting** | [ASPIRE](../../sources/aspire-paper.md): a skill library that compounds, 14% → 62%; [Hassabis](../../sources/wef-davos-2026-the-day-after-agi.md): world models and continual learning as what "will need to be" solved | None. **No concept page exists** — see gaps below | Unclear until the wiki organizes what it has |
| 4 | **Generalize rather than memorize** | [LIBERO-PRO](../../sources/libero-pro-paper.md): >90% → **0.0%** under perturbation; [π0.5](../../entities/pi-zero-5.md): scene generalization bought, instruction generalization not; [S1](../../sources/skild-s1-blog.md): 43 vs 53% in-distribution inverts to 66 vs 9% on unseen tasks | The declared-axis experiment is the controlled form of this question | **Yes** (same experiment as #1) |
| 5 | **Uncertainty and multiple futures** | The [Dawid & LeCun blueprint](../../sources/dawid-lecun-lvebm-lecture-notes.md) prescribes a latent `z` for exactly this; **no JEPA in the wiki implements it** ([JEPA](../../concepts/world-models/jepa.md)); [Balestriero](../../sources/information-bottleneck-ep11-jepa-balestriero.md) on why rich actions make it unnecessary — the wiki's reading that actions are doing `z`'s job ([world-action model](../../concepts/world-models/world-action-model.md)) | [Backlog](../../backlog.md): build a JEPA that has `z`, compare on weak-action settings; read [identifiability of controlled world models](https://arxiv.org/abs/2607.22430) first | **Yes** — any existing latent world model is the testbed |
| 6 | **The sensing mixture** | [τ](../../sources/tau-touch-augmented-vla-paper.md): same π0.5 backbone, tactile added, plug insertion **20% → 60%**, four-task average **28.75% → 71.25%**, ablation returns to baseline | [Backlog](../../backlog.md): τ's future-visual-supervision trick on a **6-axis wrist F/T sensor** instead of a GelSight-class sensor | Needs a tactile or F/T sensor and a π0.5 fine-tuning budget; the *force-vs-vision* debate with [FLUX-mimic](../../sources/flux-3-launch.md) is blocked on evidence only the vendors hold |
| 7 | **Evaluation without millions of trials** | [RoboLab](../../sources/nvidia-robolab-evaluation-blog.md): ±2 pp needs ~1,030 rollouts, typical papers run ~70 ([audit](../platforms/vla-success-rate-audit.md)); [WorldArena](../../sources/worldarena-paper.md): both learned evaluators score policies **higher than the simulator's own verdict** | The wiki's standing discipline — record N and compute at ingest — is a policy, not an experiment | Yes as method; no as a research result |
| 8 | **Physical commonsense from non-robot data** | Robot corpora **hundreds to low thousands of hours** ([crowdsourced data](../../concepts/learning/crowdsourced-robot-training-data.md)); [EgoScale](../../sources/egoscale-paper.md): 1k–20k hours of human video, **no saturation**, authors decline to extrapolate; [Go-Big](../../sources/figure-project-go-big.md): the wiki's only human-video-only transfer | None filed | No — the interesting regime starts at thousands of hours |
| 9 | **Semantic safety** | [GR 2 safety report](../../sources/gemini-robotics-2-safety-report.md): the vendor states the enforcement layer is out of scope; the layer is **measured, sometimes predicted, not enforced** ([semantic safety](../../concepts/safety/semantic-safety.md)); the physical half *is* enforced ([safety filters](../../concepts/robotics/safety-filters.md)) | None filed; the [guardrails thread](../agents/guardrails-for-robot-agents.md) sketches the interlock | Architecture work is reachable; benchmarks are single-lab |
| 10 | **Transfer across radically different bodies** | [Demo-JEPA](../../sources/demo-jepa-paper.md): V-JEPA 2.1 latents stay embodiment-specific — an explicit transform is needed even between 6–7 DoF parallel-gripper arms | The **"which robot is this?" linear probe** on V-JEPA 2.1 latents (Demo-JEPA's own open question) | **Yes** — a probe on released latents, no training |

## The three the document picks, and why they are the same experiment twice

The document selects #1, #5 and #10 as reachable. Read against the table, #1 and #10 are **the same measurement on different checkpoints**: a linear probe asking whether a nuisance factor (agent colour; robot identity) is decodable from a latent that was supposed to abstract it away. Stage 0 of the declared-axis experiment and the Demo-JEPA probe share code, share the [representation-evaluation](../../concepts/learning/representation-evaluation.md) protocol, and share a failure mode — a probe that finds the factor says the latent *kept* it, not that the planner *uses* it. The [backlog](../../backlog.md) already ranks Stage 0 as the highest-value-per-hour item in the wiki; the embodiment probe should be run in the same session, because the second checkpoint costs almost nothing once the first is set up.

#5 is different in kind. It is not a probe but a **build**: give a JEPA the latent `z` its blueprint prescribes, and find the boundary of the action-conditioned architecture by removing or weakening actions. It is the only one of the three that could produce a result no paper has, and it depends on #1 — a `z` that captures "the many futures compatible with one past" only helps if the representation it sits on kept the information that distinguishes those futures.

## Arguing with the ranking

The document orders by how "fundamental" each question seems, without saying what that means. A usable criterion is **dependency**: which question, answered, changes the answer to the most others.

- **#7 (evaluation) belongs at the top, not seventh.** Every number in the other nine rows was produced under the rollout regime the audit indicts, and the WorldArena result says the cheap alternative is biased in a known direction. Until evaluation is trustworthy, "answered" is not a state any of the others can reach. The wiki's own rule — treat every LIBERO number as provisional — is this ranking already applied.
- **#1 stays at the top** for the reason the document gives: representation is upstream of prediction, planning, uncertainty and transfer.
- **#6 (sensing mixture) is a partial answer, not an open question.** τ measured it. What remains open is the *cheap substitute* question, which is narrower and engineering-shaped.
- **#3 (continual learning) is the least-explored in the wiki and possibly the most important for the household setting** the wiki is oriented to — the *deploy → experience → learn → retain* loop is the difference between a robot that works in a demo and one that still works in a home after a month. Its low rank in the wiki's material reflects the wiki's reading history, not the problem's weight.

## Addendum (2026-09-11): what the navigation-line and BitRobot ingests change

A day's ingests — [HIW-500](../../sources/bitrobot-hiw-500-dataset-page.md), the [BitRobot whitepaper](../../sources/bitrobot-network-whitepaper.md), the [Earth Rover Challenge](../../sources/earth-rover-challenge-frodobots-2k.md), and the complete Berkeley RAIL navigation line ([GNM](../../sources/gnm-paper.md) → [ViNT](../../sources/vint-paper.md) → [NoMaD](../../sources/nomad-paper.md) → [MBRA](../../sources/mbra-paper.md) → [OmniVLA](../../sources/omnivla-paper.md)) — touch four of the ten rows. None closes a question; two move a cell in the table.

- **#7 Evaluation gains an instrument, not a fix.** The row says the wiki's answer is a policy, not an experiment. There is now an external instrument: the Earth Rover Challenge runs a **calibrated multi-city fleet** that scores a policy as a fraction of the best human teleoperator's run, with 20 h/week of pre-event access for any team, and the BitRobot whitepaper names *evaluation fleets for hire* as its economic loop 1. The navigation papers add four partial-credit metrics — mean progress, maximum displacement without intervention, SPL, coverage rate — now on the [policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) page. Two limits: it is sidewalk navigation with four discrete actions at ~500 ms latency, and the navigation papers' own cells are 8–24 trials, so the [audit](../platforms/vla-success-rate-audit.md)'s sample-size indictment is untouched. The ranking argument above (#7 to the top) now has a concrete mechanism to point at.
- **#8 "Reachable here?" flips from No to Yes — for navigation.** OmniVLA trains on **8,680 h of car dashcam video** and MBRA on 100 h of YouTube walking tours, both with actions synthesized by a model-based relabeler, and both report measured gains (BDD-V halves failures; YouTube-trained 0.875 vs 0.500). The mechanism — a differentiable unicycle plus monocular-depth collision proxy — runs on one GPU. The manipulation analogue is exactly the open part: the authors say no obvious robot model exists for it. The row's "hundreds to low thousands of hours" of robot data also moves: HIW-500 is 500+ h of humanoid whole-body teleop under CC BY.
- **#10 sharpens.** [Demo-JEPA](../../sources/demo-jepa-paper.md)'s embodiment-specific latents are a *manipulation* result. Navigation transfers wheeled → quadruped ([Go1](../../entities/unitree-go1.md)) → quadrotor with zero robot-specific data because GNM's **normalized-waypoint action space** is shared across bodies. The open question is therefore not "transfer across radically different bodies" but **"transfer where no shared low-dimensional action abstraction exists"** — which is manipulation, and which is why [latent action tokens](../../concepts/learning/latent-action-tokens.md) exist. The missing cross-embodiment concept page (gaps below) now has five more primaries to build from.
- **#5 gets a robot-scale datapoint for the "actions are doing `z`'s job" reading.** NoMaD models the multiple futures at a junction in the **action** head (diffusion), with no latent world variable, and the point-estimate policy in the same table collapses to the mean and collides (50% / 1.0 collisions vs 98% / 0.2). This supports Balestriero's argument above; it says nothing about the weak-action regime the backlog experiment targets, because NoMaD is rich-action by construction.

Two smaller notes. On **#1**, MBRA is a data-side datapoint about what can be *discarded*: the crowdsourced action stream was worth zero and the observations carried everything — a representation question asked of a dataset rather than a latent. On **#2**, the navigation line reached kilometer-scale horizons with an **explicit topological memory plus a short-horizon policy**, not with subgoals in a latent; it is the standing alternative to [HWM](../../sources/hwm-paper.md)'s mechanism and should be named as such when #2 is next revisited.

## The loop as a map of the wiki

The document's reduction — in the wiki's rewording, *perceive → represent → predict → plan, under semantic constraints → act, through a physical safety filter → observe consequences → learn* — doubles as a coverage map. The [source page](../../sources/robot-research-direction-notes.md) tabulates which pages carry each stage. One stage and one veto point are thin: **learn** (no continual-learning page; the wiki's learning material is almost entirely *pre-deployment*) and the **semantic constraint on plans** (measured by benchmarks, enforced nowhere in the wiki — the physical filter on actions *is* enforced). Those are the two that make a robot *durable*, which is consistent with the document's closing worry: the field has gotten good at individual pieces while the closed loop remains open.

> [!note] Why the wiki reworded the document's loop (resolved 2026-09-11)
> The document ends its loop with a stage called *"stay safe."* Two things are wrong with it. It reads as the robot's self-preservation, when the object of safety is people, property and the task. And it makes safety a *stage* — something learned end-to-end like the rest — whereas the [safety-filter](../../concepts/robotics/safety-filters.md) literature and the [GR 2 report](../../sources/gemini-robotics-2-safety-report.md)'s own language treat safety as a **deterministic wrapper with veto authority**, kept outside the learned system. The wiki's material also shows *where* the vetoes sit, and it is two places, not one: [semantic safety](../../concepts/safety/semantic-safety.md) (ASIMOV, the constitution) is a constraint on **plans** — "not the knife into the child's hand" is decided before any motor command — and [safety filters](../../concepts/robotics/safety-filters.md) (CBFs, reachability) are a constraint on **actions**, emitting the nearest certifiable action to the one the policy proposed. Hence *plan, under semantic constraints → act, through a physical safety filter*: safety is not a stage, it is two veto points, one on plans and one on actions, and the second is the only one the wiki has seen enforced.

## Gaps this page exposes

Two concepts the ten questions depend on have no page:

- **Continual learning / catastrophic forgetting** — mentioned on eight pages, organized nowhere. Needed for #3.
- **Cross-embodiment** — the phrase appears on over a hundred pages; the only titled page is the narrow [soft-prompt method](../../concepts/learning/soft-prompt-cross-embodiment.md). Needed for #10, and the [Demo-JEPA](../../sources/demo-jepa-paper.md) finding that "cross-embodiment" in practice means three similar arms is exactly the kind of claim a concept page should hold.

Both are filed in the [backlog](../../backlog.md).

## Related

- [The abstraction tax](abstraction-tax.md) — the narrowed claim behind #1 and #4
- [The declared-axis experiment](declared-axis-experiment.md) — the experiment behind #1, #4 and #10
- [JEPA for a household mobile manipulator](jepa-for-household-mobile-manipulator.md) — the decision page this direction serves
- [What world models are measurably good for](what-world-models-are-measurably-good-for.md) — the four-role verdict that #7 rests on
- [Success-rate audit](../platforms/vla-success-rate-audit.md) — the rollout arithmetic
- [Representation evaluation](../../concepts/learning/representation-evaluation.md) — the protocols for the measurement half of the question
- [Identifiability](../../concepts/world-models/identifiability.md) — the theory for the measurement half

## Sources used in this synthesis

- [Robot Research Direction (first-party notes)](../../sources/robot-research-direction-notes.md) — the ranking and the focused question
- [HWM paper](../../sources/hwm-paper.md) · [AI House Davos 2026](../../sources/ai-house-davos-2026-lecun-embodied-ai.md) · [Davos 2026 — the day after AGI](../../sources/wef-davos-2026-the-day-after-agi.md)
- [ASPIRE](../../sources/aspire-paper.md) · [LIBERO-PRO](../../sources/libero-pro-paper.md) · [Skild S1](../../sources/skild-s1-blog.md) · [Joint-Embedding vs Reconstruction](../../sources/joint-embedding-vs-reconstruction-paper.md) · [stable-worldmodel](../../sources/stable-worldmodel-paper.md) · [LeVJEPA](../../sources/levjepa-paper.md)
- [Dawid & LeCun lecture notes](../../sources/dawid-lecun-lvebm-lecture-notes.md) · [Balestriero, Information Bottleneck EP11](../../sources/information-bottleneck-ep11-jepa-balestriero.md) · [Critique of World Model](../../sources/critique-of-world-model-paper.md)
- [τ](../../sources/tau-touch-augmented-vla-paper.md) · [FLUX 3 / FLUX-mimic](../../sources/flux-3-launch.md)
- [RoboLab methodology](../../sources/nvidia-robolab-evaluation-blog.md) · [WorldArena](../../sources/worldarena-paper.md)
- [EgoScale](../../sources/egoscale-paper.md) · [Project Go-Big](../../sources/figure-project-go-big.md)
- [Gemini Robotics 2 safety report](../../sources/gemini-robotics-2-safety-report.md) · [Demo-JEPA](../../sources/demo-jepa-paper.md)
