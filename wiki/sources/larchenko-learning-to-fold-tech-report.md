---
title: "Learning to Fold: prizewinning solution at LeHome Challenge 2026 (Larchenko, 2026)"
type: source
url: https://arxiv.org/abs/2606.27163
local_path: raw/larchenko-learning-to-fold_2606.27163.pdf
sha256: 0c0adcddacec9c389e7e36e00ca38983bd75ffbae9253964c799c1543b9af995
author: "Ilia Larchenko (independent researcher)"
published: 2026-06-25
ingested: 2026-09-07
venue: "arXiv cs.RO; read at v2 (2026-07-18). v1 (2026-06-25) carried a CUPED-coefficient error the author corrects in v2 (§6.2) — v1 not retained. Code github.com/IliaLarchenko/lehome_solution; checkpoints HF IliaLarchenko/lehome_sim and lehome_real"
format: paper (25 pp; engineering case study, self-described 'not a controlled experiment')
tags: [lehome, icra-2026, so-arm101, bimanual, garment-folding, deformable, rl, vla, pi0.5, flow-matching, awr, recap, cfg, best-of-n, thompson-sampling, reward-shaping, gae, cuped, asynchronous-rl, hugging-face-hub, isaac-lab, domain-randomization, sim-to-real, dagger, camera-alignment, units-bug, competition, primary]
---

# Learning to Fold — the tech report

The primary behind the [Part 1 video](larchenko-lehome-part1-rl-for-vlas.md). **1st of 62** in the LeHome 2026 simulation round at **79.63 %**, **2nd** in the ICRA real-world final at **865 / 1080**. The author's own framing is the right one to keep: *"an engineering case study, not a controlled experiment … I describe what I did and what shipped, not which pieces were necessary."* What the report adds over the video is everything in Parts 2 and 3 that had not yet been released — reward and advantage design, inference-time tuning, the full leaderboard, data scale, and the one-week sim-to-real sprint — plus a self-reported maths error and a units bug.

## Summary

A π0.5-derived VLA (frozen SigLIP-So400m → Gemma-2B prefix → Gemma-300M flow-matching expert, 30-step 12-D delta chunks, three 224×224 cameras, **no language input**) is improved by an asynchronous RL flywheel of one training worker, any number of rollout workers, and a manual DAgger station, sharing state only through Hugging Face Hub repositories. Advantage is consumed twice: **AWR through the data-loader** (`P(frame) ∝ exp(clip(A,−2,2))`, with inverse-sampling importance weights so the auxiliary heads stay unbiased) and **RECAP-style conditioning** of the action expert (an advantage token plus an AdaRMS channel), which enables classifier-free guidance at inference. **The policy is its own value function**: linear heads off one image-only query token predict success, completion, garment type, and the challenge's own keypoint-distance ratios; a second query at the tail of the action expert predicts those quantities 30 frames ahead plus a stop-gradient **success residual** used as a Q-like score for best-of-N. Reward is the binary success densified into keypoint checkpoints with all reward withdrawn on failure; advantages come from GAE over a CUPED-dampened success baseline and a potential-based completion term, blending toward a GRPO-style outcome-only segment baseline as rollouts go stale. Seven inference knobs are tuned per garment type by a Thompson-sampling bandit during rollout collection. Sim-to-real in one week: strip every sim-only head, fine-tune a late-but-not-latest checkpoint on a 60/30/10 mix of organiser BC, own teleop + DAgger, and augmented sim replays, with a camera-overlay alignment tool, per-source motion-speed factors, and very heavy augmentation.

## Key claims

### Protocol (§1, §8)

- Sim round: **20 garments per type** (10 seen with organiser BC data; 10 unseen, of which 2 public and 8 private), each **× 10 episodes**, binary full-fold success only, 30 Hz, Isaac Lab. Real final: **5 garments per type** (3 seen, 2 unseen), partial credit, organisers' jury, **unseen garments carry a 50 % bonus**, maximum 1080, 20 Hz. Garment category is **never given** at evaluation.
- Depth from the overhead camera was available and unused. The simulator's shaped "niceness" reward was available and unused.

### Leaderboard (Table 5, Table 7)

