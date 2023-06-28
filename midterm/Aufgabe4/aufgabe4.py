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
def get_alphabet_order(n1, n2):
    if n1 == n2:
        return 0
    else:
        for symbol1,symbol2 in zip(n1,n2):
            if symbol1 < symbol2:
                return 1
            elif symbol1 > symbol2:
                return -1
            



if __name__ == '__main__':
    with open("Aufgabe4/firmaA.csv", "r") as fA:
        with open("Aufgabe4/firmaB.csv","r") as fB:
            companyA = fA.readlines()
            companyB = fB.readlines()

            indxA = 0
            indxB = 0

            newCompany = []
            maxA = len(companyA)
            maxB = len(companyB)

            max = maxA if maxA<maxB else maxB
            while(indxA < max and indxB < max):
                order = get_alphabet_order(companyA[indxA],companyB[indxB])
                if order == 0:
                    newCompany.append(companyA[indxA])
                    indxA += 1
                    indxB += 1
                elif order == 1:
                    newCompany.append(companyA[indxA])
                    indxA += 1
                elif order == -1:
                    newCompany.append(companyB[indxB])
                    indxB +=1
            if indxA == max:
                for man in companyB[indxB:]:
                    newCompany.append(man)
            elif indxB == max:
                for man in companyA[indxA:]:
                    newCompany.append(man)
            with open("Aufgabe4/newCompany.csv","w") as Fnew:
                Fnew.write("".join(newCompany))