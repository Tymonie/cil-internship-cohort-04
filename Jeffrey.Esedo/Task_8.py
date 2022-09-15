
from email.mime import image
from PIL import Image

def resize_jpg(filepath):
    # Open image
    im= Image.open(filepath)
    #copy image
    copy_img= im.copy()
    # Size of the image in pixels (size of original image)
    width, height = im.size
    # setting points for crop image 
    left = 4
    top = height / 5
    right = 154
    bottom = 3 * height / 5
    # crop image 
    crop_img = copy_img.crop((left, top, right, bottom))
    newsize = (300, 300)
    img1 = crop_img.resize(newsize)
    new_img= img1.show()
    return new_img

resize_jpg(input(f"filepath:"))