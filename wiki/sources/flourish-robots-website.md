---
title: "Flourish Robots — Flourish 1 product site, Terms of Sale, and Privacy Policy"
type: source
url: https://flourish-robots.com/
local_path: raw/2026-10-07-flourish-robots-website.md
sha256: a91b90a0a2525f8e00ed1f092a358b828717c02868996a2635682709dfad15f0
local_path_superseded: raw/2026-10-02-flourish-robots-homepage-wayback.md
sha256_superseded: 9c5f5f42f64cd239055d294e60c53e3e6a3fa14d9ae20d106d998e5fed5cca35
author: Flourish Robots Corporation
published: 2026-09-29
ingested: 2026-10-07
venue: company website (Framer)
format: "product landing page + Terms of Sale + Privacy Policy + contact page, captured 2026-10-07; Terms and Privacy both 'Last updated: September 8 2026'. Tab-panel text ('What could it do in your home?') recovered from the page's JS bundle because it is not in the server-rendered HTML."
tags: [flourish, flourish-1, home-robot, mobile-manipulator, consumer-robotics, pre-order, end-user-programming, phone-teleop, cloud-inference, subscription, privacy, terms-of-sale, vendor-source, primary]
---

# Flourish Robots — Flourish 1 product site, Terms of Sale, and Privacy Policy

> [!note] This is the primary
> Everything decision-grade about [Flourish 1](../entities/flourish-1.md) — price, deposit terms, limits, warranty, data handling — is on these four pages. The launch press ([Robot Report](therobotreport-flourish-one.md), [CNET](cnet-flourish-1.md), [Clubic](clubic-flourish-1.md), [press release](flourish-1-launch-press-release.md)) adds hardware and company detail the site does not carry, and gets several of the site's terms wrong. The **Terms of Sale and Privacy Policy say more about the product than the landing page does.**

## Summary

[Flourish Robots](../entities/flourish-robots.md) sells **Flourish 1**, a wheeled two-armed home robot, as a **limited run of 50 numbered units at $3,555**. You reserve one with a **$1,555 deposit**, refundable until it ships, and shipping is planned for **December 2026**. The landing page sells three verbs. **Teach it**: build a task from drag-and-drop steps in a phone app, then drive the robot through it from your phone for ~30 minutes, and the task is ready ~1 hour later. **Talk to it**: voice commands. **Forget it**: schedule the task. There is also a **developer SDK and a task store**. "Advanced AI features" come with **6 months of cloud compute, then $50/month (optional), or use your own GPU**. The legal pages change the picture. The **Terms of Sale** describe *"an experimental product… not a finished consumer appliance"* that *"will sometimes fail at tasks it performed correctly the day before"*, sold **as-is, with no warranty and no returns once delivered**. The **Privacy Policy** says that during live operation *"sensor and camera data is transmitted between the robot and our servers so the system can decide what to do next"*. So the robot's moment-to-moment decisions depend on the network.

## Key claims

