---
title: ACT++ (act-plus-plus)
type: entity
subtype: method
created: 2026-05-25
updated: 2026-05-25
sources: 2
tags: [act-plus-plus, act, mobile-aloha, imitation-learning, stanford, zipeng-fu]
---

**ACT++** — the ML codebase shipped with [Mobile ALOHA](aloha.md) ([Fu, Zhao, Finn — Stanford, 2024](../sources/mobile-aloha-paper.md)). Hosted at https://github.com/MarkFzp/act-plus-plus ("MarkFzp" = Zipeng Fu's GitHub handle). Named as an evolution of [ACT (Action Chunking Transformer)](act.md), bundling the mobile-specific extensions the Mobile ALOHA paper introduces.

## Approach (inferred from the Mobile ALOHA paper + repo naming)

ACT++ extends original [ACT](act.md) along the dimensions Mobile ALOHA needs:

- **16-dim action vector** — original ACT predicted 14-dim joint positions for the two ALOHA arms; ACT++ appends the 2-dim mobile base linear+angular velocity, yielding the 16-dim Mobile ALOHA action.
- **Co-training across heterogeneous datasets** — samples mini-batches from both the static-ALOHA dataset (`D_static`, 825 demos, base actions zero-padded) and the in-domain Mobile ALOHA dataset for each task. Equal-probability sampling default; batch size 16. **Method-agnostic gain**: avg +34% absolute, up to +90%.
- **Action-chunk delay-shift** — to compensate for the mobile base's velocity-control delay (>10 cm error on 1m-radius 180° turns), executes the **first k−d arm actions** and the **last k−d base actions** of an action chunk of length k. Position-controlled arms run at the start of the chunk; delayed base velocity commands run at the end.

## Why "++"

The Mobile ALOHA paper consistently cites the method as "ACT [104]" rather than "ACT++"; the "++" naming appears only on the GitHub repo, signaling that the code is the original ACT codebase with the mobile-specific bits added. Treat this entity as the **mobile-extended ACT codebase**, not a distinct algorithm.

## Related
- [ACT](act.md) — predecessor.
- [Mobile ALOHA](aloha.md) — the platform ACT++ ships with.
- [Tony Z. Zhao](tony-zhao.md) — ACT first author.
- [Zipeng Fu](zipeng-fu.md) — ACT++ repo owner (`MarkFzp`).
- [Imitation learning](../concepts/learning/imitation-learning.md) — broader concept.

## Code
- Repo: https://github.com/MarkFzp/act-plus-plus

## Mentioned in
- [Mobile ALOHA Paper](../sources/mobile-aloha-paper.md)
- [Mobile ALOHA project page](../sources/mobile-aloha-project-page.md)
