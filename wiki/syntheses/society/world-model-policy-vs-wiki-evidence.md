---
title: World-model policy claims vs. this wiki's technical evidence
type: synthesis
created: 2026-08-07
updated: 2026-08-08
tags: [policy, governance, world-model, evaluation, synthesis, spatial-intelligence]
---

The [HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md) is the first *prescriptive* policy document in a wiki otherwise built from ~370 technical sources — its only predecessor from the same institute, the [AI Index 2026](../../sources/stanford-hai-ai-index-2026.md), measures rather than recommends. About 37 wiki sources touch [world models](../../concepts/world-models/world-model.md) directly. That makes the brief testable in an unusual way: it makes empirical claims about a field this wiki has been accumulating primary sources on for months. This page scores them.

Short version — **the brief is right about the things it is least equipped to know, and thin on the things it should have found easily.**

---

## Claims the wiki corroborates, sometimes harder than the brief does

### "Evaluation is a research patchwork, not a settled standard"

**Corroborated, and the wiki's version is more damning.** The brief argues from the benchmark landscape (VBench, VideoPhy, PhyGenBench, WorldScore, WorldModelBench, WorldArena, [LIBERO](../../entities/libero.md)) that none gives policymakers an adequate basis for safety-critical deployment. [Robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) reaches the same conclusion from inside robotics with numbers the brief doesn't have:

- **±2 pp confidence on a success rate requires ≈1,030 rollouts.** Typical published practice is ~70.
- **[LIBERO-PRO](../../sources/libero-pro-paper.md) takes >90% policies to 0.0%** under perturbations that preserve the task — memorization, not capability.
- Scores saturate above 90%, so the top of the leaderboard is where discrimination is worst.

The brief says the benchmarks can't support *deployment* decisions. The wiki's evidence says they can't reliably support *ranking two policies against each other*. That is a stronger claim, and the brief would have been improved by it.

### "Each architecture fails differently and therefore demands a different evaluation"

**Corroborated precisely.** The brief's three-way split — video generators without persistent scene representation lose coherence; 3D-native systems get geometry but miss change; latent state-space models trade visual detail for change prediction — is the same partition as [generative-video vs JEPA world models](../world-models/generative-video-vs-jepa-world-models.md) and [world-model simulators](../../concepts/world-models/world-model-simulators.md). A policy author with no access to the primary literature arrived at the wiki's own taxonomy. That is a good sign about the brief's technical sourcing.

### "The categories are collapsing into unified models"

**Corroborated, with instances the brief doesn't name.** [Cosmos 3](../../sources/cosmos-3-technical-report.md) is renderer, simulator, and planner in one dual-tower network — queryable as VLM, video generator, forward-dynamics model, inverse-dynamics model, or policy. [Genie Envisioner](../../entities/genie-envisioner.md) / GE-Sim2 makes action first-class inside a video generator. The [world-action model](../../concepts/world-models/world-action-model.md) concept page exists because this collapse already happened. The brief's policy conclusion — safeguards attach to deployment context, not model class — is therefore not speculative hedging; it is already forced.

### "Action-labeled interaction data is the scarce input"

**Corroborated as a scarcity claim; partly undercut as a market-failure claim.** That action data can't be scraped and must be gathered by operating machines is exactly why the wiki's data pages exist. But the brief's inference — that the market "may still underprovide shared action data and simulation environments for startups, universities, and public agencies" — sits next to [Open X-Embodiment](../../entities/open-x-embodiment.md), [DROID](../../entities/droid.md), and the [LeRobot](../../entities/lerobot.md) Hub, which are large public pools assembled by academic-industrial collaboration with no federal coordination at all. The honest version is narrower: *open action data exists and is growing; what's missing is coverage of public-interest domains with diffuse commercial returns.* The brief does eventually say that, but only after arguing the general case.

### "Teaching to a flawed test"

