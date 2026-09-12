---
title: PhyGenBench — Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation (Meng, Liao et al.; 2024)
type: source
url: https://arxiv.org/abs/2410.05363
fetch_url: https://arxiv.org/pdf/2410.05363v1
author: Fanqing Meng, Jiaqi Liao, Xinyu Tan, Wenqi Shao, Quanfeng Lu, Kaipeng Zhang, Yu Cheng, Dianqi Li, Yu Qiao, Ping Luo
published: 2024-10-07
ingested: 2026-09-11
venue: arXiv v1 (technical report) — Shanghai Jiao Tong University / OpenGVLab, Shanghai AI Laboratory / University of Hong Kong / CUHK
local_path: raw/2410.05363v1.pdf
sha256: f7492a30a8364fb4bfdc6be9e594410710907d761ce603acfad8f1a77842e5dd
format: pdf (23 pp. incl. appendix, 9 figures, 12 tables)
tags: [phygenbench, phygeneval, video-generation, text-to-video, physical-commonsense, intuitive-physics, world-simulator, benchmark, vlm-judge, llm-judge, gpt-4o, vqascore, kling, gen-3, pika, cogvideox, open-sora, opengvlab, shanghai-ai-lab]
---

## Summary

The first benchmark in this wiki that asks a text-to-video model a physics question with a **known answer**. OpenGVLab's premise is the one Sora made fashionable — that T2V generation is "a promising path towards constructing the universal world simulator" — and its test is deliberately elementary: 160 prompts, each engineered to exercise exactly one of **27 textbook physical laws** across four domains (mechanics, optics, thermal, material properties), where the correct outcome is unambiguous — the stone sinks, the egg breaks, the copper burns green. The evaluator, **PhyGenEval**, is a three-tier pipeline that does not ask a VLM "is this physically plausible?" — the paper shows that question yields near-zero human correlation — but instead has **GPT-4o read the law and write the questions**, then routes them to image-, multi-image-, and video-level VLMs in turn. Against three human annotators the ensemble reaches **Spearman ρ = 0.81** where VideoPhy manages 0.04. The headline: the best model tested, Runway's **Gen-3, scores 0.51** on physical commonsense; every open-source model lands 0.36–0.45; Kling 0.49. Scaling CogVideoX from 2B to 5B moves the average 0.39 → 0.45 and mechanics 0.38 → 0.39; rewriting prompts to spell out the expected outcome buys Kling 0.07; a visual-quality enhancer that lifts Vchitect above Kling on VBench moves its physics score by **0.00**. The authors' conclusion is that dynamics — not appearance — is where these models fail, and that scaling and prompting do not reach it.

## Key claims

### Benchmark design (§3, Appendix A)

- **160 prompts, 27 laws, 4 domains** (Table 3): Mechanics — 7 laws (gravity, buoyancy, solid pressure, atmospheric pressure, elasticity, friction, surface tension), 40 prompts; Optics — 6 (reflection, refraction, scattering, dispersion, interference & diffraction, straight-line propagation), 50 prompts; Thermal — 6 phase transitions (solidification, melting, liquefaction, boiling, deposition, sublimation), 30 prompts; Material Properties — 5 physical (color, hardness, solubility, combustibility, flame reaction) + 3 chemical (acidity, redox, dehydration), 40 prompts. 165 unique objects, 42 unique actions, mean caption length 18.75 words.
- **One law per prompt, by construction.** "Multiple physical laws could be included in a single prompt, which may bring confusion … even for human annotators. To avoid this, we carefully curate prompts to ensure a one-to-one correspondence." The law is an annotation shipped with the prompt and is an *input* to the evaluator.
- **Five-step pipeline** (Fig. 2b): conceptualization from Halliday-Resnick-style textbook physics → manual prompt writing → GPT-4o augmentation with object/action detail, "carefully designed to avoid revealing the expected physical phenomenon" → GPT-4o object substitution for diversity (egg → vase, glass bottle; rock → wall, metal) → manual quality control, including a check that current T2V models can render the scene semantically at all.
- **Why not VideoPhy** (Appendix A.2): VideoPhy's 688 prompts cover solid–solid / solid–fluid / fluid–fluid interactions with **no physical-law annotation**, and its prompts are terse and sometimes unrenderable ("The wristwatch knob winds the inner spring tightly"). On a 64-prompt sample, semantic-alignment scores average **0.80 on PhyGenBench vs 0.63 on VideoPhy** (Table 4; CogVideoX-5B 0.78 vs 0.48, Vchitect 0.84 vs 0.63, Kling 0.89 vs 0.77) — the argument being that you cannot grade physics in a video that failed to depict the scene.
- Definitions the paper adopts (after Swartz 1985): *physical commonsense* = intuitive everyday understanding; *physical law* = universal principle; *physical phenomenon* = the observable event. And, following the intuitive-physics literature, the target is "visually and interactively natural to humans, rather than … strict physical accuracy."

