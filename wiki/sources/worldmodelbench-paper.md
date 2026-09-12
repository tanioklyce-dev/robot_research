---
title: WorldModelBench — Judging Video Generation Models as World Models (Li, Fang et al.; 2025)
type: source
url: https://arxiv.org/abs/2502.20694
fetch_url: https://arxiv.org/pdf/2502.20694v1
author: Dacheng Li, Yunhao Fang, Yukang Chen, Shuo Yang, Shiyi Cao, Justin Wong, Michael Luo, Xiaolong Wang, Hongxu Yin, Joseph E. Gonzalez, Ion Stoica, Song Han, Yao Lu
published: 2025-02-28
ingested: 2026-09-11
venue: arXiv v1 (UC Berkeley, UC San Diego, NVIDIA, MIT)
local_path: raw/2502.20694v1.pdf
sha256: 06d9fc1ba30f12e751b2e38f17ce591118575c7d10bf19720b70c2f73ccf7e4d
format: pdf (11 pp. incl. supplementary, 11 figures, 9 tables)
tags: [worldmodelbench, world-model-evaluation, benchmark, video-generation, physics-adherence, instruction-following, human-annotation, vlm-as-a-judge, reward-model, vader, kling, mochi, cogvideox, open-sora, nvidia, berkeley, mit, vila]
---

## Summary

