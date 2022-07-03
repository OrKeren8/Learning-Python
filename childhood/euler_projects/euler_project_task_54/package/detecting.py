class RankDetector(object):

    def __init__(self, hand_nums, hand_suits):  # get the numbers and suits in one and as lists
        self.hand_nums = list(hand_nums)  # list of the numbers in the current hand
        self.hand_suits = list(hand_suits)  # list of the suits in the current hand
        self.ranks = {'high_card': 1, 'one_pair': 2, 'two_pairs': 3, 'three_of_a_kind': 4, 'straight': 5, 'flush': 6, 'full_house': 7, 'four_of_a_kind': 8, 'Straight_Flush': 9, 'royal_flush': 10}
        self.stat = {'2.first_duplicate': 0, '3.value1': 0, '4.second_duplicate': 0, '5.value2': 0, '1.rank': 0, '6.highCard': 0}
    """
    a function that takes a hand of cards and checks if there is
    straight/flush/straight flush/ straight royal.
    the function returns the best case it found as it name 1.rank
    and the high card of the hand
    """

    def flush_straight_comb(self):
        straight_check = 0
        flush_check = 0
        sum_of_nums = 0

        high_card = self.hand_nums[4]  # the last card in the sorted hand has the highest value
        for i in range(4):  # go through the hand
            sum_of_nums += self.hand_nums[i]
            if self.hand_nums[i + 1] - self.hand_nums[i] == 1:  # check if attached
                straight_check += 1
            if self.hand_suits[i] == self.hand_suits[i+1]:  # check if the suits in the same color
                flush_check += 1
        if straight_check == 4 and flush_check == 4:  # of the hand has straightFlush
            self.stat['1.rank'], self.stat['6.highCard'] = self.ranks['Straight_Flush'], high_card
        elif (straight_check == 3) and (self.hand_nums[3] == 5) and (self.hand_nums[4] == 14) and flush_check == 4: # in case of 1,2,3,4,5 and flush
            self.stat['1.rank'], self.stat['6.highCard'] = self.ranks['Straight_Flush'], 5
        elif flush_check == 4:  # if only flush
            self.stat['1.rank'], self.stat['6.highCard'] = self.ranks['flush'], high_card
        elif straight_check == 4:  # if only straight
            self.stat['1.rank'], self.stat['6.highCard'] = self.ranks['straight'], high_card
        elif (straight_check == 3) and (self.hand_nums[3] == 5) and (self.hand_nums[4] == 14):  # in a case of 1,2,3,4,5
            self.stat['1.rank'], self.stat['6.highCard'] = self.ranks['straight'], 5
        return dict(self.stat)

    """
    a function that gets a hand of cards and checks if there is
    pair/ two pairs/ 3 of a kind/ full house/ 4 of a kind
    the function returns the best case it found
    """
    def x_of_a_kind(self):
        self.stat['1.rank'], self.stat['6.highCard'] = 0, 0  # reset the stat of the hand
        high_card = self.hand_nums[4]  # the last card in the sorted hand has the highest value
        repeat_list = []  # a list that gets the times a number shows in a hand
        value_list = []  # a list that get the numbers that in a hand two times or more
        for i in range(1, 15):  # go through all the numbers
            x = self.hand_nums.count(i)  # get how many times every numbers shows in the hand
            if x >= 2:  # if a number in the hand 2 times or more keep it
                repeat_list.append(x)
                value_list.append(i)
        if len(repeat_list) < 1:  # if there is no duplicate numbers
            self.stat['6.highCard'] = high_card
        elif len(repeat_list) < 2:  # if there is only one number that appears more then one time
            if repeat_list[0] == 2:  # if the number appears 2 times
                self.stat['2.first_duplicate'], self.stat['3.value1'], self.stat['1.rank'] = repeat_list[0], value_list[0], self.ranks['one_pair']
            if repeat_list[0] == 3:  # if the numbers appear 3 times
                self.stat['2.first_duplicate'], self.stat['3.value1'], self.stat['1.rank'] = repeat_list[0], value_list[0], self.ranks['three_of_a_kind']
            if repeat_list[0] == 4:  # if the number appear 4 times
                self.stat['2.first_duplicate'], self.stat['3.value1'], self.stat['1.rank'] = repeat_list[0], value_list[0], self.ranks['four_of_a_kind']
        else:  # if there are more than two numbers that appears more than one time in a hand
            if repeat_list[1] > repeat_list[0]:  # place the number with more appearance in the hand first
                repeat_list[1], repeat_list[0] = repeat_list[0], repeat_list[1]
                value_list[1], value_list[0] = value_list[0], value_list[1]
            if repeat_list[0] == 3:
                self.stat['2.first_duplicate'] = repeat_list[0]
                self.stat['3.value1'] = value_list[0]
                self.stat['4.second_duplicate'] = repeat_list[1]
                self.stat['5.value2'] = value_list[1]
                self.stat['1.rank'] = self.ranks['full_house']
                self.stat['6.highCard'] = high_card
            else:  # if there are two pairs
                if value_list[1] > value_list[0]:  # place the number with the higher value in the hand first
                    repeat_list[1], repeat_list[0] = repeat_list[0], repeat_list[1]
                    value_list[1], value_list[0] = value_list[0], value_list[1]
                self.stat['2.first_duplicate'] = repeat_list[0]
                self.stat['3.value1'] = value_list[0]
                self.stat['4.second_duplicate'] = repeat_list[1]
                self.stat['5.value2'] = value_list[1]
                self.stat['1.rank'] = self.ranks['two_pairs']
                self.stat['6.highCard'] = high_card
        return dict(self.stat)
