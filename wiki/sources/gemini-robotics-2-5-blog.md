---
title: "Gemini Robotics 2.5 accelerates real-world general dexterity (DeepMind blog)"
type: source
url: https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/
fetch_url: https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/
local_path: raw/2026-11-17-deepmind-gemini-robotics-2-5-blog.md
sha256: 39f0a71d6acba32560772de6417591e73c47fdf966effdd1350a85a0ab6ce335
author: Carolina Parada (Google DeepMind)
affiliation: Google DeepMind
published: 2026-11-10
ingested: 2026-11-17
venue: deepmind.google blog
format: "model announcement: prose, four per-task bar charts (GR 2 vs GR 2.5), demo videos. Captured 2026-11-17 via curl with main-element text extraction; the four charts are saved in raw/assets/gemini-robotics-2-5/. Videos were not captured."
tags: [gemini-robotics, gemini-robotics-2-5, vla, dexterity, deformables, tool-use, kitting, humanoid, apptronik, apollo-2, sharpawave, franka-duo, mercedes-benz, gemini-4-argon, asimov, jailbreak, steerability, real-to-sim, vendor-source, primary]
---

# Gemini Robotics 2.5 accelerates real-world general dexterity (DeepMind blog)

## Summary

Google DeepMind announces **Gemini Robotics 2.5** (2026-11-10), a new VLA it calls its "most capable" to date, three and a half months after [Gemini Robotics 2](gemini-robotics-2-blog.md). The post makes three claims. **Dexterity**: across "over 200 distinct tasks" the model has a "30% to 100% higher success rate depending on the type of task" and runs "20% to 30% faster" than the previous baseline, with four per-task charts comparing it to GR 2. **Reliability**: in a proof-of-concept on Mercedes-Benz production lines, [Apptronik's Apollo 2](../entities/apptronik-apollo.md) kitted automotive brackets at a **96% success rate**. **Safety**: inference-time "reasoning guidance" for steering around hazards, plus a new jailbreak benchmark, **ASIMOV-Jailbreak**, on which [Gemini 4 Argon](../entities/gemini-4-argon.md) scores 99.5%. The post credits Argon with accelerating the model's development through simulated data and failure analysis. Only a VLA is announced: there is no ER 2.5 and no On-Device 2.5, and the model is "rolling out to our robotics partners," with no public access.

## Key claims

### Evaluation: four per-task charts against GR 2

The model was evaluated "across 200 distinct tasks" on two platforms: **Apollo 2 with the five-finger, 22-DoF [SharpaWave](../entities/sharpa-wave.md) hand**, and the **[Franka](../entities/franka-panda.md) Duo** with two-finger parallel grippers. The headline is "30% to 100% higher success rate depending on the type of task, while completing tasks 20% to 30% faster." The post does not say whether "30% to 100% higher" is relative or in percentage points, and the speed figure has no chart.

Each chart plots one bar per task, sorted by GR 2.5 success, with GR 2 overlaid. Task names are shown only for the called-out bars below; the rest are unlabeled.

| Chart | Task (platform) | GR 2 | GR 2.5 |
|---|---|---:|---:|
| Tabletop pick & place | Pick rubber duck and place on yellow plate (Duo) | 86% | 100% |
| | Extract disk drive from bay (Duo) | 0% | 100% |
| | Pick up a lime and put it on the top shelf (Apollo + Sharpa) | 0% | 100% |
| | Clean up kitchen mixer (Apollo + Sharpa) | 0% | 60% |
| Multi-step & contact-rich | Close lid of black toolbox (Duo) | 0% | 93% |
| | Unhang mug to table (Duo) | 29% | 75% |
| | Sweep trash into dustpan with brush (Apollo + Sharpa) | 0% | 52% |
| | Pack rice cooker (Apollo + Sharpa) | 0% | 40% |
| Precision kitting & insertion | Take a picture with the Polaroid camera (Duo) | 0% | 92% |
| | Unscrew light bulb (Apollo + Sharpa) | 63% | 90% |
| | Put the pliers in the black toolbox (Duo) | 7% | 82% |
| | Kit all tools into bin (Duo) | 33% | 70% |
| Dexterous tools & deformables | Pack pastries into box using tongs (Apollo + Sharpa) | 5% | 100% |
| | Untie ribbon bow on gift box (Apollo + Sharpa) | 0% | 70% |
| | Hang cardigan sweater on clothes hanger (Apollo + Sharpa) | 0% | 62% |
| | Fold pants with board (Apollo + Sharpa) | 0% | 40% |

What the charts show beyond the callouts (read off the images, so approximate):

- **Bar counts.** About 76 tabletop, 20 multi-step, 49 precision and 36 dexterous bars, roughly 180 in total against the stated "over 200."
- **The distribution is wide.** In every chart GR 2.5 runs from 100% down to about 10%. Each chart ends in a tail of tasks at roughly 10% (about nine on tabletop pick-and-place, four each on precision and dexterous).
- **Multi-step and contact-rich is the largest jump.** GR 2 has a visible non-zero bar on only 3 of 20 tasks; GR 2.5 is non-zero on all 20 and at 100% on four.
- **Not every task improved.** The GR 2 bar is drawn on top, so where only the hatched bar is visible GR 2.5 is at or below GR 2. That is the case for a few tasks per chart, including some below 100% (two tabletop tasks near 71%, two precision tasks near 67% and 43%). The charts cannot separate "equal" from "regressed."

> [!warning] Contradiction: the GR 2 baseline here is lower than GR 2's own launch numbers
> The [GR 2 blog](gemini-robotics-2-blog.md) reported **unscrew bulb 92%** on Apollo with SharpaWave hands. This post's chart gives GR 2 **63%** on "Unscrew light bulb" on Apollo + Sharpa, and GR 2.5 **90%**, which is below GR 2's originally published figure. Similarly, GR 2's launch "dustpan" result was **32%**; here GR 2 scores **0%** on "Sweep trash into dustpan with brush."
>
> Neither post describes its protocol, so the tasks may differ in objects, scenes or scoring despite the matching names. But a reader holding only the earlier post would conclude that bulb-unscrewing did not improve, and a reader holding only this one would see +27 points. Until DeepMind publishes the evaluation setup, treat the GR 2 column as a re-measured baseline under new conditions, not as GR 2's published performance.

> [!note] Still no trial counts
> No n is given for any bar. The called-out percentages imply different denominators from task to task (5% needs at least 20 trials; 29% and 86% fit 7 or 14), so per-task n is probably small and uneven. Under the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), the 0% → 90%+ jumps survive any plausible n, and mid-range differences between neighbouring bars do not. There is still no external baseline: every comparison is GR 2.5 against GR 2.

