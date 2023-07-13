##get input from Console
char_list = list(input("Bitte zu üerbsetzenden String eingeben: "))

ord_char = [ord(c.lower())-96 for c in char_list]

for c,o in zip(char_list, ord_char):
    print(f"{c} -> {o:02}")
