# consts
the_number = 1
index = 0

'''getting the range of the dividers for the user'''
range_of_div = input('insert a number that means the range of the dividers')

'''finding the number'''
while True:
    print(the_number)
    for i in range(1, int(range_of_div)+1):
        if the_number % i == 0:
            index += 1
    if index == int(range_of_div):
        break
    the_number += 1
    index = 0
'''print the found number'''
print(the_number)




