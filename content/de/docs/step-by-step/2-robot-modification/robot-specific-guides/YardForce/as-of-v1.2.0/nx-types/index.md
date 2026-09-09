---
title: "NX Modelle"
linkTitle: "NX Modelle"
weight: 30
description: >
  Umbauanleitung für YardForce NX Mäher mit Trägerplatine ab Version 1.2.0
---
{{% alert title="Nur für Trägerplatinen ab 1.2.0!" color="warning" %}}
Diese Anleitung gilt ausschließlich für **Trägerplatinen ab Version 1.2.0**!<br>
![Erkennungsmerkmale der Trägerplatine v1.2.0](../carrierboard_version_v1.2.0.jpg)<br>
{{% /alert %}}

{{% alert title="Anleitung in Arbeit" color="info" %}}
Diese Anleitung wird gerade geschrieben. Schau bald wieder vorbei oder frag auf [Discord](https://discord.gg/jE7QNaSxW7) nach aktuellen Informationen.
{{% /alert %}}

## GPIO-Eingänge konfigurieren

Die YardForce-NX-Modelle verwenden GPIO-basierte Sensoren für die Radanhebeerkennung, Stopptasten und Kollisionserkennung.
Diese müssen konfiguriert werden, bevor der Roboter einsatzbereit ist.

Für NX-Modelle gibt es derzeit noch keine eigene hardwarespezifische `inputs.yaml`.
Verwende als Ausgangspunkt die [Definition für SA/SC-Modelle](https://github.com/ClemensElflein/open_mower_ros/blob/main/src/open_mower/params/hardware_specific/YardForceSA_OEM/inputs.yaml) als Vorlage und passe sie an deine Verkabelung an.

Ausführliche Hinweise findest du unter [GPIO-Eingänge konfigurieren]({{< relref "/docs/Knowledge-Base/configuration/configure-gpio-inputs" >}}) – einschließlich der Hall-MUX-Auswahl, die bei Trägerplatinen ab Version 1.2.0 erforderlich ist.
