import random
import time

from PIL import Image

from poker_game.modules.mouse import Mouse
from poker_game.modules.pictures import Pictures

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
    m.click_mouse(dic_of_buttons['play now'])


def print_new_cards(hand_card_index, desk_card_index):
    '''
    function which print the value of the cards on the desk only if ocured a change in the cards
    :return: ---
    '''
    cards = [[None, None], [None, None], [
        None, None], [None, None], [None, None]]
    first_hand_card = [[None, None]]
    full = False
    collect_desk = True
    while True:
        current_cards = pic.check_deck_cards("desk", 5)
        current_first_hand_card = pic.check_deck_cards("1 hand", 1)
        if current_first_hand_card != [[None, None]] and current_first_hand_card != first_hand_card:
            first_hand_card = current_first_hand_card
            print('save hand cards')
            pic.collect_cards('1 hand', 1, 1, hand_card_index)
            pic.collect_cards('2 hand', 1, 1, hand_card_index)
            hand_card_index += 1
            print(pic.check_deck_cards("1 hand", 1))
            print(pic.check_deck_cards("2 hand", 1))
            m.click_mouse((1177, 885))
        if full:
            if collect_desk:
                print('save desk cards')
                pic.collect_cards('desk', 5, 1, desk_card_index)
                collect_desk = False
                desk_card_index += 5
            flag = 0
            for index3 in range(5):
                if current_cards[index3] == [None, None]:
                    flag += 1
            if flag == 5:
                collect_desk = True
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


# print_new_cards(int(input("last hand number")), int(input("last desk number")))


'''
def koko(card_type, card_type_2, treshold, black_or_white):

    i = -1
    error_index = 0
    while error_index < 1000:
        i += 1
        try:
            momo = Image.open('images/{} {}s/t {} {} {}.jpg'.format(card_type,card_type_2, card_type, card_type_2, str(i)))
            image_index = pic.check_similarity(momo, pic.ref_image_list('images/{} {}s/'.format(card_type, card_type_2), '{} {}'.format(card_type, card_type_2)), treshold, black_and_white=black_or_white)
            pic.save_photo(momo, 'images/sorted {} {}s/{}/'.format(card_type, card_type_2, image_index + 1), '{} {}'.format(card_type, card_type_2), i)
        except FileNotFoundError:
            print(i)
            error_index += 1



koko('desk', 'num', 220, True)
koko('desk', 'shape', 70, False)

koko('1 hand', 'num', 300, True)
koko('1 hand', 'shape', 150, False)

koko('2 hand', 'num', 300, True)
koko('2 hand', 'shape', 150, False)

'''
