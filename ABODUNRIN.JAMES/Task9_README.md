# install python from your vscode marketplace
# install the required module for the task 'py -m pip install pillow'

# import module (with an alias if you wish)
from PIL import Image as img

#  save the picture file path into a variable
my_pic = "picture file path on your pc" 

# define your function with two arguments
def resize(copy, size):
#     copy the image
    img_copy = img.open(copy)
#     resize the image
    img_size = img_copy.resize(size)
#     show the image with its new size
    return img_size.show()

# call the function with the right arguments
