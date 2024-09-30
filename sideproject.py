import math
from PIL import Image


image = Image.open('invert.png')
def invert(image):
    data = image.load()
    blank_image = Image.new('RGB', (image.width, image.height))
    blank_image_data = blank_image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = data[x, y]
            blank_image_data[x, y] = (255 - r, 255 - g, 255 - b)
    return blank_image

invert1 = invert(image)
invert1.save('invert.png')
        

