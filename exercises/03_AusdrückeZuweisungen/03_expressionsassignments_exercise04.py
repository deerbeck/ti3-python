##get input from Console
char_list = list(input("Bitte zu üerbsetzenden String eingeben: "))

#get ASCII list from characters
order_list = [ord(e.lower())-96 for e in char_list]

#zip both lists together to get char to corresponding order
result  = [f"{c} -> {o:02d}" for c,o in zip(char_list, order_list)]

for e in result:
    print(e)