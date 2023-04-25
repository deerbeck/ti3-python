<!--- Technische Informatik (FK04)"
Author: Benjamin Kormann			Date: <2022 Feb 03> 
Changes by: Fabian Flohr            Date: <2023 Mar 16> 

--->
<img style="float:right" src="images/hm-logo.png" height="100">  

**TI3-Programmieren: Versuch 03**

Sommersemester 2023 | V 1.0 | Prof. Dr. Fabian Flohr
Original assignments provided by Prof. Dr. Benjamin Korman

***
# Zielsetzung: Umweltdaten systematisch analysieren

In diesem Versuch werden die Vorlesungsinhalte an einem konkreten Umweltbeispiel angewendet. Zur Bewertung der Luftqualität werden verschiedene Luftschadstoffe gemessen und in Bezug auf die gesundheitliche Bedeutung interpretiert. Das Umweltbundesamt beschreibt dies für Stickstoffdioxid in einem [Artikel](https://www.umweltbundesamt.de/themen/luft/luftschadstoffe-im-ueberblick/stickstoffoxide/stickstoffdioxid-gesundheitliche-bedeutung-von#welche-unterschiedlichen-beurteilungswerte-gibt-es-fur-stickstoffdioxid) und geht darin auf die einzuhaltenden Grenzwerte im Innenraum, am Arbeitsplatz und die Außenluft ein. 

Lesen Sie in dem Artikel die Abschnitte *Welche unterschiedlichen Beurteilungswerte gibt es für Stickstoffdioxid?* und *Grenzwerte Stickstoffdioxid* durch, so dass Sie die folgenden Fragen beantworten können:

1. Wie hoch ist der Langzeitgrenzwert für NO<sub>2</sub> für die Außenluft in µg/m<sup>3</sup>?
2. Wie hoch ist der Kurzzeitgrenzwert für NO<sub>2</sub> für die Außenluft im Einstundenmittel µg/m<sup>3</sup>?
3. Wie hoch ist die Alarmschwelle für NO<sub>2</sub> für die Außenluft µg/m<sup>3</sup>?

Über die Internetseite des [Bayerischen Landesamts für Umwelt](https://www.lfu.bayern.de/luft/immissionsmessungen/messwertarchiv/index.htm) können Schadstoffdaten von aufgestellten Umweltmessstationen (Außenluft) abgerufen werden. Das Datenangebot umfasst die Stoffe Stickstoffdioxid, Stickstoffmonoxid, Feinstaub-PM<sub>10</sub>, Feinstaub-PM<sub>2,5</sub>, Ozon, Kohlenmonoxid, BTX (Benzol, Toluol und o-Xylol), Schwefeldioxid und Schwefelwasserstoff. Bei diesem Praktikumsversuch liegt der Fokus auf NO<sub>2</sub> und PM<sub>10</sub>. Aktuelle NO<sub>2</sub> Messwerte der Lothstraße in München mit Einteilung in eine Luftgüteklasse können [online](https://www.lfu.bayern.de/luft/immissionsmessungen/messwerte/stationen/detail/803/172) betrachtet werden.



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
4. Sie haben ausreichend (mehr als 4) **commit Nachrichten** in Git erstellt
5. Der Quelltext besitzt einen **Dokumentationsgrad** von **mindestens 25 %** (Der Dokumentationsgrad bestimmt sich aus der Anzahl der Kommentarzeilen im Quelltext (Zeilen mit #) im Verhältnis zu der Gesamtanzahl Zeilen Quelltext.)

Die Punkte 4) und 5) werden automatisiert ermittelt. Bei dem Gespräch mit dem Praktikumsbetreuer stellen Sie neben Ihrer eigenen Lösung auch die Punkte 4) und 5) eigenständig mit vor.

Mit Hilfe der CI/CD Lösung von GitLab werden mit jedem `git push` automatisch die Testfälle ausgeführt und der Dokumentationsgrad aller .py-Dateien ermittelt. Zum Abrufen der Ergebnisse der ausgeführten Testfälle gehen Sie wie vor im **Abschnitt 3.4.2.2** im Einführungsdokument zu Git beschrieben. 


### WICHTIG

Sie dürfen in diesem Versuch alle Ihnen bislang vermittelten Python-Konstrukte verwenden. Gehen Sie schrittweise vor und überspringen Sie die Aufgaben nicht. Gehen Sie erst zur nächsten Aufgabe weiter, wenn die Funktionalität der zu bearbeitenden Aufgabe erfolgreich abgeschlossen ist.

