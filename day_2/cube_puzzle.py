import re
red_max = 12
green_max = 13
blue_max = 14
sum = 0

def check_game(array):
    # split the hands into individual ones
    array = array.split(";")
    for game in array:
        # split into individual cube colors
        game = game.split(",")
        for hand in game:
            amount, color = hand.strip().split(" ")
            print(amount, color)
            if color == "red" and int(amount) > red_max:
                return False
            if color == "blue" and int(amount) > blue_max:
                return False
            if color == "green" and int(amount) > green_max:
                return False
            
    return True


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            id, hands = line.split(":")
            # get just the id from the id section
            id = (re.findall("(\d+)", id))[-1]
            # check the hands of the game we are on, if it is good then add the id to the sum
            print(id, ":", hands)
            if check_game(hands):
                sum += int(id)
                
print(sum)
