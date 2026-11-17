---
title: "Gemini Robotics: Bringing AI into the Physical World (tech report)"
type: source
url: https://storage.googleapis.com/deepmind-media/gemini-robotics/gemini_robotics_report.pdf
fetch_url: https://storage.googleapis.com/deepmind-media/gemini-robotics/gemini_robotics_report.pdf
local_path: raw/gemini-robotics-report-2025.pdf
sha256: 0a326fa9a810fa5c187ec0391a7608fd33c81e9fb29f645cfebc667123d4bbbe
author: Gemini Robotics Team, Google DeepMind
affiliation: Google DeepMind
published: 2025-03-12
ingested: 2026-11-17
venue: Google DeepMind technical report (also arXiv 2503.20020)
format: "64-page PDF (101 MB), built 2025-03-11. Main text pp. 1–29 read in full; model card (App. A) and Appendix C.1, C.2, D.1 and D.4 read; the remaining appendix task lists and prompts skimmed. Per-task results are in bar charts that were not transcribed."
tags: [gemini-robotics, gemini-robotics-er, erqa, vla, embodied-reasoning, aloha-2, pointing, code-as-policy, in-context-learning, cloud-inference, action-chunking, pi-zero-baseline, diffusion-policy, apptronik, franka, asimov, semantic-safety, google-deepmind, primary]
---

# Gemini Robotics: Bringing AI into the Physical World

> [!note] Publication date
> The PDF was built on 2025-03-11 and the models were announced on 2025-03-12. The arXiv identifier is from memory of the public record, not from the PDF.

## Summary

The founding technical report of the [Gemini Robotics](../entities/gemini-robotics.md) line, and the generation the wiki was missing: it had [1.5](gemini-robotics-1-5-report.md), [2](gemini-robotics-2-blog.md) and [2.5](gemini-robotics-2-5-blog.md) but not the original. The report introduces three things on top of Gemini 2.0. **ERQA**, a 400-question embodied-reasoning benchmark. **Gemini Robotics-ER**, a Gemini 2.0 Flash variant with enhanced spatial reasoning that can control a robot with no action training, by writing code or by in-context learning. And **Gemini Robotics**, a VLA "fine-tuned to predict robot actions directly," split between a cloud-hosted backbone and an on-robot action decoder. The argument running through it is that embodied reasoning in the backbone is what the action model's generalization and adaptability are built on, and the evidence is a set of real-robot comparisons against a re-implemented π0 and a diffusion policy trained on the same data.

## Key claims

### ERQA and embodied reasoning (§2)

- **ERQA**: "400 multiple choice Visual Question Answering (VQA)-style questions" across spatial, trajectory, action, state-estimation, pointing, multi-view and task reasoning; 28% use more than one image. All questions were manually labeled. Open-sourced (p. 4–5).

| Model (Feb 2025) | ERQA | with CoT |
|---|---:|---:|
| Gemini 2.0 Pro Experimental | 48.3 | 54.8 |
| GPT-4o | 47.0 | 50.5 |
| Gemini 2.0 Flash | 46.3 | 50.3 |
| Gemini 1.5 Flash / 1.5 Pro | 42.3 / 41.8 | |
| GPT-4o-mini | 37.3 | 40.5 |
| Claude 3.5 Sonnet | 35.5 | 45.8 |

- **Pointing** (accuracy; Table 3): Gemini Robotics-ER scores 71.3 on Paco-LVIS, 49.5 on Pixmo-Point and 45.0 on Where2Place, against Gemini 2.0 Flash at 46.1 / 25.8 / 33.8. [Molmo](../entities/molmo.md) 72B leads Where2Place at 63.8.
- **3D detection**: ER reaches 48.3 AP@15 on SUN-RGBD, called a new state of the art, with the caveat that the best prior model was measured "on an easier set of 10 categories" (Table 4).
- **Capabilities listed**: 2D detection, pointing, trajectory prediction, top-down grasp prediction (new in ER), multi-view correspondence, metric 3D boxes from a single image.

### Controlling a robot without action training (§2.3)

On a bimanual [ALOHA](../entities/aloha.md) 2, with a perception-and-motion API and a loop of images, state and execution feedback:

