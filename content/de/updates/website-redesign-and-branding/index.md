---
title: "Neues Website-Design und OpenMower-Designsystem"
date: 2026-03-21
author: "Clemens Elflein"
description: "Die Dokumentationswebsite wurde von Grund auf neu gestaltet. Außerdem haben wir das erste offizielle OpenMower-Designsystem veröffentlicht."
---
Die Dokumentation auf openmower.de hat ein komplett neues Erscheinungsbild bekommen. Gleichzeitig veröffentlichen wir das erste offizielle **OpenMower-Designsystem**.

### **Was sich auf der Website geändert hat**

Die Website verwendet jetzt ein eigens angepasstes Theme, das direkt auf den OpenMower-Design-Tokens aufbaut: lokal bereitgestellte Schriften DM Sans und DM Mono, eine einheitliche Farbpalette aus Grün auf dunklem Hintergrund und eine Startseite, die klar zeigt, was das Projekt ist: eine GPL-lizenzierte Plattform auf Basis von ROS und RTOS, die die geschlossene, herstellerkontrollierte Firmware von Mährobotern ersetzt. Ohne Herstellerbindung und ohne undurchsichtige Blackbox.

### **Das OpenMower-Designsystem**

Mit [`design-openmower-branding`](https://github.com/ClemensElflein/OpenMower) haben wir jetzt ein versioniertes Designsystem, das dem Projekt auf jeder Plattform einen einheitlichen Auftritt gibt:

- **Farbpalette** – Primärgrün `#1B9D52`, dunkle Graphitflächen und bernsteinfarbene Code-Akzente
- **Typografie** – DM Sans Variable und DM Mono in allen Schriftstärken
- **Komponentenbibliothek** – Buttons, Karten, Hinweise, Tabellen und Eingabefelder, alle auf Tokens aufgebaut und dokumentiert
- **Logodateien** – Vollständiger Schriftzug als SVG und quadratische Bildmarke, nutzbar für Kopfzeilen, Favicons und Marketing
- **Maschinenlesbare Tokens** – `tokens.json` als zentrale Quelle, dazu eine für KI optimierte Token-Datei und ein Theme-Factory-JSON für Claude Code

Das Theme wird als **Material-UI-v6-Theme** bereitgestellt und lässt sich direkt in React/MUI-Projekte einbinden. Die Design-Tokens sind formatunabhängig. Zuordnungen für Tailwind und CSS Custom Properties sind ebenfalls enthalten.

**Live-Demo →** [https://xtech.github.io/design-openmower-branding/](https://xtech.github.io/design-openmower-branding/)

Die Markenelemente stehen unter CC BY-NC-SA 4.0, der Theme-Code unter MIT.
