from collections import Counter

text = 'hello, my name is or keren and i am learning to code with python' \
        'it\'s my first time to get really deep in the coding session and i try to find the best thing i can do with' \
        'this leg whivh pleas me as well' \
        'for now i have a lot of fun but i do have thoughts about the best leg i should learn' \
        'actually after i finish the tutorial i can just to different leg'

words = text.split()
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)