---
title: "Datenerfassung"
linkTitle: "Datenerfassung"
weight: 995
description: "Welche Daten dein Mäher sendet und wann."
---
## Worum es hier geht
Diese Seite erklärt, welche Daten dein Mäher mit OpenMowerOS über das Netzwerk sendet und warum. Wie die Website openmower.de selbst mit Cookies und Webanalyse umgeht, erfährst du in unserer [Datenschutzerklärung]({{< param name="privacy_policy" >}}).

## Suche nach Betriebssystem-Updates
OpenMowerOS prüft einmal täglich automatisch, ob Updates verfügbar sind. Es installiert sie nicht automatisch: Ist eine neue Version verfügbar, erscheint beim nächsten Aufruf des Befehls `openmower` ein Hinweis – künftig auch in der App.

Bei jeder Prüfung wird eine Anfrage mit folgenden Informationen an unseren Update-Server gesendet:

- **Deine IP-Adresse** fällt bei jeder Netzwerkanfrage an. Sie wird nur zur Übermittlung der Antwort verwendet und über die normale Verarbeitung der Anfrage hinaus weder protokolliert noch gespeichert.
- **Eine eindeutige Geräte-ID**, die zufällig auf deinem Gerät erzeugt wird. Sie lässt sich weder dir noch dem Eigentümer des Mähers zuordnen. Wir erfassen dazu keine Namen, E-Mail-Adressen oder andere identifizierende Angaben.
- **Die aktuell installierte Betriebssystemversion**, damit der Server feststellen kann, ob eine neuere Version verfügbar ist.

Weitere Daten werden nicht gesendet: keine Standortdaten, keine Nutzungsstatistiken und keine Telemetriedaten darüber, wie du deinen Mäher verwendest.

### Prüfung deaktivieren
Lege auf dem Gerät eine leere Datei unter `/data/openmower/no-update-check` an, zum Beispiel per SSH mit `touch /data/openmower/no-update-check`. Damit wird die tägliche Prüfung deaktiviert. Lösche die Datei, um sie wieder einzuschalten.

## Warum wir diese Daten erfassen
- **IP-Adresse**: Sie ist technisch notwendig, um auf die Anfrage zu antworten, wie bei jedem Server im Internet.
- **Eindeutige Geräte-ID**: Damit können wir ungefähr erkennen, wie viele aktive Installationen es gibt und welche Versionen sie verwenden, ohne einzelne Nutzer zu identifizieren. So beurteilen wir auch, ob eine neue Betriebssystemversion ausgereift genug ist, um sie als aktuelle stabile Version freizugeben. Läuft eine Version eine Zeit lang erfolgreich auf vielen unterschiedlichen Geräten, können wir sie mit mehr Vertrauen allgemein empfehlen, als wenn wir sie direkt am Erscheinungstag zur stabilen Version erklären würden.
- **Betriebssystemversion**: Sie wird benötigt, um festzustellen, ob und welches Update angeboten werden soll.

## Fragen
Wenn du Fragen dazu hast, melde dich über unsere [Community-Kanäle]({{< relref "/community" >}}).
