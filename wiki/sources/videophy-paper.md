---
title: VideoPhy — Evaluating Physical Commonsense for Video Generation (Bansal, Lin, Xie, Zong et al.; arXiv v2 2024)
type: source
url: https://arxiv.org/abs/2406.03520
fetch_url: https://arxiv.org/pdf/2406.03520v2
author: Hritik Bansal, Zongyu Lin, Tianyi Xie, Zeshun Zong, Michal Yarom, Yonatan Bitton, Chenfanfu Jiang, Yizhou Sun, Kai-Wei Chang, Aditya Grover
published: 2024-06-05
ingested: 2026-09-11
venue: arXiv preprint (v1 2024-06-05, v2 2024-10-03); the PDF is marked "Preprint" and states no conference venue
local_path: raw/2406.03520v2.pdf
sha256: 71e32ba65a8646a6c03ce0f58284d97ceafff437d0e2608b60754b0ea3721605
format: pdf (43 pp., 29 figures, 12 tables)
tags: [videophy, videocon-physics, physical-commonsense, intuitive-physics, video-generation, text-to-video, benchmark, world-model-evaluation, human-annotation, mllm-critic, auto-evaluator, cogvideox, ucla, google-research, primary-source]
---

## Summary

The first benchmark built specifically to ask whether text-to-video models obey **intuitive physics**, from UCLA (with two Google Research co-authors), and the primary behind a name the wiki had been carrying second-hand for a month. VideoPhy is **688 human-verified captions** — 289 solid-solid, 291 solid-fluid, 108 fluid-fluid interactions, each also labelled easy/hard by two physics-simulation PhD students — fed to **twelve** 2024-era T2V models (seven open, five closed), with every generated video scored **by people, not metrics**, on two binary axes: *semantic adherence* (does the video show the caption?) and *physical commonsense* (does it obey physics?). The headline is bleak: the best model, CogVideoX-5B, produces a video that passes both tests for **39.6%** of prompts; every other model is **below 20%**, and OpenSora manages 4.9%. Every model is worst on solid-solid contact (best: 24.4%), and physics scores fall as the amount of motion rises (r = −0.8). The paper then trains **VideoCon-Physics**, a 7B video-LM fine-tuned on 12,000 of its own human labels, because the frontier VLMs it tried were close to coin-flips at judging physics — GPT-4V scored ROC-AUC 53 and Gemini-1.5-Pro 58 against the human labels. VideoCon-Physics reaches 73, and reproduces the human *ranking* of models well enough to serve as a leaderboard, with one visible misranking (Pika). This is the 2024 origin of two findings the wiki later recorded from 2026 sources: generators fail physics far more often than they fail aesthetics, and off-the-shelf multimodal judges cannot see it.

## Key claims

### Benchmark construction (§2, Table 2)

- **Three-stage pipeline.** (1) GPT-4 generates candidate captions — 500 each for solid-solid and solid-fluid, 200 for fluid-fluid, with prompts (Appendix D) that forbid static scenes, invisible processes (dissolving, boiling, corrosion), phase changes, and "penetration" actions like scratching; (2) the **authors** verify captions for clarity, moderate complexity, and correct category; (3) two "experienced graphics researchers (senior Ph.D. students in physics-based simulation)" independently label each caption **easy (0) or hard (1)** by how hard it would be to simulate in a state-of-the-art physics engine. Disagreements — "less than 5% of the instances" — were discussed to unanimity. Difficulty is defined *within* a category and "cannot be compared across different categories."
- **What "hard" means to a simulation expert** (Table 1): deformables over rigid bodies (harder PDEs), high-speed over slow motion (numerical stiffness), mixing different fluids over mixing the same fluid, complex contact over a simple topple. The examples: "Bottle topples off the table" (easy, rigid bodies) vs "Scrubber scrubs a dirty dish" (hard, complex contacts); "Rain splashing on a pond" (easy) vs "Ink spreading in still water" (hard).
- **Final statistics:** 688 captions; 138 unique actions; average caption length **8.5 words**; 366 easy / 322 hard; 12 models; **11,330 generated videos**; **36,500 human annotations**. Split **344 train / 344 test** prompts with matched category and difficulty distributions — the test half is the benchmark, the train half exists to train the auto-rater.
- The authors defend the small size by analogy to Winoground (400), Visit-Bench (500), LLaVA-Bench (90), and Vibe-Eval (269): "Given that human verification demands significant expert hours and is not scalable within our budget, we prioritize data quality."
- A footnote records that GPT-4-enhanced *longer* captions were tried and dropped: "most of the T2V models are poor at following long/enhanced captions most of the time."

