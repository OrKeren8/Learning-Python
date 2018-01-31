import random


max_x = 20
max_y = 20
x_value = 0
y_value = 0
a = 0 #const that tells if the current order is in the list of orders (1 is yes, 0 is no)
b = 0#const that tells how many times the program failed to find new order
order_of_moves = ''
list_of_orders = []


while True:  # sepose to be (b < number)
    if(x_value < max_x and y_value < max_y):
        random_chose = random.randint(0,1)
        if(random_chose == 0):
            x_value += 1
            order_of_moves = order_of_moves + '0'
        elif(random_chose == 1):
            y_value += 1
            order_of_moves = order_of_moves + '1'
    elif(x_value == max_x and y_value < max_y):
        y_value += 1
        order_of_moves = order_of_moves + '1'
    elif(y_value == max_y and x_value < max_x):
        x_value += 1
        order_of_moves = order_of_moves + '0'
    elif(x_value == max_x and y_value == max_y):
        for index in range (len(list_of_orders)):
            if(order_of_moves == str(list_of_orders[index])):
                a += 1
        if(a == 0):
            list_of_orders.append(order_of_moves)
            print(len(list_of_orders))
            b = 0
        else:
            b += 1
        a = 0
        x_value = 0
        y_value = 0
        order_of_moves = ''

print(len(list_of_orders))