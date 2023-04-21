with open('exercise1.txt',"r") as my_file:
    print(my_file.tell())
    while True:
        line = my_file.readline().strip()
        if not line:
            break
        print(line)
    print(my_file.tell())