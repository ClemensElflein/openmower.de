---
title: "Step 1: Check Compatibility"
linkTitle: "Check Compatibility"
weight: 10
description: >
  Check if your robotic mower can be converted to an Open Mower.
---

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

flowchart TD
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

# Officially Supported Mowers

## Yard Force
![OpenMower-V2 YardForce Carrierboard](yf-mainboard.jpg)

**Check out the Git Repo Here:** [https://github.com/xtech/hw-openmower-yardforce](https://github.com/xtech/hw-openmower-yardforce)

The project got started on a YardForce Classic 500(B), and there are photo guides in this documentation on how to disassemble and reassemble it. From a user's perspective, the YardForce Classic 500(B) is the "best supported" mower. 

**However, there are more mowers from the YardForce brand that are compatible:**

In theory, every YardForce model with the Core + Outer Frame Chassis (SA, SC, LUV, N and NX Line) that has a production year of 2019+ has compatible electronics to replace the stock mainboard with an OpenMower one.

{{% alert color="warning" %}}
As of today the YardForce Amiro, Compact, EasyMow, MowBest, XPower and MB series models are not (yet) compatible.  
The main reason is that the OpenMower mainboard does not fit in their chassis.
{{% /alert %}}


## SABO / John Deere

There is a dedicated mainboard for **SABO MOWit 500F** (Series-I & II) and **John Deere Tango E5** (Series-I & II) mowers.

**Check out the Git Repo Here:** [https://github.com/xtech/hw-openmower-sabo](https://github.com/xtech/hw-openmower-sabo)

This Carrierboard is compatible with the following mower models:

- SABO MOWit 500F (Series-I & II)
- John Deere Tango E5 (Series-I & II)

|                          Series-I Carrierboard (v0.2)                          |                         Series-II Carrierboard (v0.2)                          |
| :----------------------------------------------------------------------------: | :----------------------------------------------------------------------------: |
| ![OpenMower-V2 SABO Carrierboard Series-I v0.2](om-sabo-cb-s1-v02.jpg)  | ![OpenMower-V2 SABO Carrierboard Series-II v0.1](om-sabo-cb-s2-v02.jpg) |
|                   **Series-I (v0.1) @ John Deere Tango E5**                    |                     **Series-II (v0.1) @ Sabo MOWiT 500F**                     |
| ![V0.1 Carrierboard Series-I assembled](johndeere-s1-v01-assembled.jpg) |   ![V0.1 Carrierboard Series-II assembled](sabo-s2-v01-assembled.jpg)   |

These mowers are **well supported**. Even the display controller was replaced by a fully functional, modern user interface!

<div style="padding-bottom: 2.5rem">
<video width="640" height="360" controls>
  <source src="sabo-gui.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
</div>




## Universal Board
The universal board contains all features needed for an Open Mower build (e.g., three BLDC/DC motor controllers, a LiPo charger on board, connectors for GPS, emergency sensors, etc.). It has screw terminals for easy connections and can be broken into smaller modules if it doesn't fit as a whole board.

**Check out the Git Repo Here:** [https://github.com/xtech/hw-openmower-universal](https://github.com/xtech/hw-openmower-universal)

![V2 Universal Board with Modules](BreakingTheBoard.jpg)


### Other Compatible Brands
The following mower brands are known to have compatible hardware with the Universal mainboard. If you want to check your specific model, ask on Discord. The probability is high that it will work:

- **Husqvarna**: Most Husqvarna mowers
- **Gardena**: Most Gardena mowers  
- **Fuxtec / Redback**: Fuxtec and Redback mowers


### Custom Hardware
If you have a custom chassis, there is a good chance you can get it to work with the Universal board. Ask on Discord for guidance on your specific setup.

