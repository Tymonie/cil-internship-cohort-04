# Simple function to copy and resize a jpg file
requirement to run the function
* pip install opencv-python
* python 3.7 and above

```python 
import cv2
path_to_image = ""      # image path can is placed as string here


# function that displays the image
def show_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function to copy and resize an image by a percentage of its original size
# percent_size_change expects a float number between 0.1 - 1.0 for reduction in size and above 1.0 for increase
def copy_n_resize_image(image_path, percent_size_change):
    # opens the image
    image = cv2.imread(image_path)

    image_copy = image.copy()   # makes a copy of the image

    # new size of copied image
    width = int(image_copy.shape[1] * percent_size_change)
    height = int(image_copy.shape[0] * percent_size_change)
    dimension = (width, height)

    # image resizing and display to visually compare with original
    resized_image_copy = cv2.resize(image_copy, dimension, interpolation=cv2.INTER_AREA)
    show_image(image)
    show_image(resized_image_copy)
    return resized_image_copy

copy_n_resize_image(path_to_image, 0.1)
```