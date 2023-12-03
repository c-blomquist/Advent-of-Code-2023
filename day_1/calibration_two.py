# Work for part two of AOC

import re

content = []
numbers = []
values = []
total = 0

def replaceNumbers(input):
    result = []
    word_to_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for value in input:
        if(re.match("(one|two|three|four|five|six|seven|eight|nine)", value)):
            result.append(word_to_num[value])
        else:
            result.append(value)
    return result
            
            
            

with open("./input.txt", "r") as file:
    content = file.readlines()
    
for line in content:
    numbers.append(re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line))
    
for found_nums in numbers:
    found_nums = replaceNumbers(found_nums)
    values.append(int(found_nums[0]) * 10 + int(found_nums[-1]))
    
for x in values:
    total += x
    
print("The total is:", total)

