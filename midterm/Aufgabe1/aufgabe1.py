'''
Aufgabe (List Comprehension, Periodensystem) [4 P]

Gegeben ist ein Ausschnitt aus dem Periodensystem der Elemente als Liste 
von Listen in der Variablen psystem. In der zweiten Spalte werden 
die Erdalkalimetalle geführt. 

Erzeugen Sie eine Liste, die alle Erdalkalimetalle beinhaltet und 
deren Kurzbezeichnung auf den Buchstaben 'a' enden.

psystem = [["H", "", ""], 
           ["Li", "Be", ""], 
           ["Na", "Mg", ""], 
           ["K", "Ca", "Sc"], 
           ["Rb", "Sr", "Y" ], 
           ["Cs", "Ba", "La"], 
           ["Fr", "Ra", "Ac"]]
'''


if __name__ == '__main__':
    psystem = [["H", "", ""], 
           ["Li", "Be", ""], 
           ["Na", "Mg", ""], 
           ["K", "Ca", "Sc"], 
           ["Rb", "Sr", "Y" ], 
           ["Cs", "Ba", "La"], 
           ["Fr", "Ra", "Ac"]]
    
    erdalkalimetalle  = [row[1] for row in psystem]

    metalle_a = list(filter(lambda x: x[-1] == "a" if len(x) > 0 else None,erdalkalimetalle))

    print(metalle_a)
