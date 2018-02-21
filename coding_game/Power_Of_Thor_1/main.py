import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if initial_tx > light_x:
        if initial_ty > light_y and (1 < initial_tx) and (1 < initial_ty):
            print('NW')
        if (initial_ty < light_y) and (1 < initial_tx) and (initial_ty < 17):
            print('SW')
        elif 1 < initial_tx:
            print('W')
    elif initial_tx < light_x:
        if initial_ty > light_y and (initial_tx < 39) and (1 < initial_ty):
            print('NE')
        if initial_ty < light_y and (initial_tx < 39) and (initial_ty < 17):
            print('SE')
        elif initial_tx < 39:
            print('E')
    else:
        if initial_ty > light_y and (1 < initial_ty):
            print('N')
        elif 1 < initial_ty:

            print('S')
