import cv2

from denoising.denoising_techniques.py import nonlocal_means_denoising, bilateral_filtering, wavelet_transform

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