# Capture: https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/
Captured 2026-11-17 via curl; visible text of the page's <main> element. Images and videos are not included; the four result charts are saved under raw/assets/gemini-robotics-2-5/. Link targets in the article body:
  whole-body intelligence -> https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
  our robotics partners -> https://deepmind.google/models/gemini-robotics/#partners
  Apptronik’s Apollo 2 -> https://apptronik.com/apollo/apollo-2
  Franka Duo platform -> https://franka.de/fr3-duo
  Gemini Robotics ER -> https://deepmind.google/models/gemini-robotics/embodied-reasoning/
  Gemini Robotics 2.5 -> https://deepmind.google/models/gemini-robotics/vla/
  agentic robotics evaluations -> https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf#page=200
  ASIMOV-Jailbreak -> https://huggingface.co/datasets/google/asimov_agentic
  robotics research capabilities -> https://developers.googleblog.com/gemini-4-argon-for-robotics/

November 10, 2026 Models
# Gemini Robotics 2.5 accelerates real-world general dexterity
Carolina Parada

Share


Your browser does not support the video tag.

We’re enabling robots to learn faster for the real world - from everyday skills to the factory floor
Today, we are introducing Gemini Robotics 2.5, our most capable vision-language-action (VLA) model to date. Gemini Robotics 2.5 increases both the breadth of skills a robot can learn and the speed at which it can acquire them. This enhances dexterity, reliability, and safety to help robots step out of the lab and into more unstructured, real-world environments, where they can assist people with a greater range of tasks.
Earlier this year, we brought whole-body intelligence to robots of many types, including humanoids. Now, in large part thanks to Gemini 4 Argon's ability to accelerate robotics research, we have further pushed the frontier of physical intelligence. We tested Gemini Robotics 2.5’s capabilities in task breadth, performance, and complexity across over 200 distinct tasks, though this approach could scale to many more.
Gemini Robotics 2.5 marks a leap forward in three key areas:
- Dexterity: Our robots can perform significantly more tasks with greater performance and dexterity — from using everyday tools to handling delicate, flexible objects.
- Reliability: During a real-world proof-of-concept on Mercedes-Benz production lines, our models helped Apptronik’s Apollo 2 humanoid pick and pack automotive parts with a 96% success rate. This could enable robots to take on monotonous work, to enable technicians to focus on complex build tasks.
- Safety: As robots move into everyday environments, we have improved physical safety steerability and introduced a new benchmark to test against adversarial jailbreaks specific to robotics.
Gemini Robotics 2.5 is rolling out to our robotics partners.

Your browser does not support the video tag.

Your browser does not support the video tag.

## Expanding task breadth, reliability, and dexterity
Because real-world environments are unstructured and unpredictable, robots must be able to handle everyday objects with both fine precision and high reliability.
With Gemini Robotics 2.5, we expanded the model capabilities in task breadth, performance, and complexity. We evaluated the model across 200 distinct tasks — such as serving food with tongs, tying a bow on a gift box, and pipetting a liquid. These tasks represent a step toward human-level dexterity by combining a number of skills, including advanced tool use, complex manipulation of deformables, and handling delicate objects with finesse.
Our evaluations show significant increases in task precision, robustness, and speed. Compared to previous baselines, Gemini Robotics 2.5 achieves a 30% to 100% higher success rate depending on the type of task, while completing tasks 20% to 30% faster.
Like our previous Gemini Robotics models, it natively works with many different robot types, including Apptronik’s Apollo 2 humanoid robot (featuring the five-finger, 22 degree-of-freedom SharpaWave hand) and the Franka Duo platform with two-fingered parallel grippers.

Slide 1 of 4

### Testing real-world reliability with Apptronik’s Apollo and Mercedes-Benz
The ultimate measure of a robotics model is whether it can perform dependably in an active workplace. To put Gemini Robotics 2.5 to the test, we partnered with Apptronik and Mercedes-Benz to use Apollo 2 humanoid robots on active automotive production lines in Kecskemét, Hungary, and Sindelfingen, Germany.
Robots struggle to adapt to new unpredictable environments, our Gemini Robotics models give Apollo the ability to think, reason over multiple steps, and take action adapting to changes. In this proof-of-concept, Apollo 2 autonomously performs automotive kitting: the repetitive, physically taxing task of sorting individual parts from bulk bins into organized trays in the exact order needed for each vehicle on the line. Offloading this monotonous prep work helps keep the assembly line moving, while freeing up technicians to focus on complex build tasks.
Using our embodied reasoning model (Gemini Robotics ER) to keep track of the workflow, and the Gemini Robotics 2.5 actions model to control its hands and arms, the robot reaches into supply bins, picks up metal automotive brackets, and places them into sequencing containers, all while correcting for any gaps. Achieving a 96% success rate, this pilot shows promising progress toward widespread real-world industrial applications.

