import cv2
from common_functions import *


def blur(image):
    return cv2.bilateralFilter(image, 9, 175, 175)
    # return cv2.GaussianBlur(image, (11, 11), 0)


def gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def process_image(image, functions=[gray, blur]):
    for function in functions:
        image = function(image)
    return image


if __name__ == "__main__":
    image = cv2.imread("cuboid.jpeg")
    processed_image = process_image(image)
    show_image("Processed Image", processed_image)
