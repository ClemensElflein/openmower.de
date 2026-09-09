---
title: "ROS-Parameter verwalten"
linkTitle: "ROS-Parameter konfigurieren"
weight: 400
description: "So zeigst du ROS-Parameter in OpenMower an und überschreibst sie über Shell und Konfigurationsdateien, um das System gezielt anzupassen."
---
## ROS-Parameter anzeigen und einstellen

OpenMower basiert auf ROS. Ein großer Teil seines Verhaltens wird deshalb über Parameter gesteuert. Wenn du diese Parameter prüfen und ändern kannst, lässt sich der Betrieb deines Mähers gezielt anpassen.

### Alle Parameter auflisten

Öffne die OpenMower-Shell, um alle aktuell aktiven ROS-Parameter anzusehen:

```bash
openmower shell
```

Führe dann aus:

```bash
rosparam list
```

Damit erhältst du eine vollständige Liste der aktuell geladenen Parameter. Das ist ein guter erster Schritt bei der Fehlersuche oder wenn du die Konfiguration deines Mähers verstehen möchtest.

### Parameter überschreiben

Alle Parameter lassen sich über die Konfigurationsdatei `mower_params.yaml` anpassen. Sie ist die zentrale Stelle, um Standardwerte zu überschreiben.

Am einfachsten bearbeitest du sie mit:

```bash
openmower configure ros

```

### Beispiel

In diesem Beispiel überschreiben wir den Geschwindigkeitsparameter.

#### 1. Aktuellen Parameterwert abfragen

Wenn du mit `rosparam list` einen Parameter gefunden hast, kannst du seinen Wert mit `rosparam get <parameter>` abfragen:

```bash
🚜 openmower@openmower-v2:~$ rosparam get /move_base_flex/FTCPlanner/speed_fast
0.4
```

Die Mähgeschwindigkeit beträgt hier aktuell 0,4 m/s.

#### 2. Wert in deiner Konfiguration ändern

Rufe auf dem Hostsystem `openmower configure ros` auf und übertrage den Parameternamen in YAML. Jedes `/` entspricht dabei einer zusätzlichen Einrückung um zwei Leerzeichen.

Für unser Beispiel sieht das so aus:

```yaml
move_base_flex:
  FTCPlanner:
    speed_fast: 0.5
```

#### 3. Datei speichern und neuen Wert prüfen

Nach dem Speichern startet ROS automatisch neu. Prüfe anschließend, ob der neue Wert übernommen wurde:

```bash
🚜 openmower@openmower-v2:~$ rosparam get /move_base_flex/FTCPlanner/speed_fast
0.5
```

:tada: Fertig!

### Wenn es Probleme gibt

Wird ein Parameter nicht korrekt überschrieben, stelle sicher, dass du die neueste OpenMower-Version verwendest. Wenn es weiterhin nicht funktioniert, frag auf Discord nach.
