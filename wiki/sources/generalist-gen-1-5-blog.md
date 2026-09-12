---
title: "GEN-1.5: Embodied Foundation Models are One-Shot Learners (Generalist AI, Aug 2026)"
type: source
url: https://generalistai.com/blog/gen-1.5
local_path: raw/2026-08-19-generalist-ai-gen-1-5.md
sha256: 1d209b7422e2018cde3389611672f8965622879fcd94fc8f2c75574c71ec6f71
author: "Generalist Team (Generalist AI) — no individual authors named"
published: 2026-08-19
venue: "Generalist AI blog, ~17 min read (~3,940 words), with a suggested BibTeX citation"
format: vendor research blog (no paper, no code, no weights, no third-party evaluation)
tags: [gen-1-5, generalist-ai, in-context-robot-learning, physical-prompting, one-shot, few-shot, emergence, test-time-training, sim-to-real, improvisation, robot-foundation-model, embodied]
ingested: 2026-09-07
rechecked: 2026-09-12
---

## Summary

> [!note] Re-checked 2026-09-12 — no upstream change
> Re-fetched and compared against the `raw/` snapshot word-by-word and number-by-number: the only differences are footer navigation and citation superscripts glued to words by extraction. No revision. The [S1 re-check](skild-s1-blog.md) the same day found that S1's prompts are egocentric *human* videos, so human-to-robot — hedged here as *"in some cases"* — is S1's default mode; the comparison table on [the concept page](../concepts/learning/in-context-robot-learning.md) now reflects that.


**A robot foundation model that learns a new physical task from a single 3–12 second demonstration placed in its context window, with no gradient updates.** Generalist calls this **physical prompting** — the prompt is a sensorimotor sequence (sensor data plus action trajectory) rather than text — and reports **59% ± 10% average success across 10 diverse tasks** one-shot from the pretrained model, rising to **83% ± 9%** after **10 gradient steps on 5 minutes of data**.

GEN-1.5 is described as a large multimodal model with a **30-second context window** over video plus *"other sensor, language, and proprioceptive inputs"*, emitting **100 Hz action trajectories**. It has been **pretraining continuously for over eight months** across three phases, on a data engine of *"activities captured in homes, warehouses, factories, and elsewhere"* — **1,891,392 scenes**, per a nearest-neighbour search they run later in the post.

The framing is explicitly the GPT-3 analogy: few-shot in-context learning arriving as an emergent property of scale rather than as a designed mechanism.

> [!warning] Vendor blog. No paper, no code, no weights, no third-party evaluation, no trial counts.
> Every number here is self-reported by a company raising against this narrative. **No rollout counts are given** for any success rate; the quoted ±std dev is unlabelled as to whether it is across tasks, seeds or trials; there are **no baselines**; and the 10 tasks are described but not tabulated per-task. By the [policy-evaluation standard](../concepts/robotics/robot-policy-evaluation.md) this wiki applies, a 59% average with no n supports nothing quantitative. Read the *shape* of the claims, not the numbers.
>
> To their credit, the post is unusually careful about what it does not claim: *"the tasks are simple and short-horizon,"* *"the success rates are modest,"* and *"skills learned in-context are currently more brittle than finetuned models."*

## The finding that matters most here: it contradicts the wiki's other ICL source

The wiki's [in-context robot learning](../concepts/learning/in-context-robot-learning.md) page is built on [Skild's S1](skild-s1-blog.md), whose central mechanistic claim is that the inner loop must be **trained**:

> Pre-training must therefore use episodic data in which **the task is identified only by an in-context demonstration** — otherwise the model has no pressure to learn the inner loop at all, and will simply learn the tasks.

GEN-1.5 says the opposite, in detail:

> These capabilities appear to emerge directly from pretraining on large amounts of physical interaction data. **We did not explicitly train for any of them: no architectural changes to promote in-context learning, no inner or outer meta-learning loop, no auxiliary objectives** encouraging improvisation.

And the supporting detail is what makes it more than a rhetorical difference. Pretraining used **randomly sampled continuous spans** from the data engine, *"with **no bespoke infrastructure for packing examples into context**"* — so **physical prompts introduce discontinuous jumps in time that the model never saw in training.** If accurate, the model is being asked to do something structurally absent from its training distribution and doing it anyway.

