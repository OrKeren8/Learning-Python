len_of_numbers = int(input('how many numbers do you want to sort'))
numbers = []
print('enter the numbers with enter after every number')
for i in range(len_of_numbers):
    numbers.append(int(input()))


def quick_sort(list, start_location, stop_location):
    indecator = list[stop_location]
    gard = start_location
    for index_1 in range(start_location, stop_location):
        if list[index_1] <= indecator:
            list[index_1], list[gard] = list[gard], list[index_1]
            gard += 1
    list[stop_location], list[gard] = list[gard], list[stop_location]
    return gard


def sort_management(list, start_location, stop_location):
    if start_location < stop_location:
        gard = quick_sort(list, start_location, stop_location)
        sort_management(list, start_location, gard-1)
        sort_management(list, gard + 1, stop_location)


sort_management(numbers, 0, (len(numbers) - 1))
print(numbers)
