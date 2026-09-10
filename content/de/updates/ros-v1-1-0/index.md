---
title: "OpenMower ROS v1.1.0"
date: 2025-12-07
author: "Clemens Elflein"
description: "Kartenformat auf JSON umgestellt, Fehler mit ungemähten Streifen behoben, JSON-RPC über MQTT, SVG-Kartenansicht, Switch-Pro-Controller-Unterstützung und vieles mehr."
---
[v1.1.0](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.1.0) bringt eine nicht rückwärtskompatible Änderung des Kartenformats, die Korrektur eines seit Langem bestehenden Planerfehlers und zahlreiche neue Funktionen.

### Kartenformat auf JSON umgestellt

Die Karte wird jetzt als `map.json` statt als `map.bag` gespeichert. Beim ersten Start nach dem Update wird deine vorhandene `map.bag` **automatisch konvertiert**. Du musst nichts von Hand tun. Danach wird nur noch `map.json` gelesen und aktualisiert.

Das MQTT-Kartenformat wurde an die interne Darstellung angepasst. Falls die Karte nach dem Update in der Weboberfläche nicht richtig erscheint, lade die Seite mit Strg+F5 vollständig neu oder leere den Browser-Cache.

### Keine ungemähten Streifen mehr zwischen den Bahnen {#ungemähte-streifen-behoben}

Ein seit Langem bekannter Fehler, bei dem zwischen den Bahnen schmale Grasstreifen stehen blieben, ist behoben. Ursache war ein falscher Parameter im Flächenplaner. Falls du die Schnittbreite vorübergehend kleiner als den tatsächlichen Messerdurchmesser eingestellt hattest, um den Fehler zu umgehen, kannst du nun wieder den korrekten Wert verwenden.

### Neue Funktionen

- **JSON-RPC 2.0 über MQTT** – Der Mäher stellt eine JSON-RPC-2.0-Schnittstelle über MQTT bereit. Jeder MQTT-Client kann ihn darüber gezielt abfragen und fernsteuern.
- **Unterstützte Funktionen über MQTT abrufen** – Der Mäher veröffentlicht zur Laufzeit, welche Funktionen er unterstützt. Angebundene Systeme können diese Informationen abfragen, statt von einem fest vorgegebenen Funktionsumfang auszugehen.
- **Karte als SVG anzeigen** – Ein neues Werkzeug wandelt die Mähkarte in eine SVG-Datei um. So kannst du sie auch ohne Verbindung zum Mäher ansehen und nach Fehlern untersuchen.
- **Flächen- oder Randmähen je Fläche überspringen** – Für einzelne Flächen lässt sich einstellen, ob das Mähen der Innenfläche, der Randbahnen oder beides ausgelassen wird.
- **Switch-Pro- und Shield-Controller unterstützt** – Zwei weitere Gamepads können zur manuellen Steuerung verwendet werden.
- **Regenerkennung über MQTT** – Das Flag `rain_detected` ist jetzt im MQTT-Topic `robot_state/json` enthalten.
- **ROS-Knoten automatisch neu starten** – Abgestürzte Knoten werden nach zehn Sekunden automatisch neu gestartet. Das erhöht die Zuverlässigkeit.
- **Wartezeiten beim An- und Abdocken einstellbar** – Verzögerungen vor und nach den Manövern lassen sich über Umgebungsvariablen konfigurieren.
- **An- und Abdocken abbrechen** – Laufende An- und Abdockmanöver können jetzt abgebrochen werden.
- **Snapshot-Aufzeichnung** – Für die Fehlersuche lassen sich Momentaufnahmen der zuletzt empfangenen ROS-Nachrichten aufzeichnen.
- **Web-App aktualisiert**.

### Wichtige Fehlerbehebungen

- Hindernisse außerhalb der Mähfläche werden bei der Flächenplanung nicht mehr berücksichtigt.
- Simulator für Karten ohne Ladestation repariert.
- GPS-Protokollauswahl bei v1-Hardware an das Verhalten der v2-Hardware angeglichen.
- Mehrere Topic-Namen korrigiert.

### Interne Änderungen und Infrastruktur

- Verarbeitung von Umgebungsvariablen umfassend überarbeitet.
- GPS-Treiber in den Namensraum `ll/services/gps` verschoben.
- Docker-Build und CI-Workflows aktualisiert.
- `spdlog`-Ausgabe in das ROS-Logging umgeleitet.
- Lizenz auf **GPLv3** umgestellt.

**Vollständige Änderungsliste:** [v1.0.2 → v1.1.0](https://github.com/ClemensElflein/open_mower_ros/compare/v1.0.2...v1.1.0)
