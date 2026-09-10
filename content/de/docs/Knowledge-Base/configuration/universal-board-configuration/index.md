---
title: "Universal-Board konfigurieren"
linkTitle: "Universal-Board konfigurieren"
weight: 230
description: >-
  So richtest du das Universal-Board für eigene Mäher-Umbauten ein:
  Parameterübersicht, Vorlagendatei und Kalibrierung der Radencoder.
---
Diese Anleitung gilt für **eigene Mäher-Umbauten** mit dem OpenMower-Universal-Board. Bei solchen Aufbauten musst du mehrere hardwarespezifische Parameter selbst messen und einstellen, damit der Mäher korrekt funktioniert. Bei unterstützten Modellen sind diese bereits vorgegeben.

Alle individuellen Parameter gehören in `~/params/custom_params.yaml` auf dem Mäher.

{{% alert title="Nicht openmower configure ros verwenden" color="warning" %}}
`openmower configure ros` öffnet standardmäßig `mower_params.yaml`. Für eigene Umbauten ist das die **falsche Datei**. Bearbeite immer direkt `custom_params.yaml`:

```bash
nano ~/params/custom_params.yaml
```

Alle anderen `openmower`-Befehle, etwa `openmower configure env`, funktionieren wie gewohnt.
{{% /alert %}}

## Konfigurationsvorlage

Lade die Vorlage als Ausgangspunkt herunter und speichere sie auf dem Mäher unter `~/params/custom_params.yaml`:

**[custom_params.yaml herunterladen](custom_params.yaml)**

Die folgenden Abschnitte erklären alle mit `# TODO` markierten Parameter.

---

### Differentialantrieb

```yaml
ll:
  services:
    diff_drive:
      wheel_distance_m: 0.325
      ticks_per_m: 1600.0
```

