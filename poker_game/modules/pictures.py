from PIL import ImageGrab
from PIL import ImageChops
import time
from PIL import Image
import datetime


class Pictures:
    cards = {
        'desk num path': 'images/all numbers/',
        'desk num name': 'a desk nums',
        'desk num x base card coor': 753,
        'desk num y base card coor': 491,
        'desk num card length': 23,
        'desk num card width': 26,
        'desk num between cards': 86,
        'desk num thresh hold': 220,
        'desk shape path': 'images/all shapes/',
        'desk shape name': 'a desk shapes',
        'desk shape x base card coor': 747,
        'desk shape y base card coor': 518,
        'desk shape card length': 15,
        'desk shape card width': 26,
        'desk shape between cards': 86,
        'desk shape thresh hold': 70,

        '1 hand num path': 'images/first hand nums/',
        '1 hand num name': 'a hand nums',
        '1 hand num x base card coor': 848,
        '1 hand num y base card coor': 786,
        '1 hand num card length': 39,
        '1 hand num card width': 55,
        '1 hand num between cards': 0,
        '1 hand num thresh hold': 220,
        '1 hand shape path': 'images/first hand shapes/',
        '1 hand shape name': 'a hand shapes',
        '1 hand shape x base card coor': 862,
        '1 hand shape y base card coor': 834,
        '1 hand shape card length': 42,
        '1 hand shape card width': 27,
        '1 hand shape between cards': 0,
        '1 hand shape thresh hold': 70
    }


    @staticmethod
    def screen_pic():
        full_screen = ImageGrab.grab()
        return full_screen


    def specific_pic(self, area):
        cropped_image = self.screen_pic().crop(area)
        return cropped_image


    def card_pics(self, card_type, pics):
        """
        :param card_type: the type of the card, from desk, 1 hand, 2 hand ...
        :param pics: how many pics there are to take
        method that takes 5 images of the card's number and 5 shots of the card's shape on the poker desk
        :return: a list of 5 tuples first item for the card num and the second for it's shape
        """
        pic_list = []
        for i in range(pics):
            card_num = self.specific_pic((self.cards['{} num x base card coor'.format(card_type)] + self.cards['{} num between cards'.format(card_type)] * i + i,
                                            self.cards['{} num y base card coor'.format(card_type)],
                                            self.cards['{} num x base card coor'.format(card_type)] + self.cards['{} num card width'.format(card_type)] + self.cards['{} num between cards'.format(card_type)] * i + i,
                                            self.cards['{} num y base card coor'.format(card_type)] + self.cards['{} num card length'.format(card_type)]))

            card_shape = self.specific_pic((self.cards['{} shape x base card coor'.format(card_type)] + self.cards['{} shape between cards'.format(card_type)] * i + i*3,
                                            self.cards['{} shape y base card coor'.format(card_type)],
                                            self.cards['{} shape x base card coor'.format(card_type)] + self.cards['{} shape card width'.format(card_type)] + self.cards['{} shape between cards'.format(card_type)] * i + i*3,
                                            self.cards['{} shape y base card coor'.format(card_type)] + self.cards['{} shape card length'.format(card_type)]))

            pic_list.append((card_num, card_shape))
        return pic_list


    def collect_cards(self, card_type, num_of_cards, iterations, start_num, delay=0, debug=False):
        """
        takes several screenshots of the card's number and shapes and save them only if they are known
        :param card_type: the type of the card, from desk, 1 hand, 2 hand ...
        :param num_of_cards: how many cards there are to collect each time
        :param iterations: how many times the program take the screenshots
        :param start_num: the first index of the pictures that will be saved
        :param delay: the time between every screenshot in seconds
        :param debug: True for debug mode
        :return: None
        """
        card = [101, 101]
        nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        shapes = ['heart', 'diamond', 'spades', 'clubs']
        pic_num = start_num
        for iteration in range(iterations):
            time.sleep(delay)
            pic_list = self.card_pics(card_type, num_of_cards)
            for pic in pic_list:
                card[0] = self.check_similarity(pic[0], self.ref_image_list(self.cards['{} num path'.format(card_type)], self.cards['{} num name'.format(card_type)]), self.cards['{} num thresh hold'.format(card_type)], black_and_white=True)
                card[1] = self.check_similarity(pic[1], self.ref_image_list(self.cards['{} shape path'.format(card_type)], self.cards['{} shape name'.format(card_type)]),self.cards['{} shape thresh hold'.format(card_type)])
                if card[0] != 101 and card[1] != 101:
                    if debug:
                        print('{} of {}'.format(nums[card[0]], shapes[card[1]]))
                    self.save_photo(pic[0], self.cards['{} num path'.format(card_type)], '{} desk nums'.format(card_type), pic_num)
                    self.save_photo(pic[1], self.cards['{} shape path'.format(card_type)], '{} desk shapes'.format(card_type), pic_num)
                    pic_num += 1


    def check_deck_cards(self, card_type, num_of_cards, debug=False):
        """
        takes a screenshot of the card's numbers and shapes on the desk and and return their value
        :param card_type: the type of the card, from desk, 1 hand, 2 hand ...
        :param num_of_cards: how many cards there are to collect each time
        :param debug: True to print the values
        :return: the cards and their shapes
        """
        card = [101, 101]
        nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        shapes = ['heart', 'diamond', 'spades', 'clubs']
        pic_list = self.card_pics(card_type, num_of_cards)
        value = []
        for pic in pic_list:
            card[0] = self.check_similarity(pic[0], self.ref_image_list(self.cards['{} num path'.format(card_type)], self.cards['{} num name'.format(card_type)]), self.cards['{} num thresh hold'.format(card_type)], black_and_white=True)
            card[1] = self.check_similarity(pic[1], self.ref_image_list(self.cards['{} shape path'.format(card_type)], self.cards['{} shape name'.format(card_type)]),self.cards['{} shape thresh hold'.format(card_type)])
            if card[0] != 101 and card[1] != 101:
                if debug:
                    print('{} of {}'.format(nums[card[0]], shapes[card[1]]))
                value.append([nums[card[0]], shapes[card[1]]])
            else:
                value.append([None, None])
        return value


    @staticmethod
    def ref_image_list(ref_images_path, ref_images_name):
        """
        takes the path and the name of the referense images and append them to one list of comparable images
        :param ref_images_path: the path which the images are in
        :param ref_images_name: the 'first name' of this type of images
        :return: return the referense list of images
        """
        reference_images = []
        for i in range(1, 27):
            try:
                image = Image.open('{}{} {}.jpg'.format(ref_images_path, ref_images_name, i))
                reference_images.append(image)
            except FileNotFoundError:
                break
        return reference_images


    @staticmethod
    def check_similarity(image1, comp_images, threshold, black_and_white=False, debug=False):
        """
        check the most similarity from a list of images to one additional pic
        :param image1: first image
        :param comp_images: list of images
        :param threshold: the maximum amount of different pixels to consider the pic as one of the list
        :param black_and_white: put true only if can be two images that are the same but with different colors
        :param debug: true for debug mode
        :return: the place in the list of the correct card
        """
        min_diff_pixels = threshold
        the_image = 101
        index = 0
        if black_and_white:
            image1 = image1.convert('1')

        for image in comp_images:
            if black_and_white:
                image = image.convert('1')
            diff = ImageChops.difference(image1, image).convert('1')
            pix_val = list(diff.getdata())
            diff_pixels = 0
            for pixel in pix_val:
                if pixel != 0:
                    diff_pixels += 1
            if debug is True:
                print('the amount of diff pixels from reference is {}'.format(diff_pixels))
            if diff_pixels < min_diff_pixels:
                min_diff_pixels = diff_pixels
                the_image = index
            index += 1
        return the_image


    @staticmethod
    def save_photo(image, path, pre_name, pic_num ):
        """
        save a given photo
        :param image: the image object to save
        :param path: the path of the saved image
        :param pic_num: the index of the saved image name
        :param pre_name: the image name
        :return: None
        """
        image.save('{}{} {}.jpg'.format(path, str(pre_name), str(pic_num)))
