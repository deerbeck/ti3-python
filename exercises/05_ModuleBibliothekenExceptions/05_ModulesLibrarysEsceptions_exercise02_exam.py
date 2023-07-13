# task 1 anagram
# open textfile with contextmanager
class ProgramQuit(Exception):
     pass

while True:
    try:
        command = input("Pleas input your command ['?','q','a','s']: ").lower()
        if command == "?":
            print("'?' - Anzeigen des Hilfetexts.")
            print("'q' - Programm wird beendet.")
            print("'a' - Addition zweier Zahlen.")
            print("'s' - Subtraktion zweier Zahlen.")
        elif command == "a":
            val1 = float(input("Wert 1: "))
            val2 = float(input("Wert 2: "))
            print(f"Ergebnis: {val1} + {val2} = {(val1+val2):.3f}")
        
        elif command == "s":
            val1 = float(input("Wert 1: "))
            val2 = float(input("Wert 2: "))
            print(f"Ergebnis: {val1} - {val2} = {(val1-val2):.3f}")
        elif command == "q":
            raise ProgramQuit
        else:
            print("Fehlerhafte Eingabe, bitte wiederholen.")

    except ValueError:
                print("Bitte Zahlen eingeben!")
    except EOFError:
        raise ProgramQuit
    except ProgramQuit:
         print("Programm wird beendet!")
         break