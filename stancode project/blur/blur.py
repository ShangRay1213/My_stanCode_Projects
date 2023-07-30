"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: smiley face
    :return: blurred smiley face
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixels_r = 0
            pixels_b = 0
            pixels_g = 0
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if img.width > x+i >= 0 and img.height > y+j >= 0:
                        pixel = img.get_pixel(x+i, y+j)
                        pixels_r += pixel.red
                        pixels_b += pixel.blue
                        pixels_g += pixel.green
                        count += 1
            new_p = new_img.get_pixel(x, y)
            new_p.red = pixels_r // count
            new_p.blue = pixels_b // count
            new_p.green = pixels_g // count
    return new_img


def main():
    """
    TODO: blur the smiley face
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
