'''
Aufgabe (List Comprehension, Periodensystem) [4 P]

Gegeben ist ein Ausschnitt aus dem Periodensystem der Elemente als Liste 
von Listen in der Variablen psystem. In der zweiten Spalte werden 
die Erdalkalimetalle geführt. 

Erzeugen Sie eine Liste, die alle Erdalkalimetalle beinhaltet und 
deren Kurzbezeichnung auf den Buchstaben ’a’ enden.

psystem = [["H", "", ""], 
           ["Li", "Be", ""], 
           ["Na", "Mg", ""], 
           ["K", "Ca", "Sc"], 
           ["Rb", "Sr", "Y" ], 
           ["Cs", "Ba", "La"], 
           ["Fr", "Ra", "Ac"]]
'''

psystem = [["H", "", ""], 
           ["Li", "Be", ""], 
           ["Na", "Mg", ""], 
           ["K", "Ca", "Sc"], 
           ["Rb", "Sr", "Y" ], 
           ["Cs", "Ba", "La"], 
           ["Fr", "Ra", "Ac"]]

if __name__ == '__main__':
    # Option 1
    ea = [e1 for (e0, e1, e2) in psystem if len(e1) > 0 and e1[-1] == 'a']
    
    # Option 2
    psystem_vert = list(zip(*psystem))
    ea = [elem for elem in psystem_vert[1] if elem.endswith('a')]

    print(ea)
    
