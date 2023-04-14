import numpy as np

def create_area(size):
    #check if size is in given max and min perimiters
    if max(size) > 10 or min(size) < 2:
        return None
    #create empty area using list comprehension
    else:
        return [[' '] * size[1] for i in range(size[0])]

# main in application
if __name__=='__main__':
    # replace
    pass
