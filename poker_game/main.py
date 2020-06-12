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


def save_5_cards_from_desk(iterations, delay, start_num):
    num = start_num
    for i in range(iterations):
        time.sleep(delay)
        pic_list = pic.cards_pics()
        for item in pic_list:
            pic.save_photo(item[1], pic.cards['path'], 'desk shapes', num)
            num +=1


def save_only_middle_card_num():
    num = 0
    for i in range(300):
        time.sleep(15)
        pic_list = pic.cards_pics()[0]
        pic.save_photo(pic_list[2], num, 'desk nums ')
        num +=1


def check_if_card():
    cards_list = []
    comp_images = []
    num_of_images = 0
    for num1 in range(1, 14):
        image1 = Image.open('images/all numbers/a desk nums {}.jpg'.format(num1))
        comp_images.append(image1)
    for num2 in range(2000):
        try:
            image = Image.open('images/all numbers/desk nums {}.jpg'.format(num2))
            card_num = pic.check_similarity(image, comp_images, 220, black_and_white=True)
            num_of_images += 1
            if card_num != 101:
                cards_list.append(card_num + 1)
                image.save('images/sorted nums/{}/{}{}.jpg'.format(str(card_num + 1), 'card ', str(num2)))
        except FileNotFoundError:
            pass
    print(len(cards_list))
    print(num_of_images)

def print_cards(iterations, delay):
    time.sleep(delay)
    for _ in range(iterations):
        cards = pic.cards_pics()[0]
        for i in range(5):
            cards[i][0].show()
            cards[i][1].show()


def check_if_card_shape():
    cards_list = []
    comp_images = []
    num_of_images = 0
    for num1 in range(1, 5):
        image1 = Image.open('images/all shapes/a desk shapes {}.jpg'.format(num1))
        comp_images.append(image1)
    for num2 in range(2000):
        try:
            image = Image.open('images/all shapes/desk shapes {}.jpg'.format(num2))
            if num2 == 190:
                card_num = pic.check_similarity(image, comp_images, pic.cards['thresh hold'], debug=True)
            else:
                card_num = pic.check_similarity(image, comp_images, pic.cards['thresh hold'])
            num_of_images += 1
            if card_num != 101:
                cards_list.append(card_num + 1)
                image.save('images/sorted shapes/{}/{}{}.jpg'.format(str(card_num + 1), 'card ', str(num2)))
        except FileNotFoundError:
            pass
    print(len(cards_list))
    print(num_of_images)


def print_new_cards():
    cards = [[None, None], [None, None], [None, None], [None, None], [None, None]]
    full = False
    for i in range(100000):
        current_cards = pic.check_deck_cards("desk", 5)
        if full:
            flag = 0
            for index3 in range(5):
                if current_cards[index3] == [None, None]:
                    flag += 1
            if flag == 5:
                full = False
        else:
            for index in range(5):
                if cards[index] != current_cards[index]:
                    if current_cards[0] != [None, None] and current_cards[1] != [None, None] and current_cards[2] != [None, None]:
                        cards = current_cards
                        if cards[4] != [None, None]:
                            full = True
                        print(cards)
                        break


momo = pic.card_pics("1 hand", 1)
momo[0][0].show()
momo[0][1].show()
