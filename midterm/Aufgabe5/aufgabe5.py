'''
Aufgabe (Kontextmanager) [10 P]

Zur einfachen Performancemessung eines Algorithmus kann 
der Kontextmanager von Python verwendet werden.

|-------------------------------------------------------|
|                        MyTimer                        |
|-------------------------------------------------------|
| -title: str                                           |
| -start: float                                         |
| -end: float                                           |
|-------------------------------------------------------|
| +MyTimer(title_: str)                                 |
| +__enter__(self): MyTimer                             |
| +__exit__(self, exc_type, exc_value, traceback): void |
|-------------------------------------------------------|

Implementieren Sie dazu die Klasse MyTimer gemäß dem oben angegebenen UML Klassendiagramm. 
Realisieren Sie die beiden Methoden __enter__() und __exit__(), so dass beim Eintritt des 
Kontextmanagers (enter) die Zeit gestartet, beim Verlassen (exit) die Zeit gestoppt und 
die vergangene Zeit (end-start) auf der Konsole ausgegeben wird. 
Der Parameter title des Konstruktors soll bei der Ausgabe in __exit__() als Erstes ausgegeben werden.

Hinweise: Die Parameter der Methode __exit__() müssen bei der Implementierung zwar 
in der Signatur angegeben, jedoch können diese bei der Methodenimplementierung 
ignoriert werden. Die Funktion time() des Moduls time liefert die vom Zeitpunkt des 
Aufrufs vergangenen Sekunden seit dem 01.01.1970 um 00:00:00 Uhr als float Wert zurück.
'''

from time import time


class MyTimer:
    pass
