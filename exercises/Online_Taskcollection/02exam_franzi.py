def evalpostfix(expr: list) -> float:
    stack = []
    for e in expr:
        if e.isdecimal():
            stack.append(e)
        else:
            try:
                nr = stack.pop()
                nl = stack.pop()
                buf = nl+e+nr
                stack.append(str(eval(buf)))
            except SyntaxError:
                print("Not a viable python operation!")
            except ZeroDivisionError:
                print("Division by 0 not possible!")
    return stack[-1]

if __name__ == "__main__":
    expr = [['5','3','8','*','+'],
            ['5','3','*','8','+'],
            ['2','7','3','/','2','6','*','-','+']]
    
    for e in expr:
        r = evalpostfix(e)
        print(f"{e} -> {r}")
        
        