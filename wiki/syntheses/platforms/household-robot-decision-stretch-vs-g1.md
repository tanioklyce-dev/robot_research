---
title: Household robot decision — Stretch 4 and the 2026 field
type: synthesis
created: 2026-05-08
updated: 2026-11-08
tags: [stretch, unitree-g1, decision, household-robot, comparison, hello-robot, recommendation, 1x-neo, nori-a3, weave-robotics, sunday-robotics]
---

# Household robot decision — Stretch 4 and the 2026 field

A buying decision for one use case: **a research-grade robot to navigate a home, pick things off the floor, put away dishes, and open cans.** Originally a two-way comparison of Stretch 3 and the Unitree G1, this page now covers every home-capable robot on sale or announced as of **2026-11-08**.

> [!note] Bottom line (2026-11-08)
> **Buy a [Stretch 4](../../entities/stretch.md) if you need a research platform you can receive now.** It is the only shipping robot here that combines documented developer access, onboard depth sensing, and a long-lift, payload-rated arm. **Budget for porting, not for a working household stack.** The published household evidence is from Stretch 2/3, and `stretch_ai` still documents only Stretch 3.
>
> **Under $5k, a [NORI A3](../../entities/nori-a3.md) ($1,688) is the cheap bimanual experiment**, but it has no depth sensor and no published results. **Nothing on sale today does dishes and cans reliably.** [Sunday Memo](../../entities/sunday-robotics.md) has the best dishes demonstration and can't be bought yet.

## What changed since May

