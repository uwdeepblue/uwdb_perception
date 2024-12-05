import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image
image = cv2.imread("images/noisy_butterfly.jpg", cv2.IMREAD_GRAYSCALE)  # Use IMREAD_COLOR for color images

# Apply Bilateral Filtering
bilateral_filtered = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

# Display the result
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(bilateral_filtered, cmap='gray'), plt.title('Bilateral Filter')
plt.show()