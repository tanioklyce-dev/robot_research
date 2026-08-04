---
title: "CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation"
type: source
url: https://arxiv.org/abs/2603.22435
author: "Letian (Max) Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Dantong Niu, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi \"Jim\" Fan"
affiliation: NVIDIA, UC Berkeley, Stanford University, Carnegie Mellon University
published: 2026-03-23
ingested: 2026-08-03
venue: "ICML 2026 (Proceedings of the 43rd ICML, Seoul; PMLR 306)"
format: conference paper (58 pp with appendices)
local_path: raw/2603.22435v2.pdf
license: arXiv preprint (v1 2026-03-23, v2 2026-07-02)
tags: [code-as-policy, llm-agent, benchmark, robot-manipulation, libero-pro, behavior, robosuite, evaluation, rlvr, grpo, skill-library, test-time-compute, sim-to-real, nvidia-gear, primary-source]
---

## Summary

The first systematic measurement of **[code-as-policy](../concepts/agents/code-as-policy.md) as an autonomous controller**, and the paper that separates *agent capability* from *designer-provided scaffolding* — the confound running through the entire code-as-policy line since [Code as Policies](../concepts/agents/code-as-policy.md) (Liang et al., 2023). Prior CaP systems reported strong zero-shot numbers while calling human-tuned macros like `stack_objs_in_order()`; CaP-X shows that **as those macros are stripped away, performance falls monotonically**, so much of the published success belonged to the API designer rather than the model.

The framework has four parts: **CaP-Gym** (187 interactive robot-coding tasks behind a Gymnasium/REPL interface), **CaP-Bench** (12 frontier models × 8 tiers ablating abstraction, iteration, and grounding), **CaP-Agent0** (a *training-free* agentic harness), and **CaP-RL** (GRPO post-training of the coding agent itself). The constructive result is that **test-time compute buys back what abstraction removal costs**: with multi-turn execution feedback, visual differencing, an auto-synthesized skill library, and ensembled reasoning, an agent operating on *low-level* primitives matches or beats human-expert code on 4 of 7 tasks — and beats post-trained VLAs under perturbation without any task-specific training data.

> [!note] Read together with [ASPIRE](aspire-paper.md)
> ASPIRE (Jun 2026, overlapping authors) is **built on CaP-X** and treats CaP-Agent0 as its primary baseline. CaP-X establishes the measurement; ASPIRE pushes the numbers. Ingested as a pair.

## Key claims

### The core confound: abstraction inflates code-as-policy results (§3.1, §3.3)

- CaP-Bench varies **primitive abstraction** across four single-turn tiers: **S1** high-level macros + privileged ground-truth state, **S2** high-level macros + real perception (*"the default setting for most prior work"*), **S3** low-level primitives (`solve_ik()`, `sam3_text_prompt()`) with usage examples, **S4** low-level with signatures/docstrings only.
- **Success increases monotonically S4 → S1** (Fig. 3), "mirroring how prior Code-as-Policies approaches relying on high-level primitives report strong zero-shot performance." High-level macros "reduce the effective search space and allow models to focus on task sequencing."
- The cost is expressivity: abstraction "imposes a generality ceiling that masks failures in low-level reasoning." Low-level tiers enable behaviors high-level APIs cannot represent (e.g. hierarchical perception fallback).
- **Recommendation to the field:** *"generalist embodied coding agents be evaluated primarily on primitive-level performance, ensuring that success stems from robust reasoning rather than from the inductive biases of an over-engineered, often task-specific, API set."*

### Takeaway 1 — frontier models still trail human experts (§3.3)

- Human reference: **N=7 paper authors**, each with 2+ years robotics-programming experience, writing single Python scripts against the *identical* API, iterating until **88.5% average single-turn success**.
- Across 12 models at S4, **none matches human-crafted programs in zero-shot Pass@1**. Closed-source consistently beats open-source; newer models are stronger. Models evaluated: Gemini-3-Pro, GPT o1 / o4-mini / 5.1 / 5.2, [Claude](../entities/anthropic.md) Haiku 4.5 and Opus 4.5, GPT-OSS-20B/120B, Qwen3-235B, Qwen2.5-Coder-7B-Instruct, Kimi K2 Instruct, DeepSeek-V3.1-Terminus.

### Takeaway 3 — feedback modality matters more than feedback quantity (§3.3)

The multi-turn tiers produce the paper's most transferable engineering finding:

| Tier | Feedback given to the agent | Effect |
|---|---|---|
| **M1** | `stdout` / `stderr` execution traces | **Improves** over single-turn across all models |
| **M2** | Raw RGB observations interleaved per turn | **Degrades** relative to M1 |
| **M3** | **Visual Differencing Module** — a VLM converts observations to structured *text* | **Best**; consistently beats both M1 and M2 |
| **M4** | M3's VDM + low-level primitives | Reaches **parity with high-level multi-turn (M3)**, surpasses high-level single-turn (S2) |

