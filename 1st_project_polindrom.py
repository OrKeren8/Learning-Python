while True:
    def is_palindrome(x):
        if x[::-1] == x:
            return True
        else:
            return False


    sequence = input('enter a sequence')
    print(is_palindrome(sequence))
