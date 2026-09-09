---
title: "OpenMower: Das v2-Hardware-Update"
date: 2025-06-07
author: "Clemens Elflein"
description: "Die modulare, mäherunabhängige v2-Hardwareplattform ist da: drei Trägerplatinen-Entwürfe, neu geschriebene Firmware und vollständig offene Software."
---
Seit dem letzten ausführlichen OpenMower-Update ist eine Weile vergangen – tatsächlich drei Jahre. Damals war das Projekt kaum mehr als ein Prototyp. Keine Kits, keine ausgereifte Bedienung, nur ein paar gelötete Platinen und Befehle im Terminal.

Inzwischen hat sich OpenMower deutlich weiterentwickelt.

### **Was wir gemeinsam erreicht haben**

Am Anfang mussten Nutzer ihre Mäher von Grund auf umbauen und oft die gesamte Platine von Hand löten. Schon um den Mäher überhaupt zum Mähen zu bringen, musste man sich mit Terminalbefehlen beschäftigen. Von Plug-and-play war das weit entfernt.

Die Community ist drangeblieben, und gemeinsam haben wir viel geschafft:

- ✅ **Fertige Hardware-Kits** sind erhältlich.
- ✅ **Bessere Dokumentation** erleichtert den Einstieg erheblich.
- ✅ Ein **einsatzbereites Betriebssystem-Image** lädt die aktuelle Software über Docker. Danke an [@DocGalaxyBlock](https://github.com/docgalaxyblock)!
- ✅ Eine **eigene App** ermöglicht es, Mähflächen einzulernen, Aufträge zu starten und den Fortschritt zu verfolgen.
- ✅ Die **Software läuft deutlich stabiler.**
- ✅ Es gibt sogar eine **Home-Assistant-Integration** aus der Community!

<br>

* * *

### **Die OpenMower-v2-Hardware ist da**

##### **Warum wir neue Hardware brauchen**

Trotz aller Fortschritte hat die bisherige OpenMower-Hardware eine große Einschränkung: **Sie funktioniert nur mit YardForce-Mähern.**
Andere Hardware einzusetzen ist derzeit sehr aufwendig und wurde deshalb nur bei wenigen Eigenbauten umgesetzt. So war OpenMower eigentlich nicht gedacht.

Das wollten wir ändern – mit einer **modularen Hardwareplattform, die unabhängig vom Mähermodell ist**.

##### **Das neue Hardwarekonzept**

Über ein Jahr lang habe ich die Hardware von Grund auf neu entworfen, um OpenMower weiterzubringen. Die neue Architektur teilt die Hardware in zwei Teile:

- **Ein universelles Core-Board**
- **Einfache, modellspezifische Trägerplatinen**

Das **Core-Board** ist die zentrale Recheneinheit. Es enthält:

- Raspberry Pi Compute Module 4 oder alternative Module mit ähnlichem Formfaktor
- Leistungsfähigen STM32-Mikrocontroller mit 550 MHz
- Gigabit-Ethernet-Switch
- Integrierte IMU
- Flash-Speicher für die Konfiguration
- SODIMM-Steckverbinder für einfache Integration und Montage

Dieses Core-Board bleibt bei allen Mähern gleich.

Die **Trägerplatinen** sind dagegen auf das jeweilige Mähermodell zugeschnitten. Sie übernehmen:

- Stromversorgung
- LiPo-Ladeschaltung mit Konfiguration und Überwachung per Software
- Motortreiber
- Physische Anschlüsse
- EEPROM, damit das Core-Board den Mäher, auf dem die Software läuft, automatisch erkennen kann
- Außerdem sind ein I2S-Soundchip, eine 12-V-Versorgung und ein Anschluss für eigene Erweiterungen vorhanden

Die Trägerplatinen sollen möglichst einfach bleiben, damit sie sich leicht an neue Mäher anpassen lassen.

#### **YardForce-v2-Platine**

Die YardForce-v2-Platine ähnelt in ihrer Form der bisherigen v1-Platine und hat dieselben Anschlüsse.
Dazu kommen ein integrierter Soundchip, weitere Not-Aus-Anschlüsse, zusätzliche Ethernet-Ports, ein Anschluss für UM9XX-GPS-Platinen, eine per Software schaltbare 12-V-Versorgung für eigene Erweiterungen und der Erweiterungsanschluss.

![YardForce-Mainboard](YardForceModules.jpg)

#### **SABO-/John-Deere-Platine**

Das SABO-Mainboard – tolle Arbeit von [@Apehaenger](https://github.com/Apehaenger) – bietet dieselben Funktionen wie die YardForce-v2-Platine und funktioniert mit diesen Mähern:

- SABO MOWit 500F (Serie I und II)
- John Deere Tango E5 (Serie I und II)

![SABO-Mainboard](SABO_Mainboard.jpg)

#### **Universal-Board**

Das Universal-Board ist etwas Besonderes. Es ist für viele Roboterplattformen ausgelegt. Die Stromversorgung erfolgt über Schraubklemmen oder XT30-Stecker.
Motoranschlüsse können direkt angelötet oder ebenfalls über Schraubklemmen verbunden werden.

Für GPS gibt es drei Möglichkeiten: das Ardusimple-F9P-Arduino-Board, Ardusimple micro oder UM9XX GPS.

Die Besonderheit: Passt die Platine nicht in deinen Mäher, kannst du sie in Module zerlegen, wie auf dem Bild zu sehen. Diese lassen sich im Mäher verteilen und über Strom- und Datenkabel wieder verbinden. Aktuell verwenden wir SATA für die Datenverbindungen. In der nächsten Version sollen andere Steckverbinder zum Einsatz kommen.

![Universal-Board in einzelne Module zerlegen](BreakingTheBoard.jpg)

### **Firmware: Von Grund auf neu geschrieben**

Die neue Firmware ist vollständig quelloffen und GPL-lizenziert. Sie läuft auf ChibiOS, dem Echtzeitbetriebssystem, das auch die xESC-Motorcontroller verwenden.
Der STM32-Mikrocontroller übernimmt jetzt mehr Aufgaben. Deshalb wurde die Firmware komplett neu geschrieben.

Die wichtigsten Eigenschaften:

- **Eine einzige Binärdatei für alle Mäher!** Die Firmware erkennt die eingebaute Mäherhardware beim Einschalten automatisch und richtet sich entsprechend ein.
- Kommunikation zwischen STM32 und Pi über **Ethernet** für mehr Geschwindigkeit und Flexibilität bei der Entwicklung.
- **Ausfallsicheres Verhalten**: Not-Aus und Ladeschaltungen arbeiten unabhängig von der ROS-Software.
- Das Compute Module kann im Leerlauf ausgeschaltet werden, um Energie zu sparen.

Vielen Dank an [@rovo89](https://github.com/rovo89) für die Unterstützung bei der Firmware!

### **Was bereits verfügbar ist**

Es gibt bereits **drei Trägerplatinen-Entwürfe**:

- ✅ **YardForce** – der Referenzentwurf, der mehr bietet als die bisherige Hardware
- ✅ **John Deere / SABO** – vielen Dank an [@Apehaenger](https://github.com/Apehaenger)!
- ✅ **Universal-Board** – mit vielen weiteren Modellen kompatibel

Eine kleine **Beta-Testrunde** haben wir ebenfalls abgeschlossen, mit guten Ergebnissen. Einige Umbauten laufen seit Monaten ohne Probleme.

<br>

📬 **Wenn du an der Hardware interessiert bist, schreib Apehaenger auf Discord eine Direktnachricht!**

<br>

* * *

### **Wie es mit OpenMower weitergeht**

Wir sind noch nicht fertig. Das steht als Nächstes an:

- 🚀 **Umstieg auf ROS2** – ROS1 hat sein Supportende erreicht
- 📅 **Visuelle Zeitplanung**
- 🧠 **Hindernisvermeidung**
- 🛠️ **Allgemeine Verbesserungen der Bedienbarkeit**

An vielen dieser Themen arbeitet die Community bereits. Es ist spannend zu sehen, wie aus dem praktischen Einsatz neue Funktionen entstehen.

### **Mach mit!**

##### **v2-Hardware bekommen**

Ich würde mich freuen, wenn viele die v2-Hardware ausprobieren und testen. Deshalb werde ich bald eine begrenzte Stückzahl anbieten.
Möchtest du die v2-Hardware testen oder sogar an der Entwicklung mitarbeiten? Bei der v2-Dokumentation helfen? Oder einfach zu den Ersten gehören, die die neue Hardware ausprobieren?

In jedem Fall gilt:
📬 **Schreib Apehaenger auf Discord eine Direktnachricht!**

##### **Das Projekt unterstützen**

Wenn du das Projekt finanziell unterstützen und mir mehr Zeit für OpenMower ermöglichen möchtest, schau auf meinem [Patreon](https://www.patreon.com/ClemensElflein) vorbei. Jeder Beitrag hilft, und ich freue mich sehr über die Unterstützung.
Danke fürs Lesen – bis zum nächsten Update!

<br>

### **Fragen**

#### Funktioniert mein v1-Mäher dann nicht mehr?
Doch. Die Software bleibt mit der bisherigen Hardware kompatibel.

#### Wird das neue Kit teurer als das bisherige?
Das neue Kit kostet fast genauso viel wie das bisherige, obwohl es mehr kann.

#### Brauche ich die neue Hardware, um die OpenMower-Software zu verwenden?
Nein. Es gibt eine klar definierte Schnittstelle zur unteren Kommunikationsebene. Eigene Umbauten mit per Reverse Engineering erschlossener Originalhardware oder anderer eigener Hardware sind weiterhin möglich.
