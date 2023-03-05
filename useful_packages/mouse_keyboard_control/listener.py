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

def check_start_button(data):
    data = str(data)
    if data == "'s'":
        print('stop')
        b.stop()
        with mlis(on_click=click_location) as a:
            a.join()


user_input = input('type 1 to print the location of the mouse when moved\ntype 2 to collect the keys pressed from the keyboard\ntype 3 to print the location of the mouse when clicked, to start press s\n')
if user_input == '1':
    with mlis(on_move=print_location) as m:
        m.join()

elif user_input == '2':
    with klis(on_press=write_to_file) as k:
        k.join()

elif user_input == '3':
    with klis(on_press=check_start_button) as b:
        b.join()