### The two metrics and the annotation protocol (§3)

- **Semantic adherence (SA ∈ {0,1})** — are the caption's actions, entities, and relationships depicted? **Physical commonsense (PC ∈ {0,1})** — do movements and object states follow "intuitive physics that humans acquire with their experience in the real-world"? PC is judged from the video alone, independent of the caption. The reported figures are the fraction with SA = 1, with PC = 1, and the **joint** SA = 1 ∧ PC = 1, which the authors treat as the headline.
- **Why binary.** Dense feedback is "hard to acquire and miscalibrated"; binary judgment is what text-to-image alignment work uses. Annotators were *not* asked to name the violated law — too slow and expensive.
- **Who annotated.** Qualified Amazon Mechanical Turk workers, briefed over a shared Slack channel; **14 workers "who have studied high-school physics"** passed a qualification test. Paid **$18/hour**; total annotation spend **$3,500**. Model identity was hidden. Static outputs were to be judged as static scenes ("a folded brick does not follow physical commonsense"); grainy or speckled static output counts as PC = 0.
- **Benchmark labels:** one video per test prompt per model, **three annotators, majority vote** — **24,500 annotations**. **Inter-annotator agreement: 75% (SA), 70% (PC)** — "human annotators find the task of judging physical commonsense more subjective than semantic adherence." A footnote attributes the disagreement to "differing tolerance for commonsense violations in imperfect videos" and predicts it will shrink as models improve.
- **Auto-rater training labels:** two videos per *train* prompt for nine models (CogVideoX and Dream Machine excluded as too recent), **one annotator each**, 12,000 annotations, half per metric.

### Headline results — human evaluation (Table 3, n = 344 test prompts per model)

| Model | **SA = 1 ∧ PC = 1** | SA | PC | joint, solid-solid | joint, solid-fluid | joint, fluid-fluid |
|---|---:|---:|---:|---:|---:|---:|
| *Open* | | | | | | |
| **CogVideoX-5B** | **39.6** | 63.3 | 53 | 24.4 | 53.1 | 43.6 |
| VideoCrafter2 | 19.0 | 48.5 | 34.6 | 4.9 | 27.4 | 32.7 |
| CogVideoX-2B | 18.6 | 47.2 | 34.1 | 12.7 | 21.9 | 25.4 |
| LaVIE | 15.7 | 48.7 | 28.0 | 8.5 | 15.8 | 34.5 |
| SVD-T2I2V | 11.9 | 42.4 | 30.8 | 4.2 | 17.1 | 18.2 |
| ZeroScope | 11.9 | 30.2 | 32.6 | 6.3 | 14.4 | 20.0 |
| OpenSora | 4.9 | 18.0 | 23.5 | 1.4 | 7.5 | 7.3 |
| *Closed* | | | | | | |
| Pika | 19.7 | 41.1 | 36.5 | 13.6 | 16.3 | **44.0** |
| Dream Machine (Luma) | 13.6 | **61.9** | 21.8 | 12.1 | 16.6 | 9.0 |
| Lumiere-T2I2V (Google) | 12.5 | 48.5 | 25.0 | 8.4 | 17.1 | 10.9 |
| Lumiere-T2V (Google) | 9.0 | 38.4 | 27.9 | 8.4 | 9.6 | 9.1 |
| Gen-2 (Runway) | 7.6 | 26.6 | 27.2 | 4.0 | 8.1 | 15.1 |

