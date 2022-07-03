while True:
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
        cube = []
        # building an empty cube
        for index_1 in range(length_of_rib):
            list.append(cube, [])
            for index_2 in range(length_of_rib):
                list.append(cube[index_1], '0')

        # fill the cube with numbers
        raw_spot = 0
        column_spot = length_of_rib // 2
        serial_number = 1
        # if the cube isn't full keep fill it
        while serial_number < length_of_rib ** 2 +1:
            cube[raw_spot][column_spot] = serial_number
            last_raw_spot = raw_spot
            raw_spot -= 1
            if raw_spot == -1:
                raw_spot = length_of_rib - 1
            last_column_spot = column_spot
            column_spot += 1
            if column_spot == length_of_rib:
                column_spot = 0
            if cube[raw_spot][column_spot] != '0':
                raw_spot = last_raw_spot + 1
                if raw_spot == length_of_rib:
                    raw_spot = 0
                column_spot = last_column_spot
            serial_number += 1
        return cube


    # print the cube
    cube = cube_builder(user_selection())
    for i in range(len(cube)):
        print(cube[i])

