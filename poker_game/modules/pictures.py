from PIL import ImageGrab
from PIL import ImageChops
import time
from PIL import Image
import datetime


class Pictures:
    desk_cards_nums = {
        'x base card coor': 753,
        'y base card coor': 491,
        'card length': 23,
        'card width': 26,
        'between cards': 86,
        'thresh hold': 220
    }

    desk_cards_shapes = {
        'x base card coor': 745,
        'y base card coor': 518,
        'card length': 15,
        'card width': 26,
        'between cards': 86,
        'thresh hold': 220
    }


    @staticmethod
    def screen_pic():
        full_screen = ImageGrab.grab()
        return full_screen


    def specific_pic(self, area):
        cropped_image = self.screen_pic().crop(area)
        return cropped_image


    def desk_cards_nums_pics(self):
        """
        method that takes 5 images of the card's number on the poker desk
        :return: a list if the 5 images
        """
        pic_list = []
        for i in range(5):
            card_num = self.specific_pic((self.desk_cards_nums['x base card coor'] + self.desk_cards_nums['between cards'] * i + i,
                                            self.desk_cards_nums['y base card coor'],
                                            self.desk_cards_nums['x base card coor'] + self.desk_cards_nums['card width'] + self.desk_cards_nums['between cards'] * i + i,
                                            self.desk_cards_nums['y base card coor'] + self.desk_cards_nums['card length']))

            card_shape = self.specific_pic((self.desk_cards_shapes['x base card coor'] + self.desk_cards_shapes['between cards'] * i + i*3,
                                            self.desk_cards_shapes['y base card coor'],
                                            self.desk_cards_shapes['x base card coor'] + self.desk_cards_shapes['card width'] + self.desk_cards_shapes['between cards'] * i + i*3,
                                            self.desk_cards_shapes['y base card coor'] + self.desk_cards_shapes['card length']))

            pic_list.append((card_num, card_shape))
        return pic_list


    def collect_numbers(self, iterations, start_num, delay=0):
        """
        takes several screenshots of the card's number on the desk and save them only if they are known numbers
        :param iterations: how many times the program take the screenshots
        :param start_num: the first index of the pictures that will be saved
        :param delay: the time between every screenshot in seconds
        :return: None
        """
        pic_num = start_num
        for iteration in range(iterations):
            time.sleep(delay)
            pic_list = self.desk_cards_nums_pics()
            for pic in pic_list:
                card_num = self.check_if_card(pic)
                if card_num != 101:
                    self.save_photo(pic, pic_num, 'desk nums')
                    pic_num += 1


    def check_if_card(self, compare_image):
        reference_images  = []
        for num in range(1, 14):
            image = Image.open('images/a desk nums {}.jpg'.format(num))
            reference_images.append(image)
        card_num = self.check_similarity(compare_image, reference_images, self.desk_cards_nums['thresh hold'])
        return card_num


    @staticmethod
    def check_similarity(image1, comp_images, threshold):
        """
        check the most similarity from a list of images to one additional pic
        :param image1: first image
        :param comp_images: list of images
        :param threshold: the maximum amount of different pixels to consider the pic as one of the list
        :return: the place in the list of the correct card
        """
        min_diff_pixels = threshold
        the_image = 101
        index = 0
        image1 = image1.convert('1')

        for image in comp_images:
            image = image.convert('1')
            diff = ImageChops.difference(image1, image)
            pix_val = list(diff.getdata())
            diff_pixels = 0
            for pixel in pix_val:
                if pixel != 0:
                    diff_pixels += 1
            if diff_pixels < min_diff_pixels:
                min_diff_pixels = diff_pixels
                the_image = index
            index += 1
        return the_image


    @staticmethod
    def save_photo(image, pic_num, pre_name):
        """
        save a given photo
        :param image: the image object to save
        :param pic_num: the index of the saved image name
        :param pre_name: the image name
        :return: None
        """
        image.save('images/{} {}.jpg'.format(str(pre_name), str(pic_num)))

'''
    def check_if_card_num(self, compare_image):
        """
        compere every card number that can be on the desk to the given image and check if one of them are equal
        :param compare_image: the new image that have taken
        :return: if the new image is a number from the desk
        """
        for num in range(1, 14):
            reference_image = Image.open('images/desk nums {}.jpg'.format(num))
            equal = self.check_similarity(reference_image, compare_image, self.desk_cards_nums['thresh hold'])
            if equal is True:
                return True
        return False
'''
'''
    @staticmethod
    def check_similarity(image1, image2, threshold):
        """
        check if the two given images are the same, it consider a minimal change of threshold
        :param image1: first image
        :param image2: second image
        :param threshold: the maximum amount of different pixels to consider the two images as equal
        :return: True for similarity and False for not
        """
        image1 = image1.convert('1')
        image2 = image2.convert('1')
        diff = ImageChops.difference(image1, image2)
        pix_val = list(diff.getdata())
        diff_pixels = 0
        for pixel in pix_val:
            if pixel != 0:
                diff_pixels += 1
        if diff_pixels < threshold:
            return True
        return False
'''