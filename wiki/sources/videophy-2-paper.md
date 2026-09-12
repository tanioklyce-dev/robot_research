---
title: VideoPhy-2 — A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation (Bansal, Peng, Bitton et al.; 2025)
type: source
url: https://arxiv.org/abs/2503.06800
fetch_url: https://arxiv.org/pdf/2503.06800v1
author: Hritik Bansal, Clark Peng, Yonatan Bitton, Roman Goldenberg, Aditya Grover, Kai-Wei Chang
published: 2025-03-09
ingested: 2026-09-11
venue: arXiv v1
local_path: raw/2503.06800v1.pdf
sha256: 64bfa8cffed26df7091d68dd3c127a5719847c2f61ab21aa14a69c920c03b910
format: pdf
tags: [videophy-2, videophy, physical-commonsense, video-generation, benchmark, world-model-evaluation, human-annotation, physical-rules, conservation-laws, auto-evaluator, vlm-judge, wan2.1, cogvideox, cosmos, hunyuanvideo, sora, luma-ray2, ucla, google-research, bansal, primary-source]
---

## Summary

The second VideoPhy benchmark, from UCLA and Google Research, and the first in the family to ask its question **per physical law rather than per video**. Where [VideoPhy](videophy-paper.md) (2024) scored 688 prompts about *material interactions* with a binary judgment, VideoPhy-2 curates **197 real-world actions** (143 sports/physical activities, 54 object interactions) seeded from Kinetics, UCF-101 and Something-Something v2, expands them with Gemini-2.0-Flash-Exp into **3,940 multi-event prompts**, generates ~6,800 videos from seven text-to-video models, and has three paid annotators per video rate **semantic adherence (SA)** and **physical commonsense (PC)** on 5-point Likert scales *as separate tasks* — the PC rater never sees the prompt. The novelty is a third layer: for every video, an LLM writes three testable physical rules tagged with the law they exemplify ("the ball moves up after bouncing off the floor — Elasticity"), annotators mark each rule followed / violated / cannot-be-determined and add violations the LLM missed, and the result is **102K human annotations** that can be aggregated by law. The headline is that the best model, **Wan2.1-14B, scores 32.6% joint (SA ≥ 4 ∧ PC ≥ 4) on the full test set and 21.9% on a 60-action hard subset**; that closed models (Sora 23.3%, Luma Ray2 20.3%) do *not* beat the open ones; that **conservation of mass and momentum are violated in ~40% of the rules that invoke them** while reflection and buoyancy sit below 20%; and that physical commonsense is essentially uncorrelated with aesthetics (r = 0.09), motion quality (0.002), and even prompt adherence (0.14). A 7B fine-tuned evaluator, **VideoPhy-2-AutoEval**, is offered as the scalable substitute — and its own numbers (Pearson 0.37 with human PC on unseen prompts, against 0.11 for Gemini-2.0-Flash-Exp) are the most honest measurement in the paper of how far the judges lag the annotators.

## Key claims

### The action-centric design (§2, Table 1, Appendix B–C)