Die zur Verfügung gestellten Unit Tests helfen Ihnen dabei festzustellen, ob Ihre Lösung richtig ist. Dazu ist es erforderlich, dass Sie sich genau an die vorgegebenen Funktionsnamen halten.

**Ihnen wird vermutlich auffallen, dass die Pipeline für die vorherigen Versuche nicht mehr gestartet werden. Die Pipeline wurde so konfiguriert, dass sie für die bisherigen Praktikumsversuche nur noch gestartet wird, wenn es Änderungen an .py Dateien dieser Versuche gibt. Die Pipeline für diesen Versuch wieder immer ausgeführt.**


# Aufgabenstellung

Das Bayerische Landesamt für Umwelt stellt im Archiv stündliche Messdaten teilweise seit 1980 als Excel-Dokument zur Verfügung. Für die programmatische Verarbeitung der NO<sub>2</sub> und PM<sub>10</sub> Datensätze (2018 bis heute) liegen im Versuchsverzeichnis Ihres GitLab Repositorys bereits in das `csv` (comma-separated-value) Format konvertierte Dateien im `data` Unterverzeichnis vor. Darin sind die 1-Stundenmittelwerte aller Messstationen (u.a. München/Lothstraße) für den jeweiligen Messzeitraum enthalten. 

*Hinweis*: Verwenden Sie für die Versuchsbearbeitung nur die mitgelieferten csv-Dateien. 


## Aufgabe 1: Das Einlesen der Messwerte

Definieren Sie eine Funktion `read_data(location, val_name)`, die die Daten einer Messstation (`location`) aus allen vorhandenen Dateien für einen Schadstoff (`val_name`) einliest und geeignet als Tabelle zur Verfügung stellt. Es gibt verschiedene Möglichkeiten der Repräsentation. So könnte man die Daten als Liste von Dictionaries oder als Dictionary von Listen oder Tupel darstellen. Auch eine Liste von Tupel oder ein Tupel von Tupel wäre möglich. 

**Für diesen Versuch muss ein Dictionary von Listen verwendet werden.**

In der Datei `ass03.py` ist der Rumpf der Funktion `read_data()` bereits gegeben. Fügen Sie darin die folgenden beiden Zeilen hinzu:
```
lfu = lfubay.LfuBay()
data = lfu.metric_data(location, val_name)
```
Nach Aufruf von `metric_data()` befinden sich in `data` alle zum Schadstoff `val_name` der Messstation `location` gehörenden Messdaten. Dabei werden diese Daten in `data` am Beispiel NO<sub>2</sub> für München/Lothstraße wie folgt als Liste von Listen (zweidimensionaler Array) abgelegt:
```
[['01.01.2018', '01:00', 48.0],
 ['01.01.2018', '02:00', 39.0],
 ['01.01.2018', '03:00', 25.0],
....
 ['03.03.2022', '00:00', None]]
```

Die erste Spalte beschreibt das Datum, die zweite Spalte die Uhrzeit (`00:00-23:00`) und die letzte Spalte den Wert als `float` oder `None`, falls kein gültiger Wert erfasst wurde.

Nun müssen die Einträge aus `data` in ein Dictionary überführt werden. Ein Dictionary-Eintrag ermöglicht dabei den Zugriff auf alle Einträge (Zeilen) einer Spalte von `data`. Das Dictionary soll in diesem Teil der Aufgabe die folgenden drei Keys aufweisen: `'date'`, `'time'` und `val_name`. Wobei der dritte Schlüsselname (Key) beliebig gewählt werden kann (siehe Parameter der Funktion). Dieses Dictionary wird im Folgenden Tabelle genannt. 

*Hinweis für Profis*: Es gibt eine nicht ganz einfach verständliche einzeilige Lösung zum Erstellen der Listen eines Directory-Eintrags. 

```
# sample list
m = [[1, 10, 100], [2, 20, 200], [3, 30, 300], [4, 40, 400]]
# unpacking and zipping
mt = list(zip(*m))
# result  
print(mt)
[(1, 2, 3, 4), (10, 20, 30, 40), (100, 200, 300, 400)]
```

Zum Testen rufen Sie im Hauptmodul die `read_data()` Funktion wie folgt auf:
```
if __name__ == '__main__':
	tab_no2 = read_data('München/Lothstraße', 'NO2')
	tab_pm10 = read_data('München/Lothstraße', 'PM10')
```

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Sie können nun die CI/CD Funktionalität zum automatisierten Test Ihrer Aufgabe 1 verwenden. Pushen Sie den aktuellen Stand in GitLab und betrachten Sie die Ergebnisse der Unit Tests in GitLab. Diese sollten grün (erfolgreich) sein.


