---
title: "FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning (Oh, Liu, Tao et al., 2026)"
type: source
url: https://arxiv.org/abs/2606.12406
local_path: raw/2606.12406.pdf
sha256: 6bf6e00df93b068787ff4efeec0375a238597ca0fccb3b587394e7aed64e792c
author: "Steven Oh*, Jason Jingzhou Liu*, Tony Tao*, Philip Han, Kenneth Shaw, Satoshi Funabashi, Ruslan Salakhutdinov, Deepak Pathak (*equal contribution)"
affiliations: "Carnegie Mellon University; Waseda University"
published: 2026-06-10
revised: 2026-08-12 (v2; text substantively identical to v1 — layout changes only on a word-level diff)
venue: "arXiv preprint, CoRL-style formatting; no peer-reviewed venue as of ingest"
format: paper (22 pp; 8 pp body + references + appendix)
arxiv: 2606.12406
project_page: https://jasonjzliu.com/factr2
tags: [force-sensing, external-torque-estimation, motor-current, inverse-dynamics, LSTM, force-feedback-teleoperation, contact-rich, data-reweighting, behavior-cloning, agilex-piper, yam, franka-panda, leap-hand, flow-matching, ACT, cmu, pathak]
ingested: 2026-09-12
---

# FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning

## Summary

**Force sensing for arms that have no force sensor, from ten minutes of waving the arm around.** NEXT (Neural External Torque estimation) trains a two-layer LSTM on ~10 minutes of contact-free motion to predict the motor torque (from motor current × torque constant) that free-space motion *should* need, given a 50-step history of joint positions, velocities and tracking error; at deployment the external torque is the residual between measured and predicted. Training takes about a minute on an RTX 3090; inference is 1.76 ms on one CPU thread. On a [Franka](../entities/franka-panda.md), whose built-in joint-torque sensing serves as ground truth, NEXT's contact-phase error is **0.547 Nm** against **1.47** for a momentum disturbance observer and **4.40** for a model-based inverse-dynamics residual — and in free space it is *less noisy than the Franka's own sensor* (0.414 vs 0.449 Nm). On a **$2,500 [AgileX Piper](../entities/agilex-piper.md)** with no sensor, free-space error is 0.018 Nm.

The estimate is then used twice. For **force-feedback teleoperation**, a 20-participant study on the Franka rated NEXT-based feedback easier than no feedback, a disturbance observer, or position–position coupling, and comparable to the original FACTR system using the dedicated sensors. For **policy learning**, FIRST (Force-Informed Re-Sampling Training) uses the torque signal only to *label* demonstration frames as free-space, pre-contact (the second before contact onset) or contact, then **up-samples the pre-contact and contact frames** in each minibatch. Across five long-horizon contact-rich tasks on a bimanual Piper (250 demonstrations each, 20 rollouts) FIRST beats the base policy, base + torque input, FACTR's visual curriculum, and TA-VLA's auxiliary loss, by *"over 17% in task progress."* The sharpest secondary finding: **up-sampling *pre-contact* frames alone (1 : 5 : 1) does more than up-sampling contact frames** — *"the moments before contact are especially important as they determine reaching the correct pose and alignment"* — and re-weighting the *loss* instead of the *sampling* does not work.