- CogVideoX-5B's lead over every other model is significant by paired t-test (**p < 0.0001**, footnote 7); the authors credit its data curation (detailed captions, filtering low-motion and low-quality clips). CogVideoX-2B → 5B is read as capacity scaling helping physics (PC 34.1 → 53).
- **SA and PC come apart.** Dream Machine has the highest SA of any model (61.9%) and near-bottom PC (21.8%): "optimizing for semantic adherence does not necessarily lead to good physical commonsense."
- **Solid-solid is the worst category for every model.** The best joint score there is CogVideoX-5B's 24.4%; four models are below 5%. Pika is best on fluid-fluid (44.0%); CogVideoX-5B is best on solid-fluid (53.1%, with SA 76.5 / PC 59.3).
- **Hard captions score lower than easy on both metrics for essentially every model** (Table 6): CogVideoX-5B SA 63.8 → 62.5, PC 55.3 → 50.3; Dream Machine PC 29.4 → 12.5; Lumiere-T2I2V SA 56.6 → 38.7. "Captions that are harder to simulate physically are also harder to control via conditioning."
- **Correlations with quality and motion** (Appendix O, Table 11; LAION aesthetics and RAFT optical flow): aesthetics–PC **+0.3**, aesthetics–SA +0.5, **motion–PC −0.8**, motion–SA −0.1. Closed models have the highest aesthetics and still fail: Gen-2 scores 5.8 on the aesthetic classifier and 7.6% joint.
- **Not evaluated:** Sora, Kling, and Genmo — no API access. Gen-2 and Pika videos were obtained through custom scripts on **$225** of subscriptions.

> [!note] Cell sizes, and two appendix rows that do not reconcile
> Each overall cell is one video for each of 344 prompts; if the category split is as even as the paper says, the solid-solid and solid-fluid cells are ~145 videos and the **fluid-fluid cells ~54**, so Pika's 44.0 vs CogVideoX-5B's 43.6 there is a difference of well under one video. Separately, the fine-grained appendix rows for CogVideoX-5B do not match the main text: Table 7 gives its solid-solid PC as 24.5 and fluid-fluid joint as 18.2 (Table 3: 43.3 and 43.6), and its four outcome cells sum to 94.5% and 74.6% rather than 100%; Table 8 gives easy/hard joint 22.9/24.5, which cannot average to the 39.6 of Table 3. Every other model's rows reconcile. Table 3 and Table 6 are internally consistent with the abstract and text, and this page uses them. Likewise, the text says Gemini-1.5-Pro's PC ROC-AUC is "54" while Table 4 and the introduction's "15 points" both imply **58**; the table is used here.

### Failure taxonomy (§5.2, Appendix Q)

Six modes, illustrated with ~60 annotated clips across all twelve models (Figures 15–26): **conservation of mass** (volume or texture changes over time — milk poured, level does not rise; coffee beans appear from nowhere), **Newton's first law** (velocity changes with no force), **Newton's second law** (momentum violated — water droplets hang in the air, a diver floats), **solid constitutive law** (rigid objects deform — a metal spoon bends while stirring, a coin splits and remerges), **fluid constitutive law** (unnatural flow), and **non-physical penetration** (fingers through fingers, tea through the cup). The authors' summary of the underlying deficit: models "struggle to accurately identify individual objects and comprehend their material properties." Even CogVideoX-5B shows dominoes changing geometry mid-topple (Figure 5). Gen-2 "sometimes generates static objects in the air with slow camera motion, instead of meaningful physical dynamics."

### VideoCon-Physics — the auto-evaluator (§3.3, §6, Appendices F, J, L)