## Aufgabe 2: Typische Kenndaten der Messungen

Definieren Sie eine Funktion `stats(table, val_name)`, die ein Tupel zurückliefert in dem sich `Anzahl`, `Minimum`, `Maximum` und `Durchschnitt` aller Werte des angegebenen Keys `val_name` der Tabelle table zurückliefert. Sie können davon ausgehen, dass zumindest ein Messwerteintrag vorhanden ist. Die Messwerte liegen entweder als `float` oder `None` vor. Testen Sie diese Funktion mit den Werten aus den zur Verfügung gestellten Dateien. Geben Sie dabei die Ergebnisse geeignet formatiert aus, verwenden Sie dazu die formatierte Ausgabe mit der Methode `format()`. 

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Sie können nun die CI/CD Funktionalität zum automatisierten Test Ihrer Aufgabe 2 verwenden. Pushen Sie den aktuellen Stand in GitLab und betrachten Sie die Ergebnisse der Unit Tests in GitLab. Diese sollten grün (erfolgreich) sein.


## Aufgabe 3: Vorbereitung der Zusammenführung zweiter Messwerttabellen

Definieren Sie die Funktion `add_entry(table, d, t, val_name0, val_name1, val0, val1)`, die die Tabelle `table` um einen Eintrag für den durch `d` und `t` angegebenen Zeitpunkt (Datum/Zeit) und für die Messwerte `val0/val1` mit den Messwertnamen `val_name0/val_name1` ergänzt. Die Funktion dient zum Belegen einer Tabelle mit zwei Messwert Datensätzen (z. B. `val_name0: 'NO2'`, `val_name1: 'PM10'`) für einen angegebenen Zeitpunkt. 

In der Funktion wird nicht überprüft, ob es bereits einen Eintrag für den angegebenen Zeitpunkt gibt, sondern die übergebenen Daten werden einfach an die vorgegebenen Listen (im Dictionary) angehängt.

Testen Sie Ihre Funktion indem folgendes Dictionary 
```
weather = {'date': [], 'time': [], 'temp': [], 'hygro': []}
```
um zwei Datensätze ergänzt wird. Das Dictionary soll danach wie folgt aussehen: 
```
weather = {'date': ['22.11.2019', '23.11.2019'], 'time': ['8:15', '8:15'], 'temp': ['5.5', '6.0'], 'hygro': ['54','65']}
```

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Sie können nun die CI/CD Funktionalität zum automatisierten Test Ihrer Aufgabe 3 verwenden. Pushen Sie den aktuellen Stand in GitLab und betrachten Sie die Ergebnisse der Unit Tests in GitLab. Diese sollten grün (erfolgreich) sein.



## Aufgabe 4: Kennenlernen der Funktion check_time

Die Funktion `check_time(table0, table1, i0, i1)` ist bereits in der Datei `v3_util.py` vorhanden. Sie ermittelt, ob der zum Zeilenindex `i0` von `table0` gehörige Zeitpunkt vor/gleichzeitig/nach dem zum Zeilenindex `i1` von `table1` gehörige Zeitpunkt ist. Die Funktion gibt entsprechend die Werte `-1/0/1` zurück. Ist der Index einer Tabelle ungültig (zu groß) wird der Eintrag der anderen Tabelle als zeitlich davor eingestuft.

Importieren Sie diese Funktion aus `v3_util.py` in Ihr Programm. Testen Sie die Funktion, indem Sie die vorhandenen NO<sub>2</sub> und PM<sub>10</sub> Daten über `read_data()` einlesen (nennen Sie die Schlüssel der Messwerte am besten 'NO2' bzw. 'PM10') und rufen `check_time()` für verschiedene Zeilenkombinationen (verschiedene Werte für die Indizes `i0` und `i1`, die auch außerhalb des gültigen Bereiches liegen können) auf. 
Die zum Testen gewählten Zeilenkombinationen sollten natürlich so gewählt werden, dass man auch alle möglichen Ergebnisse (`-1, 0 oder 1`) erhält. 

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Sie können nun die CI/CD Funktionalität zum automatisierten Test Ihrer Aufgabe 4 verwenden. Pushen Sie den aktuellen Stand in GitLab und betrachten Sie die Ergebnisse der Unit Tests in GitLab. Diese sollten grün (erfolgreich) sein.




