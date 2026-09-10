---
title: "RTK-GPS-Navigation und Koordinatensystem"
linkTitle: "GPS / Koordinatensystem"
weight: 300
description: "So mäht OpenMower mit RTK-GPS ohne Begrenzungskabel. Erfahre mehr über Korrekturdaten, Empfangsvoraussetzungen und das lokale Koordinatensystem."
---
## Wie RTK-GPS das Begrenzungskabel ersetzt

RTK (Real-Time Kinematic) kombiniert Satellitenmessungen am Mäher mit Korrekturdaten einer festen Referenzstation oder eines NTRIP-Dienstes. Mit einem guten RTK-Fix kann OpenMower seine Position zentimetergenau bestimmen und die Mähflächen abfahren, die du in der App erfasst hast.

Die Karte legt Rasengrenzen, feste Hindernisse und Verbindungswege fest. Du musst diese [Flächen selbst erfassen]({{% relref "/docs/knowledge-base/operation/record-areas" %}}) und in deinem Garten testen.

### Empfang und Korrekturdaten

Der Mäher braucht zuverlässigen Satellitenempfang und fortlaufend Korrekturdaten. Gebäude und Bäume in der Nähe können den Empfang stören. Eine normale GPS-Position ohne RTK-Fix reicht für präzises Mähen nicht aus. Lies die [Anleitung zur GPS-Fehlersuche]({{% relref "/docs/troubleshooting/gps-rtk" %}}), wenn du die Eignung deines Gartens prüfst.

Du kannst eine [eigene Basisstation einrichten]({{% relref "/docs/knowledge-base/gps/rtk-base-setup" %}}) oder einen geeigneten Korrekturdienst nutzen. Berücksichtige Empfänger, Antenne, Datenverbindung und mögliche Gebühren des Korrekturdienstes bei deiner [Kostenplanung]({{% relref "/docs/knowledge-base/getting-started/shopping-list" %}}).

## Positionsbestimmung / Koordinatensystem

OpenMower bestimmt seine Position in einem lokalen 2D-Koordinatensystem. Die aktuelle Position des Roboters lässt sich damit durch die Koordinaten (X / Y) des VRP und seine aktuelle Ausrichtung beschreiben.

Den Ursprung des Koordinatensystems kannst du frei wählen oder auf die Basisstation legen. Bei einem externen Korrekturdienst musst du den Ursprung von Hand festlegen.

OpenMower verwendet ein rechtshändiges ENU-Koordinatensystem.
