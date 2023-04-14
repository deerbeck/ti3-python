import numpy as np


def create_area(size):
    """"Create empty two dimensional array with given size = (rows, colums)"""
    # check if size is in given max and min perimiters
    if max(size) > 10 or min(size) < 2:
        return None
    # create empty area using list comprehension
    else:
        return [[' '] * size[1] for i in range(size[0])]


def fill_area(area, p0, is_horiz, length):
    """Fill given two dimensional array with Position of the ship of given length and start position as well as considering horizontal or vertical orientation"""
    if is_horiz:
        #fill horizontal position using Slice assignemnts on the column
        area[p0[0]][p0[1]:(p0[1]+length)] = ['X']*length
    else:
        #fill vertical position by looping through rows of the area
        for i in range(length):
            area[p0[0]+i][p0[1]] = 'X'
    return area

# main in application
if __name__ == '__main__':
    # replace
    pass