### PhyGenEval (§4, Appendix B)

Two scores, each on a 0–3 scale and reported normalised to 0–1: **SA** (semantic alignment — are the objects and the action there?) and **PCA** (physical commonsense alignment — did the law play out?). SA is a two-stage GPT-4o pass: extract objects and actions from the prompt, then check the video for object presence (0–2) and action occurrence (0/1). PCA is the contribution, a three-tier hierarchy from single frame to whole video:

| Stage | Question | Who writes the question | Frame retrieval | Who answers |
|---|---|---|---|---|
| **1. Key physical phenomena detection** | Does the expected outcome appear in the keyframe? ("Is the egg broken?") | GPT-4o, from prompt + law: a retrieval prompt *p_r* plus affirmative/negative statement pairs | CLIPScore locates keyframe *I_i*; a 5-frame window *i−2…i+2* is scored | **VQAScore** (single image) — ratio of affirmative to affirmative+negative VQA score |
| **2. Physics order verification** | Is causality in the right order? q1: first → key; q2: key → last; q3: first–key–last | GPT-4o: retrieval prompt + three questions | CLIPScore keyframe, windowed | **GPT-4o or LLaVA-Interleave** (multi-image yes/no) |
| **3. Overall naturalness** | Four-option rubric from "Completely Fantastical" to "Almost Realistic" | GPT-4o rewrites DEVIL's generic rubric into a **prompt-specific** standard *g_spec* | whole video | **InternVideo2 or GPT-4o** (video VLM) |

- Each stage is discretised to 0–3, the three are averaged and **floored** to give the final score. Non-monotonic processes (egg hits rock) get both an intermediate and a last-frame question; monotonic ones (melting) get only the last frame. A correct keyframe with the wrong outcome scores zero — retrieval accuracy alone earns nothing.
- Stage 2 rests on an explicit assumption: current models "generally maintain outcome consistency (e.g., the egg would not reassemble itself after it is broken)," so ordering can be checked from keyframes rather than every frame.
- The final PhyGenEval score is an **ensemble of a GPT-4o route and an open-source route** (LLaVA-Interleave + InternVideo2); the authors recommend running both, calling the cost "acceptable" given the benchmark's size.

### Agreement with human judgment (§5, Table 1, Appendix C)

- **Human study: 64 prompts × 8 models = 512 videos, 3 annotators**, each giving integer 0–3 SA and PCA scores against the rubric in Fig. 9; scores are averaged and "rounded up." No inter-annotator agreement statistic is reported.
- **PCA correlation with humans, overall:** PhyGenEval **Kendall τ 0.78 / Spearman ρ 0.81**; DEVIL 0.17 / 0.18; VideoScore 0.17 / 0.19; **VideoPhy 0.03 / 0.04**. Per domain PhyGenEval ranges τ 0.72 (mechanics) to 0.81 (material).
- **SA correlation** (Table 6): PhyGenEval τ 0.53 / ρ 0.56 vs Grid-LLaVA (T2V-CompBench) 0.35 / 0.39, VideoPhy 0.13 / 0.17, VideoScore 0.05 / 0.05. Swapping GPT-4o for Grid-LLaVA inside PhyGenEval's own two-stage scheme drops it to 0.42 / 0.44 — the decomposition and the judge each contribute.
- **Ablations, all reported as human correlation (Tables 8–10):**
  - Each stage alone: keyframe-only τ 0.56, order-only 0.55, naturalness-only 0.42; all three together **0.78**. Every pair is worse than the triple.
  - Open-source-only route τ 0.62 / ρ 0.66; GPT-4o-only 0.66 / 0.71; ensemble 0.78 / 0.81.
  - **The naturalness stage without the LLM-written rubric is close to useless.** Reconstructing the column-garbled Table 8: with a single generic rubric applied to every video (DEVIL's method), InternVideo2 correlates at τ ≈ −0.10 and GPT-4o at ≈ 0.19 overall; with GPT-4o first rewriting the rubric per prompt, InternVideo2 rises only to ≈ 0.07 while GPT-4o reaches ≈ 0.53. (Read the ordering, not the third decimal — the table's columns did not survive extraction cleanly.)
