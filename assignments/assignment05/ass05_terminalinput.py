from ass05_rooms import *
from ass05_roommanagement import *
from ass05_customer import *
from ass05_json_handling import *
from ass05_plotting import *
from matplotlib import pyplot as plt
import glob
import sys
import os

##self explainatory through the given strings

def start_menu():
    
    print("\n---------Startmenü!---------")
    print("Willkommen im Raumverwaltungssystem der Hochschule München.")
    print("Aktuell besitzt ihr Raumverwaltungssystem folgende Räume, sowie Buchungen:\n" + str(RM) + "\n")
    print("Bitte geben Sie Ihre gewünschte Aktion ein:")
    command = input("'Raum hinzufügen' | 'Kunde hinzufügen' | 'Kunden anzeigen' | 'Raum buchen' | 'Raum freigeben' | 'Speichern' | 'Laden' | 'Plotting' | 'Beenden'\n")
    
    if command == "Raum hinzufügen":
        return add_room()
    elif command == "Kunde hinzufügen":
        return add_customer()
    elif command == "Kunden anzeigen":
        return show_customers()
    elif command == "Raum buchen":
        return book_room()
    elif command == "Raum freigeben":
        return unbook_room()
    elif command == "Speichern":
        return safe()
    elif command == "Laden":
        return load()
    elif command == "Beenden":
        return shutdown()
    elif command == "Plotting":
        return plotting()
    else:
        print("\n---------Eingabe fehlerhaft!---------")
        return start_menu()



def add_room():
    print("\n---------Raum hinzufügen---------")
    print("Aktuell gibt es folgende Räume und Buchungen:")
    print(RM)
    print("Sie können einen der drei Raumtypen 'Vorlesungsraum'/'Abstellraum'/'Meetingraum' hinuzfügen.")
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    command = input("Um einen neuen Raum hinzuzufügen geben Sie bitte folgende Daten ein:\n<Raumnummer> <Kapazität> <Raumtyp>:\n")

    if len(input_data := command.split(" ")) == 1:
        if command == "Startmenü":
            print("\n---------Zurück ins Startmenü!---------")
            return start_menu()
        print("\n---------Eingabe fehlerhaft!---------")
        return add_room()

    if len(input_data) != 3:
        print("\n---------Eingabe fehlerhaft!---------")
        return add_room()

    room_number = input_data[0]
    capacity = input_data[1]
    room_type = input_data[2]
    if type(capacity) != int:
        print("\n---------Kapazität muss eine Ganzzahl sein!---------")
        return add_room()

    if room_type == "Vorlesungsraum":
        presentation_medium = input("""Beim Raumtyp 'Vorlesungsraum' wird noch ein Präsentationsmedium benötigt:
              Eingabe bitte wie folgt: <Präsentationsmedium>:\n""")
        RM.new_classroom(room_number, int(capacity), presentation_medium)
        return start_menu()
    elif room_type == "Abstellraum":
        area = input("""Beim Raumtyp 'Abstellraum' wird noch die Fläche des Raums benötigt:\n
              Eingabe bitte wie folgt: <Fläche>:\n""")
        RM.new_closet(room_number, int(capacity), area)
        return start_menu()
    elif room_type == "Meetingraum":
        RM.new_meetingroom(room_number, capacity)
        return start_menu()
    else:
        print(f"\n---------Raumtyp {room_type} nicht vorhanden!---------")
        return add_room()



def add_customer():
    print("\n---------Kunde hinzufügen---------")
    print("Aktuell gibt es folgende Kunden:")
    print(RM.get_customers())
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    print("Um einen neuen Kunden hinzuzufügen geben Sie bitte folgende Daten ein:")
    command = input("<Vorname Nachname> <E-Mail Adresse>:\n")

    if len(input_data := command.split(" ")) == 1:
        if command == "Startmenü":
            print("\n---------Zurück ins Startmenü!---------")
            return start_menu()
        print("\n---------Eingabe fehlerhaft!---------")
        return add_customer()

    if len(input_data) != 3:
        print("\n---------Eingabe fehlerhaft!---------")
        return add_customer()

    customer_name = input_data[0] +" "+ input_data[1]
    customer_mail = input_data[2]
    
    if "@" not in customer_mail:
        print("\n---------Falsches Format der E-Mail Adresse!---------")
        return add_customer()

    RM.new_customer(customer_name, customer_mail)

    return start_menu()


def show_customers():
    print("\n---------Kunden:---------")
    print(RM.get_customers())
    input("Bitte <Enter> drücken um zurück ins 'Startmenü' zu kommen:")
    return start_menu()


