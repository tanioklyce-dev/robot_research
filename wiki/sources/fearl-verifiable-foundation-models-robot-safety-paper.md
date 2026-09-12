---
title: "Verifiable Foundation Models for Robot Safety — FEARL (Corsi, Kim & Fox, 2026)"
type: source
url: https://arxiv.org/abs/2606.23754
local_path: raw/2606.23754.pdf
sha256: f4aa4276f7030a846ce16ebca5484767f57cf31427ab03419d08a000e091530b
author: "Davide Corsi*, Kyungmin Kim*, Roy Fox (*equal contribution)"
affiliations: "University of California, Irvine"
published: 2026-06-22
venue: "arXiv preprint (v1), CoRL-style formatting; no peer-reviewed venue as of ingest"
format: paper (17 pp; 8 pp body + references + appendix)
arxiv: 2606.23754
tags: [formal-verification, runtime-shielding, safety, foundation-models, vla, smolvla, stretch-2, unitree-go2, lidar, neural-network-verification, epsilon-prove, sim-to-real, navigation]
ingested: 2026-09-12
---

# Verifiable Foundation Models for Robot Safety (FEARL)

## Summary

**Make a foundation-model policy formally verifiable by not verifying the foundation model.** FEARL (Foundation-Enabled Assured Robot Learning) splits the policy into a large **Controller C** — any backbone, including an off-the-shelf VLA — that compresses images and language into a bounded context vector *z* ∈ [−1, 1]^d, and a tiny **Safety module S** (a two-layer, 32-unit MLP) that takes *z* together with low-dimensional *safety sensors* (an 11-ray LiDAR scan, a planar pose) and emits the final action. Safety properties are written over the sensors only — *if any front ray is under 0.2 m, never move forward* — and are required to hold **for every possible context vector**, so *"Module S never selects an unsafe action in the specified sensor region regardless of what the foundation model perceives or infers from the high-dimensional inputs, and of any hallucinations it may have."* A neural-network verifier (ε-ProVe, extended to universally quantified context and multiple constraints) then certifies which region of S's input domain is provably safe; a runtime shield is consulted only outside that region.

Across a 2D playground, a simulated [Stretch 2](../entities/stretch.md) indoor-navigation task (custom LLM+ViT controller, and separately a [SmolVLA](../entities/smolvla.md) controller), and a simulated [Unitree GO2](../entities/unitree-go2.md) outdoor task, the verifier certifies **78.9–99.4%** of the safety module's input domain offline, and shielding drives violations to **zero** at override rates of **0.09–1.13%** of steps. A mapless variant transfers to a **physical Stretch 2** without retraining or re-verification: over 18 episodes, **61.1% success with zero collisions** shielded, against the same 61.1% success and a **27.8% collision rate** unshielded.

> [!note] Where the guarantee lives, and where it does not
> The certificate is over a 2-layer MLP's input box, probabilistic ((δ, ρ)-safe: ρ ≤ 0.5% false-positive volume at δ = 99.99%), and covers only constraints expressible on the safety sensors. The paper is explicit that this **excludes semantic safety** — *"recognizing that a glass cup should not be placed near the edge of a table"* — and all experiments use **discrete** action sets (3–4 actions). The bound ties the shield's performance cost to the *uncertified volume*, and one number shows what that cost can be: the SmolVLA variant loses **12 points of success** (80.1 → 68.2) when shielded, which the paper describes as a *"small performance drop."*

## Key claims

### Architecture (Sec. 3)

