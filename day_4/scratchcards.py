def check_card(winning_nums, card):
    card_val = 0
    counter = 0
    for num in card:
        if num in winning_nums:
            counter += 1
            if counter == 1:
                card_val += 1
            if counter > 1:
                card_val *= 2
    return int(card_val)


if __name__ == "__main__":
    sum_val = 0
    winning_nums = []
    card = []

    with open("./input.txt", "r") as file:
        for line in file.readlines():
            winning_nums_input, card_input = line.strip().split("|")
            _, winning_nums_input = winning_nums_input.strip().split(":")
            winning_nums = [
                num for num in winning_nums_input.strip().split(" ") if num != ""
            ]
            card = [num for num in card_input.strip().split(" ") if num != ""]

            sum_val += check_card(winning_nums, card)

    print("Total value of scratchcards:", sum_val)
