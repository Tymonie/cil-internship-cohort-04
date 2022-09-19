import imghdr
from PIL import Image

image = Image.open('food.jpg')
print(image)
image.show()
print(image.size)
image.thumbnail((2500, 2500))
image.save('image.thumbnail.jpg')

print(image.size) 