- **Seeds.** >600 candidate actions from Kinetics, UCF-101 and SSv2; two independent groups of STEM student authors kept only actions both marked as relevant to physical commonsense (dropping typing, arguing, petting a cat, playing instruments); 232 survived, then Gemini-2.0-Flash-Exp deduplicated to **197 actions** — **143 physical/sports activities, 54 object interactions** (full list in Appendix Table 9). The SSv2-derived object interactions read like manipulation primitives: *pushing something so that it almost falls off but doesn't*, *putting something that can't roll onto a slanted surface so it slides down*, *poking a stack of something without the stack collapsing*.
- **Prompts.** Gemini generates **20 prompts per action → 3,940**, under a template (Appendix Fig. 11) that demands visible physical interactions with direct outcomes, forbids mental states / sounds / poetic language / subtle motion, and asks for **multiple events per prompt** ("draws the bowstring back to full tension, then releases the arrow, which flies straight and strikes a bullseye"). Average **16 words** per original caption; a Mistral-NeMo-12B prompt upsampler (from the Cosmos paper) produces **138-word** dense captions for models that accept them. Relative to VideoPhy-1: **5.72× more captions, 1.88× longer originals, 16.2× longer upsampled**.
- **Physical rules.** Rules are *not* derived from the prompt, because models often fail the prompt yet make a physically fine video. Instead each generated video is captioned by Gemini-2.0-Flash-Exp, then Gemini writes **three rules with associated laws** from the caption (a two-step process the authors say worked better than rule-from-video directly; footnote 1). Rules must be observation-centric, about material behaviour rather than actor intent, testable, and *guaranteed by the prompt* (Appendix Fig. 12 gives good/bad examples — "the gravity acts on the ball" is rejected as untestable). Because LLM rules may not be visually grounded, annotators get a third label, **cannot be determined (CBD)**, and are asked to write additional violated rules; those free-text violations are converted back into rule + law statements by Gemini.
- **Hard subset.** Model-based selection in the style of Humanity's Last Exam / ZeroBench: generate with **CogVideoX-5B**, keep the **60 actions (of 197) on which it scores zero joint performance** → **1,200 prompts** (Appendix Table 10). The authors characterise them as physics-rich momentum transfer (discus, passing a football), state change (bending until it breaks), balance (tightrope) and complex motion (backflip, pole vault, pizza tossing).
- **Split.** Test **590 prompts (197 × 3)**, training **3,350 (197 × 17)**; the training split exists only to build the auto-evaluator.

### Human annotation (§3.1–3.2, §4)

- **12 AMT annotators**, qualification-tested, remotely briefed, paid **$18/hr**. **Three annotators per video.** SA and PC are averaged and rounded to the nearest integer; rule labels are by majority vote.
- Two separate tasks by design: SA (prompt + video) and PC-plus-rules (video only). The authors say VideoPhy-1's single combined task "may introduce evaluation bias, as annotators have access to the prompt while conducting the physical commonsense evaluation." Annotators saw the *original* prompt, not the upsampled one, so short-prompt models are not penalised.
- **Agreement 75–80%** across tasks — "reasonable given the task subjectivity and comparable to the agreement scores in prior work." No kappa is reported.
- **Metric.** Joint performance = fraction of videos with **SA ≥ 4 and PC ≥ 4**. The posterior P(PC ≥ 4 | SA ≥ 4) is deliberately *not* reported because a model that adheres to 1 of 1,000 prompts and happens to be physical on that one would score 100% (footnote 3).
- **Volume and cost.** Benchmark annotations: **10.2K SA, 10.2K PC, 30.6K rule** judgments for **$2,600**. Auto-evaluator training set: **~50K** annotations for **$3,515**. Table 1 totals **~6,800 generated videos** and **102K annotations**.

### Headline results (Table 2 — joint %, human-evaluated)

| Model | Class | All | Hard | Physical activities | Object interactions | n videos |
|---|---|---:|---:|---:|---:|---:|
| **Wan2.1-14B** | open | **32.6** | **21.9** | **31.5** | **36.2** | 590 |
| CogVideoX-5B | open | 25.0 | 0.0† | 24.6 | 26.1 | 590 |
| Cosmos-Diffusion-7B | open | 24.1 | 10.9 | 22.6 | 27.4 | 590 |
| HunyuanVideo-13B | open | 17.2 | 6.2 | 17.6 | 15.9 | 590 |
| VideoCrafter2 | open | 10.5 | 2.9 | 10.1 | 13.1 | 590 |
| Luma Ray2 | closed | 20.3 | 8.3 | 21.0 | 18.5 | 394 |
| Sora | closed | 23.3* | 5.3* | 22.2* | 26.7* | **60** |

\* Sora: 60 videos generated by hand in the Sora playground (no API), randomly drawn from the 590. Ray2: 2 prompts per action on API budget. The authors flag that "for closed models … we used fewer captions, which influences their evaluation outcomes."
† CogVideoX-5B's 0.0 on Hard is **by construction** — the hard subset is defined as the actions on which it scored zero.

- All videos are **< 6 s** (3–6 s, 320×512 to 832×480; Appendix Table 8). Hunyuan and VideoCrafter2 got the *original* captions because their CLIP text encoder caps at 77 tokens; the others got upsampled captions. Veo 2 and Kling were excluded for lack of API access.
- The abstract rounds the hard-subset figure to **22%**; Table 2 says 21.9%.
- Authors' reading: Wan's lead comes from diverse multimodal training data and motion filtering; **closed models "are not necessarily superior"**; Cosmos-7B's second place on Hard (beating the larger Hunyuan-13B) is attributed to human-action-heavy training data plus synthetic simulations. Sports/physical activities score "generally lower" than object interactions — true for Wan, CogVideoX, Cosmos and Sora, reversed for Hunyuan and Ray2.

