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
Use this flowchart to check compatibility:
```mermaid
%%{init: {
  "flowchart": {
    "nodeSpacing": 15,
    "diagramPadding": 3
  },
  "themeVariables": {
    "fontSize": "12px"
  }
}}%%

flowchart LR
    %% Nodes
    Start([Start])
    CheckList{"Is the mower in the<br/>Compatible Mowers List?"}
    Compatible(["<b>Compatible</b><br/>Proceed with standard install"])
    CheckEncoders{"Does the mower have<br/>Wheel Encoders?"}
    Incompatible(["<b>Incompatible</b><br/>Ask on Discord for confirmation"])
    CheckBattery{"Check Battery Voltage<br/>(Series count 5S - 8S)"}
    CheckSpace{"Enough space for<br/>Universal Mainboard?"}
    UniversalMainboard(["<b>Universal Mainboard</b><br/>Hardware looks good"])
    AskDiscord(["<b>Unknown Compatibility</b><br/>Ask on Discord"])

    %% Classes
    classDef decision fill:#FFF,stroke:#666,stroke-width:2px,color:#333;

    %% Assign class to decision nodes
    class CheckList,CheckEncoders,CheckBattery,CheckSpace decision;
    
    %% Styles
    style Start fill:#93c0f0,stroke:#333,stroke-width:2px,color:#333
    style Compatible fill:#256d33,stroke:#333,stroke-width:2px,color:#fcfcfc
    style UniversalMainboard fill:#256d33,stroke:#333,stroke-width:2px,color:#fcfcfc
    style Incompatible fill:#a63a41,stroke:#333,stroke-width:2px,color:#fcfcfc
    style AskDiscord fill:#e19e20,stroke:#333,stroke-width:2px,color:#fcfcfc

    %% Logic Connections
    Start --> CheckList
    
    CheckList -- Yes --> Compatible
    CheckList -- No --> CheckEncoders
    
    CheckEncoders -- No --> Incompatible
    CheckEncoders -- Yes --> CheckBattery
    
    %% Voltage Calculation: 
    %% 5S (5 * 3.6V = 18V) to 8S (8 * 4.2V = 33.6V)
    CheckBattery -- "Yes: 18.5V - 29.6V" --> CheckSpace
    CheckBattery -- "No: < 18.5V or > 29.6V" --> AskDiscord

    CheckSpace -- Yes --> UniversalMainboard
    CheckSpace -- No --> AskDiscord
```



{{% alert title="Battery Voltage Explained" color="info" %}}
The voltage range **18.5V - 29.6V** corresponds to **5S-8S lithium battery packs** based on nominal cell voltage (3.7V per cell):
- 5S: 5 × 3.7V = 18.5V nominal
- 8S: 8 × 3.7V = 29.6V nominal

Check your mower's battery label or manual to determine the series count.
{{% /alert %}}

### Officially Supported Mowers

The following mowers are fully supported with dedicated carrier boards:

- **YardForce Classic 500(B)** - Most common, well-documented
- **Other YardForce Models (SA Series)**
- **SABO MOWit 500F** (Series-I & II)
- **John Deere Tango E5** (Series-I & II)

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

#### 2. OpenMower Hardware v2
Custom electronics consisting of:
- **Core Board**: Universal computing module with Raspberry Pi CM4, STM32 controller, IMU
- **Carrier Board**: Model-specific board (YardForce, SABO/John Deere, or Universal)

{{% alert title="Hardware Version 2" color="success" %}}
OpenMower v2 hardware is now available and recommended for all new builds. v1 hardware is deprecated. See the [v2 Announcement]({{% relref "/updates" %}}) for details.

**To purchase v2 hardware:** Contact @Apehaenger on Discord.
{{% /alert %}}

#### 3. RTK GPS System
RTK GPS enables centimeter-level accuracy by sending error corrections to the robot via Wi-Fi or radio.
Therefore, you will need one or two RTK GPS receivers:
- **Rover (required)**: GPS module mounted on the robot
- **Base Station (optional)**: Fixed GPS module providing correction data OR access to an NTRIP service. Some countries have free RTK services available.


#### **Ready to shop?** Check the detailed [Shopping List]({{% relref "/docs/knowledge-base/shopping-list" %}}).


## Build Overview

![Open Mower Build Overview](flow_chart.jpg)

Follow these steps in sequence:


# TODO: Fill this section



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
- **OpenMower Wiki**: Community-contributed guides and tips
- **YouTube Channel**: Video tutorials and project updates

See the [Links]({{% relref "/docs/links" %}}) page for all resources.


## Next Steps

If you have a compatible mower and are ready to start building:

➡️ [Review the Shopping List]({{% relref "/docs/knowledge-base/shopping-list" %}})

➡️ [Check the Conversion Guide]({{% relref "/docs/Conversion-Guide/" %}})