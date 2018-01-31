ranks = ['high card', 'one pair', 'two pairs',
         'three of kind', 'straight', 'flush',
         'full house', 'four of a kind', 'Straight Flush', 'royal flush']
left_hand_nums = []
left_hand_suits = []
right_hand_nums = []
right_hand_suits = []


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


def check_rank(hand_nums, hand_suits):


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
