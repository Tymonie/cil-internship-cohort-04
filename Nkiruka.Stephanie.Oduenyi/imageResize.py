from PIL import Image
import os, shutil

def resizeImage(imgSrc, imgDest):
    widthRatio = int(input('Enter width ratio: '))
    heightRatio = int(input('Enter height ratio: '))
    #image copy
    original = imgSrc
    target = imgDest
    imgCopy = shutil.copyfile(original, target)


    img = Image.open(imgCopy)
    #img.show()
    
    width, height = img.size
    #print(width, height)

    newWidth = width//widthRatio
    newHeight = height//heightRatio

    resizedImage = img.resize((newWidth, newHeight))
    #print(resizedImage.size)

    #resizedImage.show()
    #resizedImage.save('resizedBaby.jpeg')

    return resizedImage