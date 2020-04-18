from mouse_keyboard_control.poker_game.modules.mouse import Mouse
import time

dic_of_buttons = {
    'select table': (1123, 711),
    '5k payment': (608, 500),
    '500k payment': (733, 500),
    'play now': (954, 752),
    'game play time - normal':(850, 660)
}
time.sleep(3)
m = Mouse()
m.click_mouse(dic_of_buttons['select table'])
m.click_mouse(dic_of_buttons['5k payment'])
m.click_mouse(dic_of_buttons['game play time - normal'])
m.click_mouse(dic_of_buttons['play now'])



