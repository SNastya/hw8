import argparse
import os
import sys
from PIL import Image, ImageDraw


def negative(image_path):
    image_pic = Image.open(image_path)
    width, height = image_pic.size
    pix = image_pic.load()
    draw = ImageDraw.Draw(image_pic)
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
    image_pic.save('negative_' + image_path)
    image_path = os.path.abspath(image_path)
    return image_path


def sepia(image_path):
    image_pic = Image.open(image_path)
    width, height = image_pic.size
    pix = image_pic.load()
    draw = ImageDraw.Draw(image_pic)
    depth = 30
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))
    image_pic.save('sepia_'+ image_path)
    image_path = os.path.abspath(image_path)
    return image_path


def b_w(image_path):
    image_pic = Image.open(image_path)
    width, height = image_pic.size
    pix = image_pic.load()
    draw = ImageDraw.Draw(image_pic)

    factor = 100

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > (((255 + factor) // 2) * 3):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    image_pic.save('b_w_' + image_path)
    image_path = os.path.abspath(image_path)
    return image_path


def replace():
    parser = argparse.ArgumentParser()
    parser.add_argument('-im_n', '--image_name', type=str)
    parser.add_argument('-f', '--filter', type=str)
    namespace = parser.parse_args(sys.argv[1:])
    image = namespace.image_name
    print(image)
    # image = Image.open(image)
    filter = namespace.filter

    if filter == 'negative':
        old_path = negative(image)
    elif filter == 'black_n_white':
        old_path = b_w(image)
    elif filter == 'sepia':
        old_path = sepia(image)

    old_path = os.path.abspath(image)
    old_path = os.path.dirname(old_path)
    new_path = os.path.dirname(old_path) + '\\filtered_image'

    if os.path.exists(new_path) == True:
        os.replace(old_path + '\\' + image, new_path + '\\' + image)

    elif os.path.exists(new_path) == False:
        os.replace(old_path + '\\' + image, str(os.mkdir(new_path)) + '\\' + image)

    return parser


if __name__ == '__main__':
    replace()
