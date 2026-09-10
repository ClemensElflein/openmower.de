---
title: "Firmware-Version v0.0.3"
date: 2026-03-06
author: "Clemens Elflein"
description: "v0.0.3 verbessert die SABO-/John-Deere-Unterstützung, das Akkumanagement, die dynamische Energieverwaltung und den Eingabedienst."
---
Firmware [v0.0.3](https://github.com/xtech/fw-openmower-v2/releases/tag/v0.0.3) ist da. Diese Version ist ein großer Schritt für SABO- und John-Deere-Nutzer und verbessert außerdem die Zuverlässigkeit auf allen Plattformen.

### Unterstützung für SABO / John Deere

Der größte Teil der Arbeit an dieser Version floss in die SABO-Unterstützung. Das hat fast vollständig [@Apehaenger](https://github.com/Apehaenger) vorangetrieben – vielen Dank!

Die SABO-Trägerplatine wird damit nun gut unterstützt:

- **BMS-Integration** – Das SBS/SABO-Batteriemanagementsystem ist jetzt eingebunden. Die Firmware kann dadurch Betriebszustand, Ladezustand und Alterungszustand des Akkus erfassen.
- **Dynamische Energieverwaltung** – Die Energieverwaltung kann nun während des Betriebs auf Zustandsänderungen reagieren und ist an die SABO-Plattform angebunden. Die Firmware kann die Energiezustände damit dynamisch anpassen.
- **Effizientere COBS-Verarbeitung** – Der YardForce-ESC-Treiber hat einen Interrupt zur Zeichenerkennung erhalten. Das macht die Auswertung von COBS-Frames effizienter und senkt die CPU-Last bei der seriellen Kommunikation.

### Verbesserungen am Eingabedienst

Auch die Eingabeverarbeitung wurde überarbeitet:

- **Einstellbare Verzögerungen** – Verzögerungen des Eingabedienstes lassen sich jetzt konfigurieren. Entprellung und Halteverhalten können so leichter an die jeweilige Plattform angepasst werden.
- **Tastendrücke simulieren** – Ein neuer Mechanismus kann Tastendrücke softwareseitig erzeugen. Das hilft bei automatisierten Tests und Hardware-in-the-Loop-Simulationen.
- **Not-Aus auch bei kurzen Signalen** – Die Firmware löst den Not-Aus jetzt auch dann korrekt aus, wenn ein Eingang nur sehr kurz aktiv ist. Solche kurzen Signale konnten zuvor übersehen werden. Die Korrektur verbessert die Sicherheit auf allen Plattformen.

### Interne Änderungen

- `xbot_framework` und das Submodul `services` wurden auf die jeweils neueste Version aktualisiert.
- Der SystemView-Build für Echtzeit-Tracing und Fehlersuche wurde repariert.

### Download

Das Firmware-Paket findest du auf der [Release-Seite von v0.0.3](https://github.com/xtech/fw-openmower-v2/releases/tag/v0.0.3):

- **`fw-openmower-v2-v0.0.3.zip`** – enthält Binärdateien für alle unterstützten Trägerplatinen
