<img style="float:right" src="images/hm-logo.png" height="100">  

**TI3-Programmieren: Versuch 05**

Sommersemester 2023 | V 1.0 | Prof. Dr. Fabian Flohr

***
# Zielsetzung: Planung und Umsetzung eines Objektverwaltungssystem
In diesem Versuch sind sie nicht nur der Entwickler sondern auch Systemarchitekt und Stakeholder. Aufgabe ist es, ein Objektverwaltungssystem zu entwickeln, das es Benutzern ermöglicht, verschiedene Objekte zu erfassen, zu speichern, zu bearbeiten und abzurufen. Sie dürfen frei entscheiden welche Art von Objektverwaltung sie realisieren. 
Unten finden Sie einige Vorschläge. Bitte beachten Sie bei der Umsetzung die Randbedingungen und Anforderungen im Kapitel **Aufgebenstellung**. Diese werden bei der Abnahme durch den Praktikumsbetreuer geprüft.

## Allgemeine Hinweise

Bevor Sie mit der Bearbeitung dieses Versuchs starten lesen Sie bitte die allgemeinen Hinweise auf der ersten Seite genau durch.

### Verwendung von CI/CD

Für die Bearbeitung des Praktikumsversuchs wird Ihnen neben der Versionsverwaltung Git die sog. Continuous Integration (CI) Funktionalität von GitLab zur Verfügung gestellt. Diese bewirkt, dass Sie ihren entwickelten Softwarestand in Ihr eigenes Repository in GitLab pushen können und anschließend werden automatisiert Tests auf Ihren Quelltext ausgeführt. Darüber haben Sie die Möglichkeit, selbst festzustellen, ob Ihre Implementierung noch grundlegende Fehler enthält. Wichtig dabei zu wissen ist, dass erfolgreiche Tests noch keine Garantie dafür sind, dass Ihr Programm am Ende keine Fehler enthält. Aber es werden grundsätzliche Aspekte geprüft. Hierzu wird empfohlen, dass Sie in dem PDF-Dokument *Einführung in das Versionsverwaltungssystem Git und das LRZ GitLab* die Abschnitte 3.4.2 vollständig lesen.

### Abgabe des Versuchs

Jeder Praktikumsteilnehmer muss den eigenen Versuch beim jeweiligen Praktikumsbetreuer vorstellen und Fragen zu der Lösung beantworten. Dabei ist es auch wichtig, dass *Ihre eigene Lösung in Ihrem eigenen Git Repository in GitLab* (`git push`) vorhanden ist.

### Abnahmekriterien

Bei der Abgabe werden die Praktikumsbetreuer nicht nur auf die Funktionalität, sprich das zu erreichende Ergebnis achten. Die erfolgreiche Abgabe unterliegt den folgenden Kriterien:
1. **Aufgabenstellung** ist funktional **erfüllt** und alle untern genannten **Anforderungen** und **Konzepte** sind umgesetzt.
2. Die von Ihnen selbst erstellten **Testfälle** laufen alle **erfolgreich** durch
3. **Fragen** zur Lösung und zu Konzepten in Python **müssen beantwortet werden**
4. Sie haben ausreichend (mehr als 4) **commit Nachrichten** in Git erstellt
5. Der Quelltext besitzt einen **Dokumentationsgrad** von **mindestens 25 %** (Der Dokumentationsgrad bestimmt sich aus der Anzahl der Kommentarzeilen im Quelltext (Zeilen mit #) im Verhältnis zu der Gesamtanzahl Zeilen Quelltext.)

Die Punkte 4) und 5) werden automatisiert ermittelt. Bei dem Gespräch mit dem Praktikumsbetreuer stellen Sie neben Ihrer eigenen Lösung auch die Punkte 4) und 5) eigenständig mit vor.

### WICHTIG

Sie dürfen in diesem Versuch alle Ihnen bislang vermittelten Python-Konstrukte verwenden. Die Abnahme erfolgt anhand der Anforderungen und geförderten Rahmenbedingungen im Kapitel **Aufgabenstellung**.

**Ihnen wird vermutlich auffallen, dass die Pipeline für die vorherigen Versuche nicht mehr gestartet werden. Die Pipeline wurde so konfiguriert, dass sie für die bisherigen Praktikumsversuche nur noch gestartet wird, wenn es Änderungen an .py Dateien dieser Versuche gibt. Die Pipeline für diesen Versuch soll immer ausgeführt werden.**


