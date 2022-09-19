from PIL import Image
import glob,os
#This Is the function called resizer
def Resizer(File_path,Image_name,Base_width,Base_height,New_Image_name):
    # We open the picture
    im = Image.open(os.path.join(File_path,Image_name))
    im.show()
    # We resize the image based on the width and height provided
    im = im.resize((Base_width,Base_height),Image.ANTIALIAS)
    # The image is then saved
    im.save(os.path.join(File_path,New_Image_name)+'.jpeg')
    #Then we show the resized image again.
    im = Image.open(os.path.join(File_path,New_Image_name))
    im.show()
