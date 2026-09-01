---
title: World-model evaluation
type: concept
created: 2026-08-07
updated: 2026-08-31
sources: 12
tags: [world-model, evaluation, benchmark, physical-validity, policy, vbench, worldscore, physion-eval, mllm-critic]
---

**World-model evaluation** — establishing whether a learned environment is **valid for the use it is being put to**. Distinct from measuring how good its outputs look, and distinct from measuring whether a policy trained inside it scores well.

The [HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md) frames this as the third governance object, after content (what a system generates) and authority to act (what a system may do): **the validity of the learned environment itself.** Its verdict on the current state is unambiguous — evaluation "remains a research patchwork rather than a settled standard," and "none gives policymakers an adequate basis to assess a world model for safety-critical deployment."

## Two failure modes that look identical from the outside

**1. The visual plausibility trap.** A renderer produces a persuasive depiction without modeling the geometry, dynamics, or physical constraints needed for safety. AI-generated video shows fire or flowing water that doesn't obey physics; a generated building looks sound with no stable underlying structure. The system looks competent **to a human observer**.

**2. The simulation-to-reality gap.** The system performs well *inside* the generated environment and fails outside it — sensor noise, lighting, weather, wear, unexpected human behavior, edge-case physics. Here nobody is fooled by appearances; the model is simply wrong about a world it was never shown. See [sim-to-real transfer](../learning/sim-to-real-transfer.md).

**And the compound of the two, which is specific to world models: teaching to a flawed test.** When a learned model is used both to *train* a system and to *judge* it, the model's errors become invisible. The brief's example: if the model understates the risk of skidding in rain, a vehicle trained inside it learns to drive too fast — and still scores well when the same flawed model tests it. "The score would reflect an error in the model, not readiness for a real road."

> [!warning] Now measured — and the bias has a direction
> [WorldArena](../../sources/worldarena-paper.md) ran two world models as policy evaluators against the RoboTwin simulator's own verdict and found that **both "have consistently higher success rates than those measured in the simulator, suggesting partial overfitting to successful trajectories."** A learned evaluator *flatters* the policies it evaluates.
>
> What survives is **ranking**, not level: Ctrl-World correlates at **r = 0.986** with the simulator's ordering while reporting inflated absolute rates; Cosmos-Predict 2.5 manages only **r = 0.483**. So a learned evaluator can be a usable comparator and an unusable measurement at the same time.
>
> One complication before treating this as settled: [Veo](../../entities/veo.md) reports the **opposite sign** — Pearson 0.88 against 1,600+ real evaluations with absolute predicted rates running *low*. Both papers agree ranking beats level; they disagree on which way the level moves. Different substrates (RoboTwin sim vs real Gemini Robotics evaluations), so the disagreement may be about what the model was compared against rather than about the models.

## Each architecture fails differently

The brief's sharpest technical observation, and it maps cleanly onto this wiki's existing families:

| Design | Characteristic failure | Wiki page |
|---|---|---|
| Video generators **without a persistent scene representation** | Lose consistency over time; objects drift, flicker, vanish | [generative-video vs JEPA](../../syntheses/world-models/generative-video-vs-jepa-world-models.md) |
| **3D-native** systems (explicit geometry) | Spatially consistent, but "still fail to capture how a world *changes*" | [world-model simulators](world-model-simulators.md) |
| **Latent state-space** models (compressed internal representation) | Prioritize predicting change over visual detail — so visual metrics score them wrongly in both directions | [JEPA](jepa.md), [latent space](latent-space.md) |

The consequence: **each demands a different evaluation.** A single leaderboard across these families is measuring three different things.

## Evaluation should match function

Keyed to the [functional taxonomy](world-model-functional-taxonomy.md):

