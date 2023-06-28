'''
Aufgabe (Rekursion) [4 P]

Ein einfacher Kompressionsalgorithmus reduziert die Anzahl der zu speichernden 
Zeichen eines Strings. So wird der String "aaaabbbcca" auf "a4b3c2a1" komprimiert, 
wobei die Ziffer (1-9) nach einem Zeichen für die Häufigkeit es Zeichens steht.

Implementieren Sie eine rekursive Funktion uncompress_rec(s_comp), 
die aus dem komprimierten String die ursprüngliche Zeichenkette wiederherstellt.
'''


def uncompress_rec(s_comp):
    return s_comp[0]*int(s_comp[1]) if len(s_comp) == 2 else s_comp[0]*int(s_comp[1]) + uncompress_rec(s_comp[2:])

if __name__ == "__main__":
    print(uncompress_rec("a4b3c2a1"))
