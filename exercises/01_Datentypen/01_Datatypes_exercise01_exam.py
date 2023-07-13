import math

command1 = input("please input w for würfel q for quader and qp for quadratische pyramide: ")

if command1 == "w":
    a = float(input("Bitte würfel seitenlänge eingeben: "))
    print(f"Fläche Würfel = {6*a**2}")
    print(f"Volumen Würfel = {a**3}")
elif command1 == "q":
    a,b,c = tuple(input("Bitte Seitenlängen a b c eingeben:").split())
    a,b,c = float(a),float(b),float(c)
    print(f"Fläche Quader = {2*a*b+2*a*c+2*b*c}")
    print(f"Volumen Quader = {a*b*c}")
elif command1 == "qr":
    a,ha = tuple(input("Bitte Grundfläche sowie Höhe a ha eingeben:").split())
    a,ha = float(a),float(ha)
    hs = math.sqrt(ha**2+(a/2)**2)
    print(f"Fläche Quadratische Pyramide = {a*(a+2*hs)}")
    print(f"Volumen Qaudratische Pyramide = {(a**2*ha)/3}")

