from PIL import ImageGrab
from PIL import ImageChops
import time
from PIL import Image
import datetime

class Pictures:
    x_base_card_coor = 753
    y_base_card_coor = 491
    card_length = 23
    card_width = 26
    between_cards = 86
    pic_list = []

    @staticmethod
    def screen_pic():
        full_screen = ImageGrab.grab()
        return full_screen

    def specific_pic(self, area):
        cropped_image = self.screen_pic().crop(area)
        return cropped_image

    def desk_cards_pics(self):
        for i in range(5):
            whole_card = self.specific_pic((self.x_base_card_coor + self.between_cards * i + i,
                                            self.y_base_card_coor,
                                            self.x_base_card_coor + self.card_width + self.between_cards * i + i,
                                            self.y_base_card_coor + self.card_length))
            # whole_card = whole_card.convert('1')
            # up_half_card = whole_card.crop((0, 0, 23, 23))
            # down_half_card = whole_card.crop((0, 26, 28, 49))
            # self.pic_list.append(up_half_card)
            # self.pic_list.append(down_half_card)
            self.pic_list.append(whole_card)
        return self.pic_list

    def collect_numbers(self, iterations, delay=0):
        for _ in range(iterations):
            time.sleep(delay)
            self.desk_cards_pics()
        for item in self.pic_list:
            if_num = self.check_if_card_num(item)
            if not if_num:
                self.pic_list.remove(item)
        self.save_photo_list(self.pic_list)

    @staticmethod
    def check_if_card_num(compare_image):
        image1 = Image.open('0.jpg')
        image2 = Image.open('1.jpg')
        test = Image.open('54.jpg')
        diff1 = ImageChops.difference(image1, test)
        diff2 = ImageChops.difference(image2, test)
        if not diff1.getbbox() or not diff2.getbbox():
            return False
        print('1' + str(diff1.getbbox()))
        print('2' + str(diff2.getbbox()))
        diff1.show()
        diff2.show()
        return True

    @staticmethod
    def save_photo_list(picture_list, start_num=2):
        for i in picture_list:
            i.save(str(start_num)+".jpg")
            start_num += 1

# time.sleep(3)
# pic = Pictures()
# pic.desk_cards_pics()