- **Renderer** used for concept art → judge by how convincing it looks. Plausibility *is* the product.
- **Simulator** used for infrastructure planning → higher bar: is its geometry and physics **actually correct**?
- **Planner** embedded in a robot → tested repeatedly across varied real-world conditions.
- **Interactive** systems add one more: do skills practiced in simulation, by a person or a robot, **transfer to the real task**?

The principle: *the closer a system comes to real-world actions, the more its evaluation should weigh physical validity, robustness, and transfer beyond the test setting.*

## The benchmark landscape as of mid-2026

| Benchmark | What it measures | Primary source |
|---|---|---|
| **VBench** | Visual quality, prompt alignment, temporal smoothness — explicitly **not** whether scenes obey physical law | not ingested |
| **VideoPhy** / **PhyGenBench** / **Cosmos-Eval** / **PhyWorldBench** | Physical commonsense in generated video, via automated metrics or model-based critics | not ingested |
| **[Physion-Eval](../../entities/physion-eval.md)** | Physical realism in generated video, judged by **expert human reasoning** — 10,990 traces, 0.1 s glitch localization, failure taxonomy. Also measures the *critics*: MLLMs are 2–6× less sensitive than untrained humans | **[ingested](../../sources/physion-eval-paper.md)** |
| **WorldScore** | Controllability, quality, and dynamics in world *generation* (Duan, Yu, Chen, [Fei-Fei Li](../../entities/fei-fei-li.md), Wu — arXiv 2504.00983) | not ingested |
| **WorldModelBench** | Judges video models specifically **as world models** | not ingested |
| **[WorldArena](../../entities/worldarena.md)** | Perceptual quality **plus functional utility** as data engine / policy evaluator / action planner — extended in 2.0 to visuotactile, RL environments, and real robots | **[ingested](../../sources/worldarena-paper.md)** · **[2.0](../../sources/worldarena-2-paper.md)** |
| **[WorldRoamBench](../../entities/worldroambench.md)** | **Long-horizon stability** of interactive world models: per-frame action, visual drift, interaction physics, memory | **[ingested](../../sources/worldroambench-paper.md)** |
| **[LIBERO](../../entities/libero.md)** | Simulated manipulation task completion — the robotics anchor of the list | [ingested](../../sources/libero-pro-paper.md) |
| **Myhill-Nerode compression / distinction** ([Vafa et al.](../../sources/vafa-world-model-implicit.md)) | **Internal coherence** of the world model implicit in a sequence model, against a DFA ground truth. Not perceptual, not utility — the third axis | **[ingested](../../sources/vafa-world-model-implicit.md)** |

The progression VBench → VideoPhy/PhyGenBench → WorldScore/WorldModelBench → WorldArena runs from *how it looks* toward *what it is good for*. WorldArena and WorldRoamBench sit at that far end and now have primary sources here.

