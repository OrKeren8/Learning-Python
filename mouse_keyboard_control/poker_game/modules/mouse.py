from pynput.mouse import Controller
from pynput.mouse import Button
import time

class Mouse:
    after_press_time = 0.5
    mouse_cont = Controller()

    def click_mouse(self, click_coordinates):
        self.mouse_cont.position = click_coordinates
        time.sleep(self.after_press_time)
        self.mouse_cont.click(Button.left)
        time.sleep(self.after_press_time)

    def drag_mouse(self, start_coordinates, stop_coordinates):
        self.mouse_cont.position = start_coordinates
        time.sleep(self.after_press_time)
        self.mouse_cont.press(Button.left)
        time.sleep(self.after_press_time)
        self.mouse_cont.move(stop_coordinates[0] - start_coordinates[0], stop_coordinates[1] - stop_coordinates[1])
        time.sleep(self.after_press_time)
        self.mouse_cont.release(Button.left)
        time.sleep(self.after_press_time)