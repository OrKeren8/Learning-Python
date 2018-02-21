import math
s_p = 0  # s_p => serial prime number
i = 0  # const
flag = False
c_s_p = 0  # c_s_p => current serial prime number.
c_n = 1  # c_n => current number
list_of_primes = []

s_p = int(input('insert the serial of the prime number you want to find'))

while c_n < s_p:
    c_n += 1
    for div in range(2, math.floor(math.sqrt(c_n)) + 1):
        if c_n % div == 0:
            flag = True
            break

    if not flag:
        list_of_primes.append(c_n)
        print('adding {0} to primes'.format(c_n))
    flag = False
print(sum(list_of_primes))
print('finished')

