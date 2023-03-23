<!--- Technische Informatik (FK04)"
Author: Benjamin Kormann			Date: <2022 Feb 03> 
Changes by: Fabian Flohr            Date: <2023 Mar 16> 

--->
<img style="float:right" src="images/hm-logo.png" height="100">  

**TI3-Programmieren: Versuch 01**

Sommersemester 2023 | V 1.0 | Prof. Dr. Fabian Flohr
Original assignments provided by Prof. Dr. Benjamin Korman

***
# Zielsetzung: Slicing und List Comprehension

In diesem Versuch ist es das Ziel, Slicing und List Comprehension einzuüben.



## Allgemeine Hinweise

Bevor Sie mit der Bearbeitung dieses Versuchs starten lesen Sie bitte die allgemeinen Hinweise auf der ersten Seite genau durch.

### Verwendung von CI/CD

Für die Bearbeitung des Praktikumsversuchs wird Ihnen neben der Versionsverwaltung Git die sog. Continuous Integration (CI) Funktionalität von GitLab zur Verfügung gestellt. Diese bewirkt, dass Sie ihren entwickelten Softwarestand in Ihr eigenes Repository in GitLab pushen können und anschließend werden automatisiert Tests auf Ihren Quelltext ausgeführt. Darüber haben Sie die Möglichkeit, selbst festzustellen, ob Ihre Implementierung noch grundlegende Fehler enthält. Wichtig dabei zu wissen ist, dass erfolgreiche Tests noch keine Garantie dafür sind, dass Ihr Programm am Ende keine Fehler enthält. Aber es werden grundsätzliche Aspekte geprüft. Hierzu wird empfohlen, dass Sie in dem PDF-Dokument *Einführung in das Versionsverwaltungssystem Git und das LRZ GitLab* die Abschnitte 3.4.2 vollständig lesen.

### Abgabe des Versuchs

Jeder Praktikumsteilnehmer muss den eigenen Versuch beim jeweiligen Praktikumsbetreuer vorstellen und Fragen zu der Lösung beantworten. Dabei ist es auch wichtig, dass *Ihre eigene Lösung in Ihrem eigenen Git Repository in GitLab* (`git push`) vorhanden ist.

### Abnahmekriterien

Bei der Abgabe werden die Praktikumsbetreuer nicht nur auf die Funktionalität, sprich das zu erreichende Ergebnis achten. Die erfolgreiche Abgabe unterliegt den folgenden Kriterien:
1. **Aufgabenstellung** ist funktional **erfüllt**
2. Die **Testfälle** laufen alle **erfolgreich** durch
3. **Fragen** zur Lösung und zu Konzepten in Python **müssen beantwortet werden**
4. Sie haben ausreichend (mehr als 5) **commit Nachrichten** in Git pro Praktikumsaufgabe erstellt. Achtung: es zählen nur die Commits in den jeweiligen Aufgabenordnern.
5. Der Quelltext besitzt einen **Dokumentationsgrad** von **mindestens 25 %** (Der Dokumentationsgrad bestimmt sich aus der Anzahl der Kommentarzeilen im Quelltext (Zeilen mit #) im Verhältnis zu der Gesamtanzahl Zeilen Quelltext.)

Die Punkte 2), 4) und 5) werden automatisiert ermittelt. Bei dem Gespräch mit dem Praktikumsbetreuer stellen Sie neben Ihrer eigenen Lösung auch die Punkte 4) und 5) eigenständig mit vor.

