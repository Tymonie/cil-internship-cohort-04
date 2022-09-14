
import PIL
from PIL import Image
def main(file_path, x, y):
    image = Image.open(file_path)
    print(image.size)
    resized_image = image.resize((x, y))
    resized_image.save("resized_image.jpg")
main("Image/jumping.jpg", 50, 50)

