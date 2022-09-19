import numpy as np
import cv2
import matplotlib.pyplot as plt

path = "./20492e134256739.Y3JvcCw4MDgsNjMyLDAsMA.jpg"


def resize(path,height, width):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img.shape)
    # img = img.resize(height, width)
    img = cv2.resize(img, dsize=(height, width), interpolation=cv2.INTER_CUBIC)
    # print(img.shape)
    plt.imsave('resizedimage.jpg', img)
    
resize(path,200, 200)