### What physics is not correlated with (Table 3)

Pearson correlation of human scores with automated video metrics on the benchmark videos: SA vs LAION aesthetics **0.10**, PC vs aesthetics **0.09**; SA vs RAFT motion quality **0.02**, PC vs motion **0.002**; **SA vs PC 0.14**. "A model cannot achieve high performance on our dataset simply by optimizing for aesthetics and motion quality."

### Which laws are violated most (Fig. 5, §5.1)

Violation score per law = violated rules / all rules invoking that law, pooled across models. **Conservation of momentum (linear or angular) and conservation of mass: ~40%.** **Reflection and buoyancy: < 20%** ("relatively mastered"). Inertia, gravity, friction and elasticity lie between; the figure gives no numerals for them. Qualitative examples: a rock rolling and *accelerating uphill* (Wan, Fig. 7), a hot-air balloon shrinking and expelling water (Wan), a sledgehammer deforming after a swing and a broken board appearing from nowhere (Hunyuan), a javelin expelling sand before landing (Cosmos), a golf ball not moving after being struck (Ray2), a jetski moving backward (Ray2).

### VideoPhy-2-AutoEval (§3.3, §5.2, Appendix H)

- **VideoCon-Physics (7B)** — VideoPhy-1's evaluator — fine-tuned with **LoRA (r = α = 32, dropout 0.05) on ~50K human annotations** from videos of three models (HunyuanVideo, Cosmos, CogVideoX) over the 3,350 training prompts; multi-task with a shared backbone for SA (1–5), PC (1–5) and rule classification (0/1/2); 3 epochs, lr 5e-4, 4×A6000, batch 64.
- **Table 4 (Pearson × 100 vs human, SA / PC):** unseen prompts — AutoEval **47 / 37**; best baseline VideoCon-Physics 32 / 25; Gemini-2.0-Flash-Exp 26 / 11; VideoLLaVA 30 / 2; VideoScore 17 / 10. Unseen video models — AutoEval **45 / 37**; VideoCon-Physics 27 / 26; Gemini 31 / 11. The paper's relative gains: +47.4% / +49.0% average over the best baseline; **+81% (SA) and +236% (PC) over Gemini** on unseen prompts.
- **Table 5 (joint 0/1 prediction):** on unseen prompts AutoEval **accuracy 79.1, F1 51.1** vs VideoCon-Physics **75.6 / 2.6**; on unseen models **76.3 / 49.3** vs **75.0 / 4.2**. The VideoPhy-1 evaluator's ~75% accuracy with F1 ≈ 3 means it almost never predicts a positive on VideoPhy-2 videos and scores near the base rate. (The stated relative gain for unseen models is +49.1%; the printed averages give ≈ +58.6%. Minor, but do not re-quote that figure.)
- **Table 6 (rule classification accuracy, unseen prompts / unseen models):** random 34.5 / 31.2; VideoLLaVA 38.1 / 38.7; Gemini-2.0-Flash-Exp 59.2 / 57.1; **AutoEval 78.7 / 72.9**.
- The authors call it "reliable" and "robust"; the numbers say a Pearson of 0.37–0.47 with the human score, which is a moderate correlation at best.

### Versus VideoPhy-1 (Table 7, Appendix A.3)

| | VideoPhy (2024) | VideoPhy-2 |
|---|---|---|
| Prompts | 688 | **3,940** |
| Focus | material interactions (solid/fluid/…) | **real-world actions** |
| Human rating | 0–1 | **1–5 Likert** |
| SA and PC | one combined task | **two separate tasks; PC rater blind to prompt** |
| Physical-rule annotations | no | **yes, with laws** |
| Dense captions, hard subset | no | yes |
| Evaluator | VideoCon-Physics | VideoPhy-2-AutoEval (fine-tuned from it) |