| Rank | Sim round (overall / long top / short top / long pants / shorts) | Real final |
|---|---|---|
| 1 | **ilya 79.63 % / 74.5 / 70.0 / 80.5 / 93.5** | sZs 895 |
| 2 | Shubham @ Vorwerk 73.50 / 73.0 / 62.5 / 71.5 / 87.0 | **ilya 865** |
| 3 | Dum-E 73.38 / 76.5 / 62.0 / 75.5 / 79.5 | Dum-E 762.5 |
| 4 | SCUT-Unlimited 73.13 | SCUT-Unlimited 635 |
| 5 | GraspYesAI 70.63 | sisigakgak 570 |
| 6 | sZs 69.63 | Shubham @ Vorwerk 470 |

Top outright on three types, third on long tops (77.0 and 76.5 ahead). Short tops hardest for nearly everyone; shorts easiest. **Unseen garments *"barely an issue"*** — only slightly below seen — with one miss on a long-pants instance that *"looked like shorts even to me."*

### Scale and training (§2.6, §8.2)

- **~12,500 retained rollout episodes (~4.3 M frames) over ~140 sessions**, cumulative *"a few times larger"*; ~30 s per episode; 3–5 Isaac Sim processes per machine behind one stateless policy server.
- One H200, batch 192, **~300 k steps**; 20 k-step BC warm-up; cosine LR 1e-4 → 1e-5 over 100 k; frozen SigLIP; 5 flow samples per item; trainer iteration ≈ 1000 steps, checkpoint every ~500.
- Rollout datasets decay ×0.98 per iteration (floor 0.1); BC sampled ∝ `exp(3(1−SR_garment))`; **checkpoint rollbacks** (3 in round 1, 1 in round 2) — retrain a days-old checkpoint on everything collected since, which *"reliably kicked the policy out of local optima"*; he notes π*0.6 does this systematically.
- The author's own verdict: *"I would not call this approach sample-efficient."*

### Architecture (§4–5)

- Carried over from his BEHAVIOR-1K winner and **not claimed here**: no text, correlated flow noise (empirical action covariance, shrinkage 0.5), correlation-aware soft inpainting at chunk boundaries, cross-layer KV-cache mixing, multi-sample flow matching.
- New: hierarchical attention groups (images + current query | state (256-bin discretised) + garment token | advantage token | FAST tokens + FAST query, training-only); advantage token masked always when A < 0 and stochastically when A ≥ 0 (P(neutral) 0.5 → 0.1 as A goes 0 → 2); **AdaRMS** carries flow time + garment + advantage; **Exclusive Self-Attention** (Zhai 2026) in both transformers, adopted on *"recent fashion"*; **per-timestep action normalisation** with a smooth `a + s√t + e` std fit.
- Heads and loss weights (Table 2–3): success 0.05, TTC 0.05 (legacy), completion 0.02, garment 0.02, checkpoint 0.001, FAST 0.01, keypoint-distance 0.02 (21 outputs, per-type NaN-masked slices), future heads 0.01–0.1. **Success tail boost**: last 20 frames of successes × 20 on the BCE, because near-misses linger in visually identical "almost done" states. Extra weight decay 0.001 on head kernels; success labels smoothed toward the per-garment mean (α = 0.05).
- The keypoint world-model substitute is *"generally only available in simulation, since the targets require privileged data."*

### Reward and advantage (§6)

- Checkpoints from the challenge's own conditions (5 tops / 4 shorts / 4 → 7 long pants): mid-fold 0.5, full 1.0; for tops the first 0.5 is **allocated gradually** as the primary proximity distance closes; on failure **all reward is withdrawn**, spread from the last frame of maximum cumulative reward, so the return is exactly the success indicator.
- Value = `P(success) − R_cum` from the success head. Two problems with plain `return − V`: checkpoint rewards cancel, and the variance argument assumes a perfect predictor. He borrows **CUPED** (A/B-testing control variates): the optimal coefficient is `θ* = ρ(V̂, G)·σ(G)/σ(V̂)`, estimable from rollouts. **Self-reported mistake**: during the competition (and in v1) he believed θ* uncomputable and used a fixed **α_s = 0.5**; post-hoc the true per-garment value was **0.4–0.8, median ≈ 0.5**, *"so the mistake was not critical."*
- EMA smoothing (0.2), a **value tail correction** interpolating the last 30 frames toward the known outcome, a completion head as a second, policy-stable signal (trained on successes only), **GAE γ = 0.999, λ = 0.99** over both; stale rollouts blend from GAE toward a **GRPO-style per-garment segment baseline** with weight = current sampling share; **precision boost** +0.3 on the tightest 20 % of successes; global std normalisation, clip [−2, 2]. His own summary: *"over-engineered and could probably be simplified without losing much."*

