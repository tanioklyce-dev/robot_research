---
source_url: https://bitrobot.ai/whitepaper
collected: 2026-09-11
published: 2025-03-10
author: Michael Cho, Jonathan Victor, Juan Benet
title: BitRobot Network Whitepaper
companion_urls:
  - https://bitrobot.ai/origin (timeline; appended below)
  - https://bitrobot.ai/network (subnet list, FAQ headings, research citations; appended below)
note: HTML page, tag-stripped. The §5.1 reward formula is an image with no alt text and is not captured; only its variable definitions are. §4.4 and §4.5 repeat one paragraph on the live page (rendering duplication, preserved as-is).
---

# BitRobot Network Whitepaper (2025-03-10) — tag-stripped capture

BitRobot / Whitepaper
core methodology
Network Whitepaper
march 10, 2025
Michael Cho, Jonathan Victor, Juan Benet
Contents
Section 1: Abstract
Section 2: introduction
Section 3: Problem definition
section 4: network design & protocol
Section 5: Economy
Section 6: Future work
1. Abstract
The BitRobot Network whitepaper proposes a subnet-based architecture designed for distributed robotic work and collaboration. Key components include Verifiable Robotic Work (VRW) for robotic task definition and verification, Equipment Node Tokens (ENT) for equipment ownership and network access, and Subnets as the operational layer for task execution. Subnets are managed by Subnet Owners, who oversee their operation; Subnet Validators, who verify task completion; and Subnet Contributors, who supply equipment and resources. The economic model aims to align incentives across participants and facilitates seamless coordination. This framework enables the aggregation of critical resources, with the aim of driving innovation and progress in the field of Embodied AI.
2. Introduction
The arms race for Artificial General Intelligence (AGI) is in full motion - with companies and governments racing to acquire the data, compute and talent required to create the most performant frontier models. Given the pace of innovation for AI in the digital context (e.g. for text, images, and videos), there are high hopes that a similar step change in growth is around the corner for the world of robotics. This optimism is bolstered by momentum across several critical trends:
Transformers scaling across modalities
The transformer architecture [1] has proven versatile in its ability to scale both in quantity, with large amounts of data and compute, and scope, across a range of modalities (e.g. text, images, and videos) - leading to a single unified model that works across multimodal domains (e.g. VLMs [2]). Robotics data, when thought of as transformer tokens, can fit within this same architecture, and therefore should receive scaling benefits when combined with other modalities (e.g. VLAs [3]).
Learning from demonstrations
Human teleoperated demonstrations (e.g. techniques like behavioral cloning, imitation learning, offline reinforcement learning, etc) have begun to show real promise. Tasks that the field has previously struggled with [4, 18] (e.g. clothes folding) are starting to see positive momentum - and if scaled may help solve for generalization of challenging domains (e.g. dexterous manipulation).
Advancements in simulation
Simulations have evolved substantially in certain domains (e.g. locomotion), where policies trained in simulations can often transfer zero-shot to real-world embodiments such as quadrupeds [5] and drones [6]. The rise of generative AI, the increasing number of realistic world models [7, 8, 9] and the proliferation of physics engine toolings [10, 11, 12] all point to the potential for using simulations to accelerate progress by building a more robust foundation for models.
Learning from videos
Web-scale videos also point towards a rich, largely untapped, reservoir of training data that can help advance Embodied AI. In particular, human videos, especially those filmed with ego-centric views, show promise for humanoids and bimanual robotic arms [13, 14]. Meanwhile, progress is also being made where human videos may be closing the gap with labor-intensive teleoperated robotic data [15].
Learning from cross embodiment
Increasing research evidence indicates that there may be significant positive learning transfer when Embodied AI models are trained from a diverse range of robotic embodiments. This suggests that the absolute quantity of data required may be substantially reduced and that the resulting models may be more generalizable if the training datasets come from a wide array of robot types [16, 17].
Advancements in robotic hardware
The maturity of adjacent industries (e.g. smartphones, EVs, semiconductor chips) translates to strong supply chains and cheap components for inputs to robotic systems (e.g. actuators, cameras, GPS, IoT sensors). For certain types of robots (e.g. consumer-grade sidewalk robots, robotic arms, quadrupeds, etc), this means affordable hardware that can be distributed at scale at consumer price points. In parallel, there are increased innovations on new hardware designs, ranging from tendon-driven mechanics, pneumatics and hydraulic-based actuations and various new touch/tactile sensors.
3. Problem Definition
Despite the momentum described above, Embodied AI still faces many real-world constraints that make scaling of physical intelligence a significant bottleneck in the pursuit of true AGI.
3.1 Data Challenges
Below we describe the challenges facing the three main types of robotic data (synthetic data, real-world video data, and teleoperation data) needed for improving Embodied AI.
Sim-to-real gap
Despite its success in certain subfields, synthetic data has had challenges transferring zero-shot in real world settings for many other robotic tasks (e.g. in-the-wild robotic navigation, robotic manipulation with deformable objects). While simulations can drastically speed up the creation of training scenarios, the challenge is in focusing the search space to the long tail of edge cases that are actually relevant in the real world.
Embodiment gap
Real-world video data, while a promising accelerant to Embodied AI research, suffer from the embodiment gap. Video data lacks precise information about physical presence and contextual awareness, making it difficult to build an AI that can replicate the exact responses a human might have. For example, thousands of video hours of Lionel Messi playing football can build a basic foundation, but lacks information about his specific body, data processing, and sensory inputs - making it challenging to exactly replicate his actual decision making and execution on the field.
Unconscious-to-conscious gap
Unlike other modalities (e.g. text) which are available at scale on the public internet, teleoperation data, collected in real world settings capturing human action inputs as a response to external events, requires costly coordination and investment of both physical hardware and human man-hours to produce. As a result, while a promising data source for Embodied AI models, very few large-scale teleoperation datasets naturally exist [19].
Critically, while many robotics researchers agree that these are the primary data bottlenecks to solving Embodied AI, there is a lack of consensus about which challenge (or combination of challenges) are the most pressing to solve first.
3.2 Resource Challenges 
Furthermore, while robotics data remains a significant bottleneck, real-world evaluations and resource asymmetries may prove to be an even larger point of friction to the pace of Embodied AI innovations.
Lack of hardware for real-world evaluations
For Embodied AI, the only way to evaluate a new model is to observe how the model fares in real world settings. Witnessing failure cases (e.g. a self-driving car driving into a lamp post) is critical in understanding the limits to what a model can do - and as the model improves, the rate of failure is only observable with large-scale fleets of robots. As a result, the ability for researchers to evaluate their own models is rate limited, without access to large amounts of robots to which to deploy their models.
Resource distribution asymmetry
While a few large corporate labs are able to make substantial progress (given they have access to dataset flywheels, evaluation platforms, and compute, storage and bandwidth) - large pools of researchers (in academia or early-stage startups) and hardware providers are unable to iterate at the same pace. This points to a worrying trend of significant concentration of scientific progress in just a handful of entities.
Below is an illustration of the asymmetry of access to various resources amongst the various entities.
Fig 1: Rough mapping of resource access for key players in the Embodied AI landscape.
4. The BitRobot Network: Design and Protocol
4.1 Overview of the BitRobot Network
In response to the challenges listed above, we present the BitRobot Network, a modular network of robotic subnets, each generating valuable resources, to accelerate Embodied AI and robotics innovation.
In the BitRobot Network, subnets can be formed to solve for resource gaps on the path to Embodied AI. This can range from aggregating hardware (e.g. fleets of robots for massively parallelized evaluation of new AI models) or human labor (e.g. teleoperators to control various robots) to more sophisticated coordination among multiple resources (e.g. researchers testing latest models on real world robot fleets while training on GPUs provided by compute providers). By decentralizing resource aggregation, BitRobot can leapfrog the resources that any individual corporate lab might amass on its own - and democratize access across the full Embodied AI community.
The subnet structure allows for permissionless resource formation and experimentation - while aligning all participants around a shared economy and outcome.
4.2 Key Components of the BitRobot Network
The BitRobot Network is built around the following components:
Verifiable Robotic Work (VRW)
The Verifiable Robotic Work (VRW) is a quantifiable and verifiable measure of any robotic work that is deemed useful to help advance Embodied AI. This may include work done collecting data in the real world (e.g. the total distance driven by sidewalk robots, the difficulty scores of these sidewalk robot drives, etc) or in simulation (e.g. the number of scenarios generated for robotic arms that are tasked to fold clothes, the quality scores of such generated scenes, etc). VRW may also include the work done in creating Embodied AI models and evaluating them in either real-world settings or simulation environments. Finally, different types of Subnet Contributors may have different VRW even within the same Subnet (e.g. teleoperator based on duration of operating robots, robot keepers based on robot online hours, etc).
Embodied Node Token (ENT)
The Embodied Node Token (ENT) is a unique identifier within the system, designed to serve as the digital twin of a physical robot. Represented as an NFT, the ENT ensures a unique identity for each robot in the BitRobot Network. Each ENT requires collateral to receive on-chain payments, which can be used to enforce accountability and incentivize compliance within the system. The ENT also functions as the conduit for payments for robot owners.
Subnets
A BitRobot Subnet represents clusters of resources creating value for the BitRobot Network. Subnets can range in scope: from hardware acquisition, to creation of novel datasets, to creation of new AI models, to competitions. Subnets can work on a diverse range of tasks (defined by each Subnet’s Verifiable Robotic Work) and embodiments, resulting in a wide variety of outputs, ranging from real-world datasets, synthetic datasets, to new AI models, physical hardware fleet, etc. Within Subnets there are several roles: Subnet Owners, Subnet Validators, and Subnet contributors - though many participants may play multiple roles and work across multiple subnets. Subnets can earn income via direct payments (e.g. stablecoins for renting out a fleet of robots), by network emissions, or both.
Subnet Owners
Subnet Owners represent the creators of a subnet. Subnet owners must define the VRW for their subnet, the type of subnet outputs (e.g. dataset, AI models, cryptographic proofs), subnet validation, and the percent of subnet rewards to be distributed to the various participants in the Subnet. Subnet Owners can be individuals, groups of people, or protocols.
Subnet Validators
Subnet Validators evaluate the output of Subnet Contributors against the defined VRW for the subnet. Internal to the subnet, the scores assigned by Subnet Validators determine how incoming subnet rewards are split among Subnet Contributors. Subnets can have as few or as many validators as the Subnet Owners determine, and Subnet Validators may be Subnet Owners themselves.
Subnet Contributors
Subnet Contributors provide the necessary inputs for a subnet to create a useful output. Each subnet may have multiple types of contributors - ranging from researchers, to teleoperators, to robot manufacturers, and many more. Given each Subnet may be focused on a different outcome, it is expected that each subnet will have a different set of contributor types based on the requirements for their tasks.
4.3 Life cycles of Subnets and Contributors
4.3.1 Subnets
Subnets are instantiated by their owners, and are required to define several parameters including: reward splits, VRW definitions, and validation conditions. Subnets can be constructed to aggregate resources (e.g. humanoid robot pools for hire), to create novel datasets (e.g. urban navigation data), or to simply evaluate models.
Subnets can also be defined to be private or public - private subnets are not eligible for emissions, while public subnets are eligible. Private subnets are consumers of the frameworks and resources of the BitRobot Network, while public subnets may both be consumers and contributors (see Section 4.4 for more details). Public subnets will receive their share of rewards based on the delegation-weighted voting mechanism at every voting epoch. Funds received by subnets are split to reward Subnet Owners, Validators and Contributors based on each subnet’s predefined allocation rules.
Fig 4: Flowchart showing the major milestones from creation to the ongoing running of a public subnet
4.3.2 ENTs and Contributors
Once subnets are spun up, contributors can join subnets to participate in the defined forms of verifiable work. For human contributors, this can be as simple as taking on tasks available from the various subnets (e.g. teleoperating a robot) using a wallet as an identifier. For robot contributors, they first need to be registered with an ENT NFT. Robot owners (who own ENT NFTs) will be able to participate in multiple relevant subnets while maximizing the utilization rate of each physical robot.
Fig 5: Flowchart showing the major milestones for adding a robotic resource to a subnet
4.4 IP Assignment and Ownership 
Datasets and Models produced by public subnets (emission-receiving) in the BitRobot Network are by default open-sourced for non-commercial use. 
Any datasets or models produced by private subnets (non-emissions receiving) do not fall under this regime.
4.5 Governance
Datasets and Models produced by public subnets (emission-receiving) in the BitRobot Network are by default open-sourced for non-commercial use. 
Any datasets or models produced by private subnets (non-emissions receiving) do not fall under this regime.
BitRobot Foundation
The BitRobot Foundation’s mission is to advance Embodied AI research by facilitating the growth of the BitRobot Network.
To achieve this mission, the BitRobot Foundation will help grow and support infrastructure development work (e.g. tracking of work done by individual ENTs, networking support for subnets working on teleoperation, data pipeline support for subnets working on datasets generation, etc), providing administrative support for the Senate and evangelizing work (e.g. hackathons, grant administrations, etc), and supporting grants to develop the supporting ecosystem.
The BitRobot Foundation will also take on more Embodied AI research and engineering work over time in order to fully maximize the research and economic impacts arising from the commercial use of its IPs (datasets or AI models).
BitRobot Senate
The BitRobot Senate is composed of nominated representatives of the broader cryptocurrency and Embodied AI research communities - aimed at ensuring resources flow towards the subnets creating the highest value. The BitRobot Senate governs economic weights associated with network measurements (see Section 5.1 below) which are used to evaluate the value of the outputs generated by the subnets.
At regular intervals (called “Voting Epochs”), the BitRobot Senate will vote on the inclusion of new robotic subnets for emissions. At the same time, the BitRobot Senators will also individually vote on the weights proposals for network distributions assigned to each robotic subnet based on the performance and value contribution from the individual subnet to the overall network.
Gandalf AI
The BitRobot Foundation will develop and operate “Gandalf AI”, an ongoing effort to create a fully open-sourced AI agent model that provides weights proposals for network measurements and distributions for each robotic subnet, serving as a counter balance to the economic influence wielded by the Senate.
Network Participants
BitRobot Network participants can directly influence the impact of decisions made by Senators and Gandalf AI via delegation of their voting power. In this way, the participants can provide a check on any individual senator by allocating more decision making power with other senators or in an extreme case - entirely allocating decision making power to Gandalf AI.
5. BitRobot Economy
The BitRobot Economy is composed of a diverse set of participants from all stages of the value creation pipeline (early research, fundamental development, productionisation). The structure of the BitRobot economy aims to support all of these participants by balancing the flows of the economy across the different types of contribution to the value chain.
5.1 Economic Flows to Subnets
The BitRobot Senate and Gandalf AI will use a Measurement-Evaluation-Rewards (MER) loop to determine how emissions should be allocated between subnets. As described in the next section, BitRobot Network participants can increase (or decrease) the relative power of the BitRobot Senate or Gandalf AI’s votes via delegation.
Measurements
Defined via protocol governance, these are the metrics (and its relevant calculation) that subnets will be evaluated against. For example, a measurement may apply to a specific subnet (e.g. “Qualified Miles” for Subnet 1) or a more generic measurement that could be relevant to multiple subnets (e.g. number of rented humanoid robots). Members of the Senate and Gandalf AI will individually assign weights to each measurement, indicating their opinion of the relative importance of each metric against the rest.
Evaluation
Members of the Senate and Gandalf AI will individually evaluate subnets against each of the relevant metrics to create a distribution list per Member based on their own assessment.
Reward
Each Senator and Gandalf AI’s distribution lists are weighted by their delegations, summed, and normalized to produce the distribution for that epoch of emissions to each subnet.
Specifically, 
Dj : Weighted delegations to Gandalf AI or Senator 
Nl : New emissions in Voting Epoch l 
Eij : Evaluation weight % of Measurement i, submitted by Senator j
Mik : Measurement i, achieved by the relevant Subnet k Therefore, the amount of rewards distributed to Subnet k during epoch l, will be: 
Each Senator and Gandalf AI’s distribution lists are weighted by their delegations, summed, and normalized to produce the distribution for that epoch of emissions to each subnet.
Specifically, : 
Dj : Weighted delegations to Gandalf AI or Senator 
j : New emissions in Voting Epoch l : 
Evaluation weight % of Measurement i, submitted by Senator j : 
Measurement i, achieved by the relevant Subnet k Therefore, the amount of rewards distributed to Subnet k during epoch l, will be: 
Emissions flowing to each subnet are then distributed between Owners, Contributors, and Validators against the Verifiable Robotic Work rules defined by each subnet.
Emissions flowing to each subnet are then distributed between Owners, Contributors, and Validators against the Verifiable Robotic Work rules defined by each subnet.
Each Senator and Gandalf AI’s distribution lists are weighted by their delegations, summed, and normalized to produce the distribution for that epoch of emissions to each subnet.
Specifically, : 
Dj : Weighted delegations to Gandalf AI or Senator 
j : New emissions in Voting Epoch l : 
Evaluation weight % of Measurement i, submitted by Senator j : 
Measurement i, achieved by the relevant Subnet k Therefore, the amount of rewards distributed to Subnet k during epoch l, will be: 
Emissions flowing to each subnet are then distributed between Owners, Contributors, and Validators against the Verifiable Robotic Work rules defined by each subnet.
5.2 Economic Consumption
There are several areas where the BitRobot Network requires forms of economic consumption. Some of these areas are described below, but we envision more use cases to be defined by the community as the BitRobot Network matures.
Fee Payments
Subnet Registration Fees
These are fees paid per epoch by Subnet Owners to maintain an active subnet. Subnet Registration Fees create an economic cost for joining the BitRobot economy to prevent spam.
ENT Registration Fees
These fees are paid per epoch by owners of Robots upon registering new robots into the BitRobot economy.
Resource Allocation Fees
These fees are calculated as a small percentage of the revenue paid to Subnet Owners when third parties rent resources via subnets in the BitRobot ecosystem.
Licensing Fees
These are fees paid by third parties to commercially license the data or assets stewarded by the BitRobot Foundation.
Penalties
These are fees paid by any participant when violating conditions of the BitRobot Network or relevant subnets.
Collateral
Different components of the BitRobot Network (e.g. ENTs) may require economic collateral to be attached to ensure accountability and enable penalties for malicious actors that might attempt to abuse the BitRobot Network.
Delegating
BitRobot Network participants may delegate voting power to the BitRobot Senate or Gandalf AI, increasing the weight of the delegatee’s votes in determining how BitRobot Network emissions are steered to subnets.
5.3 Economic Loops
There are two primary economic loops in the BitRobot Ecosystem:
In the first economic loop, the network rewards are used to acquire useful robotic resources. This can be seen as assembling markets of resources (which may include any useful resource from compute to physical robots to teleoperator man-hours, etc) that can be consumed by any third-party. Thus network utilization incurs a fee, to balance the emissions and utilization.
Example:
 An AI lab hires a fleet of sidewalk robots to evaluate their latest model. The AI lab will pay a resource allocation fee to the network, with the remaining funds being allocated to the hardware owners (via the subnet’s definition of Verifiable Robotic Work) whose robots are used in the evaluation of the model.
