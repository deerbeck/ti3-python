'''
Aufgabe (csv-Dateien) [8 P]

Nach der Fusion zweier Versandhäuser müssen die Kundendaten dieser zweier 
Firmen verschmolzen werden. In den Dateien firmaA.csv und firmaB.csv sind die 
Kundendaten der beiden Firmen enthalten. Glücklicherweise sind die Daten in beiden Dateien 
im identischen CSV-Format:

            NAME;PLZ

Die Einträge sind zudem alphabetisch nach Namen sortiert. 
Die Dateien beginnen jeweils in der ersten Zeile mit Daten.
Aus den Kundendaten der beiden Firmen soll eine nach Namen sortierte Gesamt-Liste durch die 
Anwendung des Merge-Algorithmus, der im Praktikum vorgestellt wurde, erstellt werden.

Schritte der Implementierung:
• Öffnen Sie beide Dateien mit Hilfe eines Kontextmanagers.
• Speichern Sie die Datensätze der beiden Dateien in Listen zwischen.
• Verschmelzen Sie die Datensätze mit dem Merge-Algorithmus zu einer Gesamt-Liste.
'''


if __name__ == '__main__':
    with open('firmaA.csv', 'r') as f1:
        with open('firmaB.csv', 'r') as f2:
            rows1 = f1.readlines()
            rows2 = f2.readlines()

    rows_all = []
    n1 = len(rows1)
    n2 = len(rows2)
    i1 = 0
    i2 = 0
    name1 = rows1[i1].split(';')[0]
    from1 = False
    while i1 < n1 and i2 < n2:
        if from1:
            name1 = rows1[i1].split(';')[0]
        else:
            name2 = rows2[i2].split(';')[0]
        if name1 <= name2:
            rows_all.append(rows1[i1])
            i1 += 1
            from1 = True
        else:
            rows_all.append(rows2[i2])
            i2 += 1
            from1 = False
    if i1 < n1:
        rows_all += rows1[i1:n1]
    else:
        rows_all += rows2[i2:n2]

    # Nicht erforderlich gemäß Aufgabenstellung
    print(n1, n2, len(rows_all))
    print(rows_all)
