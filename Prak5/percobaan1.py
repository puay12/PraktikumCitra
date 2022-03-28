import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('sundae.jpg', 0)
img1 = np.abs(img - 30.)
img1 = np.uint8(img1)
img2 = img + 30.
img2 = np.uint8(img2)

plt.subplot(131)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image")
plt.subplot(132)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title("Brigtness -30")
plt.subplot(133)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title("Brigtness +30")
plt.show()