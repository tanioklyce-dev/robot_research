# Runway — Praxis-1 Is Now Available (2026-11-11)
Source: https://runway.com/news/company-news/praxis-1-is-now-available — text extracted from <main>, fetched 2026-11-12

News/Company NewsPraxis-1 Is Now Available
November 11, 2026 · by Runway
State-of-the-Art Performance
Adapt It to Your Hardware
Why Open Weight
Try it Today
Contents
State-of-the-Art Performance
Adapt It to Your Hardware
Why Open Weight
Try it Today
Praxis-1, our state-of-the-art world action model, is now available to everyone with open weights under the Apache 2.0 license. We introduced Praxis-1 in September as our first world action model, built on the same large-scale video pretraining behind our general world models. Our launch partners including Noble Machines, Standard Bots and Ultra have been running it on their own hardware: a legged humanoid, a six-axis industrial arm and a dual-arm warehouse robot. Today, the same model is open to every robotics developer and researcher.
All videos at 1x speed.
State-of-the-Art Performance
Praxis-1 is a 27B-parameter mixture-of-experts diffusion transformer that predicts video and actions together. It is the top-performing world action model on NVIDIA’s RoboLab-120 leaderboard, and it outperforms every open-weight VLA. On RoboLab-120, Praxis-1 reaches 46.2% success across 1,200 episodes, compared with 42.9% for FLUX 3 Action, 36.8% for Cosmos3 Nano and 28.0% for π0.5.
RoboLab-120 LeaderboardModel | RoboLab-120 Success | 
Praxis-1 | 46.2% | 
FLUX 3 Action | 42.9% | 
Cosmos3 Nano | 36.8% | 
π0.5 | 28.0% | 
Data as of November 2026; Success rate across 1,200 episodes
Praxis-1 is available today on GitHub, on Hugging Face with native LeRobot support, and in vLLM-Omni, with hosted inference on Reactor. Everything you need to run and adapt it on your own hardware is released under Apache 2.0, including for commercial use. That covers the weights and the inference and fine-tuning code, with support for both full fine-tuning and LoRA. Praxis-1 runs out of the box across NVIDIA hardware, from data center GPUs like H100 and B200, to workstation GPUs like RTX 5090 and RTX PRO 6000, to Jetson Thor on the robot itself.
"Pick up the purple comb on the right then put the purple comb into the bag""Place the white mug upside down on the yellow tray""Pick up the red pepper and place it in the mug""Pick up the cutting board and place it in the yellow tray""Pick the teddy bear and place it on the towel"All videos at 1x speed.
Adapt It to Your Hardware
Praxis-1 learns how objects behave and how tasks unfold from large-scale video, which gives it a head start on a new embodiment before fine-tuning on any hardware or domain-specific data. Our research has shown that web video matches teleoperated robot video as pretraining data for policy performance, which shifts the bottleneck on a capable policy to how much general video a model can learn from.
With our partners, a single Praxis-1 checkpoint has adapted to a variety of embodiments with light fine-tuning, and with LoRA you can adapt it to your own embodiment, cameras and tasks without retraining the full model. Fine-tuned on Google’s RT-1 robot, which never appeared in its training data, Praxis-1 reaches 80.0% success on SimplerEnv, well above the original RT-1 policy at 52.4%.
Why Open Weight
When we announced Praxis-1, we committed to shipping it as an open model. U.S. leadership in physical AI will depend on investment in both hardware and software, and on a level of interoperability and openness from American models that physical use cases don't have yet. Open weights give hardware developers the flexibility to run, inspect and adapt a world action model on their own terms. Praxis-1 builds on Runway’s work as a founding member of the Cosmos Coalition, advancing open world models for physical AI. Together, Runway and NVIDIA are opening frontier technology stacks giving developers shared foundations to build on and solve physical AI challenges.
Try it Today
Download Praxis-1 on Hugging Face and view the code on GitHub, or try it on Runway Dev. Developers can post train Praxis-1 for their domain specific use cases with NeMo Automodel hands-on tutorials. If you're planning a deployment, contact our robotics team.
Discover more
ResearchIntroducing Praxis-1ResearchAccelerating Robot Policy Evaluation with General World ModelsResearchReal-Time Video at Batch Size One

---
# Companion: Introducing Praxis-1 (Runway Research, September 2026)
Source: https://runway.com/research/introducing-praxis-1 — fetched 2026-11-12 (page carries a Nov 11 update banner)

