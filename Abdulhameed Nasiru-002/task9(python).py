from PIL import Image

def resize(im,new_width):
    width,height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = im.resize((new_width,new_height))
    return resized_image
im = Image.open("images/sample.jpg")

im_resized = resize(im,200)
im_resized.save("images/sample1.jpg")
im_resized.show()
