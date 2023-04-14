def create_area(size):
    # Create empty two dimensional array with given size = (rows, colums)
    """"Create empty two dimensional array with given size = (rows, colums)"""
    # check if size is in given max and min perimiters

    if max(size) > 10 or min(size) < 2:
        return None
    # create empty area using list comprehension
    else:
        return [[' '] * size[1] for i in range(size[0])]


def fill_area(area, p0, is_horiz, length):
    # Fill given two dimensional array with Position of the ship of given length and start position as well as considering horizontal or vertical orientation
    """Fill given two dimensional array with Position of the ship of given length and start position as well as considering horizontal or vertical orientation"""

    if is_horiz:
        # fill horizontal position using Slice assignemnts on the column
        area[p0[0]][p0[1]:(p0[1]+length)] = ['X']*length
    else:
        # fill vertical position by looping through rows of the area
        for i in range(length):
            area[p0[0]+i][p0[1]] = 'X'
    return area


def print_column_numbers(n):
    """Print out formated line including numbering of columns"""
    # Print out formated line including numbering of columns

    # print column numbers with join function and list comprehension of given columns number
    print(" |" + "".join([str(i) for i in range(n)]) + "| ")


def print_area(area, title):
    """Print out game area with given title"""
    # Print out game area with given title

    # define number fo rows and columns for better readability
    rows, columns = len(area), len(area[0])
    print(title)
    print_column_numbers(columns)
    
    #loop through area and print out each row
    for i in range(rows):
        print(str(i) + "|" + "".join(area[i]) + "|")
    
    print_column_numbers(columns)

# ##testing area:
# test = create_area((4,5))
# test1 = fill_area(test, (1,1), False, 3)
# print_area(test1,"Spieler 1")

# main in application
if __name__ == '__main__':
    # replace
    pass