In the second economic loop, the network rewards are used to both acquire a useful robotic resource, and create a useful output (e.g. dataset or AI model). When that output is licensed, the fees are used to support the BitRobot ecosystem.
Example:
 An AI lab wants to commercially license the robotic arm dataset created by the BitRobot Network. The license fees are used to support the BitRobot ecosystem.
6. Future Work
We have presented the BitRobot Network as a powerful framework for creating clusters of resources to accelerate Embodied AI. Below are areas BitRobot Network participants may consider for ongoing improvement:
Augmenting Verifiable Robotic Work With Cryptographic Proofs
At launch, the BitRobot Network will focus on Verifiable Robotic Work - a looser constraint (public inputs, public outputs, public transformations) that allows the BitRobot Network to address a wider swath of data collection, processing, and transformation - than what might be economically feasible given the state of zero knowledge protocols today. As the cost curves drop, we envision incorporating cryptographic guarantees to strengthen the economic loops in the ecosystem.
Markets and Services on top of Network Resources
We envision more sophisticated interactions being built by BitRobot Network participants on top of the primitives inside of the BitRobot economy. As the BitRobot Network stabilises the capital flows moving through the economy, we envision markets and services to form to improve the capital efficiency for providers on the BitRobot Network.
Markets and Services on top of Network Resources
BitRobot is maximally useful when it becomes the global hub for talent, manufacturer, service providers, research labs, and AI companies to coordinate their resources against tasks that accelerate Embodied AI. A critical focus will be expanding the scope of participants to accelerate the flywheel of growth in the ecosystem.
AI Agent Controlled Resources
A key feature of designing the BitRobot Network to be protocol first is in enabling AI Agents to control physical resources. We expect enabling composability between the BitRobot Network and AI agents to be a continuing focus as the BitRobot Network scales and AI agents mature.
Evolving Governance
At launch, we expect the BitRobot Foundation and the Senate to play important roles in helping bootstrap the BitRobot Network and helping steer the flywheel for growth for the BitRobot Network. As the BitRobot Network matures, we expect more responsibilities to transition directly between BitRobot Network participants and Gandalf AI.
References
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin. 2017. Attention is all you need. 
https://arxiv.org/abs/1706.03762
Akash Ghosh, Arkadeep Acharya, Sriparna Saha, Vinija Jain, Aman Chadha. 2024. Exploring the Frontier of Vision-Language Models: A Survey of Current Methodologies and Future Directions 
https://arxiv.org/abs/2404.07214
Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, Irwin King. 2024. A Survey on Vision-Language-Action Models for Embodied AI 
https://arxiv.org/abs/2405.14093
Julen Urain, Ajay Mandlekar, Yilun Du, Mahi Shafiullah, Danfei Xu, Katerina Fragkiadaki, Georgia Chalvatzaki, Jan Peters. 2024. Deep Generative Models in Robotics: A Survey on Learning from Multimodal Demonstrations 
https://arxiv.org/abs/2408.04380
Yecheng Jason Ma, William Liang, Hung-Ju Wang, Sam Wang, Yuke Zhu, Linxi Fan, Osbert Bastani, Dinesh Jayaraman. 2024. DrEureka: Language Model Guided Sim-To-Real Transfer 
https://arxiv.org/abs/2406.01967
Jiaxu Xing, Ismail Geles, Yunlong Song, Elie Aljalbout, Davide Scaramuzza. 2024. Multi-Task Reinforcement Learning for Quadrotors 
https://arxiv.org/abs/2412.12442
Anthony Hu, Lloyd Russell, Hudson Yeo, Zak Murez, George Fedoseev, Alex Kendall, Jamie Shotton, Gianluca Corrado. 2023. GAIA-1: A Generative World Model for Autonomous Driving https://arxiv.org/abs/2309.17080
World Labs. 2024. Generating worlds. 
https://www.worldlabs.ai/blog
Nvidia. 2025. Nvidia Cosmos. 
https://www.nvidia.com/en-us/glossary/world-models
Stone Tao, Fanbo Xiang, Arth Shukla, Yuzhe Qin, Xander Hinrichsen, Xiaodi Yuan, Chen Bao, Xinsong Lin, Yulin Liu, Tse-kai Chan, Yuan Gao, Xuanlin Li, Tongzhou Mu, Nan Xiao, Arnav Gurha, Zhiao Huang, Roberto Calandra, Rui Chen, Shan Luo, Hao Su. 2024. ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI 
https://arxiv.org/abs/2410.00425
Zhou Xian, Yiling Qiao, Zhenjia Xu, Tsun-Hsuan Wang, Zhehuan Chen, Juntian Zheng, Ziyan Xiong, Yian Wang, Mingrui Zhang, Pingchuan Ma, Yufei Wang, Zhiyang Dou, Byungchul Kim, Yunsheng Tian, Yipu Chen, Xiaowen Qiu, Chunru Lin, Tairan He, Zilin Si, Yunchu Zhang, Zhanlue Yang, Tiantian Liu, Tianyu Li, Kashu Yamazaki, Hongxin Zhang, Huy Ha, Yu Zhang, Michael Liu, Shaokun Zheng, Zipeng Fu, Qi Wu, Yiran Geng, Feng Chen, Milky, Yuanming Hu, Guanya Shi, Lingjie Liu, Taku Komura, Zackory Erickson, David Held, Minchen Li, Linxi "Jim" Fan, Yuke Zhu, Wojciech Matusik, Dan Gutfreund, Shuran Song, Daniela Rus, Ming Lin, Bo Zhu, Katerina Fragkiadaki, Chuang Gan. 2024. Genesis: A Generative and Universal Physics Engine for Robotics and Beyond 
https://genesis-embodied-ai.github.io/
Kevin Zakka, Baruch Tabanpour, Qiayuan Liao, Mustafa Haiderbhai, Samuel Holt, Jing Yuan Luo, Arthur Allshire, Erik Frey, Koushil Sreenath, Lueder A. Kahrs, Carmelo Sferrazza, Yuval Tassa, Pieter Abbeel. 2025. MuJoCo Playground https://playground.mujoco.org/assets/playground_technical_report.pdf
Shikhar Bahl, Russell Mendonca, Lili Chen, Unnat Jain, Deepak Pathak. 2023. Affordances from Human Videos as a Versatile Representation for Robotics 
https://arxiv.org/abs/2304.08488
Ruijie Zheng, Yongyuan Liang, Shuaiyi Huang, Jianfeng Gao, Hal Daumé III, Andrey Kolobov, Furong Huang, Jianwei Yang. 2024. TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies
 https://arxiv.org/abs/2412.10345