> [!warning] A third axis, and it undercuts most of the column above
> Nearly every row in this table is scored **automatically or by a model judge**. [Physion-Eval](../../sources/physion-eval-paper.md) (Mar 2026) measures those judges against people and finds them badly outmatched: on Youden's J, untrained viewers score **24.9–37.1%** (exocentric) and **48.4–61.8%** (egocentric) while the best of ten MLLM critics reaches **19.1%** and **9.8%** — Gemini 3.0 Pro misses over **74.4%/90.1%** of videos containing glitches ordinary people spot at once. Neither denser temporal sampling nor enabling "thinking" helps (Δ*J* < 2.0 points), which the authors attribute to the **visual encoder**, not the reasoner: language-space reasoning cannot recover transient cues the encoder never captured.
> Two consequences. First, **the automated benchmark layer is itself unvalidated** — this is the same failure the wiki recorded on the model side (WorldArena's EWMScore correlates r = 0.360 with action planning), now found one level up. Second, the generators are worse than headline numbers suggest: **83.3% of exocentric and 93.5% of egocentric** generated clips carry at least one human-identified physical violation.

Note a small closed loop in the policy record: **WorldScore was co-authored by two of the HAI brief's own authors** (Fei-Fei Li, Jiajun Wu), and its first author Haoyi Duan appears on WorldArena 2.0. The brief presents the benchmark landscape as external evidence without noting the overlap.

### A fourth axis: sample-efficiency against a human baseline

Everything in the table above scores an **artifact** — a video, a rollout, a sequence model. The cognitive-science tradition instead scores an **agent solving a problem**, and does it against a measured human baseline on identical stimuli. See [physical reasoning benchmarks](physical-reasoning-benchmarks.md): **PHYRE** and **Virtual Tools**, scored by **AUCCESS**, which weights success toward *fewer attempts*.

Two imports worth making. First, that family separates **performance** from **human alignment** and reports both — [Causal-PIK](../../sources/causal-pik-paper.md) is simultaneously higher-scoring than humans and *less* correlated with them per-puzzle on Virtual Tools, because it solves puzzles people find hard. Robot-policy evaluation here routinely treats "matches human success rate" as if it implied similar competence structure; it does not. Second, **a score without its action space or attempt budget is uninterpretable** — humans beat Causal-PIK 36.6 to 24.8 on PHYRE once both get 10 attempts.

### The coherence axis, and the pattern all three axes converge on

[Vafa et al. (2024)](../../sources/vafa-world-model-implicit.md) supply what the rest of this table lacks: a **formal** ground truth. Where the world is a DFA, the Myhill-Nerode theorem makes "has a world model" decompose into two checkable halves — prefixes reaching the same state must admit the same continuations (**compression**), prefixes reaching different states must be separable by some suffix (**distinction**). See [belief states and mixed states](belief-states-and-mixed-states.md) for why these are the discrete cousin of a POMDP belief.

The numbers are stark. A transformer trained on NYC taxi rides scores **1.00** on next-token legality and **0.91** on a current-state probe — the field's two standard diagnostics — while scoring **0.10** on compression precision, and its reconstructed Manhattan contains streets with impossible orientations and flyovers. GPT-4 solves seating-arrangement logic puzzles at task accuracy **1.00** with compression precision **0.21**.

> [!note] One finding, three formalisms
> The wiki now has the same result from three unrelated directions, and it is worth stating once:
> - [stable-worldmodel](../../sources/stable-worldmodel-paper.md): **prediction MSE correlates poorly with planning success** — being out of distribution, not error magnitude, breaks planning.
> - [WorldArena](../../sources/worldarena-paper.md): perceptual score correlates **r = 0.360** with action planning.
> - [Vafa et al.](../../sources/vafa-world-model-implicit.md): near-perfect task performance alongside compression precision 0.10–0.21.
>
> **Whatever a model's headline competence measures, it is not the coherence of its world model.** Every axis of this table that scores outputs rather than structure inherits the problem — which is also why [Physion-Eval](../../sources/physion-eval-paper.md)'s finding that the automated *judges* are weaker than untrained humans compounds rather than duplicates it.

Vafa et al. add a second finding with direct bearing on robot data collection: across both navigation and Othello, **models trained on random or synthetic data recovered more structure than models trained on real expert data** — real traversals never cover the state space widely enough. The wiki's data-collection sources ([Mobile ALOHA](../../sources/mobile-aloha-paper.md), [DROID](../../entities/droid.md), [Figure's Index](../../entities/figure-index.md)) all collect expert demonstrations, which is structurally the regime that scored worst here.

### What the measurements actually say

Two independent labs, two task domains, one result.

**[WorldArena](../../entities/worldarena.md)** (manipulation) quantifies the gap directly. Its EWMScore — the unweighted mean of 16 video-quality metrics — correlates with:

| Against | Pearson r |
|---|---:|
| Human judgment | **0.825** |
| Data-engine utility | 0.600 |
| **Action-planning performance** | **0.360** |