- Case studies (Fig. 4): VideoScore and DEVIL rate an egg bouncing off a rock "like rubber" as physically correct (3/3), a rock floating on water as correct, and none of the three baselines can catch a red copper flame — "they cannot incorporate domain-specific physical commonsense."

### Results (§5, Table 2 — PCA, 0–1; "Human" is the 64-prompt subset)

| Model | Size | Mechanics | Optics | Thermal | Material | **Average** | Human |
|---|---|---:|---:|---:|---:|---:|---:|
| **Gen-3** (Runway) | — | 0.45 | 0.57 | 0.49 | **0.51** | **0.51** | **0.48** |
| **Kling** (Kuaishou) | — | 0.45 | **0.58** | **0.50** | 0.40 | 0.49 | 0.44 |
| CogVideoX | 5B | 0.39 | 0.55 | 0.40 | 0.42 | 0.45 | 0.37 |
| Vchitect 2.0 | 2B | 0.41 | 0.56 | 0.44 | 0.37 | 0.45 | 0.36 |
| Open-Sora V1.2 | 1.1B | 0.43 | 0.50 | 0.44 | 0.37 | 0.44 | 0.35 |
| Pika | — | 0.35 | 0.56 | 0.43 | 0.39 | 0.44 | 0.36 |
| CogVideoX | 2B | 0.38 | 0.43 | 0.34 | 0.39 | 0.39 | 0.31 |
| Lavie | 860M | 0.30 | 0.44 | 0.38 | 0.32 | 0.36 | 0.30 |

- "Even the best-performing model, Gen-3, only attains a PCA score of 0.51 … current T2V models struggle to generate videos that comply with intuitive physics."
- **Optics is easiest for everyone** — the authors attribute this to "abundant and explicit representation of optical knowledge in pre-training datasets." Vchitect 2.0 and CogVideoX-5B match the closed models on optics and both beat Pika overall; Lavie is lowest in every column.
- **Semantic alignment is high across the board** (Table 7, human SA: Kling 0.89, Gen-3 0.86, Vchitect 0.84, down to Lavie 0.55) — the scenes render; the physics doesn't. Qualitatively (Fig. 5): every model fails the glass ball sinking in a bathtub (Open-Sora and Gen-3 leave it suspended); CogVideoX makes melting ice cream *grow*; only Gen-3 shows partial dry-ice sublimation; every model fails the egg-on-rock, Kling rendering it as a rubber bounce; no model gets the sulfuric-acid-on-bread carbonisation.
- Test conditions differ by model (Table 5): Gen-3 was evaluated on 11 s, 24 fps, 1280×768 clips; Pika on 3 s; CogVideoX-5B on 6 s at 8 fps and 640×360. The paper does not discuss whether clip length or frame rate interacts with the keyframe-window evaluator.

### Scaling, prompting, and enhancement don't fix it (§6, Appendix D)

- **Scaling (Table 2, Fig. 7):** CogVideoX 2B → 5B lifts the average **0.39 → 0.45** but mechanics only **0.38 → 0.39**. Qualitatively the larger model fixes *static* phenomena (thin-film interference on bubbles, rust on iron, a more realistic boil) and still cannot bounce a football. "While scaling up enhances the model's capacity to generate videos that align with physical commonsense for individual objects, it may be insufficient for physical phenomenons involving dynamic physical laws. Addressing these challenges likely requires extensive training on carefully curated synthetic data" (citing PhysGen).
- **Prompt rewriting (Table 11):** appending the expected outcome to each prompt ("…the egg shatters, breaking apart") raises CogVideoX-5B **0.45 → 0.52** and Kling **0.49 → 0.56**; CogVideoX-5B's mechanics stays at 0.39. Rewriting "only solves a few simple issues (e.g., flame color)" — the egg still doesn't break, the stone still doesn't sink (Fig. 8).
- **Visual enhancement (Table 12):** VEnhancer-processed Vchitect 2.0 "even surpass[es] Kling" on VBench, and scores **0.45 → 0.45** on PhyGenBench; Spearman 0.86 between per-model scores before and after. The authors read this as evidence PhyGenEval is measuring physics and not quality — and that a better VBench rank "doesn't necessarily imply a better understanding of physical common sense."

