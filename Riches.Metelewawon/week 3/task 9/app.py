from PIL import Image


def resize(width,height): #create function

    #open the image which could be jpeg or png
    img_path = "C:\Users\Runzboi\Desktop\cil-intership-04\cil-internship-cohort-04\Riches.Metelewawon\week 3\task 9\christina-rumpf-gUU4MF87Ipw-unsplash.jpg"
    
    img =Image.open(img_path)

    # WIDTH and HEIGHT are integers
    resized_img = img.resize((width,height ))

     #save in either png or jpeg.
    resized_img.save("resized_picture.jpg")
    resized_img.save("resized_picture.png")
    
#Enter any number for the width and height of your picture 
resize(600,500) 