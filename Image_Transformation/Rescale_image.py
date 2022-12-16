from skimage import color, data, io
from skimage.transform import rescale
import matplotlib.pyplot as plt

# loading gray astronaut image from database
image = color.rgb2gray(data.astronaut())

# showing original image
plt.title("Original Image")
io.imshow(image)
io.show()

# rescaling to 1/4th of original image
rescaled_img = rescale(image, 0.25, anti_aliasing=False)

#Displaying rescaled image
plt.title("Rescaled Image")
io.imshow(rescaled_img)
io.show()
