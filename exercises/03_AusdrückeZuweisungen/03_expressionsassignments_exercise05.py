##using a stack to control C code 
#initialzing stack
stack = []

##string under test to control:
#sut = "while (1)"
sut = "if ( a==0 && ( b > 0) )"
#sut = "if ( ( a > b ) ) )"

#define function to easily return wrong or right parenthesis
def check_stack(sut: str):
    for e in sut:
        if e == "(":
            stack.append(e)
        elif e == ")":
            try:
                if stack.pop() == ")":
                    continue
            except:
                return print(f"Ungültige Klammerung: {sut}")
    return print(f"Gültige Klammerung: {sut}")

check_stack(sut)


