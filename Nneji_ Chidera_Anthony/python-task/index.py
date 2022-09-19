from PIL import Image

def resizeimage(width,height):

 img1 =Image.open(img1.jpg)   
 img2 =Image.open(img2.jpg)   
 img3 =Image.open(img3.jpg)

 resized_img = img1.resize(width,height)   
 resized_img = img2.resize(width,height)   
 resized_img = img3.resize(width,height) 

 resized_img.save("optmize_pictuew.png") 

 resizeimage(200, 500)
