# NVIDIA Technical Blog — "Post-Train NVIDIA Cosmos 3 Edge for On-Device Robot Control"
# https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-edge-for-on-device-robot-control/
# Published 2026-08-19, by Saeed Babamohamadi (NVIDIA technical marketing engineer, physical AI).
# Captured 2026-09-12 by curl + <article>-tag extraction. The embedded tutorial video (Video 1) and
# the header GIF are lost; the "AI-Generated Summary" block at the top is the page's own (Nemotron) and
# is kept as it appeared. Code blocks survived with their line breaks collapsed in places.

Robotics

# Post-Train NVIDIA Cosmos 3 Edge for On-Device Robot Control

[img: A robot picking up a tool. https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/Cosmos.gif]

 Aug 19, 2026

 By Saeed Babamohamadi 

 Like

 Discuss (0)

L

T

F

R

E

## AI-Generated Summary

NVIDIA Jetson Thor can run the 4B Cosmos 3 Edge omni-model natively for on-device robot manipulation policies.
Post-training Cosmos 3 Edge on the Cosmos3-DROID dataset produces a policy that generates action chunks in about 1.53 seconds on Jetson AGX Thor T5000, enabling continuous real-time control.
In closed-loop RoboLab evaluation, the post-trained Edge policy reaches 22.9% success across 120 language-conditioned manipulation tasks.
The Cosmos framework provides reproducible post-training and deployment scripts through the open cosmos-framework repository.

### Next Steps
Download the Cosmos Edge policy weights and data to begin post-training.
Explore Cosmos Edge on Jetson for deployment guidance and examples.
Get the Cosmos framework code on GitHub to access post-training and deployment scripts. 

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. Learn more

Robots need policies that can adapt to their sensors, environments, and tasks while running on onboard computing hardware. World models offer a foundation for learning physical interactions, but their size can make on-device deployment difficult. This changes with the new NVIDIA Cosmos 3 Edge.

Cosmos 3 Edge is a 4B omni-model (with a 2B NVIDIA Nemotron-based reasoner) in the Cosmos 3 family. It was pretrained on the same physical-world data as NVIDIA Cosmos 3 Nano and NVIDIA Cosmos 3 Super and starts with the same grounding in how objects move and interact. Plus, the model is small enough to run on-device on NVIDIA Jetson Thor.

## What you’ll build

By the end of this tutorial, you’ll have a post-trained Cosmos 3 Edge manipulation policy that can run on Jetson Thor and be evaluated in closed-loop simulation.

You’ll learn how to:

Post-train Cosmos 3 Edge to predict robot actions.

Serve the resulting policy on Jetson Thor.

Run inference inside a receding-horizon control loop.

Evaluate policy behavior in closed-loop simulation.

Each step is reproducible from the open cosmos-framework repo, and the released checkpoint is available on HuggingFace.

Video 1. How to post-train NVIDIA Cosmos 3 Edge into an on-device robot policy

## Why post-train Cosmos 3 Edge for on-device robot manipulation?

World foundation models are pretrained on large multimodal datasets that capture patterns in object motion and physical interaction, such as how objects fall, slide, and respond to contact. Cosmos natively generates actions based on physical understanding and prediction capabilities. This prior knowledge provides a useful starting point for robot-policy training rather than requiring the policy to learn all physical relationships from task-specific demonstrations.

Deploying these models on a physical robot, however, introduces two practical constraints:

Device memory: The model and its runtime state must fit within the memory available on the robot.

Control latency: The complete inference pipeline must be fast enough to support the robot’s required control frequency.

Post-training Cosmos 3 Edge addresses each of these constraints. The resulting policy model fits within Jetson Thor’s memory, so inference runs directly on the robot rather than being offloaded to a data-center GPU.

