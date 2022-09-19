import shutil
from PIL import Image

def resize_img(image_loc, new_width, new_height):
    # shutil.copy(image,"image2.png")
    
    image = Image.open(image_loc)
    image.thumbnail((new_width, new_height), Image.ANTIALIAS)
    image.save('resized_image', 'JPEG', quality=88)
    
resize_img("lion.jpeg", 200, 40)