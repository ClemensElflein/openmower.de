---
title: "CM4-eMMC flashen"
linkTitle: "CM4-eMMC flashen"
weight: 110
description: "So spielst du mit rpiboot und Raspberry Pi Imager ein neues Betriebssystem-Image auf den eingebauten eMMC-Speicher des Raspberry Pi Compute Module 4."
---
{{% alert title="Nur für CM4 mit eMMC" color="warning" %}}
Diese Anleitung gilt **nur für CM4-Varianten mit eingebautem eMMC-Speicher**. Das CM4 Lite hat keinen eMMC-Speicher, sondern verwendet eine microSD-Karte. Dieser Vorgang ist dafür nicht nötig.

Prüfe die Modellnummer deines CM4: Bei Varianten mit eMMC ist die Speichergröße im Namen enthalten, zum Beispiel CM4008032 für 32 GB eMMC. Lite-Varianten sind ausdrücklich als „Lite“ gekennzeichnet, zum Beispiel CM4008000.
{{% /alert %}}

Das CM4 mit eMMC nutzt eingebauten Flash-Speicher statt einer microSD-Karte. Um ein neues Image aufzuspielen, musst du es in den USB-Bootmodus versetzen. Dann erscheint es auf deinem Computer als Massenspeicher.

Diese Anleitung beschreibt die OpenMower-spezifischen Schritte. Weitere Details findest du in der [offiziellen Raspberry-Pi-Dokumentation](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc).

## Voraussetzungen

- Einen Computer mit Linux, Windows oder macOS
- Ein Micro-USB-Kabel zum USB-Anschluss des xCore-Boards
- Das Betriebssystem-Image, das du aufspielen möchtest, zum Beispiel OpenMower OS

## Schritt 1: USB-Bootmodus aktivieren

Das xCore-Board hat eine Taste **Rpi Boot**. Es ist die linke der beiden Tasten; die Beschriftung befindet sich unter dem CM4-Steckplatz.

![Position der Taste Rpi Boot auf dem xCore-Board](images/rpi-boot-button.png)

1. Halte **Rpi Boot** gedrückt.
2. Schließe dabei die Stromversorgung an das xCore-Board an oder verbinde das Micro-USB-Kabel mit deinem Computer.
3. Lass die Taste los, sobald das Board mit Strom versorgt wird.

Das CM4 ist jetzt im USB-Bootmodus.

## Schritt 2: rpiboot auf dem Computer installieren

{{< tabpane text=true >}}

{{% tab header="Linux" %}}
```bash
sudo apt install rpiboot
sudo rpiboot
```
{{% /tab %}}

{{% tab header="Windows" %}}
1. Lade das Installationsprogramm von der [usbboot-Release-Seite](https://github.com/raspberrypi/usbboot/releases) herunter und führe es aus.
2. Starte den Computer nach der Installation neu.
3. Öffne bei aktiviertem USB-Bootmodus des CM4 **Start → rpiboot - Mass Storage Gadget**.
{{% /tab %}}

{{% tab header="macOS" %}}
Baue rpiboot aus dem Quellcode und führe dann aus:
```bash
rpiboot -d mass-storage-gadget64
```
Die Anleitung zum Bauen findest du im [usbboot-Repository](https://github.com/raspberrypi/usbboot).
{{% /tab %}}

{{< /tabpane >}}

Nach wenigen Sekunden erscheint der eMMC-Speicher des CM4 auf deinem Computer als USB-Massenspeicher.

{{% alert title="Tipp" color="info" %}}
Wenn das Gerät nicht erkannt wird, verzichte auf USB-Hubs und verbinde das Micro-USB-Kabel direkt mit dem Computer.
{{% /alert %}}

## Schritt 3: Image aufspielen

Schreibe das Betriebssystem-Image mit **Raspberry Pi Imager** auf das eMMC-Gerät. Wähle den eMMC-Speicher als Ziel aus. Er wird wie jedes andere USB-Laufwerk angezeigt.

Unter Linux/macOS kannst du alternativ `dd` verwenden:

```bash
sudo dd if=your-image.img of=/dev/sdX bs=4MiB status=progress oflag=sync
```

Ersetze `/dev/sdX` durch den tatsächlichen Gerätepfad des eMMC-Speichers. Prüfe ihn vor dem Ausführen sorgfältig.

## Schritt 4: Vom eMMC starten

Wenn das Schreiben abgeschlossen ist, trenne das Micro-USB-Kabel und schalte die Stromversorgung des Boards aus und wieder ein. Das CM4 startet jetzt mit dem neu aufgespielten Image.
