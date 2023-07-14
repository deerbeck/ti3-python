print("Bitte Auswahl treffen, welche Umwandlung sid vollziehen wollen:")
print(
"""(1) Umrechnung von Celsius nach Kelvin
(2) Umrechnung von Celsius nach Fahrenheit
(3) Umrechnung von Kelvin nach Celsius
(4) Umrechnung von Kelvin nach Fahrenheit
(5) Umrechnung von Fahrenheit nach Celsius
(6) Umrechnung von Fahrenheit nach Kelvin""")
command = input()

if command == "1":
    temp = float(input("Bitte Temperatur in Celsius eingeben: "))
    print(f"Die Temperatur beträgt {(temp+273.15):.3f} Kelvin")
elif command == "2":
    temp = float(input("Bitte Temperatur in Celsius eingeben: "))
    print(f"Die Temperatur beträgt {(temp*1.8 + 32):.3f} Fahrenheit")
elif command == "3":
    temp = float(input("Bitte Temperatur in Kelvin eingeben: "))
    print(f"Die Temperatur beträgt {(temp-273.15):.3f} Celsius")
elif command == "4":
    temp = float(input("Bitte Temperatur in Kelvin eingeben: "))
    print(f"Die Temperatur beträgt {((temp-273.15)*1.8 +32):.3f} Fahrenheit")
elif command == "5":
    temp = float(input("Bitte Temperatur in Fahrenheit eingeben: "))
    print(f"Die Temperatur beträgt {((temp-32)/1.8):.3f} Celsius")
elif command == "6":    
    temp = float(input("Bitte Temperatur in Fahrenheit eingeben: "))
    print(f"Die Temperatur beträgt {(((temp-32)/1.8)+273.15):.3f} Kelvin")
else:
    print("Opfer!")