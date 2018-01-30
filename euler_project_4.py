number_1 = 999
index_1 = 100
index_2 = 100
m = 0
palindrome = 0

while index_1 < number_1:
    number_2 = 999
    while index_2 < number_2:
        number_3 = number_1 * number_2
        str_number_3 = str(number_3)
        list_number_3 = list(str_number_3)
        list_number_3.reverse()
        reversed_str_number_3 = ''.join(str(e) for e in list_number_3)
        number_2 = number_2 - 1
        if str_number_3 == reversed_str_number_3 and number_3 > palindrome:
            palindrome = number_3
    number_1 = number_1 - 1

print(palindrome)