**Product and price (landing page)**
- **$3,555; reserve for $1,555**, *"fully refundable until shipping."* **Only 50 units, numbered 01 to 50.** Ships **December 2026**. Includes a *"direct line to the founders."*
- Spec strip: **3'7" height · 44 lb weight · 3.3 lb payload · 12 h runtime · floor to 35" reach.** That is ≈109 cm, 20 kg, 1.5 kg and 89 cm. The payload is given as **one number with no per-arm qualifier**; see the contradiction below.
- Compute: *"Advanced AI features: 6 months of cloud compute included, then $50/month (optional), or use your own GPU."* **This line replaced *"Runs on-device. Advanced AI tasks need extra compute: your GPU or our plan (details soon)"* between 2026-10-02 and 2026-10-07.** See [Edition history](#edition-history). No SoC, sensor, DOF or arm specification appears anywhere on the site.
- Reliability, stated by the vendor with no protocol, N or task list: *"A year ago a taught task worked 60% of the time. Today it's 80%. Tomorrow we're going for 99."*
- Marketing register: *"Be an early adopter… You wouldn't be a customer. You'd be a pioneer."* *"Frontier tech. It gets better every month you own it."*

**Teaching workflow (landing page)**
1. *"Build the task. Lay out the steps in the app: go to the entrance, pick up a shoe, put it in the cabinet, come back. 5 minutes, drag and drop, no code."*
2. *"Show it how, for 30 minutes. Then drive it from your phone, a few times, from different spots in the room."*
3. *"1 hour later, it's yours… You get a notification when it's ready."*
- Or *"install one someone else taught, in 5 seconds."* Developers *"write your own nodes, ship your own apps"* and publish to a store.

**Advertised tasks and stated limits (tab panels, from the page bundle)**
- *Morning:* puts shoes away · scoops the litter box · refills the water bowl · weather and what to wear · wakes you up.
- *While you're out:* tidies · puts clothes back · dusts shelves · pet-hair remover on the couch · **loads the washing machine and starts it** · waters plants · *"keeps an eye on the place"* · plays with the cat.
- *Evening:* wipes table crumbs · cleans countertops · sweeps in front of the litter box · throws out food packaging.
- *On request:* brings you a beer · throws a toy for the dog · calendar and reminders.
- **"What it can't do": *"No water · Nothing over 1.5 kg · Nothing breakable · No stairs · Not perfect. It works around your kids. It doesn't look after them."***

**Terms of Sale (last updated 2026-09-08)**
- Opens with: *"Flourish 1 is an experimental product sold in a limited run of 50 units to early adopters. It is not a finished consumer appliance… it will sometimes fail at tasks it performed correctly the day before, and it is sold with no warranty and no returns once delivered. We are telling you this first because we would rather lose the sale than have you find out later."*
- §1: *"a mobile home robot with a manipulator arm"* (singular; the press and photos show two). It cannot operate around water, handle objects over 1.5 kg or **sharp objects**, or climb stairs. It is **not a childcare, eldercare, medical, or security device**. It requires Wi-Fi, a smartphone and mains power. *"Certain advanced functions require additional computing resources,"* supplied by your own hardware or by a paid plan.
- §2–3: *"Payment is taken in full at the time of order."* That conflicts with the landing page's $1,555 deposit; see below. December 2026 is *"a good-faith estimate… not a guaranteed date."* A delay notice follows the FTC Mail Order Rule (16 C.F.R. Part 435): silence counts as consent to the first delay, and a second delay triggers an automatic refund. You can cancel any time before shipment.
- §4: international buyers are the **importer of record**.
- §5: *"All sales are final… no trial period and no cooling-off period."*
- §6: **"AS IS" and "WITH ALL FAULTS"**, with all implied warranties disclaimed. Repairs and spares are at Flourish's *"sole discretion and without obligation."*
- §7: the software is licensed, not sold. Cloud services *"may be modified, priced, or discontinued"*. *"We will not deliberately reduce the core function of a unit you own."*
- §8: no commercial, medical or care use. Supervise the robot near children, animals and vulnerable adults. Tell household members and visitors that the robot carries a camera.
- §9: SDK workflows from other owners are **not reviewed** by Flourish. You may not build anything that disables safety limits or exceeds the payload.
- §10: liability is capped at the price paid. §11: Delaware law. **§12: for EU/UK consumers, the statutory right of withdrawal and the conformity guarantee survive.** Jurisdictions requiring certification or a local representative may have their orders cancelled.

**Privacy Policy (last updated 2026-09-08)**
- Four headline promises: no recording without a yes, every session asks first; approved recordings go to Flourish; *"Live operation is not stored. When the robot is working, video passes between the robot and our servers to make decisions and is discarded."*; data is not sold.
- §2: approved recordings include **camera footage, depth and sensor data, robot movement data** and the workflow steps. "Depth" is the only sensor hint on the site. Telemetry includes *"task success and failure records."*
- §5: recordings fine-tune the task they belong to, and *"train and improve the models that run tasks on Flourish robots"*. When a recording is used beyond your own unit, identifying material is removed first. **Declining to record means the task cannot be taught**, because *"teaching a task requires a recording session."*
- §7: *"We are based in the United States and our infrastructure is located there."* EU/UK/Swiss data goes to the US under Standard Contractual Clauses.
- §8: data already in a trained model *"cannot be individually extracted; deletion stops any further use."*
- §10 tells readers to *"write to **[PRIVACY EMAIL]**"*. **The placeholder was never filled in.**
- §11: footage containing children is treated as sensitive. §12: automated decisions *"concern movement and object handling."*

## Contradictions and tensions

> [!warning] Contradiction — deposit vs. "payment taken in full"
> The landing page sells a **$1,555 reservation**. Terms §2 says *"Payment is taken in full at the time of order."* Both pages are live on the same date. Either the Terms predate the deposit model (they are dated 2026-09-08, three weeks before launch) or the deposit is not an "order" under the Terms. A buyer cannot tell which from the documents.

> [!warning] Contradiction — payload: total or per arm?
> The site says **3.3 lb** and *"nothing over 1.5 kg"*, with no per-arm qualifier. [The Robot Report](therobotreport-flourish-one.md) says **each** arm carries 1.5 kg and mis-converts that to "4 lb". *Interesting Engineering* says a **total** of 3.3 lb. The primary supports only "objects up to 1.5 kg"; it never says whether two arms can share a heavier load.

> [!warning] Contradiction — data location and retention
> The Privacy Policy puts all infrastructure **in the US** and keeps approved recordings for model training beyond your unit. [Clubic](clubic-flourish-1.md), interviewing the founder, says compute is hosted **in Europe or the US depending on the customer's country**, and that training videos are **deleted once used** unless the customer agrees to share them. [CNET](cnet-flourish-1.md) says you can opt out of training-data sharing in the app. The policy says opting out of recording means you cannot teach. The legal text is the binding one.

> [!note] "Not a paid beta" vs. the Terms
> The CEO told [CNET](cnet-flourish-1.md): *"It's a product launch, not a paid beta."* His own Terms call it *"an experimental product… not a finished consumer appliance"* with no warranty and no returns. The Terms are the more honest document and the more useful one.

> [!note] Warranty depends on where you live
> For US buyers there is **no warranty**. [Clubic](clubic-flourish-1.md) tells French readers that *"the two-year legal guarantee applies"*. That is consistent with Terms §12, which preserves EU statutory conformity rights, but it is not something the US buyer gets.

## What the network dependence means

Three statements, read together, fix the architecture more precisely than any press piece does:

1. Live sensor and camera data goes **to Flourish's servers "so the system can decide what to do next"** (Privacy §2).
2. The cloud plan is "optional" after 6 months, with your own GPU as the alternative (landing page).
3. Without a subscription the robot *"still moves, obeys voice and replays the recorded gestures it was shown"* (founder, via [Clubic](clubic-flourish-1.md)).

So the **learned, generalizing behaviour runs off-robot**. That is the part the CEO describes to CNET as *"you're teaching it the task, not a fixed sequence of coordinates"*. What survives without it is **trajectory replay**, which is exactly the fixed-coordinates behaviour he says the product is not. The onboard computer, a [Raspberry Pi](../entities/raspberry-pi-5.md) per [The Robot Report](therobotreport-flourish-one.md) (model unstated), is a body controller and sensor relay. That fits the other sub-$5k home robots in this wiki ([NORI A3](../entities/nori-a3.md), [Sourccey](../entities/sourccey.md)). It is the clearest case yet for the [value-chain page](../syntheses/society/consumer-robotics-value-chain.md)'s Tier 2 thesis, because **Flourish prices the model-serving layer explicitly: $50/month.**

## Entities mentioned
- [Flourish Robots](../entities/flourish-robots.md) · [Flourish 1](../entities/flourish-1.md)
- Comparators named in the press, not on the site: [1X NEO](../entities/1x-neo.md); Weave Isaac 1 (no entity page)

## Concepts touched
- [End-user robot programming](../concepts/robotics/end-user-robot-programming.md): drag-and-drop task graph plus demonstration, with no code.
- [Imitation learning](../concepts/learning/imitation-learning.md): per-home, per-task fine-tuning from ~30 minutes of phone teleop.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md): owner-consented, per-session recording that feeds fleet models.
- [Robot security](../concepts/robotics/robot-security.md): a camera robot whose live decisions round-trip to a vendor server.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): "60% → 80%", with no protocol.

