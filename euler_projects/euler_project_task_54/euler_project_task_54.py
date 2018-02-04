from .detecting import RankDetector

left_hand_nums = []
left_hand_suits = []
right_hand_nums = []
right_hand_suits = []


def main():
    with open('poker_hands.txt') as hands:
        for line in hands:
            list_of_line = convert_T_J_Q_K_A_to_nums(line)
            # get the numbers and suits of each hand:
            for i in range(0, 13, 3):
                left_hand_nums.append(int(list_of_line[i]))
                left_hand_suits.append(list_of_line[i+1])
                right_hand_nums.append(int(list_of_line[i+15]))
                right_hand_suits.append(list_of_line[i+16])
            # call to the function that check the highest rank of the hand:
            left_hand_rank = check_rank(left_hand_nums, left_hand_suits)
            right_hand_rank = check_rank(right_hand_nums, right_hand_nums)
            print(left_hand_rank)
            print(right_hand_rank)
            #
            # need to take the ranks of hands and compare them
            #
            # clear hands for next round
            right_hand_nums.clear()
            right_hand_suits.clear()
            left_hand_nums.clear()
            left_hand_suits.clear()


def convert_T_J_Q_K_A_to_nums(line):
    list_of_line = list(line)
    for i in range(0, 29):
        if list_of_line[i] == 'T':
            list_of_line[i] = 10
        elif list_of_line[i] == 'J':
            list_of_line[i] = 11
        elif list_of_line[i] == 'Q':
            list_of_line[i] = 12
        elif list_of_line[i] == 'K':
            list_of_line[i] = 13
        elif list_of_line[i] == 'A':
            list_of_line[i] = 14
    return list_of_line


def check_rank(hand_nums, hand_suits):  # call to the functions that gives the rank of the hand a important values
    best_rank = []  # the best case of the hand and important values on that case
    rank_class = RankDetector(hand_nums, hand_suits)
    first_function_rank = rank_class.flush_straight_comb()
    second_function_rank = rank_class.x_of_a_kind()
    if first_function_rank[0] > second_function_rank[4]:  # check which function found the best rank case in a hand
        best_rank = first_function_rank
    else:
        best_rank = second_function_rank
    return best_rank


if __name__ == "__main__":
    main()
