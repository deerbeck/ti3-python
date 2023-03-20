#states and corresponding capitals
states_dict = {'Baden-Württemberg':'Stuttgart', 'Bayern':'München', 'Berlin':'Berlin', 'Brandenburg':'Potsdam', 'Bremen':'Bremen', 'Hamburg':'Hamburg', 'Hessen':'Wiesbaden', 
               'Mecklenburg-Vorpommern':'Schwerin', 'Niedersachsen':'Hannover','Nordrhein-Westfalen':'Düsseldorf', 'Rheinland-Pfalz':'Mainz', 'Saarland':'Saarbrücken',
                'Sachsen-Anhalt':'Magdeburg', 'Sachsen':'Dresden','Schleswig-Holstein':'Kiel', 'Thüringen':'Erfurt'}

#get input from console
state = input("Bitte geben sie das Bundesland ein, dessen Hauptstadt sie wissen möchten: ")

#work with try and except to cover faulty inputs:

try:
    print("Die Hauptstadt von {} ist {}.".format(state, states_dict[state]))

except:
    print("Die Eingabe ist kein deutsches Bundesland!")
    state = input("Bitte geben sie das Bundesland ein, dessen Hauptstadt sie wissen möchten: ")