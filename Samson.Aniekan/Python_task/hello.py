from PIL import Image

image = Image.open(r"C:\Users\DANIEL\Desktop\cilAssessment\cil-internship-cohort-04\samson.aniekan\python_task\trucking.jpg")

width, height = image.size
 
# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
  
# Cropped image of the dimension given above
# (the original image wouldn't be changed)
im1 = image.crop((left, top, right, bottom))
newsize = (300, 300)
im1 = im1.resize(newsize)
# Shows the image in image viewer
im1.show()


