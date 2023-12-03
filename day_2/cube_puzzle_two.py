sum = 0


def get_game_power(array):
    red_min = 0
    blue_min = 0
    green_min = 0
    # split the hands into individual ones
    array = array.split(";")
    for game in array:
        # split into individual cube colors
        game = game.split(",")
        for hand in game:
            amount, color = hand.strip().split(" ")
            if color == "red":
                if int(amount) > red_min:
                    red_min = int(amount)
            if color == "blue":
                if int(amount) > blue_min:
                    blue_min = int(amount)
            if color == "green":
                if int(amount) > green_min:
                    green_min = int(amount)

    return red_min * blue_min * green_min


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            _, hands = line.split(":")
            sum += get_game_power(hands)

print(sum)
