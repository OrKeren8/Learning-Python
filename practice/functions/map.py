money_list = [20, 40, 100]


def double_money(money):
    return money * 2


doubled_money_list = list(map(double_money, money_list))
print(doubled_money_list)
