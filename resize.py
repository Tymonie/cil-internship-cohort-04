# using the PIL(pillow) library to resize the image
from PIL import Image #defining the library
def image_resize(url,left,top,bottom,right):
  im = Image.open(url)
  width, height = im.size
  left = 4
  top = height /5
  bottom = 3*height/5 
  right = 151

  im1 = im.crop((4, top, right, bottom))
  newsize = (300,300)
  im1 = im1.resize(newsize)
  im1.show()
#calling the python function
image_resize('jurrasic.jpg')