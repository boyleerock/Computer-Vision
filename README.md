# Computer-Vision

***processing_tool.py*** inculdes:
1. **load(img_path)** -> load an image from a file path
2. **print_stats(image)** -> Prints the height, width and number of channels in an image.
3. **crop(image, start_row, start_col, num_rows, num_cols)** -> Crop an image based on the specified bounds. Use array slicing.
4. **change_contrast(image, factor)**-> Change the value of every pixel by following
                                        
                                        x_n = factor * (x_p - 0.5) + 0.5
                                        where x_n is the new value and x_p is the original value.
                                        Assumes pixel values between 0.0 and 1.0 
                                        If you are using values 0-255, change 0.5 to 128.
                                        
5. **resize(input_image, output_rows, output_cols)** -> Resize an image using the nearest neighbor method.
6. **greyscale(input_image)** -> Convert a RGB image to greyscale. 

*** convolution.py *** inculdes:
1. **conv2D(image, kernel)** -> Convolution of a 2D image with a 2D kernel.
2. **test_conv2D():** -> A simple test for your 2D convolution function.
3. **conv(image, kernel)** -> Convolution of a RGB or grayscale image with a 2D kernel
4. **gauss2D(size, sigma)** -> Function to mimic the 'fspecial' gaussian MATLAB function.
5. **corr(image, kernel)** -> Cross correlation of a RGB image with a 2D kernel
