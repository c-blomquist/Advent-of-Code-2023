import re


def number_of_ways_to_win(time, distance):
    count = 0
    for x in range(time):
        result = (x * 1) * (time - x) > distance
        if result:
            count += 1
    return count


times = []
distances = []
with open("../inputs/day6.txt", "r") as file:
    times = re.findall("(\d+)", file.readline())
    time = "".join(times)
    distances = re.findall("(\d+)", file.readline())
    distance = "".join(distances)

print(number_of_ways_to_win(int(time), int(distance)))