- **Base model:** VideoCon, a 7B open video-text model (mPLUG-Owl-video lineage) trained on *real* video for semantic-adherence judgment. It is prompted "Does this video entail the description [T]?" (SA) or "Does this video follow physical laws?" (PC) and scored as p(Yes)/(p(Yes)+p(No)). Fine-tuned with LoRA (r = 32, α = 32, dropout 0.05) on all attention-block projections, 5 epochs, peak LR 1e-4, batch 32, 2×A6000, 32 frames at 224×224. A single multi-task classifier; separate SA and PC classifiers gave no gain.
- **Agreement with humans on unseen prompts** (Table 4, ROC-AUC vs the majority-vote test labels, videos from models seen in training):

| Judge | SA | PC |
|---|---:|---:|
| Random | 50 | 50 |
| GPT-4-Vision (8 uniformly sampled frames) | 53 | 53 |
| Gemini-1.5-Pro-Vision (full video) | 73 | 58 |
| VideoCon, zero-shot | 65 | 54 |
| **VideoCon-Physics** | **82** | **73** |

  Gains over zero-shot VideoCon are 17 (SA) and 19 (PC) points; over Gemini, 9 and 15. The authors' reading: "GPT-4-Vision's judgments are close to random"; Gemini is good at SA and "close to random in physical commonsense" — "existing multimodal foundation models lack the capability to judge physical commonsense." Even the fine-tuned judge finds PC harder than SA.
- **Generalization to unseen generators** (Table 5): an ablated VideoCon-Physics trained only on VideoCrafter2, ZeroScope, LaVIE, OpenSora, SVD-T2I2V and Gen-2 videos, tested on the three remaining training-set models: SA **79** vs 64 zero-shot, PC **72** vs 57 — +15 on each.
- **Leaderboard fidelity** (Table 10): human ranking of open models CogVideoX-5B > VideoCrafter2 > CogVideoX-2B > LaVIE > SVD-T2I2V > ZeroScope > OpenSora; the automatic leaderboard (mean of VideoCon-Physics SA and PC) swaps only LaVIE and CogVideoX-2B. Closed models show "similar trends," except that **Pika — the human-ranked best closed model — "achieves a relatively low score on the automatic leaderboard,"** which the authors attribute to needing more training data.
- **Proposed uses** (Appendix N): cheap model selection before human evaluation; data filtering; and as a **reward model** for post-training video generators — proposed, not tested.

### Fine-tuning a generator on VideoPhy data did not help (Appendix P, Table 12)

Lumiere-T2I2V fine-tuned on the **1,000** train-set (video, caption) pairs that humans scored SA = 1 ∧ PC = 1, then scored by VideoCon-Physics: SA **46 → 36.5**, PC **25 → 24.6**. Offered explanations: too few samples, a mixed on-/off-policy training set drawn from several generators, and "vanilla finetuning being a bad algorithm for learning from these samples."

### Stated limitations (Appendix A) and scope

- Only solids and fluids; "more branches of physics, including projective geometry," are future work. 688 captions. Not an exhaustive model list.
- **Annotators are mostly US and Canadian AMT workers**, so the labels "reflect the perceptual biases of the annotators from Western cultures."
- Not stated as a limitation but worth recording: the benchmark is **text-conditioned only** — no action or image conditioning is scored — and the "general-purpose physical world simulator" framing in the abstract is tested only through T2V prompting. Captions and annotations are MIT-licensed; videos inherit their generators' licences.

## Reading it against the wiki

> [!note] What the wiki had wrong about this paper
> The [world-model evaluation](../concepts/world-models/world-model-evaluation.md) landscape table files VideoPhy under "physical commonsense in generated video, via **automated metrics or model-based critics**," and [Physion-Eval](physion-eval-paper.md)'s page repeats that the landscape is "largely automated or model-judged — VBench, VideoPhy, PhyGenBench." That is backwards for this paper. **Every headline number in VideoPhy is a three-annotator human majority vote**; the model critic is a downstream product trained on 12,000 of those labels, offered because human evaluation "is both expensive and difficult to scale." The [physical-reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) page's "human annotation or a model judge" is the accurate version. Also: the [backlog](../backlog.md) entry for this ingest links VideoPhy to arXiv 2406.11888, which is an unrelated paper on neural logic programs; the correct identifier is 2406.03520.

