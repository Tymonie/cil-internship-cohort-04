
import PIL
from PIL import Image
def main(file_name):
    image = Image.open(file_name)
    print(image.size)
    resized_image = image.resize((200, 200))
    resized_image.save("resized_image.jpg")
main("Image/MyPicture.jpg")

