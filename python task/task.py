from PIL import Image
def resize(width,height): #create function
    #open the image which could be jpeg or png
    img = Image.open("picture.jpg")
    # WIDTH and HEIGHT are integers
    resized_img = img.resize((width,height ))
    resized_img.save("resized_picture.jpg") #save in either png or jpeg.
    resized_img.save("resized_picture.png")
resize(600,500) #Enter any number for the width and height of your picture 