> [!warning] Two vendors, opposite mechanisms, same capability claim
> **S1**: the outer loop is *designed* — structure your episodes so the task is only identifiable from the in-context demo, and the model learns to learn.
> **GEN-1.5**: no such structure, no meta-learning, no packing; ICL *emerged*.
>
> They agree on the **shape** — both say ICL only pays past a scale threshold (S1's crossover at 100k h; Generalist's *"past a certain threshold of pretraining, the cost of adaptation becomes negligible"*) — and disagree on whether the inner loop is **built or grown**. That is a real, testable disagreement about how to train these systems, and **neither source can settle it**: both are vendor blogs with no ablations.
>
> What would settle it: an **ICL-vs-scale curve** with the episodic-structure variable ablated. Generalist shows validation loss improving over eight months (Fig. 3); they do **not** show in-context ability appearing at a threshold. **They demonstrate that the model has ICL, not that it emerged** — which is the gap between the claim and the evidence.

Their own hypotheses for the emergence, offered as speculation: **burstiness and Zipfian structure** in the distribution of physical observations and actions, by analogy to [Chan et al. 2022](https://arxiv.org/abs/2205.05055) on what drives ICL in transformers; and that *"physical work contains naturally repetitive cycles, and the model may have learned to detect and extend such patterns,"* citing *LLMs as General Pattern Machines*.

## The capability list

**One-shot in-context.** 3–12 seconds of a single demonstration in the 30-second window; the rest holds rolling observations. Prompts are recorded either as **human data with a pair of handheld grippers** or as robot rollouts. Tasks named: zippers, jar lids, retrieving money from a wallet, marker into cup, pouring bolts, brushing a cube into a bowl, removing a vacuum pad. **59% ± 10%.**

**Compositional generalization.** Two independently recorded prompts in context — unzip a pouch, retrieve money — and the model *"chains them into one continuous behavior, bridging the two with intermediate motions, recoveries, and ambidexterity that appear in neither prompt."* They propose **"physical prompt engineering"**: assemble a compound task from a library of short reusable prompts rather than collecting a demonstration of the whole thing. Delivered through a **drag-and-drop interface** for selecting which demonstrations enter the context.

**Zero-shot sim-to-real, and they define the term carefully.** Normally "zero-shot sim2real" means train in a simulator and deploy without real data. Here the claim is different and stranger: **pretraining contains no simulation data at all** — *"neither rendered video nor simulated dynamics"* — and a demonstration recorded **in simulation** works as a physical prompt for the real robot, with the prompted behavior generalizing to different hands and new object positions and sizes.

**Human-to-robot.** *"In some cases"* a person demonstrates with their own hands in view of the robot's cameras and the robot reproduces it. Hedged, and no rate given.

**Few-step adaptation.** 1–10 gradient steps on 1–5 minutes of data (~10–50 demonstrations), against the *"tens of thousands of gradient steps"* they say is typical. One-step on one minute of data: **66.5%** on a held-out task. They frame it as **test-time training in an extremely low-data regime**, noting that TTT usually needs tens of steps.

> [!note] The most mechanistically interesting number in the post
> **Ten gradient steps change the weights on held-out tasks by less than 0.15%** — *"suggesting that fine-tuning slightly reconfigures knowledge already present rather than building new representations."*
>
> That is a concrete, checkable statement about *where the capability lives*, and it is the kind of claim the wiki's [LoRA](../concepts/learning/low-rank-adaptation.md) and [knowledge-insulation](../concepts/learning/knowledge-insulation.md) material argues about without a number. It also supports their own strongest sentence: adaptation *"is closer to **reminding the model of something it nearly knows**, with a tiny amount of compute."*

## Improvisation, and a counterintuitive claim about fine-tuning

The improvisation examples are the most vivid part and the least measured:

- Fine-tuned on 5 minutes of brush-sweeping demonstrations, the model **uses a banana as a makeshift brush**; handed a **dustpan** it departs strategically — lifting the block and dumping it — *"an entirely new contact sequence… with no language guidance."*
- It **removes a paper obstacle** covering the bowl (and sometimes replaces it), from a model fine-tuned for **one** gradient step, with no paper in the task data.
- Stuck Lego bricks on the fingertips get removed **with the other hand**.
- **Bimanual** jar-lid rotation when demonstrations used one hand; **ambidexterity** when demonstrations used one arm.
- Models fine-tuned to place *one* block in *one* bowl sometimes **sort blocks by colour** — offered as *"a generalized form of physical commonsense."*

> [!note] More fine-tuning, less improvisation — stated as a trade-off
> *"It strengthens as the number of fine-tuning gradient steps decreases, presumably because **lightly adapted models stay closer to their pretrained priors** and can draw on a broader repertoire of behaviors when the situation departs from the demonstrations."*
>
> This is the robotics form of the alignment-tax / forgetting argument, stated as a **capability** trade-off rather than a safety one: task-specific competence and generality are in tension, and the tension is tunable by step count. If it holds it is a design principle — *adapt as little as you can get away with* — and it is exactly the opposite of the field's default instinct to fine-tune to convergence.

**Credit where due on the contamination check.** The dustpan claim is supported by a **nearest-neighbour language search over 1,891,392 scenes** to show the nearest pretraining examples *"bear little resemblance."* That is more effort than most emergence claims get. The limit is that it is a *language* search over scene descriptions, so a visually similar but differently-described episode would not surface.

## The lineage

| | | |
|---|---|---|
| **GEN-0** | ~Nov 2025 | *"Embodied Foundation Models That Scale with Physical Interaction"* — where they report seeing **predictable scaling laws** |
| **GEN-1** | ~Apr 2026 | *"Scaling Embodied Foundation Models to Mastery"* — post-training to **99%+** success on simple tasks; first signs of *"improvisational intelligence"* |
| **GEN-1.5** | Aug 2026 | one-shot and few-shot in-context learning; pretraining started in parallel with GEN-1 and has run **8+ months** |

None of GEN-0, GEN-1, or their *"The Dark Matter of Robotics: Physical Commonsense"* is ingested here.

Their thesis in one line: *"more pretraining makes adaptation faster, cheaper, and more general. **We do not yet see where that curve asymptotes.**"* And the business argument that follows — the general-purpose robot's promise was *"always conditioned on an expert programming them, which took months"*; if specification reduces to showing, then **how fast a robot becomes useful and who can work with one both change**.

## Entities mentioned

- [Generalist AI](../entities/generalist-ai.md) — **new page**: the company and the GEN lineage.
- [GEN-1.5](../entities/gen-1-5.md) — **new page**: the model.
- No robot platform, no partner, no customer, and no individual researcher is named anywhere in the post.

## Concepts touched

- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — **the second demonstration-conditioned instance, and it contradicts the first on mechanism.**
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — they invoke test-time training explicitly for the 1–10 step regime.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — the emergence-at-threshold claim belongs to that literature.
- [VLA models](../concepts/learning/vla-models.md) — the alternative specification channel; they argue demonstrations beat language for tasks *"difficult to precisely describe."*
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — a genuinely new variant: prompt from sim, with no sim in pretraining.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — handheld-gripper human data as the prompt medium.
- [Imitation learning](../concepts/learning/imitation-learning.md) — the parent tradition.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — where the missing trial counts bite.

## Open questions

- **Did in-context learning emerge, or was it always there?** The post shows a model that has ICL and a validation-loss curve that improves. It does not show ICL appearing at a scale threshold. **An ICL-vs-compute curve is the single figure that would convert this from anecdote to result**, and it is a figure they are in a position to produce.
- **Which of S1 and GEN-1.5 is right about the outer loop?** Designed episodic structure vs emergence. Both are vendor blogs; the disagreement is precise and neither ablates. This is now the most interesting unresolved question on the [in-context page](../concepts/learning/in-context-robot-learning.md).
- **What are the "other sensor inputs"?** The model is said to process video *"alongside other sensor, language, and proprioceptive inputs."* Unspecified — and several named tasks (jar lids, zippers) are genuinely [contact-rich](../concepts/robotics/contact-rich-manipulation.md), so whether force or tactile is in that list matters for the wiki's standing question about whether contact skills are learnable from vision alone. **Unlike [mimic-video](mimic-video-paper.md), absence cannot be inferred here** — the phrase leaves room.
- **What is the inference rate?** *"Produces 100 Hz action trajectories"* is an **output trajectory resolution**, not a demonstrated closed-loop inference rate, and the post gives no latency. A 30-second video context is a large amount to attend over; the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) cannot place this without a measured number.
- **Does the sim-prompt result survive contact?** *Prompt from simulation, act in reality* is the most surprising claim in the post, and it bears directly on the [contact-data argument](../concepts/robotics/contact-rich-manipulation.md): if task *specification* can be simulated once pretraining is real, the scarce-data problem moves but does not vanish. Note the pretraining is still entirely real physical data — this does not contradict the data pyramid, it relocates which layer has to be real.
- **Ten tasks, unnamed rates.** A per-task table with rollout counts would cost them nothing and would move this from a hypothesis with a plausible shape to a result.
