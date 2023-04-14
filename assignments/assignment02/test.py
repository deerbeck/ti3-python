
# check for occupation of position by another boat
if is_horiz:
    # check validity of columnindex
    if p0[1] + length > columns:
        return False
    # check horizontal position using Slicing column
    if "X" in area[p0[0]][p0[1]:(p0[1]+length)]:
        return False

else:
    # check validity of rowindex
    if p0[0] + length > rows:
        return False
    # check vertical position by looping through rows of the area
    for i in range(length):
        if area[p0[0]+i][p0[1]] == 'X':
            return False
        