import random

def create_area(size):
    """"Create empty two dimensional array with given size = (rows, colums)"""
    # Create empty two dimensional array with given size = (rows, colums)

    # check if size is in given max and min perimiters
    if max(size) > 10 or min(size) < 2:
        return None
    # create empty area using list comprehension
    else:
        return [[' '] * size[1] for i in range(size[0])]


def fill_area(area, p0, is_horiz, length):
    """Fill given two dimensional array with Position of the ship of given length and start position as well as considering horizontal or vertical orientation"""
    # Fill given two dimensional array with Position of the ship of given length and start position as well as considering horizontal or vertical orientation

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

    # loop through area and print out each row
    for i in range(rows):
        print(str(i) + "|" + "".join(area[i]) + "|")

    print_column_numbers(columns)


def check_area(area, p0, is_horiz, length, profi_check=False):
    """Check that ship of given length can be filled in given position p0"""
    # Check that ship of given length can be filled in given position p0

    rows, columns = len(area), len(area[0])

    # check for occupation of position by another boat
    # optional profi_check to account for official rules

    try:
        # check validity of row and columnindex
        if p0[0] < 0 or p0[1] < 0:
            return False
            # check for occupation of position by another boat
        if is_horiz:
            # check validity of columnindex
            if p0[1] + length > columns:
                return False
        else:
            # check validity of rowindex
            if p0[0] + length > rows:
                return False

        # loop through positions to check for occupation of board
        for i in range(length):
            # loop through rows or columns depending on is_horiz
            row = p0[0] if is_horiz else p0[0] + i
            col = p0[1] + i if is_horiz else p0[1]
            if area[row][col] == "X":
                return False
        
        # checking according to offical rulse
        if profi_check:
            # loop through positions to check for occupation of board and neighboring ships
            for j in range(-1, 2):
                for i in range(-1, length + 1):
                      # loop through rows or columns depending on is_horiz
                    row = p0[0] + j if is_horiz else p0[0] + i
                    col = p0[1] + i if is_horiz else p0[1] + j
                    if area[row][col] == "X":
                        return False
                    
    # exception to use EAFP
    except IndexError:
        return False
    
    return True

def generate_boat(area, boat_spec):
    """Generate random new boat with given length = boat_spec in area."""
    ###Generate random new boat with given length = boat_spec in area.
    rows, columns = len(area), len(area[0])
    #set number of trys to generate new boat
    trys = 5
    
    for i in range(trys):
        #generate random startingpoint p0
        p0 = (random.randint(0, rows), random.randint(0, columns))

        #generate random is_horiz value
        is_horiz = (random.randint(0,1))

        #check if generated boat can fit in area
        if check_area(area,p0,is_horiz,boat_spec):
            fill_area(area,p0,is_horiz,boat_spec)
            break
        else:
            continue



# m = 7
# n = 8
# area = create_area((m, n))
# fill_area(area, (1, 2), True, 5)
# fill_area(area, (3, 4), False, 3)

# print(check_area(area, (3, 3), True, 3))


# main in application
if __name__ == '__main__':
    # replace
    pass
