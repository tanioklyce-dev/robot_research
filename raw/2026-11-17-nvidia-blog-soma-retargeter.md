# Capture: https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/
Captured 2026-11-17 via curl; visible text of the page's <article> element from the title to the author bio (navigation, date line, comments and related posts trimmed; images and GIFs not captured). Reached from an NVIDIA Robotics Facebook video (https://fb.watch/KYOMuecQOe/, posted 2026-11-17, 9 s, no captions) whose caption links here via nvda.ws/3Xg9uxn. Page metadata: published 2026-11-13. Key link targets:
  repository -> https://github.com/NVIDIA/soma-retargeter (v0.2.0)
  SOMA-X -> https://github.com/NVlabs/SOMA-X
  BONES-SEED -> https://huggingface.co/datasets/bones-studio/seed
  GEM-X -> https://github.com/NVlabs/GEM-X ; Kimodo -> https://github.com/nv-tlabs/kimodo ; ARDY -> https://github.com/nv-tlabs/ardy
  SONIC SOMA converter -> https://github.com/NVlabs/GR00T-WholeBodyControl/blob/main/gear_sonic/data_process/convert_soma_csv_to_motion_lib.py
  ProtoMotions -> https://github.com/NVlabs/ProtoMotions ; MotionBricks paper -> https://arxiv.org/html/2604.24833v1#S7.SS4


# Adapt Human Motion for Robots with NVIDIA SOMA Retargeter

By John Malaska

Like

Discuss (0)

- L

- T

- F

- R

- E

## AI-Generated Summary

- NVIDIA SOMA Retargeter adapts human motion data to the proportions and joint structure of specific humanoid robots using the shared SOMA skeleton representation.
- The retargeting pipeline scales motion targets to the robot, solves inverse kinematics with Newton built on NVIDIA Warp, and applies post-processing corrections such as foot-plant adjustment.
- Developers can source human motion from motion-capture datasets like BONES-SEED, video reconstruction with GEM-X, or generative models such as Kimodo and ARDY that output on the SOMA skeleton.
- The v0.2 release provides reference configurations and retargeted motion examples for five humanoid robots including Unitree G1, Unitree H2, Booster T1, AgiBot X2 Ultra, and AgiBot A3T3.
- Tools such as the Robot Configurator and IK weight optimizer help align reference poses, map skeletons, and tune inverse-kinematics priorities for smoother robot motion.
- Retargeted trajectories export as CSV files and convert into motion-library formats for policy training workflows like SONIC and ProtoMotions, enabling simulation evaluation of balance, contact, and tracking accuracy.
### Next Steps
- Explore the SOMA Retargeter repository for installation instructions, reference configurations, and interactive examples.
- Follow the Robot Configurator guide to add a new humanoid embodiment or refine an existing configuration.
- Review the batch-retargeting guide to process motion collections for a target robot without the viewer.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. Learn more

Human motion offers roboticists a great starting point for teaching humanoid robots how to move. A human demonstration captures the coordination and timing behind natural movement, from everyday actions to complex tasks. But a robot cannot simply copy the same joint motion from a human. Its proportions, joint structure, and range of motion are different, so the movement needs to be adapted to fit the robot.

The open source NVIDIA SOMA Retargeter helps you adapt human motion to your robot’s proportions and range of motion. Built around the shared human-motion representation in NVIDIA SOMA-X, it provides tools to configure your robot, refine the resulting movement, and process motion data for downstream training.

This post explains the retargeting process, the tools for refining robot motion, and the connection to policy learning.

## From human motion to robot joint trajectories

Human motion can come from many sources, including a motion capture session, a video, an online dataset, or a generative model. These sources often output motion with different skeletons and file formats. Representing compatible human motion on the SOMA skeleton gives the retargeter a consistent input.

