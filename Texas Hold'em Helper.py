import re


def error(card_split):
    color_data = ["S", "H", "C", "D"]
    card_number_data = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for each in card_split:
        if each[0] not in card_number_data or each[1] not in color_data:
            print("扑克输入错误")
            return False
    card_split_dic = {}.fromkeys(card_split)  # 这种方法建立字典，会把列表里的元素当做字典的键，由于字典的键不能重复，所以会自动去重
    if len(card_split_dic) == len(card_split):
        pass
    else:
        print("输入含有重复值")
        return False
    return True


def sorted_card(card_split):
    # 按照从小到大的顺序整理牌
    sorted_card_split = sorted(card_split, key=lambda x: (
        str(x[0]) == "A", str(x[0]) == "K", str(x[0]) == "Q", str(x[0]) == "J", str(x[0]) == "10", str(x[0]) == "9",
        str(x[0]) == "8", str(x[0]) == "7", str(x[0]) == "6", str(x[0]) == "5", str(x[0]) == "4", str(x[0]) == "3",
        str(x[0]) == "2", str(x[1]) == "S", str(x[1]) == "H", str(x[1]) == "C", str(x[0]) == "D"))
    return sorted_card_split


def combo_defined(card_split):
    result = ""
    link_count = 0
    color_data = ["S", "H", "C", "D"]
    card_number_data = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    card_number = [card[0] for card in card_split]
    card_color = [card[1] for card in card_split]

    for each_card in card_color:
        if card_color.count(each_card) >= 5:
            result = "同花" + str(each_card) + " "

    for each_card in card_number:
        if card_number.count(each_card) == 4 and each_card not in result:
            result += "四个" + each_card + " "

        if card_number.count(each_card) == 3 and each_card not in result:
            result += "三个" + each_card + " "

        if card_number.count(each_card) == 2 and each_card not in result:
            result += "两个" + each_card + " "

    # 顺子判定未完成


    print(card_split, result)
    pass


def card_sum(player_card, house_card):
    card_sum = player_card + house_card

    card_split = re.findall(r'.{2}', card_sum)  # 正则化语法，数字代表按照多少长度将字符串等分成列元素
    if not error(card_split):
        return 0
    sorted_card_split = sorted_card(card_split)  # 按照从小到大的顺序整理牌
    combo_defined(sorted_card_split)
    # print(sorted_card_split)


def main():
    player_card = "JHQH"
    first_round = "JSJC8D"
    second_round = "8C"
    third_round = "KH"
    card_sum(player_card, first_round + second_round + third_round)


main()