The remaining factor is control latency. The DROID action policy runs in real time, directly on the robot. On an NVIDIA Jetson AGX Thor T5000, it generates each action chunk in about 1.53 seconds (running at 640×540 resolution and 15 Hz), while a single chunk covers roughly 2.13 seconds of robot motion. Because the next chunk is ready before the current one finishes, the arm moves continuously, with no data-center GPU in the loop. The policy supports continuous streaming on-device by generating action chunks and replanning after each inference cycle. It doesn’t replan after every observation.

In closed-loop RoboLab tasks, the post-trained policy reaches 22.9% success. Together, these results show that a 4B world foundation model can serve as a practical, real-time, on-device policy backbone. This model fits on a Jetson AGX Thor and runs entirely on the robot.

## What data does the policy train on?

The release policy in this tutorial trains on the nvidia/Cosmos3-DROID dataset. It contains 76k successful teleoperated trajectories, approximately 350 hours across 86 tasks and 564 scenes, collected with a Franka Panda arm and Robotiq gripper.

The dataset is packaged in LeRobotDataset v3.0 format at 640 × 360 resolution. Prepare it in three stages:

Filter idle and non-task frames.

Select successful demonstrations for training.

Apply random cropping, rescaling, and color jitter during training.

hf download nvidia/Cosmos3-DROID --repo-type dataset --local-dir Cosmos3-DROID

## Bring your own robot data

Convert your data to the LeRobot Dataset v3 (per-frame camera video, joint states, gripper state, actions, task instruction).

For a DROID-like Franka setup, the primary change is the dataset path. A different embodiment needs its own experiment configuration that defines the action space, dimensionality, camera layout, and normalization settings.

Cosmos 3 supports several embodiments, including dual-arm Franka, UR, WidowX 250, LeRobot SO101. See the Cosmos 3 Edge model card for the embodiment list.

### Prerequisites

Before starting, confirm that you have:

The latest Cosmos framework release.

The validated training hardware: NVIDIA DGX Station with the NVIDIA GB200 Grace Blackwell Superchip or the NVIDIA GB300 Grace Blackwell Ultra Desktop Superchip.

The supported NVIDIA CUDA and container versions: CUDA 13.0 (cu130), NGC 26.06-py3.

Access to the Cosmos 3 Edge base checkpoint.

Access to the Cosmos3-DROID dataset.

A Hugging Face access token.

This is foundation model post-training, not a single-GPU fine-tune. The validated run uses 64 nodes of 4× GB200 for 60K iterations, roughly 68 hours (~17.4K GB200-hours). Plan compute accordingly.

 | Setting | Value
 | Initialization | Cosmos3 Edge checkpoint
 | Action space | joint_pos: 8-D absolute (7 joints + gripper)
 | State | Proprioception enabled (use_state=true)
 | Observation | 3-camera canvas: wrist (360×640) over two exterior views (180×320 each) → 540×640
 | Action chunk | 32 future actions at 15 Hz per prediction
 | Action heads | Freshly initialized encoder + decoding MLP + embedding tokens, 5× LR multiplier
 | Loss balance | Vision flow-matching weighted to match action loss
 | Learning rate/batch | 2e-4; global batch 8192 (32 samples/rank × 256 ranks, HSDP 32×8)
 | Schedule | Long-cosine decay (cycle 100K) across a 10K-iteration run; checkpoint every 1K
 | Normalization | Raw joint values, no normalization
Table 1. Post-training configuration and hyperparameters

### How to run post-training

At a high level, post-training is broken into four steps:

Download the dataset.

Convert the base checkpoint to distributed-checkpoint (DCP) format.

Apply the curation filter.

Launch

# Download the Cosmos3-DROID dataset (success split)
hf download nvidia/Cosmos3-DROID --repo-type dataset --local-dir /path/to/Cosmos3-DROID

# Convert the base checkpoint to DCP (one-time; runs on CPU — it repacks weights, no GPU math)
python -m cosmos_framework.scripts.convert_model_to_dcp \ -o /path/to/Cosmos3-Edge-dcp --checkpoint-path Cosmos3-Edge

