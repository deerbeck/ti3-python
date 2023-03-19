import math

# select geometrical body
geometric_body = input(
    "Please name the geometrical object of which you want to calculate the volume and surface: 'cube' , 'cuboid' or 'square pyramid': ")

# differentiation of the geometric bodys

if geometric_body == 'cube':
    # input of sidelength
    side_a = int(
        input("Please state the length of the sides of the cube in integers: "))
    # calculate volume and surface
    volume = side_a**3
    surface = side_a**2 * 6

elif geometric_body == 'cuboid':
    # input of sidelengths
    side_a = int(
        input("Please state the length of the side 'a' of the cuboid in integers: "))
    side_b = int(
        input("Please state the length of the side 'b' of the cuboid in integers: "))
    side_c = int(
        input("Please state the length of the side 'c' of the cuboid in integers: "))
    # calculate volume and surface
    volume = side_a*side_b*side_c
    surface = 2 * side_a * side_b + 2 * side_a * side_b + 2 * side_b * side_c

elif geometric_body == 'square pyramid':
    side_a = int(
    input("Please state the length of the sides of the footprint of the quadratic pyramid in integers: "))
    height_h = int(
    input("Please state the height of the sides of the quadratic pyramid in integers: "))
    ##calculate height of one sidetriangle to calculate surface
    height_ha = math.sqrt(height_h**2 + (side_a/2)**2)

    volume = (side_a**2 * height_h)/3
    surface = (side_a**2 + side_a*height_ha*2)
    



# new input if previous input was faulty
else:
    print("Not supported input. Please do only select one of the three options.")
    geometric_body = input(
        "Please name the geometrical object of which you want to calculate the volume and surface: 'cube' , 'cuboid' or 'square pyramid': ")


