##using a stack to control C code 
#initialzing stack
stack = []

##string under test to control:
#sut = "while (1)"
#sut = "if ( a==0 && ( b > 0) )"
sut = "if ( ( a > b ) ) )"

#define function to easily return wrong or right parenthesis
def check_stack(sut: str):
    right = True
    for c in sut:
        if c == "(":
            stack.append(c)
        elif c ==")":
            try:
                if stack.pop() == "(":
                    continue
                else:
                    right = False
            except IndexError:
                right = False
    print("Gültige Klammerung :"+sut) if right else print("Ungültige Klammerung: " + sut)

check_stack(sut)