| | Zero-shot (code generation) | In-context (10 demonstrations) |
|---|---:|---:|
| Gemini 2.0 Flash, simulation, 7 tasks | 27% | 51% |
| Gemini Robotics-ER, simulation | 53% | 65% |
| Gemini Robotics-ER, real robot, 3 tasks | 25% | 65% |

- Simulation figures are averages "over 50 trials" per task; real ones over 9 or 10 (Tables 5, 6).
- "Especially zero-shot robot control performance is strongly correlated with better embodied understanding": ER nearly doubles Flash.
- Zero-shot fails outright where precision is needed: packing a toy is 0% for both models in simulation, and dress folding is 0% on the real robot, "mostly due to its inability to generate precise enough grasps."
- In-context learning feeds demonstrations as text: object keypoints and end-effector poses interleaved with language descriptions of the action. No external keypoint model is needed.
- The stated limit: "as a VLM, there are inherent limitations for robot control, especially for more dexterous tasks, due to the intermediate steps needed" (p. 14).

### The VLA: architecture and data (§3.1)

- **Two parts**: "a VLA backbone hosted in the cloud" and "a local action decoder running on the robot's onboard computer." The backbone is "a distilled version of Gemini Robotics-ER" with latency "optimized from seconds to under 160ms."
- **Latency**: "end-to-end latency from raw observations to low-level action chunks is approximately 250ms. With multiple actions in the chunk, the effective control frequency is 50Hz."
- **Data**: "thousands of hours of real-world expert robot demonstrations" collected "on a fleet of ALOHA 2 robots... over 12 months," covering "thousands of diverse tasks," plus web, code, multimodal and embodied-reasoning data.
- **Not given**: parameter counts, decoder architecture, action representation, exact hours.

### Out-of-the-box results (§3.2–3.4)

- **Baselines**: a re-implementation of [π0](../entities/pi-zero.md) trained on the same mixture, which the authors say beats the public checkpoint, and a task-conditioned multi-task [diffusion policy](../entities/diffusion-policy.md). Both run locally on an RTX 4090.
- **Method**: models are run "back-to-back in random order (A/B testing)," allowing "a pairwise t-test" (App. C.1). Both binary success and a 0–1 progress score are reported.
- **20 dexterous tasks**: Gemini Robotics is "proficient at half of the tasks out of the box with a success rate exceeding 80%" and is the only model with non-zero success on the hardest. "Some of the most dexterous tasks are still quite challenging" (e.g. "insert shoe lace").
- **Language following**: 25 instructions in five scenes. The π0 re-implementation "struggles with interpreting descriptive language attributes" on unseen objects.
- **Generalization**: 85 tasks, 20% in-distribution, the rest split across visual, instruction (typos, new languages, paraphrase) and action (new positions, new object instances) shifts. Gemini Robotics leads on all three and "achieves non-zero performance in those cases where the baselines fail catastrophically."

### Specialization and adaptation (§4)