Research · September 2026
Introducing
Praxis-1
An open-weight world action model that turns Runway's video pretraining into control for real robots.
Update: As of November 11, Praxis-1 is now available. Read more about it in our announcement and technical report.
Praxis-1
Contents
Introduction
Video Pretraining
Early Partners
Open Weights
Early Access
Praxis-1 · front view · 1x speedside view“Pick up the tennis ball and put it in the box.”
Today we're announcing Praxis-1, our first open-weight world action model. It's built on the same large-scale video pretraining behind our general world models. We're actively testing Praxis-1 with early partners across a variety of embodiments, and will release it publicly in the coming months.
Every robotics project with ambitions of large-scale deployments runs into the same problem: real-world data is scarce and expensive to collect in the volume a generalist policy needs. For deployments with frequent edge cases, like autonomous driving or household robotics, there’s no practical path to collect the data required for training, let alone at meaningful volume.
Video, however, is effectively limitless, and is becoming infinite as generative models reach parity with real video on both quality and speed. People film and upload more of everyday life each day than any robot lab could capture through teleoperated demonstrations. More recently, we've found that simulating robot policies inside our world model predicts real-world results with 0.95 correlation, comparing favorably to more expensive 3D reconstruction–based techniques. Praxis-1 extends our bet that the best policy models will learn from video, and use that scale to bring embodied intelligence to every industry on earth.
Video Pretraining As a Foundation for Policy
We’ve recently extended our work on pretraining large video models into interactive, real-time video models like Solaris and GWM Worlds 2. By teaching our models how to generate accurate physics — how objects behave, how hands move, what a task looks like partway through — we’ve created dynamic, complex environments for agent training in the digital and physical world. Praxis-1 brings the same approach to robotics, providing a generalist policy model for robotics developers and researchers that works across any embodiment or environment, no matter how complex.
A policy that already understands physical plausibility and object behavior from video pretraining has an enormous head start on one built from action data alone. The premise is similar to language models learning on available text; teaching those models the structure of the world from large-scale data allows them to now operate effectively in settings that differ from their training sets.
Figure 1 — Multi-step tasks in complex environments
The base approaches the shelf, navigates towards the object, takes the book and puts it away. 1x speed
01Approaches the shelf02Assesses the approach03Picks up the object04Removes it from the environmentWe find that the same pattern holds in robotics: policy performance improves as we scale third-person video. The bottleneck on a capable policy becomes how much general video a model can train on.
Figure 2 — Web video matches teleop robot video
Final placement error after finetuning, against hours of pretraining video. Lower is better.
20 cm18 cm16 cm12 cm20 cm18 cm16 cm12 cm10¹ hrs10² hrs10³ hrsWeb video, from scratch16.1 cmTeleop robot video, from scratch16.0 cmError bars and band: ±1 SEM over 93 evaluation pairs. Differences smaller than a bar are not significant.
Figure 3 — Where policies usually break
Four cases that defeat policies trained on demonstrations alone. 1x speed
Rigid, repeatedMany near-identical objects, one targetClutteredOcclusion, overlapping tablewareTransparentIce and clear plastic, weak depth cuesDeformableCloth with no fixed grasp pointTesting With Early Partners
We're rolling Praxis-1 out to key partners ahead of a public launch, including Noble Machines, Standard Bots and Ultra, each running the model on their own hardware. We’ll be providing early access to additional partners pre-launch. This testing is designed to ensure both efficacy and safety – we’ll evaluate on a variety of embodiments and environments, identifying and closing potential gaps before moving to general availability.
Noble Machines
Bimanual manipulation. 2x speed
noblemachines.ai

Standard Bots
6-DoF arm · RO1. 2x speed
standardbots.com

Ultra
Mobile base
ultra.tech

Figure 4 — Studio, home
The same policy moved between environments without retraining. 1x speed
StudioControlled light, fixed rigKitchenDomestic counter, mixed lightWhy Open Weight
When Praxis-1 releases publicly, we'll ship it with open weights rather than as a closed model. We believe that U.S. leadership in physical AI is critical. Regaining our global lead in manufacturing, accelerating productivity across our economy and securing ourselves and our allies will rely on this. Achieving this will require a significant increase in investment across both hardware and software, but it will also require a level of interoperability and openness from American models that does not currently exist for physical use cases. We view open world models as a compounding advantage that gives hardware developers flexibility and control they don’t currently have.
Early Access
We are providing pre-launch access to select partners. If you are interested in testing Praxis-1 on your own hardware ahead of public release, contact our robotics team.
Contact our robotics team