# Aufgabenstellung

Das Objektverwaltungssystem sollte **folgende Anforderungen** erfüllen:

1. Benutzereingabe: Das System sollte die Benutzereingabe zur Erfassung von Objektdaten ermöglichen. Dabei sollten relevante Informationen wie e.g. Name, Beschreibung, Kategorie und Wert des Objekts erfasst werden.

2. Speicherung der Objekte: Implementieren Sie eine Datenstruktur, um die erfassten Objekte effizient zu speichern. Sie können hierfür zum Beispiel eine Liste, ein Array oder eine Datenbank verwenden.

3. Bearbeitung von Objekten: Das System sollte Funktionen bereitstellen, um gespeicherte Objekte zu bearbeiten. Der Benutzer sollte in der Lage sein, Objekte anhand ihrer eindeutigen Kennungen zu suchen und ihre Eigenschaften zu aktualisieren.

4. Abfrage von Objekten: Implementieren Sie geeignete Funktionen, um gespeicherte Objekte abzurufen, anzuzeigen und zu visualisiern. Der Benutzer sollte die Möglichkeit haben, Objekte anhand verschiedener Kriterien wie Kategorie, Name oder Wert zu suchen und die entsprechenden Informationen zu erhalten.

5. Benutzerfreundliche Benutzeroberfläche: Gestalten Sie eine benutzerfreundliche Benutzeroberfläche, die dem Benutzer ermöglicht, das Objektverwaltungssystem einfach zu bedienen. Verwenden Sie hierfür eine geeignete Eingabeaufforderungen. Optional: Umsetzung mit grafischer GUI (zB Tkinter)

6. Fehlerbehandlung: Implementieren Sie eine angemessene Fehlerbehandlung, um Benutzereingaben zu validieren und Fehlerfälle abzufangen. Das System sollte den Benutzer über etwaige Fehler informieren und ihm klare Anweisungen zur Fehlerbehebung geben.

7. Testen und Dokumentation: Testen Sie das entwickelte Objektverwaltungssystem gründlich, um sicherzustellen, dass es korrekt funktioniert. Dokumentieren Sie die aktuelle Funktionsweise und Einschränkungen.


Zeichen Sie zunächst bitte zunächt ein **UML-Klassendiagramm** in welchem Sie die wesentlichen Klassen, Attribute, Methoden und deren Zusammenhänge aufführen.
Es ist nicht nötig eine vollumfängliche Lösung zu entwickeln, die für alle Fälle funktioniert. Versuchen Sie aber die **aktuellen Funktionen und Einschränkungen Ihrer Lösung zu dokumentieren**.

Die Lösung soll **objektorientiert** in Python implementiert werden.
Folgende **Konzepte der Objektorientierung** müssen in Ihrem Klassendiagramm sowie in Ihrer Implementierung eine *sinnvolle* Anwendung finden:
- Abstrakte Klasse
- Statische Funktionen und Parameter
- Kapselung und Zugriff (private and protected)
- Vererbung
- Polymorphismus
- Komposition

Weiter sollen folgende **Konzepte**  *sinnvoll*  eingesetzt werden:
- Logging-Mechanismen: Verwenden Sie das Logging-Paket und nutzen Sie verschiedene Logging-Konfigurationen um Logging-Ausgaben in der Entwicklungszeit zum Debuggen und zur
- Fehlerbehandlung mit Exceptions: Fangen Sie kritische Fehler mit Exceptions ab. Das Programm sollte nicht abstürzen sondern eine sinnvolle Fehlermeldung ausgeben.
- Visualisierung mit matplotlib: Visualisieren Sie den Bestand, Preise etc. grafisch.
- Persistenz mit JSON oder Datenbank (e.g. sqllite): Verwenden Sie entweder JSON oder eine Datenbank um die verwalteten Objekte persistent zu speichern und wieder zu laden,

Bitte schreiben Sie selbst mindestns **sechs sinnvolle Unit-Tests** um Ihre Implementierung zu testen. Die bestandenen Test-Cases führen Sie dann bitte auch in Gitlab vor. Hierfür passen Sie dann bitte die **CI/CD Pipeline** individuell anpassen.