## Open questions
- What is the 60% / 80% figure measured over? Which tasks, how many trials, in whose home? The "year ago" baseline predates the company's January 2026 founding ([Robot Report](therobotreport-flourish-one.md)), so it presumably comes from the founder's pre-company prototype.
- What exactly runs on the robot? Navigation and obstacle stop must, since the safety claim is that the robot halts when a person or animal enters its workspace. Does that stop work with the network down?
- What does a store "task" contain: a workflow graph, a fine-tuned checkpoint, or both? A checkpoint fine-tuned on one home would not transfer, which bears on the *"install one someone else taught, in 5 seconds"* claim.
- What does the "own GPU" path require (VRAM, OS, model format)? Undocumented.
- Will the deposit-vs-full-payment conflict in the Terms be fixed before December?

## Edition history

Captured twice: the **2026-10-02 Wayback Machine capture** (`local_path_superseded`, homepage only) and this ingest's **2026-10-07 capture** (`local_path`, homepage plus legal pages). A line-level diff of the two homepages shows three changes in five days:

| 2026-10-02 | 2026-10-07 |
|---|---|
| *"**Runs on-device.** Advanced AI tasks need extra compute: your GPU or our plan **(details soon)**"* | *"Advanced AI features: **6 months of cloud compute included, then $50/month (optional)**, or use your own GPU."* |
| *"Preferred by top industry professionals"* (above the press logos) | *"As featured in"* |
| — | a *"Talk with founders"* button beside every reserve button, linking to a new contact page |

> [!warning] The "runs on-device" claim was withdrawn, not just reworded
> The 10-02 site said the robot **runs on-device**. Secondary coverage quotes it (*Humanoids Daily*: "Runs on-device, but advanced AI tasks require extra compute"), and so does [Clubic](clubic-flourish-1.md) (*"Le site assure qu'il fonctionne en local"*). The Privacy Policy, dated three weeks **before** that capture, already said live camera data goes to Flourish's servers *"so the system can decide what to do next"*. The current site drops "on-device" and prices the cloud plan. **The revision brings the landing page into line with the Privacy Policy.** Treat any secondary source that says Flourish 1 "runs on-device" as quoting the superseded edition.

The press-logo change also reads as a correction: the logos are the outlets that covered the launch (Robot Report, CNET, Forbes, Clubic, BFM TV), not endorsements.

The Terms of Sale and Privacy Policy were not in the Wayback capture, so no earlier edition of them was compared. Both say "Last updated: September 8 2026."

> [!note] Why no `fetch_url`
> The `sha256` fields seal the **extracted-text captures**, not the live HTML. A re-fetched Framer page would never hash-match a text capture, so the drift script cannot sweep this source. To re-check, re-extract the text and diff it, as done above.
