# finding all of the prime numbers under the given number - 600851475143'''

prims = []
biggest_prime_factor = 0
the_number = 13195
i = 0
for number in range(2, int(10000)):
    for m in range(1, number):
        if number % m == 0:
            i = i+1
    if i < 2:
        prims.append(number)
    i = 0

'''searching the factor numbers'''
for i in range(0, len(prims)):
    if ((the_number % prims[i]) == 0) and (biggest_prime_factor < prims[i]):
        biggest_prime_factor = prims[i]
        the_number = the_number / prims[i]
print(biggest_prime_factor)
