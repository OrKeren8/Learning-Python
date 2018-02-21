s_p = 0  # s_p => serial prime number
i = 0  # const
c_s_p = 0  # c_s_p => current serial prime number.
c_n = 1  # c_n => current number

s_p = int(input('insert the serial of the prime number you want to find'))

'''
a loop that finds prime numbers and return a pesific one that the user wants
'''
while c_s_p < s_p:
    c_n += 1
    for div in range(1, c_n):
        if c_n % div == 0:
            i = i+1
    if i < 2:
        c_s_p += 1
        print(c_s_p)
    i = 0
print(c_n)
print('finished')
