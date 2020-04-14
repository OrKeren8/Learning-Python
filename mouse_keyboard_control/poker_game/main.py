from .mouse import Mouse
import time

dic_of_buttons = {
    'select table': (1123, 711),
    '5k payment': (608, 500),
    '500k payment': (733, 500),
}
m = Mouse()
time.sleep(3)
m.click_mouse(dic_of_buttons['select table'])
m.drag_mouse(dic_of_buttons['5k payment'], dic_of_buttons['500k payment'])

# mouse.position = dic_of_buttons['5k payment']
# time.sleep(0.5)
# mouse.press(Button.left)
# time.sleep(0.5)
# mouse.move(dic_of_buttons['500k payment'][0] - dic_of_buttons['5k payment'][0], dic_of_buttons['500k payment'][1] - dic_of_buttons['5k payment'][1])
# time.sleep(0.5)
# mouse.release(Button.left)