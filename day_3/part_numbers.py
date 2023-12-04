import re
content = []
sum_val = 0

special_characters = ['#', '*', '$', '+', '@', '-', '=', '&', '%', '/', '+', '']
found_indexes = set()


def add_to_sum(matrix, i, j, value):
    found_indexes.add((i, j))
    global sum_val
    number = value
    index = j
    flag = True
    while flag:
        j -= 1
        try:   
            value = matrix[i][j]
            if bool(re.match("\d", value)):
                number = value + number
                found_indexes.add((i, j))
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
                found_indexes.add((i, j))
            else: 
                flag = False
        except IndexError:
            flag = False
    sum_val += int(number)

# this also seems needlessly long and complex but I am not sure what else to use
def check_adjacent(matrix, i, j):
    try:
        value = matrix[i+1][j]
        if bool(re.match("\d", value) and (i+1, j) not in found_indexes):
            add_to_sum(matrix, i+1, j, value)
    except IndexError:
        value = None
    try:
        value = matrix[i+1][j-1]
        if bool(re.match("\d", value) and (i+1, j-1) not in found_indexes):
            add_to_sum(matrix, i+1, j-1, value)
    except IndexError:
        value = None
    try:
        value = matrix[i+1][j+1]
        if bool(re.match("\d", value) and (i+1, j+1) not in found_indexes):
            add_to_sum(matrix, i+1, j+1, value)
    except IndexError:
        value = None
    try:
        value = matrix[i][j-1]
        if bool(re.match("\d", value) and (i, j-1) not in found_indexes):
            add_to_sum(matrix, i, j-1, value)
    except IndexError:
        value = None
    try:
        value = matrix[i][j+1]
        if bool(re.match("\d", value) and (i, j+1) not in found_indexes):
            add_to_sum(matrix, i, j+1, value)
    except IndexError:
        value = None
    try:
        value = matrix[i-1][j-1]
        if bool(re.match("\d", value) and (i-1, j-1) not in found_indexes):
            add_to_sum(matrix, i-1, j-1, value)
    except IndexError:
        value = None
    try:
        value = matrix[i-1][j]
        if bool(re.match("\d", value) and (i-1, j) not in found_indexes):
            add_to_sum(matrix, i-1, j, value)
    except IndexError:
        value = None
    try:
        value = matrix[i-1][j+1]
        if bool(re.match("\d", value) and (i-1, j+1) not in found_indexes):
            add_to_sum(matrix, i-1, j+1, value)
    except IndexError:
        value = None


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            content.append(list(line.replace('\n', '')))
        
    #large time complexity here, not sure how to do it better though 
    for i, line in enumerate(content):
        for j, symbol in enumerate(line):
            if symbol in special_characters:
                check_adjacent(content, i, j)
    print("Sum of parts found", sum_val)