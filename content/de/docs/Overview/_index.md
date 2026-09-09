---
title: "Überblick"
linkTitle: "Überblick"
weight: 1
description: "So rüstest du Mähroboter mit OpenMower auf RTK-GPS-Navigation um: App-Einblicke, unterstützte Hardware, Smart-Home-Anbindung und Informationen zum Umbau."
carousel:
  - image: open_mower_app_1.jpg
  - image: open_mower_app_2.jpg
  - image: homeassistant_dashboard.png
  - image: smarthome_tracker.png
---
### Warum es OpenMower gibt

**OpenMower** ist ein Open-Source-Projekt, das handelsübliche Mähroboter in zuverlässige, RTK-gesteuerte Mäher verwandelt. Aus einem Garagenprototyp ist eine von der Community gepflegte Plattform mit wiederverwendbarer Elektronik, Software und Dokumentation geworden.

Das ursprüngliche Vorstellungsvideo gibt dir einen schnellen Einblick in das Konzept:

<a href="https://www.youtube.com/watch?v=BSF04i3zNGw" target="_blank"><img src="https://user-images.githubusercontent.com/2864655/161540069-f4263fa7-a47b-49d2-a7bc-d1cdc3a47704.jpg" alt="Vorschaubild des OpenMower-Videos" /></a>



### Was OpenMower bietet

- **Navigation ohne Begrenzungskabel:** Die präzise Positionsbestimmung mit RTK-GPS ersetzt das Begrenzungskabel und ermöglicht mehrere Mähzonen.
- **Moderne App:** Über die Weboberfläche kannst du OpenMower am Computer oder Smartphone einrichten, Mähzeiten planen und den Mäher manuell steuern.
- **Smart-Home-Anbindung:** Die native Home-Assistant-Integration stellt Live-Daten zu Akku, Motoren und Sensoren bereit. Damit kannst du zum Beispiel automatisch bei Regen pausieren.
- **Von der Community erprobte Elektronik:** Die modulare v2-Hardware kombiniert ein Core-Board auf CM4- und STM32-Basis mit Trägerplatinen für verbreitete Mäher-Chassis.
- **Offen und anpassbar:** Die Quelltexte von Firmware, App und ROS-Software sind offen zugänglich. Du kannst sie nachvollziehen, anpassen und eigene Beiträge einreichen.
- **Sicherheit im Blick:** Eigene Not-Aus-Schleifen und Watchdogs sichern Mähwerk und Antrieb ab.

{{< carousel height="500" unit="px" items="4" duration="3000" >}}


### Unterstützte Hardware

OpenMower ersetzt die Originalelektronik in kompatiblen Chassis. Zu den häufig umgebauten Modellen gehören:

- YardForce Classic 500(B) und SA-Serie
- SABO MOWit 500F (Serie I und II)
- John Deere Tango E5 (Serie I und II)

Du bist unsicher, ob dein Mäher geeignet ist? Schau zuerst in die Liste der [kompatiblen Mäher]({{% relref "/docs/knowledge-base/getting-started/compatible-mowers" %}}) und frag bei offenen Fragen vor dem Hardwarekauf auf Discord nach. Mit der universellen Trägerplatine können erfahrene Bastler auch weitere Modelle umrüsten, sofern die Grundvoraussetzungen erfüllt sind: Radencoder, eine unterstützte Spannung und genügend Platz für das Mainboard.

---

### So geht es weiter

- [Erste Schritte]({{% relref "/docs/getting-started" %}}): Benötigte Kenntnisse, Ablaufdiagramm zur Kompatibilität und der gesamte Umbau im Überblick.
- [Kompatible Mäher]({{% relref "/docs/knowledge-base/getting-started/compatible-mowers" %}}): Prüfe vor dem Hardwarekauf, ob dein Chassis geeignet ist.
- [Einkaufsliste]({{% relref "/docs/knowledge-base/getting-started/shopping-list" %}}): Ausführliche Teileliste einschließlich RTK-Komponenten.
- [Links]({{% relref "/docs/links" %}}): GitHub-Repositories, Discord-Einladung, Videos und weitere Anlaufstellen.


### Roadmap

Dank der Beiträge aus der Community entwickelt sich OpenMower ständig weiter. Aktuelle Themen sind unter anderem:

- Hindernisse erkennen und umfahren
- Bessere Zeitplanung und Abläufe für mehrere Mähflächen
- Weitere Trägerplatinen und Zubehör für neue Mäher-Chassis
- Zusätzliche Werkzeuge zur Kartenbearbeitung und Diagnose

Wenn du mithelfen möchtest, komm auf unseren Discord-Server, melde Probleme oder steuere Dokumentation und Code bei.
