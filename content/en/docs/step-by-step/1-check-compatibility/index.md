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
{{< include-markdown file="/docs/Knowledge-Base/compatible-mowers/index.md" >}}
