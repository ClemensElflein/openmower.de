---
title: "Mitmachen"
linkTitle: "Mitmachen"
weight: 990
description: >
  So kannst du zu OpenMower beitragen: Code, Firmware, Dokumentation und Hilfe in der Community.
---
OpenMower ist ein Community-Projekt. Jeder Beitrag ist willkommen: Fehlermeldungen, Code, Verbesserungen an der Dokumentation oder einfach Hilfe für andere auf Discord.

Du weißt noch nicht, wo du anfangen sollst? Lies den Überblick zur [Systemarchitektur]({{< relref "/docs/knowledge-base/getting-started/architecture" >}}), um das Zusammenspiel der Komponenten zu verstehen, bevor du in ein bestimmtes Repository einsteigst.

## An dieser Dokumentation mitarbeiten

Die Dokumentation zu verbessern ist eine der einfachsten Möglichkeiten, etwas beizutragen. Für kleine Korrekturen brauchst du keine lokalen Werkzeuge.

**Für kleine Änderungen** wie Tippfehler, Formulierungen oder ergänzende Hinweise: Unten auf jeder Seite findest du **Diese Seite bearbeiten**. Klicke darauf, bearbeite die Datei direkt auf GitHub und öffne einen Pull Request. Fertig.

**Für größere Änderungen** wie neue Artikel oder Umstrukturierungen: Starte die Website lokal mit Docker. Außer Docker selbst musst du dafür nichts installieren.

1. [Erstelle einen Fork des Repositories](https://github.com/ClemensElflein/openmower.de/fork) auf GitHub.
2. Klone deinen Fork:
   ```bash
   git clone https://github.com/<your-username>/openmower.de.git
   cd openmower.de
   ```
3. Starte den lokalen Entwicklungsserver:
   ```bash
   docker compose up
   ```
4. Öffne [http://localhost:8080](http://localhost:8080) im Browser. Wenn du eine Datei speicherst, wird die Website automatisch neu erstellt. Falls `502 Bad Gateway` erscheint, warte kurz – der Server startet noch.
5. Wenn du mit deinen Änderungen zufrieden bist, beende den Server mit <kbd>Strg</kbd>+<kbd>C</kbd>. Erstelle einen Commit, pushe ihn und öffne einen Pull Request im Haupt-Repository.

Die Dokumentation ist in Markdown geschrieben und verwendet das Theme [Hugo Docsy](https://www.docsy.dev/).

## Code beitragen

{{% alert title="Bevor du größere Änderungen angehst" color="warning" %}}
Öffne zuerst ein Issue, um deinen Ansatz zu besprechen, bevor du Zeit in die Umsetzung steckst. Vielleicht arbeitet bereits jemand am selben Thema. Oft gibt es auch Architekturentscheidungen, die für die Umsetzung eine Rolle spielen. Eine kurze Abstimmung kann dir viel unnötige Arbeit ersparen und erhöht die Chance, dass dein Pull Request übernommen wird.

Du kannst deine Idee auch im Kanal **#software** auf [Discord](https://discord.gg/jE7QNaSxW7) besprechen, bevor du mit dem Programmieren beginnst.
{{% /alert %}}

OpenMower ist nach Aufgaben auf mehrere Repositories aufgeteilt. So bleibt jedes Repository übersichtlich, und Hardware, Firmware und Software können sich unabhängig weiterentwickeln, ohne dass Änderungen in einem Bereich andere, nicht betroffene Teile beeinträchtigen.

### Software

| Repository | Inhalt |
|---|---|
| [open_mower_ros](https://github.com/ClemensElflein/open_mower_ros) | ROS-Software: Navigation und Planung |
| [openmower-app](https://github.com/xtech/openmower-app) | Die OpenMower-App für Smartphone und Browser |
| [OpenMowerOS](https://github.com/ClemensElflein/OpenMowerOS) | Das Betriebssystem-Image |

### Firmware

| Repository | Inhalt |
|---|---|
| [fw-openmower-v2](https://github.com/xtech/fw-openmower-v2) | Mainboard-Firmware: Motorsteuerung, Sensortreiber und Hardware-Abstraktion |
| [xesc_firmware](https://github.com/ClemensElflein/xesc_firmware) | Firmware der xESC-Motorcontroller |

### Hardware

| Repository | Inhalt |
|---|---|
| [hw-openmower-universal](https://github.com/xtech/hw-openmower-universal) | Universal-Mainboard |
| [hw-openmower-yardforce](https://github.com/xtech/hw-openmower-yardforce) | YardForce-Mainboard |
| [hw-openmower-sabo](https://github.com/xtech/hw-openmower-sabo) | SABO-/John-Deere-Mainboard |

## Probleme melden

- **Softwarefehler**: Öffne ein Issue im passenden GitHub-Repository.
- **Fehler in der Dokumentation**: Öffne ein Issue oder einen Pull Request in [openmower.de](https://github.com/ClemensElflein/openmower.de).
- **Fragen und allgemeiner Austausch**: Nutze [Discord](https://discord.gg/jE7QNaSxW7).

## Das Projekt unterstützen

OpenMower wird in der Freizeit entwickelt und gepflegt. Wenn du das Projekt finanziell unterstützen möchtest, geht das über [Patreon](https://patreon.com/ClemensElflein).

---

## Verhaltensregeln

OpenMower ist ein offenes Projekt, in dem alle willkommen sind. Wer mitmacht – in GitHub-Issues, Pull Requests, auf Discord oder anderswo in der Community – soll sich an die folgenden Regeln halten.

### Geh respektvoll mit anderen um

Behandle alle mit Respekt. Unterschiedliche Meinungen sind in Ordnung, persönliche Angriffe, Belästigung und diskriminierende Sprache nicht. Das gilt unabhängig von Erfahrung, Hintergrund oder der Art des Beitrags.

### Bleib konstruktiv

Beziehe dein Feedback auf die Arbeit, nicht auf die Person. Erkläre, *warum* etwas geändert werden sollte, statt nur eine Änderung zu verlangen. Jeder hat einmal angefangen.

### Hab Geduld

OpenMower lebt von freiwilliger Mitarbeit. Die Zeit der Maintainer und Mitwirkenden ist begrenzt. Dass eine Antwort etwas dauert, ist normal. Nach ein paar Tagen freundlich nachzufragen ist völlig in Ordnung.

### Bleib beim Thema

Diskussionen sollten sich auf OpenMower und das jeweilige Thema beziehen. Gespräche über andere Themen gehören in die passenden Discord-Kanäle.

### Geh von guten Absichten aus

Die meisten möchten helfen. Wenn etwas unhöflich oder unverständlich klingt, bedenke, dass sprachliche Unterschiede oder ein anderer Kommunikationsstil die Ursache sein können, bevor du den Konflikt verschärfst.

### Umgang mit Verstößen

Verstöße gegen diese Regeln können zu einer Verwarnung führen. Bei wiederholten oder schweren Verstößen ist ein Ausschluss aus den Community-Bereichen möglich. Darüber entscheiden die Maintainer des Projekts.
