import math

bogen = float(input("Bitte den Winkel im Bogenmaß eingeben: "))

grad = (bogen/(2*math.pi)) * 360

grad_i = int(grad)
minutes = int((grad-grad_i)*60)
seconds = int(((grad-grad_i)*60 - minutes)*60)

print(f"Der Winkel beträgt: {grad_i}° {minutes}\' {seconds}\"")