### Inference (§7, Table 4)

- H = 30, 10 Euler steps; per-type executed actions **3–5**, playback stretch = executed, anchor 3–6, inpainting onset 0.4–0.5, **CFG scale 7–9**, noise temperature **0.7–0.9**, candidates **2–3**. Best-of-N scores by the average of conditional and unconditional Δsuccess, with a retry on all-negative.
- **Tuned online by a factorised Thompson-sampling bandit** (Beta arms per parameter, reward = success − per-type SR, posteriors decayed each iteration, only unbiased rollouts update it, frozen for submission). The bandit's drift is itself evidence: guidance kept pinning to the top of a 0–2 range until he moved it to 5–11; N > 3 never helped; short execution windows always won.
- **A candid oddity**: *"The correlation between the FM head's prediction and the actual outcome was effectively zero in all my experiments — yet 2–3-candidate rollouts consistently beat single-candidate ones."* His hypothesis is that best-of-N only matters at rare multimodal bottleneck states, avoiding the worst chunk.

### Sim-to-real (§9) — one week, never touching the evaluation robot

- **Why zero-shot failed**: overfit to rendering. The cleanest diagnostic in the report — resizing 640×480 → 224 directly vs 640 → 320 → 224, *"nearly invisible to the human eye,"* **dropped sim success significantly, and the auxiliary heads could perfectly tell the two apart**. Also the organiser's real data folded some types differently (other sleeve first; pants from the bottom; shorts rotated 180° in half the episodes), adding multimodality. And: *"sim → my robot → their robot,"* with the organiser BC set itself collected on a third rig.
- *"It was only when I assembled the real follower rig … that I realized we had been dealing with kids' clothes the entire time."*
- Recipe: late-but-not-latest checkpoint; **strip** the keypoint head, both future heads, advantage conditioning, CFG and best-of-N (no advantage exists on the real robot) — keep the action objective, garment and completion heads; fine-tune on **three buckets** (Table 6):

  | Source | Episodes / frames | Batch share | Per-frame rate |
  |---|---|---|---|
  | Organiser BC | 500 / 187 k | 60 % | ×1.00 |
  | Own teleop + DAgger | 321 + 471 = 792 / 451 k | 30 % | ×0.21 |
  | Sim success replays | 1,723 / 625 k | 10 % | ×0.05 |

- **Camera-overlay alignment tool**: drive the robot to a dataset frame's joint state, overlay live cameras on the frame (and sim renders on real frames) — shared with the organisers and other teams. Then deliberately **randomise his own rig** (cameras, recalibration, lighting) so no geometry is load-bearing.
- **Speed factors** per source so per-step deltas agree: organiser ×1.0, home teleop ×1.5, sim ×0.65, DAgger ×2.0, per chunk by anchor-frame origin.
- **DAgger weighting as a crude advantage**: human-correction frames highest; autonomous frames far from interventions low; **the 5 s before a takeover ramp to zero**. Rig: two leader + two follower arms, three-pedal foot switch, leaders tracking followers during autonomy for jump-free handover. Focusing on hard initial states *"may have been a mistake"* — the final's states were easier than expected.
- **The units bug**: between two LeRobot 0.4.x releases the SO-101 follower's default state switched from a normalised −100…100 range to **degrees**; the two look almost identical on screen and skew every joint by ~10 %; found **two days before the deadline**, fixed by post-processing.
- Discussion: the policy was unexpectedly robust to day-to-day rig drift (credited to rig randomisation + augmentation); *"cheap image augmentations are underused in robotics"*; the model *"is bigger than the task needs"*; exploration attempts *"mostly just push the chunk off the action manifold"*; recovery came only from humans. Regret: two toolkits — a **single pipeline** with a real-side value model driving conditioning, best-of-N and DAgger weighting *"gets well past where either round landed alone — my guess is 90 %+."*