> [!warning] This paper does not contain the claim Skild's S1 post cites it for
> [Skild's S1 announcement](skild-s1-blog.md) cites *"Oh et al., 2026"* — this paper — for the premise that *"when post-training data is sufficiently large and provides dense coverage of the task, even policies trained from scratch with no pre-training can match the peak performance of a post-trained foundation model."* **Neither v1 nor v2 of FACTR 2 makes that comparison.** It never post-trains a foundation model; every policy here is an ACT or flow-matching head *"randomly initialized and trained from scratch,"* and the words *pre-train*, *foundation model* and *post-train* do not appear outside the reference list. Whatever Skild meant — perhaps that from-scratch policies on 250 demonstrations reach high task progress, which the paper does show — the specific sentence is not FACTR 2's. Recorded on the S1 page as a misattribution.

## Key claims

### NEXT — external torque without a sensor (Sec. 4, 6.1, Tab. 1, App. A)

| Setting (Franka, L1 error, Nm) | FILIC (model residual) | Disturbance observer | Built-in sensor | **NEXT** |
|---|---|---|---|---|
| Contact (vs factory external-torque estimate) | 4.395 | 1.471 | 0 (reference) | **0.547** |
| Free space (vs zero) | 2.460 | 2.429 | 0.449 | **0.414** |

- Input `[q, q̇, Δq_d]` over **H = 50** steps at 100 Hz; the tracking-error term *"provides useful information about controller effort and actuator response"*; LSTM > GRU > MLP, and the LSTM gains most from longer history (Tab. 4). Stateless sliding window, so no hidden-state drift.
- No system identification, no payload calibration, no sensor at any stage. Data collection is a coverage procedure: each joint through its range, then Cartesian-like multi-joint motion, slow and fast; *"recorded once and replayed on new robot setups."*
- **Limitations stated**: absolute scale depends on the manufacturer's torque constant *K* (fine for teleop and normalized policy inputs, needs calibration for absolute force); robot-specific, retrain per arm.
- Piper free-space: **0.018 Nm** vs 0.248 (observer) and 0.435 (FILIC); contact cannot be evaluated on the Piper (no reference sensor), so the teleop study stands in.

### Teleoperation (Sec. 6.1, App. A.5)

Five conditions on the Franka with 20 participants (GELLO leader, wiping task): no feedback, disturbance observer, position–position, FACTR Teleop with the built-in sensors, FACTR Teleop with NEXT. NEXT rated easiest to use and lowered applied joint torque *"comparably to FACTR Teleop, which uses dedicated joint torque sensors."* Repeated on the Piper minus the sensor condition. Ratings and torques are in figures; no numbers in text.

### FIRST — re-sampling by contact phase (Sec. 5, 7, Tab. 2, App. D)

- Phase labels from the L1 norm of estimated torque with hysteresis thresholds; pre-contact = the *F* frames (one second) before each onset.
- Five bimanual Piper tasks: LEGO assembly with **LEAP Hand V2**, NIST belt assembly, NIST insertion, tool clean-up (screwdriver insertion + case assembly), cap screwing (with an over-turn penalty of 0.02 per extra turn). 250 demos each; **20 rollouts**; metric is **task progress** (fraction of rubric stages), not binary success.
- Baselines share architecture and objective (flow-matching DiT with DINOv3-Base vision, chunk 30; repeated with ACT): base, base + torque input, FACTR (Gaussian-blur curriculum), TA-VLA (auxiliary torque reconstruction).

| Up-sampled phase (Tab. 2, flow matching) | Avg progress |
|---|---|
| Contact only (1 : 1 : 5) | 0.670 |
| **Pre-contact only (1 : 5 : 1)** | **0.818** |
| Pre-contact + contact (1 : 3 : 3 / 1 : 5 : 5) | 0.811 (best on cap screwing, 0.825) |

- Validation loss on pre-contact and contact frames is higher than on free motion under default sampling; up-sampling brings it down (Fig. 7) — the paper's mechanism claim.
- Magnitude sweeps peak around **5×**; larger *"can over-bias the training distribution."*
- **Sampling beats loss weighting** (Tab. 11, LEGO/ACT): weighted regression 0.345–0.478 vs FIRST 0.501–0.573 vs none 0.453 — *"directly increasing the loss contribution of sparse contact-related samples can make optimization less stable."*
- **Works without torque as a policy input** (Tab. 9): phase-based up-sampling alone improves ACT and flow matching, and adding the torque input on top is better again (e.g. flow matching, belt assembly: 0.150 → 0.213 → 0.767 with input + PC up-sampling).
- **Raw motor current is not enough** (Tab. 10, ACT): current helps NIST insertion (0.22 → 0.43) but not cap screwing (0.44 → 0.44); NEXT torque helps both (0.57, 0.53). Current-conditioned policies *"often continue rotating the cap after it is already tightened."* Attention to the force tokens spikes at the tightening event only for the NEXT-conditioned policy.

## Why it matters in this wiki

- **[Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md)** — the page's data argument is that force *"cannot be obtained from the web."* This paper's reply is that on the robot it can be obtained **without a sensor**, from current and a learned free-space model, on a $2,500 arm. It moves the cost of force data from hardware to ten minutes of setup.
- **The pre-contact finding.** Failures concentrate in the second before contact, and that second is where training weight pays. It is the same intuition as [FACTR](#lineage)'s original curriculum and [RoboTTT](robottt-paper.md)'s failures-as-context, stated as a data-mixture rule with an ablation.
- **[Tactile sensing](../concepts/robotics/tactile-sensing.md)** — joint-torque estimation gives a wrench at the joints, not a pressure map at the fingertips; the two answer different questions, and this paper is the cheap end of the wrist-side option.
- **[Imitation learning](../concepts/learning/imitation-learning.md)** — a data-reweighting result where *how* you emphasise (sampling vs loss) matters more than *that* you emphasise.
- **Platforms.** [AgileX Piper](../entities/agilex-piper.md) (bimanual, $2,500 each) and [YAM](../entities/yam.md) are named as arms this makes force-capable; the Franka is the reference.
- **[Deepak Pathak](../entities/deepak-pathak.md)** is last author while running [Skild](../entities/skild-ai.md) — and Skild's S1 post cites this paper for a claim it does not make.

### Lineage

FACTR (Liu, Li, Shaw, Tao, Salakhutdinov, Pathak; RSS 2025) — force-feedback teleoperation with dedicated joint-torque sensors plus a visual-blur curriculum for contact-rich policy learning. FACTR 2 generalises it *"beyond arms with dedicated force sensors."* Original FACTR is uningested.

## Entities mentioned

- [Franka Panda](../entities/franka-panda.md) — ground-truth platform; [AgileX Piper](../entities/agilex-piper.md) — the low-cost target and bimanual policy platform; [YAM](../entities/yam.md) — named as a supported low-cost arm (AIRe Lab loaned units).
- [Deepak Pathak](../entities/deepak-pathak.md), Ruslan Salakhutdinov, Kenneth Shaw (LEAP Hand) — CMU.
- [DINOv3](../entities/dinov3.md) — policy vision encoder.
- [Skild AI](../entities/skild-ai.md) — cites this paper in the S1 post.

## Concepts touched

- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) · [Tactile sensing](../concepts/robotics/tactile-sensing.md) · [Impedance control](../concepts/robotics/impedance-control.md) (where an external-torque estimate would feed) · [Imitation learning](../concepts/learning/imitation-learning.md) · [Flow matching](../concepts/learning/flow-matching.md)

## Open questions

- **Contact-phase accuracy on the Piper** — only free-space error is measurable; the user study is the proxy.
- **Success rates.** Task progress is reported; binary success only in the appendix tables for two tasks.
- **Does NEXT survive payload changes** (a grasped object changes the free-space torque)? Not discussed.
- **Transfer of the pre-contact rule** to policies with pretrained action heads — every policy here is from scratch.
- **Original FACTR** — uningested; the curriculum baseline here is its method.
