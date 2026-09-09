---
title: "OpenMower ROS v1.1.1"
date: 2026-03-16
author: "Clemens Elflein"
description: "Korrekturversion: Inaktive Flächen überspringen, chronologische Echtzeit-Logs, Parameter über MQTT und Filter für Meta-RPC-Anfragen."
---
[v1.1.1](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.1.1) ist eine gezielte Korrekturversion auf Basis von v1.1.0.

### Was ist neu?

**Inaktive Mähflächen überspringen** – Der Mäher überspringt jetzt korrekt Flächen, die als inaktiv markiert sind. Flächen, die du nur vorübergehend deaktivieren möchtest, musst du damit nicht mehr löschen und neu erfassen. Danke an [@rovo89](https://github.com/rovo89).

**Parameter über MQTT veröffentlichen** – Die Konfigurationsparameter des Mähers werden jetzt über MQTT veröffentlicht. Externe Werkzeuge und Hausautomationssysteme können die aktuelle Konfiguration damit leichter auslesen und einbinden. Danke an [@rovo89](https://github.com/rovo89).

**Meta-RPC-Anfragen ignorieren** – JSON-RPC-Metaanfragen werden nun korrekt herausgefiltert, statt als unbekannte Befehle behandelt zu werden. Danke an [@rovo89](https://github.com/rovo89).

**Reihenfolge der Echtzeit-Logs korrigiert** – Eine Korrektur am Echtzeit-Logging stellt sicher, dass Meldungen in der richtigen zeitlichen Reihenfolge ausgegeben werden. Danke an [@Apehaenger](https://github.com/Apehaenger).

**Vollständige Änderungsliste:** [v1.1.0 → v1.1.1](https://github.com/ClemensElflein/open_mower_ros/compare/v1.1.0...v1.1.1)