- **Stretch 3 is sold out** ([purchase page](https://hello-stretch3.com/purchase)), so the old recommendation can no longer be followed for a new robot.
- **The software argument weakened.** The [`stretch_ai` README](../../sources/stretch-ai-github-readme.md) names only Stretch 3. Stretch 4 has a new control stack on ROS 2 Jazzy ([launch](../../sources/hello-robot-stretch-4-launch.md)).
- **Stretch 4's payload removes an old objection.** It carries 2.5 kg extended and 4 kg retracted ([entity](../../entities/stretch.md)), against the roughly 1.5 kg this page used for Stretch 3.
- **The G1 now has a home dataset.** [HIW-500](../../entities/hiw-500.md) records 500+ hours of teleoperated household work in 12 real homes. It is data, not a measured policy result.
- **A consumer tier appeared**, listed below. Most of it is pre-order, and its claims are the vendors' own.

**Corrections to the May version.** It said [Robot Utility Models](../../sources/robot-utility-models-paper.md) covered about three of the four task categories. It covers only part of one: its tissue and paper-bag pickups relate to floor pickup, and its other tasks are door opening, drawer opening and object reorientation. The May figure of 50–70% success on dishes had no source and is removed. The ~$16k G1 "EDU base" price was uncited and did not match Unitree's own listing.

## The field

Prices are vendor-listed on 2026-11-08 unless marked. "Evidence" means a published result with stated trials, not a video.

| Robot | Form | Price | Status | Developer access | Evidence in homes |
|---|---|---|---|---|---|
| **[Stretch 4](../../entities/stretch.md)** | Wheeled, one telescoping arm, lift | **$29,950** | **Shipping**, typically 2–4 weeks ([launch](../../sources/hello-robot-stretch-4-launch.md)) | ROS 2 + Python SDK, open source | **Previous generations only** (see below) |
| **[NORI A3](../../entities/nori-a3.md)** | Wheeled, two 7+1-DOF arms, lift | **$1,688** | **Shipping in batches**, by press reports; site says Fall 2026 ([site](../../sources/nori-robotics-site.md)) | Laptop training app | None |
| **[XLeRobot](../../entities/xlerobot.md)** | Wheeled, two 5-DOF arms, fixed torso | **~$660** parts | Build it yourself | Open hardware, [LeRobot](../../entities/lerobot.md) | Community demos only |
| **[Unitree G1](../../entities/unitree-g1.md)** | Biped | **$13,500** without SDK; **EDU by quote** ([Unitree](../../sources/unitree-g1-product-page.md)) | In stock | EDU only | [HIW-500](../../entities/hiw-500.md) teleoperation data; no policy results |
| **[Unitree G1-D](../../sources/unitree-g1-product-page.md)** | Wheeled, two 7-DOF arms, column | By quote | Listed | Data and training tooling | None found |
| **[UniX AI Panther](../../entities/unix-ai-panther.md)** | Wheeled, two 8-DoF arms, 80 cm lift | Not published | Vendor says delivering ([launch](../../sources/unix-ai-panther-launch.md)) | None stated | One vendor video |
| **[Weave Isaac 1](../../entities/weave-robotics.md)** | Wheeled, two 6-DOF arms | **$7,999** or $449/mo | Pre-order, fall 2026, California first ([Weave](../../sources/weave-isaac-1-product-page.md)) | None stated | None; teleop-assisted |
| **[1X NEO](../../entities/1x-neo.md)** | Biped | **$20,000** or $499/mo | Pre-order; no confirmed delivery as of mid-October ([order page](../../sources/1x-neo-order-page.md)) | None stated | None; scheduled remote operator |
| **[Flourish 1](../../entities/flourish-1.md)** | Wheeled, two arms, lift | **$3,555** + $50/mo after 6 months | Pre-order, 50 units, December 2026 ([site](../../sources/flourish-robots-website.md)) | SDK | Vendor's "80%," no protocol |
| **[Sourccey](../../entities/sourccey.md)** | Wheeled, two 5-DOF arms, lift | Not published | Roadmap now launch Nov 2026, ship Dec 2026 ([site](../../sources/vulcan-robotics-sourccey-site.md)) | Open source, LeRobot | None |
| **[Sunday Memo](../../entities/sunday-robotics.md)** | Wheeled, two 7-DOF arms | Not set | Beta "late 2026," not for sale ([site](../../sources/sunday-memo-site.md)) | None stated | Vendor videos |
| **[Figure 03](../../entities/figure-03.md)** | Biped | Not for sale | No home deployment announced | None | None |
| **[LG CLOiD](../../entities/lg-cloid.md)** | Wheeled, two 7-DOF arms | Not announced | CES demonstration ([LG](../../sources/lg-cloid-ces-2026.md)) | None stated | None |

## Capability against the task list

Only robots a buyer could plausibly get in the next few months are rated. ✅ is published evidence or a designed capability, ⚠️ is plausible but unproven, and ❌ is not supported.

| Task | Stretch 4 | NORI A3 | G1 EDU | Isaac 1 | NEO |
|---|---|---|---|---|---|
| **Navigate a house** | ✅ Holonomic base, 3D LiDAR, Nav2 | ⚠️ 2D LiDAR; base type unpublished | ⚠️ Falls remain the risk in clutter | ⚠️ Vendor claim | ⚠️ Vendor claim |
| **Floor pickup** | ⚠️ Earlier Stretch evidence; floor reach unstated, needs re-validation | ⚠️ Lift column; floor reach unpublished | ❌ Requires whole-body balance; no measured result | ⚠️ Vendor claim for clothes and toys | ⚠️ Vendor claim |
| **Put away dishes** | ⚠️ Payload now adequate; one arm; no published result | ⚠️ 1.5 kg per arm; no depth; breakage risk | ❌ 5-DOF arms, ~3 kg | ❌ Not a listed feature | ⚠️ Advertised; delivered autonomy "basic" |
| **Open cans** | ❌ One arm cannot hold and open | ❌ No demonstration | ❌ No demonstration | ❌ Not offered | ❌ Not offered |

**Dishes and cans remain unsolved on anything you can buy.** Memo's site shows dishwasher loading, labelled autonomous, without success rates or trial counts ([site](../../sources/sunday-memo-site.md)). No source reviewed here shows any robot opening a can.

## Published evidence

- **Stretch 2/3.** [RUM](../../sources/robot-utility-models-paper.md) reached **90% average success** across five tasks in real homes (74.4% raw plus 15.6% after retries). [OK-Robot](../../sources/ok-robot-project-page.md) reached 58.5% on open-vocabulary pick-and-drop in 10 homes, and 82% in uncluttered ones. Long-term use is documented in the [in-home deployments synthesis](../assistive/long-term-in-home-robot-deployments.md).
- **Stretch 4.** None yet in this wiki. Its base, wrist, sensors and software all changed, so **those results are grounds for optimism, not a specification**.
- **G1.** [HIW-500](../../entities/hiw-500.md) and Unitree's [UnifoLM-WLA-1.0](../../sources/unifolm-wla-1-project-page.md) give a real starting point, with open data and weights. WLA reports video carousels and no numbers.
- **Consumer tier.** Flourish's unqualified 80% is the only figure anyone offers. By the [success-rate audit](vla-success-rate-audit.md)'s standard, it is an unknown-N claim.

## Recommendation

**For this research use case: Stretch 4**, with a corrected rationale.

1. **It can be bought and received now.** Every stronger-sounding alternative is pre-order, beta or quote-only.
2. **It has the right body.** It is a passively stable wheeled base, with a telescoping arm on a 120 cm lift, 2.5–4 kg payload, 3D LiDAR and wrist depth. No biped here avoids the falling problem. Earlier Stretches picked objects off the floor, but the [Stretch 4 datasheet](../../sources/hello-robot-stretch-4-datasheet.md) as captured here does not state the lowest gripper height, so confirm that with Hello Robot before buying.
3. **It is open enough to do research.** The open ROS 2 and Python stack comes with new [Stretch 4 documentation](https://docs.hello-robot.com/), including puppet-teleop data collection and VLM grasping. Hello Robot says more is still being developed.
4. **Its lineage has the only rigorous in-home data**, even though that data needs re-validation on the new hardware.

**Budget.** $29,950 + $1,495 docking station = **$31,445**. Adding the Jetson Orin NX at its current **$2,995** brings it to **$34,440** ([purchase page](https://hello-robot.com/purchase/)). The site says Stretch 4 is "currently only certified for laboratory and research use," so it is not a consumer appliance.

**First experiment.** Before relying on the Stretch lineage, port one RUM policy and rerun its tissue and bag pickups at the published 10 trials per environment. Those results will show how much of the old evidence transfers.

### By situation

| If you want… | Choose | Why |
|---|---|---|
| A research platform now | **Stretch 4** | As above |
| Bimanual experiments under $5k | **NORI A3** | Two redundant arms at the lowest price, with depth and robustness unknown. Add a depth camera if the design allows it. |
| A fully open build | **[XLeRobot](../../entities/xlerobot.md)** | Inspectable and cheap, with low payload and 5-DOF arms |
| Humanoid or whole-body research | **G1 EDU**, or G1-D for manipulation data | Avoid the $13,500 model: Unitree's table shows no secondary development |
| Laundry and tidying done for you, in California | **Wait for Isaac 1 reports** | The closest match, but teleop-assisted and unproven |
| Dishes specifically | **Watch Memo's beta** | The strongest demonstration, with no availability |

## When this answer should change

- **Publication:** a measured Stretch 4 household result, or an official `stretch_ai` port.
- **Delivery:** independent owner reports on Isaac 1, NEO or NORI A3 that include intervention rates.
- **Memo** goes on sale with a published dishwasher success rate.
- **G1:** a policy result with trial counts in real homes built on HIW-500 or WLA.

> [!note] Prices drift
> Between May and November, Stretch's Jetson add-on rose from $2,495 to $2,995 and Flourish's deposit fell from $1,555 to $200. Re-check vendor pages before purchase.

## Sources used in this synthesis

- [Stretch 4 launch](../../sources/hello-robot-stretch-4-launch.md), [datasheet](../../sources/hello-robot-stretch-4-datasheet.md), [stretch_ai README](../../sources/stretch-ai-github-readme.md)
- [RUM paper](../../sources/robot-utility-models-paper.md), [OK-Robot](../../sources/ok-robot-project-page.md)
- [Unitree G1 pages](../../sources/unitree-g1-product-page.md), [HIW-500 dataset](../../sources/bitrobot-hiw-500-dataset-page.md), [UnifoLM-WLA-1.0](../../sources/unifolm-wla-1-project-page.md)
- [NORI A3 site](../../sources/nori-robotics-site.md), [Flourish site](../../sources/flourish-robots-website.md), [Sourccey site](../../sources/vulcan-robotics-sourccey-site.md)
- [1X order page](../../sources/1x-neo-order-page.md), [Weave Isaac 1](../../sources/weave-isaac-1-product-page.md), [Sunday Memo](../../sources/sunday-memo-site.md), [UniX Panther](../../sources/unix-ai-panther-launch.md), [LG CLOiD](../../sources/lg-cloid-ces-2026.md)

## Related

- [Humanoid platforms survey](humanoid-platforms-survey.md) · [Robot platforms comparison](robot-platforms-comparison.md) · [Sourccey vs XLeRobot](sourccey-vs-xlerobot.md)
- [Consumer robotics value chain](../society/consumer-robotics-value-chain.md)
- [Long-term in-home deployments](../assistive/long-term-in-home-robot-deployments.md)
- [LeWM on ROSOrin Pro — feasibility analysis](../projects/lewm-on-rosorin-pro-feasibility.md)
