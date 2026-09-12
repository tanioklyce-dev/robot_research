---
title: "FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning (Liu, Li et al., RSS 2025)"
type: source
url: https://arxiv.org/abs/2502.17432
local_path: raw/2502.17432.pdf
sha256: 8d59e64b4e599f6cbb67096647f546b28fccca5ceaa7ef86df8500fbc3c4fcab
author: "Jason Jingzhou Liu*, Yulong Li*, Kenneth Shaw, Tony Tao, Ruslan Salakhutdinov, Deepak Pathak (*equal contribution)"
affiliations: "Carnegie Mellon University"
published: 2025-02-24
revised: 2025-04-24 (v2)
venue: "Robotics: Science and Systems (RSS) 2025, doi:10.15607/RSS.2025.XXI.079"
format: paper (15 pp; 9 pp body + references + appendix)
arxiv: 2502.17432
project_page: https://jasonjzliu.com/factr/
tags: [force-feedback, teleoperation, bilateral, leader-follower, GELLO, curriculum, modality-attention, contact-rich, behavior-cloning, ACT, franka-panda, NTK, cmu, pathak]
ingested: 2026-09-12
---

# FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning

## Summary

**Two fixes for the fact that force is available on good arms and ignored by everyone.** First, a **bilateral low-cost leader–follower rig**: GELLO-style 3D-printed leader arms with off-the-shelf servos, but *actuated*, so the follower's sensed external joint torque is played back to the operator's hand (scaled, with a damping term), with gravity and friction compensation, a null-space law to hold a user-chosen rest posture, joint-limit potentials, and gripper force feedback from the servo current. In a user study across four contact-rich tasks that gives **+64.7% completion rate, −37.4% completion time, +83.3% ease of use** over an un-actuated leader arm, whose users kept losing contact and tripping velocity limits.

Second, **FACTR**, a training curriculum for using the force channel in behaviour cloning. The problem is stated plainly: contact torque *"remains close to zero for significant periods,"* so a policy given vision and force *"tends to disregard force input and rely predominantly on visual information."* The fix is to **blur (or downsample) the visual input at the start of training and anneal the blur to zero**, in pixel or latent space, so the early gradient goes to the force encoder; a neural-tangent-kernel sketch shows why (at infinite blur the visual kernel is rank-one, so only the force path can separate examples). On unseen objects across box lifting, non-prehensile pivoting, fruit pick-and-place and dough rolling, an ACT policy goes from **21.3% (vision only) → 61.2% (vision + force, no curriculum) → 87.5% (FACTR)**; cross-attention to the force token rises at contact; and after a box is knocked down the FACTR policy retries (**27/30**) where the vision-only one stays still (4/30).

> [!note] Scope
> Four tasks, 50 demonstrations each, 5–10 trials per object; the policy is ACT with a pretrained ViT; the arms are [Franka Pandas](../entities/franka-panda.md) with OpenManipulator-X grippers, i.e. the method **assumes joint-torque sensing on the follower** — the limitation [FACTR 2](factr-2-paper.md) removes a year later. Curriculum hyper-parameters are task-dependent by the authors' own account, though the ablation finds *"no uniform advantage or disadvantage"* among operators and schedulers (Tab. II: 15–21 of 25).

## Key claims

### Teleoperation (Sec. III, V-B)

- Leader torque τ = τ_feedback + τ_null + τ_grav + τ_friction + τ_limit; feedback τ = μ_f K_p τ_ext − K_d q̇, with K_p the leader/follower max-torque ratio and *only external* torques relayed, so the operator does not feel the follower's inertia or friction (contrast Kobayashi et al.'s position-error bilateral coupling).
- Null-space projection (I − J†J)(−K_p(q − q_rest) − K_d q̇) lets the user set the rest posture, which matters in confined spaces (Fig. 3); gravity compensation by RNEA; Riemannian motion policies for bimanual self-collision avoidance.
- Gripper feedback from servo current with an EMA (α = 0.1). Bill of materials in Appendix VIII / Table III: **~$1,230 per leader arm with gripper** at the time of publication.
- User study, four tasks: completion +64.7%, time −37.4%, ease +83.3%. Failure mode of the baseline: without feeling contact, users drift the leader far from the follower; on release the PID slams the follower past velocity limits.

### Policy (Sec. IV, V-C)

- Encoder–decoder transformer: ViT vision tokens + one MLP force token → encoder → k action tokens cross-attend → joint-position chunk; MSE loss.
- **Curriculum operators**: Gaussian blur or max-pool downsampling, applied to pixels or to the ViT latent sequence; schedulers constant / linear / cosine / exponential / step, with a warm-up at full blur *"to warm-up the randomly initialized force encoder."*
- **NTK argument** (App. VII): with blur σ → ∞ all inputs map to the same vector, the kernel matrix becomes rank-one, and gradient flow can only fit a global constant through vision — so early learning must go through force.

| Unseen objects, avg success | Vision-only ACT | ACT + force | **FACTR** |
|---|---|---|---|
| Four tasks | 21.3% | 61.2% | **87.5%** |

- Train-object success is similar across methods except dough rolling, where vision-only *"smashes the dough without any rolling"* — visual frames during oscillatory rolling are near-identical while torque oscillates (Fig. 8).
- **Recovery** (Tab. I, box knocked down after first lift): vision-only 4/30, +force 16/30, FACTR **27/30**; the torque *"revert[s] to pre-lift values when the object is dropped."*
- Attention (Fig. 9): with FACTR, force attention exceeds vision attention as the arms contact the box — *"signaling a mode switch."*
- Ablation (pivot task, 25 trials): fixed blur < any decaying schedule; pixel vs latent, blur vs downsample, and scheduler choice are within noise.

## Why it matters in this wiki

- **The origin of the FACTR line.** [FACTR 2](factr-2-paper.md) keeps the teleoperation controller and replaces the sensor requirement with a learned free-space model; it also drops this paper's blur curriculum for phase-based up-sampling, and reports the curriculum as a baseline it beats.
- **A modality-imbalance result with a mechanism.** The wiki's [contact-rich](../concepts/robotics/contact-rich-manipulation.md) and [tactile](../concepts/robotics/tactile-sensing.md) pages argue that force must be *sensed*; this paper shows sensing it is not enough — a policy will ignore a sparse channel unless training makes it look — and the NTK sketch says why.
- **Teleoperation hardware.** An actuated GELLO with force feedback, gravity compensation and null-space posture control, at low cost; the [imitation-learning](../concepts/learning/imitation-learning.md) page's data-collection thread has no other bilateral rig.

## Entities mentioned

- [Franka Panda](../entities/franka-panda.md) — follower arms (joint-torque sensing); OpenManipulator-X grippers; ZED2 and wrist cameras.
- [Deepak Pathak](../entities/deepak-pathak.md), Ruslan Salakhutdinov, Kenneth Shaw, Tony Tao, Jason Liu, Yulong Li — CMU.

## Concepts touched

- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) · [Imitation learning](../concepts/learning/imitation-learning.md) · [Impedance control](../concepts/robotics/impedance-control.md) (the leader's compliance laws) · [Tactile sensing](../concepts/robotics/tactile-sensing.md)

## Open questions

- **Torque-sensor precision** on the Franka limits fine tasks (authors' limitation); FACTR 2's learned estimate is *less* noisy than the sensor in free space.
- **Does the curriculum transfer to diffusion / flow policies?** Only ACT here; FACTR 2 runs both and finds the curriculum is beaten by up-sampling.
- **Trial counts** — 5–10 per object; the headline is an average over few objects.
