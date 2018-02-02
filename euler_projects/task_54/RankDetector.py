class RankDetector(object):

    def __init__(self, hand_nums, hand_suits):
        self.hand_nums = hand_nums
        self.hand_suits = hand_suits

    def royal_flush(self):
        check = 0
        for i in range(4):
            if self.hand_nums[i + 1] - self.hand_nums[i] == 1:
                check += 1
            if self.hand_suits[i] == self.hand_suits[i+1]:
                check += 1
        if check == 8:
            return 'royal flush'
