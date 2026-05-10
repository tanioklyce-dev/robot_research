---
title: Underserved PAR domains — dressing, bathing, medication
type: synthesis
created: 2026-05-09
updated: 2026-05-09
tags: [assistive-robotics, par, dressing, bathing, medication, underserved-domains, exoskeleton, soft-robotics, hcrlab]
---

The [Nanavati, Ranganeni & Cakmak 2024 systematic review](../sources/nanavati2024-physically-assistive-robots-review.md) identifies **dressing, bathing/grooming, and managing medications** as the highest-priority research gaps in physically assistive robots. These domains have high user need (per IADL surveys) but proportionately little PAR research. Why? This synthesis enumerates what each task requires that current PAR systems do not deliver, what hardware or methods classes might unlock them, and what is realistic for an independent researcher to attempt.

> [!note] TL;DR
> The three underserved domains share a common pattern: each requires **safe sustained physical contact with a non-recoverable user** plus a task-specific failure-mode profile that the field's current pick-and-place / fetch toolkit doesn't address. Dressing needs deformable manipulation + skin contact; bathing needs water-tolerant hardware + body-aware compliance; medication needs precision + verification under regulatory constraint. None are purely a learning problem — each gates on a hardware or systems class where the wiki's robot-learning corpus has little to say.

---

## What the systematic review actually found

[Nanavati et al. 2024](../sources/nanavati2024-physically-assistive-robots-review.md) screened 1,981 papers and included 87 PAR studies. The domain distribution within the included set:

- **Three spikes** dominate: navigation, eating/feeding, pick-and-place / housework.
- **Three dips** are flagged as underserved relative to user need: **dressing**, **bathing/grooming**, **managing medications**.

The gap is not subjective — it's measured against IADL (Instrumental Activities of Daily Living) surveys of what people with disabilities and their caregivers report needing. The gap is also self-reinforcing: low engagement → fewer datasets → fewer benchmarks → fewer papers → low engagement.

---

## Dressing

### What the task actually requires

Dressing involves **manipulating deformable garments** *while* **sustaining safe contact with a moving body** *while* **respecting user pace and modesty**. None of the wiki's mainstream manipulation toolkit handles all three.

| Sub-capability | Wiki coverage | Notes |
|---|---|---|
| **Deformable cloth manipulation** | Thin. [RUM](../sources/robot-utility-models-paper.md) trains on tissue and bag pickup — small deformable objects. RoboCasa365 includes household items but not garments. No dedicated cloth-manipulation source. | Cloth-on-cloth grasping, sleeve threading, button alignment — all unrepresented. |
| **Body-aware physical contact** | [HCR Lab handover work](../sources/hcrlab-publications.md) — affordance-aware handover poses for users with mobility constraints (RA-L). But handover ≠ dressing. | Skin contact across multiple seconds is qualitatively different from instant transfer. |
| **Compliant arm hardware** | [tenoexo](../sources/relab-ethz-tenoexo.md) is a hand orthosis (5N/finger), not a dressing arm. [Stretch](../entities/stretch.md)'s arm is light (~2 kg payload) but not specifically compliant. | Need force-controlled, low-impedance arms. Soft robotics relevant. |
| **User-paced execution** | [Variable-LoC pattern](levels-of-autonomy-in-assistive-robotics.md) from [Nanavati 2025](../sources/nanavati2025-feeding-out-of-lab.md) is the right design pattern. | Conceptually transferable; not tested on dressing. |

### What might unblock dressing

- **Compliant manipulator class.** Either a soft-robotics arm or a force-controlled rigid arm operated under impedance/admittance control. [Virginia Tech Assistive Robotics Lab](../sources/virginia-tech-assistive-robotics-lab.md) (Prof. Alan Asbeck) works in adjacent territory — soft robotics, exoskeletons, haptics — but doesn't ingest as a dressing-specific source.
- **Cloth-state estimation.** No JEPA / world-model paper in the wiki demonstrates cloth-state representation. The closest is RoboCasa's household objects, which are mostly rigid.
- **Datasets.** No dressing-specific demonstration dataset in the wiki. RUM-style data collection (Stick-v2 + iPhone) doesn't capture cloth deformation cleanly.

### Realistic researcher target

A first-step contribution: **dressing-task demonstration dataset on Stretch with a single user with motor impairment**. Even 50 demos of "putting on a sleeve" with structured failure documentation would be useful. The [Multiple Ways of Working with Users](../sources/nanavati2024-multiple-ways-par.md) methodology applies directly — community researcher partnership, CBPR principles, off-nominal scenario co-design.

---

## Bathing / grooming

### What the task actually requires

