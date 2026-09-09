---
title: "YardForce-Trägerplatine v1.0.0-beta bis v1.0.1-beta"
date: 2024-10-19
author: "Clemens Elflein"
description: "Erste Veröffentlichung der YardForce-v2-Trägerplatine, gefolgt von Verbesserungen an Effizienz und GPS-Stromversorgung."
---
Die YardForce-v2-Trägerplatine ist der Referenzentwurf für die OpenMower-v2-Hardwareplattform. Sie verbindet das universelle xCore-Board mit Motoren, Ladeschaltung und Sensoren des YardForce-Mähers. Dabei nutzt sie denselben SODIMM-Formfaktor und dieselben Anschlüsse wie die ursprüngliche Platine.

### v1.0.0-beta – 2024-10-07

Erste öffentliche Version des Entwurfs der YardForce-v2-Trägerplatine.

### v1.0.1-beta – 2024-10-19

- **Bias-Versorgung für den DC/DC-Wandler** – Eine zusätzliche Bias-Versorgung verbessert den Wirkungsgrad bei geringer Last.
- **F9P-Stromschalter** – Ein eigener Schalter für die Stromversorgung des Ardusimple-F9P-GPS-Moduls ermöglicht es, GPS unabhängig abzuschalten.
- **xCore-Bibliothek aktualisiert** – Die xCore-KiCad-Bibliothek wurde auf den neuesten Stand gebracht.

### Download

Die Fertigungsdateien (Gerber, Stückliste und Bestückungsdaten) für jede Version findest du auf der [Release-Seite](https://github.com/xtech/hw-openmower-yardforce/releases).