- The M2 degradation is attributed to a **cross-modal alignment gap**: "foundation models are rarely trained to jointly reason over software coding and images of physical task execution."
- M4 ≥ S2 is the **test-time compute scaling** claim: *"robustness can be synthesized at runtime by increasing an agent's capacity for reasoning, verification, and self-correction over atomic primitives"* — i.e. you can buy back the abstraction penalty rather than hard-coding macros.
- Absent visual grounding, successful agents **self-instrument**: injecting print statements to surface object poses, then explicitly verifying task completion (e.g. checking relative heights to confirm a stack).

### CaP-Agent0 — the training-free harness (§4)

Three components, each derived from a benchmark finding:

1. **Visual Differencing Module** (from Takeaway 3).
2. **Auto-synthesized persistent skill library** — successful S3 rollouts are pooled **across all 12 models and 7 tasks** (so the library is *not* model-specific), function definitions extracted by regex, and Gemini-3-Pro prompted to identify recurring task-agnostic logic. Yields **9 verified task-agnostic primitives**. Unlike fixed human APIs, "these skills are *discovered*… and retain the expressivity of low-level interfaces."
3. **Parallel reasoning** — 9 queries to one model, or 3 each to GPT-5.2 / Claude Opus 4.5 / Gemini-3-Pro, synthesized by a central coding agent.

**Ablation (avg. success, Fig. 8):** S3 **24%** → M4 **55%** → +skill library **59%** → +1-model parallel **66%** → +3-model parallel **68%**. Evaluated at **100 trials per task**. CaP-Agent0 matches or exceeds human expert code on **4 of 7** tasks despite operating solely on low-level primitives.

> [!warning] Two of the four ablation steps do not survive their sample size
> At n=700 (7 tasks × 100 trials), checked against the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md): the multi-turn/VDM step (24→55) and the first parallel-reasoning step (59→66) are solid (p < 10⁻⁴ and p = 0.007). But **the skill library's own contribution (+4 pp, 55→59) is not statistically established (p = 0.13)**, nor is the third parallel model (+2 pp, 66→68; p = 0.43).
>
> This matters because the skill library is the component the paradigm's *architectural* argument leans on hardest. CaP-X's evidence for it is weak; **[ASPIRE](aspire-paper.md)'s is much stronger** — a library-size scaling curve (N = 0 → 25 → 50 → 90) and a 4% → 31% zero-shot transfer result. Cite ASPIRE, not this ablation, for "skill libraries compound."

### CaP-Bench++ — code-as-policy vs. VLAs under perturbation (§4.2)

**[LIBERO-PRO](libero-pro-paper.md), 30 tasks** (Table 2). Success under initial-**Pos**ition and instruction (**Task**) perturbations:

| Method | object Pos | object Task | goal Pos | goal Task | spatial Pos | spatial Task |
|---|---|---|---|---|---|---|
| [OpenVLA](../entities/openvla.md) | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| [π0](../entities/pi-zero.md) | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| π0.5 | 0.17 | 0.01 | **0.38** | 0.00 | **0.20** | 0.01 |
| **CaP-Agent0** | **0.22** | **0.18** | 0.26 | **0.17** | 0.12 | **0.14** |

> [!note] The shape of this result matters more than the magnitude
> All numbers are low. But **CaP-Agent0 is training-free and the VLAs are post-trained**, and the two degrade differently: VLAs collapse to ~0 under *instruction* perturbation because "VLAs are trained on a different instruction distribution," whereas the coding agent is roughly as good on Task as on Pos. Code-as-policy's robustness advantage here is **against paraphrase, not against physics** — it is comparable to π0.5 on position perturbation and only wins decisively on instruction changes.

**[BEHAVIOR](../entities/behavior-benchmark.md)** (Table 3, R1Pro wheeled humanoid, **25 trials/task**), navigation / task success:

| Task | Human | S3 | CaP-Agent0 |
|---|---|---|---|
| Pick up Radio | 88% / 36% | 72% / 24% | 80% / **56%** |
| Pick up Soda Can | 80% / 72% | 52% / 32% | **84%** / 72% |

CaP-Agent0 exceeds the *human expert* on radio task success (56% vs 36%) by repositioning for a better view when occluded — the human and S3 baselines both fail on lost sight lines.

### CaP-RL — RL on the coding agent, and what actually transfers (§5)

- GRPO post-training of **Qwen2.5-Coder-7B-Instruct**, 50 iterations per task, on 3 tasks. Trained on **S1 privileged APIs** to avoid noisy reward from compounding perception error, then **evaluated on S2** (noisy perception).

| Method | Cube Lift | Cube Stack | Spill Wipe | *Real* Cube Lift | *Real* Cube Stack |
|---|---|---|---|---|---|
| Human Expert | 93% | 73% | 100% | 92% | 84% |
| Qwen2.5-Coder-7B | 25% | 4% | 30% | 24% | 12% |
| **Qwen w/ CaP-RL** | **80%** | **44%** | **93%** | **84%** | **76%** |

