import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.restoration import denoise_wavelet
from skimage import img_as_float, img_as_ubyte

# Load an image
image = cv2.imread("images/noisy_butterfly.jpg", cv2.IMREAD_GRAYSCALE)  # Use IMREAD_COLOR for color images

# Convert image to float
image_float = img_as_float(image)

# Apply Wavelet Denoising
wavelet_denoised = denoise_wavelet(
    image_float,
    method='BayesShrink',  # or 'VisuShrink'
    mode='soft',           # or 'hard'
    rescale_sigma=True     # Ensures correct handling of noisy images
)
# Convert back to uint8
wavelet_denoised = img_as_ubyte(wavelet_denoised)

# Display the result
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(wavelet_denoised, cmap='gray'), plt.title('Wavelet Denoising')
plt.show()