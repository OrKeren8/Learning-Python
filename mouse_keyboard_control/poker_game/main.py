from mouse_keyboard_control.poker_game.modules.mouse import Mouse
from mouse_keyboard_control.poker_game.modules.pictures import Pictures
from PIL import Image, ImageChops
import time

dic_of_buttons = {
    'select table': (1123, 711),
    '5k payment': (608, 500),
    '500k payment': (733, 500),
    'play now': (954, 752),
    'game play time - normal': (850, 660)
}
# time.sleep(2)
m = Mouse()
pic = Pictures()

# m.click_mouse(dic_of_buttons['select table'])
# m.click_mouse(dic_of_buttons['5k payment'])
# # m.click_mouse(dic_of_buttons['game play time - normal'])
# m.click_mouse(dic_of_buttons['play now'])

# m = 0
# time.sleep(1)
# pic_list = pic.desk_cards_pics()
# for i in pic_list:
#     i.save(str(m)+".jpg")
#     m += 1

# im1 = Image.open('0.jpg')
# im2 = Image.open('1.jpg')
# im1.show()
# im2.show()
#
# diff = ImageChops.difference(im1, im2)
# print(diff.getbbox())
# diff.show()
# diff = ImageChops.difference(im1, im3)
# print(diff.getbbox())
# diff.show()

pic.collect_numbers(1, 1)

# pic.check_if_card_num()