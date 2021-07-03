from processing_tool import *
from convolution_tool import *

mandrill_image = load('images/mandrill.jpg')

#create a 5x5 Gaussian kernel with sigma = 1.0
gaussian_kernel_5_10 = gauss2D(5, 1.0) 
display(gaussian_kernel_5_10, 'Gaussian kernel, 5x5, sigma=1.0')

gaussian_kernel_5_10_image = conv(mandrill_image, gaussian_kernel_5_10)
display(gaussian_kernel_5_10_image, 'Gaussian kernel image, 5x5, sigma=1.0')

#create a 15x15 Gaussian kernel with sigma = 4.0
gaussian_kernel_15_40 = gauss2D(15, 4.0) 
display(gaussian_kernel_15_40, 'Gaussian kernel, 15x15, sigma=4.0')

gaussian_kernel_15_40_image = conv(mandrill_image, gaussian_kernel_15_40)
display(gaussian_kernel_15_40_image, 'Gaussian kernel image, 15x15, sigma=4.0')

# See what is lost when filtering:

# resize to the same size first
image1_288 = resize(mandrill_image, 288, 288)
# Then subtract the filtered image from the origina
display(image1_288 - gaussian_kernel_15_40_image, 'The lost information')