- **Long-horizon dexterity**: six tasks (origami fox, lunch-box packing, spelling game, card game, tongs, scooping), each fine-tuned on 2,000–5,000 episodes. Average success **79%**; lunch-box packing 100% over 20 trials for a task of over two minutes. The spelling game handles 4 of 6 unseen hand-drawn sketches.
- **Pretraining is what makes this work**: the same model trained from scratch on the specialization data alone gets "0% success rates across the board."
- **Reasoning-enhanced variant**: fine-tuning on a re-labeled dataset so the model predicts keypoint trajectories as an "internal chain of thought" raises success on out-of-distribution tasks that need one-step reasoning, semantic knowledge or spatial understanding (100 trials; Fig. 24).
- **Fast adaptation**: on 7 of 8 short tasks, above 70% success "with at most 100 demonstrations (equivalent to 15 minutes to 1 hour)." Baselines are competitive or better on the easier ones.
- **New embodiments**, described as preliminary: a bi-arm [Franka](../entities/franka-panda.md) (four industrial tasks including two from NIST Assembly Task Board 2, one needing about 40 N; average success 63%) and [Apptronik's Apollo](../entities/apptronik-apollo.md) humanoid with five-fingered hands. In-distribution success is "on par or slightly better than" a single-task diffusion policy; the advantage is in visual and action generalization.

### Safety (§5)

- Physical action safety stays in "the lowest levels of the control stack"; "we need VLA models such as Gemini Robotics to be interfaced with such safety-critical lower-level controllers."
- **Semantic action safety** is introduced with the examples the wiki already knows: "a soft toy must not be placed on a hot stove... a knife should not be pointed at a human." The [ASIMOV](../entities/asimov-benchmark.md) datasets were released "concurrent with this tech report," and ER models "are post-trained on such instances."
- A new output modality needed new content safety: post-training gives "a 96% rejection rate for bias-inducing pointing queries, compared to a baseline rate of 20%."
- Constitutions and post-training mitigate degradation "under an adversarial prompt."

### Stated limitations (§6)

Gemini 2.0 "may struggle with grounding spatial relationships across long videos, and its numerical predictions (e.g., points and boxes) may not be precise enough for more fine-grained robot control tasks." Future work: combining multi-step reasoning with dexterity in novel situations, more simulation data, and "zero-shot cross-embodiment transfer."

## Reading it against what came after

- **The stated future work is the later roadmap.** Zero-shot cross-embodiment transfer became [1.5's Motion Transfer](gemini-robotics-1-5-report.md); "lean more on simulation" became [Argon-generated practice runs for 2.5](gemini-robotics-2-5-blog.md); trajectory chain-of-thought became 1.5's Embodied Thinking.
- **Evaluation practice went backwards in public.** This report states trial counts, randomized back-to-back ordering, a paired test, and an external baseline trained on the same data. The [GR 2](gemini-robotics-2-blog.md) and [GR 2.5](gemini-robotics-2-5-blog.md) announcements give none of these.
- **ERQA's ceiling moved a long way.** The best score here is 54.8 with chain of thought. [Gemini 4 Argon](../entities/gemini-4-argon.md) reported 87% twenty months later. See [ERQA](../entities/erqa.md).
- **The cloud dependency is explicit.** The 2025 VLA cannot run without a network round trip of about 160 ms inside a 250 ms loop. That is the gap the later On-Device models were built to fill.
- **The baseline is the authors' own re-implementation.** The π0 comparison uses a version retrained on DeepMind's data, justified by an appendix figure showing it matches or beats the public checkpoint on fast-adaptation tasks. It is still a comparison the baseline's authors did not run.

## Entities mentioned
- [Gemini Robotics](../entities/gemini-robotics.md) · [Google DeepMind](../entities/google-deepmind.md) · [ERQA](../entities/erqa.md)
- [ALOHA](../entities/aloha.md) (ALOHA 2) · [Franka Panda](../entities/franka-panda.md) (bi-arm) · [Apptronik Apollo](../entities/apptronik-apollo.md)
- [π0](../entities/pi-zero.md) and [Diffusion Policy](../entities/diffusion-policy.md) (baselines) · [Molmo](../entities/molmo.md) (pointing comparison)
- [ASIMOV Benchmark](../entities/asimov-benchmark.md) · [NEISS](../entities/neiss.md)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md)
- [Code as policy](../concepts/agents/code-as-policy.md): the zero-shot control path
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md): demonstrations as text in the prompt
- [Cross-embodiment](../concepts/learning/cross-embodiment.md): adaptation by fine-tuning, before Motion Transfer
- [Chain of thought](../concepts/learning/chain-of-thought.md): CoT on ERQA; trajectories as internal reasoning
- [Semantic safety](../concepts/safety/semantic-safety.md)

## Open questions
- Model sizes, decoder design and action representation. None are given, and the 1.5 report did not give them either.
- How many hours "thousands of hours" is, and how much of the result depends on a 12-month ALOHA 2 collection no one else has.
- Per-task numbers for the 20-task and 85-task evaluations. They are in charts that were not transcribed here.
- Whether the Apollo results were ever quantified. The humanoid appears in one figure with no success rate.

## Related sources
- [Gemini Robotics 1.5 tech report](gemini-robotics-1-5-report.md) · [Gemini Robotics 2 blog](gemini-robotics-2-blog.md) · [Gemini Robotics 2.5 blog](gemini-robotics-2-5-blog.md): the three later generations.
- [ASIMOV Benchmark paper](asimov-benchmark-paper.md): released concurrently.
- [π0 paper](pi-zero-paper.md): the baseline.
- [Gemini 4 Argon for Robotics](gemini-4-argon-robotics-blog.md): the ERQA 87% claim.
