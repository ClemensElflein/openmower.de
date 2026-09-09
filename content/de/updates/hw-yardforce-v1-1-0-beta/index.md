---
title: "YardForce-Trägerplatine v1.1.0-beta"
date: 2025-06-19
author: "Clemens Elflein"
description: "Wählbare Lüfterspannung, Sicherungen, AGPIO an Erweiterungsanschlüssen und verbesserter Bestückungsdruck."
---
[v1.1.0-beta](https://github.com/xtech/hw-openmower-yardforce/releases/tag/v1.1.0-beta) bringt mehrere Hardware-Verbesserungen für die YardForce-v2-Trägerplatine.

### Änderungen

**Wählbare Lüfterspannung** – Die Versorgungsspannung der Lüfteranschlüsse lässt sich jetzt einstellen. Passende Beschriftungen wurden ergänzt. Der dritte FAN-Anschluss wurde entfernt und die Dokumentation im Bestückungsdruck entsprechend angepasst. Damit ist [#3](https://github.com/xtech/hw-openmower-yardforce/issues/3) behoben.

**Sicherungen** – Zum Schutz wurden Sicherungen in den Versorgungspfad aufgenommen.

**AGPIO an den Erweiterungsanschlüssen** – Die Pins der Erweiterungsanschlüsse verwenden jetzt AGPIO. Das eignet sich auf dem STM32 besser für analoge und allgemeine Signale.

**Verbesserter Bestückungsdruck** – Beschriftungen auf der gesamten Platine wurden ergänzt und korrigiert.

### Download

**[release-hw-openmower-yardforce-v1.1.0-beta.zip](https://github.com/xtech/hw-openmower-yardforce/releases/tag/v1.1.0-beta)** – Gerber-Dateien, Stückliste und Bestückungsdaten.
