---
title: "Schritt 1: Kompatibilität prüfen"
linkTitle: "Kompatibilität prüfen"
weight: 10
description: >
  Prüfe, ob sich dein Mähroboter zu einem OpenMower umbauen lässt.
---
Prüfe vor dem ersten Kauf, ob dein Mäher mit OpenMower kompatibel ist.
Dieses Ablaufdiagramm hilft dir dabei:
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
    CheckList{"Steht der Mäher auf der<br/>Liste kompatibler Mäher?"}
    Compatible(["<b>Kompatibel</b><br/>Standardinstallation durchführen"])
    CheckEncoders{"Hat der Mäher<br/>Radencoder?"}
    Incompatible(["<b>Nicht kompatibel</b><br/>Zur Bestätigung auf Discord nachfragen"])
    CheckBattery{"Akkuspannung prüfen<br/>(Zellen in Reihe: 5S - 8S)"}
    CheckSpace{"Genügend Platz für<br/>das Universal-Mainboard?"}
    UniversalMainboard(["<b>Universal-Mainboard</b><br/>Hardware sieht geeignet aus"])
    AskDiscord(["<b>Kompatibilität unklar</b><br/>Auf Discord nachfragen"])

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
    
    CheckList -- Ja --> Compatible
    CheckList -- Nein --> CheckEncoders
    
    CheckEncoders -- Nein --> Incompatible
    CheckEncoders -- Ja --> CheckBattery
    
    %% Voltage Calculation: 
    %% 5S (5 * 3.6V = 18V) to 8S (8 * 4.2V = 33.6V)
    CheckBattery -- "Ja: 18.5V - 29.6V" --> CheckSpace
    CheckBattery -- "Nein: < 18.5V oder > 29.6V" --> AskDiscord

    CheckSpace -- Ja --> UniversalMainboard
    CheckSpace -- Nein --> AskDiscord
```



{{% alert title="Akkuspannung erklärt" color="info" %}}
Der Spannungsbereich **18,5 V bis 29,6 V** entspricht **5S- bis 8S-Lithium-Akkupacks**, ausgehend von der Nennspannung der Zellen (3,7 V pro Zelle):
- 5S: 5 × 3,7 V = 18,5 V Nennspannung
- 8S: 8 × 3,7 V = 29,6 V Nennspannung

Die Anzahl der in Reihe geschalteten Zellen findest du auf dem Akkuetikett oder in der Anleitung deines Mähers.
{{% /alert %}}

## Unterstützte Mähermodelle
Die [Übersicht kompatibler Mäher]({{% relref "/docs/knowledge-base/getting-started/compatible-mowers" %}}) listet Modelle von YardForce, SABO und John Deere auf. Sie enthält Fotos der Trägerplatinen und Anforderungen für Umbauten mit dem Universal-Board. Prüfe dein genaues Modell und die Platinenrevision, bevor du weitermachst.
