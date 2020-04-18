from pynput.keyboard import Listener as klis
from pynput.mouse import Listener as mlis


def write_to_file(data):
    data = str(data)
    with open('log.txt', 'a') as logf:
        logf.write(data)


def print_location(x, y):
    print('the location of the mouse is (' + str(x) + ', ' + str(y) + ')')

def click_location(*args):
    print(args)


user_input = input()
if user_input == '1':
    with mlis(on_move=print_location) as m:
        m.join()

elif user_input == '2':
    with klis(on_press=write_to_file) as l:
        l.join()

elif user_input == '3':
    with mlis(on_click=click_location) as s:
        s.join()
