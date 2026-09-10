---
title: "Gamepad verwenden"
linkTitle: "Gamepad verwenden"
weight: 510
description: "Verbinde ein USB-Gamepad mit OpenMower, steuere damit den Roboter und erfasse deine Mähflächen."
---
Mit einem USB-Gamepad kannst du OpenMower während der Flächenerfassung intuitiv und präzise steuern. Die Analogsticks helfen dir, die Umrandungen deiner Mähflächen sauber abzufahren. Das fällt damit leichter als mit dem Bildschirm-Joystick der Web-App.

Jedes Xbox-kompatible USB-Gamepad funktioniert ohne weitere Einrichtung. Stecke es einfach in einen USB-Anschluss deines Raspberry Pi. OpenMower erkennt es automatisch.

{{% alert title="Aufzeichnungsmodus erforderlich" color="info" %}}
Die Gamepad-Steuerung funktioniert nur im **Aufzeichnungsmodus**. Aktiviere diesen Modus in der OpenMower-App, bevor du die unten beschriebenen Tasten verwendest.

Wenn noch keine Karte erfasst wurde, startet OpenMower automatisch im Aufzeichnungsmodus. Du musst dann nichts weiter tun.
{{% /alert %}}

## Videoanleitung

Das folgende Video zeigt die gesamte Flächenerfassung, einschließlich der Steuerung per Gamepad und des Speicherns der Mähflächen.

{{< youtube j7qkwuoHJpI >}}

## Tastenbelegung

{{< figure src="images/gamepad_controls.png" caption="OpenMower-Gamepad-Steuerung (Bild von shutterstock.com lizenziert)" >}}

Die Tabellen beschreiben alle Tasten für die normale Bedienung und Flächenerfassung. Meist hältst du **A** zum Fahren gedrückt und verwendest **B**, um Aufzeichnungen zu starten und zu stoppen.

### Fahren

| Eingabe | Aktion |
|-------|--------|
| **A** gedrückt halten + linker Analogstick | Mäher fahren |
| **RB** | Turbomodus: schneller fahren |

### Flächen erfassen

| Eingabe | Aktion |
|-------|--------|
| **B** | Aufzeichnung des aktuellen Polygons starten / stoppen |
| **Y** + **Steuerkreuz oben** | Aktuelle Fläche abschließen und als **Navigationsfläche** speichern: Der Mäher darf hier fahren, mäht aber nicht |
| **Y** + **Steuerkreuz unten** | Aktuelle Fläche abschließen und als **Mähfläche** speichern: Mindestens eine ist erforderlich |

### Ladestation

Zum Erfassen der Ladestation brauchst du zwei getrennte Positionspunkte, die die Anfahrtrichtung festlegen. Die Verbindungslinie zeigt dem Mäher, wie er sich bei der Rückkehr zur Ladestation ausrichten soll.

1. Fahre zu einem Punkt etwa **1,5 m vor der Ladestation**, sodass der Mäher zur Station zeigt. Drücke **X**, um den ersten Punkt zu erfassen.
2. Fahre vorwärts, bis die **Vorderräder gerade am Rand der Ladestation stehen**. Fahre noch nicht ganz hinein. Drücke erneut **X**, um den zweiten Punkt zu erfassen.

| Eingabe | Aktion |
|-------|--------|
| **X** beim ersten Drücken | Anfahrpunkt etwa 1,5 m vor der Ladestation erfassen |
| **X** beim zweiten Drücken | Einfahrtspunkt am Rand der Ladestation erfassen |
