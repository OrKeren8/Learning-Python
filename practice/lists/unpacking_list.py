# this line take every element from the list and put it in different variable
data, name, price = ['December 23', 'Bread gloves', 8.51]


def drop_first_last(grades_list):
    first, *middle, last = grades_list
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([95, 65, 84, 51, 87, 95, 98, 96, 92])