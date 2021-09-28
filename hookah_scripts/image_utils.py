import cv2
import numpy
import random

HOOKAH_SHOWCASE_WINDOW_NAME = "hookah window nigger"
MAX_RGB = 255
WHITE_PIXEL = (255, 255, 255)
BLACK_PIXEL = (0, 0, 0)
black_threshold = 20
white_threshold = 200


def show_image(image: numpy.ndarray):
    image = cv2.resize(image, (image.shape[0] * 3, image.shape[1] * 3))
    cv2.imshow(HOOKAH_SHOWCASE_WINDOW_NAME, image)
    cv2.waitKey(2)


def is_black_pixel(tested_pixel):
    return not all([cord > black_threshold for cord in tested_pixel])


def is_white_pixel(tested_pixel):
    return all([cord > white_threshold for cord in tested_pixel])


def get_color_in_range(base_color: tuple, diff=7):
    return random.randint(base_color[0], base_color[0] + diff), \
           random.randint(base_color[1], base_color[1] + diff), random.randint(base_color[2], base_color[2] + diff)


def paint_horizontally(image: numpy.ndarray, num_parts):
    height, width = image.shape[0:2]
    for i in range(1, num_parts + 1):
        random_int = 3
        print(random_int)
        color = random.randint(0, MAX_RGB), random.randint(0, MAX_RGB), random.randint(0, MAX_RGB)

        sizeof_part = height / num_parts
        for x in range(int((sizeof_part * i) - sizeof_part), int(sizeof_part) * i):
            for y in range(width):
                if is_black_pixel(tuple(image[x][y])):
                    image[x][y] = BLACK_PIXEL
                elif is_white_pixel(tuple(image[x][y])):
                    image[x][y] = WHITE_PIXEL
                else:
                    #image[x][y] = (155, 155, 155)
                    image[x][y] = [(color[i] + image[x][y][i]) % MAX_RGB for i in range(3)]
    return image


def paint_picture(image: numpy.ndarray):
    while True:
        copy = numpy.copy(image)
        pic1 = paint_horizontally(copy, random.randint(1,10))
        show_image(pic1)

    return paint_horizontally(image, 5)
