import time
dictionary = {}

user_select = 0
while user_select != 4:
    # getting from the user the number of the task he wants the program to do
    try:
        print("insert the number of the task you want me to do\n"
              "1) add a word to the dictionary\n"
              "2) search for a word in the dictionary\n"
              "3) delete a word from the dictionary\n"
              "4) stop the program")
        user_select = int(input())
    except ValueError:
        print("i am sorry, that wasn't a number...")
    # if the task chose by the user do it
    if user_select == 1:
        dictionary.update({input('the word in english'): input('the translation in hebrew')})
        print('the word added Successfully')
    elif user_select == 2:
        search_the_word = str(input('write the word you want to search:'))
        if search_the_word in dictionary:
            print(dictionary[search_the_word])
        else:
            print("the word isn't in the dictionary")
    elif user_select == 3:
        delete_the_word = str(input('write the word you want to delete:'))
        if delete_the_word in dictionary:
            del dictionary[delete_the_word]
            print('the word deleted Successfully')
        else:
            print("the word isn't in the dictionary")
    # waiting for the user to read the answer and clearing the
    # page to the next operation
    time.sleep(2)
    print('\n' * 20)
    user_select = 0
print(dictionary)