SOMA Retargeter reads a Biovision Hierarchy (BVH) animation on the SOMA base skeleton. As Figure 1 below shows, it scales motion targets to the robot’s proportions, solves for joint poses, and applies configured corrections. The output is a comma-separated values (CSV) file containing the robot’s root position, orientation, and joint angles for each frame. These trajectories describe the desired movement for a downstream learning or control system.

Figure 1. The retargeting pipeline converts SOMA BVH motion into robot joint trajectories through scaling, inverse kinematics, and post-processing. Across many clips, the resulting animations can form a motion library for downstream reference preparation and policy training.

## Sources of human motion

Developers can draw on recorded performances, reconstruct motion from video, or generate new movements:

- Motion-capture data. BONES-SEED provides a collection of human motion-capture data.

- Video reconstruction. GEM-X reconstructs whole-body 3D human motion from a single video using the SOMA body model. Its demo workflow connects video reconstruction with G1 retargeting, showing how a recorded action can become a robot motion reference.

- Motion generation. Kimodo and ARDY let developers generate human movement from text and pose constraints. Kimodo supports creating motion sequences from those descriptions, while ARDY adds interactive steering as the motion unfolds. Both offer models that generate motion on the SOMA skeleton.

## Adapting motion to different humanoid robots

The SOMA Retargeter v0.2 release includes sample motions supplied by Bones from the BONES-SEED dataset, along with reference retargeting results and configurations for five humanoid robots: Unitree G1, Unitree H2, Booster T1, AgiBot X2 Ultra, and AgiBot A3T3. These examples show how joint angles and foot placement change across humanoid embodiments according to their specific proportions and range of motion. The paired human motions and robot results give you a starting point for exploring the tool and comparing your own output.

For this example, use the supplied Unitree G1 configuration to retarget a forward walk from the sample motions. After installing SOMA Retargeter, open a terminal in the repository root and start the viewer:

uv run python app/bvh_to_csv_converter.py --config assets/default_bvh_to_csv_converter_config.json --viewer gl

The BVH to CSV Converter opens with unitree_g1 selected by default. In Scene Options, expand Motion, select Load on the BVH Motion row, and open the bundled file from here. The SOMA human animation appears in the viewer.

Under Scene Options → Motion, select Retarget on the BVH Motion row. The retargeter scales the source targets to G1, solves the configured inverse-kinematics objectives for each frame, and applies the configured post-processing. The viewer then displays the robot animation with the human source motion. Positioning gizmos let you separate them for inspection.

Figure 2. The BVH to CSV Converter displays the human source motion alongside the retargeted Unitree G1 motion, with controls for loading, retargeting, and saving the result.

Use the playback controls to inspect the result. A recognizable forward walk and continuous motion are useful first checks; the robot’s poses will differ from the human’s because its proportions and joints are different. Under CSV Motion, select Save and give the output a new name, such as my_first_retarget.csv, to keep it separate from the supplied reference. The saved file contains the robot’s root pose and joint values over the animation.

To compare your output with the supplied G1 reference result for this walk, use the CSV Motion Load control to open each CSV in turn and inspect the same point in the motion. The reference file is located in the repository here. The results should show the same general movement, though exact values can vary with configuration and dependency versions. The first-retarget guide covers this example in more detail.

## Configuring your robot and refining its motion

The supplied G1 configuration gives you a starting point for retargeting, while the included reference result provides a point of comparison as you adjust the settings to refine the motion. With the Robot Configurator, you can refine an existing robot configuration or create one for a new robot by loading its robot description and defining how human motion maps to it.

You can align human and robot reference poses, adjust scale, and map the source skeleton to robot body parts. The resulting configuration can be saved and reused across motion clips.

Figure 3. The source motion is a one-handed wave, but an unaligned reference pose makes Booster T1 hold both arms outward (left). After aligning the robot’s reference pose with the SOMA human reference, one hand waves beside its head while the other arm rests at its side (right). Both panels use the same input motion and IK settings, isolating the effect of reference-pose alignment.

