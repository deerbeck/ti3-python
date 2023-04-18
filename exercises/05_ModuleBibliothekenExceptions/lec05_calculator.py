def calculator():
    print("Bitte Input für den Taschenrechner.")
    operator_dict = {"*": lambda a,b: a*b , "/": lambda a,b: a/b, "+" : lambda a,b: a+b, "-": lambda a,b: a-b}
    first_num = input("1. Zahl: ")
    second_num = input("2. Zahl: ")
    operator = input("Operation (*, /, +, -): ")
    try:
        print("Ergebnis: " + str(operator_dict[operator](int(first_num),int(second_num))))
    except KeyError:
        print("Fehlerhafte Eingabe, bitte erneut versuchen: ")
        calculator()
    except ValueError:
        print("Fehlerhafte Eingabe, bitte erneut versuchen: ")
        calculator()

calculator()