Mit Hilfe der CI/CD Lösung von GitLab werden mit jedem `git push` automatisch die Testfälle ausgeführt und der Dokumentationsgrad aller .py-Dateien ermittelt. Zum Abrufen der Ergebnisse der ausgeführten Testfälle gehen Sie wie vor im **Abschnitt 3.4.2.2** im Einführungsdokument zu Git beschrieben. Für die Bewertung des Dokumentationsgrads wird das Tool `radon` (Sie müssen dieses Tool nicht installieren. Es ist in GitLab hinterlegt. Quelle: https://pypi.org/project/radon) verwendet, welches das Ergebnis als Artefakt der CI/CD-Pipeline zur Verfügung stellt. Lesen Sie dazu auch den **Abschnitt 3.4.2.3** im Einführungsdokument zu Git. 

### WICHTIG

Für die Bearbeitung dieses Versuchs dürfen Sie ausschließlich List Comprehensions und Slicing verwenden. Schleifen (`for`, `while`) bzw. Bedingungen (`if`) als Konstrukte der Ablaufsteuerung sind nicht erlaubt. Die eingereichte Lösung wird nur akzeptiert, wenn Sie vollständig auf Konstrukte der Ablaufsteuerung verzichten. 

**Die zur Verfügung gestellten Unit Tests helfen Ihnen dabei festzustellen, ob Ihre Lösung richtig ist. Dazu ist es erforderlich, dass Sie sich genau an die vorgegebenen Variablennamen halten.**



# Aufgabenstellung

Der erste Versuch nutzt eine Verschlüsselungstechnologie zur Wiederherstellung eines geheimen Textes.


## Aufgabe 1: Verschlüsselung

Für die Bearbeitung der Aufgabe 1 nutzen Sie die Datei `ass01_1.py`.

Gegeben ist ein Text, der in der Datei `text_assignment01.txt` gespeichert vorliegt. Sie können diese Datei in Ihrem Programm mit Hilfe der folgenden Zeile laden:
```
text = open(‘text_assignment01.txt‘, ‘r‘).readlines()
```
Die Funktion `open()` öffnet die Textdatei und stellt ein Datei-Objekt zur Verfügung. Die Methode `readlines()` liefert eine Liste aller Textzeilen als Liste von Strings. Der Text enthält ein geheimes Codewort. Um es zu extrahieren, gehen Sie wie folgt vor:

- Der Code setzt sich zusammen aus dem dritten Zeichen (Index: 2) der sechsten Zeile (Index: 5), dem 27.-29. Zeichen der dritten Zeile, den ersten drei Zeichen der zweiten Zeile und den ersten drei Zeichen der letzten Zeile. Legen Sie das Ergebnis in der Variable `temp_code` ab. Nutzen Sie zur Ermittlung auch Slices.
- Invertieren Sie nun die Reihenfolge und hängen Sie die sich ergebenden Zeichen fünfmal hintereinander. Schneiden Sie die letzten beiden Zeichen ab. Betrachten Sie aus diesem Wort jedes achte Zeichen, beginnend mit dem neunten Zeichen (Index: 8). Legen Sie das Ergebnis in der Variable `codeword` ab.
- Schreiben Sie die Extraktion des Codeworts aus dem `temp_code` in einer Python Zeile.

*Hinweis*: Quelltextzeilen wie die bislang umgesetzten erschweren die nachträgliche Lesbarkeit, sofern diese ohne Quelltextkommentare programmiert wurden. Ergänzen Sie den Quelltext um einsprechende Kommentare, so dass Sie auch selbst Ihren eigenen Quelltext nach Wochen wieder verstehen können.

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Sie können nun die CI/CD Funktionalität zum automatisierten Test Ihrer Aufgabe 1 verwenden. Pushen Sie den aktuellen Stand in GitLab und betrachten Sie die Ergebnisse der Unit Tests in GitLab. Diese sollten grün (erfolgreich) sein.


## Aufgabe 2: Die Entschlüsselung der Botschaft

Für die Bearbeitung der Aufgabe 2 nutzen Sie die Datei `ass01_2.py`.

### Grundlagen

Das Codewort können wir für die Ver- und Entschlüsselung von Daten nutzen. Eine einfache (zwar sehr unsichere) Möglichkeit ist es, den Buchstaben Zahlen zuzuordnen. Wir wählen `‘A‘->0`, `‘B‘->1` etc. Die Verschlüsselung ergibt sich durch ein `xor` zwischen Botschaftszeichen und Codewort, dabei werden die Codezeichnen durchgewechselt, also z.B. für die Botschaft ‘ABCDE‘, Code: ‘FG‘:
```
'A' xor 'F' --> 0 xor 5 = 5 	= 'F'
'B' xor 'G' --> 1 xor 6 = 7 	= 'H'
'C' xor 'F' --> 2 xor 5 = 7 	= 'H'  etc.
```
Das Entschlüsseln kann mit genau demselben Verfahren erfolgen:
```
'F' xor 'F' --> 5 xor 5 = 0	= 'A'
'H' xor 'G' --> 7 xor 6 = 1	= 'B'
'H' xor 'F' --> 7 xor 5 = 2	= 'C'  etc.
```

### Einzeichencode

Wir nähern uns der Aufgabe schrittweise und betrachten zunächst einen aus einem Zeichen bestehenden Code. Die zugehörige Nummer eines Buchstabens `ch` erhalten Sie mit Hilfe `ord(ch)-65`, der Buchstabe zur Nummer `nb` ergibt sich aus `chr(nb+65)`. Recherchieren Sie die Funktionen `ord()` und `chr()`. Testen Sie z.B. `ord(‘D‘)`.

Entschlüsseln Sie die Botschaft `‘RTFVQXSSE‘` (Variablenname: `message1`) mit dem Code `‘X‘` (Variablenname: `code1`). Gehen Sie zur Bearbeitung schrittweise vor:

- Weisen Sie den Variablen `code1` und `message1` die entsprechenden Strings zu.
- Ermitteln Sie nun die Variable `code1_val` und `message1_val`. Die Variable `code1_val` soll den zum Codezeichen gehörigen Zahlencode, `message1_val` eine Liste der zu den Buchstaben gehörenden Zahlencodes enthalten. Für die Botschaft `‘ABC‘` und den Code `‘F‘` sollte `code1_val 5` und `message1_val [0,1,2]` sein.
- Ermitteln Sie die Liste der entschlüsselten Zahlencodes in `result1_val`. Für die Botschaft `‘ABC‘` und den Code `‘F‘` sollte `result1_val [5,4,7]` sein. 
*Hinweis*: Die Variable `result1_val` soll keine Buchstaben enthalten.
- Weisen Sie der Variablen `result1` den sich ergebenden String zu. 
*Hinweis*: Durch `‘‘.join([‘A‘, ‘B‘, ‘C‘])` kann eine Liste von Strings zu einem String `‘ABC‘` kombiniert werden.

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Sie können nun die CI/CD Funktionalität zum automatisierten Test Ihrer Aufgabe 2 verwenden. Pushen Sie den aktuellen Stand in GitLab und betrachten Sie die Ergebnisse der Unit Tests in GitLab. Diese sollten grün (erfolgreich) sein.

## Aufgabe 3: Allgemeiner Code

Für die Bearbeitung der Aufgabe 3 nutzen Sie die Datei `ass01_3.py`.

Entschlüsseln Sie die Botschaft `‘SLCVZCILAG‘` (Variablenname: `message`) mit dem von Ihnen gefundenen Code aus Aufgabe 1 mit Hilfe einer Zeile Python-Quelltext. Hierzu erweitern Sie das in Aufgabe 1 erstellte Programm um allgemeine Codes.
*Hinweis*: Fügen Sie den vollständigen Code aus Ausgabe 1 (`ass01_1.py`) in die Datei `ass01_3.py` ein. **Nutzen Sie dafür nicht die import Anweisung.**

Gehen Sie wieder schrittweise vor:

- Definieren Sie eine Variable `code_long`, die den Code entsprechend der Länge der Botschaft verlängert. Für die Botschaft `‘ABCDE‘` und den Code `‘FG‘` sollten Sie ein `code_long` mit dem Wert `‘FGFGF‘` erhalten. Die Berechnung soll unabhängig von der Länge der Botschaft und des Codes funktionieren.
- Modifizieren Sie die Berechnung von `code1_val`, so dass Sie `code_long` nutzt und das Ergebnis in `code_val` ablegt.
- Legen Sie die Ganzzahlen der Entschlüsselung in der Variable `result_val` ab. Nutzen Sie dazu die Vorgehensweise aus Aufgabe 2.
- Ermitteln Sie den entschlüsselten String, legen diesen in der Variablen `result` ab und geben Sie ihn auf der Konsole aus.
*Hinweis*: Nutzen Sie die `zip()`-Funktion.

Prüfen Sie abschließend nochmal die Menge Ihrer Quelltextkommentare und ergänzen Sie diese ggf., so dass Sie den Quelltext bei erneuter Betrachtung leichter verstehen können. 

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Sie können nun die CI/CD Funktionalität zum automatisierten Test Ihrer Aufgabe 3 verwenden. Pushen Sie den aktuellen Stand in GitLab und betrachten Sie die Ergebnisse der Unit Tests in GitLab. Diese sollten grün (erfolgreich) sein.
