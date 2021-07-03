from processing_tool import *

mandrill_image = load('images/mandrill.jpg')

# This should crop the eye from the mandrill image
display(crop(mandrill_image, 25, 80, 25, 50), 'cropped image')

display(resize(mandrill_image, 200, 400 ), 'resized image 200,400')

constracted_05_img = change_contrast(mandrill_image, 0.5)
display(constracted_05_img, 'image_change_contrast: 0.5')

# test if the constrast function is reversible
display(change_contrast(constracted_05_img, 2), 'Factor:0.5 -> 2')

constracted_15_img = change_contrast(mandrill_image, 1.5)
display(constracted_15_img, 'image_change_contrast : 1.5')

display(greyscale(mandrill_image), 'greyscale image')
