import random
import time


def main():
    while not little_game():
        pass
    time.sleep(1)
    print("and now lets sort some numbers")
    time.sleep(1)
    try:
        with open('numbers.txt') as numbers_file:
            numbers = []
            for num in numbers_file:
                numbers.append(num.strip())
            sort_management(numbers, 0, len(numbers) - 1)
            print(numbers)
    except FileNotFoundError:
        print("there is no numbers.txt file")
    try:
        with open('city.txt') as city_file:
            city = []
            for name in city_file:
                city.append(name.strip().capitalize())
            city += get_city()
            city.sort()
            with open('city.txt', 'w') as city_file:
                for name in city:
                    city_file.write(name + '\n')

    except FileNotFoundError:
        print("there is no names.txt file")




def little_game():
    time.sleep(1)
    print("lets play a little game, insert a number' i will generate an random number betwin 1 to 10 and you will try to guess the number.")
    try:
        user_input = input("enter you'r guess!")
        random_num = random.randint(1, 11)
        if random_num == int(user_input):
            print("you are right! my number is indeed ", random_num)
        else:
            print("ho i am sorry")
            for _ in range(3):
                time.sleep(0.3)
                print(".")
            time.sleep(0.3)
            print("my number is ", random_num)
        return True
    except ValueError:
        print("there was a problem, please try again")
        return False


def sort_management(list, start_location, stop_location):
    if start_location < stop_location:
        Guard = quick_sort(list, start_location, stop_location)
        sort_management(list, start_location, Guard - 1)
        sort_management(list, Guard + 1, stop_location)


def quick_sort(list, start_location, stop_location):
    indicator = list[stop_location]
    Guard = start_location
    for index_1 in range(start_location, stop_location):
        if list[index_1] <= indicator:
            list[index_1], list[Guard] = list[Guard], list[index_1]
            Guard += 1
    list[stop_location], list[Guard] = list[Guard], list[stop_location]
    return Guard



def get_city():
    city_list = []
    user_input = ''
    print('now,i want you to give me some names which i will store in a new text file and sort them by their letters')
    print('write name by name until you want to stop, to do that just enter "stop"')
    try:
        while user_input != 'stop':
            user_input = input('name:')
            if user_input != 'stop':
                city_list.append(user_input.strip().capitalize())

                print(city_list)
    except():
        pass

    return city_list





if __name__ == "__main__":
    main()

