#Import required Image library
from PIL import Image

#Copy an Image file from the source
im = Image.open("image_file.jpg")

#Display actual image
im.show()

#Resize the image, say half the width and half the size of the original image
resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))

#Display the resized image
resized_im.show()

#Save the resized image
resized_im.save('resized_im.jpg')
