# המטרה היא מציאת המספר המחולק שמוצא הכי הרבה מספרים שאינם מספרים ראשוניים
# אני עושה זאת על ידי רשימה הגדולה מהמספר הראשוני הגדול ביותר שאותו אני רוצה למצוא ובכל פעם שיש איזה מחלק שמצא
# מספר לא ראשוני אני מוסיף לאינדקס השווה לערכו שברשימה הזו אחד ובסוף ממיין אותם מהגדול לקטן על פי כמות המספרים שהם חשפו
#
#
#
import math

list_of_primes = []
list_of_dividers = {}
max_num = int(input('insert a number'))
current_num = 1
for list_index in range(int(math.floor(math.sqrt(max_num))) + 1):
    list_of_dividers[list_index] = 0

while current_num < max_num:
    current_num += 1
    for div in range(2, int(math.floor(math.sqrt(current_num))) + 1):
        if current_num % div == 0:
            list_of_dividers[div] += 1
            break
    print(current_num)

for item in sorted(zip(list_of_dividers.values(), list_of_dividers.keys())):
    print(item)
print('finished')
