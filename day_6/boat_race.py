import re


def number_of_ways_to_win(time, distance):
    count = 0
    for x in range(time):
        result = (x * 1) * (time - x) > distance
        if result:
            count += 1
    return count


result = 1
times = []
distances = []
with open("../inputs/day6.txt", "r") as file:
    times = re.findall("(\d+)", file.readline())
    distances = re.findall("(\d+)", file.readline())

for time, distance in zip(times, distances):
    ways_to_win = number_of_ways_to_win(int(time), int(distance))
    if ways_to_win > 0:
        result *= ways_to_win


print(result)
