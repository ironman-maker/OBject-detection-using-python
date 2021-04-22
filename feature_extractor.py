import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from skimage.io import imread, imshow

image = imread('image_8_original.png', as_gray=True)
imshow(image)

#checking image shape 
image.shape, image
view raw

image = imread('puppy.jpeg', as_gray=True) 
image.shape, imshow(image)

#pixel features

features = np.reshape(image, (660*450))

features.shape, features

image = imread('puppy.jpeg') 
image.shape
view raw

image = imread('puppy.jpeg')
feature_matrix = np.zeros((660,450)) 
feature_matrix.shape

for i in range(0,iimage.shape[0]):
    for j in range(0,image.shape[1]):
        feature_matrix[i][j] = ((int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2]))/3)
features = np.reshape(feature_matrix, (660*450)) 
features.shape


#calculating horizontal edges using prewitt kernel
edges_prewitt_horizontal = prewitt_h(image)
#calculating vertical edges using prewitt kernel
edges_prewitt_vertical = prewitt_v(image)

imshow(edges_prewitt_vertical, cmap='gray')
