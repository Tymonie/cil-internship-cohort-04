#! /usr/bin/python

from PIL import Image

def Image_resize():
    img = Image.open("Image.jpg") # Opens the desired image.
    img_copy = img.copy()
    height = int(input("Height: ")) # Image height
    width = int(input("Width: ")) # Image width
    img_resize = img_copy.resize((height, width)) # Resize the image
    img_save = img_resize.save("demo.jpg") # Saves the resize image as demo.jpg.
    img_size = print("New image size: {}".format(img_resize.size)) # Prints the size of the resized image.
    img_show = img_resize.show() # Preview the resized image.


Image_resize()