Juntao Ren, Priya Sundaresan, Dorsa Sadigh, Sanjiban Choudhury, Jeannette Bohg. 2025. Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning. 
https://arxiv.org/abs/2501.06994
Open-X Embodiment authors. 2024. Open X-Embodiment: Robotic Learning Datasets and RT-X Models. 
https://arxiv.org/abs/2310.08864
Lawrence Yunliang Chen, Kush Hari, Karthik Dharmarajan, Chenfeng Xu, Quan Vuong, Ken Goldberg. 2024. Mirage: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting https://arxiv.org/abs/2402.19249
Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Lucy Xiaoyang Shi, James Tanner, Quan Vuong, Anna Walling, Haohuan Wang, Ury Zhilinsky. 2024. π0: A Vision-Language-Action Flow Model for General Robot Control 
https://www.physicalintelligence.company/download/pi0.pdf
Kevin Black. 2024. From Octo to π0: How to train your generalist robot policy. 
https://www.youtube.com/live/ELUMFpJCUS0?si=3hKJD8C9qpFQokHd&t=16864

---

# Companion: bitrobot.ai/origin (captured 2026-09-11)

BitRobot / Origin
origin
From weekend project
to 
global robotics network
From weekend project
to 
global robotics network
A chronological record of experiments, milestones, and decisions leading to the BitRobot Network.
A chronological record of experiments, milestones, and decisions leading to the BitRobot Network.
Network timeline
begins 2022
archive data
development history
2022
FrodoBots Lab
FrodoBots Lab started as a weekend project by brothers Michael and Sam Cho to gamify robotics data collection. It quickly grew into a global effort connecting gamers, robots, and researchers—laying the foundation for the BitRobot Network.
jul 2023
ET Fugi
FrodoBots Lab launched its first game, turning sidewalk robots into playable characters in a global scavenger hunt. Thousands joined across 40+ cities, showing how network incentives can drive large-scale robotics data collection.
Explore ET Fugi
may 2024
2k Dataset published
FrodoBots data enabled UC Berkeley’s RAIL Lab to train a state-of-the-art generalist navigation model, validating its value for frontier robotics research and proving that crowdsourced, real-world data can meaningfully advance embodied AI.
Explore dataset
oct 2024
Earth Rovers takes 1st place at IROS
FrodoBots realized that value lies not just in collecting data, but in testing models in the real world. To support this, they launched Earth Rovers—a robotic navigation challenge featured in a paper co-authored with leading researchers from Google DeepMind and academia.
Read the paper
feb 2025
Teaming up with Protocol Labs
Founder Juan Benet and former ecosystem lead Jonathan Victor join to develop the BitRobot Network—scaling FrodoBots’ early experiments into a platform for real-world data generation, model development, and evaluation across diverse robotics use cases.
BitRobot is built on the insight that data from any use case improves models for all use cases — enabling cross-domain learning through a diverse, shared robotics network.
REad press release
mar 2025
BitRobot publishes its whitepaper
The BitRobot Network whitepaper proposes a subnet-based architecture designed for distributed robotic work and collaboration.
read the paper
today
Global Collaboration,
Real-World Impact
Global Collaboration,
Real-World Impact
Global Collaboration,
Real-World Impact
The BitRobot Network is where real-world robotics meets global coordination—unleashing the collective power of people, machines, and code to drive embodied AI forward.
join the network
Network
Grand Challenges
publications
Whitepaper
origin
Shop
')">
')">
Join the Network

