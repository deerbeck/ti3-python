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
    newword = ""
    code = [ord(c)-ord('a') for c in wort]
    newword = [(c + verschiebung) % 26 for c in code]
    output = [chr(c + ord("a")) for c in newword]

    return "".join(output)


if __name__ == "__main__":
    test = caesar("halloz", 4)
    test2 = caesar(test, -4)
    print(test)
    print(test2)