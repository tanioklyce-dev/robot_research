---
title: Fast-ball tracking for robots — what transfers from broadcast sports CV
type: synthesis
created: 2026-07-21
updated: 2026-07-23 (§9 — clutter-matched diversity: 3 machines, Pokémon 0.606)
tags: [object-tracking, heatmap, tracknet, motion-attention, pinball, table-tennis, latency, perception, reflex-control, project]
---

# Fast-ball tracking for robots — what transfers from broadcast sports CV

The [TrackNet](../../entities/tracknet.md) family solved a problem that looks identical to one the wiki's projects need: **find a small, fast, blurred, often-occluded ball in video**. Six years and four versions produced a mature answer for *broadcast sports analytics*. This page asks the harder question — **how much of it survives contact with a robot that has to act on the answer**, specifically the [pinball-playing robot](pinball-playing-robot.md) and any future table-tennis work descending from the [USC MARL project](../../sources/usc-table-tennis-marl.md).

Short version: **the perception core transfers well and beats the approach currently written into the pinball page. The trajectory-repair machinery does not transfer at all, for a reason the source papers never have to confront.**

> [!note] Status
> This is analysis, not a validated build. The sourced claims carry citations; the latency arithmetic and the causal/non-causal split are my own reasoning over those sources and are flagged where they occur.
>
> **[§8 Field evidence](#8-field-evidence-added-2026-07-21) (2026-07-21)** revisits every recommendation against a first-party implementation ([pinball_tracker](../../sources/pinball-tracker-repo.md)). Two were refuted. Read it before acting on §7.
>
> **[§9 Cross-machine transfer](#9-cross-machine-transfer-added-2026-07-22-substantially-corrected-same-day) (2026-07-22)** — a third machine was labeled and the same model scored **0.555 F1** on it. §9 was **substantially corrected the same day** — a 5-frame label-alignment bug had made this look like a collapse (0.232). It still partly **un-revises** §8's data-cost finding and re-ranks the levers in §7. Read §9 before §8's optimism.

## 1. What the literature actually establishes

Three findings from the cluster are solid and directly relevant:

- **Heatmaps beat bounding boxes at this object scale, by a lot.** YOLOv7 scores **68.0 F1** where TrackNetV3 scores **97.5** on the same shuttlecock task ([TrackNetV4, Table I](../../sources/tracknetv4-motion-attention-2024.md)). The cause is scale: a ball is **2–12 px across, mean ≈ 5** ([TrackNet V1 §V](../../sources/tracknet-huang-2019.md)), which starves box regression of signal while remaining perfectly expressible as a small Gaussian in a dense map. See [heatmap-based object localization](../../concepts/robotics/heatmap-object-localization.md).
- **Temporal context is worth more than architecture.** Going from one input frame to three lifts V1's F1 from **92.5 → 98.2**, mostly in recall, and lets the model **place a ball that is fully occluded in the current frame** by inference from its neighbours ([V1 §V](../../sources/tracknet-huang-2019.md)). No other single change in the family's history comes close to that.
- **Explicit motion adds a little more, nearly free.** [Motion attention](../../concepts/robotics/motion-attention.md) — absolute frame differencing through a learnable normalization, multiplied into the visual features — adds **+0.4–0.6 F1** on top of V2 and V3 at **~1% throughput cost**, buying recall and paying a little precision ([V4, Table I](../../sources/tracknetv4-motion-attention-2024.md)).

### This revises a decision already on the pinball page

[Pinball-playing robot](pinball-playing-robot.md) currently specifies: *"track by combining high-FPS frame-differencing + a YOLO-nano-class ball detector fine-tuned on own footage — never a single cue."*

The instinct — **fuse motion and appearance, don't trust one cue** — is exactly right, and is precisely what [motion attention](../../concepts/robotics/motion-attention.md) does. But the proposed *mechanism* is the weaker version of it in two ways:

1. **YOLO-nano is the wrong detector class for a 27 mm ball on a playfield**, by ~30 F1 on the closest published analogue. A TrackNetV2-class heatmap net is the better-evidenced choice.
2. **Hand-fusing two independent cues is what motion attention replaces.** V4's contribution is that the fusion is *learned* and *internal* — the network decides what magnitude of frame-difference counts as salient, rather than a hand-tuned threshold arbitrating between a differencer and a detector. The classical version of this is exactly what was brittle enough to motivate the learned one.

**Recommended revision: TrackNetV2 backbone + V4 motion-attention module, trained on own footage.** Not V3 — see §3.

## 2. The chrome-ball problem argues *for* this, strongly

The pinball page identifies the hardest perception obstacle: a **27 mm mirror ball behind glass**, reflecting the playfield's own flashing general illumination, so **colour and brightness are unstable frame to frame**.

That is close to a worst case for an appearance-only detector — the thing you are asking it to recognize has no stable appearance. It is a comparatively *good* case for motion-weighted heatmap tracking:

- The ball's **motion signature is stable even when its appearance is not**. Frame differencing keys on *change*, and a fast ball is the largest coherent change in the frame regardless of what colour it currently is.
- The heatmap formulation never needs a confident class decision — only a peak. Under unstable appearance, a soft dense map degrades more gracefully than a thresholded box detection that either fires or doesn't.
- V4's **absolute** differencing matters here specifically: a mirror ball crossing a bright GI flash produces both large positive *and* large negative intensity swings. Signed differencing would discard half of them, and V4 reports exactly that failure mode — **missed detections** ([V4 §II.B](../../sources/tracknetv4-motion-attention-2024.md)).

The polarizer + steep-angle + lens-hood mitigations on the pinball page remain necessary; they reduce the glare the tracker must survive. This just says the tracker choice should also be glare-tolerant.

## 3. What does not transfer — the causality wall

This is the finding that matters most, and it is invisible in the source papers because **sports analytics is an offline discipline**. A broadcast tracker may freely look at frame *t+30* to decide frame *t*. A robot that must flip in ~20 ms may not.

Sorting the family's modules by whether a real-time control loop can use them:

| Module | Version | Needs future frames? | Usable in a reflex loop? |
|---|---|---|---|
| Heatmap tracking head | V1–V4 | No | **Yes** |
| Multi-frame input stack | V1+ | No — trailing frames only | **Yes** |
| Motion attention | V4 | No — needs `t−1` | **Yes** |
| Background estimation | V3 | Not per-frame, but needs a **median over the rally/match** | Partly — precompute, see below |
| **InpaintNet trajectory rectification** | V3 | **Yes — it inpaints gaps from surrounding context** | **No** |

**InpaintNet is where V3's headline gain comes from** — recall 94.56 → 99.33 ([V3 repo](../../sources/tracknetv3-repo.md)) — and it is structurally non-causal. It detects holes in a trajectory and fills them from what came before *and after*. For match analytics that is free accuracy. For a robot deciding when to fire a solenoid, the frames that would fill the hole **have not happened yet**.

> [!warning] Don't buy TrackNetV3 for a real-time loop
> V3's advantage over V2 is concentrated in a module a reflex controller cannot run. Adopting V3 and then disabling InpaintNet leaves you with roughly V2-plus-background-estimation — while paying V3's throughput cost. **V2 + V4 motion attention is the better real-time configuration**, and it is exactly the pairing V4 benchmarks (shuttlecock F1 90.6 → 91.4 at ~161 fps).
>
> The gap InpaintNet would have filled must instead be covered by the **ballistic/Kalman predictor already specified on the pinball page** — which is the causal way to solve the same problem, and which the pinball design got right independently.

**Background estimation is a partial exception.** V3 estimates the background as a **median image** over a match or rally. A cabinet-clamped rig looking at a fixed playfield could compute that median **once during setup** and hold it — no future frames, no per-frame cost. That is a genuinely transferable trick for a static rig, decoupled from InpaintNet.

## 4. The static-camera assumption: a lucky break, and a warning

Every motion-derived component in this family assumes the **background is stationary between frames** — V3's background estimation and V4's frame differencing both break under ego-motion, and **no paper in the cluster evaluates a moving camera** ([motion attention](../../concepts/robotics/motion-attention.md)).

This splits the wiki's two candidate projects cleanly:

- **Pinball — assumption satisfied, by design.** The [cabinet-hugging rig fork](pinball-playing-robot.md) mounts the playfield camera on a rig clamped to the machine. The camera does not move relative to the playfield, and the playfield is **planar** — so a 2-D heatmap in image space *is* the answer, with a fixed homography to table coordinates. **This is close to an ideal deployment for TrackNet**, and it is an under-appreciated argument for the self-contained-rig fork over arms-as-pressers: the rig fork buys a static camera, and a static camera is what makes the best-evidenced tracker legal.
- **Table tennis — assumption violated twice.** A head-mounted or base-mounted camera on a moving robot makes global motion dominate the difference map. And table tennis is **not planar** — you need the ball's 3-D position and velocity, which a single monocular heatmap does not give you. Fixing the first needs ego-motion compensation (warp frame `t−1` into frame `t` by homography before differencing) — mechanically straightforward, entirely untested in this literature. Fixing the second needs stereo or a second view, i.e. running the tracker twice and triangulating.

**Verdict: TrackNet transfers to pinball nearly as-is, and to table tennis only after two unvalidated extensions.** If the goal is to get a fast-ball loop working at all, pinball is by far the cheaper first target — which is consistent with, and adds a perception argument to, the sequencing already on the pinball page.

## 5. Latency arithmetic

> [!warning] The published FPS numbers are not your FPS
> V4 reports ~**160 fps** for TrackNetV2 and the V3 repo reports **25 fps**, but neither states the GPU, and V4's footnote concedes its V3 figure times *the entire script* including data loading and file writing. These are almost certainly desktop-GPU numbers. Assume a substantial derate on Jetson-class hardware; **measure before designing around any of them.** The wiki has no TrackNet-on-Jetson benchmark, and I could not find one.

With that caveat, the shape of the budget from the pinball page: at **120 FPS (8.3 ms/frame)** a 3 m/s ball moves ~25 mm/frame, and the total pre-fire budget is ~**15–30 ms** for detector + decision + solenoid.

The load-bearing observation is that **a TrackNetV2-class net must run at or above camera framerate to be worth the camera**. A 120 FPS global-shutter sensor feeding a tracker that manages 40 FPS has bought nothing — you have a 25 ms perception tick inside a 15–30 ms budget, and the predictor is now extrapolating across three dropped frames. Two mitigations, both already implied by the pinball page's ROI-crop note:

- **Crop hard.** TrackNet's native `640×360` is already small; a lower-playfield ROI cuts it further. Inference cost falls roughly with pixel count.
- **Shrink the backbone.** V1's VGG-16 encoder is heavy and dated by the standards of edge CV. Nothing in the family's evidence says VGG-16 specifically is required — the load-bearing choices are *heatmap output* and *multi-frame input*, both backbone-agnostic. A distilled or narrower encoder is an obvious and untested optimization.

## 6. The data cost is the real gate

The cluster's most under-advertised finding: **cross-sport transfer fails outright.** Tennis-trained V1 applied zero-shot to badminton scores **35.2 F1** (recall 22.9%) ([V1 §V](../../sources/tracknet-huang-2019.md)). And even within one sport, V1's 10-fold cross-validation drops recall **97.3 → 75.7**, so generalization across *courts and lighting* is far weaker than the headline number suggests.

Pinball is further from tennis than badminton is. **Assume no pretrained weights help; assume you label your own data.** V1 used **20,844 frames** for tennis; the V3 shuttlecock set and V4's multi-ball set are comparable in scale.

> [!warning] Revised by field evidence — see [§8](#8-field-evidence-added-2026-07-21), then [§9](#9-cross-machine-transfer-added-2026-07-22-substantially-corrected-same-day)
> This section originally called 20k frames "the actual cost of entry." A
> first-party implementation reaches **0.878 F1 held-out on 600 training
> frames** — ~20× less. Weakly evidenced (see §8 for the caveats), but enough
> that "start at ~1k and measure" beats committing to a 10–20k campaign.
>
> **Partly un-revised 2026-07-22.** A *second* held-out machine drops the same
> model to **0.555 F1** ([§9](#9-cross-machine-transfer-added-2026-07-22-substantially-corrected-same-day)).
> 600 frames bought one lucky generalization hop, not a robust tracker — which
> is much closer to this section's original pessimism than §8's revision
> suggested. "Start at ~1k and measure" survives as *method*; the implied
> conclusion that ~1k is *sufficient* does not.

Two things make it much cheaper than it sounds, and they compound:

1. **The [Keras repo's labeling tool](../../sources/weekenddeeplearning-tracknet-repo.md)** exists precisely for this and emits the `Frame, Visibility, X, Y` CSV the whole family consumes. It is the single most valuable thing in that repo — note it is **GPL-3.0**, but a labeling tool used to *produce data* does not put its license on the resulting model.
2. **~~Bootstrap the labels, don't hand-draw them.~~** ⚠️ **Refuted — see [§8](#8-field-evidence-added-2026-07-21).** The reasoning was that on a fixed rig with a controlled background, classical frame-differencing plus a median-background subtract makes a poor real-time tracker but a decent *offline* auto-labeler. In practice it tracked **8% of frames** — a lit insert is a better blob than a mirror ball. Hand-label the seed set.

## 7. Recommendation

For the [pinball fast loop](pinball-playing-robot.md):

1. **Adopt a TrackNetV2-class heatmap backbone + V4 motion attention.** Replaces the currently-specified YOLO-nano + hand-fused frame-differencing with the better-evidenced version of the same idea.
2. **Skip InpaintNet / TrackNetV3.** Non-causal; its job belongs to the Kalman predictor already in the design.
3. **Precompute the background median once at setup** — V3's one transferable trick for a fixed rig.
4. **Weight the rig fork accordingly.** The self-contained cabinet rig buys a static camera, which is a precondition for most of the above working at all.
5. **Budget for a labeling campaign** — ⚠️ **revised, see [§8](#8-field-evidence-added-2026-07-21)**: hand-label a seed set of order **~1k frames and measure**, rather than the 10–20k auto-bootstrapped campaign originally recommended here. Classical-CV bootstrapping tracked 8% of frames on real footage and emits confident wrong labels.
6. **Benchmark on the actual target hardware before committing** — no TrackNet-on-Jetson number exists, and the whole design depends on the tracker keeping up with the camera.

Start from the **[MIT-licensed V3 repo](../../sources/tracknetv3-repo.md)** even though V3 itself is the wrong model — it is PyTorch, maintained, and its tracking module is trainable standalone with InpaintNet simply not invoked. That is a cleaner base than the GPL Keras repo, from which you want only the labeling tool.

## 8. Field evidence (added 2026-07-21)

This page was written against the literature. The
**[pinball_tracker](../../sources/pinball-tracker-repo.md)** repo — first-party,
built independently and a few days *before* the TrackNet ingest — is the first
source in the wiki that actually built one of these and measured it. It
**confirms the central architectural call and refutes two of the
recommendations above.**

### Confirmed

- **Heatmap over boxes, arrived at independently.** The project converged on
  heatmap regression + stacked frames for the same stated reason given in §1,
  without having read the TrackNet papers. Convergent design under the same
  constraints is decent evidence the constraint analysis is right.
- **Static camera / planar playfield is the right deployment.** Homography
  normalization to a canonical top-down warp works, and removes camera angle as
  a variable exactly as §4 predicted.
- **The causality discipline holds in practice.** An independent audit of the
  inference path found **no future-frame usage** — the trailing-window
  convention is identical in training and inference. §3's warning is
  implementable without contortion.

### Refuted — recommendation 5 was wrong

§6 and recommendation 5 advise: *"bootstrap the labels, don't hand-draw them —
classical CV as an offline auto-labeler, hand-fix the failures."* The reasoning
was that an offline labeler can be slow and use future frames, so it should be
easy.

**Tested and it fails.** The best bootstrap configuration tracked **24 of 300
frames (~8%)**, and the project's own guidance is now *"for lamp-heavy
competitive footage, skip bootstrap — hand-label."*

The flaw in my reasoning was assuming the ball is the most salient blob once you
have a fixed background. On a pinball playfield it is not: **a lit insert is
rounder, brighter and more stable than a motion-blurred mirror ball**, and a
classical tracker that locks onto a blinking insert satisfies a
constant-velocity physics gate indefinitely. Frame-differencing plus blob
detection has no way to prefer the ball. This is the same appearance-instability
argument §2 makes *for* motion-weighted heatmap tracking — I simply failed to
apply it to the labeler as well as to the model.

> [!warning] Revised recommendation
> **Hand-label the seed set.** Budget for it. A classical bootstrap may still be
> worth trying on a clean fixed rig with the GI off or dimmed, but it cannot be
> assumed to work on real gameplay footage, and it produces confident wrong
> labels rather than flagged low-confidence proposals — the worst failure mode
> for a labeling aid.

### Revised — the data cost is far lower than estimated

§6 asserts *"V1 used 20,844 frames for tennis... that is the actual cost of
entry,"* and recommendation 5 budgets **10–20k frames**.

The project reaches **F1 0.878 ± 0.020 on a held-out machine with 600 training
frames** — roughly 20× less than estimated.

> [!note] Weakly evidenced, and the direction of the error is unknown
> The val set is one 10-second ball flight, only 201 frames are human keyframes,
> and the same set both selects the checkpoint and reports the result; the test
> split is empty. Treat 600 frames as a **promising lower bound on a single
> easy-ish generalization step**, not as the cost of a robust tracker. The
> honest revision is "start at ~1k frames and measure, rather than committing to
> a 10–20k campaign up front" — a materially different plan from the original
> recommendation either way.

> [!warning] The hedge above was right — see [§9](#9-cross-machine-transfer-added-2026-07-22-substantially-corrected-same-day)
> "A promising lower bound on a single easy-ish generalization step" is exactly
> what it turned out to be. The third machine landed on 2026-07-22 and the same
> model scored **0.555 F1** on it. **Do not cite the 20×-cheaper finding without
> §9.** The defensible version is: 600 frames can clear *one* favourable
> machine-to-machine hop; they do not buy a tracker that survives an arbitrary
> new playfield.

Plausible reasons the estimate was too high: homography normalization removes a
large source of variance the tennis datasets had to learn through; a pinball
playfield is planar and bounded where a tennis court is not; and a 1.95M-param
model needs less data than a VGG-16-scale one.

### Partially answers a logged open question

*"Can the VGG-16 encoder be replaced with an edge-scale backbone without losing
tiny-object sensitivity?"* — **evidence says yes.** A **~1.95M-parameter U-Net**
(≈1/8th a VGG-16 TrackNet) achieves 0.878 F1 held-out and runs ~50 FPS at
`px_per_mm=0.5`. Not a controlled ablation — no VGG-16 baseline was trained on
the same data — so this is evidence, not proof. But it is more than the TrackNet
literature offers, which has never ablated the backbone at all.

### Corrects a factual claim

§5's latency arithmetic borrows *"a 3 m/s ball"* from the pinball page, and this
page's author separately asserted flipper shots run 5–8 m/s. **Measured over
2,400 labeled rows: peak 4.87 m/s**, median 6.8–8.7 mm/frame, max 162.5
mm/frame. The wiki now has real numbers; use those.

### Still untested

The one recommendation nothing has exercised: **motion attention**. The project
has no explicit motion signal — no frame differencing anywhere, motion is purely
implicit via frame stacking, matching TrackNet V1/V2. It remains the cheapest
available accuracy lever and is still unvalidated on pinball footage.

**As of 2026-07-22 it now has a concrete failure to aim at** — see
[§9](#9-cross-machine-transfer-added-2026-07-22-substantially-corrected-same-day), which argues V3-style
**background estimation** may be the better-targeted of the two untried levers
for this particular failure, because the distractors that break the model are
*stationary*.

## 9. Cross-machine transfer (added 2026-07-22, **substantially corrected same day**)

> [!warning] This section originally reported a transfer *collapse*. That was a data bug.
> The held-out clip's labels were **5 frames out of alignment** with the video —
> its task clip starts at source frame 32700, not the 32705 in its filename, and
> the import trusted the filename. Every figure in the first version of this
> section was computed against time-shifted ground truth.
>
> | | as first published | **corrected** |
> |---|---|---|
> | 1 training machine | 0.232 / 0.200 | **0.555** |
> | 2 training machines | 0.266 | **0.638** |
> | localization | ~17 px | **~8 px** |
>
> **The claim that this reproduced V1's tennis→badminton failure (35.2 F1) is
> withdrawn.** So is the supporting claim that the model "emits no heat at the
> ball locations" — recall was flat across decode thresholds because the
> comparison was against ground truth in the wrong place, not because the
> heatmap was empty. What survives is a real but *moderate* venue gap, and the
> diversity result below, which was measured on both label versions and holds
> either way.
>
> **Method note worth more than the result.** The bug was invisible to every
> aggregate metric and to a careful list of ruled-out causes (spatial offset,
> scale, decode threshold, per-object and per-segment recall). It was caught by a
> human watching an overlay video and noticing the labels *trailed the ball*.
> Checking a *spatial* offset was wrongly treated as ruling out import bugs in
> general; **temporal** alignment was never checked. Render the overlay and watch
> it whenever a source is labeled.

§8 was written when [pinball_tracker](../../sources/pinball-tracker-repo.md) had
one held-out machine. It now has two. The second is harder, but not catastrophic.

| source (split) | machine | P | R | F1 |
|---|---|---|---|---|
| `foofighters_deadflip` (val) | Foo Fighters Pro | 0.903 | 0.927 | **0.914** |
| `pokemon_cooltoy` (test) | Pokémon Premium | 0.572 | 0.540 | **0.555** |

Same checkpoint, same evaluation recipe, both machines unseen in training.

**A second venue costs roughly 0.32 F1** — a substantial, actionable degradation,
but the model is still tracking the ball most of the time (localization ~8 px,
well inside a ball radius). The residual failures concentrate where the playfield
is densest with **round, shiny, ball-like decorations** (a large Pokéball toy,
Pikachu figurines, glossy plastics) and in the pop-bumper scrum.

### How this relates to the literature's failure mode

The first version of this section claimed this reproduced V1's zero-shot
tennis→badminton result (**35.2 F1**, recall 22.9%). **With correct labels it
does not** — 0.555 is a different regime entirely, and the resemblance was an
artifact of the alignment bug.

The honest reading is milder and still useful: cross-*venue* transfer degrades
materially for this model family, consistent with V1's 10-fold cross-validation
dropping recall **97.3 → 75.7** across courts and lighting *within* one sport
([V1 §V](../../sources/tracknet-huang-2019.md)). A pinball machine is a venue
whose entire visual identity is bespoke art, so expect a per-venue penalty — but
expect it to look like V1's cross-court number, not its cross-*sport* number.

> [!note] A cautionary note on confirmation
> The withdrawn claim was attractive precisely because it matched a published
> result so neatly. A number that lands on top of the literature's is weak
> evidence of correctness and should raise, not lower, scrutiny of the
> measurement — the agreement here was coincidence produced by a bug.

### Consequence: augmentation is not the fix — predicted, then measured

The prediction filed here on 2026-07-22, before the run finished: *nothing in
this literature cluster shows augmentation closing a transfer gap of this
magnitude.* V3 uses mixup and still needs in-domain data; V1's answer to
badminton was to label badminton. Augmentation perturbs the pixels you have — it
does not synthesize a Pokéball toy into Godzilla's playfield, and the failure is
object-level, not lighting-level.

**Measured the same day, and the prediction held.** Same training recipe, only
the augmentation config changed (photometric jitter aimed *directionally* at the
brighter target palette rather than sprayed symmetrically):

| | Foo Fighters (val) | Pokémon (test) |
|---|---|---|
| baseline | 0.914 | **0.555** |
| directional augmentation | **0.928** | **0.566** |

Pokémon moved **+0.011** — small enough to be noise on a single run. (These are the corrected figures; measured against the misaligned labels the same comparison read 0.232 → 0.229, i.e. −0.003. Both versions agree it is close to flat, since a constant ground-truth shift affects both arms equally.) **Augmentation is
eliminated as a route past a venue gap of this size**, which is a stronger
statement than the literature offered — the papers never tried and failed, they
simply labeled the new domain.

> [!note] It is not worthless — it just solves a different problem
> Foo Fighters *improved* 0.914 → 0.928, entirely on precision (0.903 → 0.942,
> false positives 60 → 34). Augmentation bought in-distribution robustness on
> the machine that already worked, and nothing on the hard domain gap. That is a
> clean demonstration of the boundary: **augmentation hardens what the model has
> already learned to see; it cannot teach an object class the training set never
> contained.** Keep it on — just do not budget it against transfer.

One transferable method note: **symmetric jitter sprays away from a known
target.** Pokémon is brighter than Godzilla's dark booth, so symmetric
brightness spends half its draws moving the wrong way; the first config
brightened in only 56% of draws and some draws crushed the frame to black,
destroying signal. Aiming the range (98% brightening, bounded) is strictly
better when the direction of the domain shift is known. Inspect rendered
augmented samples before spending epochs — both that and a cutout setting that
fully erased the ball in ~30% of samples were caught by eye, not by loss curves.

### The better-targeted lever: background estimation, not motion attention

§8 lists motion attention as the cheapest untried lever, and it still is *in
general*. But for **this specific failure** I think [V3's background
estimation](../../sources/tracknetv3-repo.md) is the sharper tool, and the
reason is a property of the distractors:

**The objects that break the model do not move.** A Pokéball toy and a row of
figurines are geometrically static. A median background image over a rally —
which §3 already identifies as the one V3 trick that transfers to a fixed rig,
computable once at setup with no future frames and no per-frame cost — captures
them almost exactly. Fed as an auxiliary input, it lets the network learn to
discount whatever is *always there*. Balls move; toys don't. That is a direct
answer to the measured failure, where motion attention is an indirect one.

> [!warning] Motion attention has a pinball-specific risk the source papers don't face
> Frame differencing on a playfield is dominated by **insert and flasher
> flicker** — lamps changing intensity at fixed positions. This is exactly what
> sank classical bootstrap labeling at 8% of frames ([§8](#refuted--recommendation-5-was-wrong)).
> V4's module is structurally better than that baseline: the difference map is
> *multiplied into* appearance features late in the network (`A_t ⊚ V_t`) rather
> than deciding alone, so a blinking insert must also look like a ball to
> survive. But badminton has no analogue of a playfield full of animated lamps,
> so V4's reported +0.4–0.6 F1 should **not** be assumed to carry over. Measure
> it on pinball footage before believing it.

Both are cheap enough to test, and they are orthogonal — background estimation
suppresses *static* clutter, motion attention amplifies *moving* evidence. On a
static-camera rig there is no reason not to try both.

### Tested: a second training machine helps, and is expensive per point

The diversity hypothesis above was then measured rather than assumed. Training on
**two machines** (Godzilla + Foo Fighters) with Pokémon still held out, changing
nothing but the training data:

A **fixed-volume control** separates the two explanations — is it the second
machine, or simply more data? All three runs use identical config and `last.pt`,
scored on corrected labels:

| training data | samples | Pokémon (held out) |
|---|---|---|
| 1 machine | 600 | 0.555 |
| **2 machines, same volume** | 600 | **0.598** |
| **2 machines, full** | 1200 | **0.638** |

**Diversity is worth +0.043 at constant sample count; the extra volume adds a
further +0.040.** Both effects are real and roughly equal — the naive
two-machine gain was *not* just "more data," but it was half that. Localization
also improves (8.8 → 8.1 px).

This result held on both the misaligned and corrected labels, which is why it
survived the correction above when the headline transfer number did not: a
*relative* comparison between models scored the same way is robust to a constant
ground-truth shift, while any *absolute* claim about capability is not. Worth
remembering when triaging which conclusions a data bug destroys.

> [!warning] Two traps this run walked into
> - **The held-out figure for a machine that moved into training is
>   meaningless.** Foo Fighters scores 0.992 in the two-machine runs, but it is
>   training data there. Easy to misread as a spectacular result when a source
>   changes split.
> - **Checkpoint selection is not comparable across split changes.** The
>   two-machine runs have no val split, so their `best.pt` degenerates to
>   lowest-train-loss. Every row above uses the unselected `last.pt`; comparing an
>   unselected checkpoint against a val-selected one understates the gain by ~3
>   points.

**Interpretation.** Coverage is a genuine lever, and now a measured one — but the
exchange rate is modest: roughly +0.04 F1 per additional labeled cabinet, on this
sample of one. For a robot expected to face an arbitrary showroom machine, buying
transfer one cabinet at a time is a slow road, which keeps **background
estimation** (below) attractive as a complement, since its target — static
playfield decorations — is what the extra machine did least to address.

### Tested: clutter-matched diversity (added 2026-07-23)

The obvious follow-up: Foo Fighters is a second *machine*, but it is not a
*cluttered* one — it lacks the round shiny decorations that actually break the
model on Pokémon. So two machines were labeled specifically for that failure
mode — **Avengers: Infinity Quest** and **Elvira's House of Horrors**, both
dense with round inserts and toy sculptures, Elvira on a new camera rig — and
added to training (Godzilla + AIQ + Elvira; Foo Fighters kept as val, Pokémon
still the untouched test). These were **multiball** clips (2–6 balls), a harder
labeling job than the single-ball sources.

Because this run *has* a val split (Foo Fighters), its `best.pt` is a real
val-selected checkpoint — so the honest comparison is against another
val-selected `best.pt`, i.e. the one-machine baseline, **not** the `last.pt`
numbers above (which came from runs with no val split). Both checkpoint families,
Pokémon test, corrected labels:

| training | checkpoint | P | R | F1 | loc |
|---|---|---|---|---|---|
| Godzilla only | best.pt (val-sel) | 0.495 | 0.600 | 0.542 | 9.6 px |
| **Godzilla + AIQ + Elvira** | **best.pt (val-sel)** | 0.595 | 0.618 | **0.606** | **6.9 px** |
| Godzilla only | last.pt | 0.572 | 0.540 | 0.555 | 8.8 px |
| Godzilla + FF | last.pt | 0.671 | 0.608 | 0.638 | 8.1 px |
| **Godzilla + AIQ + Elvira** | **last.pt** | **0.735** | 0.565 | **0.639** | 7.1 px |

**A "yes, and" result — and the "and" is the interesting part.**

- **Diversity helps again.** Val-selected, adding the two cluttered machines
  lifts Pokémon **0.542 → 0.606** (+0.064). The val machine (Foo Fighters)
  improved too: best val F1 **0.920 → 0.963**.
- **But clutter-matching did *not* beat plain diversity on aggregate F1.** On the
  comparable `last.pt`, Godzilla+FF (0.638) and Godzilla+AIQ+Elvira (0.639) are a
  dead heat. The hypothesis was that machines *sharing the failure mode* would
  help more per cabinet. On F1 alone, they did not.
- **Where they did help is precisely the failure mode.** The cluttered-machine
  model reaches **precision 0.735** — the highest Pokémon precision recorded, and
  precision (firing on decorations) was *the* defect — plus the best localization
  yet (7.1 px, down from 8.1). It bought that precision with recall (0.608 →
  0.565): the model became more conservative, firing on fewer decorations but
  also missing more real balls. For a reflex controller that trades a gap against
  an outlier, that is arguably the *better* error profile even at equal F1, but
  it is not the free lunch "label the failure mode" implied.

> [!warning] What this comparison is not
> - **The training sets are not nested.** "2 machines" is Godzilla+FF; "3
>   machines" is Godzilla+AIQ+Elvira, with **no Foo Fighters**. So this is not
>   "2 → 3"; it is two different three-vs-two compositions. The clean isolation
>   (hold everything fixed, add one cluttered machine) was not run.
> - **Still one test machine.** Pokémon cannot distinguish "clutter-matching
>   plateaus" from "these two particular machines happened not to transfer
>   better." A second cluttered *test* machine is what would settle it.
> - **Pokémon has now been scored many times.** Every such score erodes it as
>   held-out evidence. Treat the precision gain as the durable finding and the
>   F1 as a soft point estimate.

**Reading.** Labeling for the failure mode did not raise the headline number
beyond what any second machine gave, but it moved the *error profile* toward the
defect it was aimed at — higher precision, tighter localization, fewer decoration
false positives. That is consistent with the failure being real and addressable,
and with **background estimation** (next) being the more direct tool for it,
since the residual precision loss is still about *static* clutter.

### Revised recommendation ordering for the pinball fast loop

Superseding §7's item 5 and re-ranking the accuracy levers:

1. **Training diversity is the blocking issue, not a polish item.** One train
   machine does not cover arbitrary playfield art. Label additional *train*
   machines — chosen for clutter, not convenience — before tuning anything else.
   **Now measured (2026-07-22):** a second machine lifts the held-out target
   0.555 → 0.638. Real, but ~+0.04 F1 per cabinet labeled, so treat
   it as necessary-not-sufficient and pair it with item 2.
2. **Background estimation** — best-matched to the measured failure, and free at
   inference on a fixed rig.
3. **Motion attention** — still the cheapest general lever; carries the
   lamp-flicker caveat above.
4. ~~**Augmentation** — worth a run, low prior.~~ **Run and eliminated
   (2026-07-22):** 0.555 → 0.566 on the target machine. Keep it on for the
   in-distribution precision it does buy (+0.014 on the machine that already
   worked), but it is not a transfer lever.
5. **Match `max-peaks` to the true ball count when evaluating.** The project
   found that a peak cap above the real object count manufactures false
   positives: its val clip scored 0.537 F1 (precision 0.376) at the default cap
   of 4 versus 0.914 at the correct cap of 1. This is the practical face of the
   open multi-ball formulation question below, and it silently corrupts any
   precision number in this family.

> [!note] What would change this conclusion
> A single additional cluttered *training* machine lifting Pokémon materially
> would confirm "diversity, not architecture." If it doesn't, the problem is
> architectural — the model is keying on appearance in a way that stacked frames
> alone don't fix — and background estimation / motion attention move from
> optional levers to required ones.

## Related

- [pinball_tracker (repo)](../../sources/pinball-tracker-repo.md) — the
  first-party implementation providing the field evidence in §8 and §9.
- [Pinball-playing robot — project scoping](pinball-playing-robot.md) — the project this revises; see its Vision + reflex budget section.
- [XLeRobot camera options (low light)](xlerobot-camera-options-low-light.md) — sensor-side sibling analysis.
- [TrackNet (model family)](../../entities/tracknet.md), [heatmap-based object localization](../../concepts/robotics/heatmap-object-localization.md), [motion attention](../../concepts/robotics/motion-attention.md).
- [Learning to play Table Tennis using MARL (USC)](../../sources/usc-table-tennis-marl.md) — the other fast-ball candidate; §4 explains why it is the harder perception target.
- [SAHI](../../concepts/robotics/sahi-slicing-inference.md) — the alternative small-object route, rejected here: it multiplies inference cost per frame, which is the one resource a reflex loop cannot spend.

## Open questions

- **No TrackNet-on-Jetson benchmark exists.** This is the single biggest unknown in the recommendation above and the first thing to measure.
- Does motion attention survive **ego-motion compensation** (homography-warp before differencing), or does warping residual break the learned normalization? Untested anywhere.
- ~~Can the VGG-16 encoder be replaced with an edge-scale backbone?~~ **Partially answered — see [§8](#8-field-evidence-added-2026-07-21)**: a ~1.95M-param U-Net reaches 0.878 F1 held-out. Still no controlled ablation; the TrackNet family has never ablated the backbone at all.
- For pinball specifically: **multi-ball modes**. V4's multi-ball dataset labels a "primary" ball, but pinball multiball has no primary — you may need all of them, which is a different output formulation (multiple peaks, no argmax). **Now has a concrete cost attached** ([§9](#9-cross-machine-transfer-added-2026-07-22-substantially-corrected-same-day)): with no argmax you must cap the peak count, and a cap above the true ball count manufactures false positives — 0.537 vs 0.914 F1 on the same clip. A per-frame ball-count estimate, rather than a fixed cap, is the unbuilt piece.
- **Does cross-machine transfer have a floor?** Two held-out machines gave 0.914 and 0.555 with no obvious a-priori way to tell which kind a new machine would be ([§9](#9-cross-machine-transfer-added-2026-07-22-substantially-corrected-same-day)). Predicting transfer difficulty from playfield properties (clutter density, count of spherical decorations, GI brightness) is unexplored and would be worth more than another point estimate.
