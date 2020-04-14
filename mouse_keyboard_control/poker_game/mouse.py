from pynput.mouse import Controller
from pynput.mouse import Button
import time


class Mouse:
    after_press_time = 0.5

    # def click_mouse(self, click_coordinates):
    #     Controller.position = click_coordinates
    #     time.sleep(self.after_press_time)
    #     Controller.click(Button.left)
    #     time.sleep(self.after_press_time)
    #
    # def drag_mouse(self, start_coordinates, stop_coordinates):
    #     Controller.position = start_coordinates
    #     time.sleep(self.after_press_time)
    #     Controller.press(Button.left)
    #     time.sleep(self.after_press_time)
    #     Controller.move(stop_coordinates[0] - start_coordinates[0], stop_coordinates[1] - stop_coordinates[1])
    #     time.sleep(self.after_press_time)
    #     Controller.release(Button.left)
    #     time.sleep(self.after_press_time)
