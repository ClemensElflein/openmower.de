---
title: "GPIO-Eingänge konfigurieren"
linkTitle: "GPIO-Eingänge konfigurieren"
weight: 220
description: >-
  Richte mit dem OpenMower-Eingabedienst GPIO-Eingänge für Not-Aus-Taster,
  Sensoren zum Erkennen angehobener Räder und weitere Taster ein.
---
## Überblick

In OpenMower kannst du GPIO-Pins als digitale Eingänge konfigurieren, die einen Not-Aus oder andere Ereignisse auslösen. Typische Anwendungen sind:

- **Sensoren an den Rädern**: erkennen, wenn der Mäher angehoben wird
- **Stopptasten**: Not-Aus-Tasten am Mäher
- **Kollisionssensoren**: erkennen, wenn der Mäher gegen ein Hindernis fährt

## Schritt 1: Konfigurationsdatei für die Eingänge anlegen

Als Ausgangspunkt für deine `inputs.yaml` empfehlen wir eine fertige, hardwarespezifische Konfiguration, die du an deine Verkabelung anpasst. Vorlagen für deine Trägerplatine findest du hier:

[https://github.com/ClemensElflein/open_mower_ros/tree/main/src/open_mower/params/hardware_specific](https://github.com/ClemensElflein/open_mower_ros/tree/main/src/open_mower/params/hardware_specific)

Lade die passende `inputs.yaml` herunter und speichere sie unter `/home/openmower/params/inputs.yaml`.

Hier ein einfaches Beispiel zur Orientierung:

```yaml
gpio:
  - name: Front left wheel lift
    line: GPIO10
    active: low
    emergency:
      reason: lift
      delay: 2500

  - name: Front right wheel lift
    line: GPIO11
    active: low
    emergency:
      reason: lift
      delay: 2500

  - name: Top stop button 1
    line: GPIO12
    active: low
    emergency:
      reason: stop
      delay: 10

  - name: Top stop button 2
    line: GPIO13
    active: low
    emergency:
      reason: stop
      delay: 10
```

### Konfigurationsfelder

| Feld              | Beschreibung                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| `name`             | Lesbare Bezeichnung des Eingangs                                                                 |
| `line`             | Name des GPIO-Pins, zum Beispiel `GPIO10`                                                                      |
| `active`           | Logikpegel, der das Ereignis auslöst: `low` oder `high`                                              |
| `emergency.reason` | Not-Aus-Art: `lift` für angehobene Räder, `stop` für die Stopptaste, `collision` für Hinderniserkennung |
| `emergency.delay`  | Entprellzeit/Verzögerung in Millisekunden, bevor der Not-Aus ausgelöst wird                                   |

## GPIO-Pinzuordnung

Das Beispiel oben verwendet GPIO10 bis GPIO13. So sind sie den physischen Anschlüssen der jeweiligen Platine zugeordnet.


{{< tabpane text=true >}}
{{% tab header="**Wähle deine OpenMower-Trägerplatine**:" disabled=true /%}}
{{% tab header="YardForce ab v1.2.0" text=true %}}

### OpenMower-YardForce-Platine ab v1.2.0

Ab dieser YardForce-Platinenversion kannst du zwischen den bisherigen OM-JST-XH-Anschlüssen und der Originalverkabelung über die CoverUI wählen. Die JST-XH-Anschlüsse sind vor allem für Umrüstungen von HWv1 gedacht, die Originalverkabelung für neue Umbauten.
Dafür besitzt die Platine einen Hall-Multiplexer (MUX), den du in `inputs.yaml` so einstellst:
```
yf_cover_ui:
  # ---- Hall Inputs Source Selector ----
  # "om" when the hall sensors get connected to the XHST plugs of the OpenMower board
  #      (or the robot-adapter-pinheader)
  # "oem_idc" when the hall sensors get connected to the (non-modded) OEM CoverUI board
  #      (and CoverUI get connected via the 16pin IDC cable to the OpenMower board)
  - name: Hall Inputs Source Selector
    id: hall_mux
    value: oem_idc
``` 

<br>Je nach Hall-MUX-Einstellung sind die GPIOs wie in diesem Bild zugeordnet:
![YF Hall-MUX GPIOs](./YF_asof_1.2.0.jpg)
<br>
Die grün markierten Stecker/GPIOs gehören zur Hall-MUX-Einstellung `om`, die orange markierten zu `oem_idc`.

{{% /tab %}}
{{% tab header="YardForce bis v1.1.0-beta" text=true %}}

### OpenMower-YardForce-Platine bis v1.1.0-beta

Halte die Platine so, dass die Ethernet-Ports unten links liegen. Die Pins sind von oben nach unten aufgelistet.

| Position      | GPIO   |
| ------------- | ------ |
| 1. (ganz oben) | GPIO10 |
| 2.           | GPIO11 |
| 3.           | GPIO12 |
| 4.           | GPIO13 |

{{% /tab %}}

{{% tab header="Universal" text=true %}}


### OpenMower-Universal-Board

Halte die Platine so, dass die Ethernet-Ports zu dir zeigen.

| Position     | GPIO   |
| ------------ | ------ |
| Oben links     | GPIO13 |
| Oben rechts    | GPIO12 |
| Unten rechts | GPIO11 |
| Unten links  | GPIO10 |

{{% /tab %}}

{{% tab header="SABO/John Deere" text=true %}}

### OpenMower-SABO-/John-Deere-Platine

Wenn du die Eingabekonfiguration der SABO-/John-Deere-Trägerplatine ändern möchtest, lade am besten die [Standarddatei `inputs.yaml`](https://github.com/ClemensElflein/open_mower_ros/blob/main/src/open_mower/params/hardware_specific/Sabo/inputs.yaml) herunter.

{{% /tab %}}

{{< /tabpane >}}

## Schritt 2: Eingabedienst aktivieren

Ergänze Folgendes in deiner `mower_params.yaml`, bei Umbauten mit dem Universal-Board in `custom_params.yaml`:

```yaml
ll:
  services:
    input:
      config_file: /data/params/inputs.yaml
```

So öffnest du die Datei zum Bearbeiten:

```bash
openmower configure ros
```

{{% alert title="Pfadzuordnung unter OSv2" color="info" %}}
Unter OSv2 wird `/home/openmower/params` im Container als `/data/params` eingebunden. Bei einem anderen Aufbau musst du den Pfad in `config_file` entsprechend anpassen.
{{% /alert %}}

## Schritt 3: OpenMower neu starten

Speichere beide Dateien und starte den Dienst neu, um die Änderungen zu übernehmen:

```bash
openmower restart
```

Die GPIO-Eingänge sind jetzt aktiv. Sobald der festgelegte Logikpegel erkannt wird, lösen sie die konfigurierten Not-Aus-Ereignisse aus.
