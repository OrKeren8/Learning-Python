print('hello, \ni am here to finde the largest \nproduct i can made with 4 adjacent digits \nfrom every number you will enter and print it for you' )

'''a loop that check if the number that the user enter is correct'''
check = 0
while not check:  # while the number doesnt good for the opperatin try to get other number
    number = input('for that i need you enter a number whith more then 4 digits here =>')
    if int(number) < 1000:
        print('enter other number please')
    else:
        check = 1

number_list = list(number)  # list of the number the user entered
digits_num = len(number_list)  # how many digits there are in the givven number
bigest_product = 0
for index_1 in range(digits_num-3):  # going throw the whole number
    current_prouct = 1  # start point for multiplication
    for  index_2 in range (index_1, index_1+4):
        current_prouct = int(number_list[index_2]) * current_prouct

    if current_prouct > bigest_product:
        bigest_product = current_prouct

print(bigest_product)