The first benchmark to say out loud that a video generator claiming to be a **world model** should be judged on whether its futures are *feasible*, not whether they are pretty. WorldModelBench is **350 text + first-frame condition pairs** across **7 application domains** (robotics, autonomous driving, human activities, industry, natural scenes, gaming, animation) and **56 subdomains**, each generated video scored out of **10** on three dimensions: **instruction following** (0–3, four levels), **commonsense** (0–2, frame-wise and temporal quality, borrowed from VBench), and **physics adherence** (0–5, one binary flag each for Newton's first law, mass conservation/solid deformation, fluid mechanics, impenetrability, gravity). The authors collected **8,336 complete crowd votes (67K labels, 65 voters)** over **14 models**, then fine-tuned a **2B-parameter VLM judge (VILA-2B)** on them — the paper's headline is that this small judge predicts human world-modeling labels with lower error than GPT-4o, and that using it as a differentiable reward (VADER-style) on Open-Sora 1.2 "noticeably" improves the generator. The measurement results are the durable part: the best model (Kling v1.5) fully completes only **61%** of instructed tasks, **12%** of its videos violate mass conservation, VBench's aggregate ranking correlates only **0.28** with physics adherence, and every image-to-video model scores below its text-to-video sibling. The reward-fine-tuning result is **qualitative only** (Figures 8, 11); the paper itself calls it "positive signs" and "promising signals," and it should be read that way.

## Key claims

### The benchmark (§3)

- **350 instances = 7 domains × 50 samples**, drawn from 5–10 subdomains per domain (Figure 3; 56 subdomains total). Both **T2V and I2V** are supported — the image condition is the first frame of a reference video, and the text prompt is a GPT-4o caption of "the difference between the first frame and the subsequent frames." Reference videos: driving from [nuScenes](../entities/nuscenes.md), robotics from [Open X-Embodiment](../entities/open-x-embodiment.md), human activities from ActivityNet, everything else keyword-filtered from OpenVid-1M. All 350 pairs were manually verified (§3.2).
- **Scoring rubric (§3.1), total 0–10:**
  - *Instruction following*, 0–3: **L0** subject absent or stationary; **L1** moves but wrong action (car told to turn left turns right); **L2** partial (hand moves toward shoulder, never touches); **L3** fully completes.
  - *Commonsense*, 0–2: frame-wise quality (0/1) and temporal quality (0/1 — flicker, choppy motion, objects appearing/disappearing). Explicitly "not the main focus" but "a prerequisite."
  - *Physics adherence*, 0–5, one binary per law: (1) Newton's first law — no motion without force; (2) conservation of mass / solid mechanics — no irregular deformation; (3) fluid mechanics; (4) impenetrability; (5) gravitation — no floating. The five were "selected based on common failures of contemporary models" and VideoPhy's findings.
- **Positioning (Table 1):** VBench has 946 prompts and no human labels; VideoArena 1,500 prompts / 30K labels, unreleased; VideoPhy 688 prompts / 73K labels, unreleased, physics scored 0/1 with no I2V support; WorldModelBench 350 / 67K, **labels released**, I2V supported. The authors' criticism of VideoPhy is that daily-object interactions "are not the most relevant domains to world models" — hence the application-driven domain list.
- **WorldModelBench-Hard:** the **45 prompts** with the lowest average score across the five closed models. Kling drops **9.08 → 7.87** (judge scores, Table 8); OpenSora-I2V 5.82 → 4.71.

### Human annotation (§3.3, Table 2)

- **8,336 complete votes** from **65 voters**, **1.70 votes per video**, each vote a dense 8-label annotation (1 + 2 + 5) → **67K labels**.
- Agreement: **87.1%** of votes on the same video are within ±2 total points; converted to pairwise win/loss, **70.0%** agreement (the authors compare this to 70–75% in VideoPhy and 72.8–83.1% in Chatbot Arena). Ten "at least CS PhD level" experts define a ±1σ band; **96.2%** of expert and **95.4%** of crowd votes fall inside it.

### Results on 14 models (§4.1, Table 3 — human scores)

Open: OpenSora-v1.2 (T2V, I2V), OpenSora-Plan-v1.3 (T2V, I2V), T2V-Turbo-v2, CogVideoX-5B (T2V, I2V), Pandora, Mochi. Closed: Luma 1.6, Runway Gen-3, MiniMax, Kling v1.5, and Mochi via API ("Mochi-official"). Open models run at the vendors' recommended settings (Appendix 8.3).

| Model | Instr. (0–3) | Frame | Temporal | Newton | Mass | Fluid | Penetr. | Grav. | **Total (0–10)** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Kling v1.5 | 2.36 | 0.94 | 0.92 | 0.93 | 0.88 | 0.96 | 0.89 | 0.93 | **8.82** |
| MiniMax | 2.29 | 0.91 | 0.88 | 0.93 | 0.81 | 0.96 | 0.86 | 0.94 | 8.59 |
| Mochi-official | 2.01 | 0.89 | 0.83 | 0.94 | 0.82 | **0.99** | **0.92** | **0.98** | 8.37 |
| Runway Gen-3 | 2.15 | 0.87 | 0.78 | 0.91 | 0.69 | 0.94 | 0.82 | 0.91 | 8.08 |
| Luma 1.6 | 2.01 | 0.81 | 0.76 | 0.89 | 0.62 | 0.95 | 0.77 | 0.90 | 7.72 |
| Mochi (open) | 2.22 | 0.63 | 0.63 | 0.94 | 0.58 | 0.97 | 0.71 | 0.94 | 7.62 |
| OpenSora-Plan T2V | 1.79 | 0.70 | 0.77 | 0.90 | 0.66 | 0.97 | 0.89 | 0.93 | 7.61 |
| CogVideoX-5B T2V | 2.11 | 0.60 | 0.51 | 0.91 | 0.52 | 0.96 | 0.74 | 0.95 | 7.31 |
| CogVideoX-5B I2V | 1.89 | 0.56 | 0.43 | 0.87 | 0.43 | 0.96 | 0.66 | 0.96 | 6.75 |
| OpenSora-Plan I2V | 1.77 | 0.47 | 0.54 | 0.84 | 0.42 | 0.97 | 0.70 | 0.92 | 6.62 |
| Pandora | 1.56 | 0.42 | 0.53 | 0.91 | 0.50 | 0.96 | 0.74 | 0.94 | 6.57 |
| T2V-Turbo-v2 | 1.33 | 0.49 | 0.43 | 0.88 | 0.42 | 0.96 | 0.75 | 0.96 | 6.22 |
| OpenSora T2V | 1.71 | 0.40 | 0.33 | 0.89 | 0.32 | 0.95 | 0.60 | 0.92 | 6.11 |
| OpenSora I2V | 1.60 | 0.37 | 0.25 | 0.90 | 0.25 | 0.92 | 0.60 | 0.94 | 5.83 |

The authors' four observations:

- **"Large gap to ideal video world model."** Kling, the top model, has **61%** of videos fully completing the instructed task; **12%** violate mass conservation and **11%** show objects penetrating each other.
- **Better commonsense does not mean a better world model.** Luma beats open Mochi on frame quality (0.81 vs 0.63) and temporal quality (0.76 vs 0.63), yet finishes the task in **44% vs 53%** of videos, with physics essentially tied (**4.13 vs 4.14** of 5).
- **I2V is worse than T2V for all three sibling pairs:** CogVideoX 7.31 vs 6.75, OpenSora-Plan 7.62 vs 6.62, OpenSora 6.11 vs 5.83 — "insufficient tuning on I2V models."
- **Top open models are competitive:** Mochi 7.62 and OpenSora-Plan 7.61 versus Luma 7.72.
- Also: a **tradeoff across dimensions** — Mochi-official has the highest physics adherence but a mid-pack instruction score. Pairwise Bradley–Terry Elo (Figure 6; 100 bootstrap rounds, OpenSora anchored at 800) gives the same overall ordering; on the physics-only Elo, Mochi-official tops Kling.
- **Where models fail (Figure 7 heatmap):** "most models suffer from autonomous driving, human activities and robotics" — throwing, jumping, a robot arm opening something — and do well on natural scenes (plants, animals, water). The three decision-relevant domains are the three hardest.

### The fine-tuned judge (§3.3, §4.2, Appendix 8.4)

- **Setup.** Each vote becomes 8 QA pairs; the VLM sees the condition and the video and emits a score per criterion. Per prompt, **12 of 14 models plus the original reference video (full reward)** form the training set and the **2 held-out models** form the test set — held-out *models*, not held-out *prompts*. Training: **4,421 videos × 8 labels**; test: **713 videos** (API refusals excluded). Majority vote is ground truth. GPT-4o and Gemini-1.5-Pro reasoning chains that reach the correct answer are distilled in as extra training data.
- **Per-criterion error rate on the test set (Table 5, lower is better; instruction / commonsense / physics):** GPT-4o **29.3 / 35.0 / 36.0**; GPT-4o + CoT 29.7 / 28.5 / 45.6; Gemini-1.5-Pro 30.7 / 34.5 / 29.3; Gemini-1.5-Pro + CoT 29.3 / **19.5** / 28.3; [Qwen2-VL-2B](../entities/qwen.md) 30.3 / 39.0 / 39.7; the row labelled "VILA-2B +Zero-Shot" **21.0 / 28.0 / 24.0**; the row labelled "VILA-2B +CoT Fine-tuned" 32.3 / 16.4 / 29.7.

> [!warning] Table 5's row labels do not match its own narrative
> The text says the fine-tuned VILA-2B judge is the one that beats GPT-4o, but the best-averaging row (21.0/28.0/24.0, mean 24.3) is labelled "+Zero-Shot" and the "+CoT Fine-tuned" row averages 26.1. Taken literally, an *un*-fine-tuned 2B VILA would beat GPT-4o, which no other sentence in the paper claims. Almost certainly a labelling slip in v1 (the natural reading is that both VILA rows are fine-tuned, with and without chain-of-thought). Also note the abstract's "8.6% higher average accuracy than GPT-4o" and the introduction's "9.9% lower error rate" are two different numbers for the same comparison; GPT-4o's mean error is 33.4 (zero-shot) or 34.6 (CoT), so either figure is reachable depending on which pair of rows is meant. Quote the per-criterion numbers, not the headline.

- **What the paper does not emphasize:** Gemini-1.5-Pro + CoT averages **25.7** — within ~1.4 points of the best VILA row, and *better* on commonsense (19.5 vs 28.0). The margin over GPT-4o is real; the margin over the strongest off-the-shelf baseline is small.
- **Aggregate agreement (Table 4).** Comparing model-level *totals*, the judge's mean prediction error is **4.1%** (max **6.81%**, Runway). On instruction following alone, Kendall **τ = 0.96** against the human ordering, mean error 2.79% (Table 7). **The judge scores 13 of 14 models higher than humans do** (all Table 4 errors positive except OpenSora-I2V at −0.17%); Kling goes 8.82 → 9.08. Physics sub-scores under the judge saturate — Newton and fluid read **1.00** for every closed model (Table 9) against 0.89–0.99 from humans.

### The judge as a reward (§3.4, §4.2, Appendix 8.2)

- Objective: maximize the summed judge reward over the grading criteria, VADER-style reward gradients. The judge is autoregressive, so the gradient is taken through the **softmax probability gap between the "No" and "Yes" answer tokens** rather than the discrete score.
- Applied to **Open-Sora v1.2 T2V**. Evidence: **Figure 8 and Figure 11 — qualitative pairs only** (flicker removed on "a goose playing chess"; instruction compliance on the bear-with-cake prompt; "sticky" fluid, deformation, wake behind a boat, fireworks obeying inertia). The authors: "This shows positive signs for future works to further improve the reward model"; "promising signals." **No before/after benchmark score is reported.**

### WorldModelBench vs VBench (§4.3, Appendix 8.1)

Eight models re-scored with VBench on WorldModelBench's prompts, then pairwise win rates compared. **Frame-wise quality win rates correlate at 0.69** between the two benchmarks; **physics-adherence win rates vs VBench's all-dimension win rate correlate at only 0.28**. Per VBench dimension against physics adherence (Table 6): subject consistency 0.15, background consistency 0.19, motion smoothness 0.34, **dynamic degree −0.05**, aesthetic quality 0.41, imaging quality 0.24. The authors' conclusion: "VBench does not effectively distinguish between videos based on their adherence to physical laws."

### Stated limitations (§5)

- **Sample size.** 350 prompts is "considerably smaller" than VideoPhy's 688, chosen for inference cost ("Mochi takes 5 minutes for 4 A100 GPUs"). Defended as "indicative" because the top two closed models separate cleanly (8.82 vs 8.59).
- Closed APIs refused some prompts — white cells in the heatmap, and the 713-video test set "excluding some samples that closed API endpoints refuse."
- Not stated but visible: the judge is validated on held-out *models* for the *same* 350 prompts, so nothing in the paper measures how it generalizes to new prompts or domains.

## Reading it against the wiki

> [!note] This fills the "not ingested" row — and moves it one column left
> The [world-model evaluation](../concepts/world-models/world-model-evaluation.md) table lists WorldModelBench between WorldScore and WorldArena in a progression "from *how it looks* toward *what it is good for*." Having read it: WorldModelBench is an **output-scoring** benchmark — a rubric applied to generated clips by crowd workers and a VLM — not a utility benchmark. Its real advance over VideoPhy is *what* is scored (instruction levels, five named laws, application domains, I2V) and *who* scores it (released human labels plus a calibrated judge). It belongs beside VideoPhy, not beside [WorldArena](../entities/worldarena.md). Nothing in it asks whether a policy planned inside the generator would work.

- **The generative-video tradition's own critic problem, a year before Physion-Eval.** [Physion-Eval](physion-eval-paper.md) found MLLM critics 2–6× less sensitive than untrained humans. WorldModelBench already shows the shape: GPT-4o's per-criterion error is 29–36%, and even the purpose-built judge misses 16–30% of individual labels — while its *aggregate* agreement is 4.1%. Per-video judgement is mediocre; leaderboard ordering is fine. This is the same "ranking survives, level does not" pattern the evaluation page records for world-models-as-evaluators, now in the judge-of-generators role, and with the same sign: **the learned judge flatters** (13 of 14 models scored above their human totals). A benchmark whose automated judge inflates and saturates on the physics sub-scores should be read from its human column, which the authors released precisely so that one can.
- **Domain difficulty tracks decision relevance.** Robotics, driving, and human activities are the hardest subdomains; natural scenes are the easiest. The domains the [HAI brief](hai-world-model-spatial-intelligence-brief.md) cares about for governance and the domains this wiki cares about for manipulation are where video generators score worst — a point the brief's citation of WorldModelBench does not draw out.
- **VBench's 0.28.** The correlation table is the cleanest single-source statement the wiki has that *perceptual quality and physical validity are different quantities*, from a group with no latent-space axe to grind. It sits alongside [WorldArena](worldarena-paper.md)'s r = 0.360 (perception vs action planning) and [VP²](vp2-paper.md)'s FVD-vs-control sign flips. Dynamic degree at −0.05 is worth remembering: more motion is not more physics.
- **Physics violation rates disagree with Physion-Eval by an order of magnitude**, and the difference is the instrument. Here Kling's worst per-law rate is 12%; Physion-Eval reports **83–94%** of generated clips carrying at least one human-identified violation. WorldModelBench uses a five-item checklist filled in by crowd workers on 4-second clips with 1.7 votes each; Physion-Eval uses expert reasoning traces with 0.1 s localization. The checklist measures what an annotator notices in one pass, and it is not obvious which number a downstream user should trust — but the gap says the rubric's granularity is doing a lot of the work.
- **Reward fine-tuning: file under [reward post-training](../concepts/learning/reward-post-training-diffusion.md), as a claim, not a result.** The mechanism (differentiable VADER gradients through a VLM's yes/no logit gap) is a reusable trick, and the judge is the first video-world-model reward model the wiki has. But the evidence is four cherry-picked pairs on the *weakest* model in the table (Open-Sora 1.2 T2V, 6.11). If the judge inflates and saturates on the physics criteria, optimizing against it is optimizing a soft target; the paper does not test for that.
- **Sample-size discipline.** 350 prompts × 1.7 votes; the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) habit applies. The top-two separation the authors point to (8.82 vs 8.59) is 0.23 of 10 points; sub-score differences of a few hundredths (fluid: 0.92–0.99 across all 14 models) are within what 1.7 votes on a binary flag can resolve. Use the ordering and the instruction/mass/temporal columns, where the spread is large.
- **Where it points.** [PAN](pan-world-model-paper.md)'s Action Simulation Fidelity protocol borrows WorldModelBench's VLM-judge design; this page is now the primary for that lineage.

## Entities mentioned

- [NVIDIA](../entities/nvidia.md) (Chen, Yin, Han, Lu; both first authors interned there), UC Berkeley (Gonzalez, Stoica — the Chatbot Arena group, whose agreement methodology is reused), UC San Diego (Xiaolong Wang), MIT (Song Han; VILA is his lab's VLM).
- Reference-video datasets: [nuScenes](../entities/nuscenes.md), [Open X-Embodiment](../entities/open-x-embodiment.md), ActivityNet (no page), OpenVid-1M (no page).
- Judged models (no entity pages): Kling v1.5, MiniMax, Mochi / Genmo, Runway Gen-3, Luma 1.6, CogVideoX-5B, Open-Sora 1.2, Open-Sora-Plan 1.3, T2V-Turbo-v2, Pandora.
- Judges: VILA-2B (fine-tuned), GPT-4o, Gemini-1.5-Pro, [Qwen2-VL-2B](../entities/qwen.md).
- Cited as the motivating "video world model" claims: Sora, Genie (see [Genie 3](../entities/genie-3.md) for the current version), the 1X world model, [RT-1](../entities/rt-1.md) / [RT-2](../entities/rt-2.md) as decision-making applications, and [LeCun](../entities/yann-lecun.md)'s 2022 position paper for the definition.
- Contemporaries: [WorldArena](../entities/worldarena.md), [Physion-Eval](../entities/physion-eval.md) — the benchmarks this one is now compared against.

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the landscape row this fills; the judge-inflation and VBench-correlation findings.
- [Physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) — squarely in the generative-video tradition (human annotation *and* a model judge, no human baseline on task solving).
- [World models](../concepts/world-models/world-model.md) — the "feasible next frames given text and image" definition the paper adopts.
- [Reward post-training of diffusion models](../concepts/learning/reward-post-training-diffusion.md) — a VLM judge as differentiable reward via the yes/no logit gap.
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) — the VLM-as-a-judge use case for physics understanding.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the same sample-size arithmetic, applied to a video benchmark.
- [Generative video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md), [what world models are measurably good for](../syntheses/world-models/what-world-models-are-measurably-good-for.md) — pixel-family benchmarking, and why an output rubric is not a utility measurement.

## Open questions

- Does the judge generalize to **new prompts**? The split holds out models, never prompts; a judge trained on 12 models' outputs for a prompt has seen the reference video and the prompt's typical failure modes.
- Would the reward-fine-tuned Open-Sora score higher on WorldModelBench's *human* column, or only on the judge? The paper reports neither.
- Why do crowd checklists find ~10% per-law violation rates where Physion-Eval's expert protocol finds >80% per clip — annotator sensitivity, clip length, or rubric granularity?
- The Table 5 labelling: which VILA-2B row is the shipped judge? (A later arXiv version or the GitHub release may resolve it; not checked.)
- Robotics is one of the three hardest domains, yet the 50 robotics prompts are OXE first frames with GPT-4o action captions — how much of the difficulty is the arm, and how much is caption ambiguity about what "opens" means?