### Stated limitations

The paper has no limitations section. What it concedes in passing: the benchmark is "relatively small" (offered as the reason GPT-4o's cost is tolerable); single judge models carry "potential biases," which is why two routes are ensembled; the order-verification stage depends on the outcome-consistency assumption above; and the intuitive-physics target is naturalness to a human viewer rather than physical accuracy. Not addressed: annotator agreement, sensitivity of the CLIPScore keyframe retrieval, whether GPT-4o's question-writing is itself correct on the chemistry items, or whether the evaluator generalises to prompts without a shipped law annotation.

## Reading it against the wiki

> [!note] The judge is handed the answer key — and that is the finding
> The [world-model evaluation](../concepts/world-models/world-model-evaluation.md) page carries [Physion-Eval](physion-eval-paper.md)'s result that MLLM critics are 2–6× less sensitive than untrained humans at spotting physics violations, and this paper's ρ = 0.81 looks like a contradiction. It is not, and the ablation says why. PhyGenEval never asks a VLM to *find* the violation. It ships a one-law annotation with every prompt, has GPT-4o convert the law into yes/no questions with a known answer, and lets the vision model do only the lookup. The closest thing in the paper to an unscaffolded critic — the naturalness stage with a generic rubric — correlates at τ ≈ −0.10 (InternVideo2) to 0.19 (GPT-4o), which is Physion-Eval's number from the other side. So the two sources agree on the mechanism: **language-side reasoning about physics works; vision-side detection of physics does not**, and PhyGenEval is an architecture for routing as much of the job as possible to the former. The price is that it only runs on prompts whose physics is declared in advance. It cannot grade a video whose physics nobody wrote down, which is every video a robot's world model will ever produce.

- **The VEnhancer result is the visual-plausibility trap, measured, two years before the [HAI brief](hai-world-model-spatial-intelligence-brief.md) named it.** A post-processor that raises a model's VBench rank above Kling changes its physics score by nothing. That is the same dissociation [WorldArena](worldarena-paper.md) later quantified (perceptual score vs action planning, r = 0.360) and [VP²](vp2-paper.md) found earlier with task-dependent sign — with the difference that here the intervention *only* touched appearance, so the decoupling is clean rather than correlational. Worth citing on [perception-distortion](../concepts/world-models/perception-distortion-tradeoff.md) as the generator-side instance.
- **Optics-easy, mechanics-hard is the same split as [generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) predicts.** Reflection, refraction and bubble interference are properties of a *frame*; buoyancy, elasticity and breakage are properties of a *trajectory*. Every model in Table 2 scores highest on the frame-property domain and the authors' scaling analysis lands on the same line: 5B fixes rust and bubbles, not the bouncing ball. The data-abundance explanation they offer (optics is over-represented in pretraining) is plausible but untested; the alternative — that appearance is what a per-frame denoising objective optimises and dynamics is what it merely inherits — is the wiki's standing hypothesis and fits the same numbers.
- **On [physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md), this belongs in the generative-video column, but note what it borrows and what it drops.** The introduction cites Battaglia–Hamrick–[Tenenbaum](../entities/josh-tenenbaum.md) 2013 and infant object-permanence work as motivation, then uses none of that tradition's method: humans here are *annotators*, never *subjects*; there is no human performance baseline on the task and no attempt budget, because generation is a single shot. It is the "physical judgment" side of that page's judgment-vs-problem-solving split, applied to a generator's output.
- **The scaling result is weaker than the abstract makes it sound, and the wiki should quote it with its size.** One model family, two sizes, 0.39 → 0.45. That is consistent with [VP²](vp2-paper.md)'s no-trend-from-6M-to-300M and with the [VLA scaling](../concepts/learning/scaling-laws-vla.md) page's scepticism, but it is n = 1 pair on a 160-prompt benchmark; the qualitative static-vs-dynamic split (Fig. 7) is the more durable claim. The proposed remedy — "extensive training on carefully curated synthetic data" — is the [synthetic flywheel](../concepts/learning/synthetic-data-flywheel.md) argument made from the benchmark side.
- **Sample sizes.** 160 prompts total, 30–50 per domain; the human-correlation study is 64 prompts × 8 models, three annotators, no agreement statistic. By the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline the 0.51-vs-0.49 Gen-3/Kling gap is noise and 0.51-vs-0.36 Gen-3/Lavie is real; the per-domain numbers rest on 30–50 clips each and should be read as ordering only.

## Entities mentioned

- **Runway Gen-3, Kuaishou Kling, Pika** (proprietary; no pages) and **CogVideoX 2B/5B (Zhipu), Open-Sora V1.2 (HPC-AI), Lavie, Vchitect 2.0 (Shanghai AI Lab)** (open; no pages) — the eight evaluated models.
- **OpenGVLab / Shanghai AI Laboratory**, Shanghai Jiao Tong University, University of Hong Kong, CUHK — no pages. Corresponding authors Wenqi Shao and Ping Luo.
- [OpenAI](../entities/openai.md) — Sora as the framing example of "T2V as world simulator"; GPT-4o as the question-writer and one of the judges throughout. GPT-4V is named once (Appendix B.2) for the order-verification yes/no.
- [Physion-Eval](../entities/physion-eval.md), [WorldArena](../entities/worldarena.md) — later benchmarks this page is read against (not cited by the paper).
- [Josh Tenenbaum](../entities/josh-tenenbaum.md) — Battaglia et al. 2013 cited as the intuitive-physics-engine motivation.
- Baseline evaluators: VideoPhy (Bansal et al. 2024), VideoScore / MantisScore, DEVIL (Gemini 1.5 Pro-based naturalness), Grid-LLaVA (T2V-CompBench), VQAScore (Lin et al. 2024), LLaVA-Interleave, InternVideo2, VEnhancer — no pages.

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — this is the "PhyGenBench" row of that page's landscape table, now read; an LLM-scaffolded VLM judge on declared-law prompts.
- [Physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) — generative-video tradition; borrows the cognitive-science motivation without the human-baseline method.
- [Perception-distortion tradeoff](../concepts/world-models/perception-distortion-tradeoff.md) — the VEnhancer null result as the generator-side decoupling of appearance from physics.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) and [world model](../concepts/world-models/world-model.md) — the "T2V → world simulator" framing the paper tests and finds wanting.
- [Embodied reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) — the judge-side evidence that VLM physics competence lives in the language model, not the visual encoder.
- [Scaling laws (VLA)](../concepts/learning/scaling-laws-vla.md), [synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md) — the scaling null and the proposed synthetic-data remedy.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md), [what world models are measurably good for](../syntheses/world-models/what-world-models-are-measurably-good-for.md).

