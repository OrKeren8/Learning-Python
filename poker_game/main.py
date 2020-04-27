from poker_game.modules.mouse import Mouse
from poker_game.modules.pictures import Pictures
from PIL import Image
import random
import time

dic_of_buttons = {
    'select table': (1123, 711),
    '5k payment': (608, 500),
    '500k payment': (733, 500),
    'play now': (954, 752),
    'game play time - normal': (850, 660)
}

m = Mouse()
pic = Pictures()

def start_game():
    m.click_mouse(dic_of_buttons['select table'])
    m.click_mouse(dic_of_buttons['5k payment'])
    # m.click_mouse(dic_of_buttons['game play time - normal'])
    m.click_mouse(dic_of_buttons['play now'])


def save_5_cards_from_desk():
    num = 93
    for i in range(2000):
        time.sleep(20)
        pic_list = pic.desk_cards_nums_pics()
        for item in pic_list:
            pic.save_photo(item, num, 'desk nums ')
            num +=1


def save_only_middle_card_num():
    num = 0
    for i in range(300):
        time.sleep(15)
        pic_list = pic.desk_cards_nums_pics()
        pic.save_photo(pic_list[2], num, 'desk nums ')
        num +=1


# def check_if_card_num():
#     not_succsess = 0
#     image1 = None
#     image2 = None
#     pre_name = 'num'
#     momo = []
#     koko = [130, 110, 80, 110, 100, 100, 140, 120, 140, 210, 140, 230, 180]
#     for num2 in range(900):
#         eq = False
#         for num1 in range(1, 14):
#             try:
#                 image1 = Image.open('images/a desk nums {}.jpg'.format(num1))
#                 image2 = Image.open('images/desk nums {}.jpg'.format(num2))
#                 equal =  pic.check_similarity(image1, image2, koko[num1 - 1])
#                 if equal:
#                     eq = True
#                     # print('{} and {} are the same'.format(num1, num2))
#                     # momo.append((num1, num2))
#                     image2.save('images/{}/{}{}.jpg'.format(str(num1),str(pre_name), str(num2)))
#             except FileNotFoundError:
#                 eq = True
#         if not eq:
#             if image2:
#                 image2.show()
#                 not_succsess += 1
#     # print(len(momo))
#     print(not_succsess)


def check_if_card():
    cards_list = []
    comp_images = []
    num_of_images = 0
    for num1 in range(1, 14):
        image1 = Image.open('images/a desk nums {}.jpg'.format(num1))
        comp_images.append(image1)
    for num2 in range(1000):
        try:
            image = Image.open('images/desk nums {}.jpg'.format(num2))
            card_num = pic.check_similarity(image, comp_images, 220)
            num_of_images += 1
            if card_num != 101:
                cards_list.append(card_num + 1)
                image.save('images/{}/{}{}.jpg'.format(str(card_num + 1), 'card ', str(num2)))
        except FileNotFoundError:
            pass
    print(len(cards_list))
    print(num_of_images)

def print_desk_cards(iterations, delay):
    time.sleep(delay)
    for _ in range(iterations):
        cards = pic.desk_cards_nums_pics()
        for i in range(5):
            cards[i][0].show()
            cards[i][1].show()
# pic.collect_numbers(200, 836, 2)
print_desk_cards(1, 2)
# check_if_card()