---
title: "Universal-Board v1.1.1-beta"
date: 2025-06-19
author: "Clemens Elflein"
description: "3,3-V-Versorgung des EEPROM korrigiert, SATA durch XH-Steckverbinder ersetzt, Sicherung und I2C4-EEPROM-Pins ergänzt."
---
[v1.1.1-beta](https://github.com/xtech/hw-openmower-universal/releases/tag/v1.1.1-beta) behebt einen kritischen Fehler in der EEPROM-Stromversorgung und ändert die Steckverbinder zwischen den Modulen.

### Änderungen

**3,3-V-Versorgung des EEPROM korrigiert** – In der vorherigen Version war die 3,3-V-Versorgung des EEPROM nicht angeschlossen. Die Verbindung ist jetzt korrekt verlegt; damit ist [#6](https://github.com/xtech/hw-openmower-universal/issues/6) behoben. Ohne diese Korrektur kann das Core-Board das EEPROM der Trägerplatine nicht auslesen und das angeschlossene Mähermodell deshalb nicht automatisch erkennen.

**XH-Steckverbinder ersetzen SATA** – Die Datenverbindungen zwischen den Modulen wurden von SATA auf XH umgestellt. SATA war in den frühen Versionen eine pragmatische Wahl. XH-Steckverbinder eignen sich besser für diesen Zweck und sind leichter zu beschaffen.

**Sicherung ergänzt** – Im Versorgungspfad wurde eine Sicherung zum Schutz eingebaut.

**I2C4-EEPROM-Pins** – Pins für die I2C4-EEPROM-Schnittstelle wurden ergänzt.

**Fehler in der Stückliste korrigiert.**

### Download

**[release-hw-openmower-universal-v1.1.1-beta.zip](https://github.com/xtech/hw-openmower-universal/releases/tag/v1.1.1-beta)** – Gerber-Dateien, Stückliste und Bestückungsdaten.