Other rows of Table 7: VBench 1,746 prompts, EvalCrafter 700, Physics-IQ 396, PhyGenBench 160. The authors' critiques of neighbours: Physics-IQ (first-frame conditioning, similarity to ground-truth continuation) has unclear agreement with human judgment and doesn't extend to multi-event scenes; PhyGenBench's one-prompt-one-law mapping breaks when a model fails the prompt but obeys physics; WorldSimBench's numerical-solver ground truth inherits the sim-to-real gap.

### Stated limitations and hedges

There is no limitations section. What the paper hedges itself: the Sora asterisk (n = 60) and the reduced Ray2 set; annotator agreement of 75–80% "given the task subjectivity"; LLM-generated rules "may not always be visually grounded" (hence CBD); rule generation direct from video "did not yield high-quality outputs"; two models could not receive the dense captions; videos are deliberately short "as they are easier to evaluate." Unhedged but worth knowing: the physical-rule vocabulary is a fixed list seeded in the prompt (gravity, buoyancy, elasticity, friction, conservation of mass, reflection, refraction, …) with "other well-known laws acceptable"; every rule, caption, dedup pass and free-text-to-rule conversion goes through the same Gemini-2.0-Flash-Exp; and the hard subset is defined relative to one open model.

## Reading it against the wiki

> [!note] Correction to the evaluation table
> [World-model evaluation](../concepts/world-models/world-model-evaluation.md) lists VideoPhy in a row described as "physical commonsense in generated video, via **automated metrics or model-based critics**." That is the wrong emphasis for VideoPhy-2: its gold standard is **102K human annotations by three raters per video**, and the automatic evaluator is a distilled convenience whose correlation with those humans it reports (0.37–0.47). Physical rules are LLM-*proposed* but human-*verified*. The row should read "human-rated, with a fine-tuned VLM auto-rater." The [physical-reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) page's "human annotation or a model judge" is accurate.

