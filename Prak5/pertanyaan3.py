import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('sundae.jpg', 0)
img1 = 128 - img
img1 = np.uint8(img1)
img2 = 255 - img
img2 = np.uint8(img2)

plt.subplot(221)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image")
plt.subplot(222)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title("Invers (128)")
plt.subplot(223)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title("Invers (255)")
plt.show()