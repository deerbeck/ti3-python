#provided input for exercise 02
my_list = list('123456789')

my_list = my_list[:4:] + my_list[6::]
print(my_list)
my_list = my_list + ["a","b","c","d","e","f"]
print(my_list)
my_list = ["0"] + my_list
print(my_list)
my_list = my_list[:5:] + ["5", "6"] + my_list[5::]
print(my_list)