Simulation **N=100/task**; real world **N=25/task** on a [Franka Emika Panda](../entities/franka-panda.md).

- **The sim-to-real mechanism is the paper's cleanest conceptual contribution:** what crosses the reality gap is the **code-as-action-space**, not a visuomotor mapping. "The agent learns to compose shared perception and control tools that are fixed across simulation and reality, rather than mapping raw visual features to motor commands." A 7B model gains **+60 pp** on real cube lift from *simulation-only* RL.

### CaP-Gym infrastructure (§2)

- **187 tasks**: 7 [Robosuite](../entities/robosuite.md) + 130 [LIBERO-PRO](libero-pro-paper.md) + 50 [BEHAVIOR](../entities/behavior-benchmark.md). Gymnasium interface binding a low-level environment loop to a stateful **Code Executor** REPL; one "turn" = agent receives observations, emits a Python program, environment runs it to completion.
- Perception primitives: **SAM3** (language-conditioned segmentation), **[Molmo 2](../entities/molmo2-er.md)** (open-vocabulary pointing), OpenCV, Open3D. Control primitives: motion planners and IK via **PyRoki** — agents reason in Cartesian space and delegate feasibility. All primitives are **stateless services** for high-throughput parallel evaluation.
- Deliberately designed so the same interface drives **real hardware**: zero-shot demos on [Franka Panda](../entities/franka-panda.md) and **[AgiBot](../entities/agibot.md) G1** with no major cross-embodiment change "with the exception of single arm to bimanual control primitive modifications."

## Entities mentioned
- [NVIDIA GEAR](../entities/nvidia-gear.md) · [NVIDIA](../entities/nvidia.md) · [Ken Goldberg](../entities/ken-goldberg.md) · [Jim Fan](../entities/jim-fan.md) · [Yuke Zhu](../entities/yuke-zhu.md) · [Letian (Max) Fu](../entities/letian-fu.md)
- [CaP-X](../entities/cap-x.md) (the framework as an entity) · [Robosuite](../entities/robosuite.md) · [LIBERO](../entities/libero.md) · [BEHAVIOR](../entities/behavior-benchmark.md) · [MuJoCo](../entities/mujoco.md)
- [OpenVLA](../entities/openvla.md) · [π0](../entities/pi-zero.md) · [Molmo 2](../entities/molmo2-er.md) · [Anthropic](../entities/anthropic.md) (Claude Haiku 4.5 / Opus 4.5 among the 12 models)
- [Franka Panda](../entities/franka-panda.md) · [AgiBot](../entities/agibot.md)

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — the paper is now this page's primary measured source.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — CaP-Bench's S1–S4 tiers are an empirical *sub-ladder inside* Anthropic's "level 2 / programmatic control."
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — 100 trials/task, N=7 human baseline, disclosed protocol.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Agent skills](../concepts/agents/agent-skills.md) — the auto-synthesized library.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — code-as-action-space as the transfer object.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — RLVR/GRPO applied to the *code writer*, not the policy.
- [VLA models](../concepts/learning/vla-models.md) — the comparison class.

## Open questions
- **The human baseline is the authors themselves** (N=7). They designed the API and the tasks. 88.5% is described as a "near-upper-bound," but author-written reference solutions on an author-designed API is a favorable measurement for the *ceiling* and an unfavorable one for claims of "exceeding human performance." An independent expert baseline would settle it.
- **Does the CaP-Bench ranking survive its sample sizes?** 100 trials/task is well above the field norm, but the CaP-Agent0 ablation chain (55 → 59 → 66 → 68) contains steps of 4 pp and 2 pp — see the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md); at n=700 (7 tasks × 100) a 2 pp step is not separable.
- **CaP-Agent0's cost is unreported in the comparison.** It issues up to 9 parallel model queries per turn across three frontier models, multi-turn. The "training-free" framing is true but relocates cost from training to inference; no token or wall-clock accounting appears alongside the VLA comparison, which makes the head-to-head with a single forward-pass VLA policy an unequal-compute comparison.
- **Why does π0.5 beat CaP-Agent0 on `libero-goal` Pos (0.38 vs 0.26) and `libero-spatial` Pos (0.20 vs 0.12)?** The paper emphasizes the instruction-perturbation win and does not analyze where the trained policy still leads.
- **Molmo 2 and SAM3 are load-bearing** but neither is ingested in this wiki; the perception stack's own error rate is not separated from the agent's reasoning error except at tier S1.

## Related sources
- [ASPIRE](aspire-paper.md) — built on CaP-X; CaP-Agent0 is its baseline.
- [Introducing Waddle](waddle-labs-introducing-waddle.md) — the deployed commercial claim this paper supplies the missing numbers for; Waddle cites CaP-X as ref [13].
- [LIBERO-PRO](libero-pro-paper.md) — the perturbation suite CaP-Bench++ uses.
- [How Claude Performs on Robotics Tasks](anthropic-how-claude-performs-on-robotics-tasks.md) — the wiki's other LLM-drives-robot measurement, at a different abstraction level.
