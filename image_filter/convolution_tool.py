import math
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

def conv2D(image, kernel):
    """ Convolution of a 2D image with a 2D kernel. 
    Convolution is applied to each pixel in the image.
    Assume values outside image bounds are 0.
    
    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    out = None
    padding = 1
    imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
    imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
    # print(imagePadded)

    h_imagepadded, w_imagepadded = imagePadded.shape
    h_kernel, w_kernel = kernel.shape
    out = np.zeros((h_imagepadded - h_kernel +1, w_imagepadded - w_kernel +1))
    
    # out[0, 0] = (kernel * imagePadded[0: h_kernel, 0: h_kernel]).sum()
    # print(out[0, 0])
    
    for i in range(h_imagepadded - h_kernel +1):
        for j in range(w_imagepadded - w_kernel +1):
            out[i, j] = (kernel * imagePadded[i: i + h_kernel, j: j + h_kernel]).sum()

    return out
    
def test_conv2D():
    """ A simple test for your 2D convolution function.
        You can modify it as you like to debug your function.
    
    Returns:
        None
    """

    # Test code written by 
    # Simple convolution kernel.
    kernel = np.array(
    [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ])
    
    
    # Create a test image: a white square in the middle
    test_img = np.array(
    [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ])

    # Run your conv_nested function on the test image
    test_output = conv2D(test_img, kernel)

    # Build the expected output
    expected_output = np.zeros((5, 5))
    expected_output = np.array(
    [
         [ 16,27,33,39,28],
         [ 39,63,72,81,57],
         [ 69,108,117,126,87],
         [ 99,153,162,171,117],
         [ 76,117,123,129,88]
    ])
    # print(test_output)
    
    # Test if the output matches expected output
    assert np.max(test_output - expected_output) < 1e-10, "Your solution is not correct."

def conv(image, kernel):
    """Convolution of a RGB or grayscale image with a 2D kernel
    
    Args:
        image: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
    """
    out = None
    
    if len(image.shape) == 2:			 # grayscale image is 2D
    	out = conv2D(image, kernel)
    elif len(image.shape) == 3:			 # RGB image is 3D
    	# Applying the 2D convolution to each channel independently.
    	r = conv2D(image[:,:,0], kernel) 
    	g = conv2D(image[:,:,1], kernel)
    	b = conv2D(image[:,:,2], kernel)
    	#and then make these three channel stacked to a new RGB image
    	out = np.stack((r, g, b), axis=2)
    	# print(out.shape)
    return out

    
def gauss2D(size, sigma):

    """Function to mimic the 'fspecial' gaussian MATLAB function.
       You should not need to edit it.
       
    Args:
        size: filter height and width
        sigma: std deviation of Gaussian
        
    Returns:
        numpy array of shape (size, size) representing Gaussian filter
    """

    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()


def corr(image, kernel):
    """Cross correlation of a RGB image with a 2D kernel
    
    Args:
        image: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
    """
    out = None
    
    filpped_kernel = np.flip(kernel,1)
    # print(filpped_kernel)

    out = conv(image, filpped_kernel)

    return out
