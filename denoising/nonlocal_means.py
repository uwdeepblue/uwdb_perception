import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image
image = cv2.imread("images/noisy_butterfly.jpg", cv2.IMREAD_GRAYSCALE)  # Use IMREAD_COLOR for color images

# Apply Non-Local Means Denoising
denoised_image = cv2.fastNlMeansDenoising(image, None, h=10, templateWindowSize=7, searchWindowSize=21)

# Display the result
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(denoised_image, cmap='gray'), plt.title('Denoised')
plt.show()