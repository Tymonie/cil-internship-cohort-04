from PIL import Image
import PIL

## First method up for consideration
def ImageResizer1():

  image = Image.open('demo_image.jpg')
  print(image.size)
  image.thumbnail((400, 400))
  image.save('image_thumbnail.jpg')
  print(image.size) 

ImageResizer1()


## Second method up for consideration
def ImageResizer2():
  fixed_height = 420
  image = Image.open('demo_image.jpg')
  print(image.size)
  height_percent = (fixed_height / float(image.size[1]))
  width_size = int((float(image.size[0]) * float(height_percent)))
  image = image.resize((width_size, fixed_height), PIL.Image.Resampling.NEAREST)
  image.save('resized_nearest.jpg')
  print(image.size)

ImageResizer2()