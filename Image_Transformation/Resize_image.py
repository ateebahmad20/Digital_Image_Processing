from skimage import color, data, io
from skimage.transform import resize
import matplotlib.pyplot as plt

# loading gray astronaut image from database
image = color.rgb2gray(data.astronaut())

# showing original image
plt.title("Original Image")
io.imshow(image)
io.show()

# resizing original image
resized_img = resize(image, (100, 200))

#Displaying Resized image
plt.title("Resized Image")
io.imshow(resized_img)
io.show()