- **The "critics can't see physics" result is two years older than the wiki thought.** The wiki records from [Physion-Eval](physion-eval-paper.md) (2026) that MLLM critics are 2–6× less sensitive than untrained humans and that the automated benchmark layer is therefore unvalidated. VideoPhy reported the same thing in June 2024 with a cruder instrument: GPT-4V at ROC-AUC 53 and Gemini-1.5-Pro at 58 on physics, against 73 for the same Gemini on semantics. The pattern — frontier VLMs are competent at *what is depicted* and near chance at *whether it could happen* — has held across two model generations. Physion-Eval's open question of whether a critic trained on the benchmark's own human traces would do better was also already answered here, modestly: 12,000 binary labels and a LoRA lift a 7B judge from 54 to 73 on physics, which is real and still well short of the 82 the same model reaches on semantics.
- **Ranking survives, level does not — again.** The automatic leaderboard reproduces the human ordering of open models with one adjacent swap, and misplaces Pika among the closed ones. That is the same shape the wiki found in [WorldArena](worldarena-paper.md) (Ctrl-World as evaluator: r = 0.986 on ordering, inflated absolute rates) and [Veo](../entities/veo.md) (Pearson 0.88, deflated absolute rates): a learned judge is a usable comparator and an unreliable measurement at once. VideoPhy is the earliest instance of it in this wiki, and its authors frame the auto-rater exactly that way — a screen before human evaluation, not a replacement.
- **Motion is the enemy of physics, r = −0.8.** This is the strongest correlation in the paper and the least discussed. Combined with the instruction that a plausible *static* scene can pass PC, it means the benchmark structurally rewards a generator that moves less — the mirror image of the tension the wiki recorded from WorldRoamBench, where strict physics penalizes action-following. Nobody has a scoring rule that does not trade physics against motion or physics against controllability; see the [perception-distortion tradeoff](../concepts/world-models/perception-distortion-tradeoff.md) for why a point estimate under uncertainty drifts toward the blur.
- **Solid-solid contact is where everything fails, and it is the category robotics needs.** Every model's worst category is rigid and deformable bodies in contact — topple, catch, crush, stack — at a best of 24.4% and a median well under 10%. The wiki's manipulation sources live entirely in that cell. The difficulty labels add something the 2026 benchmarks lack: they come from **simulation experts asking how hard the scene would be for a physics engine**, and the generators' scores fall with that label. Hard-to-simulate is hard-to-generate, which is a small piece of evidence that the [generative-video and simulator](../syntheses/world-models/generative-video-vs-jepa-world-models.md) routes to a world model stumble on the same physics rather than on different things. The paper's §1 also argues explicitly that simulators cannot serve as ground truth for generated video — no reliable single-view 3D geometry, hand-tuned material parameters, unknown lighting, and "physical simulations are not equivalent to ground truth" — which is why the two traditions in [physical-reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) use different ground truths by design, not by neglect.
- **Sample-size discipline.** By the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) standard, the overall cells (n = 344) separate CogVideoX-5B from the pack comfortably (the authors' own t-test agrees), the open-model ordering below it is a spread of 19.0 to 11.9 that no test in the paper resolves, and the fluid-fluid cells (~54 videos) cannot rank Pika against CogVideoX-5B at all. The 70% inter-annotator agreement on a binary label is worth carrying forward: a substantial share of the physics labels were contested among people who had all passed a physics screen.
- **Post-training on "good" generations went backwards.** The one attempt to use the benchmark to *improve* a generator (Appendix P) lost 9.5 points of semantic adherence and gained nothing on physics with 1,000 mixed-source clips. The authors propose VideoCon-Physics as a reward model but never run it in a loop. This is the untested half of the [reward post-training](../concepts/learning/reward-post-training-diffusion.md) story for video: the wiki has the credit-assignment machinery from image generation and, here, evidence that vanilla SFT on filtered outputs is not enough.
- **Historical numbers, not current ones.** Twelve 2024 models, several since retired; Sora and Kling untested. The wiki's newer physics-realism source, [Physion-Eval](physion-eval-paper.md), reports 83–93.5% of 2026-model clips carrying a human-identified violation on a different protocol, so the two are not directly comparable — but the direction has not reversed. Treat VideoPhy's model table as a dated baseline and its *design* (human binary labels on material-pair captions, a fine-tuned judge, the motion correlation) as the durable contribution.

## Entities mentioned

- **UCLA** (Bansal, Lin, Xie, Zong, Jiang, Sun, Chang, Grover) and **Google Research** (Yarom, Bitton) — no pages; Google Research is distinct from [Google DeepMind](../entities/google-deepmind.md), whose Gemini-1.5-Pro-Vision is the strongest zero-shot baseline here.
- [OpenAI](../entities/openai.md) — GPT-4 generated the captions; GPT-4V is a near-random judge baseline; Sora was not evaluated (no API).
- Generators evaluated, none with a wiki page: CogVideoX-2B/5B (Zhipu), VideoCrafter2, LaVIE, Stable Video Diffusion (as SVD-T2I2V via SDXL images), ZeroScope, OpenSora; Pika, Luma Dream Machine, Runway Gen-2, Google Lumiere (T2V and T2I2V). Amazon Mechanical Turk supplied the annotators (no page).
- Comparators in the wiki: [Physion-Eval](../entities/physion-eval.md), [WorldArena](../entities/worldarena.md), [Veo](../entities/veo.md). The paper's stated motivation cites text-guided video generation for agents (UniPi, Genie — the 2024 Genie, not [Genie 3](../entities/genie-3.md)).

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the benchmark-landscape row this page corrects, and the earliest instance of the ranking-vs-level pattern.
- [Physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) — the generative-video tradition's founding member; human perception as ground truth by design.
- [Perception–distortion tradeoff](../concepts/world-models/perception-distortion-tradeoff.md) — the motion–physics correlation of −0.8 as a benchmark-level version of the same pressure.
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) — VLMs in the judge role, and why they fail at it.
- [Reward post-training of diffusion and flow models](../concepts/learning/reward-post-training-diffusion.md) — VideoCon-Physics proposed as a reward model; the negative SFT result.
- [Low-rank adaptation](../concepts/learning/low-rank-adaptation.md) — how the judge was fine-tuned.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — the paper's argument that simulators cannot be ground truth for generated video.
- [What world models are measurably good for](../syntheses/world-models/what-world-models-are-measurably-good-for.md) — the 2024 baseline for the generator side.

## Open questions

- Would a 2026 judge (Gemini 3, Cosmos Reason, a video-native encoder) still sit near 58 on VideoPhy's PC labels? Physion-Eval says the frontier critics remain poor on its protocol; nobody has re-run them on this one, which has the advantage of being cheap and public.
- Why does the trained judge lag on physics (73) but not semantics (82) when the training labels are the same size for both? Label noise (70% vs 75% agreement) explains some of it; the rest is unexplained.
- Is the motion penalty in the *models* or in the *annotators*? Faster clips are harder to generate and harder to judge; the paper cannot separate the two, and a re-annotation at reduced playback speed would.
- The difficulty labels were made by simulation experts against 2024 physics engines. Whether the same captions are "hard" for a differentiable or GPU engine today, and whether the generator gap follows, is untested.
- VideoPhy-2 (2025) is described in the backlog as action-centric with rule-level violation labels; how its numbers relate to these is not yet in the wiki.
