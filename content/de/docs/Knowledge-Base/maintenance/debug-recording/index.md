---
title: "Diagnoseaufzeichnung erstellen"
linkTitle: "Diagnoseaufzeichnung"
weight: 610
description: "So zeichnest du ein rosbag zur Untersuchung von Positionsproblemen und anderen Fehlern auf und lädst es zum Teilen vom Mäher herunter."
---
Bei der Fehlersuche, besonders bei Positionsproblemen, liefert eine rosbag-Aufzeichnung den Entwicklern eine vollständige Momentaufnahme der Sensordaten. Diese Anleitung zeigt dir, wie du sie erstellst und vom Mäher herunterlädst.

{{% alert title="Hinweis zum Datenschutz" color="warning" %}}
Ein rosbag enthält rohe Sensordaten, darunter die **GPS-Position deines Mähers**. Wenn du die Datei teilst, gibst du damit den Standort deines Gartens preis. Teile sie nur mit Personen, denen du vertraust.
{{% /alert %}}

## Voraussetzungen

- OpenMower läuft und der Mäher hat einen GPS-Fix: grünes GPS-Symbol in der App
- Du kannst per SSH oder Webterminal auf den Mäher zugreifen

## Schritt 1: Aufzeichnung starten

Verbinde dich per SSH oder Webterminal mit dem Mäher und öffne die ROS-Shell:

```bash
openmower shell
```

Wechsle in das Aufzeichnungsverzeichnis und starte die Aufzeichnung aller Topics:

```bash
cd /data/recordings
rosbag record -a
```

Damit werden **alle** aktiven ROS-Topics aufgezeichnet. Lass das Terminal offen. Die Aufzeichnung läuft, bis du sie mit <kbd>Strg</kbd>+<kbd>C</kbd> stoppst.

## Schritt 2: Flächenerfassung aktivieren

Öffne die OpenMower-App und aktiviere den **Modus zur Flächenerfassung**, den du auch zum Aufzeichnen der Mähflächen verwendest. Dadurch senden alle relevanten Topics für GPS, IMU und Radodometrie mit voller Rate.

{{% alert title="GPS-Fix erforderlich" color="warning" %}}
Das GPS-Symbol in der App muss **grün** sein, bevor du losfährst. Daten einer Aufzeichnung ohne Fix lassen sich für die Analyse nicht verwenden.
{{% /alert %}}

## Schritt 3: Testmuster fahren

Fahre die folgenden Muster ab. Jedes prüft einen anderen Aspekt der Positionsbestimmung:

| Muster | Zweck |
|---|---|
| Gerade Strecken | Lineare Odometrie und Übereinstimmung mit GPS |
| Eine Acht | Kombination aus Kurvenfahrt und Geradeausfahrt |
| Auf der Stelle im Uhrzeigersinn drehen | Schätzung des Gierwinkels, Ausrichtung laut IMU im Vergleich zu GPS |
| Auf der Stelle gegen den Uhrzeigersinn drehen | Dasselbe in Gegenrichtung |

Ein bis zwei Minuten pro Muster reichen aus. Du brauchst keine große Fläche; ein kleines freies Rasenstück genügt.

## Schritt 4: Aufzeichnung stoppen

Kehre zum Terminal zurück und drücke <kbd>Strg</kbd>+<kbd>C</kbd>. Gib dann `exit` ein, um die ROS-Shell zu verlassen.

Die `.bag`-Datei liegt jetzt unter `~/recordings/` auf dem Mäher. Den Dateinamen findest du mit:

```bash
ls -lh ~/recordings/
```

Der Name enthält einen Zeitstempel, zum Beispiel `2024-06-01-12-34-56.bag`.

## Schritt 5: Datei herunterladen

Kopiere die `.bag`-Datei aus `~/recordings/` vom Mäher auf deinen Computer.

{{< tabpane text=true >}}

{{% tab header="Linux / macOS" %}}
Verwende `scp` in deinem lokalen Terminal:

```bash
scp openmower@<mower-ip>:recordings/<filename>.bag .
```

Ersetze `<mower-ip>` durch die IP-Adresse des Mähers und `<filename>` durch den tatsächlichen Dateinamen. Die Datei wird in dein aktuelles Verzeichnis heruntergeladen.
{{% /tab %}}

{{% tab header="Windows" %}}
**Windows 10 ab Build 1809 und Windows 11** enthalten einen OpenSSH-Client. Öffne die **Eingabeaufforderung** oder **PowerShell** und führe aus:

```bat
scp openmower@<mower-ip>:recordings/<filename>.bag .
```

Verwende auf **älteren Windows-Versionen** stattdessen einen grafischen SFTP-Client:

- **[WinSCP](https://winscp.net)** – kostenlos und quelloffen
- **[Cyberduck](https://cyberduck.io)** – kostenlos und plattformübergreifend

Verbinde dich mit Protokoll **SFTP**, Host `<mower-ip>` und Benutzer `openmower`. Öffne `/home/openmower/recordings/`, um die Datei herunterzuladen.
{{% /tab %}}

{{< /tabpane >}}

{{% alert title="Tipp" color="info" %}}
`.bag`-Dateien lassen sich sehr gut komprimieren. Wenn du sie vor dem Teilen als ZIP packst, kann das die Dateigröße deutlich reduzieren.
{{% /alert %}}

Teile die heruntergeladene Datei mit der Person, die dir bei der Fehlersuche hilft, etwa über Discord, einen Dateifreigabedienst oder einen anderen passenden Weg.

## Schritt 6: Aufräumen

Lösche nach der Fehlersuche die Aufzeichnungen vom Mäher, um Speicherplatz freizugeben:

```bash
# delete a specific file
rm ~/recordings/<filename>.bag

# delete all recordings
rm ~/recordings/*.bag
```
