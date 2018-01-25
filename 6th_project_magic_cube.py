def user_selection():
    ask_user = True
    while ask_user:
        print('insert the length of the rib of the magic cube:')
        try:
            length_of_rib = int(input())
            if length_of_rib % 2 != 0:
                ask_user = False
            else:
                print("the number has to be odd")
        except ValueError:
            print('you have to insert a number')
    return length_of_rib


def cube_builder(length_of_rib):
    empty_raw = []
    cube = []
    raw_spot = 0
    column_spot = length_of_rib//2
    serial_number = 1
    # building an empty cube
    for index_1 in range(length_of_rib):
        list.append(cube, [])
        for index_2 in range(length_of_rib):
            list.append(cube[index_1], '')
    # fill the cube with numbers
    cube[raw_spot][column_spot] = serial_number
    return cube


cube = cube_builder(user_selection())
for i in range(len(cube)):
    print(cube[i])
