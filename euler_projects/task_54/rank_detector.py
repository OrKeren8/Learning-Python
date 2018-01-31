class RankDetector:
    limhok = 1

    def royal_flush(self, hand_nums, hand_suits):
        check = 0
        for i in range(4):
            if hand_nums[i + 1] - hand_nums[i] == 1:
                check += 1
            if hand_suits[i] == hand_suits[i+1]:
                check += 1
        if check == 8:
            return 'royal flush'