| Parameter | Einzustellender Wert |
|---|---|
| `wheel_distance_m` | Abstand in Metern zwischen den Mitten des linken und rechten Antriebsrads. Mit einem Maßband messen. |
| `ticks_per_m` | Encoderimpulse pro gefahrenem Meter. Muss gemessen werden; siehe [Radencoder kalibrieren](#calibrating-wheel-ticks) weiter unten. |

---

### IMU-Ausrichtung

```yaml
    imu:
      axis_config: "+X-Y-Z"
```

| Parameter | Einzustellender Wert |
|---|---|
| `axis_config` | Ausrichtung des Mainboards relativ zum Mäher-Chassis. `+X-Y-Z` passt bei flacher, waagerechter Montage mit der X-Achse der Platine nach vorne. Passe den Wert an, wenn dein Mainboard schräg oder gedreht eingebaut ist. |

---

### Akkuspannungen

```yaml
    power:
      battery_full_voltage: 20.0
      battery_empty_voltage: 18.5
      battery_critical_voltage: 16.5
      battery_critical_high_voltage: 21.0
      charge_critical_high_voltage: 30.0
      charge_critical_high_current: 1.5
```

Lies die Spannungsangaben deines Akkupacks nach und trage die passenden Werte ein.

| Parameter | Einzustellender Wert |
|---|---|
| `battery_full_voltage` | Spannung des vollständig geladenen Akkupacks laut Spezifikation. |
| `battery_empty_voltage` | Spannung, bei der der Mäher zur Ladestation zurückkehrt. |
| `battery_critical_voltage` | Notabschaltung bei Unterspannung. Unterhalb der Rückkehrschwelle (`battery_empty_voltage`) einstellen, aber so hoch, dass keine schädliche Tiefentladung eintritt. |
| `battery_critical_high_voltage` | Überspannungsschutz. Etwas oberhalb der Spannung bei voller Ladung einstellen. |
| `charge_critical_high_voltage` | Höchste zulässige Ausgangsspannung des Ladegeräts. |
| `charge_critical_high_current` | Höchster zulässiger Ladestrom in Ampere. |

---

### GPS-Antennenversatz

```yaml
xbot_positioning:
  antenna_offset_x: 0.3
  antenna_offset_y: 0.0
```

Die Positionsbestimmung muss wissen, wo die GPS-Antenne relativ zum **Drehmittelpunkt** des Mähers sitzt, also zur Mitte zwischen den beiden Antriebsrädern.

| Parameter | Einzustellender Wert |
|---|---|
| `antenna_offset_x` | Versatz nach vorne/hinten in Metern. Positiv bedeutet: Antenne vor dem Drehmittelpunkt. Von der Mitte zwischen den Rädern bis zur Antenne messen. |
| `antenna_offset_y` | Versatz nach links/rechts in Metern. Positiv bedeutet: Antenne links. Bei mittig montierter Antenne normalerweise 0. |

---

### GPS-Kartenursprung

```yaml
    gps:
      datum_lat: 53.457452
      datum_long: 10.014737
```

Diese Werte sind in der Vorlage nicht mit `TODO` markiert. **Du musst sie trotzdem ändern.** Trage Koordinaten nahe deiner Ladestation ein. Dieser Punkt wird zum Ursprung der Mäherkarte. Die Koordinaten kannst du mit einem GPS- oder Kartenwerkzeug ermitteln.

---

### NTRIP-Zugangsdaten

```yaml
ntrip_client:
  host: "www.your-ntrip-caster.de"
  port: 2101
  username: "ntripuser"
  password: "ntrippass"
  mountpoint: "ntripmount"
```

Trage die Zugangsdaten deines RTK-Korrekturdienstes ein.

---

### Sicherheitssensoren

Bevor du den Mähmotor aktivierst, konfiguriere und prüfe alle Sicherheitssensoren: Hebeerkennung, Neigungserkennung und Stopptasten. Das erfolgt über die GPIO-Eingabekonfiguration. Die vollständige Anleitung findest du unter [GPIO-Eingänge konfigurieren]({{< relref "/docs/Knowledge-Base/configuration/configure-gpio-inputs" >}}).

### Mähmotor aktivieren

```yaml
mower_logic:
  enable_mower: false
```

Setze den Wert erst auf `true`, wenn alle Sicherheitssensoren angeschlossen und konfiguriert sind und ihre korrekte Funktion geprüft wurde. Der Betrieb ohne funktionierende Sicherheitssensoren ist unsicher.

---

## Radencoder kalibrieren {#calibrating-wheel-ticks}

Mit diesem Verfahren ermittelst du `ticks_per_m` für die Radencoder deines Mähers.

### Voraussetzungen

- OpenMower läuft
- Zugriff per SSH oder Webterminal
- Eine ebene Fläche mit etwa 10 m freier, gerader Strecke
- Etwas zum Markieren von Start- und Endposition, etwa Klebeband oder Kreide

### Schritt 1: Aufzeichnungsmodus aktivieren

Öffne die OpenMower-App und aktiviere den **Modus zur Flächenerfassung**. So sind Fahrmotoren und Radencoder aktiv und veröffentlichen Odometriedaten.

### Schritt 2: Anfangswerte der Encoderzähler notieren {#schritt-2-anfangswerte-des-tachos-notieren}

Öffne die ROS-Shell:

```bash
openmower shell
```

Abonniere das Status-Topic des linken ESC und notiere den Wert von `tacho`:

```bash
rostopic echo /ll/diff_drive/left_esc_status
```

Schreibe den Wert auf und drücke <kbd>Strg</kbd>+<kbd>C</kbd>. Wiederhole das für das rechte Rad:

```bash
rostopic echo /ll/diff_drive/right_esc_status
```

### Schritt 3: Zehn Meter geradeaus fahren

Markiere die aktuelle Position des Mähers und fahre genau **10 Meter** geradeaus. Fahre langsam und gleichmäßig. Je gerader die Strecke, desto genauer das Ergebnis.

### Schritt 4: Endwerte der Encoderzähler notieren {#schritt-4-endwerte-des-tachos-notieren}

Abonniere beide Topics erneut und notiere die neuen `tacho`-Werte:

```bash
rostopic echo /ll/diff_drive/left_esc_status
```

```bash
rostopic echo /ll/diff_drive/right_esc_status
```

### Schritt 5: ticks_per_m berechnen

Berechne die Differenz für jedes Rad. Ist sie negativ, ändere das Vorzeichen:

```
left_diff  = |tacho_end_left  - tacho_start_left|
right_diff = |tacho_end_right - tacho_start_right|
```

Die beiden Werte sollten ungefähr gleich sein. Bilde den Mittelwert und teile ihn durch 10:

```
ticks_per_m = (left_diff + right_diff) / (2 * 10)
```

### Schritt 6: Wert übernehmen

Bearbeite `custom_params.yaml` direkt:

```bash
nano ~/params/custom_params.yaml
```

Trage den berechneten Wert ein:

```yaml
ll:
  services:
    diff_drive:
      ticks_per_m: <your_value>
```

Speichere die Datei und starte OpenMower neu, um den Wert zu übernehmen.

{{% alert title="Tipp" color="info" %}}
Wiederhole die Messung zwei- oder dreimal und bilde den Mittelwert, um die Genauigkeit zu verbessern. Kleine Abweichungen von der geraden Linie beeinflussen die einzelnen Messwerte.
{{% /alert %}}
