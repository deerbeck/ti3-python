import sys

# Flächenberechnung eines Kreises
pi = 3.1415  # ID:---1 #Type: float # refcount = 1
print("ID {}".format(id(pi)))
print("Type: {}".format(type(pi)))
print("refcount: {}".format(sys.getrefcount(pi)))
print("----------------")

radius = 10  # ID:---2 #Type: int # refcount = 1
print("ID {}".format(id(radius)))
print("Type: {}".format(type(radius)))
print("refcount: {}".format(sys.getrefcount(radius)))
print("----------------")

area = radius*radius*pi  # ID:---3 #Type: float # refcount = 1
print("ID {}".format(id(area)))
print("Type: {}".format(type(area)))
print("refcount: {}".format(sys.getrefcount(area)))
print("----------------")

# Volumenberechnung eines Zylinders
my_pi = pi  # ID:---1 #Type: float # refcount = 2
print("ID {}".format(id(my_pi)))
print("Type: {}".format(type(my_pi)))
print("refcount: {}".format(sys.getrefcount(my_pi)))
print("----------------")

my_radius = 12  # ID:---4 #Type: int # refcount = 1
print("ID {}".format(id(my_radius)))
print("Type: {}".format(type(my_radius)))
print("refcount: {}".format(sys.getrefcount(my_radius)))
print("----------------")

my_height = 100  # ID:---5 #Type: int # refcount = 1
print("ID {}".format(id(my_height)))
print("Type: {}".format(type(my_height)))
print("refcount: {}".format(sys.getrefcount(my_height)))
print("----------------")

my_area = my_radius*my_radius*my_pi  # ID:---6 #Type: float # refcount = 1
print("ID {}".format(id(my_area)))
print("Type: {}".format(type(my_area)))
print("refcount: {}".format(sys.getrefcount(my_area)))
print("----------------")

my_volume = my_area * my_height  # ID:---7 #Type: float # refcount = 1
print("ID {}".format(id(my_volume)))
print("Type: {}".format(type(my_volume)))
print("refcount: {}".format(sys.getrefcount(my_volume)))
print("----------------")
