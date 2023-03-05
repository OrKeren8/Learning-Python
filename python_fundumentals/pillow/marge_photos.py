from PIL import Image


assassin = Image.open('assasin.jpg')
assassin = assassin.transpose(Image.ROTATE_270)
assassin = assassin.resize((1980, 1113))
ship1 = Image.open('ship1.jpg')
ship1 = ship1.resize((1980, 1113))
r1, g1, b1 = assassin.split()
r2, g2, b2 = ship1.split()

dic1 = {'0': '4', '1': '2', '2': '1'}
list2 = [r2, g2, b2]
list3 = [r1, g1, b1]
for _ in range(8):
    list1 = [None, None, None]
    sum = _
    for k in sorted(dic1, key=dic1.get, reverse=True):
        if sum >= int(dic1[k]):
            list1[int(k)] = list3[int(k)]
            sum -= int(dic1[k])
        else:
            list1[int(k)] = list2[int(k)]
    print(list1)
    new_img = Image.merge('RGB', list1)
    new_img.show()