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


time.sleep(3)
a = Pictures()
one = 85
three = 95
d = []
for i in range(5):
    d.append(a.specific_pic((750 + one*i, 487, 811 + three*i, 576)))
time.sleep(3)
for i in d:
    i.show()

