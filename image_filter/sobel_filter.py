from processing_tool import *
from convolution_tool import *

image_skycraper = load('images/skycraper.jpg')
horizontal_sobel_kernel = np.array(
    [
        [1,0,-1],
        [2,0,-2],
        [1,0,-1]
    ])

horizontal_sobel_image = conv(image_skycraper, horizontal_sobel_kernel)
display(greyscale(horizontal_sobel_image), 'Horizontal sobel')

# Vertical Sobel edge filter 
vertical_sobel_kernel = np.array(
    [
        [1,2,1],
        [0,0,0],
        [-1,-2,-1]
    ])

vertical_sobel_image = conv(image_skycraper, vertical_sobel_kernel)
display(greyscale(vertical_sobel_image), 'Vertical sobel')

# I found the addWeighted() method in OpenCV to combine two sobel filters 
# and we can see the vertical edge and  horizontal edge in the image below.

import cv2
combination_sobel_image = cv2.addWeighted(vertical_sobel_image, 0.5, horizontal_sobel_image, 0.5, 0)
display(greyscale(combination_sobel_image), 'Combination image with two sobel filters')