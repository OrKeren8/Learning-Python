import numpy as np
import heavyCalc
import timeit


size = 10000000
arr = np.random.randint(1, 101, size=size)  # size=10 for example, change as needed

t1 = timeit.default_timer()
sum = 0
for num in arr:
    sum += num
print((timeit.default_timer() - t1) * 1000, "ms")

t1 = timeit.default_timer()
"""cpp version"""
result = heavyCalc.sum_array(arr)
print((timeit.default_timer() - t1) * 1000, "ms")

"""numpy builtin function - actually working as a c func"""
sum3 = arr.sum()



