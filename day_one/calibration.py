# Work for part one of AOC

import re

content = []
numbers = []
values = []
total = 0

with open("./input.txt", "r") as file:
    content = file.readlines()
    
for line in content:
    numbers.append(re.findall("[0-9]", line))
    
for found_nums in numbers:
    values.append(int(found_nums[0]) * 10 + int(found_nums[-1]))
    
for x in values:
    total += x
    
print("The total is:", total)

