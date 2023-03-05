import cv2
import numpy


original = cv2.imread('images/original_golden_bridge.jpg')# open an image and store it inside an object
duplicate = cv2.imread('images/black_and_white.jpg')

# original = cv2.imread('images/1.jpg')# open an image and store it inside an object
# duplicate = cv2.imread('images/10.jpg')

cv2.imshow('original', original)# show the image in a new window
cv2.imshow('duplicate', duplicate)

# 1) check if two images are equal
image1 = original.shape# place inside 'image1' the pixels of the picture and its type
image2 = duplicate.shape
print(image1)
print(image2)

if original.shape == duplicate.shape:
    print('the images have same size and channels')
    difference = cv2.subtract(original, duplicate)# subtract every pixel of the images
    cv2.imshow("difference", difference)

    b, g, r = cv2.split(difference)# split the image colors to red green and blue
    cv2.imshow('b', b)
    cv2.imshow('g', g)
    cv2.imshow('r', r)

    # 'cv2.countNonZero(b)' count how many pixels are not zero - have some color in them
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print('the images are completely equal')
    else:
        print('the images are not equal')

cv2.waitKey(0)# i don't really know what each of this line do but they are essential to show the pictures
cv2.destroyAllWindows()
