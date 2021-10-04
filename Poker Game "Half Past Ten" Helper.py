# This is a poker game named "half past ten". It is similar to black jack but the player need to approch 10.5 points to win the game.
# The cards from A to 10 are represent 1 to 10 points, and JQK are half points. Suit does not count.



def value_transfer(card):
    poker = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "j", "q", "k", "A", "a"]
    while card not in poker:
        print("Wrong input, please try again")
        card = input("Input your first card：")
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if card in number:
        return int(card)
    else:
        if card == "J" or "Q" or "K" or "j" or "q" or "k":
            return 0.5
        elif card == "A" or "a":
            return 1


def card(holding_value, new_value):
    integer = [1,2,3,4,5,6,7,8,9,10]
    sum = holding_value + new_value
    if sum > 10.5:
        print("Dont take it, or you lose")
        return 0
    need_value = 10.5 - sum
    if need_value not in integer:
        print("If you get this card, you still need", need_value, "to approch 10.5")
    else:
        print("If you get this card, you still need", int(need_value), "to approch 10.5")
    possible_card = []
    if need_value == 0:
        print("10.5 is approched, you are win")
    else:
        possible_card.append("K")
        possible_card.append("Q")
        possible_card.append("J")
        while need_value > 0.5:
            if need_value <= 1.5:
                possible_card.append("A")
                need_value -= 1
            else:
                possible_card.append(int(need_value))
                need_value -= 1
        print("你还可以拿如下的牌：")
        for each_card in possible_card:
            each_card = str(each_card)
            print(each_card)


    return 0

def newcard(hold_value,new_card):
    new_card_accepted_value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "j", "q", "k", "A","a", "done" or "Done" or "DONE"]
    poker = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "j", "q", "k", "A", "a"]
    yes = ["y", "Y"]
    no = ["n","N"]
    while new_card not in new_card_accepted_value:
        print("Wrong input, please try again")
        new_card = input("Input dealer's card, or type 'Done' to end：")
    while new_card != "done" or "Done" or "DONE":
        while new_card not in poker:
            print("Wrong input, please try again")
            new_card = input("Input dealer's card, or type 'Done' to end: ")
        new_value = value_transfer(new_card)
        card(hold_value, new_value)
        take_or_not = input("If you take this card, type 'Y'; If you not, type 'N': ")
        take_or_not_accepted_value = ["Y","y","N","n"]
        while take_or_not not in take_or_not_accepted_value:
            print("Wrong input, please try again")
            take_or_not = input("If you take this card, type 'Y'; If you not, type 'N': ")
        if take_or_not in yes:
            hold_value += new_value
            print("Your current points is",hold_value)
            if hold_value == 10.5:
                print("10.5 is approched, you are win")
                return 0
        elif take_or_not in no:
            print("Your current points is",hold_value)
        new_card = input("Input dealer's card, or type 'Done' to end：")

def drink(number_of_people, name, call):
    pass


def main():
    first_card = input("Input the first card you get：")
    hold_value = value_transfer(first_card)
    new_card = input("Input dealer's card, or type 'Done' to end: ")
    newcard(hold_value,new_card)







main()
