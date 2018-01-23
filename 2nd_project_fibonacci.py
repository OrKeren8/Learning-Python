
while True:
    n = int(input('enter the place of the element in the fibonacci series you want to get'))
    print('calculating...')


    def fibonacci_function(n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return fibonacci_function(n-1) + fibonacci_function(n-2)

    the_answer = fibonacci_function(n)
    print('the answer is:')
    print(the_answer)