- Observation triplet (I_t, g, s_t): image, language, and a **safety sensor vector with well-defined semantics**. C maps (I, g) → z with a tanh so the domain is finite (a formal requirement: the verifier enumerates over S's whole input box). S maps [s; z] → action distribution.
- C is unconstrained: BERT+ViT fine-tuned with PPO+LoRA (playground); an LLM+ViT trained by SFT to a *structured* 12-D context (target one-hot, target positions, robot pose) then S by PPO (indoor); **SmolVLA** (SmolVLM2-256M backbone) with a 2-layer MLP adapter on the pre-action-head features to a learned 16-D context, LoRA + PPO end-to-end (indoor-VLA); ViT distilled from a low-dimensional PPO teacher by DAgger (outdoor, 128-D).
- S is always 2 × 32 units. ε-ProVe enumerates axis-aligned safe hyper-rectangles with a point cloud of 3,500 and depth 20.

### Three bounds (Sec. 4.1, proved in App. A)

With μ the normalized input measure and d̄ the policy's maximum state-occupancy density: violation rate ≤ ρ · d̄ · μ(certified); shield activation rate ≤ d̄ · μ(uncertified); value loss ≤ T · d̄ · μ(uncertified) · R_max. *"Minimizing μ(X_uncertified) through better training of Module S is therefore simultaneously a safety and a performance objective."* The bounds follow from the performance-difference lemma; they are loose (occupancy is bounded by its supremum) and the paper uses them qualitatively.

### Results (Tab. 2, 3; 100 episodes × 3 seeds)

| Environment | ds / dc | Certified volume (time) | Unshielded SR / VR | Shielded SR / VR | Override |
|---|---|---|---|---|---|
| Playground (2D) | 2 / 64 | **99.4%** (22.7 s) | 100 / 0 | 100 / 0 | 0.09% |
| Indoor nav, custom C (Stretch 2 sim) | 11 / 12 | 78.9% (1,522 s) | 73.1 / 1.3 | 71.3 / **0** | 0.12% |
| Indoor nav, **SmolVLA** C | 11 / 16 | 91.2% (2,691 s) | 80.1 / 2.7 | **68.2** / **0** | 1.13% |
| Outdoor nav (GO2 sim) | 3 / 128 | 82.7% (3,271 s) | 89.6 / 1.6 | 87.2 / **0** | 0.74% |

- Verification is offline, *"minutes to hours,"* and does not touch the control loop.
- Certified volume does not determine override rate on its own — occupancy does (Prop. 2): the indoor task has a smaller certified volume than outdoor and a lower override rate.
- The SmolVLA controller *"can follow out-of-distribution paraphrased instructions,"* so the 16-D bottleneck keeps usable language information.

### Sim-to-real (Sec. 5.5, App. G)

- Physical Stretch 2, ~2.5 × 1.8 m arena, three marked goals; mapless variant (language prompt + LiDAR only). Localization from an HTC Vive tracker at ~100 Hz; the 1,080-ray 360° LiDAR is reduced to the 11-ray 180° vector by nearest-beam selection, ±2-beam spatial averaging, 3–5-frame temporal averaging, max-range fill for dropouts, clip to 3 m. *"This preprocessing pipeline is the only hardware-specific modification."*
- Offline certification 77.1% (relaxed: 100 points, δ = 97.6%). **18 episodes: shielded 61.1% success, 0 collisions; unshielded 61.1% success, 27.8% collisions.** Shield active on 7.8% of steps against a 22.9% uncertified volume.
- The success drop from simulation is attributed to Vive drift and actuation noise in the *task* inputs; the shield's LiDAR input is insensitive to localization error. A representative failure: the tracker gave a wrong pose, the task estimate diverged, the robot still avoided every obstacle.

### Lineage

Verification-guided shielding (Corsi et al., RLC 2024), realizable continuous-space shields (Kim et al., L4DC 2025), and ε-ProVe (Marzari, Corsi et al., AAAI 2024) — the same group's line, now with a foundation model in front.

## Why it matters in this wiki

- **[Safety filters](../concepts/robotics/safety-filters.md)** — a fifth instance, and a different kind: the others (OSCBF, PACS, ATACOM behind Octo) filter a continuous action against a hazard geometry; this one **certifies a network** and shields only where certification failed. It answers that page's *perception* objection by construction — the safety spec is confined to sensors that measure the hazard directly — which is also why it cannot express anything the LiDAR cannot see.
- **[Semantic safety](../concepts/safety/semantic-safety.md)** — the page records that provable safety and semantic safety are *"disjoint literatures."* FEARL is a bridge that stops exactly at the boundary and says so.
- **[Safety certificates](../concepts/robotics/safety-certificates.md)** — a verified input region rather than a barrier or Lyapunov function; the "certificate" is a probabilistic statement about a small MLP.
- **The [prevention–detection–intervention](../syntheses/platforms/prevention-detection-intervention.md) layering** — a concrete *prevention* layer that composes with a VLA without touching its weights, and a measured cost (12 points on the VLA variant) for the composition.
- **SmolVLA** — the wiki's default low-cost VLA, here as a 256M-parameter backbone whose pre-head features are enough for a navigation task.

## Entities mentioned

- [Stretch](../entities/stretch.md) — Stretch 2, simulated and physical.
- [Unitree GO2](../entities/unitree-go2.md) — simulated outdoor navigation, low-level locomotion policy from Rudin et al.
- [SmolVLA](../entities/smolvla.md) — the off-the-shelf VLA controller variant.
- Roy Fox (UC Irvine) — no entity page.

## Concepts touched

- [Safety filters](../concepts/robotics/safety-filters.md) · [Safety certificates](../concepts/robotics/safety-certificates.md) · [Semantic safety](../concepts/safety/semantic-safety.md) · [Safe reinforcement learning](../concepts/learning/safe-reinforcement-learning.md) · [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — the shield is an *intervention* triggered by a certificate rather than a detector.

## Open questions

- **Continuous actions.** The framework is stated for them; every experiment is discrete. Verifying a 32-unit MLP over continuous output sets is the next test.
- **What the 12-point drop means.** On the VLA variant the shield costs more success than the custom controller. Whether that is the uncertified volume, the learned context, or the discrete action set is not separated.
- **Manipulation.** All three tasks are navigation with a workspace boundary or a range threshold. No contact, no object hazards.
- **How much task information fits in z?** 12–128 dimensions here; the paraphrase result is qualitative.
- **Eighteen real episodes.** Enough to show the shield removes collisions; not enough for a success-rate claim.
