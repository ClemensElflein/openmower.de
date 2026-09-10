---
title: "Versatz der GPS-Antenne einstellen"
linkTitle: "Antennenversatz einstellen"
weight: 410
description: "Stelle den Abstand zwischen GPS-Antenne und Mitte der Radachse ein, damit OpenMower seine Position korrekt berechnet."
---
## Überblick

OpenMower erfasst seine Position über die GPS-Antenne. Sitzt die Antenne nicht genau in der Mitte der Radachse, weicht die berechnete Mäherposition um diesen Abstand ab. Mit dem Antennenversatz gleichst du das aus.

## Koordinatensystem

Der Versatz wird im lokalen Koordinatensystem des Mähers angegeben:

- **Ursprung**: Mitte der Radachse, also zwischen den beiden Antriebsrädern
- **X-Achse**: zeigt nach vorne
- **Y-Achse**: zeigt nach links
- **Z-Achse**: zeigt nach oben (rechtshändiges Koordinatensystem)

| Richtung | Vorzeichen |
|---|---|
| Vorne | X positiv |
| Hinten | X negativ |
| Links | Y positiv |
| Rechts | Y negativ |

**Beispiele:**

- Antenne 10 cm vor und 5 cm rechts von der Mitte der Radachse → `antenna_offset_x: 0.1`, `antenna_offset_y: -0.05`
- Antenne 5 cm links von der Mitte der Radachse → `antenna_offset_x: 0.0`, `antenna_offset_y: 0.05`

## Konfiguration

Öffne die ROS-Parameterdatei:

```bash
openmower configure ros
```

Füge am Ende der Datei den folgenden Abschnitt ein und passe die Werte an die tatsächliche Position deiner Antenne an:

```yaml
xbot_positioning:
  antenna_offset_x: 0.05
  antenna_offset_y: -0.15
```

Die Werte werden in **Metern** angegeben.

Speichere die Datei. ROS startet automatisch neu und übernimmt den eingestellten Versatz.
