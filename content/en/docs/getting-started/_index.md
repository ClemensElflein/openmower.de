---
title: "Getting Started"
linkTitle: "Getting Started"
weight: 10
description: >
  How to get started with the Open Mower project.
---

## Important Info

{{% alert title="Read Before Starting" color="warning" %}}
- **Ongoing Development**: The OpenMower project is under continuous development. Be prepared to invest time and effort to get the robot fully operational. While the project is robust, you may encounter bugs or potential issues along the way.
- **DO NOT** use the stock charger with the OpenMower mainboard!
- **Lithium Batteries can be dangerous:** You will be building your own charger. Ensure you are comfortable with this process and understand the associated risks.
- **Read** the entire documentation and **gain a high-level overview**: Understand each step involved in the build before starting.
- **You are responsible for your own actions**: Make sure you know what you're doing!
- **Evolving Documentation**: This documentation is continuously being improved. There may be errors or missing steps. If you have questions, **ask on Discord**.
  {{% /alert %}}


## Prerequisites

Read this section thoroughly to understand _which_ components you will need for the Open Mower project and _why_ you need them. This will prevent unnecessary expenses and ensure you are well-prepared.


### Required Knowledge

- **Linux**: You should be comfortable using a Linux PC and know how to set up a Raspberry Pi. While the Open Mower app is available, you may need to adjust settings and debug issues.
- **Electronics**: You should have experience handling PCBs and soldering. Ensure you understand each step you will perform.


### Required Parts

The Open Mower project involves several key components:
- **The Robot**: A modified lawn-mowing robot. You will use the case and motors from an off-the-shelf robot and replace the electronics with custom components. You can either purchase the custom electronics or solder the parts yourself.
- **RTK GPS**: Precision is achieved with RTK GPS, which uses two receivers: one on the robot and one fixed base station. The base station sends error correction data to the robot, enabling centimeter accuracy. This can be done using Wi-Fi or another long-range radio. Note: Some cloud services offer RTK error corrections, both free and paid.
- **Docking Station**: The robot needs a docking station to recharge. Since the original docking station lacks the necessary charging electronics, you will replace the internal electronics. **Do not use the stock docking station with the modified robot.**

Ready to start? Check out the [Shopping List]({{% relref "/docs/knowledge-base/shopping-list" %}}).


## Compatibility Check

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

## Build Steps

![Open Mower Build Overview](flow_chart.jpg)

Follow these steps in order to build your OpenMower:
- First, modify the robot following the [Robot Assembly]({{% relref "/docs/robot-assembly" %}}) steps. Avoid leaving the mower powered on too long, as **you cannot charge it using the unmodified docking station**.
- Next, modify the docking station using the [Docking Station Assembly]({{% relref "/docs/docking-station-assembly" %}}) guide. **You will then be able to charge the battery with the new docking station.**
- Set up the software. This step connects the robot to your Wi-Fi, downloads the OpenMower software, and involves general configuration. Ensure the docking station assembly is complete before starting this step to avoid battery drain.
- Finally, with the software running, use the Open Mower App to record your mowing and navigation areas, and start mowing.

If you have the parts and are ready to assemble the robot, read the [Robot Assembly]({{% relref "/docs/robot-assembly" %}}) documentation.