### Mercedes-Benz kitting proof-of-concept

- **Where**: "active automotive production lines" in **Kecskemét, Hungary** and **Sindelfingen, Germany**, with Apptronik and Mercedes-Benz.
- **Task**: automotive kitting. Apollo 2 reaches into supply bins, picks metal brackets and places them into sequencing containers "in the exact order needed for each vehicle on the line," "correcting for any gaps."
- **Stack**: **Gemini Robotics ER** (no version given) tracks the workflow; **Gemini Robotics 2.5** controls hands and arms.
- **Result**: "a **96% success rate**." The post calls it a "proof-of-concept" and a "pilot."
- **Apptronik CEO Jeff Cardenas**: "we saw the models improve dramatically in just a few weeks of post-training and carry over to Mercedes-Benz production with very little drop-off."

> [!note] What the 96% does and does not establish
> It is the wiki's first success rate for a frontier VLA on a named, running car line, and it is a task-specific result: the Cardenas quote says the model was post-trained for weeks before deployment. Missing are the number of picks, the unit of success (per part, per tray, per shift), duration, cycle time against a human, intervention rate, and what happened on the 4%. Kitting brackets from bins into trays is also one of the more structured tasks in a plant. The quote's "very little drop-off" from lab to line is the more interesting claim, and it has no number.

### Safety

- **Steerability**: "inference-time reasoning guidance to steer around physical hazards in real-time," compared to safety classifiers around Gemini's text responses. It "boosted safe task completion around obstacles by 33% and around nearby people by 43%." No baseline rates, no n, and no statement of whether the gains are relative.
- **Agentic safety**: "Gemini 4 Argon currently leads our agentic robotics evaluations across unsafe task refusal, resolving uncertainty, and working in proximity to humans," citing page 200 of the Gemini 4 safety report (not ingested).
- **ASIMOV-Jailbreak**: "a new open-source benchmark containing hundreds of prompts that disguise unsafe requests across dozens of scenes." Argon reaches **99.5% jailbreak resistance** against **82%** for "our previous baseline, Gemini Robotics ER 2." The link points to the existing `google/asimov_agentic` Hugging Face dataset, so it appears to ship as part of the [ASIMOV-Agentic](../entities/asimov-benchmark.md) release.

