---
title: "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization"
type: source
url: https://arxiv.org/abs/2510.03827
author: Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, Guowen Zhang, Duanfeng Chu, Pan Zhou, Lichao Sun
published: 2025-10-04 (v1); 2026-05-25 (v2)
license: CC BY 4.0
tags: [libero, libero-pro, evaluation, benchmark, memorization, generalization, vla, openvla, pi-zero, methodology, critique]
---

## Summary

The paper that says the wiki's LIBERO table may not be measuring what it appears to measure. LIBERO-PRO perturbs the benchmark along four axes — **manipulated objects, initial states, task instructions, environments** — and reports that models scoring **over 90% on standard LIBERO collapse to 0.0%** under the generalized setting. The diagnosis is **memorization**: in standard LIBERO, *"evaluation tasks are identical to the training tasks, differing only by marginal perturbations in initial object states — variations so subtle as to be visually imperceptible."*

The behavioral evidence is damning in a specific way: models **continue executing the grasp when the target object is replaced**, and their **outputs are unchanged when instructions are corrupted into "messy tokens."** A policy that ignores the instruction and ignores the object is not doing language-conditioned manipulation; it is replaying a trajectory.

## Key claims

- **Standard LIBERO is train-on-test in all but name.** The evaluation tasks *are* the training tasks; only initial object states differ, and only imperceptibly. The benchmark therefore rewards rote recall of action sequences and environment layouts.
- **>90% → 0.0%.** Models achieving over 90% under the standard protocol collapse to zero under LIBERO-PRO's generalized setting. Position/configuration changes are the most destructive: near-0% for **OpenVLA** and **π0**; **π0.5** reaches 0.38 success and is the most robust of the three, but still degrades severely.
- **Instruction sensitivity is near-total.** Models show "severe sensitivity to even minimal instruction paraphrasing," and unchanged outputs under corrupted instructions — i.e. the language channel is largely inert.
- **Object substitution does not register.** Replacing the target object does not stop the grasp.
- **Models evaluated:** OpenVLA, π0, π0.5.

## The protocol detail that settles a wiki question

> *"Consistent with the original LIBERO protocol, we set the number of evaluation episodes to **50 per task**."*

This is the number the wiki has been missing. LIBERO suites hold **10 tasks each**, so:

- **n = 500 evaluation episodes per suite**
- **n = 2,000 for a four-suite average**

Those are exactly the two sample sizes the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) computed against as *assumptions*. **They are now confirmed**, so every verdict in that page's section A is grounded rather than provisional.

> [!warning] But the confirmation matters less than the collapse
> The audit established that the top of the wiki's LIBERO table (96.5–98.1) is one **statistical tie**. LIBERO-PRO makes the stronger claim that the entire band may be **measuring memorization**. A tie among numbers that don't measure generalization is a second-order problem. **If the 0.0% result holds, the LIBERO column ranks nothing, tied or not.**

## What this does and does not overturn

**Does not overturn:** LIBERO-PRO is a critique of the *benchmark*, not of the training recipes. OpenVLA-OFT's 76.5 → 97.1 improvement is a real effect *on this benchmark*, and the recipe (parallel decoding + action chunking + continuous L1 head) has independent evidence behind it, including a 25 Hz real bimanual [ALOHA](../entities/aloha.md) result. Real-world evaluations in the wiki — MolmoAct2's DROID and YAM numbers, GR00T's G1 post-training, [RoboArena](roboarena-paper.md)'s rankings — are untouched by this.

**Does overturn:** any claim that a high LIBERO score demonstrates *generalization*. And it sharpens the [RoboLab](nvidia-robolab-evaluation-blog.md) saturation critique from "the benchmark stopped discriminating above 90%" to "**the benchmark above 90% may be measuring recall**." Two independent 2025–26 groups converged on the conclusion that the field's most-reported robot-learning benchmark is broken, by different routes.

## Entities mentioned

- [LIBERO](../entities/libero.md) — the benchmark under critique.
- [OpenVLA](../entities/openvla.md), [π0](../entities/pi-zero.md), [π0.5](../entities/pi-zero-6.md) — the models evaluated.

## Concepts touched

- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — memorization as a distinct failure mode from sample size.
- [VLA models](../concepts/learning/vla-models.md) — the models whose scores are in question.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — a benchmark that rewards memorization teaches nothing about transfer.

## Open questions

- **The full per-model × per-perturbation table was not captured** at this ingest depth. What is recorded: >90% → 0.0% headline, near-0% for OpenVLA and π0 under position perturbation, π0.5 at 0.38. The per-axis breakdown (objects vs instructions vs environments) needs the paper's Figure 7 read directly.
- **Do the 2026-class models survive better?** OpenVLA, π0, and π0.5 are the tested set. **MolmoAct2, GR00T N1.7, and OpenVLA-OFT — the models at the top of the wiki's LIBERO table — were not evaluated.** Whether the newest models are less memorization-bound is the single most important open question this paper raises for the wiki.
- **Has LIBERO-PRO been adopted?** A benchmark critique only bites if people report the harder number. No evidence either way at ingest.
- **Is 0.0% literal?** The claim is stated as a collapse to zero under "our generalized setting" — whether that means the union of all perturbations or a specific one is not fully pinned down here.

## Adoption watch (updated 2026-08-03)
- [vla-evaluation-harness](vla-evaluation-harness-github.md) — LIBERO-Pro is a supported benchmark with 2026-class models (MolmoAct2, GR00T N1.7, π0.5) available in the same system; the "run a 2026-class model through LIBERO-PRO" question is no longer blocked on tooling.
- A June 2026 paper (arXiv 2606.27663, "Direct Action-Head Injection…") appears to report expanded LIBERO-PRO evaluations incl. GR00T-N1.6 — **lead, not yet ingested**; its numbers differ from this paper's protocol, so verify before quoting.
- Version note: this page reflects **v2 (2026-05-25)**, the current arXiv version; the wiki's recorded numbers were re-checked against it 2026-08-03 and stand.
