# import module 
from PIL import Image as img

# first function to copy and rezise an image
def copyRezise(image, w, h):
    copy = img.open('image')
    resize = ((w, h))
    show = resize.show()
    return show 

# calling the fuction
copyRezise('imageFile', 2000, 400)


# second function to copy and rezise an image
def resize(copy, size):
    img_copy = img.open(copy)
    img_size = img_copy.resize(size)
    return img_size.show()

# calling the fuction
resize('imageFile', (2000, 400))

