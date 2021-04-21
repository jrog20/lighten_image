"""
File: lightperi.py
---------------------
This program lightens an image.
"""

from simpleimage import SimpleImage

def lighter(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red * 1.75
        pixel.green = pixel.green * 1.75
        pixel.blue = pixel.blue * 1.75
    return image

def main():
    original_peri = SimpleImage('images/peri.jpg')
    original_peri.show()

    light_peri = lighter('images/images/peri.jpg')
    light_peri.show()

if __name__ == '__main__':
    main()
