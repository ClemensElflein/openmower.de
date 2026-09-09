---
title: "Mähmotorstrom auf 6 A erhöhen"
linkTitle: "Mähmotor auf 6 A"
description: >
  Motorkonfiguration für mehr Mähleistung anpassen.
---
Autor: ow@discord

YardForce-Classic-Mähmotor: https://gist.github.com/olliewalsh/fcc2e6d7852cad5c1f64ce0837306a66

Eine alternative Konfiguration stammt von Tomm: https://discord.com/channels/958476543846412329/961803746399101008/1110669606038806698


Der Akkustrom ist auf 3 A begrenzt, der Motorstrom auf 6 A. Die Drehzahl ist auf 3.500 U/min begrenzt. Die Leistungsreduzierung bei steigender Temperatur oder sinkender Spannung ist deaktiviert. Ich würde eine 6-A-Sicherung verwenden, da die Fahrmotoren manchmal mehr als 1 A melden.

Anleitung:
Abdeckung öffnen, Sicherung ersetzen und die Konfiguration des mittleren xESC mit folgendem Tool übertragen: [VESC-TOOL](https://vesc-project.com/vesc_tool).
