---
title: "Die Karte"
linkTitle: "Die Karte"
weight: 520
description: >
  Informationen zur OpenMower-Karte: Mähflächen, Navigationsflächen und Andockpunkt.
---
## Die Karte

Die wichtigste Grundlage für OpenMower ist seine Karte. Sie legt fest, wo der Roboter fahren darf **(= Navigationsfläche)**, welche Flächen er mähen soll **(= Mähfläche)** und wo die Ladestation steht. Mit diesen Informationen kann der Roboter selbstständig arbeiten.

Jede Fläche besteht aus **einer Umrandung** und **mehreren Hindernissen**. Der Mäher darf innerhalb der Umrandungen aller Flächen fahren, mit Ausnahme der Hindernisse. So kannst du Teile deines Rasens ausschließen und verhindern, dass der Mäher dort hineinfährt.

Die Karte wird in der Datei `map.json` gespeichert. Sie liegt auf dem Mäher unter `/home/openmower/ros_home`
