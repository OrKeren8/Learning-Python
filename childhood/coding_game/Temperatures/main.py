import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
closest_temp = 10000
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
##for i in range(5):
    ##t = int(input())
    t = int(i)
    if abs(t) < abs(closest_temp):
        closest_temp = t
    elif abs(t) == abs(closest_temp):
        closest_temp = int((t + closest_temp)/2)
        if closest_temp  == 0:
            closest_temp = abs(t)
if closest_temp != 10000:
    print(closest_temp)
else:
    print("0")
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

