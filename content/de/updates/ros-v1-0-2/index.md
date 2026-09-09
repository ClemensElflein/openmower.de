---
title: "OpenMower ROS v1.0.2"
date: 2025-06-17
author: "Clemens Elflein"
description: "GPS über TCP, Regenerkennung, schräges Abdocken, Drehzahlüberwachung und Sensorschwellen, Hintergrundton, Vorbereitungen für v2-Hardware und zahlreiche Korrekturen."
---
[v1.0.2](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.0.2) ist eine umfangreiche Version mit neuen Funktionen und Beiträgen aus der gesamten Community.

### Die wichtigsten Neuerungen

**GPS über TCP** – Der GPS-Treiber kann sich jetzt über TCP mit einer GPS-Quelle verbinden. Das erleichtert den Einsatz von GPS-Empfängern im Netzwerk und weitergeleiteten GPS-Daten. Danke an [@rovo89](https://github.com/rovo89).

**Regenerkennung** – Der Mäher reagiert jetzt auf Regen: Er unterbricht das Mähen und wartet die über `OM_RAIN_DELAY_MINUTES` eingestellte Zeit ab, bevor er weitermacht. Danke an [@olliewalsh](https://github.com/olliewalsh).

**Schräges Abdocken** – Der Mäher kann jetzt in einem Winkel abdocken. Das verbessert die Zuverlässigkeit bei Ladestationen, an denen gerades Rückwärtsfahren Probleme macht. Danke an [@AndreKR](https://github.com/AndreKR).

**Drehzahlüberwachung und Sensorschwellen** – Motordrehzahlen und einstellbare Sensorschwellen wurden ergänzt. Auch die Übermittlung der Sensordaten wurde verbessert. Danke an [@Apehaenger](https://github.com/Apehaenger).

**Hintergrundton** – Es gibt jetzt eine Option zum Abspielen von Hintergrundgeräuschen. Danke an [@Apehaenger](https://github.com/Apehaenger).

**Manuelle Steuerung bei der Flächenerfassung** – Der Mäher lässt sich nun auch im Modus zur Flächenerfassung manuell fahren. Danke an [@olliewalsh](https://github.com/olliewalsh).

**Automatische Punkterfassung umschalten** – Während einer Aufzeichnung kann die Punkterfassung ein- und ausgeschaltet werden. Danke an [@rovo89](https://github.com/rovo89).

**Mehr als zehn Andockversuche einstellbar** – Die Zahl der Andockversuche ist nicht mehr auf zehn begrenzt. Danke an [@jeremysalwen](https://github.com/jeremysalwen).

**Umgebungsvariable OM_NO_COMMS** – Eine neue Umgebungsvariable deaktiviert den Kommunikationsknoten vollständig. Das ist nützlich, wenn die Software ohne angeschlossene Hardware der unteren Ebene laufen soll. Danke an [@jeremysalwen](https://github.com/jeremysalwen).

**Größere Abstände zwischen Mähbahnen** – Der slic3r-Flächenplaner unterstützt jetzt weiter auseinanderliegende Bahnen und damit weniger dichte Mähmuster. Danke an [@ClemensElflein](https://github.com/ClemensElflein).

**IMU-Achsenzuordnung für v2-Hardware** – Die korrekte Ausrichtung der IMU-Achsen für das v2-Mainboard wurde ergänzt. Danke an [@Apehaenger](https://github.com/Apehaenger).

### Vorbereitungen für v2-Hardware

Diese Version enthält erste Grundlagen für die v2-Hardwareschnittstelle, eine überarbeitete Kommunikation mit dem Mäher, ein vergrößertes Format der Konfigurationspakete und eine `InputService`-Schnittstelle. Deren erste Version wurde für weitere Arbeiten wieder zurückgenommen; die Infrastruktur ist aber vorhanden.

### Wichtige Fehlerbehebungen

- GPS-Header-Erkennung für das UBX-Protokoll korrigiert.
- Absturz des Planers bei bestimmten Sonderfällen der Kartengeometrie behoben.
- Ständiges Starten und Stoppen des Mähmotors bei Verlust des GPS-Fix behoben.
- Speicherzugriffsfehler in slic3r korrigiert.
- Verbinden von Randbahnen bei vorhandenen Inseln repariert.
- NTRIP-Client aktualisiert, um IP-Sperren durch RTK2GO zu verhindern.
- Gleichmäßigeres Abdocken.

### Interne Änderungen

- Parametersystem umfassend überarbeitet.
- UART-Zuordnung für neuere Kernel-Versionen aktualisiert.
- Vorschau auf die Anhaltestrecke im FTC-Planer deaktiviert, sobald `speed_fast_threshold` überschritten wird.
- `spdlog` in das ROS-Logging umgeleitet.
- Unterstützung für native arm64-CI-Runner.
- Lizenz auf **GPLv3** umgestellt.

**Vollständige Änderungsliste:** [v1.0.1-edge.2 → v1.0.2](https://github.com/ClemensElflein/open_mower_ros/compare/v1.0.1-edge.2...v1.0.2)
