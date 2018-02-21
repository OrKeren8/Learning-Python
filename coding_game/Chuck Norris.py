import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
message = input()
chars = ''  # string of the binary numbers
sep_chars = ''
chuck_code = ''
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for char in message:  # split the word to chars
    char = "{0:b}".format(ord(char))  # get the binary number of the char
    char = char.zfill(7)
    chars = chars + char
for bit in range(len(chars) - 1):
    sep_chars += chars[bit]
    if chars[bit] != chars[bit + 1]:
        sep_chars += ' '
sep_chars += chars[-1]
sep_chars = sep_chars.split(' ')
for seq in sep_chars:
    if '0' in seq:
        chuck_code += '00 '
    else:
        chuck_code += '0 '
    chuck_code += '0' * len(seq) + ' '

chuck_code = chuck_code[:-1]
print(chuck_code)








