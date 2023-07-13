# greatest common devisor

# define function to calculate gcd

def ggt(a: int, b: int):
    a_start = a
    b_start = b
    while(a > 0 and b > 0):
        if a > b:
            a = a-b
        else:
            b = b-a
    # print out what the lcd of a and b is using string formats and a 1 line if condition
    print(f"ggt({a_start},{b_start}) = {a if b==0 else b}")

# use while loop to run the algorithm according to the given nassi-shneiderman diagramm

ggt(18, 6)
