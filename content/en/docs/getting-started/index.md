---
title: "Getting Started"
linkTitle: "Getting Started"
weight: 10
description: >
  How to get started with the Open Mower project.
---

{{% toc %}}

## Quick Facts

- **Build time:** A weekend for a YardForce-class mower; longer for custom chassis
- **Estimated cost:** ~€700 (excluding the mower and RTK base station)
- **Skill level:** Intermediate electronics, Linux, and mechanical skills
- **Community:** 2k+ members on Discord ready to help with reviews and troubleshooting

New to the project? Start with the [Overview page]({{% relref "/docs/overview/" %}}).


## Important Warnings

{{% alert title="Read Before Starting" color="warning" %}}
- **Ongoing Development**: OpenMower is continuously evolving. Be prepared to troubleshoot and update software.
- **Lithium Battery Safety**: You will build your own charger. Understand the risks of working with lithium batteries.
- **Your Responsibility**: Ensure you understand each modification step before proceeding.
- **Read** the entire documentation and **gain a high-level overview**: Understand each step involved in the build before starting.
- **Evolving Documentation**: This documentation is continuously improved. If you find errors or have questions, **ask on Discord**.
  {{% /alert %}}


## Is Your Mower Compatible?

Before purchasing anything, verify your mower is compatible with the OpenMower project.

### Officially Supported Mowers

The following mowers are fully supported with dedicated carrier boards:

- **YardForce Classic 500(B)** - Most common, well-documented
- **Other YardForce Models (SA Series)**
- **SABO MOWit 500F** (Series-I & II)
- **John Deere Tango E5** (Series-I & II)
- Many other models using the universal carrier board
- If you want to build a mower from scratch, that's also possible

See the full [Compatible Mowers List]({{% relref "/docs/knowledge-base/compatible-mowers" %}}) for additional models and community builds.



## What You Need to Know

### Required Skills

- **Linux Basics**: Comfortable with terminal commands, basic file system navigation, and text editing
- **Raspberry Pi Experience**: Ability to set up and configure a Raspberry Pi
- **Electronics Knowledge**: Experience with PCBs, connectors, and basic electrical safety
- **Mechanical Skills**: Ability to disassemble and reassemble your mower

{{% alert title="Note" color="info" %}}
While the OpenMower app simplifies configuration, you may need to debug issues via SSH or adjust settings manually.
{{% /alert %}}


### What Parts You'll Need

The OpenMower project requires these main components:

#### 1. The Robot
A compatible lawn-mowing robot with its case and motors. You'll replace the electronics with OpenMower hardware.
Some people are building a custom mower chassis from scratch.

#### 2. OpenMower Hardware
{{% alert title="Hardware Version 2" color="success" %}}
OpenMower v2 hardware is now available and recommended for all new builds. v1 hardware is deprecated. See the [v2 Announcement]({{% relref "/updates" %}}) for details.

**To purchase v2 hardware:** Contact @Apehaenger on Discord.
{{% /alert %}}

Custom electronics consisting of:
- **Core Board**: Universal computing module with Raspberry Pi CM4, STM32 controller, IMU
- **Carrier Board**: Model-specific board (YardForce, SABO/John Deere, or Universal)
- **3x xESC Board**: Advanced motor controllers which can drive BLDC or DC motors and provide position feedback as well as closed-loop speed control


#### 3. RTK GPS System
RTK GPS enables centimeter-level accuracy by sending error corrections to the robot via Wi-Fi or radio.
Therefore, you will need one or two RTK GPS receivers:
- **Rover (required)**: GPS module mounted on the robot
- **Base Station (optional)**: Fixed GPS module providing correction data **OR** access to an external NTRIP service which provides the corrections via the internet. Some countries have free RTK services available.


## Build Overview

![Open Mower Build Overview](flow_chart.jpg)

Follow these steps in sequence:

## Ready to shop? 
**Check the detailed [Shopping List]({{% relref "/docs/knowledge-base/shopping-list" %}}).**


## Get Support

### Discord Community

Join our active Discord community for:
- Build guidance and troubleshooting
- Hardware availability updates
- Software tips and tricks
- Feature discussions

🔗 [Join OpenMower Discord](https://discord.gg/jE7QNaSxW7)

### Documentation & Resources

- **This Documentation**: Reviewed, official information
- **YouTube Channel**: Video tutorials and project updates

See the [Links]({{% relref "/docs/links" %}}) page for all resources.


## Next Steps

If you are ready to start building:

➡️ [Review the Shopping List]({{% relref "/docs/knowledge-base/shopping-list" %}})

➡️ [Check the Step by Step Guide]({{% relref "/docs/step-by-step/" %}})