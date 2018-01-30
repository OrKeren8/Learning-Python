the_range = int(input('insert a number that the operatian will work from 1 to that number'))


''' a function that gets the sum of the squares of the numbers in the given range'''


def sum_of_sqares_fun(the_range):
    sum_of_sqares = 0
    for i in range(1, the_range+1):
        sum_of_sqares = i**2 + sum_of_sqares
    return sum_of_sqares


'''
a function that gets the square of the sum of the numbers in the given range
'''


def sqare_of_sum_fun(the_range):
    squar_of_sum = 0
    sum_of_nums = 0
    for i in range(1, the_range+1):
        sum_of_nums = i + sum_of_nums
        squar_of_sum = sum_of_nums ** 2
    return squar_of_sum


'''calculatin the difference between the sum of squars and the squars of sum in the given range of numbers'''
print('the diference is')
print(sqare_of_sum_fun(the_range) - sum_of_sqares_fun(the_range))
