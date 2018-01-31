from math import factorial


def paths_counter():
    grid_size = int(input('how many squares there are in one rib'))
    number_of_paths = factorial(grid_size * 2) / factorial(grid_size) ** 2
    return number_of_paths


print(paths_counter())



