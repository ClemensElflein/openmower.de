---
title: "OpenMower ROS v1.0.1: Edge-Versionen"
date: 2024-07-24
author: "Clemens Elflein"
description: "Drei Vorabversionen zwischen v1.0.0 und v1.0.2 mit verbessertem Andocken, NTRIP-Korrektur, YardForce-Rev4-Unterstützung und weiteren Änderungen."
---
Zwischen v1.0.0 und v1.0.2 erschienen drei Edge-Vorabversionen. Hier findest du die Änderungen jeder Version im Überblick.

### v1.0.1-edge.2 – 2024-07-24

- **Erneutes Andocken nach Wegrollen** – Rollt der Mäher von der Ladestation weg, versucht er jetzt erneut anzudocken, statt aufzugeben. Danke an [@jeremysalwen](https://github.com/jeremysalwen).
- **NTRIP-IP-Sperre behoben** – Ein Fehler wurde korrigiert, durch den der NTRIP-Client eine Sperre deiner IP-Adresse bei öffentlichen Castern auslösen konnte. Danke an [@EtheriVR](https://github.com/EtheriVR).
- **Anzahl der Andockversuche einstellbar** – `docking_retry_count` lässt sich jetzt über eine Umgebungsvariable ändern. Danke an [@gytisgreitai](https://github.com/gytisgreitai).
- **Aktuelle Mähfläche veröffentlichen** – Die aktive Mähfläche wird nun sowohl über ROS als auch über MQTT veröffentlicht. Danke an [@11phc](https://github.com/11phc).
- **YardForce-Rev4-Adapterplatine unterstützt** – Unterstützung für die Rev4-Variante der Adapterplatine ergänzt.
- **Fehlerbehebungen** – Beim Löschen eines Navigationspunkts wird die Karte nicht mehr unnötig neu aufgebaut. Der simulierte Zeitstempel von `mower/status` wird korrekt gesetzt. Bei Verlust des GPS-Fix startet und stoppt der Mähmotor nicht mehr ständig.

### v1.0.1-edge.1 – 2024-07-02

- **Besseres Andocken** – Optionale Verzögerung nach der Spannungserkennung beim Andocken; der Grund jedes Andockvorgangs wird protokolliert.
- **Not-Aus-Zustand über die App zurücksetzen** – Die OpenMower-App kann den Not-Aus-Zustand jetzt aus der Ferne zurücksetzen.
- **Konfiguration als JSON Schema** – Die Mäherkonfiguration wird jetzt durch ein JSON Schema beschrieben. Das erleichtert Validierung und passende Werkzeuge.
- **Entwicklungsumgebung in Docker** – Eine vollständig containerisierte Entwicklungsumgebung wurde ergänzt.

### v1.0.1-edge.0 – 2024-05-31

- **Zuverlässigeres Andocken** – Kurze Spannungseinbrüche durch Stromspitzen beim Mähen werden jetzt toleriert, ohne eine Rückkehr zur Ladestation auszulösen.
- **Vorzeichen bei NMEA-GPS korrigiert** – Falsches Vorzeichen im Bewegungsvektor bei NMEA-GPS-Geräten behoben.
- **Slic3r-Absturz behoben** – Speicherzugriffsfehler im Flächenplaner korrigiert.
- **Randbahnen korrigiert** – Das Verbinden von Randbahnen bei Inseln in der Karte wurde repariert.
