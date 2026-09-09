---
title: "Kompatible Mäher"
linkTitle: "Kompatible Mäher"
weight: 10
description: "Prüfe die Kompatibilität von YardForce, SABO MOWit 500F und John Deere Tango E5. Hier findest du passende Trägerplatinen und Voraussetzungen für eigene OpenMower-Umbauten."
---
## Yard Force
![OpenMower-V2 YardForce Trägerplatine]({{< relref "/docs/Knowledge-Base/getting-started/compatible-mowers" >}}/images/yf-mainboard.jpg)

**Hier geht es zum Git-Repository:** [https://github.com/xtech/hw-openmower-yardforce](https://github.com/xtech/hw-openmower-yardforce)

Das Projekt begann mit einem YardForce Classic 500(B). In dieser Dokumentation findest du bebilderte Anleitungen zum Zerlegen und Zusammenbauen. Aus Anwendersicht ist der YardForce Classic 500(B) der „am besten unterstützte“ Mäher.

**Es sind aber auch weitere Mäher von YardForce kompatibel:**

Theoretisch lässt sich bei jedem YardForce-Modell ab Baujahr 2019 mit innerem Chassis und äußerem Rahmen (SA-, SC-, LUV-, N- und NX-Reihe) das Original-Mainboard durch ein OpenMower-Mainboard ersetzen, da die Elektronik kompatibel ist.

{{% alert color="warning" %}}
Die YardForce-Modelle der Reihen Amiro, Compact, EasyMow, MowBest, XPower und MB sind derzeit (noch) nicht kompatibel.  
Der Hauptgrund ist, dass das OpenMower-Mainboard nicht in ihr Chassis passt.
{{% /alert %}}


## SABO / John Deere

Für **SABO MOWit 500F** (Serie I und II) und **John Deere Tango E5** (Serie I und II) gibt es ein eigenes Mainboard.

**Hier geht es zum Git-Repository:** [https://github.com/xtech/hw-openmower-sabo](https://github.com/xtech/hw-openmower-sabo)

Diese Trägerplatine ist mit folgenden Mähermodellen kompatibel:

- SABO MOWit 500F (Serie I und II)
- John Deere Tango E5 (Serie I und II)

|                                                      Trägerplatine Serie I (v0.2)                                                      |                                                     Trägerplatine Serie II (v0.2)                                                      |
| :------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------: |
| ![OpenMower-V2 SABO Trägerplatine Serie I v0.2]({{< relref "/docs/Knowledge-Base/getting-started/compatible-mowers" >}}/images/om-sabo-cb-s1-v02.jpg)  | ![OpenMower-V2 SABO Trägerplatine Serie II v0.1]({{< relref "/docs/Knowledge-Base/getting-started/compatible-mowers" >}}/images/om-sabo-cb-s2-v02.jpg) |
|                                               **Serie I (v0.1) @ John Deere Tango E5**                                                |                                                 **Serie II (v0.1) @ Sabo MOWiT 500F**                                                 |
| ![V0.1 Trägerplatine Serie I eingebaut]({{< relref "/docs/Knowledge-Base/getting-started/compatible-mowers" >}}/images/johndeere-s1-v01-assembled.jpg) |   ![V0.1 Trägerplatine Serie II eingebaut]({{< relref "/docs/Knowledge-Base/getting-started/compatible-mowers" >}}/images/sabo-s2-v01-assembled.jpg)   |

Diese Mäher werden **gut unterstützt**. Sogar die Displaysteuerung wurde durch eine voll funktionsfähige, moderne Benutzeroberfläche ersetzt!

<div style="padding-bottom: 2.5rem">
<video width="640" height="360" controls>
  <source src="https://www.shbe.net/openmower/sabo/Sabo_LCD_20251212.mp4" type="video/mp4">
  Dein Browser unterstützt die Videowiedergabe nicht.
</video>
</div>




## Universal-Board
Das Universal-Board enthält alles, was du für einen OpenMower-Umbau brauchst, etwa drei BLDC/DC-Motorcontroller, eine integrierte LiPo-Ladeelektronik sowie Anschlüsse für GPS und Sicherheitssensoren. Schraubklemmen erleichtern den Anschluss. Falls die Platine als Ganzes nicht hineinpasst, lässt sie sich in kleinere Module zerlegen.

**Hier geht es zum Git-Repository:** [https://github.com/xtech/hw-openmower-universal](https://github.com/xtech/hw-openmower-universal)

![v2-Universal-Board mit Modulen]({{< relref "/docs/Knowledge-Base/getting-started/compatible-mowers" >}}/images/BreakingTheBoard.jpg)


### Weitere kompatible Marken
Von den folgenden Marken sind Mäher bekannt, deren Hardware mit dem Universal-Mainboard kompatibel ist. Frag auf Discord nach, wenn du ein bestimmtes Modell prüfen möchtest. Die Chancen stehen gut, dass es funktioniert:

- **Husqvarna**: Die meisten Husqvarna-Mäher
- **Gardena**: Die meisten Gardena-Mäher
- **Fuxtec / Redback**: Mäher von Fuxtec und Redback


### Eigene Hardware
Wenn du ein eigenes Chassis hast, stehen die Chancen gut, dass du es mit dem Universal-Board betreiben kannst. Frag auf Discord nach Hilfe für deinen konkreten Aufbau.