> [!note] The safety results belong to Argon, not to GR 2.5
> The steerability numbers are about the VLA. The agentic and jailbreak numbers are about a general frontier model in the orchestrator seat, with ER 2 named as the "previous baseline." The [GR 2 safety report](gemini-robotics-2-safety-report.md) found no model in the acceptable quadrant for human-proximity monitoring; this post says Argon "leads" on proximity without giving the numbers that would show whether that gap closed.

### Argon's role in building it

Gemini 4 Argon "helped solve these bottlenecks by acting as a simulation engine, which greatly accelerated our development of Gemini Robotics 2.5." Two mechanisms are named: generating "thousands of varied, simulated practice runs from a real-world camera scene" with a digital twin, combined with real demonstrations; and helping researchers "hypothesize why task failures happen from video footage" and test fixes in simulation and on robots. No ablation separates Argon's contribution from the rest of the training recipe.

This matches the workflow in the [Argon robotics post](gemini-4-argon-robotics-blog.md), where sim data from one overhead photo lifted an unnamed "generalist VLA" from 56% to 75%. It is plausible that the unnamed VLA was a GR 2.5 development checkpoint. Neither post says so.

### What is absent

- **No ER 2.5 and no On-Device 2.5.** The orchestrator in the factory pilot is an unversioned "Gemini Robotics ER," and the agentic safety results are Argon's.
- **No whole-body results.** GR 2's headline was whole-body humanoid control. All four charts here are manipulation, and the only platforms named are Apollo 2 + SharpaWave and Franka Duo. Inspire hands, Dexmate, [SO101](../entities/so-arm101.md) and Trossen do not appear.
- **No architecture, parameters, control rate, training data or compute.** No technical report is linked.
- **Access**: partners only. Acknowledged partners: [Agile](../entities/agile-robots.md), Apptronik and Mercedes-Benz.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md) · [Gemini 4 Argon](../entities/gemini-4-argon.md)
- [Apptronik Apollo](../entities/apptronik-apollo.md) (Apollo 2) · [SharpaWave](../entities/sharpa-wave.md) · [Franka Panda](../entities/franka-panda.md) (Franka Duo) · [Agile Robots](../entities/agile-robots.md)
- [ASIMOV Benchmark](../entities/asimov-benchmark.md): ASIMOV-Jailbreak is the new member
- [Demis Hassabis](../entities/demis-hassabis.md) (acknowledgements) · Mercedes-Benz and Carolina Parada (no entity pages)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) · [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md)
- [Semantic safety](../concepts/safety/semantic-safety.md) · [AI red teaming](../concepts/safety/ai-red-teaming.md)
- [Real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md): Argon-built twins as a VLA data source
- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) · [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md): the ER + VLA split in the factory pilot

## Open questions
- **Evaluation protocol.** Trials per task, scoring rules, in- versus out-of-distribution scenes, and why the GR 2 baseline differs from GR 2's launch figures.
- **Is "30% to 100% higher" relative or absolute**, and what are the per-category averages?
- **The pilot's denominators**: picks, shifts, cycle time, interventions, and how much post-training data "a few weeks" represents.
- **Is the ER line being retired?** No ER 2.5, an unversioned ER in the pilot, and Argon replacing ER 2 as the agentic safety model. The post does not say.
- **Which hands does the Mercedes pilot use?** The lab charts use SharpaWave; the pilot section does not name the hand.
- **ASIMOV-Jailbreak composition and scoring**, and the human-proximity numbers behind "leads." Both should be in the Gemini 4 safety report (p. 200) and the Hugging Face dataset, neither ingested.
- **Was the 56% → 75% VLA in the Argon post a GR 2.5 checkpoint?**

## Related sources
- [Gemini Robotics 2 blog](gemini-robotics-2-blog.md): the previous generation and the source of the conflicting baseline figures.
- [Gemini 4 Argon for Robotics](gemini-4-argon-robotics-blog.md): the toolchain this post says accelerated GR 2.5.
- [Gemini Robotics 2: Safety Evaluations](gemini-robotics-2-safety-report.md): ASIMOV-Agentic, which ASIMOV-Jailbreak extends.
- [Gemini Robotics model page](deepmind-gemini-robotics-model-page.md): the partner list the post links to.
