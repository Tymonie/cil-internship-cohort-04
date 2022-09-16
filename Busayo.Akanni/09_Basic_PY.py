from PIL import Image
import PIL
import cv2

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


def ImageResizer3():
  
  img = cv2.imread('demo_image.jpg', cv2.IMREAD_UNCHANGED)
  print('Original Dimensions : ',img.shape)
  scale_percent = 60 # percent of original size
  width = int(img.shape[1] * scale_percent / 100)
  height = int(img.shape[0] * scale_percent / 100)
  dim = (width, height)
  
  # resize image
  resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  print('Resized Dimensions : ',resized.shape)
  cv2.imshow("Resized image", resized)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
ImageResizer3