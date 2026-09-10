---
title: "OpenMower ROS v1.2.0"
date: 2026-05-13
author: "Clemens Elflein"
description: "Einstellungen pro Mähfläche, ausführlichere Akkudaten, verbesserte Not-Aus-Behandlung für v2-Hardware, korrigierte Hindernisreihenfolge und Simulator-Verbesserungen."
---
[v1.2.0](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.2.0) bringt individuelle Einstellungen je Mähfläche, mehrere Verbesserungen für v2-Hardware und Korrekturen für einen zuverlässigeren Betrieb.

### Eigene Einstellungen für einzelne Mähflächen {#einstellungen-pro-mähfläche-überschreiben}

Der Wechsel von `map.bag` zu `map.json` in v1.1.0 hat flexible, rückwärtskompatible Erweiterungen der Karte ermöglicht. Diese Möglichkeit nutzen wir jetzt für individuelle Flächeneinstellungen: Einzelne Mähflächen können eigene Werte für `outline_count`, `outline_overlap_count`, `outline_offset` und `angle` enthalten.

Die ersten drei Werte überschreiben die globalen Vorgaben nur für die jeweilige Fläche. `angle` ersetzt die automatische Ausrichtungserkennung, die auf den ersten zwei Metern der Umrandung basiert, durch einen festen Winkel. Das hilft bei Flächen, für die die Automatik regelmäßig die falsche Richtung auswählt.

Diese Attribute müssen vorerst von Hand mit einem Texteditor in `map.json` eingetragen werden. Unterstützung in der [OpenMower-App](https://github.com/xtech/openmower-app) ist geplant. Danke an [@jrv](https://github.com/jrv) und [@rovo89](https://github.com/rovo89).

### Verbesserungen für v2-Hardware

Mehrere Änderungen betreffen speziell die v2-Hardware:

- **Eingabedienst und Not-Aus-Behandlung** – Ein neuer Eingabedienst ersetzt den bisherigen Ansatz. Not-Aus-Zustände werden detaillierter erfasst und behandelt. Danke an [@rovo89](https://github.com/rovo89).
- **High-Level-Dienst** – Ein neuer High-Level-Dienst bündelt die Steuerungslogik für v2-Platinen. Danke an [@Apehaenger](https://github.com/Apehaenger).
- **Ausführlichere Akkudaten** – Der Akkuzustand wird genauer gemeldet. Dadurch lassen sich Ladezustand und Alterungszustand des Akkus besser beurteilen. Danke an [@Apehaenger](https://github.com/Apehaenger), mit weiteren Beiträgen von [@ClemensElflein](https://github.com/ClemensElflein).

### Benutzerdefinierte Parameter haben immer Vorrang {#nutzerparameter-haben-immer-vorrang}

Die Ladereihenfolge der Parameter wurde korrigiert. Benutzerdefinierte Parameter werden jetzt zuletzt geladen und überschreiben immer die mitgelieferten Standardwerte. Zuvor konnten bestimmte Standardwerte unbemerkt die eigenen Einstellungen überschreiben. ([@ClemensElflein](https://github.com/ClemensElflein))

### Reihenfolge der Hindernisflächen korrigiert

Hindernisflächen werden jetzt unabhängig von ihrer Reihenfolge in der Karte berücksichtigt. Zuvor konnte eine Besonderheit der Flächenverarbeitung dazu führen, dass später definierte Hindernisse bei der Flächenplanung ignoriert wurden. Danke an [@olliewalsh](https://github.com/olliewalsh).

### Zuverlässigkeit und Entwicklung

- **Schutz vor Deadlocks in xbot_monitoring** – Das Überwachungssystem ist jetzt gegen Deadlocks abgesichert, durch die es unbemerkt hängen bleiben konnte. Danke an [@rovo89](https://github.com/rovo89).
- **Ungepufferte Logs** – Logmeldungen werden sofort statt gepuffert geschrieben. Beim Mitlesen erscheinen sie dadurch in Echtzeit. Danke an [@Apehaenger](https://github.com/Apehaenger).
- **Simulator-Korrekturen** – Mehrere Fehler im Simulator wurden behoben. Danke an [@olliewalsh](https://github.com/olliewalsh) und [@rovo89](https://github.com/rovo89).

**Vollständige Änderungsliste:** [v1.1.1 → v1.2.0](https://github.com/ClemensElflein/open_mower_ros/compare/v1.1.1...v1.2.0)
