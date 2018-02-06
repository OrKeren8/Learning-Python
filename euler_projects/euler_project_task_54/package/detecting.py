class RankDetector(object):

    def __init__(self, hand_nums, hand_suits):
        self.hand_nums = list(hand_nums)
        self.hand_suits = list(hand_suits)
        self.ranks = ['high card', 'one pair', 'two pairs', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'Straight Flush', 'royal flush']

    # a function that takes a hand of cards and checks if there is
    # straight/flush/straight flush/ straight royal.
    # the function returns the best case it found as it name
    # and the high card of the hand
    def flush_straight_comb(self):
        straight_check = 0
        flush_check = 0
        sum_of_nums = 0
        high_card = self.hand_nums[4]  # the last card in the sorted hand has the highest value
        for i in range(4):
            sum_of_nums += self.hand_nums[i]
            if self.hand_nums[i + 1] - self.hand_nums[i] == 1:
                straight_check += 1
            if self.hand_suits[i] == self.hand_suits[i+1]:
                flush_check += 1
        if straight_check == 4 and flush_check == 4:
            return 0, high_card, 0, 0, self.ranks.index('Straight flush'), high_card
        elif (straight_check == 3) and (self.hand_nums[3] == 5) and (self.hand_nums[4] == 14) and flush_check == 4:
            # in case of 1,2,3,4,5 and flush
            return 0, 5, 0, 0, self.ranks.index('straight flush'), 5
        elif flush_check == 4:
            return 0, high_card, 0, 0, self.ranks.index('flush'), high_card
        elif straight_check == 4:
            return 0, high_card, 0, 0, self.ranks.index('straight'), high_card
        elif (straight_check == 3) and (self.hand_nums[3] == 5) and (self.hand_nums[4] == 14):
            return 0, high_card, 0, 0, self.ranks.index('straight'), 5
        else:
            return 0, 0, 0, 0, 0, 0
    # a function that gets a hand of cards and checks if there is
    # pair/ two pairs/ 3 of a kind/ full house/ 4 of a kind
    # the function returns the best case it found

    def x_of_a_kind(self):
        current_hand_rank = []
        best_hand_rank = [0, 0, 0, 0, 0, 0]
        high_card = self.hand_nums[4]  # the last card in the sorted hand has the highest value
        repeat_list = []  # a list that gets the times a number shows in a hand
        value_list = []  # a list that get the numbers that in a hand two times or more
        for i in range(1, 15):
            x = self.hand_nums.count(i)
            if x >= 2:
                repeat_list.append(x)
                value_list.append(i)
        if len(repeat_list) < 1:  # if there is no duplicate numbers
            best_hand_rank = high_card
        elif len(repeat_list) < 2:  # if there is only one number that appears more then one time
            repeat_list.append(0)
            value_list.append(0)
            if repeat_list[0] == 2:  # if the number appears 2 times
                current_hand_rank = repeat_list[0], value_list[0], repeat_list[1], value_list[1], self.ranks.index('one pair'), high_card
                if current_hand_rank[4] > best_hand_rank[4]:
                    best_hand_rank = current_hand_rank
            if repeat_list[0] == 3:  # if the numbers appear 3 times
                current_hand_rank = repeat_list[0], value_list[0], repeat_list[1], value_list[1], self.ranks.index('three of a kind'), high_card
                if current_hand_rank[4] > best_hand_rank[4]:
                    best_hand_rank = current_hand_rank
            if repeat_list[0] == 4:  # if the number appear 4 times
                best_hand_rank = repeat_list[0], value_list[0], repeat_list[1], value_list[1], self.ranks.index('four of a kind'), high_card
                if current_hand_rank[4] > best_hand_rank[4]:
                    best_hand_rank = current_hand_rank
        # if there are 2 different numbers that appears in a hand more then one time
        else:  # if there are more than two numbers that appears more than one time in a hand
            if repeat_list[1] > repeat_list[0]:  # place the number with more appearance in the hand first
                repeat_list[1], repeat_list[0] = repeat_list[0], repeat_list[1]
                value_list[1], value_list[0] = value_list[0], value_list[1]
            if repeat_list[0] == 2:  # check if there are two pairs
                if value_list[1] > value_list[0]:  # place the number with the higher value in the hand first
                    repeat_list[1], repeat_list[0] = repeat_list[0], repeat_list[1]
                    value_list[1], value_list[0] = value_list[0], value_list[1]
                current_hand_rank = repeat_list[0], value_list[0], repeat_list[1], value_list[1], self.ranks.index('two pairs'), high_card
                if current_hand_rank[4] > best_hand_rank[4]:
                    best_hand_rank = current_hand_rank
            if repeat_list[0] == 3:
                current_hand_rank = repeat_list[0], value_list[0], repeat_list[1], value_list[1], self.ranks.index('full house'), high_card
                if current_hand_rank[4] > best_hand_rank[4]:
                    best_hand_rank = current_hand_rank
        return best_hand_rank