This is what we built Apollo for: useful work alongside people in real industrial settings. Pairing Apollo 2 with Gemini Robotics, we saw the models improve dramatically in just a few weeks of post-training and carry over to Mercedes-Benz production with very little drop-off. This is the foundation for bringing humanoid robots to industrial and commercial environments at scale.

Jeff Cardenas
Co-founder and CEO, Apptronik

Your browser does not support the video tag.

Apollo 2 using Gemini Robotics 2.5 to autonomously perform automotive kitting at a Mercedes-Benz factory.

## Advancing steerability and agentic safety for robots
As robots operate in messy, everyday spaces, physical safety is paramount. To help ensure this, we have significantly advanced Gemini Robotics 2.5’s safety features.
Gemini Robotics 2.5 uses inference-time reasoning guidance to steer around physical hazards in real-time. Much like safety classifiers add a protective layer around Gemini’s responses, this guidance allows the robot to navigate complex environments securely. In our evaluations, this capability boosted safe task completion around obstacles by 33% and around nearby people by 43%.
We are also advancing safety for long-horizon, agentic tasks. Gemini 4 Argon currently leads our agentic robotics evaluations across unsafe task refusal, resolving uncertainty, and working in proximity to humans. To test jailbreak robustness, we are releasing ASIMOV-Jailbreak, a new open-source benchmark containing hundreds of prompts that disguise unsafe requests across dozens of scenes. Argon achieves a 99.5% jailbreak resistance — a significant improvement over the 82% rate of our previous baseline, Gemini Robotics ER 2.

Your browser does not support the video tag.

Safe human-aware robot actions enabled by GR-2.5 steerability

## Accelerating robotics with Gemini 4 Argon
To teach robots new skills, researchers need massive amounts of physical data and highly efficient modeling algorithms. Gemini 4 Argon’s robotics research capabilities helped solve these bottlenecks by acting as a simulation engine, which greatly accelerated our development of Gemini Robotics 2.5.

Your browser does not support the video tag.

Examples of Gemini 4 Argon’s robotics research capabilities accelerating Gemini Robotics 2.5

Argon can generate thousands of varied, simulated practice runs from a real-world camera scene and build a realistic digital twin. Combined with real training demonstrations, this enables the robot to more quickly generalize to new scenes and objects. Argon can also help researchers hypothesize why task failures happen from video footage and test the best improvements both in simulation and directly on real robots.
Accelerated by frontier intelligence models like Gemini 4 Argon, Gemini Robotics 2.5 marks an important milestone on the path toward solving physical AGI. By advancing in dexterity, real-world reliability, and rigorous safety, we are building the physical intelligence necessary for robots to work alongside people and solve real-world challenges
## Acknowledgements
This work was developed by the Gemini Robotics team. For their leadership and support of this effort, we’d like to thank: Huizhong Chen, Radu Soricut, Jean-Baptiste Alayrac, Melvin Johnson, Edward Grefenstette, Claire Cui, Jon Shlens, David Thacker, Zoubin Ghahramani, Clement Farabet, Koray Kavukcuoglu, and Demis Hassabis. We’d like to recognize the many teams across Google and Google DeepMind that have contributed to this effort including Research, Legal, Marketing, Communications, Responsibility and Safety Council, Responsible Development and Innovation, Policy, Strategy and Operations, and our Business and Corporate Development teams. Finally, we’d like to thank our partners: Agile, Apptronik, and Mercedes-Benz teams for their support on this release.

## Related post

### Gemini 4 Argon for Robotics
October 2026Models

Learn more

### Gemini Robotics 2 brings whole body intelligence to robots
July 2026Models

Learn more

### Gemini Robotics 1.5 brings AI agents into the physical world
September 2025Models

Learn more

### Gemini Robotics brings AI into the physical world
March 2025Models

Learn more
