def error(card_split):
    color_data = ["S", "H", "C", "D"]
    card_data = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for each in card_split:
        if each[0] not in card_data or each[1] not in color_data:
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


def combo_define(player_card, house_card, card_data, color_data):
    card_sum = player_card + house_card
    card_split = [str(card_sum[0:2]), str(card_sum[2:4]), str(card_sum[4:6]), str(card_sum[6:8]), str(card_sum[8:10]),
                  str(card_sum[10:12]), str(card_sum[12:14])]
    if not error(card_split):
        return 0
    sorted_card_split = sorted_card(card_split)  # 按照从小到大的顺序整理牌
    print(sorted_card_split)


def main():
    color_data = ["S", "H", "C", "D"]
    card_data = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    player_card = "JHQH"
    house_card = "JS7C8DASQS"
    combo_define(player_card, house_card, card_data, color_data)


main()
