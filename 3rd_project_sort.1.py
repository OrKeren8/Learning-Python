len_of_numbers = int(input('how many numbers do you want to sort'))
list = []
print('enter the numbers with enter after every number')
for i in range(len_of_numbers):
    list.append(int(input()))


def sort_function(x):
    for i in range(x):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]

            # printing the process of sorting
            for m in range(len_of_numbers):
                print('*' * list[m])
            print('\n' * 10)
    if x > 1:
        x -= 1
        sort_function(x)


sort_function(len(list)-1)
print(list)