| Sub-capability | Why it's hard |
|---|---|
| **Water-tolerant hardware** | Standard research robots are not IP-rated. A wet bathroom destroys most arms. |
| **Skin-safe contact under variable surface conditions** | Wet skin is slippery; soap is foamy; force feedback under these conditions is ill-conditioned. |
| **Body-aware path planning** | The arm must avoid eyes, mouth, ears, sensitive regions; depends on user posture. |
| **Privacy and dignity affordances** | Verbal interface needs to allow user to pause, resume, redirect — under conditions where the user may not be able to easily speak (water, soap). |
| **Regulatory clearance for water-environment medical devices** | Bathing is a hands-on personal care task; commercial products would face medical-device-class regulatory review (FDA in US, CE/MDR in EU). |

### What's published in the wiki

Almost nothing. The systematic review notes the gap. [tenoexo](../sources/relab-ethz-tenoexo.md) is dry. [Virginia Tech Assistive Robotics Lab](../sources/virginia-tech-assistive-robotics-lab.md) does soft robotics broadly. No bathing-specific source exists in the wiki.

### What might unblock bathing

- **Different hardware class entirely.** Research robots are not the substrate. A purpose-built water-tolerant bathing assistant (think hospital-bed lift + shampoo arm + hand-held companion device) is plausibly the right product shape — and is closer to medical-device engineering than to robot-learning research.
- **Hospital / care-facility setting first, home later.** Bathing assistance in a controlled clinical setting has fewer regulatory and integration unknowns than in-home.

### Realistic researcher target

This is the **least tractable** of the three underserved domains for an independent researcher. Hardware barrier is high; regulatory barrier is high; user-population access is high. A research contribution would more likely be a **needs assessment** ([Multiple Ways](../sources/nanavati2024-multiple-ways-par.md)-style structured interviews and design sessions with users + caregivers + occupational therapists about what bathing assistance would need to be) than a hardware prototype.

---

## Medication management

### What the task actually requires

| Sub-capability | Why it's hard |
|---|---|
| **Precision manipulation of small objects** | Pills are small (~5–15 mm); requires sub-cm gripper precision. Stretch's gripper is not sub-cm precise. |
| **Pill-bottle opening (child-safe / push-and-turn caps)** | Bimanual or specialized tooling. Stretch is single-arm. |
| **Verification — right pill, right dose, right time, right user** | High-stakes failure mode. A medication error is unrecoverable. Requires VLM-grade verification + audit trail. |
| **Integration with existing medication systems** | Pharmacy bottles, blister packs, pill organizers, liquid medications — heterogeneous form factors. |
| **Regulatory and liability** | Medication assistance approaches medical-device classification depending on jurisdiction. |

### Why it's underserved despite being tractable-looking

Medication looks easier than dressing or bathing — it's a discrete task with concrete success criteria. But the **failure cost asymmetry** is brutal: a 1% wrong-pill rate is unacceptable, while a 1% door-opening failure rate is fine. The reliability bar is set by the worst-case failure mode, not the average.

[Yang et al. 2025](../sources/yang2025-sense-of-agency.md) explicitly identifies medication as a high-risk task where users **strongly prefer user control over autonomy**. This is consistent with the failure-cost asymmetry: users intuit what the analytical reliability calculation says.

### What might unblock medication