# Launch post-training
bash examples/launch_sft_action_policy_droid_nano.sh

### Edit and launch post-training script

Find this file in the repo:

cosmos_framework/configs/base/experiment/action/posttrain_config/action_policy_droid_nano.py

This launcher registers the recipe for Cosmos 3 Nano. To train Cosmos 3 Edge, make these three edits before launching:

Replace the NANO_MODEL_CONFIG import with EDGE_MODEL_CONFIG (from configs/base/experiment/sft/models/edge_model_config.py).

Set BASE_CHECKPOINT_PATH to the Cosmos 3 Edge DCP checkpoint from the conversion step.

Rename examples/launch_sft_action_policy_droid_nano.sh to examples/launch_sft_action_policy_droid_edge.sh

Everything else, including dataset, action space, curation filter, and training schedule, stays the same.

# Launch post-training
bash examples/launch_sft_action_policy_droid_edge.sh

For the latest end-to-end instructions, including checkpoint conversion, environment configuration, and curation-filter setup, see the DROID post-training reproduction guide and model card. These resources are updated alongside the repository. 

### How to deploy and run the policy on Jetson Thor

The policy is served by a WebSocket policy server speaking the OpenPI protocol, the same protocol used across the DROID policy ecosystem. The client sends an observation dictionary; the server returns an action chunk. For Edge, the server runs natively on Jetson Thor. At roughly 9 GB in BF16, the weights fit in Thor’s on-board memory, so both the policy server and the control client run on the robot with no data-center GPU in the loop.

Start the policy server on the robot

export HF_TOKEN=<your_hf_token>
# Thor: run eager; stock Triton wheels lack sm_110a kernels
export TORCHDYNAMO_DISABLE=1
python -m cosmos_framework.scripts.action_policy_server_robolab \
 --checkpoint_path nvidia/Cosmos3-Edge-Policy-DROID \
 --port 8000 \
 --format-prompt-as-json True
# first launch downloads weights and takes a few minutes; then:
curl localhost:8000/healthz # -> OK

Because the server runs on Thor, host="localhost", the request never leaves the robot. On device, the policy runs in real time. This is the on-device inference that Cosmos Edge enables.

### Smoke test (no robot needed)

The DROID policy is state-conditioned. Meaning that joint_position and gripper_position are real model inputs, not boilerplate. With no arm in the loop, zeros are the honest placeholder; this call just proves the server returns a well-formed action chunk.

import numpy as np
from PIL import Image
from openpi_client.websocket_client_policy import WebsocketClientPolicy

client = WebsocketClientPolicy(host="localhost", port=8000)

observation = {
 "prompt": "put the marker in the basket",
 "observation/wrist_image_left": np.asarray(Image.open("wrist.jpg")),
 "observation/exterior_image_1_left": np.asarray(Image.open("left.jpg")),
 "observation/exterior_image_2_left": np.asarray(Image.open("right.jpg")),
 "observation/joint_position": np.zeros(7, dtype=np.float32), # smoke test only
 "observation/gripper_position": np.float32(0.0), # smoke test only
}
result = client.infer(observation)
actions = result["action"] # [32, 8]: 7 joint positions + gripper, 15 Hz

### Running on the robot

The same call sits in a replanning loop. Each cycle reads fresh cameras and the arm’s measured joint and gripper positions (replacing the zeros above), executes a prefix of the chunk, then re-asks:

def get_observation():
 return {
 "prompt": "put the marker in the basket",
 "observation/wrist_image_left": read_camera("wrist"),
 "observation/exterior_image_1_left": read_camera("left"),
 "observation/exterior_image_2_left": read_camera("right"),
 "observation/joint_position": robot.joint_positions(), # REAL, 7 floats
 "observation/gripper_position": robot.gripper_position(),
 }