## The wiki's read

- **This is the most complete account of an RL-post-trained VLA on the wiki's own hardware class, and its author keeps saying not to trust the parts.** Every mechanism is labelled un-ablated. Treat it as a menu with one proof of the whole, not as evidence for any item.
- **The CUPED correction is worth more than the CUPED trick.** A practitioner publishing *"I made a logical mistake here (carried into v1)"* with the post-hoc measurement that bounds the damage is rare; the substantive lesson is that a fixed 0.5 baseline dampening was inside the empirically optimal range, so a learned control-variate coefficient is a refinement, not a fix.
- **The resize-path test should be a standard sim-overfit diagnostic.** If auxiliary heads can classify the resampling path, the policy is fitting the renderer. It costs nothing and it predicted the transfer failure before the transfer was tried.
- **Best-of-N with a zero-correlation scorer is a warning about head predictions as evidence.** The gain is real on the leaderboard and the stated mechanism is untested. Anyone reusing the "policy is its own Q" idea should measure the scorer's correlation before trusting it.
- **"Unseen generalisation was barely an issue" is same-category, same-simulator generalisation.** It says nothing against the wiki's [OOD-collapse](../syntheses/world-models/generative-video-vs-jepa-world-models.md#a-third-jepa-failure-mode-measured-may-2026-out-of-distribution-collapse) concerns; the resize test is the OOD result here, and it went the other way.
- **The units bug is a LeRobot version gotcha the wiki's own projects can hit.** Filed on the [LeRobot](../entities/lerobot.md) and [SO-ARM101](../entities/so-arm101.md) pages.
- **The "one pipeline" regret is the design the wiki should carry forward**: a real-side value model so that advantage conditioning, best-of-N, and DAgger weighting all run on hardware. He estimates 90 %+; nothing tests it.

## Edition history

- **v1 (2026-06-25)** — stated the CUPED coefficient as uncomputable and reported the fixed α_s = 0.5 without the post-hoc range. Not retained in `raw/`.
- **v2 (2026-07-18)** — §6.2 corrected: θ* is estimable from observables; measured 0.4–0.8, median ≈ 0.5. This is the sealed edition.

## Entities mentioned

- [Ilia Larchenko](../entities/ilia-larchenko.md); co-authors of the BEHAVIOR-1K solution (G. Zarin, A. Karnatak) cited as [8].
- [LeHome Challenge 2026](../entities/lehome-challenge-2026.md) — organisers' benchmark paper is Li et al., arXiv 2604.22363 (un-ingested).
- [SO-ARM101](../entities/so-arm101.md), [LeRobot](../entities/lerobot.md), [Hugging Face](../entities/hugging-face.md), [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md).
- [Physical Intelligence](../entities/physical-intelligence.md), [π*0.6](../entities/pistar06.md) — RECAP, checkpoint restarts, RTC.
- [BEHAVIOR-1K](../entities/behavior-benchmark.md) — the 2025 challenge winner is now confirmed by citation [8].

## Concepts touched

- [RL for flow-matching VLAs](../concepts/learning/rl-for-flow-matching-vlas.md) — the full recipe with numbers.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the one-week sprint, filed as a section.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — DAgger weighting as advantage; recovery only from humans.
- [Flow matching](../concepts/learning/flow-matching.md) — correlated noise, soft inpainting, CFG on advantage, noise temperature.
- [Imitation learning](../concepts/learning/imitation-learning.md), [World model](../concepts/world-models/world-model.md).

## Open questions

- The one-pipeline experiment: a real-side value model on the 792 own episodes plus organiser data.
- Ablate sampler-weighting vs loss-weighting, AdaRMS, XSA, best-of-N — all named as untested.
- Is the FM-head scorer's near-zero correlation an artefact of stop-gradient plus flow-time weighting, or of conditional-head optimism?
- How much of 79.63 % is RL over the 20 k-step BC warm-up? Not reported.
- The organisers' benchmark paper (2604.22363) for the success checker and the unseen-garment protocol.
