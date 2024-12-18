import cv2
import numpy as np
from matplotlib import pyplot as plt
from denoising.denoising_techniques.py import nonlocal_means_denoising, bilateral_filtering, wavelet_transform

if __name__ == "__main__":
    # Take user input for which image to use
    image_path = input("Enter image path: ")
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Use IMREAD_COLOR for color images

    # Take user input for which denoising technique to use
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
    
    # Load in the new version of the image

    # Take user input for which openCV classifier to use

    # Save final image and results for later comparison