## Open questions

- How much of the ρ = 0.81 is the *law annotation* rather than the pipeline? The obvious ablation — run PhyGenEval with the law field blanked and GPT-4o guessing the physics from the prompt alone — is not in the paper, and it is the one that would say whether this evaluator could ever score an undeclared scene.
- Is the naturalness stage still worth its cost? Alone it is the weakest tier (τ 0.42) and its open-source variant is near zero; the paper keeps it because the triple beats every pair, but does not report the triple without the InternVideo2 half.
- Three annotators, no agreement statistic, scores "rounded up" — what is the human ceiling on this rubric, and is 0.81 close to it?
- Clip length and frame rate vary from 3 s / 8 fps to 11 s / 30 fps across the models in Table 5. A keyframe-window evaluator (five frames around a CLIP retrieval) samples very different fractions of those clips. Does Gen-3's lead survive matched clip length?
- The chemistry items (dehydration, redox, flame reaction) require the *judge* to know that copper burns green and sulfuric acid carbonises bread. GPT-4o writes those questions. Nothing checks that its chemistry is right.
- The paper's prescription — curated synthetic physics data — is the [Cosmos](../entities/nvidia-cosmos.md)-era bet. Has any later PhyGenBench result on a synthetic-data-heavy generator confirmed or falsified it? Not in the wiki as of this ingest.