- **Smart pill organizers + verification AI, not autonomous manipulation.** The right product shape may not be a robot at all — it may be a sensorized pill dispenser + VLM verification + audit trail + caregiver alerts. This sits closer to consumer health electronics than to PAR.
- **Robot as fetcher only.** Use a Stretch (or similar) to *bring* the user a pre-organized pill organizer; let the user (or caregiver) handle the medication-handling step. This reduces the robot's failure cost surface dramatically.
- **High-reliability verification.** mLLM-based verification ([RUM](../sources/robot-utility-models-paper.md)'s gpt-4o critic loop is the closest analog) might be a building block for "did the robot pick up the right pill?" Reported false-positive rate ~5% in RUM is too high for medication.

### Realistic researcher target

The **fetcher-only** scope is achievable: Stretch + pre-organized pill organizer + open-vocabulary fetch. This pulls the medication task into the existing RUM/OK-Robot capability envelope without taking on the high-stakes pill-manipulation step. It's a less ambitious contribution than full medication management, but it's deployable today.

---

## A pattern across all three

Each underserved domain has a similar structure:

1. **Generic-manipulation methods don't suffice.** Pick-and-place / open-vocabulary fetch are not the bottleneck — the bottleneck is task-specific (cloth, water, pill verification).
2. **Hardware constraints dominate the gap, not learning algorithms.** Compliant arms (dressing), water-tolerant hardware (bathing), sub-cm precision (medication) — none come from a smarter policy.
3. **The failure-cost asymmetry penalizes "good average performance."** All three involve sustained contact with a person who cannot recover from a robot error. 90% reliability is unhelpful when the 10% includes "skin laceration" or "wrong dose."
4. **Regulatory and population-access barriers compound the technical barriers.** This is true for all assistive robotics, but more acute for these three because they're so contact-intensive.
5. **CBPR / participatory design is more, not less, important.** [Nanavati 2024 Multiple Ways](../sources/nanavati2024-multiple-ways-par.md) and [Nanavati 2025 feeding out-of-lab](../sources/nanavati2025-feeding-out-of-lab.md) show that out-of-lab user partnership is what surfaces the failure modes mainstream research misses. Underserved domains need it most.

---

## What's actionable

### For the wiki

- **Ingest cloth-manipulation literature.** Diffusion-PbD for fabric, recent dressing-robot work from CMU (HERB) or Maya Cakmak's earlier dressing studies — none currently in the wiki.
- **Ingest soft-robotics dressing work** — Asbeck lab, Soft Robotics Inc., MIT CSAIL Daniela Rus group.
- **Add a "high-reliability verification" concept page.** mLLM-as-verifier is in RUM; the verification reliability question is broadly relevant beyond medication.

### For an independent researcher

The realistic targets, ranked by tractability:

1. **Medication-fetcher on Stretch.** Most tractable. Reuses RUM-class capability. Practical contribution (a sensorized pill-organizer fetcher) plus methodological contribution (failure-cost-aware design).
2. **Dressing demonstration dataset.** Medium tractability. Requires user partnership but uses existing Stretch hardware. Could become a published dataset that later cloth-manipulation methods evaluate against.
3. **Needs assessment for bathing.** Lowest hardware barrier; highest user-engagement barrier. Most likely contribution: a structured analysis of what current bathing-assistance products fail at, what care-facility staff identify as priorities, and what hardware classes might fit. Publishable as workshop/RA-L.
4. **Survey paper update.** [Nanavati 2024](../sources/nanavati2024-physically-assistive-robots-review.md) is the canonical PAR review; a focused follow-up surveying just dressing/bathing/medication PAR work since 2023 would be useful both as a literature service and as a way to surface what's published outside the systematic review's screening venues.

---

## Open questions

- **What happens at the intersection of underserved domains?** A user who needs dressing AND medication AND bathing assistance is the actual target user — but the literature treats each domain in isolation.
- **Is there a single unified hardware class?** Compliant + water-tolerant + sub-cm precise hardware probably exists in industrial / surgical / medical-device contexts but is not in the assistive-robotics wiki. Worth surveying.
- **What does Henry Evans's deployment record suggest?** The [HCR Lab summers](../sources/maya-cakmak-research.md) include face wiping, scratching, lotion, and operating medical devices — adjacent to grooming and medication, but not the canonical underserved tasks. The closest published precedent is "uses a printer," "operates a percussion vest." Personalized medical-device operation might be a tractable bridge between underserved-domain work and existing in-home deployment infrastructure.

---

## Sources used in this synthesis

- [Physically Assistive Robots — Systematic Review (Nanavati et al. 2024)](../sources/nanavati2024-physically-assistive-robots-review.md) — the gap-identification source.
- [Multiple Ways of Working with Users (Nanavati et al. 2024)](../sources/nanavati2024-multiple-ways-par.md) — methodology for inclusive design.
- [Feeding System Out-of-lab (Nanavati et al. 2025)](../sources/nanavati2025-feeding-out-of-lab.md) — out-of-lab deployment lessons.
- [Sense of Agency (Yang et al. 2025)](../sources/yang2025-sense-of-agency.md) — high-risk-task user-control preference.
- [RELab tenoexo](../sources/relab-ethz-tenoexo.md) — wearable hand orthosis adjacent to dressing/grooming.
- [Virginia Tech Assistive Robotics Lab](../sources/virginia-tech-assistive-robotics-lab.md) — soft robotics + exoskeletons.
- [Robot Utility Models Paper (Etukuru et al. 2024)](../sources/robot-utility-models-paper.md) — mLLM verification reliability data point.
- [Maya Cakmak Research](../sources/maya-cakmak-research.md) — adjacent in-home deployment precedents.

## Related

- [Assistive robotics — R&D landscape and JEPA applicability](assistive-robotics-research-landscape.md) — broader R&D context.
- [Levels of autonomy in assistive robotics](levels-of-autonomy-in-assistive-robotics.md) — how the variable-LoC design pattern applies to high-stakes tasks.
- [Long-term in-home robot deployments](long-term-in-home-robot-deployments.md) — what real-deployment data we have.
- [Stretch as the de-facto assistive-robotics platform](stretch-as-assistive-platform.md) — what Stretch can and can't do for these domains.
- [Assistive robotics](../concepts/assistive-robotics.md) — concept overview.
