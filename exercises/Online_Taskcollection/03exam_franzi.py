python_triple = [(x,y,z) for x in range(1,43) for y in range(x,43) for z in range(y, 43) if x**2 + y**2 == z**2]

print(python_triple)