The retargeting solver uses inverse kinematics (IK) from Newton, built with NVIDIA Warp, to find joint poses that follow the scaled human targets. When a robot cannot match every target at once, IK weights determine which body parts take priority.

The experimental IK weight optimizer tunes these weights using a small set of motions representative of the robot’s intended tasks. It tests weight adjustments by retargeting those motions and checking how closely and smoothly the robot follows the targets. The selected weights are saved in a new retargeting configuration.

Sliding feet can introduce conflicting targets for a downstream motion-tracking policy: the reference foot moves while the intended action calls for planted contact. Foot-plant correction addresses this artifact by adjusting foot motion during detected contact intervals. You can refine contact timing and correction settings to reduce sliding in the reference motion before it enters a training pipeline.

Once you have refined a configuration on representative motions, headless batch retargeting lets you reuse it across a larger collection for your target robot, without operating the viewer for each clip.

## Using retargeted motion to train robot policies

During training, a motion-tracking policy learns how to turn the retargeted reference into control actions, using both the desired motion and the robot’s current state.

The SONIC training workflow includes a SOMA CSV converter for G1. It converts retargeted trajectories into SONIC’s motion-library format for training. ProtoMotions offers another framework for physics-based motion tracking. In either case, the input representation and policy need to match the target robot.

Simulation provides the next stage of evaluation, where a trained policy can be assessed for balance, ground contact, actuator limits, and tracking accuracy.

In a separate experiment with MicroDuck, human motion from Bones was adapted for the robot and used to train a controller for each clip in physics simulation.

The three-panel comparison in Figure 4 below shows the human performance, the MicroDuck reference, and the trained controller executing the motion in simulation. The reference shows the intended movement, while the simulation shows how closely the trained controller follows it.

Figure 4. Experimental adaptation of human motion for MicroDuck and training of a motion-tracking controller. Left: SOMA Human Motion. Middle: SOMA Retargeting. Right: Trained controller in Isaac Lab and Newton.

For more on simulation setup and policy training with MicroDuck, see the NVIDIA Technical Blog Using AI Agents to Teach Robots Like Microduck to Walk in Simulation and a Hugging Face post from NVIDIA called Train in Simulation, Deploy on a Real Robot: Microduck with Isaac Lab 3.0.

## Generating motion in real time with MotionBricks

You can also generate motion with MotionBricks’ SOMA human model and use SOMA Retargeter to adapt it to your robot, expanding the motion references available for downstream training.

The MotionBricks G1 model was trained in part on BONES-SEED motions adapted to G1 with SOMA Retargeter. It generates continuous whole-body motion directly for G1 between changing target poses in real time.

Figure 5. MotionBricks generates continuous motion for a SOMA human and Unitree G1 robot in the reference demos, with recent motion and target poses shown alongside each character.

The MotionBricks paper and project video demonstrate this approach on a physical Unitree G1. A G1-specific MotionBricks model supplies the motion targets, and SONIC controls their execution.

## Get started with SOMA Retargeter

The SOMA Retargeter repository includes installation instructions, reference configurations, and examples for interactive and batch retargeting. The Robot Configurator guide explains how to add a humanoid embodiment, and the batch-retargeting guide covers processing motion collections for that robot.

Louis Marcoux contributed to the work in this blog.

Discuss (0)

Like

## Tags

Robotics | Simulation / Modeling / Design | General | Isaac Lab | Intermediate Technical | Tutorial | Newton | NVIDIA Research | Physical AI | Reinforcement Learning | Robotics Simulation | Warp

##
About the Authors

About John Malaska

John Malaska is a senior product manager at NVIDIA, working on motion generation and retargeting for robotics and animation. He led the open-source release of MotionBricks and supports SOMA Retargeter. John enjoys connecting animation craft with robotics, helping bring human movement to humanoid robots. He holds a bachelor of fine arts from Pratt Institute.

[
View all posts by John Malaska
