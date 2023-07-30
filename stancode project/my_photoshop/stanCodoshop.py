"""
File: stanCodoshop.py
Name: Ray
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    pixel_avg = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5
    print(pixel_avg)
    return pixel_avg


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red = 0
    green = 0
    blue = 0
    avg = []
    for i in range(len(pixels)):
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    avg.append(red//len(pixels))
    avg.append(green//len(pixels))
    avg.append(blue//len(pixels))
    return avg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    smallest = 256
    best_pixel = []
    avg_color = get_average(pixels)
    avg_r = avg_color[0]
    avg_g = avg_color[1]
    avg_b = avg_color[2]

    for i in range(len(pixels)):
        if abs(pixels[i].red - avg_r) + abs(pixels[i].green - avg_g) + abs(pixels[i].blue - avg_b) < smallest:
            smallest = abs(pixels[i].red - avg_r) + abs(pixels[i].green - avg_g) + abs(pixels[i].blue - avg_b)
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    for x in range(width):
        for y in range(height):
            pixels = []  # A list of pixels at (x, y) from different images.
            for image in images:
                img_pixel = image.get_pixel(x, y)
                pixels.append(img_pixel)
            best = get_best_pixel(pixels)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
