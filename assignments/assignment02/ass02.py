def create_area(size):
    """"Create empty two dimensional array with given size = (rows, colums)"""
    ## Create empty two dimensional array with given size = (rows, colums)
    
    # check if size is in given max and min perimiters
    if max(size) > 10 or min(size) < 2:
        return None
    # create empty area using list comprehension
    else:
        return [[' '] * size[1] for i in range(size[0])]


def fill_area(area, p0, is_horiz, length):
    """Fill given two dimensional array with Position of the ship of given length and start position as well as considering horizontal or vertical orientation"""
    ## Fill given two dimensional array with Position of the ship of given length and start position as well as considering horizontal or vertical orientation

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


def check_area(area, p0, is_horiz, length, profi_check = False):
    """Check that ship of given length can be filled in given position p0"""
    ## Check that ship of given length can be filled in given position p0

    rows, columns = len(area), len(area[0])


    
    #check for occupation of position by another boat
    #optional profi_check to account for official rules 
    if profi_check:

        if is_horiz:
           pass
        else:
            if p0[1] + length > rows:
                return False
            

        if is_horiz:
            # check area around horizontal area by looping through rows over and under needed position
            #check validity of row and columnindex
            try:
                #check for index out of range because negative indices are not covered by exception
                if p0[1] + length > columns or p0[0] -1 < 0 or p0[0] +1 > rows or p0[1]-1 < 0:
                    return False

                for i in range(-1, 2):
                    if "X" in area[p0[0]+i][p0[1]-1:(p0[1]+length)+1]:
                        return False
                    
            except IndexError:
                return False
        else:
            # check area around vertical positon by looping through each column and row
            try:
                if area[p0[0]-1][p0[1]] == "X":
                    return False
                elif area[p0[0]+length+1][p0[1]] == "X":
                    return False
                for i in range(length):
                    if 'X' in area[p0[0]+i][p0[1]-1:p0[1]+1]:
                        return False
                
            except IndexError:
                return False

    else:

        #check validity of row and columnindex
        if is_horiz:
            if p0[0] + length > columns:
                return False
        else:
            if p0[1] + length > rows:
                return False
            
        #check for occupation of position by another boat
        if is_horiz:
            # check horizontal position using Slicing column
            if "X" in area[p0[0]][p0[1]:(p0[1]+length)]:
                return False
        else:
            # check vertical position by looping through rows of the area
            for i in range(length):
                if area[p0[0]+i][p0[1]] == 'X':
                    return False
        
    return True

##testing area:
test = create_area((4,5))
test1 = create_area((5,5))
fill_area(test1, (1,1), True, 3)
print(check_area(test, (1,1), True, 3))
print(check_area(test1, (0,0), True, 1,profi_check=True))
print_area(test1,"Spieler 1")

# main in application
if __name__ == '__main__':
    # replace
    pass
