from pynput.keyboard import Listener as klis
from pynput.mouse import Listener as mlis


def write_to_file(data):
    data = str(data)
    with open('log.txt', 'a') as logf:
        logf.write(data)


def print_location(x, y):
    print('the location of the mouse is (' + str(x) + ', ' + str(y) + ')')


if input() == '1':
    with mlis(on_move=print_location) as m:
        m.join()

else:
    with klis(on_press=write_to_file) as l:
        l.join()

# m = mlis(on_move=print_location)
# l = klis(on_press=write_to_file)
#
# l.start()
# l.stop()
# m.start()
# m.stop()