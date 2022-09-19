from PIL import Image

# The new size we want to resize our jpg file.
size = (350, 350)

def remake_image(filename):
    """A function that returns a neatly resized jpg file."""

    image = Image.open(filename, 'r')

    # Size of the image in pixels (size of original image)
    # (This is not mandatory, but for clarify we print the width and height
    # to know the original structure of our image)

    width, height = image.size
    print(width, height)

    # resized image of above dimension
    # (It will not change original image)
    resized_image = image.resize(size)

    # we show the image first to confirm
    # acceptance before saving it with another name.
    return resized_image.show()

    #resized_image.save('new_photo.jpg')


filename = input('enter a .jpg file - ')
remake_image(filename)