**[WorldRoamBench](../../entities/worldroambench.md)** (open-world roaming) finds the same thing without measuring the same quantity: "high visual quality ≠ good action following" — the two are **"largely independent."** It adds that **trajectory-level action scores above 85 can hide below-65% per-frame accuracy**, so even the *action* metric everyone reports was measuring the wrong thing.

Concrete performance, from WorldArena:

- **As a data engine** — no world model matches real demonstration data (best: WoW 45%/71% vs real 77%/66%), and the gap *widens* from simulation to a real robot.
- **As an action planner** — every world model loses to a [π0.5](../../entities/pi-zero-5.md) policy by **3–4×** (best 20%/21% vs 77%/66%).
- **As an RL environment** — this one works. Policies trained inside a learned world model close roughly two-thirds of the gap to simulator-based RL and beat SFT across the board ([WorldArena 2.0](../../sources/worldarena-2-paper.md)).

> [!note] The role distinction is the finding
> Learned dynamics are good enough to **shape** a policy and not good enough to **be** one. Neither paper states it this way, and it is the most decision-relevant thing in the cluster — see [what world models are measurably good for](../../syntheses/world-models/what-world-models-are-measurably-good-for.md).

The brief's summary judgment holds: "leading models still fail to maintain basic physical consistency, and high benchmark scores can conceal weaknesses in physical reasoning or robustness to changing conditions."

### A tension the metrics create

WorldRoamBench: **stricter physics adherence may compromise action following.** A model that refuses to clip through a wall must deviate from the keystroke-prescribed trajectory — so correct behavior is scored as error, and an aggregate that averages action and physics penalizes it twice. Nobody has proposed the right scoring rule. Worth remembering whenever a world-model leaderboard reports a single number.

## The wiki's own instrument agrees, from the policy side's blind spot

[Robot policy evaluation](../robotics/robot-policy-evaluation.md) reaches the same verdict about *policies* that the brief reaches about *world models*, with numbers the brief doesn't have: **±2 pp confidence requires ≈1,030 rollouts against the ~70 typically run**; scores saturate above 90%; and [LIBERO-PRO](../../sources/libero-pro-paper.md) drops >90% policies to **0.0%** under perturbations that preserve the task. That last result is the empirical form of the brief's "high benchmark scores can conceal weaknesses."

So the two literatures converge and neither cites the other. The policy brief says no benchmark supports safety-critical deployment decisions; the robotics measurement literature says the benchmarks in use don't even support ranking two policies against each other.

## The two literatures cannot score each other

The deepest problem with world-model evaluation as of mid-2026 isn't that instruments are missing. It's that the instruments in use are **incommensurable** — each runs on one family and cannot run on the other.

| Instrument | Scores | Runs on |
|---|---|---|
| [WorldArena](../../entities/worldarena.md) / [WorldRoamBench](../../entities/worldroambench.md) | Video quality, functional utility, long-horizon stability | Pixel predictors only |
| [stable-worldmodel](../../sources/stable-worldmodel-paper.md), [JEPA-WMs](../../sources/jepa-wms-paper.md) | Planning success under controlled variation | Latent predictors only |
| [Action-relevant latents](../../sources/action-relevant-latents-paper.md) | Inverse-dynamics probe R² | **Both** |
| [Latent video prediction](../../sources/latent-video-prediction-better-world-models-paper.md) | Five robustness axes on frozen features | **Both** |

Sixteen of WorldArena's metrics score *video*, which a [JEPA](jepa.md) model does not emit; JEPA work reports CEM/MPC planning success on Push-T and maze navigation, which video generators aren't set up to run. Neither literature can rank the other's models, and the leaderboards are therefore not comparable in either direction.

The bottom two rows are the first shared instruments, and both work by **freezing the representation and probing it** rather than by scoring outputs — which is the only level at which the families are directly comparable. What they find:

- **Pixel fidelity and action recoverability are orthogonal.** At ~20 dB PSNR, frozen action R² spans −0.01 to +0.46, and the highest-PSNR backbones (SDXL VAE, the Cosmos-1 tokenizer) score *lowest* on action, at or below zero. This is [WorldArena](../../sources/worldarena-paper.md)'s r = 0.360 restated at the representation level, now covering both families.
- **Stable ≠ usable.** VideoPrism holds representational cosine similarity above **0.98** under severe patch dropout while collapsing to **2.7%** top-1 accuracy; V-JEPA 2.1 retains **46.1%** on the same clips. The latent-space form of the plausibility trap: a similarity metric can look perfect while the representation carries nothing actionable.

### The dissociation is three years older than the 2026 benchmarks

**[VP²](../../sources/vp2-paper.md)** (Tian, Finn & Wu, ICLR 2023) established it, and with sharper evidence than anything since, because it varies the *loss* while holding architecture fixed:

| Environment | Model | FVD ↓ | Control success |
|---|---|---:|---:|
| robosuite push | SVG′ MSE | **51.7** (worst) | **80%** (best) |
| RoboDesk open slide | SVG′ +LPIPS=1 | **4.9** (best in study) | **10%** |
| RoboDesk open slide | SVG′ MSE | 22.5 | 58% |
| RoboDesk red button | FitVid +LPIPS=1 / +LPIPS=10 | 5.9 / 6.8 | **82% / 32%** |

The critical detail is worse than "weak correlation": **the sign is task-dependent.** FVD tracks success on one RoboDesk task and inverts on another, so no constant correction recovers it. And on red button, SSIM varies by 0.2 points (97.3–97.5) while success ranges 32%→82%.

VP² also supplies two design ideas the 2026 benchmarks lack: a **one-function interface** (`context_frames, action_seq → predictions`, no differentiability or architecture assumption), and a **simulator-as-model upper bound** that separates "the model is bad" from "the planner is bad."

Its scaling results have aged well and are still uncontested: **model capacity from 6M→300M produced no control-performance trend** (larger models appear to overfit action sequences), data gains **plateau early**, and the diffusion model tested needed **220 s per 10-frame forward pass** against FitVid-full's 5.63 s — competitive control at ~39× the cost.

**Still missing**: nobody has run a JEPA-family model through WorldArena's *functional* roles (data engine, policy evaluator, RL environment, action planner). The probe results predict it would do well. That prediction is untested.

## Related concepts

- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — the statistical case, from inside robotics.
- [Instruction leakage](instruction-leakage.md) — a concrete, diagnosed world-model evaluation confound.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — the older name for half of this problem.
- [World-model governance](../safety/world-model-governance.md) — what to do about it.
- [Robot safety standards](../robotics/robot-safety-standards.md) — the certification regimes this would have to plug into.

## Mentioned in

- [WorldArena paper](../../sources/worldarena-paper.md) — the perception–functionality gap, measured.
- [WorldArena 2.0 paper](../../sources/worldarena-2-paper.md) — visuotactile, world-model-as-RL-environment, and the sim-to-real usability gap.
- [WorldRoamBench paper](../../sources/worldroambench-paper.md) — long-horizon stability; per-frame action, visual drift, interaction physics, action-decoupled memory.

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md)
- [What Makes Video World Model Latents Action-Relevant](../../sources/action-relevant-latents-paper.md) — the shared inverse-dynamics probe across eight encoder families.
- [Latent Video Prediction Learns Better World Models](../../sources/latent-video-prediction-better-world-models-paper.md) — five robustness axes; "stable features are not usable features."
- [VP² — A Control-Centric Benchmark for Video Prediction](../../sources/vp2-paper.md) — the founding result; perceptual metrics vs control success, with task-dependent sign.
- [Reconstruction or Semantics?](../../sources/latent-space-robotic-world-models-paper.md) — the same dissociation at the level of a world model's *latent space*; semantic latents roughly double VLA-in-the-loop success over VAE latents.
