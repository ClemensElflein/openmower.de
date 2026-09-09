---
title: "Kartenposition nach einem Wechsel der Basisstation anpassen"
linkTitle: "Standort der Basisstation ändern"
description: >
  Wenn du die NTRIP-Basisstation versetzt oder zu einem anderen NTRIP-Anbieter wechselst,
  verschiebt sich wahrscheinlich die Position deiner Karte. Der Mäher kann dann nicht mehr
  wie gewohnt eingesetzt werden, da er nicht mehr genau mäht.
---
Mit den DATUM-Feldern OM_DATUM_LAT und OM_DATUM_LONG in der mower_config.txt kannst du die Karte verschieben.

Nach einem Wechsel der NTRIP-Basis passt du die DATUM-Felder in der mower_config.txt an: `OM_DATUM_LAT` für links und rechts,
`OM_DATUM_LONG` für oben und unten. Damit verschiebst du die gesamte Karte in die jeweilige Richtung.

Als festen Bezugspunkt zum Ausrichten der Karte kannst du die Andockposition des Mähers verwenden. Docke den Mäher dafür
über die Bedienelemente zur Flächenerfassung ab, fahre ein Stück umher, damit seine Position genau bestimmt wird,
und docke ihn anschließend mit denselben Bedienelementen manuell wieder an.

Nach dem Andocken siehst du in der Weboberfläche, dass der Mäher etwas neben der Andockposition liegt. Passe die Karte
nun in kleinen Schritten an: `OM_DATUM_LAT` verschiebt sie waagerecht, `OM_DATUM_LONG` senkrecht.
Die Genauigkeit hängt von deinem Standort auf der Erde ab; eine Änderung der siebten Stelle um eins entspricht ungefähr 1 cm.
Wenn du die Karte nach unten verschiebst, wandert die Mäherposition auf der Karte nach oben und umgekehrt.

Vergiss nicht, die exportierten Variablen neu zu laden. Am einfachsten geht das mit einem Neustart des Pi, wenn du etwas Zeit hast.
Fahre anschließend über die Bedienelemente zur Flächenerfassung wieder ein Stück umher und docke erneut manuell an.
So hast du beim Anpassen der Karte einen verlässlichen Bezugspunkt. Wenn alles passt, starte einen Mähvorgang
und schicke den Mäher sofort zur Ladestation zurück. Prüfe, ob er genau und selbstständig korrekt andockt.

Starte dann das Mähen. Der Mäher fährt zuerst den Rand ab, normalerweise in vier Runden. Prüfe besonders die vierte Runde
sorgfältig, da sie am nächsten am Rand liegt. Wenn alles passt, kannst du den Mäher wie gewohnt einsetzen.