**Corroborated — and now measured, one day after this page was written.** The brief identified the failure mode; [WorldArena](../../sources/worldarena-paper.md) sized it. Running world models as policy evaluators against the RoboTwin simulator's own verdict, **both models "have consistently higher success rates than those measured in the simulator, suggesting partial overfitting to successful trajectories."** The bias is directional: a learned evaluator *flatters* what it evaluates. Ranking survives ([Ctrl-World](../../entities/ctrl-world.md), r = 0.986); levels don't ([Cosmos](../../entities/nvidia-cosmos.md)-Predict 2.5, r = 0.483).

One loose end: [Veo](../../entities/veo.md) reports the **opposite sign** — predicted rates running low against real evaluations. Both agree ranking beats level; the direction of the level error is unexplained.

---

## Claims the wiki complicates

### "Planners are the least mature category"

**Directionally right, and the wiki is the reason it's hard to say so confidently.** This wiki holds **77 sources on [VLA models](../../concepts/learning/vla-models.md)**, many reporting LIBERO success above 90%. Read naively, that contradicts "most contemporary robot demonstrations are confined to short, narrow tasks in controlled labs."

Read against [robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md), it doesn't contradict it at all — it *is* it. The 90%+ numbers come from ~70-rollout evaluations on a benchmark whose perturbation-robust variant zeroes those same policies, and **no policy in the wiki succeeds beyond roughly four complex subtasks**. So the brief's claim survives, but only because the counter-evidence is unreliable, which is a strange thing for a policy document to be right by accident about.

> [!note] The reframing worth keeping
> "Planners are immature" and "planner benchmarks are uninformative" are different problems with different fixes. The brief treats the first as the fact and the second as a gap. The wiki's evidence suggests the second is what's actually established, and the first is inferred from it.

**Update (2026-08-08): the brief's claim now has direct evidence, from a direction nobody was looking.** [WorldArena](../../sources/worldarena-paper.md) measures world models *as action planners* and finds them **3–4× worse than a [π0.5](../../entities/pi-zero-5.md) policy** (20%/21% vs 77%/66%). So "planners are least mature" is confirmed — but note what the comparison actually shows: the mature planner in that table is a **VLA**, not a world model. The brief's taxonomy treats planning as a world-model capability tier; the measurement says the best planner available is a system from an entirely different lineage. Meanwhile world models turn out to be genuinely useful as **RL environments** — a role the brief's three-category taxonomy has no slot for at all.

### "Simulation-to-reality gap" as a policy object

**The brief's framing is one generation behind the wiki's.** [Sim-to-real transfer](../../concepts/learning/sim-to-real-transfer.md) traces the problem to 2013 and earlier under the name *simulation bias*, with the mitigation lineage (domain randomization, artificial noise injection) going back to 1995. The brief presents the gap as a new consequence of world models. What is actually new is the compound failure — a *learned* simulator that is both training environment and judge — which the brief does identify separately and which genuinely has no pre-2020 analogue.

### "World models could lower the cost of simulation"

**Still unverifiable, now with more sources that don't answer it.** Neither WorldArena paper reports cost or wall-clock, including for the RL-inside-a-video-model experiments that should be the most expensive thing in the cluster. This is the load-bearing economic claim under the entire "infrastructure and incentives" pillar, and neither the brief nor the technical literature supplies numbers. The wiki's [code-as-policy](../../concepts/agents/code-as-policy.md) page notes the same absence across a ten-paper lineage: **nobody reports cost.** The one hard comparative figure in the wiki runs the other way on inference — [LeWorldModel](../../entities/leworldmodel.md) reports up to **48× faster planning** than foundation-model-based world models, i.e. the cheap approach is the *latent* one, not the generative renderers the brief treats as the mature end of the field.

---

## What the brief has that the wiki didn't

Not everything is a scoring exercise. Four contributions are genuinely new here:

