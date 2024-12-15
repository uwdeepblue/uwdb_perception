import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.restoration import denoise_wavelet
from skimage import img_as_float, img_as_ubyte

def nonlocal_means_denoising(image):
    # Apply Non-Local Means Denoising
    denoised_image = cv2.fastNlMeansDenoising(image, None, h=10, templateWindowSize=7, searchWindowSize=21)

    # Display the result
    plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(denoised_image, cmap='gray'), plt.title('Denoised')
    plt.show()

def bilateral_filtering(image):
    # Apply Bilateral Filtering
    bilateral_filtered = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

    # Display the result
    plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(bilateral_filtered, cmap='gray'), plt.title('Bilateral Filter')
    plt.show()

def wavelet_transform(image):
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

if __name__ == "__main__":
    # Load image
    image = cv2.imread("images/noisy_butterfly.jpg", cv2.IMREAD_GRAYSCALE)  # Use IMREAD_COLOR for color images
    print("Select denoising technique: ")
    print("1. Non-Local Means Denoising")
    print("2. Bilateral Filtering")
    print("3. Wavelet Transform")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        nonlocal_means_denoising(image)
    elif choice == '2':
        bilateral_filtering(image)
    elif choice == '3':
        wavelet_transform(image)
    else:
        print("Invalid choice")