while not task_done():
 result = client.infer(get_observation())
 execute_actions(result["action"][:16], hz=15) # first 16 of 32, then replan

Executing only a prefix and replanning is standard practice: the policy self-corrects every few seconds, and because it is state-conditioned, each replan starts from where the arm actually is rather than where the previous chunk assumed it would be. Starting the server with video decoding enabled returns the policy’s imagined rollout alongside the actions, so you can inspect what the world model predicts for the chunk it emitted.

### Evaluate the policy in a closed-loop simulation

You don’t need a physical robot to validate a policy. In fact, evaluating a policy in simulation is recommended before evaluating directly on a physical robot to avoid unexpected behaviours before they affect developers or robots. RoboLab—the Isaac Lab-Arena benchmark behind the RoboLab leaderboard—is open, and its client connects to the same policy server. It executes each action chunk in physics and streams rendered observations back for a true closed loop across 120 language-conditioned manipulation tasks.

# Clone RoboLab and fetch the scene assets
git clone https://github.com/NVlabs/RoboLab.git && cd RoboLab
git lfs pull

# Build the sim image and run one task against the policy server
./docker/build_docker.sh latest
./docker/run_docker.sh latest
python policies/cosmos3/run.py --task BananaInBowlTask

# Or run headless across many envs for success-rate statistics
python policies/cosmos3/run.py --task BananaInBowlTask --num-envs 10 --headless

Swap --task for any of the 120 tasks to build a broader picture of policy behavior. Each run produces viewport and robot-camera videos plus a success log, so you can inspect both the outcome and the trajectory that produced it.

In closed-loop RoboLab evaluation, the post-trained Edge policy reaches 22.9% success across the task suite. That result is earned at a fraction of the inference compute of larger Cosmos3 variants (Nano reaches 36.8%), which is precisely the trade Edge is designed to make: real-time, fully on-robot autonomy at competitive success rates.

Note: NVIDIA Isaac Sim 5.x requires the NVIDIA RTX Server Driver Release 580 or later. Confirm the supported driver version in the RoboLab and Isaac Sim documentation before building.

## Post-training beyond robot control

Post-training techniques that improve robot control also extend to other capabilities, such as synthetic data generation for robot training. Developers can create specialized world models that generate high-quality synthetic data tailored to their environments and tasks for both indoor and outdoor robot training.

Aigen, for example, post-trained Cosmos to generate diverse synthetic crop and weed variations, enabling an autonomous weeding system to achieve strong performance using just 1% real-world data for training.

More broadly, Cosmos’s open weights and framework, with the OpenMDW1.1 license, make post-training a powerful, flexible, and easy way to create specialized, highly performant, and accurate custom models for physical AI.

## Get started

Download Cosmos Edge policy weights and data

Join the Cosmos Labs livestream on August 20

Explore Cosmos Edge on Jetson

Download Cosmos 3 checkpoints

Get the code on GitHub

Try Cosmos 3 Nano Reasoner and Cosmos 3 Nano

 Discuss (0)

 Like

## Tags

 Agentic AI / Generative AI | Edge Computing | Robotics | Simulation / Modeling / Design | General | Cosmos | Isaac Lab | Isaac Sim | Jetson | Intermediate Technical | Tutorial | featured | Physical AI | Robotics Simulation | Thor 

## 
 About the Authors

[img: Avatar photo https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/cropped-profile-201-131x131.webp]

[img: Avatar photo data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20131%20131%22%3E%3C/svg%3E]

 About Saeed Babamohamadi

 Saeed Babamohamadi is a technical marketing engineer at NVIDIA, focusing on physical AI and the application of world models in robotics. He holds a Ph.D. in mechanical engineering and robotics from Texas Tech University and an M.Sc. in computer science from the University of Tehran. He brings product management and developer relations experience to making world models practical and approachable for robotics developers.

 View all posts by Saeed Babamohamadi

## Comments