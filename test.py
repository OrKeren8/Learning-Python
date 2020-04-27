from PIL import Image
from PIL import ImageGrab
import time


full_screen = []
for i in range(3):
    image = ImageGrab.grab()
    full_screen.append(image)
    time.sleep(2)

print(full_screen.index(image))