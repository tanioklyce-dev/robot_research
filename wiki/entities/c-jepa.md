---
title: C-JEPA (Causal-JEPA)
type: entity
subtype: model
created: 2026-10-25
updated: 2026-10-25
sources: 2
tags: [c-jepa, causal-jepa, jepa, object-centric, slot-attention, world-model, masking, pusht, clevrer, brown, galilai, nyu, mila]
---

# C-JEPA (Causal-JEPA)

**C-JEPA** is an object-centric [JEPA](../concepts/world-models/jepa.md) world model from Nam, Le Lidec, [Maes](lucas-maes.md), [LeCun](yann-lecun.md) and [Balestriero](randall-balestriero.md) (Brown / GalilAI, NYU, Mila; ICML 2026; arXiv 2602.11389). A frozen slot encoder (VideoSAUR on DINOv2) gives one token per object. A bidirectional predictor is trained while **whole objects' histories are masked**, so it has to infer each hidden object from the others and from the actions ([paper](../sources/causal-jepa-paper.md)).

## Results ([paper](../sources/causal-jepa-paper.md))
- **[Push-T](pusht.md) MPC:** 88.67% with 6 tokens × 128 dims, against [DINO-WM](dino-wm.md)'s 91.33% with 196 × 384. That is 1.02% of the latent input and 8.6× faster CEM planning. The gap is about 4 of ~150 episodes and no spread is reported.
- **The ablation path on Push-T:** slots plus an autoregressive predictor reach 60.67%. A JEPA-style masked predictor reaches 76.00%. Object masking reaches 88.67%.
- **CLEVRER counterfactual QA:** +21.1 pp per question over the unmasked variant with VideoSAUR slots. With SAVi slots, heavy masking does worse than none.

## Caveats
- The slot encoder was trained on a randomised Push-T variant, and the DINO-WM baselines got 10 epochs to C-JEPA's 30.
- On CLEVRER, token and tube masking match object masking. The entity-level advantage shows up on Push-T, where tube masking collapses to 5%.
- "Causal" means time-directed predictive dependency. The authors disclaim causal identifiability.

## Why it matters here
It is the most compact world-model state in the wiki and a direct example of the token-count lever for edge MPC. It also gives a second answer to the slot-correspondence problem: an identity anchor plus Hungarian matching, where [WorldDP](worlddp.md) uses SAM2 masks. Built on [stable-worldmodel](stable-worldmodel.md), by the [LeWorldModel](leworldmodel.md) group.

## Related
- [WorldDP](worlddp.md): the other object-centric JEPA-style world model in the wiki.
- [DINO-WM](dino-wm.md): the patch-based baseline. [LeWorldModel](leworldmodel.md): same group, end-to-end encoder.

## Mentioned in
- [Causal-JEPA paper](../sources/causal-jepa-paper.md)
- [stable-worldmodel GitHub](../sources/stable-worldmodel-github.md): named as a downstream user.