## Aufgabe 5: Zusammenführen beider Messungen zu einer Tabelle

Definieren Sie eine Funktion `merge(data0, data1)`, die zwei eingelesene Tabellen (Dictionaries) akzeptiert, in eine gemeinsame Tabelle (neues Dictionary) kombiniert und als Funktionswerte an den Aufrufer zurückgibt. Es kann davon ausgegangen werden, dass die Tabellen nach der Messungszeit sortiert sind und pro Tabelle (neben Zeitpunkt der Messung) nur ein Messwert enthalten ist. In der kombinierten Tabelle sollen Messwerte, die zur selben Zeit gehören, in derselben Zeile erscheinen. Liegt für einen Zeitpunkt ein Messwert nicht vor, soll in die Tabelle stattdessen `None` eingetragen werden. Die neue Tabelle soll dabei zeitlich sortiert bleiben. 

Die verschmolzene Tabelle sollte anschließend wie folgt aussehen:

```
merged = {
  `date`= ['01.01.2018', '01.01.2018', '01.01.2018', ..., '03.03.2022'],
  `time`= [     '01:00',      '02:00',      '03:00', ...,      '00:00'],
  `NO2` = [        48.0,         39.0,         25.0, ...,         None],
  `PM10`= [       561.0,        174.0,         61.0, ...,         None]
}
```

**Vorgehensweise zur Umsetzung:**

- Nutzen Sie die Funktionen `check_time()` und `add_entry()`. 
- Schaffen Sie es, die frei gewählten Messwertnamen (Schlüssel im Dictionary) aus der Tabelle zu extrahieren und nicht vorgeben zu müssen?
*Hinweis*: Verwenden Sie dazu die Mengenoperationen, die Sie für `set`-Objekte kennengelernt haben. Die Schlüsselnamen `'date'` und `'time'` wurden, wie Sie bereits wissen, als unveränderlich festgelegt. 
- Der **klassische Merge-Algorithmus** zweier Tabellen nutzt zwei Indizes `curr_ndx0` und `curr_ndx1` mit deren Hilfe man die Tabellen durchforstet. Er läuft wie folgt ab: 
	- Es werden zwei Indizes `curr_ndx0` und `curr_ndx1` verwendet. Damit merkt man sich die Position des nächsten einzufügenden Eintrags aus Tabelle `data0` bzw. `data1`. 
	- Solange (`while`-Schleife) in beiden Tabellen noch Einträge vorhanden sind, die noch eingefügt werden müssen, wählt man immer den zeitlich kleineren Eintrag, fügt diesen in die neue Tabelle ein und erhöht `curr_ndx0` oder `curr_ndx1` entsprechend. 
	- Sind die Einträge aus den beiden Tabellen zeitgleich, fügt man die Messwerte aus beiden Tabellen zu diesem gleichen Zeitpunkt in die neue Tabelle ein und erhöht beide Indizes. 
	- Nach Beendigung der `while`-Schleife sind noch die restlichen Elemente der Tabelle, die noch Datensätze besitzen, anzufügen.
*Für Profis*: Sie können die noch fehlenden Einträge der anderen Tabelle auf einen Schlag ohne Schleife anfügen. 
- Testen Sie diese Funktion mit den über `read_data()` eingelesenen NO<sub>2</sub> und PM<sub>10</sub> 

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.


## Aufgabe 6: NO2 Grenzwerte auswerten sowie auf Konsole und in Datei ausgeben

Die Funktion `stats()` nutzt alle in der Tabelle abgelegten Datensätze verwendet. Für eine Auswertung der Einhaltung oder Überschreitung der Grenzwerte gemäß Umweltbundesamt, müssen jedoch die Jahreswerte berücksichtigt werden. 

Dazu muss die vorgegebene Funktion `no2_stats()` mit dem NO<sub>2</sub> Dictionary und die jeweilige Jahreszahl (2018, 2019, 2020, 2021) aufgerufen werden. Die Rückgabe der Funktion ist ein Tupel mit den Werten (`jährlicher Durchschnittswert`, `Anzahl Verletzungen Einstundenmittel`, `Anzahl Verletzungen 3 Einstundenmittel`, `Minimumwert`, `Maximumwert`).