def book_room():
    print("\n---------Raum buchen---------")
    print("Aktuell gibt es folgende Räume und Buchungen:")
    print(RM)
    print("Dazu gibt es folgende Kunden:")
    print(RM.get_customers())
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    print("Um einen Raum zu buchen geben Sie bitte folgende Daten ein:")
    command = input("<Raumnummer> <Kundenvorname Kundennachname>:\n")
    input_data = command.split(" ")
    
    if command == "Startmenü":
        print("\n---------Zurück ins Startmenü!---------")
        return start_menu()

    if len(input_data) != 1:
        print("\n---------Eingabe fehlerhaft!---------")
        return book_room()
    
    room_number = input_data[0]
    customer_name = input_data[1] +" "+ input_data[2]

    if RM.book_room(room_number, customer_name) == -1:
        return book_room()
    
    return start_menu()


def unbook_room():
    print("\n---------Raum freigeben---------")
    print("Aktuell gibt es folgende Räume und Buchungen:")
    print(RM)
    print("Dazu gibt es folgende Kunden:")
    print(RM.get_customers())
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    print("Um einen Raum freizugeben geben Sie bitte folgende Daten ein:")

    command = input("<Raumnummer>\n")
    input_data = command.split(" ")
    
    room_number = input_data[0]

    if command == "Startmenü":
        print("\n---------Zurück ins Startmenü!---------")
        return start_menu()

    if len(input_data) != 1:
        print("\n---------Eingabe fehlerhaft!---------")
        return unbook_room()
    
    if RM.unbook_room(room_number) == -1:
        return unbook_room()


def safe():
    print("\n---------Speichern---------")
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    print("Um das aktuelle Raumverwaltungssystem abzuspeichern geben Sie bitte folgende Daten ein:")
    command = input("<Dateiname>:\n")

    input_data = command.split(" ")
    filename = input_data[0]+ ".json"

    if command == "Startmenü":
        print("\n---------Zurück ins Startmenü!---------")
        return start_menu()

    if len(input_data) != 1:
        print("\n---------Eingabe fehlerhaft!---------")
        return safe()
    
    if safe_as_json(RM,filename) == -1:
        print("\n---------Fehler!---------")
        return safe()

    
def load():
    print("\n---------Laden---------")
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    print("Folgende gespeicherte Dateien sind vorhanden:")
    print(files := glob.glob("*.json"))
    print("Um eine gespeicherte Datei zu laden geben Sie bitte folgendes ein:")
    command = input("<Dateiname.json>:\n")
    
    input_data = command.split(" ")

    filename = input_data[0]
    
    if command == "Startmenü":
        print("\n---------Zurück ins Startmenü!---------")
        return start_menu()

    if len(input_data) != 1:
        print("\n---------Eingabe fehlerhaft!---------")
        return load()
    
    if filename not in files:
        print("\n---------Datei nicht vorhanden!---------")
        return load()
    
    terminal_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")

    if (load_from_json(RM,filename)) == -1:
        print("\n---------Fehler!---------")
        return load()
    
    sys.stdout = terminal_stdout
    print("\n---------Erfolgreich geladen!---------")
    return start_menu()
    


def plotting():
    print("\n---------Raum-Plotting---------")
    print("Willkommen im Plotting-Menü.")
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    print("Bitte geben Sie Ihre gewünschte Aktion ein:")
    command = input("'Überischt' | 'Verfügbarkeiten'\n")

    if command == "Startmenü":
        print("\n---------Zurück ins Startmenü!---------")
        return start_menu()
    
    elif command == "Übersicht":
        plot_rooms(RM)
        return plotting() 
    
    elif command == "Verfügbarkeiten":
        plot_availability(RM)
        return plotting() 
    
    else:
        print("\n---------Eingabe fehlerhaft!---------")
        return plotting()


    pass
    
def shutdown():
    print("\n---------Beenden---------")
    print("Mit dem Kommando 'Startmenü' kommen Sie zurück zum Startmenü.")
    print("Gehen Sie sicher, dass Sie vor dem Beenden alles gespeichert haben!")
    print("Mit dem Kommando 'Speichern' kommen Sie zum Speichern.")
    print("Mit dem Kommando 'Beenden' beenden Sie das Programm.")
    command = input("")
    
    input_data = command.split(" ")

    filename = input_data[0]
    
    if command == "Startmenü":
        print("\n---------Zurück ins Startmenü!---------")
        return start_menu()
    
    if command == "Speichern":
        print("\n---------Zum Speichern!---------")
        return safe()
    
    if command == "Beenden":
        print("\n---------Programm beendet!---------")
        plt.close('all')
        return 0

    if len(input_data) != 1:
        print("\n---------Eingabe fehlerhaft!---------")
        return shutdown()


RM = Roommanagement()
start_menu()

