grade = 3.0
eyecolor = 1
hair = 1
weather = 1

if eyecolor == 1:
    if hair == 1:
        final_grade = grade*(1+0.1)
    else:
        final_grade = grade*0.9
elif eyecolor == 0:
    if hair == 1:
        final_grade = grade*0.9
    else:
        final_grade = grade*1.1

if weather == 1:
    final_grade -= 1

if final_grade <1:
    final_grade = 1
elif final_grade > 6:
    final_grade = 6

final_grade = round(final_grade *2)/2

print(final_grade)

