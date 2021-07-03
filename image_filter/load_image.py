from processing_tool import *
from convolution_tool import *

mandrill_image = load('images/mandrill.jpg')
display(mandrill_image, 'Mandrill')
print_stats(mandrill_image)

image_skycraper = load('images/skycraper.jpg')
display(image_skycraper, 'Skycraper')
print_stats(image_skycraper)

man_image = load('images/man.jpg')
display(man_image, 'Man')
print_stats(man_image)