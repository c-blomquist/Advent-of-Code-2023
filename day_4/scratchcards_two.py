import re


def check_card(winning_nums, card):
    card_val = 0
    for num in card:
        if num in winning_nums:
            card_val += 1
    return int(card_val)


if __name__ == "__main__":
    sum_val = 0
    winning_nums = []
    card = []
    # this literal for the length of input makes this not be able to be used for other examples
    copies = [1] * 192

    with open("./input.txt", "r") as file:
        for line in file.readlines():
            winning_nums_input, card_input = line.strip().split("|")
            id, winning_nums_input = winning_nums_input.strip().split(":")
            id = (re.findall("(\d+)", id))[-1]
            winning_nums = [
                num for num in winning_nums_input.strip().split(" ") if num != ""
            ]
            card = [num for num in card_input.strip().split(" ") if num != ""]
            num = check_card(winning_nums, card)
            while num > 0:
                try:
                    copies[int(id) - 1 + num] = (
                        copies[int(id) - 1 + num] + copies[int(id) - 1]
                    )
                    num -= 1
                except IndexError:
                    num -= 1
    for num in copies:
        sum_val += num
    print("Total number of cards at the end:", sum_val)