Ergänzen Sie Ihr Programm, so dass für die vier Jahre (2018 bis 2021) die NO<sub>2</sub> Statistik berechnet und das Ergebnis wie folgt auf der Konsole ausgegeben wird:
```
2018: (27.352, 0, 0, 3.0, 148.0)
2019: (26.640, 0, 0, 3.0, 133.0)
2020: (23.131, 0, 0, 3.0, 144.0)
2021: (21.244, 0, 0, 3.0, 110.0)
```

Die Ergebnisse sollen nun noch in eine `csv` Datei mit dem Namen `Auswertung_NO2_München_Lothstraße_2018-2021.csv` geschrieben werden. Die Datei nutzt ein Semikolon (`;`) als Trennzeichen zwischen Spalteneinträgen in einer Zeile. Üblicherweise enthält die erste Zeile eine Überschrift der jeweiligen Spalten. Anschließend werden die Datensätze zeilenweise der Datei angefügt. Bedenken Sie, dass Sie am Ende einer jeden geschriebenen Zeile einen Zeilenumbruch benötigen. Recherchieren Sie dazu die Funktion `write()`. Die ermittelten NO<sub>2</sub> Daten müssen demnach wie folgt in die Datei geschrieben werden:

```
Jahr;Jährlicher Durchschnitt;Verletzungen Einstundenmittel;Verletzungen 3 Einstundenmittel;Minimum;Maximum
2018;27.352;0;0;3.0;148.0
2019;26.640;0;0;3.0;133.0
2020;23.131;0;0;3.0;144.0
2021;21.244;0;0;3.0;110.0
```

Sie können diese Datei nun bspw. mit Excel öffnen.

**Aufgabe:** Diskutieren Sie die Ergebnisse der NO<sub>2</sub> Schadstoffauswertung mit Ihrem Praktkikumsbetreuer.

> Nach Abschluss fügen Sie alle Änderungen dem Git Repository hinzu und versehen die Änderungen mit einer **aussagekräftigen** commit Nachricht.

> Übertragen Sie jetzt final alle Änderungen auch in GitLab (push). Es müssen nun alle Tests aus den Versuchen erfolgreich durchlaufen.

## Aufgabe 7 (freiwillig): Experimentieren mit den Umweltdaten

Sie haben nun zahlreiche Möglichkeiten, weitere Umweltanalysen durchzuführen.

### Aufgabe 7.1 (freiwillig): Erweiterung des Datensatzes

In der ausgelieferten lfubay.by Datei ist eine weitere Funktionalität enthalten, die Schadstoffmessdaten automatisiert herunterlädt und in das `csv` Format konvertiert. Durch den Aufruf von `download_data()` können die Daten geladen werden. Bei einem Rückgabewort `0` war der Download und das Konvertieren erfolgreich. Die Dateien werden automatisch in dem Verzeichnis `data` abgelegt.
```
if __name__ == '__main__':
	lfu = lfubay.LfuBay()
	success = download_data('NO2', 2010, end=2022)
```

Nun können Sie die Auswertungen auf den vergrößerten Datensatz anwenden.

*Hinweis*: Das Herunterladen und Konvertieren kann je nach Menge der Datensätze einige Zeit in Anspruch nehmen. Brechen Sie deshalb den prozess nicht ab. Sobald eine Datei einmal auf den Rechner geladen wurde, wird diese nicht erneut geladen.

### Aufgabe 7.2 (freiwillig): Auswerten anderer Messstationen

Bislang wurden die Auswertungen für München/Lothstraße durchgeführt. Die Messdaten des Landesamts für Umwelt enthalten jedoch noch weitere Messstationen. Öffnen Sie bspw. die Datei `NO2_2002_01.csv` und betrachten Sie Spaltennamen in der ersten Zeile. Darin finden Sie weitere Einträge wie: `Regensburg/Rathaus`, `Ingolstadt/Münchener Straße` oder `Andechs/Rothenfeld`. 

Ersetzen Sie beim Einlesen der Daten im Aufruf von `read_data()` die `location` auf die jeweilige Messstation und führen Sie damit die Analysen durch.

### Aufgabe 7.3 (freiwillig): Statistik über PM10

Erweitern Sie analog zur vorgegebenen `no2_stats()` Funktion Ihren Quelltext um eine `pm10_stats()` Funktion und berechnen Sie die Einhaltung bzw. Verletzung der Grenzwerte für PM<sub>10</sub>. Als Ausgangspunkt für die Recherche der Grenzwerte bieten sich die Informationsseiten des [Umweltbundesamtes](https://www.umweltbundesamt.de/themen/luft/luftschadstoffe-im-ueberblick/feinstaub) an.
 