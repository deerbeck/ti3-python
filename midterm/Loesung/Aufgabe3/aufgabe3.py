'''
Aufgabe (Caesar-Verschlüsselung) [4 P]

Eine einfache, sehr leicht zu brechende Art der Verschlüsselung 
ist die sogenannte Caesar-Verschlüsselung, bei der die Buchstaben 
um eine gewisse Anzahl (hier als verschiebung bezeichnet) zyklisch verschoben werden.
Hat z.B. die verschiebung den Wert 3, so wird aus
'a' --> 'd'
'b' --> 'e'
...
'z' --> 'c'

Implementieren Sie die Funktion caesar(wort, verschiebung),
die auf die Buchstaben im übergebenen Parameter wort die im Parameter verschiebung 
angegebene zyklische Verschiebung anwendet und das so entstandene Geheimtext-Wort 
als Ergebnis zurückliefert.
Der Einfachheit halber kann man voraussetzen, dass das übergebene wort nur aus Kleinbuchstaben besteht.
'''


def caesar(wort, verschiebung):
    code = [ord(c) - ord('a') for c in wort]
    code_move = [(e + verschiebung) % 26 for e in code]
    ch = [chr(e + ord('a')) for e in code_move]
    word_caesar = ''.join(ch)
    return word_caesar