---

# Companion: bitrobot.ai/network (captured 2026-09-11)

BitRobot / Network
the network
Coordinating the 
collective
to advance 
embodied AI
Coordinating the 
collective
to advance 
embodied AI
Robotics breakthroughs won’t come from a single lab. They’ll come from the network
Robotics breakthroughs won’t come from a single lab. They’ll come from the network
join the network
Network spec
results published regularly
Active missions: 8
updated frequently
How Subnets Coordinate Robotics Resources and Contributors
vrw phases
monthly epochs
01
Coordinate
Robotic missions for data collection, training, or real-world testing.
people, robots, and compute organized.
02
Execute
Missions brought to life with real contributions.
data collected, identities created.
03
Verify
Impacts & data measured, results proven and verified.
contributions validated.
engage
Join or launch a 
subnet
Participation is open to contributors at all levels, from hobbyists to active researchers.
Build with the network
Open opportunities
ET Fugi
SN/01
Drive and Earn
Buy a sidewalk robot. Catch aliens and complete missions to accumulate Qualified Miles.
Start driving
telearms
SN/03
Control Robotic Arms on TeleArms
Complete robotic missions in simulation, no hardware required.
play now
Axis robotics
SN/04
Control Robotic Arms on Axis
Perform expert telemetry to complete robotics tasks in simulation and earn dual network rewards
play now
lab access
Frequently Asked Questions
What is the BitRobot Network?
BitRobot is the platform for distributed robotics research and development, coordinating global resources to tackle key challenges in robotics.
What is the BitRobot Network’s business model?
How is the BitRobot Network related to FrodoBots Lab?
Why is BitRobot built as a blockchain network?
Frequently Asked Questions
What is the BitRobot Network?
BitRobot is the platform for distributed robotics research and development, coordinating global resources to tackle key challenges in robotics.
What is the BitRobot Network’s business model?
How is the BitRobot Network related to FrodoBots Lab?
Why is BitRobot built as a blockchain network?
published march 10, 2025
updated as necessary
full network spec
Read the whitepaper
View network architecture, protocol structure, governance, the BitRobot rewards program, and more. 
Start reading
Network
Grand Challenges
publications
Whitepaper
origin
Shop
')">
')">
Join the Network
Builders and researchers
selected partners
builders & researchers
Research Citations
Latest public
dataset usage
UC Berkeley
Learning to Drive Anywhere via Model-Based Reannotation (MBRA)
Ajay Sridhar, Dhruv Shah, Catherine Glossop, Sergey Levine
Read Paper
MIT CSAIL
Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers (HPT)
Lirui Wang, Xinlei Chen, Jialiang Zhao, Kaiming He
Read Paper
Tampere University, Finland
Data Scaling for Navigation in Unknown Environments
Lauri Suomela, Naoki Takahata, Sasanka Kuruppu Arachchige, Harry Edelman, Joni-Kristian Kämäräinen
Read Paper
UC Berkeley
OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation
Noriaki Hirose, Catherine Glossop, Dhruv Shah, Sergey Levine
Read Paper
UCLA
From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning
Honglin He, Yukai Ma, Wayne Wu, Bolei Zhou
Read Paper
Peking University
SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation
Jiahang Liu, Tianyu Xu, Jiawei Chen, He Wang
Read Paper
University of Amsterdam
Automatic Control, Calibration and Recording for the FrodoBots
Qi Zhang, Arnoud Visser
Read Paper
