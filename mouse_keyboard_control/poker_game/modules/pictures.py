from PIL import ImageGrab
from PIL import Image
import time
import datetime

class Pictures:

    @staticmethod
    def screen_pic():
        full_screen = ImageGrab.grab()
        return full_screen


    # @staticmethod
    def specific_pic(self, area):
        cropped_image = self.screen_pic().crop(area)
        return cropped_image


a = Pictures()
a.specific_pic((100, 100, 200, 200)).show()

