---
title: "Un nouveau robot domestique débarque : il est français et apprend vos corvées comme un chef (Clubic)"
type: source
url: https://www.clubic.com/actualite-631786-un-nouveau-robot-domestique-debarque-il-est-francais-et-apprend-vos-corvees-comme-un-chef.html
local_path: raw/2026-09-29-clubic-flourish-1.md
sha256: a76a8908fab27afc28cba6fc4efb27701e747688688dd7cc01e3c5c3dace2761
author: Alexandre Boero (Clubic)
published: 2026-09-29
ingested: 2026-10-07
venue: Clubic (French tech press)
format: "French-language launch article (~1,200 words) built on an interview with the founder; quotations below are translated"
tags: [flourish, flourish-1, home-robot, france, paris, success-rate, subscription, privacy, after-sales, founder-background, secondary]
---

# Un nouveau robot domestique débarque : il est français et apprend vos corvées

## Summary

The most skeptical and most detailed of the launch-day pieces. Clubic interviewed [the founder](../entities/flourish-robots.md) and reported what the English coverage skipped: the robot is **designed and assembled in a Paris workshop**, it is **slow** (*"putting the shoes away can take it 5 minutes"*), its **~80% success figure applies to simple tasks**, and nothing is known about harder ones. It also gives the founder's background and the **after-sales model**: modular parts, remote diagnosis, and the customer swaps the part. The article lists the open areas, *"optional subscription, imperfect success rate and unanswered questions"*, which makes it the best checklist of what the company had not said.

## Key claims (translated)
- **Made in Paris:** *"Flourish is designed and assembled in our workshop in Paris, with components coming mostly from Asia."* Same $3,555 price in France and the US (*"a tiny bit more than €3,000"*). The photos show **exposed cables**, which Clubic reads as *"a machine not so far from the prototype."*
- Body: about **1.09 m** and **~20 kg**, a wheeled base, **a conical hat**, two arms ending in grippers, each gripper topped by a small camera. **LiDAR** lets it adapt when furniture is moved.
- Cost logic: *"Almost all household tasks happen at floor or table height."* No legs, no five-fingered hands, no waterproof 10 kg arms. *"And we sell each robot at a margin."*
- **Speed:** *"It is still slow in this first version: putting the shoes away can take it 5 minutes."* Clutter: *"an apartment too cluttered for a robot vacuum will be too cluttered for it too."*
- **Success rate:** on simple tasks such as shoes or plants, about **80%**. *"One time in five, then, the sneakers stay in the hallway."* The 99% target has no deadline. *"Nothing says, for now, how the robot does on more delicate chores, such as loading the dishwasher."*
- **Compute:** *"The site states it runs locally"* (true of the [2026-10-02 edition](flourish-robots-website.md#edition-history), since withdrawn). The most advanced AI tasks need more compute than the robot carries: either an optional subscription, *"price not yet known,"* on Flourish servers *"in Europe or the United States depending on the customer's country,"* or the owner's own GPU computer. **Without a subscription the robot still moves, obeys voice, and replays the recorded gestures it was shown.**
- **Privacy:** nobody at Flourish pilots the robot remotely. Training videos are **deleted once used**, unless the customer agrees to their use for improving the company's models. What happens to everyday footage is unknown.
- **After-sales:** a modular robot. The Paris team diagnoses faults remotely and guides the customer to replace the part. *"The two-year legal guarantee applies."*
- **Founder:** École 42 alumnus (the school founded by Xavier Niel), seven years in AI and automation. He says he **sold Joyger** (logistics automation, welcome kits) and then founded **Latice.ai** (automated voice-AI fine-tuning), backed by **Kima Ventures** (Niel's fund) and The Quest. **Families Fund** led Flourish's pre-seed (amount undisclosed). Its founder, Kartik Sathappan, is quoted.

## Contradictions with other sources

> [!warning] Contradiction — where the servers are
> Clubic says Flourish servers are in **Europe or the US depending on the customer**. The [Privacy Policy](flourish-robots-website.md) says *"our infrastructure is located"* in the US and transfers EU data there under SCCs.

> [!warning] Contradiction — retention of teaching videos
> Clubic says training videos are deleted after use unless you opt in to sharing. Privacy §5 says approved recordings fine-tune your task **and** *"train and improve the models that run tasks on Flourish robots,"* with de-identification when used beyond your unit. Declining means you cannot teach.

> [!note] Warranty: consistent, but only for Europe
> The "two-year legal guarantee" is the EU statutory conformity guarantee, which Terms §12 preserves. US buyers get **no warranty** (Terms §6).

> [!note] Founder background is self-reported
> The Joyger exit, Latice.ai and the Kima backing come from this interview and from the founder-issued [press release](flourish-1-launch-press-release.md) (*"repeat founder with a prior exit… funding from a Xavier Niel-backed fund"*). A web search found no independent record. They are one origin, not two.

## Entities mentioned
- [Flourish Robots](../entities/flourish-robots.md) · [Flourish 1](../entities/flourish-1.md)

## Concepts touched
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): 80% on "simple tasks", with no N and no harder tasks reported.
- [Imitation learning](../concepts/learning/imitation-learning.md): per-customer adaptation from teaching videos.

## Open questions
- What is the replay fallback after the subscription lapses? Open-loop joint trajectories cannot handle a shoe in a new place. Is the fallback mode useful for any listed task?
