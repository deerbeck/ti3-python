##print out every box-pointerdiagramm

my_var = 33
print("ID {}".format(id(my_var)))
print("Type: {}".format(type(my_var)))
print("Value: {}".format(my_var))
print("----------------")

my_list = [17, 18, 19]
print("ID {}".format(id(my_list)))
print("Type: {}".format(type(my_list)))
print("Value: {}".format(my_list))
print("----------------")

my_var2 = my_var + 2
print("ID {}".format(id(my_var2)))
print("Type: {}".format(type(my_var2)))
print("Value: {}".format(my_var2))
print("----------------")

my_list += [20, 21, 22]
print("ID {}".format(id(my_list)))
print("Type: {}".format(type(my_list)))
print("Value: {}".format(my_list))
print("----------------")

my_list = my_var
print("ID {}".format(id(my_list)))
print("Type: {}".format(type(my_list)))
print("Value: {}".format(my_list))
print("----------------")

my_inst = 'Hochschule München'
print("ID {}".format(id(my_inst)))
print("Type: {}".format(type(my_inst)))
print("Value: {}".format(my_inst))
print("----------------")

my_inst += ' - Fakultät 04'
print("ID {}".format(id(my_inst)))
print("Type: {}".format(type(my_inst)))
print("Value: {}".format(my_inst))
print("----------------")