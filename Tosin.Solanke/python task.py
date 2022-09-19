
from PIL import Image as img
my_pic = "picture file path on your pc" 
def resize(copy, size):
    img_copy = img.open(copy)
    img_size = img_copy.resize(size)
    return img_size.show()