- **Same finding as [Physion-Eval](physion-eval-paper.md), a year earlier, from the other direction.** Physion-Eval (2026) shows frontier MLLM critics far below untrained humans at spotting glitches and blames the visual encoder. VideoPhy-2 (2025) measured the same thing with a correlation: Gemini-2.0-Flash-Exp reaches **r = 0.11** with human physical-commonsense ratings, and the fix it tries — fine-tuning a 7B video-LM on 50K human labels — gets to **0.37**. That is the experiment Physion-Eval's open question asks for ("a critic trained on the benchmark's own traces"), already run, with a result that is better than zero-shot and still weak. The wiki's [world-model evaluation](../concepts/world-models/world-model-evaluation.md) claim that "the automated benchmark layer is itself unvalidated" now has a counterexample in the sense that this layer *was* validated — and found wanting by its own authors' numbers.
- **The r = 0.360 pattern, again.** Table 3's correlations (PC vs aesthetics 0.09, vs motion 0.002, vs prompt adherence 0.14) are the video-generation form of [WorldArena](worldarena-paper.md)'s perceptual-vs-planning r = 0.360 and [VP²](vp2-paper.md)'s FVD-vs-control dissociation: looking good, following the prompt, and obeying physics are three nearly independent axes. VideoPhy-2's joint metric is a deliberate response — it refuses to let a model buy a physics score with prompt-ignoring pretty video, which is exactly the failure the posterior metric (and PhyGenBench's one-law prompts) would reward.
- **Open beats closed, twice.** Wan2.1-14B above Sora and Ray2 here; Wan 2.2 cleanest egocentric in Physion-Eval while the commercial models sat at 96–97.5% glitch rate. Two benchmarks, two Wan generations, same direction. Physion-Eval's aesthetic-optimisation hypothesis gains a data point but not a test; VideoPhy-2 only offers "diverse training data and motion filtering." The Sora comparison here rests on 60 videos, so treat it as suggestive.
- **Conservation laws are the soft spot.** ~40% violation for mass and momentum is the quantitative version of the [HAI brief](hai-world-model-spatial-intelligence-brief.md)'s "visual plausibility trap" and of Physion-Eval's worked example (ice gaining volume while melting). For the generative-video side of [world-model simulators](../concepts/world-models/world-model-simulators.md) this is the specific thing that will corrupt a policy trained on rollouts: objects appearing, mass changing, momentum not transferring on contact. Reflection and buoyancy being "mastered" is consistent with them being appearance-level regularities a pixel model can learn from stills.
- **Closest thing in the wiki to a manipulation-primitive physics test.** The 54 object-interaction actions come from Something-Something v2 and read like a contact-physics curriculum (*poking a stack so it collapses*, *putting something upright that can't stand so it falls*, *lifting a surface until something slides*). No robot appears anywhere, and the evaluation is of human-actor video, but if one wanted to score a [Cosmos](../entities/nvidia-cosmos.md)-class generator on the physics a household robot depends on, this list is a better starting vocabulary than any robot benchmark the wiki has. Cosmos-Diffusion-7B (the January 2025 Cosmos-1 generation) scoring 24.1 / 10.9 here is the only external human-rated physics number for that lineage in the wiki.
- **Sample sizes, by the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline.** 590 videos per open model: a 32.6% proportion carries roughly ±3.8 pp at 95%, so Wan vs CogVideoX (32.6 vs 25.0) is real and Cosmos vs CogVideoX (24.1 vs 25.0) is not. The hard-subset test cells are ~180 videos per model (60 actions × 3 test captions — my arithmetic, not the paper's), so 21.9 vs 10.9 is real and 8.3 vs 6.2 vs 5.3 is noise. Sora's 60 videos give ±~11 pp; the paper's asterisk is warranted. The [LLM-as-annotator loop](../concepts/learning/embodied-reasoning-vlms.md) is also worth noticing: Gemini-2.0-Flash-Exp writes the prompts, captions the videos, writes the rules, rewrites the human free-text violations, and is then a baseline judged against the labels it helped shape.

## Entities mentioned

- **Hritik Bansal, Clark Peng, Yonatan Bitton, Roman Goldenberg, Aditya Grover, Kai-Wei Chang** — UCLA and Google Research (no pages).
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — Cosmos-Diffusion-7B evaluated; its Mistral-NeMo-12B prompt upsampler reused; second-best on the hard subset.
- [OpenAI](../entities/openai.md) — Sora, evaluated on 60 hand-generated videos.
- [Google DeepMind](../entities/google-deepmind.md) — Gemini-2.0-Flash-Exp is the LLM/VLM throughout the pipeline and a judge baseline; [Veo](../entities/veo.md) 2 excluded for lack of API.
- Wan2.1-14B (Alibaba), CogVideoX-5B, HunyuanVideo-13B (Tencent), VideoCrafter2, Luma Ray2, Kling — evaluated or excluded; no pages.
- VideoCon-Physics / VideoCon, VideoLLaVA, VideoScore — evaluator baselines; no pages.

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the benchmark landscape this belongs to; see the correction above.
- [Physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) — the generative-video column of the two-traditions table; VideoPhy-2 adds a per-law violation rate to the metric list.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — the paper's own framing is video generators as "general-purpose physical world simulators."
- [Generative video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md) — the hallucination failure mode of Paradigm A, measured per law.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the joint-metric and posterior-metric argument transfers directly.
- [VideoPhy (2024)](videophy-paper.md) — the predecessor.

## Open questions

- **Does the per-law breakdown transfer to robot-relevant video?** All 197 actions are human sports and object handling; nobody has run a robot-conditioned generator (DreamGen, Genie Envisioner, Cosmos-Predict) through the rule-annotation protocol.
- **Where did SA and PC come apart?** r = 0.14 between them is remarkably low. Are the physically best videos the ones that ignored the multi-event prompt and did something simpler?
- **Is the 0.37 ceiling the encoder?** Physion-Eval says yes for zero-shot critics; VideoPhy-2's fine-tuning lifted PC correlation from 0.25 to 0.37, which is consistent with either story. A video-native encoder trained on these 50K labels is the missing experiment.
- **How much of the hard subset is CogVideoX-specific?** It was selected against one model; the fact that every other model also drops is evidence it generalises, but Wan's Hard/All ratio (0.67) is much better than Cosmos's (0.45), so "hard" is not uniformly hard.
- **Does a 2025 snapshot still hold?** The models are Wan 2.1, Sora 1, Cosmos-1. Physion-Eval's 2026 generation (Sora 2, Veo 3.1, Wan 2.2) still failed 83–93% of clips under a stricter protocol, so the ordering may have survived while the absolute numbers moved.
