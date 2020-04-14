len_of_numbers = int(input('how many numbers do you want to sort'))
numbers = []
print('enter the numbers with enter after every number')
for i in range(len_of_numbers):
    numbers.append(int(input()))


#  function that split a list to two parts
#  in the left - all the numbers that lower then the lats number in the list
#  in the right - all the numbers that higher then the lats number in the list
def quick_sort(list, start_location, stop_location):
    indicator = list[stop_location]
    Guard = start_location
    for index_1 in range(start_location, stop_location):
        if list[index_1] <= indicator:
            list[index_1], list[Guard] = list[Guard], list[index_1]
            Guard += 1
    list[stop_location], list[Guard] = list[Guard], list[stop_location]
    # printing the process of sorting
    #for index_2 in range(len_of_numbers):
    #   print('*' * numbers[index_2])
    #print('\n' * 10)

    return Guard


#  function that calls to quick_sort function to split
#  the list till it will be Completely sorted
def sort_management(list, start_location, stop_location):
    if start_location < stop_location:
        Guard = quick_sort(list, start_location, stop_location)
        sort_management(list, start_location, Guard-1)
        sort_management(list, Guard + 1, stop_location)


#  call to sort_management function in the first time with the list from
#  the user to start the process of sorting
sort_management(numbers, 0, (len(numbers) - 1))


#   print the list of numbers after sorting it from low to high
print(numbers)