1. **The third governance object.** Content → authority to act → **validity of the learned environment**. The wiki had [semantic safety](../../concepts/safety/semantic-safety.md), [guardrails](../../concepts/safety/ai-guardrails.md), and [robot safety standards](../../concepts/robotics/robot-safety-standards.md), and none of them asks whether the *environment* a policy was trained in was real enough to certify against.
2. **The procurement trap.** The most useful system-specific simulator is usually the vendor's own, because it encodes proprietary sensor, architecture and failure-mode detail — so a buying agency ends up depending on the vendor to both build and validate the system. This has no analogue anywhere else in the wiki and it is a sharp, concrete observation.
3. **Export controls aimed at the wrong chokepoint.** Compute and weights are controllable; physical-world data and deployment scale are not, and the brief argues world-model advantage may rest on the latter.
4. **Expertise migration.** As how a plant runs or how a crane operator executes a lift gets captured in simulation, "that knowledge moves from the workers who hold it toward the firms that build the models," and the operator gradually loses the ability to work without the system. The wiki's [assistive robotics](../../concepts/robotics/assistive-robotics.md) thread has the user-autonomy version of this argument; it did not have the labor version.

---

## Where this leaves the wiki

Three follow-ups were opened on 2026-08-07. Two are closed.

- ~~**Ingest WorldArena.**~~ **Done (2026-08-08)** — plus WorldArena 2.0 and [WorldRoamBench](../../entities/worldroambench.md). It is the instrument both literatures were asking for, and it says the gap is real and quantified: EWMScore correlates with human judgment at r = 0.825 and with **action planning at r = 0.360**. See [what world models are measurably good for](../world-models/what-world-models-are-measurably-good-for.md).
- ~~**Measure the shared-weights evaluation bias.**~~ **Partly closed** — WorldArena measures the sign and the ranking/level split (above). What remains open is *why* Veo's error runs the other way.
- **A primary [Genie 3](../../entities/genie-3.md) source turns out not to exist.** DeepMind has published no parameter count, architecture, or training corpus; a blog post and a model page are the whole record, and WorldRoamBench's model table independently confirms the gaps. What did arrive is **third-party measurement**: Genie 3 ranks 1st of 10 in first-person view, winning on *memory* while placing 7th on action following. A primary [World Labs](../../entities/world-labs.md) / Marble source is still missing.

New follow-up: **no benchmark in this cluster evaluates a JEPA-family model.** Every model in WorldArena and WorldRoamBench is a pixel predictor, and WorldArena's 16 metrics score *video*, which [V-JEPA 2](../../entities/v-jepa-2.md), [LeWorldModel](../../entities/leworldmodel.md), and [DINO-WM](../../entities/dino-wm.md) do not produce.

> [!note] Corrected 2026-08-08
> This page first called the latent-prediction thread "unmeasured by the field's best instruments." That overstated it — JEPA world models are measured, by [stable-worldmodel](../../sources/stable-worldmodel-paper.md) and [JEPA-WMs](../../sources/jepa-wms-paper.md), on planning success rather than video quality. The accurate diagnosis is **incommensurability**: two literatures, two instruments, neither runnable on the other's models. The first shared instruments arrived in mid-2026 ([action-relevant latents](../../sources/action-relevant-latents-paper.md), [latent video prediction](../../sources/latent-video-prediction-better-world-models-paper.md)) and both work at the probe level, not the system level. Full treatment in [what world models are measurably good for](../world-models/what-world-models-are-measurably-good-for.md).

This matters for the brief's framing specifically. Its maturity ordering assumes the commercially mature renderers are the practical path; the wiki's one hard comparative number (LeWM's **48× faster planning**) and the new probe results (pixel fidelity and action recoverability are **orthogonal**) both point the other way.

## Sources

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md)
- [World-model evaluation](../../concepts/world-models/world-model-evaluation.md) · [world-model governance](../../concepts/safety/world-model-governance.md) · [functional taxonomy](../../concepts/world-models/world-model-functional-taxonomy.md) · [spatial intelligence](../../concepts/world-models/spatial-intelligence.md)
- [Robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) · [LIBERO-PRO](../../sources/libero-pro-paper.md) · [sim-to-real transfer](../../concepts/learning/sim-to-real-transfer.md)
- [Cosmos 3](../../sources/cosmos-3-technical-report.md) · [LeWorldModel](../../entities/leworldmodel.md) · [Veo](../../entities/veo.md)
