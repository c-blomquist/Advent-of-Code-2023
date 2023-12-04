import re
content = []
sum_val = 0

gear = '*'
found_gears = set()

def get_gear(matrix, i, j, value):
    global found_gears
    found_gears.add((i, j))
    number = value
    index = j
    flag = True
    while flag:
        j -= 1
        try:   
            value = matrix[i][j]
            if bool(re.match("\d", value)):
                number = value + number
                found_gears.add((i,j))
            else:
                flag = False
        except IndexError:
            flag = False
    flag = True
    j = index
    while flag:
        j += 1
        try:   
            value = matrix[i][j]
            if bool(re.match("\d", value)):
                number = number + value
                found_gears.add((i,j))
            else: 
                flag = False
        except IndexError:
            flag = False
    return int(number)

# These functions feel very messy
def get_gear_ratio(matrix, i, j, gear_amount, gear_ratio, value):
    if gear_amount == 1:
        gear_ratio += get_gear(matrix, i, j, value)
    if gear_amount == 2:
        gear_ratio *= get_gear(matrix, i, j, value)
    if gear_amount > 2:
        gear_ratio = 0
    return gear_ratio

# this also seems needlessly long and complex but I am not sure what else to use
def check_adjacent(matrix, i, j):
    gear_amount = 0
    gear_ratio = 0
    global found_gears 
    found_gears = set()
    try:
        value = matrix[i+1][j]
        if bool(re.match("\d", value) and (i+1, j) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i+1, j, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    try:
        value = matrix[i+1][j-1]
        if bool(re.match("\d", value) and (i+1, j-1) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i+1, j-1, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    try:
        value = matrix[i+1][j+1]
        if bool(re.match("\d", value) and (i+1, j+1) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i+1, j+1, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    try:
        value = matrix[i][j-1]
        if bool(re.match("\d", value) and (i, j-1) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i, j-1, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    try:
        value = matrix[i][j+1]
        if bool(re.match("\d", value) and (i, j+1) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i, j+1, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    try:
        value = matrix[i-1][j-1]
        if bool(re.match("\d", value) and (i-1, j-1) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i-1, j-1, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    try:
        value = matrix[i-1][j]
        if bool(re.match("\d", value) and (i-1, j) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i-1, j, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    try:
        value = matrix[i-1][j+1]
        if bool(re.match("\d", value) and (i-1, j+1) not in found_gears):
            gear_amount += 1
            gear_ratio = get_gear_ratio(matrix, i-1, j+1, gear_amount, gear_ratio, value)
    except IndexError:
        value = None
    if gear_amount != 2:
        gear_ratio = 0
    return int(gear_ratio)


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            content.append(list(line.replace('\n', '')))
        
    #large time complexity here, not sure how to do it better though 
    for i, line in enumerate(content):
        for j, symbol in enumerate(line):
            if symbol == gear:
                sum_val += check_adjacent(content, i, j)
                
    print("Sum of gear ratios found", sum_val)