Befüllen Sie Ihre Objektverwaltung mit genügend **sinnvollen Datensätzen** um die Verwaltung testen zu können.


## Ideen für eine Objektverwaltungssystem

### Automarkt
Story: Als Manager eines Autohändlers möchte ich den Überblick über meinen Fahrzeugbestand in meinem Automarkt behalten.
- Spezifikation (Beispiel)
  - "Car"-Klasse mit Attributen wie Hersteller, Modell und Baujahr etc.. Methoden zum Abrufen und Festlegen der Eigenschaften des Autos.
  - "Car"-Klasse wird an weitere spezifischere Modelltypen (z.B. Minis, Kleinwagen, Kompaktwagen, 	Mittelklasse, Oberklasse, SUVs, Geländewagen, Vans und Minivans) vererbt
  - "Besitzer"-Klasse mit Kontaktdaten. Ein Auto hat 0 (Neuwagen),1 oder mehrere Vorbesitzer.
  - "CarMarket"-Klasse, welche eine Sammlung von Auto-Objekten verwaltet. 
  - Methoden zum Hinzufügen, Entfernen und Suchen von Autos im Automarkt.
  - GUI- / Terminal-Programm, das dem Benutzer ermöglicht, interaktiv die Marktverwaltung durchzuführen.
  - Laden und Speichern der Autos über ein JSON-File
  - Plotting der verfügbaren Autos im Markt (e.g. Bar-Plot, Tortendiagramm etc.) anhand Hersteller, Modell, Vorbesitzer und Baujahr etc.


### Banksystem
Story: Als Bankkunde möchte ich meine Bankkonten verwalten.
- Spezifikation (Beispiel)
  - "Bankkonto"-KLasse mit Attributen wie Kontonummer, Kontostand und Inhaber.
  - Verschiedene Kontotypen: "Girokonto", "Businesskonto" etc.
  - Implementiere Methoden zum Einzahlen, Abheben und Anzeigen des Kontostands.
  - Wende Kapselung an, um den Kontostand vor direkten Änderungen zu schützen.
  - "Kunde" mit Attributen wie Name und Kontaktdaten. Kunde besitzt 1 oder mehrere Kontos (Inhaber).
  - "Bank", die eine Sammlung von Bankkonto-Objekten mit zugehörigen Kundendaten verwaltet.
  - Methoden zum Hinzufügen von Konten, Durchführen von Transaktionen und Anzeigen von Kundendaten.
  - GUI- / Terminal-Programm, das dem Benutzer ermöglicht, interaktiv die Bank zu verwalten.
  - Laden und Speichern der Bankdaten über ein JSON-File bzw. Datenbankanbindung
  - Plotting der Bankdaten (e.g. Bar-Plot, Tortendiagramm etc.) anhand Nutzer, Bankkontotyp, Statistiken über Kontostände etc.


### Raumverwaltungssystem
Story: Als Veranstaltungsmanager möchte ich eine Anwendung zur Verwaltung der Räume in meinem Veranstaltungsort entwickeln, um eine reibungslose Buchung und Verwaltung der Räume zu gewährleisten.
- Spezifikation (Beispiel)
  - "Raum"-Klasse mit Attributen wie Raumnummer, Kapazität und Verfügbarkeit.
  - Subtypen wie "Meetingraum", "Abstellraum", "Vorlesungsraum" etc.
  - Implementiere Methoden zum Hinzufügen, Entfernen und Anzeigen von Rauminformationen sowie zur Überprüfung der Verfügbarkeit.
  - Erstelle eine Klasse namens "Raumverwaltung", die eine Sammlung von Raumobjekten verwaltet.
  - Implementiere Methoden zum Hinzufügen, Entfernen und Suchen von Räumen.
  - Implementiere Methoden zur Buchung und Freigabe von Räumen.
  - "Kunde" mit Attributen wie Name und Kontaktdaten. Kunde kann 0,1 oder mehrere Räume buchen.
  - GUI- / Terminal-Programm, das dem Benutzer ermöglicht, interaktiv die Raumverwaltung durchzuführen.
  - Laden und Speichern der Raumdaten über ein JSON-File bzw. Datenbankanbindung
  - Plotting der Raumdaten (e.g. Bar-Plot, Tortendiagramm etc.) anhand Buchung, Raumtyp, Verfügbarkeit etc.