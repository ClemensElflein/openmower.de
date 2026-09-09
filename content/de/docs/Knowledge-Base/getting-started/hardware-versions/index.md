---
title: "Hardware-Versionen und bekannte Probleme"
linkTitle: "Hardware-Versionen"
weight: 40
description: "Unterscheide OpenMower-v1- und v2-Hardware, finde die Repositories der Trägerplatinen und informiere dich über ältere Versionen, bekannte Fehler und Korrekturen."
resources:
  - src: "**.jpg"
---
{{% toc %}}

## Aktuelle Hardware (v2-Plattform)

Änderungen und bekannte Probleme der v2-Plattform findest du im jeweiligen Repository:
- **YardForce:** [https://github.com/xtech/hw-openmower-yardforce](https://github.com/xtech/hw-openmower-yardforce) 
- **SABO / John Deere:** [https://github.com/xtech/hw-openmower-sabo](https://github.com/xtech/hw-openmower-sabo)
- **Universal:** [https://github.com/xtech/hw-openmower-universal](https://github.com/xtech/hw-openmower-universal)


## Ältere Hardware (v1-Plattform)
{{% alert title="Information" color="info" %}}

Die v1-Hardware verwendet eine völlig andere Architektur als die v2-Hardware. Deshalb lässt sie sich nur schwer an neue Mähermodelle anpassen.
Wenn du bereits ein v1-Kit hast, ist das kein Grund zur Sorge: Es funktioniert weiterhin mit deinem Mäher.
Ein Umstieg auf v2 bringt dir in diesem Fall keinen wirklichen Vorteil. Für neue Umbauten wird die v2-Plattform empfohlen.
{{% /alert %}}


### 0.13.0 – Rot

{{< imgproc 0_13_b Fill "400x400 q99" />}}
{{< imgproc 0_13_a Fill "400x400 q99" />}}

#### Wichtige Änderungen

 * Eigene CoverUI zum Kit hinzugefügt
 * Unterstützung für das dfPlayer-Soundmodul entfernt 

#### Bekannte Probleme

 * Die 2,5-mm-Schrauben zur Befestigung des RPi4 fehlten. Betrifft Kits, die vor Juni 2023 verschickt wurden.
 * Die erste Charge der 0.13-Platinen wurde versehentlich mit „latest“ beschriftet. Du musst nichts unternehmen.
 * [Veraltete Firmware](https://openmower.de/archive/v1.0.2/docs/versions/errata/outdated-firmware/). Betrifft Kits, die vor Mai 2023 verschickt wurden.
 * [Falscher IC2-Chip](https://openmower.de/archive/v1.0.2/docs/versions/errata/ic2-is-wrong/). Betrifft Kits, die vor Mai 2023 verschickt wurden.
 * [Regensensorkabel hat eine Buchse, benötigt aber einen Stecker](https://openmower.de/archive/v1.0.2/docs/versions/errata/wrong-rain-sensor-cable/). Betrifft Kits, die vor Mai 2023 verschickt wurden.


### 0.12.0 – Schwarz

{{< imgproc 0_12_x Resize "400x q99" />}}

#### Wichtige Änderungen

 * IMU: LSM6DSO statt WT901

#### Bekannte Probleme

 * Die SPI-Leiterbahnen vom Pico waren falsch verlegt. Das ist bereits in der Firmware behoben. Du musst nichts unternehmen.
 * [Veraltete Firmware](https://openmower.de/archive/v1.0.2/docs/versions/errata/outdated-firmware/)
 * [Falscher IC2-Chip](https://openmower.de/archive/v1.0.2/docs/versions/errata/ic2-is-wrong/)
 * [Regensensorkabel hat eine Buchse, benötigt aber einen Stecker](https://openmower.de/archive/v1.0.2/docs/versions/errata/wrong-rain-sensor-cable/)


### 0.11.0 – Violett

{{< imgproc 0_11_x Resize "400x q99" />}}

#### Wichtige Änderungen

 * WT901 über I2C angebunden, um Pins für den dfPlayer freizugeben
 * Ladestationsplatine um zusätzliche Bohrungen und Klemmen erweitert (rot)

#### Bekannte Probleme

* [Falscher IC2-Chip](https://openmower.de/archive/v1.0.2/docs/versions/errata/ic2-is-wrong/)


### 0.10.0 – Grün

{{< imgproc 0_10_x Resize "400x q99" />}}

#### Wichtige Änderungen

 * Ladestationsplatine hinzugefügt (grün)

#### Bekannte Probleme

* [Falscher IC2-Chip](https://openmower.de/archive/v1.0.2/docs/versions/errata/ic2-is-wrong/)


### 0.9.3 – Ebenfalls grün

{{< imgproc 0_9_3 Resize "400x q99" />}}
{{< imgproc 0_9_3_gps Resize "400x q99" />}}

Erste Version. Experimenteller xESC2040 statt xESC-mini (STM32).
