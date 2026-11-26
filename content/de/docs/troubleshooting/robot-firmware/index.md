---
title: "Fehlerbehebung: Ungültige Roboter-Firmware"
linkTitle: "Roboter-Firmware"
description: >-
  Behebe den Fehler „Robot firmware ... invalid for this hardware“, indem du
  die passende Board-Variante (`ll/board`) in mower_params.yaml einstellst.
tags: [troubleshooting, firmware, board, mower_params]
aliases: ["/ll/board/"]
---
Die Firmware gibt wiederholt folgenden Fehler aus und die Status-LED blinkt rot:

```text
Robot firmware '<name>' invalid for this hardware...
```

Das bedeutet, dass der Wert von `board:` in deiner `mower_params.yaml` nicht zur
tatsächlich eingebauten Board-Variante passt. Die Firmware lehnt den Namen ab und
wartet weiter auf einen gültigen Wert.

## Lösung

{{< tabpane text=true >}}
{{% tab header="Unterstützter Mäher" text=true %}}

Öffne die ROS-Konfiguration. Dadurch wird `mower_params.yaml` geöffnet:

```bash
openmower configure ros
```
<br>

Trage unter `ll:` bei `board:` die Variante ein, die zu deiner Hardware passt:

```yaml
ll:
  board: "Worx"
```
<br>

Nach dem Speichern startet OpenMower automatisch neu. Die Status-LED sollte
anschließend grün leuchten.

{{% /tab %}}
{{% tab header="Universal / Eigenbau (MOWER=CUSTOM)" text=true %}}

Bearbeite `~/params/custom_params.yaml`:

```bash
nano ~/params/custom_params.yaml
```
<br>

Setze unter `ll:` den Wert für `board:`. Bei einem Universal-Board verwendest du
je nach Akku `Universal-5S`, `Universal-7S` oder `Universal-8S`:

```yaml
ll:
  board: "Universal-7S"
```
<br>

Beim Bearbeiten von `custom_params.yaml` wird die Software nicht automatisch
neu gestartet. Übernimm die Änderung deshalb mit:

```bash
openmower restart
```
<br>

Die vollständige Referenz für eigene Umbauten findest du unter [Universal-Board konfigurieren]({{< relref "/docs/Knowledge-Base/configuration/universal-board-configuration" >}}).

{{% /tab %}}
{{< /tabpane >}}

## Automatisch erkannt - keine Einstellung nötig

Diese Boardvarianten erkennt die Firmware beim Start an der Hardware selbst,
`board:` wird dafür ignoriert:

| Boardvariante  | Erkannt über                                                       |
| -------------- | ------------------------------------------------------------------ |
| `Sabo`         | EEPROM auf der Trägerplatine                                       |
| `xBot`         | EEPROM auf der Trägerplatine                                       |
| `YardForce`    | EEPROM sowie Mähmotor-ESC auf UARTD2 antwortet ohne YFR4-Protokoll |
| `YardForce-V4` | EEPROM sowie Mähmotor-ESC auf UARTD2 antwortet mit YFR4-Protokoll  |


## Diese Boards brauchen den Wert

Bei diesen Boards wartet die Firmware, bis ein passender Name ankommt - daher
kommt der Fehler „Robot firmware ... invalid for this hardware“:

| Boardvariante  | Hardware                                       |
| -------------- | ---------------------------------------------- |
| `Universal-5S` | Universal-Board mit 5S-Akku                    |
| `Universal-7S` | Universal-Board mit 7S-Akku                    |
| `Universal-8S` | Universal-Board mit 8S-Akku                    |
| `Worx`         | Universal-Board mit Worx-Funktionalität        |
| `Lyfco-E1600`  | Universal-Board mit Lyfco-E1600-Funktionalität |
| `Husq310MKII`  | Husqvarna-310-MKII-Platine                     |

Der Wert muss exakt übereinstimmen, einschließlich Groß- und Kleinschreibung.

Der Wert ist die Boardvariante, nicht zwingend die Platine: `Universal-5S`/`7S`/`8S`
sind dasselbe Universal-Board mit einem anderen Akku, `Worx`, `Lyfco-E1600` und
`Husq310MKII` dasselbe Board mit anderem Gehäuse und anderer UI.

Die Standardvorlage mit allen gültigen Werten findest du im OpenMowerOS-Repository:
[mower_params.yaml](https://github.com/ClemensElflein/OpenMowerOS/blob/main/stage-openmower/40-openmower/files/home/openmower/params/mower_params.yaml).
